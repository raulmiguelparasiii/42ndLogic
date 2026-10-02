# Platform adapters

Platform adapters exist so the operator does not have to learn each bounty platform before OneLogic can use it.

The adapter separates routine automation from account-holder-only actions.

Routine work can proceed without interruption when supported by connected tools: public-source verification, repository inspection, candidate generation, tests, patch preparation, ordinary GitHub comments that do not themselves accept separate terms, and preparation of a pull request.

The operator is interrupted only when current platform facts require an account-holder action, such as:

- first-time account or payout onboarding;
- identity or tax verification;
- accepting bounty/program terms when the claim itself is binding;
- a wallet signature;
- spending money, gas, a deposit, or a bond;
- a claim/submission flow that available connected tools cannot execute.

One-time setup is classified separately from per-bounty approval. Once a payout provider has been legitimately configured, OneLogic should not ask for the same setup again unless the provider itself requires it.

## Notification

The default notification sink is a single GitHub issue in 42ndLogic titled `[ACTION REQUIRED] ...`, assigned to the operator. Routine progress does not notify the operator.

The notification transport deduplicates open notices by target/action key. GitHub then delivers web, push, or email notification according to the operator's own GitHub notification settings.

The issue must never contain banking details, tax identifiers, identity documents, API keys, wallet secrets, or other credentials.
