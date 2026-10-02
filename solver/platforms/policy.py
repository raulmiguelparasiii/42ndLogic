from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ActionClass(str, Enum):
    AUTO = "auto"
    HUMAN_ONCE = "human_once"
    HUMAN_PER_ACTION = "human_per_action"


@dataclass(frozen=True)
class OperatorAction:
    id: str
    description: str
    action_class: ActionClass
    reason: str
    url: str | None = None


@dataclass(frozen=True)
class PlatformFacts:
    platform: str
    source_url: str
    can_claim_via_connected_github: bool = False
    claim_text: str | None = None
    claim_requires_assignment: bool = False
    claim_accepts_program_terms: bool = False
    account_onboarding_required: bool = False
    payout_onboarding_required: bool = False
    identity_verification_required: bool = False
    wallet_signature_required: bool = False
    spend_or_bond_required: bool = False
    submission_via_github_pr: bool = True
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class PlatformPlan:
    platform: str
    auto_actions: tuple[OperatorAction, ...]
    human_actions: tuple[OperatorAction, ...]

    @property
    def can_continue_without_interrupting_user(self) -> bool:
        return not self.human_actions


def plan_platform_actions(f: PlatformFacts) -> PlatformPlan:
    """Return the smallest human-interruption boundary justified by platform facts.

    Routine public GitHub operations may be automated when the connected account can
    perform them and no separate terms/financial authorization is implicated.

    Legal/financial identity actions stay with the account holder.
    """
    auto: list[OperatorAction] = []
    human: list[OperatorAction] = []

    if f.account_onboarding_required:
        human.append(
            OperatorAction(
                "account_onboarding",
                f"Complete one-time {f.platform} account onboarding.",
                ActionClass.HUMAN_ONCE,
                "The platform requires an account-holder action that the solver cannot safely impersonate.",
                f.source_url,
            )
        )

    if f.payout_onboarding_required:
        human.append(
            OperatorAction(
                "payout_onboarding",
                f"Connect or configure the payout method for {f.platform}.",
                ActionClass.HUMAN_ONCE,
                "Payout credentials and banking/payment details remain with the account holder.",
                f.source_url,
            )
        )

    if f.identity_verification_required:
        human.append(
            OperatorAction(
                "identity_verification",
                f"Complete identity/tax verification required by {f.platform}.",
                ActionClass.HUMAN_ONCE,
                "Identity and tax attestations require the account holder.",
                f.source_url,
            )
        )

    if f.wallet_signature_required:
        human.append(
            OperatorAction(
                "wallet_signature",
                "Approve the required wallet signature.",
                ActionClass.HUMAN_PER_ACTION,
                "The solver must never sign with or request private wallet credentials.",
                f.source_url,
            )
        )

    if f.spend_or_bond_required:
        human.append(
            OperatorAction(
                "spend_or_bond",
                "Approve the required spend, gas, deposit, or bond.",
                ActionClass.HUMAN_PER_ACTION,
                "Moving or risking funds requires explicit account-holder authorization.",
                f.source_url,
            )
        )

    if f.claim_accepts_program_terms:
        human.append(
            OperatorAction(
                "claim_terms",
                "Approve participation in the bounty/program terms for this claim.",
                ActionClass.HUMAN_PER_ACTION,
                "The claim itself binds the account to program terms.",
                f.source_url,
            )
        )
    elif f.claim_requires_assignment:
        if f.can_claim_via_connected_github and f.claim_text:
            auto.append(
                OperatorAction(
                    "request_assignment",
                    f"Post the required GitHub assignment/claim request: {f.claim_text}",
                    ActionClass.AUTO,
                    "This is a routine public GitHub operation and no separate binding terms are represented.",
                    f.source_url,
                )
            )
        else:
            human.append(
                OperatorAction(
                    "request_assignment",
                    "Request assignment/claim using the platform's required account flow.",
                    ActionClass.HUMAN_PER_ACTION,
                    "The available connected tools cannot complete the required claim flow.",
                    f.source_url,
                )
            )
    elif f.can_claim_via_connected_github and f.claim_text:
        auto.append(
            OperatorAction(
                "claim",
                f"Post the GitHub claim: {f.claim_text}",
                ActionClass.AUTO,
                "The represented claim is a routine public GitHub action with no additional terms gate.",
                f.source_url,
            )
        )

    if f.submission_via_github_pr:
        auto.append(
            OperatorAction(
                "prepare_submission",
                "Prepare the verified GitHub pull request and required claim text.",
                ActionClass.AUTO,
                "Technical submission can be prepared from the verified patch through the connected GitHub account.",
                f.source_url,
            )
        )

    return PlatformPlan(f.platform, tuple(auto), tuple(human))
