# OneLogic Mature Judgment Calculus

This document extends the strict OneLogic foundation into one reality-relative judgment calculus. It does not create separate empathy, trust, social, moral, or communication modules. The same live-state logic governs factual inference, interpretation, testimony, interpersonal judgment, inquiry, precaution, action, and correction.

The design goal is:

> preserve strict truth where reality forces it, preserve uncertainty where reality has not resolved it, preserve material human consequence where reality makes it relevant, and allow every provisional organization to remain answerable to correction.

## 1. One reality, one judgment state

Let `Omega_t` be the represented class of complete structured possibilities at time `t`, and let `omega_t` be actuality when the representation is adequate.

For referent `r`, define the OneLogic judgment state

```text
J_t(r) = <Omega_t, K_t, G_t, >=_t, Qmat(r), I_t, A_t, T_t>
```

where:

- `K_t subseteq Omega_t` is the live possibility set: possibilities not yet defeated by warranted reality-contact;
- `G_t` is the causal-informational provenance graph of observations, records, expressions, commitments, inferences, actions, consequences, and corrections;
- `>=_t` is a defeasible support preorder over live possibilities or hypotheses;
- `Qmat(r)` is the family of distinctions materially required by the referent;
- `I_t` is the available inquiry/reality-contact set;
- `A_t` is the feasible response/action set;
- `T_t` is the represented transition structure by which inquiry and action can change the world and later evidence.

These are fields of one state. None is an independent truth authority.

## 2. Strict consequence remains strict

For a partial, possibly multi-valued query `q`, categorical consequence is unchanged:

```text
K_t |= (q = v)
iff
K_t is nonempty
and every w in K_t defines q(w) = v.
```

`UNDEFINED` remains distinct from false.

A categorical claim is settled only when every live possibility forces it. No source weight, probability, popularity, emotional intensity, institutional status, usefulness, or support score may replace this condition.

## 3. Graded support without fake truth

Human and machine judgment often has asymmetric evidence before categorical settlement. OneLogic therefore permits a defeasible support preorder `>=_t` over `K_t`.

Let

```text
Max_t = {w in K_t : no live w' is strictly better supported than w}.
```

For query `q`:

```text
Forced(q=v)
iff
all w in K_t define q(w)=v.
```

```text
ProvisionallyFavored(q=v)
iff
not Forced(q=v)
and all w in Max_t define q(w)=v.
```

If the support-maximal live possibilities disagree, judgment remains open.

The distinction is absolute:

```text
provisionally favored != settled
```

A live counterexample can coexist with a provisionally favored interpretation. Ranking changes attention, expectation, and inquiry priority. Ranking alone does not delete the counterexample.

This is the core move from binary handling to mature judgment: uncertainty can have structure without being converted into certainty.

## 4. Material relevance is not chosen arbitrarily

The old OneLogic formulation preserved distinctions relative to an admitted query family. That permits a hidden failure: the reasoner could simply omit a materially important question.

The mature formulation replaces arbitrary admission with material adequacy relative to referent `r`.

`Qmat(r)` must preserve every distinction whose loss can change the judgment through one or more of the following reality relations:

```text
informational grounding
contextual interpretation
real-world constraint
affected welfare
consequence
correction / answerability
```

These are the current Stone-grounded maturity-relevant relations. They are not six independent modules. They are tests for whether a proposed compression has removed something reality still gives governing force.

Affected welfare therefore enters OneLogic in the same formal role as any other materially necessary distinction. If two live possibilities differ in a welfare consequence that can alter mature judgment, an adequate representation may not merge them merely because the immediate factual proposition is the same.

This is the logical form of empathy:

```text
Empathy(r) = preservation and governing use of materially affected welfare in Qmat(r).
```

No emotional simulation is required for that relation to be represented correctly.

## 5. Mature representation

Let `h : Omega_t -> H` be a proposed compression or representation.

`h` is materially adequate relative to `r` only if

```text
h(w1) = h(w2)
=>
q(w1) = q(w2)
for every q in Qmat(r), including definedness.
```

A representation that merges materially distinct possibilities is inadequate even if it preserves the surface query the agent originally asked.

If no available representation can preserve a newly revealed material distinction, OneLogic must output model inadequacy and expand or replace the model class.

## 6. Encoding robustness

A record can admit more than one reasonable encoding. Mature reasoning cannot obtain certainty merely by selecting the encoding most favorable to a desired interpretation.

Let `Enc_t(r)` be the nondominated admissible encodings of the accessible record that preserve the available material distinctions.

A robust categorical claim requires the same categorical result across every encoding in `Enc_t(r)`:

```text
RobustForced(q=v)
iff
for every E in Enc_t(r), K_t^E |= (q=v).
```

If one admissible encoding leaves a materially live alternative, adverse or convenient closure is blocked.

This absorbs the useful IEL idea of encoding objectivity directly into OneLogic.

## 7. Provenance and evidential dependence

