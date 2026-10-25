# 42ndLogic project memory

Read this file before changing the project.

## Purpose

42ndLogic is the public foundation repository for OneLogic: a falsifiable reality-tracking logic for strict inference, mature judgment, inquiry, correction, representation, and machine reasoning.

The current target is one reality-relative judgment calculus, not a stack of separate modules for truth, empathy, testimony, morality, communication, or action.

## Public/private boundary

This repository is intentionally limited to the public foundation:

- paper and explanatory material;
- formal definitions, proofs, and falsification work;
- a small provider-agnostic solver demonstrator;
- stable public interfaces needed to understand or test the architecture.

Do not add production revenue machinery, live opportunity discovery, target-selection policy, provider prompts, accumulated failure traces, platform-specific claim/submission behavior, private experiment data, or operational strategies whose value depends on keeping the execution advantage private.

## Core invariants

- There is one actual structured reality.
- A finite reasoner works with a corrigible represented possibility space.
- A live state `K` contains the possibilities not yet defeated by warranted information.
- Strict categorical assertion is permitted only when the query is invariant across nonempty `K`.
- A defeasible support ordering may rank live possibilities, but support alone may not delete a live possibility or manufacture categorical truth.
- `provisionally favored` and `settled` are distinct statuses.
- Reality-contact updates must retain every modeled successor compatible with the actual outcome and eliminate every modeled successor the outcome defeats.
- If actuality is excluded, contraction alone cannot repair the state.
- If actuality is outside the model class, the model class must expand or be replaced.
- Undefined is not false.
- A representation is adequate only relative to the materially required distinctions of the referent, not merely an arbitrarily admitted surface query family.
- The current Stone-grounded material closure preserves distinctions whose loss can alter mature judgment through informational grounding, contextual interpretation, real-world constraint, affected welfare, consequence, or correction.
- Affected welfare enters OneLogic as a materially required distinction where reality makes it relevant. Do not turn empathy into a scalar reward or a separate hidden module.
- Evidence plurality is causal-informational plurality. Repetition or retransmission without new ancestry does not become independent corroboration.
- Source standing may alter provisional support but does not determine truth. Previously earned standing persists defeasibly until counterevidence, domain transfer, correction failure, decay, or another material defeater changes it.
- Consideration, belief, action, precaution, expression, commitment, source reliability, claim truth, memory sincerity, historical truth, visible correction, and latent policy remain distinct unless a warranted bridge connects them.
- Material uncertainty should lead to a proportionate discriminating inquiry when one exists, otherwise correction-open suspension. Declining inquiry creates no evidence.
- Action may occur under unresolved belief when consequence makes precaution or another nondominated response warranted. Action does not retroactively settle the proposition.
- Mature response is the correction-open nondominated frontier over unresolved material pressures. Genuine tragic residue remains explicit rather than being hidden by a forced scalar optimum.
- Robust categorical settlement must survive all materially adequate nondominated encodings of the accessible record.
- Named fallacies and interpersonal failure labels are surface descriptions. The formal layer should derive them from unsupported exclusion/retention, invalid bridges, representational loss, bad inquiry, dependence inflation, premature closure, or failed correction.
- OneLogic itself receives no privileged status. Model inadequacy, reopening, and revision remain legal outputs.

## Current mature-judgment formulation

The canonical formal overview is `formal/MATURE_JUDGMENT.md`.

The unified state is approximately:

```text
J_t(r) = <Omega_t, K_t, G_t, >=_t, Qmat(r), I_t, A_t, T_t>
```

where:

- `Omega_t` is the represented possibility class;
- `K_t` is the still-live set;
- `G_t` is causal-informational provenance;
- `>=_t` is defeasible support;
- `Qmat(r)` is the materially required query family;
- `I_t` is available inquiry;
- `A_t` is feasible response;
- `T_t` is world transition.

These are fields of one judgment state, not independent authorities.

`paper/one_logic.md` is the current narrative formulation. `formal/THEOREMS.md` records exact theorem obligations and must distinguish proved gates from unproved obligations.

## Relation to the old IEL work

Interpersonal Epistemic Logic is a discovery source, not a second live logic beside OneLogic.

Useful IEL structure should be absorbed through the smallest existing OneLogic machinery:

- provenance/dependence -> `G_t`;
- source weighting/continuity -> defeasible support;
- source-truth non-identity -> strict consequence remains independent of source status;
- consideration/belief/action separation -> distinct projections of one judgment state;
- provisional assumption -> support-maximal but non-forced judgment;
- mature suspension -> open judgment with no proportionate inquiry;
- clarification/inquiry value -> inquiry frontier;
- adverse interpretation control -> encoding robustness + no premature closure;
- precaution without guilt -> action/belief separation;
- correction supremacy -> reality-contact revises every defeated component;
- recursive relevance -> preserve higher-order structure only while materially distinguishing;
- tragic choice -> nondominated response frontier with explicit residue;
- anti-self-sealing -> model inadequacy remains available.

Do not reintroduce these as separate named modules if they are derivable from the unified state.

## Engineering rules

- Keep the semantic core small.
- Treat LLMs as candidate generators, not truth authorities.
- External tests, observations, proof checkers, compilers, experiments, and validated data are reality-contact adapters.
- Do not claim a bounded search is a universal proof.
- Do not claim a formal proof establishes that the formal assumptions exhaust reality.
- Preserve explicit falsification criteria.
- Avoid adding a primitive when the same behavior is derivable from the current core.
- Keep strict truth, defeasible support, inquiry burden, and response dominance distinct even though they live in one state.
- Prefer partial orders and nondominated frontiers over invented scalar utilities when heterogeneous material pressures have no warranted common scale.
- Keep public examples minimal and reproducible.
- Never commit credentials, API keys, bank details, identity documents, or private contact information.
