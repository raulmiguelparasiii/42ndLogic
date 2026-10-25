# OneLogic: A Reality-Tracking Logic of Mature Judgment

## Abstract

OneLogic is a reality-tracking logic for reasoning under one actual world and finite, corrigible representation. Its original strict core separates actuality from the live represented possibilities, permits categorical assertion only when every live possibility agrees, updates against reality-contact by eliminating exactly what the observed outcome defeats, and requires representational expansion when actuality no longer fits the model class.

This formulation extends that same logic from binary settlement into mature judgment without replacing strict truth with a fuzzy truth value and without adding separate modules for empathy, testimony, social reasoning, morality, or action. A single judgment state now carries: the live possibilities, causal-informational provenance, defeasible comparative support, the materially required distinctions of the referent, available inquiry, feasible response, and world transition. Categorical truth remains strict. Graded support orders what remains live without turning the best-supported interpretation into fact. Material relevance is constrained by the Philosopher's Stone: informational grounding, contextual interpretation, real-world constraint, affected welfare, consequence, and correction must retain their warranted governing force. The useful structure of the earlier Interpersonal Epistemic Logic is absorbed as consequences of this smaller state and its update discipline.

The central result is a unified judgment process capable of returning categorical settlement, provisional favoring, unresolved judgment, proportionate inquiry, mature suspension, precaution without epistemic inflation, nondominated action under real tradeoff, explicit tragic residue, or model inadequacy. OneLogic therefore treats mature reasoning as reality-governed organization rather than as forced binary classification.

## 1. Semantic basis

Let `Omega_t` be the represented class of complete structured possibilities at time `t`, and let `omega_t` be actuality whenever the representation is adequate.

A finite reasoner never possesses actuality merely by possessing a model. It carries a live set

```text
K_t subseteq Omega_t
```

containing the possibilities not yet defeated by warranted reality-contact.

For a sound represented state:

```text
omega_t in K_t.
```

Queries may be partial and multi-valued. `UNDEFINED` is not false.

The mature OneLogic state relative to referent `r` is

```text
J_t(r) = <Omega_t, K_t, G_t, >=_t, Qmat(r), I_t, A_t, T_t>.
```

`G_t` is causal-informational provenance. `>=_t` is defeasible comparative support. `Qmat(r)` is the materially required query family. `I_t` is available reality-contact. `A_t` is feasible response. `T_t` represents world-changing transition.

These are fields of one reality-relative state. None receives independent truth authority.

## 2. Strict categorical consequence

For nonempty `K_t`, a categorical assertion is licensed only by invariance:

```text
K_t |= (q = v)
iff
for every w in K_t, q(w) is defined and q(w)=v.
```

This remains the settlement rule even after graded support is introduced.

A source may be highly reliable. One interpretation may be overwhelmingly plausible. A response may be practically urgent. None of these facts converts a live counterexample into nonexistence.

The strict layer therefore continues to obey:

> Preserve every possibility reality has not defeated. Eliminate exactly what warranted reality-contact defeats. Assert categorically only what the survivors force.

## 3. Sharp reality-contact update

Represent inquiry, observation, or intervention through a transition relation

```text
T_t subseteq Omega_t x O x Omega_(t+1).
```

After observed outcome `o`, define

```text
U*(K_t,o)
 = {w' : some w in K_t can produce outcome o and successor w'}.
```

Every posterior sound for the represented channel contains `U*`. `U*` is therefore the unique smallest sound posterior relative to that channel.

If actuality has already been removed from the live set, further contraction cannot restore it. If actuality lies outside the model class, correction confined to that model class cannot restore it. OneLogic must reopen or expand representation rather than manufacture certainty.

## 4. From binary settlement to mature judgment

Binary truth remains necessary for categorical claims, but mature judgment often occurs before categorical settlement.

OneLogic therefore distinguishes strict live possibility from defeasible comparative support.

