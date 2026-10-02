from __future__ import annotations

import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .models import CommandResult


class WorkspaceError(RuntimeError):
    pass


@dataclass
class GitWorkspace:
    path: Path

    MARKER = ".onelogic-workspace"

    @classmethod
    def clone(cls, repo_url: str, destination: Path, *, ref: str | None = None) -> "GitWorkspace":
        destination = destination.resolve()
        if destination.exists():
            raise WorkspaceError(f"destination already exists: {destination}")
        args = [
            "git",
            "-c",
            "core.hooksPath=/dev/null",
            "-c",
            "filter.lfs.smudge=cat",
            "-c",
            "filter.lfs.required=false",
            "clone",
            "--depth",
            "1",
            "--no-recurse-submodules",
        ]
        if ref:
            args += ["--branch", ref]
        args += [repo_url, str(destination)]
        completed = subprocess.run(args, text=True, capture_output=True, check=False)
        if completed.returncode != 0:
            raise WorkspaceError(f"git clone failed: {completed.stderr[-4000:]}")
        workspace = cls(destination)
        workspace._run_git(["config", "core.hooksPath", "/dev/null"])
        (destination / cls.MARKER).write_text("OneLogic disposable coding workspace\n", encoding="utf-8")
        return workspace

    def _assert_safe(self) -> None:
        path = self.path.resolve()
        if path == Path(path.anchor) or path == Path.home().resolve():
            raise WorkspaceError(f"refusing unsafe workspace path: {path}")
        if not (path / ".git").exists() or not (path / self.MARKER).exists():
            raise WorkspaceError("workspace marker or .git directory missing")

    def _run_git(
        self,
        args: Sequence[str],
        *,
        input_text: str | None = None,
        timeout: float = 60.0,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.path,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )

    def reset(self) -> None:
        self._assert_safe()
        reset = self._run_git(["reset", "--hard", "HEAD"])
        if reset.returncode != 0:
            raise WorkspaceError(reset.stderr[-4000:])
        clean = self._run_git(["clean", "-fdx", "-e", self.MARKER])
        if clean.returncode != 0:
            raise WorkspaceError(clean.stderr[-4000:])
        if not (self.path / self.MARKER).exists():
            (self.path / self.MARKER).write_text("OneLogic disposable coding workspace\n", encoding="utf-8")

    def apply_patch(self, diff: str) -> tuple[bool, str | None]:
        self._assert_safe()
        completed = self._run_git(
            ["apply", "--whitespace=nowarn", "-"],
            input_text=diff,
        )
        if completed.returncode != 0:
            return False, (completed.stderr or completed.stdout)[-6000:]
        return True, None

    def current_diff(self) -> str:
        self._assert_safe()
        completed = self._run_git(["diff", "--binary", "--no-ext-diff"])
        if completed.returncode != 0:
            raise WorkspaceError(completed.stderr[-4000:])
        return completed.stdout

    def changed_lines(self) -> int:
        self._assert_safe()
        completed = self._run_git(["diff", "--numstat", "--no-ext-diff"])
        if completed.returncode != 0:
            raise WorkspaceError(completed.stderr[-4000:])
        total = 0
        for line in completed.stdout.splitlines():
            parts = line.split("\t", 2)
            if len(parts) < 2:
                continue
            for value in parts[:2]:
                try:
                    total += int(value)
                except ValueError:
                    total += 1
        return total

    def run_verification(self, command: Sequence[str], *, timeout: float = 180.0) -> CommandResult:
        """Run one explicit argv command in the disposable workspace.

        This executes target-repository code. Callers must opt in at the CLI layer and
        should use an OS/container sandbox for untrusted repositories.
        """
        self._assert_safe()
        if not command:
            raise WorkspaceError("empty verification command")
        started = time.monotonic()
        env = os.environ.copy()
        env["ONELOGIC_WORKSPACE"] = str(self.path)
        try:
            completed = subprocess.run(
                list(command),
                cwd=self.path,
                text=True,
                capture_output=True,
                timeout=timeout,
                check=False,
                env=env,
            )
            rc, out, err = completed.returncode, completed.stdout, completed.stderr
        except subprocess.TimeoutExpired as exc:
            rc = 124
            out = exc.stdout or ""
            err = (exc.stderr or "") + f"\nOneLogic timeout after {timeout:.1f}s"
        return CommandResult(
            command=tuple(command),
            returncode=rc,
            stdout=out[-12000:],
            stderr=err[-12000:],
            duration_seconds=time.monotonic() - started,
        )
