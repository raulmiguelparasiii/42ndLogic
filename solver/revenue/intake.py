from __future__ import annotations

from .models import Evidence, TargetDecision, TargetStatus


def evaluate_target(e: Evidence) -> TargetDecision:
    """Classify a money target from source-level evidence.

    Hard blockers stay distinct because a large advertised reward cannot compensate
    for a closed task, absent payment evidence, somebody else's assignment, unavailable
    hardware, or paid infrastructure the operator has not authorized.
    """
    blockers: list[str] = []
    warnings: list[str] = []

    if not e.source_open or not e.source_fresh:
        blockers.append("source is closed, stale, or no longer current")
        return TargetDecision(
            TargetStatus.STALE_OR_CLOSED, False, False, tuple(blockers), (), e
        )

    if not e.payment_explicit or e.reward_amount is None or not e.reward_currency:
        blockers.append("source does not establish an explicit reward")
        return TargetDecision(
            TargetStatus.PAYMENT_UNVERIFIED, False, False, tuple(blockers), (), e
        )

    if not e.payout_path_explicit:
        blockers.append("payout mechanism or recipient eligibility is not established")
        return TargetDecision(
            TargetStatus.PAYMENT_UNVERIFIED, False, False, tuple(blockers), (), e
        )

    if not e.acceptance_criteria_explicit:
        blockers.append("acceptance boundary is underspecified")
        return TargetDecision(
            TargetStatus.UNSUITABLE, False, False, tuple(blockers), (), e
        )

    if e.assigned_to_other:
        blockers.append("source assigns the work to another contributor")
        return TargetDecision(
            TargetStatus.COMPETED, False, False, tuple(blockers), (), e
        )

    if e.requires_paid_infra:
        blockers.append("attempt requires paid infrastructure before payout")
        return TargetDecision(
            TargetStatus.REQUIRES_PAID_INFRA, False, False, tuple(blockers), (), e
        )

    if e.requires_special_hardware:
        blockers.append("acceptance requires hardware not available to the solver")
        return TargetDecision(
            TargetStatus.REQUIRES_SPECIAL_HARDWARE, False, False, tuple(blockers), (), e
        )

    if not e.local_verification_possible:
        warnings.append("full acceptance cannot be reproduced locally")

    if e.active_competing_implementations:
        warnings.append(
            f"{e.active_competing_implementations} active competing implementation(s) observed"
        )

    if e.assignment_required:
        blockers.append("assignment/claim must be obtained before work counts")
        return TargetDecision(
            TargetStatus.NEEDS_CLAIM,
            True,
            False,
            tuple(blockers),
            tuple(warnings),
            e,
        )

    if e.active_competing_implementations:
        return TargetDecision(
            TargetStatus.COMPETED,
            True,
            True,
            (),
            tuple(warnings),
            e,
        )

    return TargetDecision(
        TargetStatus.VERIFIED_CASH_NEAR,
        True,
        True,
        (),
        tuple(warnings),
        e,
    )
