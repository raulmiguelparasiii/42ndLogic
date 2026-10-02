"""Bounded countermodel attacks for OneLogic."""
from __future__ import annotations
import itertools
from dataclasses import dataclass
from typing import Iterable
from .core import *

@dataclass
class Report:
    checks: int = 0
    failures: list[str] | None = None
    def __post_init__(self):
        if self.failures is None:
            self.failures = []
    def ok(self, cond: bool, label: str):
        self.checks += 1
        if not cond:
            self.failures.append(label)

def subsets(items: tuple[int, ...]) -> Iterable[frozenset[int]]:
    for mask in range(1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if mask & (1 << i))

def nonempty_subsets(items: tuple[int, ...]):
    for s in subsets(items):
        if s:
            yield s

def query_maps(worlds: tuple[int, ...]):
    for assignment in itertools.product((0, 1, UNDEFINED), repeat=len(worlds)):
        yield Query("q", dict(zip(worlds, assignment)))

def run(max_worlds: int = 4) -> Report:
    r = Report()
    for n in range(1, max_worlds + 1):
        worlds = tuple(range(n))
        all_sets = list(subsets(worlds))

        for ideal in all_sets:
            r.ok(deviation_from_ideal(ideal, ideal).exact, f"ideal self-deviation n={n}")
            for candidate in all_sets:
                r.ok(weakly_dominates(ideal, ideal, candidate), f"ideal weak dominance n={n}")
                r.ok(strictly_dominates(ideal, ideal, candidate) == (ideal != candidate), f"ideal strict dominance n={n}")

        for k in nonempty_subsets(worlds):
            for q in query_maps(worlds):
                qmap = {"q": q}
                c = categorical_consequences(k, [q])
                for a in (Assertion("q", 0), Assertion("q", 1)):
                    r.ok((a in c) == assertion_sound_over(a, k, qmap), f"categorical mismatch n={n}")

        for actual in worlds:
            containing = [k for k in nonempty_subsets(worlds) if actual in k]
            for a in containing:
                for b in containing:
                    r.ok(actual in pooled(a, b), f"sound pooling lost actuality n={n}")

    # Exhaust every two-world transition relation.
    worlds = (0, 1)
    outcomes = (0, 1)
    triples = [Transition(a, o, b) for a in worlds for o in outcomes for b in worlds]
    for mask in range(1 << len(triples)):
        relation = [triples[i] for i in range(len(triples)) if mask & (1 << i)]
        for k in nonempty_subsets(worlds):
            for outcome in outcomes:
                star = sharp_update(k, outcome, relation)
                for proposed in subsets(worlds):
                    r.ok(update_is_sound(k, outcome, relation, proposed) == star.issubset(proposed), "sharp-update mismatch")

    return r

if __name__ == "__main__":
    report = run()
    print(f"checks={report.checks}")
    print(f"failures={len(report.failures)}")
    for failure in report.failures[:20]:
        print("FAIL", failure)
    raise SystemExit(1 if report.failures else 0)
