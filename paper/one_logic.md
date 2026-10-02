# OneLogic: A Reality-Tracking Architecture for Inference, Inquiry, and Correction

## Abstract

OneLogic is a proposed compact architecture for reasoning under one actual reality. It separates actuality from a finite reasoner's representation, treats strict categorical inference as invariance across live possibilities, treats inquiry as reality-contact that removes exactly the possibilities incompatible with an observed outcome, and requires representational revision when actuality falls outside the current model class. The architecture also yields an objective two-direction account of reasoning deviation: unsupported exclusion and unsupported retention.

The proposal is deliberately narrower than a claim to have solved every domain of reasoning. Probability, utility, causal structure, temporal structure, counterfactuals, values, and domain-specific science may live inside structured possibilities without being reduced to strict entailment. OneLogic instead attempts to characterize the outer reality-tracking discipline by which such structures are represented, queried, tested, corrected, and used without manufacturing certainty.

## 1. Semantic basis

Let **M** be a represented class of complete structured possibilities and **1 ∈ M** actuality whenever the representation is adequate. A finite reasoner has explicit represented material **E**, inducing a live state **K(E) ⊆ M**. For a sound represented state, **1 ∈ K(E)**.

A legitimate query may be partial and multi-valued. Undefinedness is not treated as falsity.

For nonempty **K**, categorical consequence is:

```
K ⊨ (q = v)  iff  every M in K defines q(M) = v.
```

Any universally sound categorical rule is contained in this invariant consequence relation. Strict soundness cannot categorically say more than all live possibilities jointly force.

## 2. Inquiry and sharp update

Represent inquiry or intervention by a transition relation:

```
T ⊆ M × O × M
```

After observed outcome **o**:

```
U*(K,o) = {M' : some M in K can produce outcome o and successor M'}.
```

Every posterior that is sound for the modeled channel must contain **U*(K,o)**. Therefore **U*** is the unique smallest sound posterior under set inclusion, and is maximally sharp relative to the represented channel.

The resulting discipline is:

> Preserve every possibility reality has not defeated. Eliminate exactly what warranted reality-contact defeats. Assert only what the survivors force.

## 3. Correction and open ontology

If actuality has already been excluded from **K**, no subset-only contraction can restore it. Correction may require reopening possibilities or revising assumptions.

If actuality lies outside the represented model class itself, no live state confined to that class can restore actuality. The model class must expand or be replaced.

## 4. Representation and material distinction

For an admitted query family **Q**, two possibilities are equivalent when every admitted query has the same definedness and value on both.

A representation that merges possibilities distinguished by an admitted query loses a material distinction. Compression is therefore legitimate only relative to the questions the representation must preserve.

## 5. Objective deviation

Once an ideal state **I** is independently established, a candidate state **A** can depart from it in two directions:

```
unsupported exclusion = I \ A
unsupported retention = A \ I
```

The exact state has zero deviation. A reasoning state weakly dominates another when both of its deviation sets are subsets of the other's; dominance is strict when at least one inclusion is strict.

For inquiry, **U*(K,o)** supplies the independently established ideal. A sound but non-sharp update can only be inferior by retaining possibilities the modeled outcome already defeats. An update that excludes any member of **U*** is unsound.

For strict inference, a universally sound rule cannot assert beyond the invariant consequence set, though it may omit conclusions already forced.

## 6. Named fallacies as surface patterns

The architecture does not identify fallacies by wording. Personal criticism, insult, popularity, chronology, emotion, or source history may be true, false, relevant, irrelevant, malicious, or benign.

A premise-to-conclusion bridge is valid only when the premise is live-realizable and every live realization of the premise carries the conclusion. One live counterexample defeats the bridge.

This explains why “the speaker is dishonest” is not automatically an ad hominem fallacy. It may matter to testimony reliability while remaining irrelevant to the truth of a mathematical theorem. Logical status depends on the bridge, not the surface form.

## 7. The OneLogic Solver

The OneLogic Solver operationalizes the architecture as a controller:

```
generate → represent → infer → discriminate → observe → update → correct → repeat
```

A language model may generate hypotheses, code patches, explanations, experiment proposals, or mathematical transformations. It is not the truth authority. External tests, compilers, proof checkers, repository behavior, datasets, instruments, simulations, or human observations may supply reality-contact.

If all live candidates agree on an answer, the answer is forced relative to the represented state. If they disagree, the solver seeks a discriminating inquiry. If no candidate survives an actual observation, the solver requests representational expansion instead of manufacturing a conclusion.

## 8. Machine use

OneLogic can serve as an epistemic control layer around existing machine intelligence. It does not replace perception, planning, motor control, representation learning, probability models, or domain knowledge. It governs questions such as:

- What is categorically warranted?
- What remains unresolved?
- Which distinction matters to the current query?
- What observation would discriminate the live alternatives?
- Which alternatives did the observation actually defeat?
- Has the current model class failed?
- Is the machine retaining defeated possibilities?
- Is it eliminating possibilities without warrant?

Potential applications include coding agents, autonomous science, research agents, model evaluation, machine-learning supervision, and multi-agent information integration.

## 9. Falsification criteria

The core should be reopened if a legitimate reality-tracking operation is produced that cannot be represented without violating the architecture.

Serious challenges include a categorical truth-preserving inference that exceeds invariance without new warranted information; a sound and strictly sharper update than **U*** for the same correctly represented channel and outcome; a materially distinct reality the architecture is forced to identify even after admissible refinement; or a required correction that cannot be represented by reopening or replacing the live/model space.

New domain content alone does not falsify the architecture.

## 10. Limits and status

Formal verification proves theorems from formal assumptions. It does not by itself prove that the assumptions exhaust every aspect of actual reality. Bounded computational search can find counterexamples within its search domain but does not replace general proof.

The current formal layer concerns strict categorical consequence and possibility-preserving update. Defeasible reasoning, graded credence, utility, action, and normative evaluation require additional domain structure.

Historical novelty and comparison with existing logical, semantic, belief-revision, learning-theoretic, causal, and state-minimization traditions require a separate scholarship pass and are not assumed here.

The associated repository contains Lean theorem statements, an axiom-audited proof workflow, a finite executable semantics, bounded adversarial countermodel search, a non-transformer OneLogic Solver controller, and a public foundation site.