Let `>=_t` be a preorder over `K_t`. It may be produced by probability, ranking theory, calibrated evidential comparison, causal inference, source modeling, or another warranted method. OneLogic does not require all domains to use one numerical credence scale.

Let

```text
Max_t = {w in K_t : no live w' is strictly better supported than w}.
```

Then

```text
Forced(q=v)
iff
all live possibilities force q=v.
```

```text
ProvisionallyFavored(q=v)
iff
not Forced(q=v)
and all support-maximal live possibilities define q=v.
```

If the support-maximal possibilities disagree, the query remains open.

The crucial non-collapse is

```text
ProvisionallyFavored(q=v) does not imply Forced(q=v).
```

A highly likely interpretation can therefore guide attention or inquiry while a materially live alternative prevents prejudicial closure.

Changing support order alone never changes strict categorical consequence while `K_t` and the query semantics remain fixed.

## 5. Material relevance and the Stone

The original OneLogic preserved distinctions relative to an admitted query family. That is insufficient for mature judgment because a reasoner can appear perfectly exact after silently excluding the questions that matter.

OneLogic therefore introduces a materially required query family `Qmat(r)`.

A distinction belongs to `Qmat(r)` when erasing it can change mature judgment relative to the declared referent through one of the reality relations identified by the Philosopher's Stone:

```text
informational grounding
contextual interpretation
real-world constraint
affected welfare
consequence
correction / answerability.
```

The set is referent-relative. A distinction irrelevant to one question may become decisive when the referent widens.

A useful formal view is to treat `Qmat(r)` as the least fixed point of material closure: begin with the declared query and repeatedly add any distinction whose variation can alter informational support, interpretation, feasible constraint, affected welfare, consequence, correction, or the nondominated response frontier. Stop only when no further materially governing distinction is exposed.

This prevents the logic from obtaining artificial certainty by narrowing the world until inconvenient reality disappears.

## 6. Empathy as logic

In the Stone, empathy is concern for affected welfare. OneLogic does not need an emotional simulation module to represent that relation.

If two otherwise similar live possibilities differ in the condition of an affected subject and that difference can alter mature judgment, then the welfare query belongs to `Qmat(r)`.

An adequate representation may not merge those possibilities.

The logical form is:

```text
AffectedWelfareRelevant(w1,w2,r)
=>
there exists q_welfare in Qmat(r)
with q_welfare(w1) != q_welfare(w2).
```

and therefore material adequacy requires

```text
h(w1) != h(w2)
```

for any representation `h` that would otherwise erase that distinction.

Empathy is thus operationalized as the preservation and governing use of affected welfare wherever reality makes welfare materially relevant.

Concern alone does not govern mature judgment. Welfare remains integrated with real-world constraint, information, context, consequence, and correction. This blocks sentimental overreach while also blocking cold calculation that treats affected persons as epistemically invisible.

## 7. Materially adequate representation

Let

```text
h : Omega_t -> H
```

be a proposed compression.

It is materially adequate relative to `r` only if

```text
h(w1)=h(w2)
=>
q(w1)=q(w2)
```

for every `q in Qmat(r)`, including definedness.

Compression is therefore allowed where difference is genuinely irrelevant and forbidden where it destroys a maturity-relevant distinction.

This also governs recursive belief depth. Higher-order beliefs are represented only while they can alter a material query, consequence, or mature response. Further nesting that changes none of those may be compressed. If deeper recursion matters, it must remain.

## 8. Encoding objectivity

Real records can admit multiple reasonable encodings. OneLogic cannot become mature merely by selecting the encoding that yields the desired answer.

Let `Enc_t(r)` be the materially adequate nondominated encodings of the accessible record. Then robust settlement requires

```text
RobustForced(q=v)
iff
for every E in Enc_t(r), K_t^E |= (q=v).
```

If one admissible encoding preserves a materially live alternative, categorical closure is not robust.

This captures the useful IEL principle of encoding objectivity in the same possibility-preserving logic.

## 9. Provenance and evidential dependence