Evidence is represented through causal-informational ancestry in `G_t`.

The number of reports is not the number of independent observations.

```text
Derivative(e_j, e_i)
=>
no new independent ancestry merely from retransmission.
```

A copied article, repost, citation chain, repeated rumor, or ten outputs derived from one dataset remain dependent unless a later node contributes independent observation, authentication, measurement, or a genuinely new testable transformation.

This prevents apparent consensus from being counted as ten independent reasons when it is one reason copied ten times.

Support update therefore acts on dependence-calibrated evidence, not raw repetition count.

## 8. Source continuity without authority

A source model is part of the represented evidence state, not a truth oracle.

Previously demonstrated domain-relevant access, accuracy, calibration, transparent uncertainty, correction under pressure, and successful prediction may alter `>=_t` for later testimony.

The effect is defeasible and domain-sensitive.

```text
source standing -> provisional support
source standing -/-> truth
```

Previously earned source standing is not reset to zero merely because a new statement arrives. It persists as evidence until counterevidence, domain transfer, manipulation evidence, correction failure, decay, or other material defeater changes it.

Conversely, accumulated source standing never grants immunity from a live counterexample.

Testimonial weight and inquiry value remain distinct. A source may currently deserve little direct belief while still being highly useful as a lead to documents, distinctions, actors, tests, or observations.

## 9. One anti-collapse principle

Many IEL non-identities reduce to one OneLogic rule:

> Distinct represented relations may not be identified unless the required bridge survives the live possibilities and relevant correction conditions.

Therefore the system does not infer without a warranted bridge:

```text
expression = private judgment
omission = denial
disclosed basis = total basis
source reliability = claim truth
alignment = coordination
consideration = belief
belief = action
precaution = guilt
sincerity = memory fidelity
memory fidelity = historical truth
visible correction = correction-open latent policy
later truth = earlier evidential warrant
```

T10 already supplies the strict core: one live counterexample defeats a categorical bridge.

This is preferable to storing a separate named rule for every conversational mistake.

## 10. Inquiry from material uncertainty

Let `U_t(r)` be the unresolved distinctions in `Qmat(r)` that can still change judgment or response.

Each available inquiry `i` has:

```text
Gain(i) subseteq U_t(r)
Cost(i) = a burden vector
```

The burden vector may contain time, monetary cost, safety risk, privacy cost, irreversibility, attention, dependence, or other real constraints. OneLogic does not require those heterogeneous costs to collapse into one scalar utility.

Inquiry `i1` dominates `i2` when it resolves a superset of the relevant unresolved distinctions while imposing no greater burden in any represented burden dimension, with at least one strict improvement.

The proportionate inquiry frontier is the available, admissible, positive-gain, nondominated set.

This yields clarification, independent research, inferential testing, direct observation, consequence testing, or another domain-specific channel from the same generic relation.

Declining inquiry adds no evidence.

```text
NoInquiry does not imply q
NoInquiry does not imply not-q
```

## 11. Mature suspension

When a materially relevant proposition remains open and no proportionate inquiry is currently available or warranted, the mature state is suspension:

```text
Suspend(q)
iff
not Forced(q=v) for any v
and no proportionate discriminating inquiry is available
and the state remains correction-open
and the reasoner does not act as though q were settled.
```

Suspension can coexist with a provisional ordering. One interpretation may be more plausible than another while neither is treated as established fact.

## 12. Precaution without epistemic inflation

Action and belief remain distinct projections of the same judgment state.

An unresolved proposition may justify precaution when the material consequence profile makes a reversible protective action nondominated across the live possibilities.

Therefore:

```text
Act(a) does not imply Settled(q)
```

Evacuating after a credible smoke warning does not require pretending that fire has already been proved. Protecting against a plausible harmful possibility does not establish guilt.

## 13. Response dominance and mature action

For each feasible response `a`, let

```text
F(a,r)
```

be the set of materially relevant pressures that remain unresolved, sacrificed, or violated by that response under the represented referent.

A correction-open response `a` dominates response `b` when

```text
F(a,r) proper-subset F(b,r).
```

This is Stone-style objective improvement: preserve every success of `b`, correct at least one additional failure, and introduce no offsetting unresolved failure.

The mature response set is

```text
Y*(r) = {a : CorrectionOpen(a) and no correction-open a' dominates a}.
```

OneLogic need not force a unique act when reality contains a genuine tradeoff.

## 14. Tragic choice

If no feasible response has an empty unresolved-pressure set, there is no clean solution.

Mature judgment returns the correction-open nondominated frontier and preserves the residue explicitly:

```text
for every a in Y*(r), F(a,r) may be nonempty.
```

The existence of unavoidable loss does not license hiding which welfare, constraint, or other material pressure was sacrificed.

This converts IEL's tragic-pressure preservation into ordinary OneLogic dominance rather than a special tragedy module.

## 15. Temporal reality and self-fulfilling action

Truth is time-indexed through `T_t`.

An action at `t` may change the truth of a proposition at `t+1`.

