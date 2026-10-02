"""Finite executable semantics for OneLogic."""
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

def bridge_valid(live: Iterable[World], premise: Query, premise_value: object, conclusion: Query, conclusion_value: object) -> bool:
    k = normalize_live(live)
    relevant = [w for w in k if premise.value(w) == premise_value]
    return bool(relevant) and all(conclusion.value(w) == conclusion_value for w in relevant)

def query_signature(world: World, queries: Sequence[Query]) -> Tuple[object, ...]:
    return tuple(q.value(world) for q in queries)

def query_quotient(worlds: Iterable[World], queries: Sequence[Query]) -> Tuple[FrozenSet[World], ...]:
    buckets: dict[Tuple[object, ...], set[World]] = {}
    for w in worlds:
        buckets.setdefault(query_signature(w, queries), set()).add(w)
    return tuple(frozenset(v) for v in buckets.values())

def representation_preserves_queries(worlds: Iterable[World], queries: Sequence[Query], representation: Mapping[World, Hashable]) -> bool:
    ws = tuple(worlds)
    for i, a in enumerate(ws):
        for b in ws[i+1:]:
            if representation[a] == representation[b] and query_signature(a, queries) != query_signature(b, queries):
                return False
    return True

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