`G_t` represents causal-informational ancestry among observations, records, expressions, transformations, inferences, commitments, actions, consequences, and corrections.

Evidence strength is not raw repetition count.

If ten reports descend from one observation, their number does not create ten independent observations. A retransmission adds independent evidential ancestry only when it introduces new observation, authentication, measurement, or another genuinely new testable transformation.

Thus

```text
independent evidence = independent ancestry,
not number of copies.
```

This blocks corroboration inflation, citation-loop inflation, and apparent consensus produced by a common source.

The support preorder is updated after dependence is represented, not before.

## 10. Source continuity without source authority

Source history is evidence about later testimony, but source and truth remain distinct.

Previously demonstrated domain-relevant access, calibration, successful prediction, transparent uncertainty, correction under pressure, and acknowledgment of error can alter provisional support. Previously earned standing does not rationally reset to zero merely because a new statement arrives.

Continuity remains defeasible. Contradiction, domain transfer, hidden incentive, repeated overconfidence, manipulation, correction refusal, or other defeating evidence can reduce the standing.

Formally:

```text
SourceStanding_t(s,r) -> update >=_t
```

while

```text
SourceStanding_t(s,r) -/-> q is true.
```

A reliable source may be wrong. An unreliable source may report truth. No source property replaces live reality.

Testimonial weight and inquiry value also remain distinct. A source can deserve little direct belief while remaining useful for locating documents, actors, distinctions, experiments, or counterevidence.

## 11. One anti-collapse rule

A large number of interpersonal reasoning failures are instances of the same structural mistake: identifying two relations without a warranted bridge.

OneLogic therefore does not store separate primitive prohibitions for every named mistake. T10 applies generally:

> A categorical bridge fails when one live possibility satisfies its premise while defeating its conclusion.

Consequently, without a warranted bridge, OneLogic refuses the following identifications:

```text
expression = private judgment
omission = denial
disclosed basis = complete basis
source reliability = claim truth
alignment = coordination
consideration = belief
belief = action
precaution = guilt
sincerity = memory fidelity
memory fidelity = historical truth
visible correction = correction-open policy
later truth = earlier evidential warrant.
```

These become applications of one logic rather than an expanding list of conversational rules.

## 12. Material uncertainty and inquiry

Let `U_t(r)` be the unresolved material distinctions still capable of changing judgment or response.

Each available inquiry `i` has a material gain set and a burden vector:

```text
Gain(i) subseteq U_t(r)
Cost(i) = <time, money, risk, privacy, irreversibility, attention, ...>.
```

The burden remains vector-valued because heterogeneous real costs need not have a universal exchange rate.

Inquiry `i1` dominates `i2` when `i1` resolves a superset of relevant uncertainty while imposing no greater represented burden in any dimension, with at least one strict improvement.

The proportionate inquiry frontier is the available, admissible, positive-gain, nondominated inquiry set.

This generic rule yields clarification, speaker inquiry, independent research, inferential testing, direct observation, consequence testing, or any other domain-specific channel without making them separate primitives.

Declining inquiry creates no evidence:

```text
NoInquiry -/-> q
NoInquiry -/-> not-q.
```

## 13. Mature suspension

When a materially relevant proposition remains unresolved and no proportionate inquiry is currently available or warranted, categorical judgment remains suspended.

```text
Suspend(q)
iff
q is not forced
and no proportionate discriminating inquiry is available
and correction remains open
and the reasoner does not act as though q were settled.
```

Suspension can coexist with a provisional ordering. One interpretation may currently be more plausible than another while neither is treated as fact.

This is especially important for interpersonal adverse attribution. The most likely negative interpretation can be provisionally favored while a live benign or less severe interpretation blocks settled accusation.

## 14. Precaution without epistemic inflation

Belief and action are distinct projections of `J_t(r)`.

An unresolved proposition may justify action when the consequence profile makes a reversible protective response nondominated across the live possibilities.

```text
Act(a) -/-> Settled(q).
```

