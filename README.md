# 42ndLogic

42ndLogic is the public foundation repository for **OneLogic**, a falsifiable reality-tracking logic for strict inference, mature judgment, inquiry, correction, and machine reasoning.

The core idea is:

> Preserve every possibility reality has not defeated. Eliminate exactly what warranted reality-contact defeats. Assert categorically only what the survivors force. Give unresolved alternatives their warranted provisional weight without turning likelihood into truth. Preserve every materially governing distinction, including affected welfare, and reopen the representation whenever reality no longer fits it.

This repository contains:

- `paper/` — the OneLogic paper in Markdown and LaTeX.
- `formal/` — executable semantics, theorem obligations, mature-judgment formulation, proofs, and bounded countermodel attacks.
- `solver/` — a small provider-agnostic demonstrator of the OneLogic reasoning loop.
- `docs/` — a minimal public site suitable for GitHub Pages.

## One judgment state

The current mature formulation is organized around one reality-relative state:

```text
J_t(r) = <Omega_t, K_t, G_t, >=_t, Qmat(r), I_t, A_t, T_t>
```

where:

- `Omega_t` is the represented possibility class;
- `K_t` is the still-live set;
- `G_t` is causal-informational provenance;
- `>=_t` is defeasible comparative support;
- `Qmat(r)` is the materially required query family;
- `I_t` is available inquiry;
- `A_t` is feasible response;
- `T_t` is world transition.

These are fields of one judgment state. OneLogic does not create separate truth, empathy, testimony, morality, or action engines.

## Strict truth and provisional judgment

For a well-defined query `q`:

```text
K |= (q = v)
iff
K is nonempty and every w in K gives q(w)=v.
```

That remains the categorical truth rule.

OneLogic also allows a defeasible support ordering over the live possibilities. If all support-maximal live possibilities agree on `q=v` while another live possibility does not, the result is **provisionally favored**, not settled.

This is the main move from forced binary handling into mature judgment: uncertainty can be structured without being erased.

## Material relevance and affected welfare

The old formulation preserved distinctions relative to an admitted query family. The mature formulation requires material adequacy relative to the referent.

The current Philosopher's Stone grounding requires OneLogic to preserve distinctions whose loss can alter mature judgment through:

```text
informational grounding
contextual interpretation
real-world constraint
affected welfare
consequence
correction / answerability
```

Affected welfare therefore enters the logic as a material reality distinction wherever it can change judgment or response. It is not implemented as an emotional simulation or scalar reward.

## Inquiry, suspension, and action

When material uncertainty remains, OneLogic seeks an available admissible inquiry that gives positive discriminating gain without being dominated by another inquiry with at least as much gain and no greater burden.

If no proportionate inquiry is available, categorical judgment remains suspended.

Action can still occur under uncertainty when consequence warrants a nondominated precautionary or practical response. Acting does not settle the unresolved proposition.

For feasible response `a`, the mature response frontier preserves correction-openness and removes responses whose unresolved material-pressure set is a strict superset of another response's. If every feasible action leaves some loss, the remaining tragic residue stays explicit.

## Provenance and source continuity

Evidence plurality is causal-informational plurality, not repetition count. Copies derived from one ancestry do not become independent corroboration merely by being numerous.

Source history may rationally change provisional support. Previously earned domain-relevant standing remains defeasible evidence until a material defeater changes it. Source standing never determines truth and never defeats a live counterexample by status alone.

## Relation to IEL

The older Interpersonal Epistemic Logic is treated as a discovery source rather than a second logic. Its useful mechanisms are compressed into OneLogic's unified state: provenance, dependence, source weighting, epistemic continuity, provisional uptake, mature suspension, clarification, adverse-interpretation control, precaution without guilt, correction, recursive relevance, strategic observability, and tragic choice.

See `formal/MATURE_JUDGMENT.md` for the exact reduction.

## Formal status

The original strict OneLogic layer characterizes categorical consequence, sharp reality-contact update, correction, query-relative representation, objective deviation, and counterexample defeat.

The mature-judgment extension adds executable bounded semantics for:

- provisional versus forced judgment;
- material-distinction preservation;
- robust settlement across admissible encodings;
- independent evidential ancestry;
- nondominated inquiry;
- correction-open response frontiers and tragic residue.

`formal/THEOREMS.md` distinguishes theorem obligations from claims already machine-proved. Do not treat a new obligation as proved merely because it has been formulated or covered by examples.

## Public solver demonstrator

The public solver demonstrates the original live-candidate loop:

```text
generate -> represent -> infer -> discriminate -> observe -> update -> correct -> repeat
```

A generator may be an LLM, symbolic engine, search process, program synthesizer, or human. The generator proposes possibilities; it does not certify them.

The mature formulation extends the target controller so that unresolved alternatives can be provisionally ranked, materially important distinctions cannot be silently erased, inquiry can be selected proportionately, and action need not pretend uncertainty disappeared.

The public repository intentionally does not contain production execution strategy or operational automation.

## Falsifiability

OneLogic must be revised if a legitimate reality-tracking counterexample defeats its structure. In particular, the mature formulation is vulnerable to a demonstrated maturity-relevant relation outside the current Stone-derived closure, a categorical truth that is warranted despite a live materially adequate counterexample, or a case where the nondominance/material-relevance rules systematically discard a real governing pressure.

OneLogic receives no exemption from its own correction rule.

## License

No license has been selected yet. All rights remain with the repository owner until a license is added.
