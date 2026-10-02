from __future__ import annotations

import argparse
import json
import shlex
import sys
import tempfile
from pathlib import Path

from .engine import CodingOneLogicSolver
from .generator import JsonCommandGenerator
from .github_source import fetch_public_issue, problem_from_issue
from .workspace import GitWorkspace


def _command(value: str) -> tuple[str, ...]:
    parts = tuple(shlex.split(value))
    if not parts:
        raise argparse.ArgumentTypeError("command cannot be empty")
    return parts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Attempt a public GitHub issue with the OneLogic coding controller."
    )
    parser.add_argument("issue_url", help="Public GitHub issue URL")
    parser.add_argument(
        "--generator",
        required=True,
        type=_command,
        help=(
            "External proposal-generator argv as one quoted string. It receives the "
            "onelogic.patch-generator.v1 JSON protocol on stdin."
        ),
    )
    parser.add_argument(
        "--test",
        action="append",
        type=_command,
        required=True,
        help="Verification argv, repeatable. Shell operators are intentionally unsupported.",
    )
    parser.add_argument("--rounds", type=int, default=6)
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--output", type=Path, default=Path("solution.patch"))
    parser.add_argument(
        "--allow-local-exec",
        action="store_true",
        help=(
            "Required safety acknowledgement. Target repository tests execute local code. "
            "Use a disposable VM/container for repositories you do not trust."
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.allow_local_exec:
        print(
            "Refusing to execute target-repository code without --allow-local-exec. "
            "Use a disposable VM/container for untrusted repositories.",
            file=sys.stderr,
        )
        return 2

    issue = fetch_public_issue(args.issue_url)
    problem = problem_from_issue(issue, tuple(args.test))

    with tempfile.TemporaryDirectory(prefix="onelogic-coding-") as tmp:
        workspace_path = Path(tmp) / "target"
        workspace = GitWorkspace.clone(
            problem.repo_url,
            workspace_path,
            ref=problem.base_ref,
        )
        solver = CodingOneLogicSolver(
            workspace=workspace,
            generator=JsonCommandGenerator(args.generator),
            problem=problem,
            max_rounds=args.rounds,
            verification_timeout_seconds=args.timeout,
        )
        result = solver.solve()

        summary = {
            "status": result.status,
            "issue": problem.issue_url,
            "reward_text": problem.reward_text,
            "winning_proposal_id": result.winning_proposal_id,
            "changed_lines": result.changed_lines,
            "rounds": len(result.trace.rounds),
            "message": result.message,
        }
        print(json.dumps(summary, indent=2))

        if result.patch is not None:
            args.output.write_text(result.patch, encoding="utf-8")
            print(f"wrote verified patch: {args.output}")
            return 0

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
