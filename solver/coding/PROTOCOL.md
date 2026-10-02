# Patch generator protocol v1

The coding controller deliberately does not hard-code a model provider. Any LLM, local model, program synthesizer, human-in-the-loop script, or future OneLogic generator can participate by implementing one JSON stdin/stdout protocol.

The controller sends a JSON object with protocol `onelogic.patch-generator.v1`, the public issue/repository context, declared verification commands, prior failure evidence, and generation requirements.

The generator returns a JSON object with a `proposals` array. Each proposal contains an `id`, a unified git `diff`, and an optional `rationale`.

The generator's rationale is never accepted as proof. Each patch is reset onto the same clean repository state, applied, and tested against the declared verification commands. Failed patches are eliminated. Failure output becomes evidence for the next expansion round.

If multiple patches survive all checks, the current proof-of-concept chooses the smallest changed-line count as a conservative engineering tie-break. That tie-break is an optimization policy, not a theorem of strict consequence.

## Security boundary

The controller never invokes a shell for generator or verification commands. Nevertheless, executing a repository's test suite executes repository code. Run money-target attempts inside a disposable VM or container unless the target repository is trusted.