A credible smoke warning can justify evacuation while the existence of a fire remains unresolved. A plausible risk can justify protection without establishing guilt. Action does not need certainty when consequence makes waiting irrational, but action cannot be used afterward as proof that the unresolved accusation was true.

## 15. Mature response frontier

For feasible response `a`, let

```text
F(a,r)
```

be the set of materially relevant pressures that remain unresolved, violated, or sacrificed by that response.

A correction-open response `a` dominates `b` when

```text
F(a,r) proper-subset F(b,r).
```

This is non-loss plus correction: every represented success of `b` is preserved, at least one additional failure is repaired, and no offsetting unresolved failure is introduced.

The mature response set is

```text
Y*(r)
 = {a : CorrectionOpen(a)
        and there is no correction-open a' that dominates a}.
```

OneLogic therefore permits more than one objectively mature response when reality contains a genuine unresolved tradeoff.

## 16. Tragic choice

Some situations have no response with empty material residue.

If

```text
for every feasible a, F(a,r) != empty,
```

maturity does not invent a clean answer. OneLogic returns the correction-open nondominated frontier and preserves every remaining sacrificed pressure explicitly.

This absorbs IEL's tragic-choice machinery into ordinary response dominance.

## 17. Time and world-changing action

Truth is time-indexed.

An action at `t` can make a proposition true at `t+1` without proving that it was true or warranted at `t`.

```text
q(omega_(t+1)) = true
-/->
q(omega_t) = true.
```

Self-fulfilling and self-defeating outcomes are therefore ordinary causal transitions, not retroactive evidence.

The same rule blocks post-hoc rationalization: a later explanation or successful outcome does not prove that the relevant integration was present before the action unless the pre-event state or policy supplies that bridge.

## 18. Strategic agents and latent policy

Observed compliance, transparency, concession, independence, or correction may be generated strategically.

OneLogic therefore permits a claim about a latent policy only when the bridge from observed behavior to that policy survives the live strategic possibilities.

An evaluator-aware performance that could occur under both correction-open and correction-resistant policies leaves the latent query unresolved.

The logic does not need a special deception detector. It preserves the alternative until discriminating reality-contact defeats it.

## 19. Prejudice as premature closure

The Philosopher's Stone grounds prejudice as judgment formed before materially relevant pressures have been integrated.

OneLogic gives this an executable logical condition:

```text
PrematureClosure(q=v,r)
iff
q=v is treated as settled
and either
  a materially adequate live possibility defeats q=v,
or
  an omitted material distinction can still change q or the mature response.
```

The highest-ranked interpretation may therefore be provisionally favored without being prejudicial. The failure occurs when provisional ranking is converted into settled judgment before material reality has closed the alternative.

This is the exact place where binary classification becomes mature judgment.

## 20. Optimal good-faith truth-seeking

Good faith alone does not make reasoning mature. A sincere reasoner can still omit consequence, ignore welfare, overread context, count dependent reports as independent, or close uncertainty too early.

Define mature OneLogic truth-seeking relative to `r` by the conjunction:

```text
Mature(J_t,r)
iff
SoundLiveState(J_t)
and MateriallyAdequate(J_t,r)
and DependenceCalibrated(J_t)
and NoCategoricalOverreach(J_t)
and ProvisionalNotCollapsed(J_t)
and MaterialUncertaintyHandled(J_t,r)
and ResponseOnMatureFrontier(J_t,r)
and CorrectionOpen(J_t,r).
```

`MaterialUncertaintyHandled` means that unresolved material uncertainty is met by a proportionate discriminating inquiry, a correction-open provisional assumption, or mature suspension. If action cannot wait, action must come from the mature response frontier without falsely settling the unresolved proposition.

This is the OneLogic form of optimal good-faith truth-seeking. The Stone supplies what mature judgment must remain answerable to; OneLogic supplies the state and update discipline that keeps those pressures governing.

## 21. Absorbing Interpersonal Epistemic Logic

