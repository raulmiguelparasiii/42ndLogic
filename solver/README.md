# OneLogic Solver

The OneLogic Solver is a reasoning controller, not a foundation model.

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

## Coding / money solver

`solver/coding/` turns the same discipline into a coding-bounty controller.

The coding loop is:

```
public issue
  -> candidate patches
  -> clean repository state
  -> declared tests / acceptance commands
  -> eliminate failed candidates
  -> feed failure evidence back to the generator
  -> expand candidates
  -> return only a patch that survives every declared check
```

An external LLM or coding model can implement the small JSON patch-generator protocol in `solver/coding/PROTOCOL.md`. The model proposes patches; it does not certify them.

The command-line entry point is:

```bash
python -m solver.coding.cli \
  https://github.com/owner/repo/issues/123 \
  --generator "your-generator-command --json" \
  --test "python -m pytest -q" \
  --allow-local-exec
```

If a patch survives all declared checks, the solver writes a canonical unified diff to `solution.patch`. If none survives, it returns failure rather than inventing success.

The current implementation deliberately does not claim or submit a bounty automatically. Claiming can carry platform terms or identity/payout requirements, so that action stays outside the reasoning engine.

## Why this is useful

A transformer can be attached as a candidate generator without granting it final authority. For coding, compilers, unit tests, repository behavior, and acceptance tests provide reality-contact. For science, adapters can use simulations, instruments, datasets, or theorem provers. For research, search/retrieval can be treated as inquiry whose result updates the live space.

## Run the demos and tests

```bash
python -m solver.demo
python -m unittest solver.test_solver -v
python -m unittest solver.coding.test_coding -v
```

## Security

Never put API keys, payout details, bank information, private identity documents, or personal contact data in this repository. Provider credentials should be injected at runtime through a secret manager or environment variables.

The coding solver executes target-repository verification commands. A repository's test suite is code execution. Use a disposable VM/container for untrusted repositories. The CLI refuses to run tests unless `--allow-local-exec` is supplied.
