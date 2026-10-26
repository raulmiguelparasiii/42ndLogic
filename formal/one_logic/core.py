"""Finite executable semantics for OneLogic.

OneLogic starts from one actual history and reasons over the finite represented
completions that remain compatible with what has transpired.  Its strict layer
preserves the original result: categorical truth is invariance across the
still-live completions.  Its mature-judgment layer adds material closure,
defeasible support, provenance, inquiry/action frontiers, and generic
relational-deviation diagnostics.

Named fallacies are not primitives here.  They are signatures of more general
failures such as a defective premise-to-conclusion bridge, representational
loss, unsupported exclusion/retention, or failure to integrate available
material correction.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple

World = Hashable
Outcome = Hashable


class _Undefined:
    def __repr__(self) -> str:
        return "UNDEFINED"


UNDEFINED = _Undefined()


@dataclass(frozen=True)
class ActualHistory:
    """A finite projection of reality as it has transpired.

    states[0] is the initial represented actual state.  Each event advances to
    the next actual state, so len(states) == len(events) + 1.
    """

    states: Tuple[Hashable, ...]
    events: Tuple[Hashable, ...] = ()

    def __post_init__(self) -> None:
        if len(self.states) != len(self.events) + 1:
            raise ValueError("actual history requires one more state than event")

    @property
    def current(self) -> Hashable:
        return self.states[-1]


def append_actual_history(history: ActualHistory, event: Hashable, state: Hashable) -> ActualHistory:
    return ActualHistory(history.states + (state,), history.events + (event,))


@dataclass(frozen=True)
class Query:
    name: str
    values: Mapping[World, object]

    def value(self, world: World) -> object:
        return self.values.get(world, UNDEFINED)


@dataclass(frozen=True)
class Assertion:
    query: str
    value: object


@dataclass(frozen=True)
class Transition:
    before: World
    outcome: Outcome
    after: World


@dataclass(frozen=True)
class Deviation:
    unsupported_exclusion: FrozenSet[Hashable]
    unsupported_retention: FrozenSet[Hashable]

    @property
    def exact(self) -> bool:
        return not self.unsupported_exclusion and not self.unsupported_retention


@dataclass(frozen=True)
class BridgeDeviation:
    """Defect of a proposed relation A=a -> B=b over the live state.

    counterexamples satisfy the premise but contradict the proposed
    conclusion. undefined_conclusion satisfies the premise while B is not
    defined.  Either blocks categorical closure.
    """

    premise_worlds: FrozenSet[World]
    counterexamples: FrozenSet[World]
    undefined_conclusion: FrozenSet[World]

    @property
    def defect_worlds(self) -> FrozenSet[World]:
        return self.counterexamples | self.undefined_conclusion

    @property
    def categorical(self) -> bool:
        return bool(self.premise_worlds) and not self.defect_worlds


@dataclass(frozen=True)
class MaterialLoss:
    """One materially required distinction erased by a representation."""

    left: World
    right: World
    query: str


@dataclass(frozen=True)
class CorrectionOpportunity:
    """A generic material correction that may revise dependent judgment."""

    id: Hashable
    distinction: Hashable
    available: bool = True
    admissible: bool = True
    material: bool = True
    integrated: bool = False


@dataclass(frozen=True)
class DeviationSignature:
    """Set-valued distance from the currently warranted relational state.

    The components remain separate because they need not share a warranted
    common scale.  A domain may add explicit measures later; OneLogic does not
    invent weights merely to produce one score.
    """

    unsupported_exclusion: FrozenSet[Hashable] = frozenset()
    unsupported_retention: FrozenSet[Hashable] = frozenset()
    bridge_defects: FrozenSet[Hashable] = frozenset()
    material_losses: FrozenSet[Hashable] = frozenset()
    correction_debt: FrozenSet[Hashable] = frozenset()

    @property
    def exact(self) -> bool:
        return not (
            self.unsupported_exclusion
            or self.unsupported_retention
            or self.bridge_defects
            or self.material_losses
            or self.correction_debt
        )

    def finite_count_vector(self) -> Tuple[int, int, int, int, int]:
        """Finite diagnostic only; counts are not a universal moral utility."""
        return (
            len(self.unsupported_exclusion),
            len(self.unsupported_retention),
            len(self.bridge_defects),
            len(self.material_losses),
            len(self.correction_debt),
        )


@dataclass(frozen=True)
class SupportOrder:
    """Defeasible ordinal support over live possibilities.

    Larger values mean greater current support. These values are not truth
    values and are not required to be probabilities. They are supplied by a
    warranted evidence model outside strict consequence.
    """

    values: Mapping[World, float]

    def value(self, world: World) -> float:
        return float(self.values.get(world, 0.0))


@dataclass(frozen=True)
class Judgment:
    """Current status of one query relative to one live state."""

    status: str  # forced | provisional | open | undefined | model_failure
    assertion: Assertion | None
    maximal_worlds: FrozenSet[World]
    live_values: FrozenSet[object]


@dataclass(frozen=True)
class EvidenceRecord:
    """Minimal provenance record.

    roots are causally/informationally independent ancestry identifiers.
    Repetition or retransmission with the same roots does not create another
    independent ancestry unit.
    """

    id: Hashable
    roots: FrozenSet[Hashable]


@dataclass(frozen=True)
class InquiryProfile:
    """One available reality-contact route.

    resolves names material distinctions the inquiry can discriminate.
    costs is a vector rather than a scalar utility. admissible may encode
    safety, access, duty, or other externally grounded constraints.
    """

    inquiry: Hashable
    resolves: FrozenSet[Hashable]
    costs: Mapping[Hashable, float]
    available: bool = True
    admissible: bool = True


@dataclass(frozen=True)
class ResponseProfile:
    """Material residue left by a candidate response."""

    response: Hashable
    unresolved_pressures: FrozenSet[Hashable]
    correction_open: bool = True


def normalize_live(live: Iterable[World]) -> FrozenSet[World]:
    return frozenset(live)


def sound(actual: World, live: Iterable[World]) -> bool:
    return actual in normalize_live(live)


def categorical_consequences(live: Iterable[World], queries: Sequence[Query]) -> FrozenSet[Assertion]:
    k = normalize_live(live)
    if not k:
        return frozenset()
    out: set[Assertion] = set()
    for q in queries:
        vals = [q.value(w) for w in k]
        if any(v is UNDEFINED for v in vals):
            continue
        first = vals[0]
        if all(v == first for v in vals[1:]):
            out.add(Assertion(q.name, first))
    return frozenset(out)


def assertion_true_in(assertion: Assertion, world: World, query_by_name: Mapping[str, Query]) -> bool:
    v = query_by_name[assertion.query].value(world)
    return v is not UNDEFINED and v == assertion.value


def assertion_sound_over(assertion: Assertion, live: Iterable[World], query_by_name: Mapping[str, Query]) -> bool:
    k = normalize_live(live)
    return bool(k) and all(assertion_true_in(assertion, w, query_by_name) for w in k)


def sharp_update(live: Iterable[World], outcome: Outcome, transitions: Iterable[Transition]) -> FrozenSet[World]:
    k = normalize_live(live)
    return frozenset(t.after for t in transitions if t.before in k and t.outcome == outcome)


def update_is_sound(live: Iterable[World], outcome: Outcome, transitions: Iterable[Transition], proposed: Iterable[World]) -> bool:
    return sharp_update(live, outcome, transitions).issubset(normalize_live(proposed))


def deviation_from_ideal(ideal: Iterable[Hashable], proposed: Iterable[Hashable]) -> Deviation:
    i, p = frozenset(ideal), frozenset(proposed)
    return Deviation(i - p, p - i)


def weakly_dominates(ideal: Iterable[Hashable], a: Iterable[Hashable], b: Iterable[Hashable]) -> bool:
    da, db = deviation_from_ideal(ideal, a), deviation_from_ideal(ideal, b)
    return da.unsupported_exclusion.issubset(db.unsupported_exclusion) and da.unsupported_retention.issubset(db.unsupported_retention)


def strictly_dominates(ideal: Iterable[Hashable], a: Iterable[Hashable], b: Iterable[Hashable]) -> bool:
    da, db = deviation_from_ideal(ideal, a), deviation_from_ideal(ideal, b)
    return weakly_dominates(ideal, a, b) and (
        da.unsupported_exclusion != db.unsupported_exclusion or
        da.unsupported_retention != db.unsupported_retention
    )


def inference_deviation(live: Iterable[World], queries: Sequence[Query], asserted: Iterable[Assertion]) -> Deviation:
    return deviation_from_ideal(categorical_consequences(live, queries), asserted)


def bridge_deviation(
    live: Iterable[World],
    premise: Query,
    premise_value: object,
    conclusion: Query,
    conclusion_value: object,
) -> BridgeDeviation:
    """Return the exact live defect set of a proposed categorical bridge."""
    k = normalize_live(live)
    premise_worlds = frozenset(w for w in k if premise.value(w) == premise_value)
    undefined = frozenset(w for w in premise_worlds if conclusion.value(w) is UNDEFINED)
    counterexamples = frozenset(
        w for w in premise_worlds
        if conclusion.value(w) is not UNDEFINED and conclusion.value(w) != conclusion_value
    )
    return BridgeDeviation(premise_worlds, counterexamples, undefined)


def bridge_valid(live: Iterable[World], premise: Query, premise_value: object, conclusion: Query, conclusion_value: object) -> bool:
    return bridge_deviation(live, premise, premise_value, conclusion, conclusion_value).categorical


def bridge_deviation_magnitude(
    deviation: BridgeDeviation,
    weights: Mapping[World, float],
) -> float | None:
    """Optional measured bridge defect under an explicitly supplied measure.

    OneLogic does not infer these weights.  With all premise worlds assigned
    equal positive weight this becomes the finite counterexample fraction.
    """
    if not deviation.premise_worlds:
        return None
    denominator = sum(max(0.0, float(weights.get(w, 0.0))) for w in deviation.premise_worlds)
    if denominator <= 0.0:
        return None
    numerator = sum(max(0.0, float(weights.get(w, 0.0))) for w in deviation.defect_worlds)
    return numerator / denominator


def query_signature(world: World, queries: Sequence[Query]) -> Tuple[object, ...]:
    return tuple(q.value(world) for q in queries)


def query_quotient(worlds: Iterable[World], queries: Sequence[Query]) -> Tuple[FrozenSet[World], ...]:
    buckets: dict[Tuple[object, ...], set[World]] = {}
    for w in worlds:
        buckets.setdefault(query_signature(w, queries), set()).add(w)
    return tuple(frozenset(v) for v in buckets.values())


def material_representation_losses(
    worlds: Iterable[World],
    material_queries: Sequence[Query],
    representation: Mapping[World, Hashable],
) -> FrozenSet[MaterialLoss]:
    """Return every material distinction erased by the representation."""
    ws = tuple(worlds)
    losses: set[MaterialLoss] = set()
    for i, a in enumerate(ws):
        for b in ws[i + 1:]:
            if representation[a] != representation[b]:
                continue
            for q in material_queries:
                if q.value(a) != q.value(b):
                    losses.add(MaterialLoss(a, b, q.name))
    return frozenset(losses)


def representation_preserves_queries(worlds: Iterable[World], queries: Sequence[Query], representation: Mapping[World, Hashable]) -> bool:
    return not material_representation_losses(worlds, queries, representation)


def representation_preserves_material_distinctions(
    worlds: Iterable[World],
    material_queries: Sequence[Query],
    representation: Mapping[World, Hashable],
) -> bool:
    """Adequacy relative to the referent's materially required query family."""
    return not material_representation_losses(worlds, material_queries, representation)