```text
q(omega_{t+1}) = true
```

does not retroactively establish

```text
q(omega_t) = true
```

or prove that the earlier evidence warranted it.

This blocks self-fulfilling and self-defeating outcomes from laundering earlier unsupported judgment.

## 16. Recursive belief and strategic agents

Higher-order beliefs, latent policies, institutions, and strategic evaluator-aware behavior are represented only to the depth at which they preserve a material distinction in `Qmat(r)` or alter the mature response frontier.

If deeper recursion changes no material query, consequence, or admissible response, query-relative compression may merge it.

If it changes one, it must remain represented.

Thus recursive relevance follows from material representation rather than requiring an arbitrary fixed theory-of-mind depth.

Visible compliance or correction does not establish a hidden policy property unless the bridge is warranted across live strategic possibilities.

## 17. Prejudice as premature closure

Stone defines prejudice as judgment formed before the materially relevant pressures on that judgment have been integrated.

OneLogic expresses that computationally:

```text
PrematureClosure(q=v,r)
iff
AssertSettled(q=v)
and there exists a live materially adequate possibility or encoding
that defeats q=v or preserves a material distinction capable of changing it.
```

The statistically most likely interpretation may be provisionally favored. Treating it as settled while materially live alternatives remain is premature closure.

This gives the ordinary word `prejudice` a direct logical failure condition instead of treating it merely as social bias terminology.

## 18. One recursive judgment process

The entire calculus can be summarized as one loop:

```text
accessible reality-contact
    -> preserve / expand materially adequate possibilities
    -> preserve provenance and dependence
    -> eliminate only defeated possibilities
    -> update defeasible support among survivors
    -> test categorical invariance
    -> if open, inspect material uncertainty
    -> inquire when a proportionate discriminating route exists
    -> otherwise suspend
    -> if action is required, choose from the correction-open nondominated response frontier
    -> observe consequence
    -> reopen support, source models, representations, beliefs, and policies where reality defeats them
    -> repeat
```

There is no separate truth logic, empathy logic, interpersonal logic, moral logic, and action logic. They are different projections of the same reality-relative state.

## 19. Relation to the Philosopher's Stone

Stone supplies OneLogic's maturity criterion for what the referent may not silently discard:

```text
purpose: affected welfare <-> real-world constraint
meaning: informational grounding <-> contextual interpretation
accountability: answerability <-> insulation
```

OneLogic supplies the state/update discipline by which those pressures remain live, are compared, tested, acted on, and corrected.

At the mature limit, facts, context, constraint, affected welfare, consequence, testimony, and correction all retain their warranted governing force without any one becoming an insulated authority.

## 20. Relation to the old IEL paper

IEL is treated here as a discovery source, not a second live logic.

The following useful IEL results are absorbed into OneLogic through the smaller machinery above:

- provenance and dependence -> `G_t` and independent ancestry;
- source weighting and epistemic continuity -> defeasible support preorder;
- source-truth non-identity -> strict consequence remains independent of source standing;
- consideration / belief / action separation -> projection separation from one judgment state;
- provisional assumption -> support-maximal but non-forced judgment;
- mature suspension -> open judgment with no proportionate inquiry;
- clarification and inquiry-channel foreclosure -> proportionate inquiry frontier;
- adverse interpretation control -> encoding robustness + no premature closure;
- precaution without guilt -> action/belief non-collapse;
- correction supremacy -> reality-contact updates all defeated state components;
- strategic observability -> bridge validity over latent-policy possibilities;
- recursive relevance -> preserve recursion only while materially distinguishing;
- tragic choice -> nondominated response frontier with explicit residue;
- framework anti-self-sealing -> model inadequacy and representation expansion remain legal outputs.

The interpersonal vocabulary is therefore compressed into OneLogic rather than duplicated beside it.

## 21. Falsification conditions

This mature extension requires revision if any of the following is demonstrated:

1. a materially relevant distinction can be discarded without changing any possible mature judgment, response, or correction condition, showing the material criterion is overinclusive;
2. a maturity-relevant distinction exists that cannot be represented through informational grounding, contextual interpretation, real constraint, affected welfare, consequence, or correction, showing the Stone-derived closure is incomplete;
3. provisional support must logically create categorical truth even while a live counterexample remains, defeating the support/truth separation;
4. duplicate dependent transmission can supply genuinely new independent warrant without new ancestry, authentication, transformation, or contact, defeating provenance discipline;
5. a dominated inquiry or response is objectively preferable while every represented material success of the dominator is preserved and no new failure appears;
6. mature suspension logically requires settling an unresolved proposition;
7. the same accessible reality admits a materially adequate encoding under which a categorical conclusion fails, while OneLogic still licenses that conclusion as robustly settled;
8. a legitimate correction requires forbidding model inadequacy, reopening, or representation expansion.

OneLogic remains answerable to the same standard it applies to every other judgment: a counterexample that defeats the structure defeats the claim.
