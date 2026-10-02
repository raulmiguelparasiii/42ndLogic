from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TargetStatus(str, Enum):
    VERIFIED_CASH_NEAR = "verified_cash_near"
    NEEDS_CLAIM = "needs_claim"
    PAYMENT_UNVERIFIED = "payment_unverified"
    AVAILABILITY_UNVERIFIED = "availability_unverified"
    COMPETED = "competed"
    REQUIRES_PAID_INFRA = "requires_paid_infra"
    REQUIRES_SPECIAL_HARDWARE = "requires_special_hardware"
    STALE_OR_CLOSED = "stale_or_closed"
    UNSUITABLE = "unsuitable"


@dataclass(frozen=True)
class Evidence:
    source_url: str
    source_open: bool
    reward_amount: float | None
    reward_currency: str | None
    payment_explicit: bool
    payout_path_explicit: bool
    acceptance_criteria_explicit: bool
    assignment_required: bool = False
    assigned_to_other: bool = False
    active_competing_implementations: int = 0
    requires_paid_infra: bool = False
    requires_special_hardware: bool = False
    local_verification_possible: bool = True
    source_fresh: bool = True
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class TargetDecision:
    status: TargetStatus
    economically_live: bool
    solve_before_claim: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]
    evidence: Evidence