IEL is now treated as a discovery source for relations that OneLogic should generate, rather than as a second logic beside it.

Its useful results reduce as follows:

```text
claim/proposition alternatives          -> K_t
causal-information graph                -> G_t
provenance/dependence                   -> ancestry in G_t
source weighting                        -> defeasible >=_t
epistemic continuity                    -> persistence of undefeated source evidence
source-truth non-identity               -> strict consequence independent of source standing
consideration/belief/action separation  -> distinct projections of J_t
provisional assumption                  -> support-maximal but non-forced judgment
mature suspension                       -> open judgment with no proportionate inquiry
clarification/inquiry value             -> inquiry frontier
adverse interpretation control          -> robust encoding + no premature closure
precaution without guilt                -> action/belief separation
correction supremacy                    -> reality-contact revises every defeated component
strategic observability                 -> bridge validity over latent-policy alternatives
recursive belief                        -> material representation depth
tragic choice                           -> nondominated response frontier with residue
memory/sincerity non-identity            -> bridge discipline
institutional policy                    -> represented world-level agent/policy structure
framework anti-self-sealing             -> model inadequacy remains a legal output.
```

The interpersonal vocabulary is compressed into OneLogic rather than duplicated.

## 22. One recursive process

The complete reasoning process is:

```text
reality-contact
 -> construct / preserve materially adequate possibilities
 -> preserve causal-informational provenance
 -> eliminate only what contact defeats
 -> update defeasible support among survivors
 -> test categorical invariance
 -> if unresolved, inspect material uncertainty
 -> use a proportionate nondominated inquiry when available
 -> otherwise suspend categorical judgment
 -> if action is required, act from the correction-open nondominated response frontier
 -> observe consequence
 -> revise support, source models, interpretation, representation, belief, and policy wherever reality defeats them
 -> expand the model if required
 -> repeat.
```

There is one logic because the same objects and same update discipline generate factual judgment, interpersonal interpretation, source learning, moral consequence, inquiry, action, and correction.

## 23. Falsification

The mature formulation must be revised if a counterexample shows any of the following:

1. categorical truth can be warranted while a live materially adequate counterexample remains;
2. provisional support logically must eliminate a live possibility even without defeating reality-contact;
3. a necessary maturity-relevant distinction exists outside informational grounding, contextual interpretation, real constraint, affected welfare, consequence, and correction;
4. a distinction included by material closure can always be erased without changing any possible mature judgment, consequence, response, or correction condition;
5. repetition with no new causal-informational ancestry can create genuinely independent evidential warrant;
6. a dominated inquiry or response is objectively superior despite preserving no additional material success and introducing no compensating correction;
7. mature suspension requires pretending an unresolved proposition is settled;
8. precaution logically entails guilt or categorical belief;
9. a categorical conclusion remains licensed even though an admissible materially adequate encoding defeats it;
10. correction requires forbidding model inadequacy, reopening, or representation expansion.

OneLogic receives no exemption from its own standard. A material counterexample that defeats the architecture requires correction of the architecture.

## 24. Scope and status

OneLogic does not claim that every linguistic sentence is Boolean, every domain should use the same probability model, every human value can be reduced to one utility number, or every possible reasoning problem is decidable.

Strict consequence, defeasible support, inquiry burden, and response dominance are deliberately separated because they answer different questions inside one judgment state.

The formal theorem layer establishes only the claims actually encoded and proved. Executable finite tests can falsify bounded cases but do not establish universality. Lean or another proof assistant can verify general consequences once the mature obligations are encoded. Formal proof still does not prove that the chosen primitives exhaust reality; that remains an empirical and philosophical falsification condition.

The objective target is compact:

> Keep reality live until reality closes it. Give the best-supported interpretation its warranted provisional weight. Preserve every material distinction, including affected welfare, that can still change mature judgment. Inquire proportionately. Suspend when warranted. Act without pretending uncertainty disappeared. Let consequence and correction reopen everything that reality defeats.
