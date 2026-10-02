"""A small, provider-agnostic OneLogic reasoning controller.

The controller does not generate language. It tracks live candidate worlds, selects
discriminating inquiries, receives actual outcomes from an oracle/reality-contact
adapter, and performs exact compatibility updates.

External models may implement CandidateGenerator. They are proposal mechanisms only.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import log2
from typing import Callable, Hashable, Iterable, Mapping, Protocol, Sequence

UNKNOWN = object()


@dataclass(frozen=True)
class Candidate:
    id: str
    answer: Hashable
    predictions: Mapping[str, Hashable]
    payload: object | None = None

    def predict(self, inquiry_id: str):
        return self.predictions.get(inquiry_id, UNKNOWN)


@dataclass(frozen=True)
class Inquiry:
    id: str
    cost: float = 1.0
    metadata: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class Observation:
    inquiry_id: str
    outcome: Hashable


@dataclass
class Trace:
    problem: str
    observations: list[Observation] = field(default_factory=list)
    live_history: list[tuple[str, ...]] = field(default_factory=list)
    expansions: int = 0


@dataclass(frozen=True)
class SolveResult:
    status: str
    answer: Hashable | None
    live_candidate_ids: tuple[str, ...]
    trace: Trace


class CandidateGenerator(Protocol):
    def generate(
        self,
        problem: str,
        trace: Trace,
        previous: Sequence[Candidate],
    ) -> Sequence[Candidate]:
        ...


class RealityContact(Protocol):
    def observe(self, inquiry: Inquiry) -> Hashable:
        ...


def exact_update(
    live: Sequence[Candidate],
    inquiry: Inquiry,
    outcome: Hashable,
) -> list[Candidate]:
    """Retain every candidate not defeated by the observed outcome.

    A candidate that did not define a prediction for this inquiry is not eliminated:
    undefined is not false.
    """
    survivors: list[Candidate] = []
    for candidate in live:
        prediction = candidate.predict(inquiry.id)
        if prediction is UNKNOWN or prediction == outcome:
            survivors.append(candidate)
    return survivors


def forced_answer(live: Sequence[Candidate]):
    if not live:
        return UNKNOWN
    values = {candidate.answer for candidate in live}
    if len(values) == 1:
        return next(iter(values))
    return UNKNOWN


def _entropy(bucket_sizes: Iterable[int]) -> float:
    sizes = [n for n in bucket_sizes if n]
    total = sum(sizes)
    if total == 0:
        return 0.0
    return -sum((n / total) * log2(n / total) for n in sizes)


def inquiry_score(live: Sequence[Candidate], inquiry: Inquiry) -> tuple[float, float, float]:
    """Heuristic only: prefer inquiries that split defined predictions efficiently.

    The semantic core does not claim this scoring rule is universally optimal.
    """
    buckets: dict[Hashable, int] = {}
    defined = 0
    for candidate in live:
        prediction = candidate.predict(inquiry.id)
        if prediction is UNKNOWN:
            continue
        defined += 1
        buckets[prediction] = buckets.get(prediction, 0) + 1
    if len(buckets) < 2:
        return (-1.0, -1.0, -inquiry.cost)
    coverage = defined / max(1, len(live))
    return (_entropy(buckets.values()) / max(inquiry.cost, 1e-9), coverage, -inquiry.cost)


def choose_inquiry(
    live: Sequence[Candidate],
    inquiries: Sequence[Inquiry],
    used: set[str],
) -> Inquiry | None:
    available = [i for i in inquiries if i.id not in used]
    scored = [(inquiry_score(live, inquiry), inquiry) for inquiry in available]
    scored = [pair for pair in scored if pair[0][0] >= 0]
    if not scored:
        return None
    scored.sort(key=lambda pair: (pair[0], pair[1].id), reverse=True)
    return scored[0][1]


class OneLogicSolver:
    def __init__(
        self,
        generator: CandidateGenerator,
        reality: RealityContact,
        inquiries: Sequence[Inquiry],
        *,
        max_steps: int = 32,
        max_expansions: int = 3,
    ):
        self.generator = generator
        self.reality = reality
        self.inquiries = list(inquiries)
        self.max_steps = max_steps
        self.max_expansions = max_expansions

    def solve(self, problem: str) -> SolveResult:
        trace = Trace(problem=problem)
        live = list(self.generator.generate(problem, trace, []))
        used: set[str] = set()
        trace.live_history.append(tuple(c.id for c in live))

        for _ in range(self.max_steps):
            answer = forced_answer(live)
            if answer is not UNKNOWN:
                return SolveResult("forced", answer, tuple(c.id for c in live), trace)

            if not live:
                if trace.expansions >= self.max_expansions:
                    return SolveResult("model_failure", None, (), trace)
                trace.expansions += 1
                live = list(self.generator.generate(problem, trace, []))
                # Reapply all recorded observations to the expanded representation.
                for obs in trace.observations:
                    inquiry = next(i for i in self.inquiries if i.id == obs.inquiry_id)
                    live = exact_update(live, inquiry, obs.outcome)
                trace.live_history.append(tuple(c.id for c in live))
                continue

            inquiry = choose_inquiry(live, self.inquiries, used)
            if inquiry is None:
                return SolveResult(
                    "non_identifiable",
                    None,
                    tuple(c.id for c in live),
                    trace,
                )

            used.add(inquiry.id)
            outcome = self.reality.observe(inquiry)
            obs = Observation(inquiry.id, outcome)
            trace.observations.append(obs)
            live = exact_update(live, inquiry, outcome)
            trace.live_history.append(tuple(c.id for c in live))

        return SolveResult("budget_exhausted", None, tuple(c.id for c in live), trace)


class StaticGenerator:
    """Deterministic generator useful for tests and reproducible experiments."""

    def __init__(self, candidates: Sequence[Candidate]):
        self.candidates = list(candidates)

    def generate(self, problem: str, trace: Trace, previous: Sequence[Candidate]) -> Sequence[Candidate]:
        return list(self.candidates)


class TableReality:
    """Reality-contact backed by an outcome table."""

    def __init__(self, outcomes: Mapping[str, Hashable]):
        self.outcomes = dict(outcomes)

    def observe(self, inquiry: Inquiry) -> Hashable:
        if inquiry.id not in self.outcomes:
            raise KeyError(f"No actual outcome configured for inquiry {inquiry.id!r}")
        return self.outcomes[inquiry.id]