def pooled(*live_sets: Iterable[World]) -> FrozenSet[World]:
    sets = [normalize_live(x) for x in live_sets]
    if not sets:
        return frozenset()
    out = set(sets[0])
    for s in sets[1:]:
        out.intersection_update(s)
    return frozenset(out)


def needs_ontology_expansion(actual: World, model_class: Iterable[World]) -> bool:
    return actual not in frozenset(model_class)


def maximally_supported(live: Iterable[World], support: SupportOrder) -> FrozenSet[World]:
    """Return support-maximal live possibilities without eliminating any."""
    k = normalize_live(live)
    if not k:
        return frozenset()
    maximum = max(support.value(w) for w in k)
    return frozenset(w for w in k if support.value(w) == maximum)


def provisional_consequences(
    live: Iterable[World],
    queries: Sequence[Query],
    support: SupportOrder,
) -> FrozenSet[Assertion]:
    """Assertions shared by all support-maximal worlds but not forced by K."""
    k = normalize_live(live)
    top = maximally_supported(k, support)
    if not top:
        return frozenset()
    forced = categorical_consequences(k, queries)
    out: set[Assertion] = set()
    for q in queries:
        vals = [q.value(w) for w in top]
        if not vals or any(v is UNDEFINED for v in vals):
            continue
        first = vals[0]
        candidate = Assertion(q.name, first)
        if all(v == first for v in vals[1:]) and candidate not in forced:
            out.add(candidate)
    return frozenset(out)


