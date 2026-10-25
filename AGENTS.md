# 42ndLogic project memory

Read this file before changing the project.

## Purpose

42ndLogic is the public foundation repository for OneLogic: a falsifiable reality-tracking architecture for strict inference, inquiry, correction, representation, and machine reasoning.

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
- A live state K contains the possibilities not yet defeated by warranted information.
- Strict categorical assertion is permitted only where the admitted query is invariant across nonempty K.
- Reality-contact updates must retain every modeled successor compatible with the actual outcome and eliminate every modeled successor the outcome defeats.
- If actuality is excluded, contraction alone cannot repair the state.
- If actuality is outside the model class, the model class must expand or be replaced.
- Undefined is not false.
- Defeasible preference, probability, utility, and action selection are not silently collapsed into strict entailment.
- Named fallacies are surface patterns. The formal layer tracks unsupported exclusion, unsupported retention, representational loss/switch, bad inquiry, and failed correction.

## Engineering rules

- Keep the semantic core small.
- Treat LLMs as candidate generators, not truth authorities.
- External tests, observations, proof checkers, compilers, experiments, and validated data are reality-contact adapters.
- Do not claim a bounded search is a universal proof.
- Do not claim a formal proof establishes that the formal assumptions exhaust reality.
- Preserve explicit falsification criteria.
- Avoid adding a primitive when the same behavior is derivable from the current core.
- Keep public examples minimal and reproducible.
- Never commit credentials, API keys, bank details, identity documents, or private contact information.
