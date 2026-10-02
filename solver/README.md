# OneLogic Solver

The public OneLogic Solver is a small reasoning-controller demonstrator.

A generator may be an LLM, search procedure, symbolic engine, human, program synthesizer, or any mixture of them. The controller's job is to prevent the generator from becoming the truth authority.

## Core loop

1. Generate candidate structured possibilities.
2. Keep the candidates still compatible with warranted evidence.
3. If every live candidate gives the same answer, return that answer as forced relative to the represented state.
4. Otherwise choose a discriminating inquiry.
5. Obtain the actual outcome from a reality-contact adapter.
6. Retain exactly the candidates compatible with the outcome.
7. If nothing survives, request representational expansion instead of manufacturing an answer.
8. Repeat until forced, non-identifiable under available inquiries, or budget-limited.

The dependency-free demo implements this loop over a finite hypothesis space.

## Why this is useful

A transformer can be attached as a candidate generator without granting it final authority. Compilers, unit tests, instruments, datasets, simulations, search results, or theorem provers can serve as reality-contact depending on the domain.

The public solver is intentionally small. Production execution policy, live target selection, platform-specific automation, provider strategy, private traces, and other operational machinery are outside this repository.

## Run the demo and tests

```bash
python -m solver.demo
python -m unittest solver.test_solver -v
```
