# OneLogic Solver

The OneLogic Solver is a reasoning controller, not a foundation model.

A generator may be an LLM, search procedure, symbolic engine, human, program synthesizer, or any mixture of them. The controller's job is to prevent the generator from becoming the truth authority.

## Loop

1. Generate candidate structured possibilities.
2. Keep the candidates still compatible with warranted evidence.
3. If every live candidate gives the same answer, return that answer as forced relative to the represented state.
4. Otherwise choose a discriminating inquiry.
5. Obtain the actual outcome from a reality-contact adapter.
6. Retain exactly the candidates compatible with the outcome.
7. If nothing survives, request representational expansion instead of manufacturing an answer.
8. Repeat until forced, non-identifiable under available inquiries, or budget-limited.

The included proof-of-concept is dependency-free Python and demonstrates adaptive inquiry over a finite hypothesis space.

## Why this is useful

A transformer can be attached as a candidate generator without granting it final authority. For coding, a future adapter can use compiler output, unit tests, repository behavior, and acceptance tests as reality-contact. For science, adapters can use simulations, instruments, datasets, or theorem provers. For research, search/retrieval can be treated as inquiry whose result updates the live space.

## Run the demo

```bash
python -m solver.demo
python -m unittest solver.test_solver -v
```

## Security

Never put API keys, payout details, bank information, private identity documents, or personal contact data in this repository. Provider credentials should be injected at runtime through a secret manager or environment variables.
