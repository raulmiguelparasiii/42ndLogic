from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from typing import Protocol, Sequence

from .models import CodingTrace, PatchProposal, ProblemSpec


class PatchGenerator(Protocol):
    def generate(self, problem: ProblemSpec, trace: CodingTrace) -> Sequence[PatchProposal]:
        ...


class StaticPatchGenerator:
    """Deterministic generator for tests and reproducible experiments."""

    def __init__(self, rounds: Sequence[Sequence[PatchProposal]]):
        self.rounds = [list(x) for x in rounds]
        self.index = 0

    def generate(self, problem: ProblemSpec, trace: CodingTrace) -> Sequence[PatchProposal]:
        if self.index >= len(self.rounds):
            return []
        result = self.rounds[self.index]
        self.index += 1
        return list(result)


@dataclass
class JsonCommandGenerator:
    """Use any external model/agent command through a small JSON protocol.

    The executable receives one JSON object on stdin and must return:

      {"proposals": [{"id": "...", "diff": "...", "rationale": "..."}]}

    No shell is used. The external program is a proposal generator only; its patches
    still have to survive repository verification.
    """

    command: tuple[str, ...]
    timeout_seconds: float = 180.0
    max_proposals: int = 8

    def generate(self, problem: ProblemSpec, trace: CodingTrace) -> Sequence[PatchProposal]:
        payload = {
            "protocol": "onelogic.patch-generator.v1",
            "problem": problem.as_prompt_payload(),
            "feedback": trace.feedback(),
            "requirements": [
                "Return unified git patches only.",
                "Do not weaken or delete acceptance tests merely to obtain a pass.",
                "Prefer the smallest patch that addresses the issue.",
                "If prior attempts failed, use the supplied failure evidence to revise the model.",
            ],
        }
        completed = subprocess.run(
            list(self.command),
            input=json.dumps(payload),
            text=True,
            capture_output=True,
            timeout=self.timeout_seconds,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                "generator command failed "
                f"(rc={completed.returncode}): {completed.stderr[-4000:]}"
            )
        try:
            decoded = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("generator did not return valid JSON") from exc
        raw = decoded.get("proposals")
        if not isinstance(raw, list):
            raise RuntimeError("generator JSON must contain a proposals array")

        proposals: list[PatchProposal] = []
        for item in raw[: self.max_proposals]:
            if not isinstance(item, dict):
                continue
            pid = item.get("id")
            diff = item.get("diff")
            if not isinstance(pid, str) or not pid.strip() or not isinstance(diff, str) or not diff.strip():
                continue
            proposals.append(
                PatchProposal(
                    id=pid.strip(),
                    diff=diff,
                    rationale=str(item.get("rationale") or ""),
                )
            )
        return proposals
