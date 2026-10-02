# Revenue target intake

Public bounty scanners frequently confuse an advertised reward with money that is actually obtainable. OneLogic therefore treats target selection itself as a reality-tracking problem.

A target is not admitted merely because another scanner says "$50 bounty." The current source must establish the reward, payout route, availability, acceptance boundary, and any assignment, competition, infrastructure, or hardware constraints.

The intake layer uses hard gates rather than one opaque score. A $3,000 task assigned to someone else is not made preferable by multiplying the dollar amount by a confidence percentage.

Current statuses: `verified_cash_near`, `needs_claim`, `payment_unverified`, `availability_unverified`, `competed`, `requires_paid_infra`, `requires_special_hardware`, `stale_or_closed`, and `unsuitable`.

The intended pipeline is:

`discovery lead -> source refresh -> evidence object -> intake decision -> coding solver -> verified patch -> human-authorized claim/submission`

Claiming a bounty, accepting platform terms, identity verification, and payout onboarding stay outside the autonomous solver unless the operator explicitly authorizes that action.
