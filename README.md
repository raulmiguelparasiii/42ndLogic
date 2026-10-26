# 42ndLogic

42ndLogic is the public foundation repository for **OneLogic**, a falsifiable first-principles reality-tracking logic for strict inference, mature judgment, inquiry, correction, representation, and machine reasoning.

The current core is:

> Ground what reality has actually done. Preserve every distinction that can still change mature judgment. Infer every conclusion reality warrants and no stronger one. Measure relational deviation where a justified measure exists. Seek discriminating reality when it can improve judgment. Act on consequence without laundering uncertainty into fact. When reality changes, let the dependent structure change with it.

This repository contains:

- `paper/` — the canonical OneLogic paper in Markdown and LaTeX.
- `formal/` — executable semantics, theorem obligations, the compact mature-judgment formulation, proofs, and bounded falsification work.
- `solver/` — a small provider-agnostic demonstrator.
- `docs/` — a minimal public site.

## One actual history

OneLogic begins with one actual time-indexed history:

```text
H_t = <omega_0, e_1, omega_1, ..., e_t, omega_t>.
```

Grounded relational structure is

```text
G_t = Ground(H_t).
```

The represented live set contains unresolved completions compatible with that grounded history; it is not a substitute for actuality.

For referent `r`:

```text
One(H_t,r)
 = <G_t, Qmat_t(r), K_t(r), >=_t, I_t, A_t, T_t, D_t>.
```

`Qmat_t(r)` is material closure, `K_t(r)` the live completion set, `>=_t` defeasible support, `I_t` inquiry, `A_t` response, `T_t` transition, and `D_t` relational deviation.

## Strict and provisional judgment

For query `q`:

```text
K |= (q=v)
iff
K is nonempty and every live completion defines q=v.
```

That remains the categorical rule.

OneLogic also permits a warranted support ordering. Claims shared by all support-maximal live completions but not by the whole live set are provisionally favored rather than settled.

The target is the strongest warranted judgment, not uncertainty for its own sake.

## General relational law

For a proposed bridge

```text
A=a -> B=b
```

define

```text
D_B
 = {m in K[A=a] : B(m) is undefined or B(m) != b}.
```

The categorical bridge is valid exactly when the premise region is nonempty and `D_B` is empty.

This single law generates many cases that older IEL prose handled separately: assumed ignorance, motive attribution, omission-as-denial, guilt-by-precaution, coordination-from-agreement, and others.

If an independently warranted measure exists, bridge deviation may also receive a magnitude. OneLogic does not invent weights merely to obtain a score.

## Material relevance and affected welfare

The Philosopher's Stone constrains material closure. OneLogic must preserve distinctions whose loss can change mature judgment through:

```text
informational grounding
contextual interpretation
real-world constraint
affected welfare
consequence
correction / answerability.
```

For representation `h`:

```text
D_M(h,r)
 = {(m,n,q) : h(m)=h(n), q in Qmat_t(r), q(m) != q(n)}.
```

Material adequacy requires `D_M` empty.

Affected welfare therefore enters as a materially governing reality distinction rather than an emotional simulation or scalar reward.

## Relational deviation

For independently warranted state `W` and proposed state `M`:

```text
E-(W,M) = W \ M
E+(W,M) = M \ W.
```

Let `D_C` be material available admissible corrections that were not integrated before dependent judgment was reused or closed.

The canonical deviation signature is:

```text
D_t = <E-, E+, D_B, D_M, D_C>.
```

Named fallacies and debate phenomena are diagnostic labels for recurring signatures, not formal primitives.

For example, an opponent's caricature can be represented as unsupported exclusion/retention relative to the warranted model of the speaker's position. If targeted clarification remains unintegrated and the same deviating model generates the next inference, the result is a recursive frame lock. Consecutive persistence can be tracked by `rho`.

## Provenance, inquiry, and response

Evidence plurality is causal-informational plurality, not repetition count. Source history may alter provisional support while remaining defeasible.

When material unresolved structure remains, OneLogic compares available inquiries by material discrimination and burden. If no proportionate inquiry is warranted, categorical closure is withheld.

Action may still be warranted under unresolved belief when consequence makes a response nondominated. Tragic residue remains explicit when no clean response exists.

## Stone, ULT, and IEL

The current division is:

```text
ULT-style grounding
    -> how reality becomes anonymous relational structure

Philosopher's Stone
    -> which materially relevant reality must retain governing force

OneLogic
    -> what judgment, inquiry, response, and correction that grounded reality warrants.
```

IEL is retained as a discovery history. Its useful cases are compressed into grounding/provenance, support, bridge validity, state deviation, material loss, correction debt, inquiry, response dominance, and recursive correction.

See `formal/MATURE_JUDGMENT.md` for the compact formal map and `paper/one_logic.md` for the full formulation.

## Formal status

The repository currently has executable finite semantics for the original strict core and bounded mature-judgment mechanisms including:

- forced versus provisional judgment;
- material-distinction preservation;
- robust categorical consequence across encodings;
- provenance ancestry;
- generic bridge deviation;
- measured bridge deviation under explicitly supplied weights;
- correction debt;
- set-valued relational deviation signatures;
- nondominated inquiry;
- correction-open response frontiers and tragic residue.

`formal/THEOREMS.md` distinguishes theorem obligations from generally proved results. `Ground(H_t)` remains an interface; unrestricted perception, semantics, and AGI are not assumed solved.

## Falsifiability

OneLogic must be revised if a material phenomenon requires a genuinely new primitive that cannot be represented through actual history, grounding, material closure, live completion, support, bridge validity, deviation, inquiry/action, and recursive correction, or if a counterexample defeats one of the formal obligations.

OneLogic receives no exemption from its own correction rule.

## License

No license has been selected yet. All rights remain with the repository owner until a license is added.
