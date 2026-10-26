# OneLogic theorem obligations

This file separates the claims of the architecture from their proof status. T1-T10 are the strict reality-tracking core. T11 onward are mature-judgment obligations and derived laws. A theorem must not be described as generally machine-proved merely because a finite executable regression passes.

## First-principles ground

OneLogic is relative to one actual time-indexed history

`H_t = <omega_0, e_1, omega_1, ..., e_t, omega_t>`.

`H_t` is reality as it has transpired in the formal referent. A grounding map `Ground(H_t)` exposes warranted relational structure from that history. The live model set represents only unresolved completions compatible with the grounded history; it is not a replacement for actuality.

For referent `r`:

`Qmat_t(r)` is the least materially closed distinction family currently required by reality.

`K_t(r)` contains the represented completions compatible with `Ground(H_t)` while preserving `Qmat_t(r)`.

The recursive judgment operator is schematically

`One(H_t,r) = <G_t, Qmat_t(r), K_t(r), >=_t, I_t, A_t, T_t, D_t>`

where `D_t` is the relational deviation signature.

# Strict core

## T1. Greatest sound categorical consequence

For nonempty `K`:

`C(K) = {[q=v] : every m in K defines q(m)=v}`.

Any categorical rule sound over every live completion is a subset of `C(K)`.

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

A representation that merges two possibilities distinguished by an admitted query loses that distinction for the admitted query family.

## T7. Model-class failure forces expansion

If actuality lies outside the represented model class, correction confined to that class cannot restore actuality.

## T8. Objective state deviation

For independently warranted ideal state `I` and proposed state `A`:

`E-(I,A) = I \ A`  unsupported exclusion

`E+(I,A) = A \ I`  unsupported retention.

The exact ideal has zero deviation. A state weakly dominates another when both deviation sets are subsets of the other's; dominance is strict when at least one inclusion is strict.

## T9. Sound categorical rules do not overreach

A universally sound categorical rule cannot assert a value outside the invariant categorical consequence set. It may still omit conclusions already forced.

## T10. One counterexample defeats a categorical bridge

For a proposed bridge `A=a -> B=b`, let

`K[A=a] = {m in K : A(m)=a}`.

The categorical bridge holds only if `K[A=a]` is nonempty and every member defines `B=b`. One counterexample or undefined conclusion in that premise region blocks categorical closure.

The rule is semantic-content neutral. It does not contain primitives such as insult, motive, ignorance, guilt, coordination, or prejudice.

# Mature-judgment obligations

## T11. Defeasible support cannot manufacture categorical truth

Let `>=` be a support preorder over nonempty `K`. Changing `>=` while holding `K` and query interpretation fixed does not change `C(K)`.

If every support-maximal live completion gives `q=v` while another live completion differs, `q=v` may be provisionally favored but is not categorically settled.

## T12. Material-relevance preservation

For referent `r`, if `q in Qmat(r)` distinguishes two represented completions in value or definedness, any representation that identifies those completions is materially inadequate relative to `r`.

Current Stone-grounded material closure includes any distinction whose removal can change judgment through informational grounding, contextual interpretation, real-world constraint, affected welfare, consequence, or correction.

## T13. Robust settlement across adequate encodings

Let `Enc(r)` be the materially adequate nondominated encodings of the accessible actual record. A categorical assertion is robustly settled only if every `E in Enc(r)` forces the same value.

## T14. Dependent transmission does not create independent ancestry

Mere retransmission, repetition, republication, or copying does not create new independent causal-informational ancestry. New observation, authentication, measurement, or a genuinely new testable transformation may create new ancestry.

## T15. Proportionate inquiry frontier

For unresolved material distinctions `U`, inquiry `i1` dominates `i2` when `i1` discriminates a superset of `U` while imposing no greater represented burden in any dimension, with at least one strict improvement.

Declining inquiry adds no event to `H_t` that supports either side merely by being declined.

## T16. Mature response dominance

For response `a`, let `F(a,r)` be its unresolved or sacrificed material pressures. If correction-open response `a` satisfies

`F(a,r) proper-subset F(b,r)`,

then `a` strictly dominates `b` relative to the represented material field.

## T17. Tragic residue is preserved

If no feasible correction-open response has empty `F(a,r)`, the mature response set may contain multiple incomparable responses with nonempty residue. OneLogic does not invent a clean optimum by erasing that residue.

## T18. Suspension and precaution do not settle unresolved propositions

When no value of `q` is categorically forced and no proportionate discriminating inquiry is warranted, withholding categorical closure is sound. A precautionary response may still be warranted by consequence across the live completions.

# General relational-deviation laws

## T19. Bridge deviation is a set, not a named fallacy

For bridge `A=a -> B=b`, define

`D_B = {m in K[A=a] : B(m) is undefined or B(m) != b}`.

`D_B = empty` is the strict bridge condition. A named phenomenon such as assuming ignorance, inferring motive, omission-as-denial, guilt-by-precaution, or coordination-from-agreement is an application of the same `D_B`, not a new primitive.

