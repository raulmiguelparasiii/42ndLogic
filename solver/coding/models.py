from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Sequence


@dataclass(frozen=True)
class ProblemSpec:
    repo_url: str
    issue_url: str
    title: str
    body: str
    verification_commands: tuple[tuple[str, ...], ...]
    base_ref: str | None = None
    reward_text: str | None = None

    def as_prompt_payload(self) -> dict[str, Any]:
        return {
            "repo_url": self.repo_url,
            "issue_url": self.issue_url,
            "title": self.title,
            "body": self.body,
            "verification_commands": [list(c) for c in self.verification_commands],
            "base_ref": self.base_ref,
            "reward_text": self.reward_text,
        }


@dataclass(frozen=True)
class PatchProposal:
    id: str
    diff: str
    rationale: str = ""


@dataclass(frozen=True)
class CommandResult:
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    duration_seconds: float

    @property
    def passed(self) -> bool:
        return self.returncode == 0


@dataclass(frozen=True)
class ProposalResult:
    proposal: PatchProposal
    applied: bool
    apply_error: str | None
    verification: tuple[CommandResult, ...]
    changed_lines: int | None
    resulting_diff: str | None

    @property
    def passed(self) -> bool:
        return self.applied and bool(self.verification) and all(x.passed for x in self.verification)


@dataclass
class RoundRecord:
    number: int
    proposals: list[ProposalResult] = field(default_factory=list)


@dataclass
class CodingTrace:
    rounds: list[RoundRecord] = field(default_factory=list)

    def feedback(self, *, max_chars: int = 14000) -> str:
        chunks: list[str] = []
        for round_record in self.rounds[-2:]:
            chunks.append(f"ROUND {round_record.number}")
            for result in round_record.proposals:
                chunks.append(f"candidate={result.proposal.id} applied={result.applied} passed={result.passed}")
                if result.apply_error:
                    chunks.append("apply_error=" + result.apply_error[-2000:])
                for check in result.verification:
                    chunks.append(
                        "command="
                        + " ".join(check.command)
                        + f" rc={check.returncode}\nstdout:\n{check.stdout[-2500:]}\nstderr:\n{check.stderr[-2500:]}"
                    )
        text = "\n\n".join(chunks)
        return text[-max_chars:]


@dataclass(frozen=True)
class CodingSolveResult:
    status: str
    winning_proposal_id: str | None
    patch: str | None
    changed_lines: int | None
    trace: CodingTrace
    message: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        return data