def judge_query(live: Iterable[World], query: Query, support: SupportOrder | None = None) -> Judgment:
    """Return the strongest status warranted by the present live state."""
    k = normalize_live(live)
    if not k:
        return Judgment("model_failure", None, frozenset(), frozenset())

    values = [query.value(w) for w in k]
    defined_values = frozenset(v for v in values if v is not UNDEFINED)
    if all(v is UNDEFINED for v in values):
        return Judgment("undefined", None, frozenset(k), frozenset())

    forced = categorical_consequences(k, [query])
    if forced:
        assertion = next(iter(forced))
        return Judgment("forced", assertion, frozenset(k), defined_values)

    if support is not None:
        top = maximally_supported(k, support)
        provisional = provisional_consequences(k, [query], support)
        if provisional:
            return Judgment("provisional", next(iter(provisional)), top, defined_values)
        return Judgment("open", None, top, defined_values)

    return Judgment("open", None, frozenset(k), defined_values)


def robust_categorical_consequence(
    live_states: Sequence[Iterable[World]],
    query: Query,
) -> Assertion | None:
    """Categorical consequence that survives every admissible live encoding."""
    if not live_states:
        return None
    common: Assertion | None = None
    for live in live_states:
        forced = categorical_consequences(live, [query])
        if len(forced) != 1:
            return None
        current = next(iter(forced))
        if common is None:
            common = current
        elif common != current:
            return None
    return common