If a warranted measure `mu` over the premise region is independently supplied, a diagnostic magnitude may be defined as

`delta_B = mu(D_B) / mu(K[A=a])`.

Without a warranted measure, the defect set itself is canonical; OneLogic does not invent weights.

## T20. Material representation-loss deviation

For representation `h`, define

`D_M(h,r) = {(m,n,q) : h(m)=h(n), q in Qmat(r), q(m) != q(n)}`

including differences of definedness.

`D_M = empty` is material adequacy. This turns caricature, overcompression, and omitted affected welfare into instances of one representation-loss relation.

## T21. Correction debt

Let `C_t` be material, available, admissible corrections capable of changing a dependent judgment. Let `Integrated_t` be the subset actually incorporated before that dependent judgment is reused or closed.

`D_C = C_t \ Integrated_t`.

Nonempty `D_C` is correction debt. Repeated reasoning that depends on the same uncorrected structure while relevant correction remains available is recursive correction failure.

## T22. Relational deviation signature

A phenomenon may be isolated by the set-valued signature

`D_t = <E-, E+, D_B, D_M, D_C>`.

The zero signature is exact relative to the represented referent. Componentwise set inclusion gives a partial ordering of deviation without forcing heterogeneous defects into one scalar.

A domain may attach warranted measures to individual components. Those measured magnitudes are diagnostics and do not replace the underlying sets.

## T23. Recursive frame-lock criterion

For an agent model `M_t(B->A)` of another participant and independently warranted model `W_t(A)`, use T8:

`E-_t = W_t(A) \ M_t(B->A)`

`E+_t = M_t(B->A) \ W_t(A)`.

If a material correction at `t` targets a member of this deviation, remains in `D_C`, and the next dependent inference reuses the same deviating model, the deviation has persisted recursively. Repetition across turns yields a frame-lock trace rather than a new primitive fallacy.

This criterion is agnostic to whether the psychological cause is prejudice, misunderstanding, strategic behavior, poor attention, or another latent mechanism. Those are further queries and require their own warrant.


## T24. Reductio as live-region elimination

For proposition or query value `P`, define `K[P] = {m in K : m satisfies P}`. If warranted consequence and grounded/material constraints eliminate every member of `K[P]`, then `K[P]` is empty and `P` is defeated relative to the current adequate model class.

The reverse proof-by-contradiction step from `not-P` being impossible to categorical `P` is valid only when the represented query partition is exhaustive. If an undefined, third, or otherwise distinct live value remains, eliminating `not-P` does not establish `P`.

A reductio is defective when the contradiction arises only after unsupported exclusion `E-`, unsupported retention `E+`, bridge defect `D_B`, or material representation loss `D_M`.


# Strongest warranted judgment

For a query family `Q`:

`C_t = C(K_t)` is the complete categorical consequence set.

Let `Max_t` be the support-maximal region of `K_t`.

`P_t = C(Max_t) \ C_t` is the provisional consequence set, subject to the rule that members of `K_t` outside `Max_t` remain live until defeated.

The unresolved residue is what material closure and valid inference still do not settle. OneLogic therefore derives as far as reality warrants rather than treating uncertainty as an objective in itself.

# Recursive correction

When reality advances

`H_t -> H_(t+1)`,

OneLogic recomputes or revises grounding, material closure, live completions, support, inquiry, response, and deviation:

`One(H_(t+1),r') = Correct(One(H_t,r), e_(t+1), omega_(t+1), r')`.

A correction operator that preserves a component already defeated by the new actual history is not exact.

# Derived phenomenon families

The following are diagnostic names for signatures, not axioms:

- manufactured position / assumed ignorance: bridge defect and often opponent-model `E+`;
- caricature / frame substitution: opponent-model `E-` and/or `E+`, often with material loss;
- omission-as-denial: bridge defect;
- source reset: unsupported exclusion of still-relevant source evidence;
- corroboration inflation: provenance dependence ignored in support;
- guilt-by-precaution: bridge defect from action to settled attribution;
- silent adverse closure: provisional ranking converted to categorical closure with live defect;
- correction foreclosure: nonempty `D_C`;
- recursive frame lock / talking past each other: persistent opponent-model deviation plus correction debt across recursive updates;
- prejudice: categorical or stance closure while a materially governing distinction remains unintegrated;
- good-faith process failure: truth-seeking aim may be present, but the operative state remains materially deviated or correction-indebted.

The labels may change while the generating logic remains the same.

# Scope

These obligations do not establish that every sentence is Boolean, that `Ground` has already solved unrestricted perception or semantics, that the represented model class is permanently complete, that ordinal support must be probabilistic, or that every heterogeneous consequence admits one scalar utility.

ULT-style relational grounding is a candidate implementation of parts of `Ground`, not an assumption that unrestricted grounding has been solved. The current bounded Empathy bridge demonstrates one intervention-grounded instance, not a completed universal perceptual system.

The Stone-derived material closure remains falsifiable. If a maturity-relevant relation exists outside the current closure, the closure must expand.

Formal proof establishes consequences of stated assumptions. It does not by itself prove that those assumptions exhaust actual reality.
