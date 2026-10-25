# OneLogic theorem obligations

The formal layer states exactly what is mechanically claimed. T1-T10 are the original strict reality-tracking core. T11-T18 are the mature-judgment obligations introduced by the unified formulation. A statement listed here is an obligation of the architecture; it must not be described as machine-proved unless its corresponding executable/Lean gate actually proves it.

## T1. Greatest sound categorical consequence

For nonempty `K`:

`C(K) = {[q=v] : every m in K defines q(m)=v}`.

Any categorical rule sound over every live possibility is a subset of `C(K)`.

## T2. Sharp sound update

For transition channel `T`:

`U*(K,o) = {m' : some m in K can transition to m' with outcome o}`.

Every posterior sound for the modeled channel contains `U*(K,o)`. Therefore `U*` is the unique smallest sound posterior.

## T3. Reality preservation

If actuality is live and the actual transition is represented by `T`, the actual successor remains in `U*(K,o)`.

## T4. Sound pooling

Two live states that both contain actuality cannot become empty merely by intersection.

## T5. Contraction cannot repair excluded actuality

If actuality is absent from `K`, no subset of `K` can restore it.

## T6. Query-relative representation

A representation that merges two possibilities distinguished by an admitted query loses a material distinction for that query family.

## T7. Model-class failure forces expansion

If actuality lies outside the current model class, correction confined to that model class cannot restore actuality.

## T8. Objective deviation and dominance

For independently established ideal `I` and candidate state `A`:

`unsupported exclusion = I \ A`

`unsupported retention = A \ I`.

The exact ideal has zero deviation and strictly dominates every materially deviant candidate under inclusion of those two error sets.

For modeled inquiry, `U*(K,o)` supplies the independently established ideal.

## T9. Sound categorical rules do not overreach

A universally sound categorical rule cannot assert a value outside the invariant categorical consequence set. It may still omit information that is already forced.

## T10. One counterexample defeats a categorical bridge

A premise-to-conclusion bridge fails if one live possibility satisfies the premise while the conclusion fails.

This is content-neutral. Insult, criticism, source reliability, popularity, chronology, emotion, or any other premise is not a fallacy by surface form. The question is whether the claimed bridge to the conclusion holds.

# Mature-judgment obligations

## T11. Defeasible support cannot manufacture categorical truth

Let `>=` be any support preorder over nonempty live state `K`. Changing `>=` while holding `K` and query interpretation fixed does not change `C(K)`.

A query value shared by every support-maximal live possibility may be provisionally favored, but if a live possibility gives a different value or leaves the query undefined, the value is not thereby categorically forced.

This separates `most supported` from `settled`.

## T12. Material-relevance preservation

For referent `r`, let `Qmat(r)` be the materially required query family. If `q in Qmat(r)` distinguishes two represented possibilities in value or definedness, any representation that identifies those possibilities is materially inadequate relative to `r`.

Stone currently constrains `Qmat(r)` to preserve distinctions that can alter mature judgment through informational grounding, contextual interpretation, real-world constraint, affected welfare, consequence, or correction.

This closes the loophole in which a reasoner remains formally exact only because it omitted a materially governing distinction from the admitted query family.

## T13. Robust settlement across admissible encodings

Let `Enc(r)` be the materially adequate nondominated encodings of the accessible record. A categorical assertion is robustly settled only if every `E in Enc(r)` forces the same value.

If one admissible encoding preserves a live counterexample or unresolved material distinction, robust settlement fails.

## T14. Dependent transmission does not create independent ancestry

If a new evidential record has no independent causal-informational ancestry beyond ancestry already represented, mere retransmission, repetition, republication, or copying does not increase the number of independent ancestry units.

A later record may add warrant by adding independent observation, authentication, measurement, or another genuinely new testable transformation; that is new contact, not repetition alone.

## T15. Proportionate inquiry frontier

For unresolved material distinctions `U`, inquiry `i1` dominates `i2` when `i1` discriminates a superset of `U` while imposing no greater represented burden in any burden dimension, with at least one strict improvement.

An available admissible inquiry with positive material gain is proportionate only if no available admissible inquiry dominates it.

Declining inquiry does not change `K`, does not create a new observation, and therefore cannot by itself establish either `q` or `not-q`.

## T16. Mature response dominance

For a feasible response `a`, let `F(a,r)` be its unresolved or sacrificed materially relevant pressures. If correction-open response `a` satisfies

`F(a,r) proper-subset F(b,r)`,

then `a` strictly dominates `b`: it preserves every represented success of `b`, corrects at least one additional failure, and introduces no offsetting unresolved failure.

The mature response set is the correction-open nondominated frontier.

## T17. Tragic residue is not logical failure

If no feasible correction-open response has empty `F(a,r)`, the mature response set may contain multiple incomparable responses with nonempty residue.

OneLogic must preserve that residue rather than manufacture a clean optimum or erase the sacrificed pressure.

## T18. Suspension and precaution do not imply settlement

When no value of query `q` is categorically forced and no proportionate discriminating inquiry is available or warranted, withholding categorical judgment is sound.

A precautionary action may still be selected from the mature response frontier when its justification is a material consequence profile rather than a claim that `q` is settled.

Therefore neither suspension nor precaution implies categorical belief in any unresolved proposition.

## Derived unifications

The following older interpersonal rules are not separate primitives in the mature formulation. They are intended to follow from T10-T18 plus the one judgment state:

- expression, commitment, disclosed basis, private judgment, source reliability, claim truth, consideration, belief, action, precaution, sincerity, memory fidelity, historical truth, visible correction, and latent policy remain distinct unless a warranted bridge connects them;
- source history may defeasibly alter support without determining truth;
- previously earned source standing remains evidence until defeated rather than resetting automatically;
- source testimonial weight and source inquiry value may diverge;
- higher-order belief is represented only to the depth at which it preserves a material distinction or changes the mature response frontier;
- action at `t` may change truth at `t+1` without retroactively proving that the changed proposition was true or warranted at `t`;
- model inadequacy, reopening, and representation expansion remain permitted outputs for OneLogic itself.

## Scope

These obligations do not establish that every sentence is Boolean, that the represented model class is permanently complete, that ordinal support must be probabilistic, that utility reduces to strict entailment, that one scalar can rank every human consequence, or that finite agents can compute every semantic consequence.

The support preorder may be instantiated by probability, ranking theory, a calibrated evidential model, or another warranted ordering, provided its output remains defeasible and does not replace strict consequence.

The Stone-derived material closure remains falsifiable. If a necessary maturity-relevant relation exists outside informational grounding, contextual interpretation, real constraint, affected welfare, consequence, and correction, the material criterion must expand.

Formal proof establishes consequences of stated assumptions. It does not by itself prove that those assumptions exhaust actual reality.