def independent_ancestry_roots(records: Iterable[EvidenceRecord]) -> FrozenSet[Hashable]:
    """Return evidential ancestry units, not transmissions or repetitions."""
    roots: set[Hashable] = set()
    for record in records:
        roots.update(record.roots)
    return frozenset(roots)


def correction_debt(corrections: Iterable[CorrectionOpportunity]) -> FrozenSet[Hashable]:
    """Material available corrections not integrated before dependent closure."""
    return frozenset(
        c.id for c in corrections
        if c.available and c.admissible and c.material and not c.integrated
    )


def deviation_signature(
    *,
    ideal: Iterable[Hashable] = (),
    proposed: Iterable[Hashable] = (),
    bridges: Iterable[BridgeDeviation] = (),
    material_losses: Iterable[MaterialLoss] = (),
    corrections: Iterable[CorrectionOpportunity] = (),
) -> DeviationSignature:
    """Compose generic relational defects without naming a surface phenomenon."""
    state = deviation_from_ideal(ideal, proposed)
    bridge_ids: set[Hashable] = set()
    for i, bridge in enumerate(bridges):
        for world in bridge.defect_worlds:
            bridge_ids.add((i, world))
    material_ids = frozenset((loss.left, loss.right, loss.query) for loss in material_losses)
    return DeviationSignature(
        unsupported_exclusion=state.unsupported_exclusion,
        unsupported_retention=state.unsupported_retention,
        bridge_defects=frozenset(bridge_ids),
        material_losses=material_ids,
        correction_debt=correction_debt(corrections),
    )


def _cost_no_greater(a: Mapping[Hashable, float], b: Mapping[Hashable, float]) -> bool:
    keys = set(a) | set(b)
    return all(float(a.get(k, 0.0)) <= float(b.get(k, 0.0)) for k in keys)


def _cost_strictly_lower(a: Mapping[Hashable, float], b: Mapping[Hashable, float]) -> bool:
    keys = set(a) | set(b)
    return any(float(a.get(k, 0.0)) < float(b.get(k, 0.0)) for k in keys)


def inquiry_dominates(a: InquiryProfile, b: InquiryProfile, unresolved: Iterable[Hashable]) -> bool:
    """Pareto dominance over material discrimination and burden."""
    u = frozenset(unresolved)
    gain_a = a.resolves & u
    gain_b = b.resolves & u
    if not gain_a.issuperset(gain_b):
        return False
    if not _cost_no_greater(a.costs, b.costs):
        return False
    return gain_a != gain_b or _cost_strictly_lower(a.costs, b.costs)


def proportionate_inquiry_frontier(
    inquiries: Sequence[InquiryProfile],
    unresolved: Iterable[Hashable],
) -> Tuple[InquiryProfile, ...]:
    """Available admissible inquiries with positive material gain and no dominator."""
    u = frozenset(unresolved)
    candidates = [
        i for i in inquiries
        if i.available and i.admissible and bool(i.resolves & u)
    ]
    frontier = [
        i for i in candidates
        if not any(j is not i and inquiry_dominates(j, i, u) for j in candidates)
    ]
    return tuple(frontier)


def response_dominates(a: ResponseProfile, b: ResponseProfile) -> bool:
    """Stone-style non-loss plus correction of at least one unresolved pressure."""
    return a.correction_open and a.unresolved_pressures < b.unresolved_pressures


def mature_response_frontier(responses: Sequence[ResponseProfile]) -> Tuple[ResponseProfile, ...]:
    """Correction-open nondominated responses, preserving tragic residue explicitly."""
    candidates = [r for r in responses if r.correction_open]
    frontier = [
        r for r in candidates
        if not any(other is not r and response_dominates(other, r) for other in candidates)
    ]
    return tuple(frontier)
