from __future__ import annotations

from dataclasses import dataclass

from .generator import PatchGenerator
from .models import CodingSolveResult, CodingTrace, ProblemSpec, ProposalResult, RoundRecord
from .workspace import GitWorkspace


@dataclass
class CodingOneLogicSolver:
    """Reality-controlled patch search.

    Candidate patches are proposals. Repository verification is reality-contact.
    A patch is accepted only when every declared verification command succeeds.

    If multiple patches survive, choosing the smallest diff is an optimization policy,
    not an additional truth claim.
    """

    workspace: GitWorkspace
    generator: PatchGenerator
    problem: ProblemSpec
    max_rounds: int = 6
    verification_timeout_seconds: float = 180.0

    def solve(self) -> CodingSolveResult:
        trace = CodingTrace()

        for round_number in range(1, self.max_rounds + 1):
            proposals = list(self.generator.generate(self.problem, trace))
            if not proposals:
                return CodingSolveResult(
                    status="generator_empty",
                    winning_proposal_id=None,
                    patch=None,
                    changed_lines=None,
                    trace=trace,
                    message="No candidate patches were generated.",
                )

            record = RoundRecord(number=round_number)
            passed: list[ProposalResult] = []

            for proposal in proposals:
                self.workspace.reset()
                applied, apply_error = self.workspace.apply_patch(proposal.diff)
                if not applied:
                    result = ProposalResult(
                        proposal=proposal,
                        applied=False,
                        apply_error=apply_error,
                        verification=(),
                        changed_lines=None,
                        resulting_diff=None,
                    )
                    record.proposals.append(result)
                    continue

                checks = []
                for command in self.problem.verification_commands:
                    check = self.workspace.run_verification(
                        command,
                        timeout=self.verification_timeout_seconds,
                    )
                    checks.append(check)
                    if not check.passed:
                        break

                result = ProposalResult(
                    proposal=proposal,
                    applied=True,
                    apply_error=None,
                    verification=tuple(checks),
                    changed_lines=self.workspace.changed_lines(),
                    resulting_diff=self.workspace.current_diff(),
                )
                record.proposals.append(result)
                if result.passed:
                    passed.append(result)

            trace.rounds.append(record)

            if passed:
                passed.sort(
                    key=lambda r: (
                        r.changed_lines if r.changed_lines is not None else 10**18,
                        r.proposal.id,
                    )
                )
                winner = passed[0]
                self.workspace.reset()
                applied, error = self.workspace.apply_patch(winner.proposal.diff)
                if not applied:
                    return CodingSolveResult(
                        status="internal_error",
                        winning_proposal_id=None,
                        patch=None,
                        changed_lines=None,
                        trace=trace,
                        message=f"Winning patch could not be reapplied: {error}",
                    )
                canonical_diff = self.workspace.current_diff()
                return CodingSolveResult(
                    status="verified",
                    winning_proposal_id=winner.proposal.id,
                    patch=canonical_diff,
                    changed_lines=self.workspace.changed_lines(),
                    trace=trace,
                    message=(
                        "At least one candidate survived every declared verification command. "
                        "The returned patch is the smallest surviving diff by changed-line count."
                    ),
                )

        return CodingSolveResult(
            status="budget_exhausted",
            winning_proposal_id=None,
            patch=None,
            changed_lines=None,
            trace=trace,
            message="No candidate survived before the configured round budget was exhausted.",
        )
