from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from solver.coding.engine import CodingOneLogicSolver
from solver.coding.generator import StaticPatchGenerator
from solver.coding.github_source import parse_issue_url
from solver.coding.models import PatchProposal, ProblemSpec
from solver.coding.workspace import GitWorkspace


GOOD_PATCH = """diff --git a/calc.py b/calc.py
--- a/calc.py
+++ b/calc.py
@@ -1,2 +1,2 @@
 def add(a, b):
-    return a - b
+    return a + b
"""

BAD_PATCH = """diff --git a/calc.py b/calc.py
--- a/calc.py
+++ b/calc.py
@@ -1,2 +1,2 @@
 def add(a, b):
-    return a - b
+    return a * b
"""


def make_repo(root: Path) -> Path:
    repo = root / "source"
    repo.mkdir()
    (repo / "calc.py").write_text("def add(a, b):\n    return a - b\n", encoding="utf-8")
    tests = repo / "tests"
    tests.mkdir()
    (tests / "test_calc.py").write_text(
        "import unittest\n"
        "from calc import add\n\n"
        "class CalcTests(unittest.TestCase):\n"
        "    def test_add(self):\n"
        "        self.assertEqual(add(2, 3), 5)\n\n"
        "if __name__ == '__main__':\n"
        "    unittest.main()\n",
        encoding="utf-8",
    )
    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "OneLogic Test"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "broken baseline"], cwd=repo, check=True, capture_output=True)
    return repo


class CodingSolverTests(unittest.TestCase):
    def test_issue_url_parser(self):
        self.assertEqual(
            parse_issue_url("https://github.com/owner/repo/issues/42"),
            ("owner", "repo", 42),
        )
        with self.assertRaises(ValueError):
            parse_issue_url("https://example.com/owner/repo/issues/42")

    def test_bad_candidate_is_eliminated_and_good_candidate_survives(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = make_repo(root)
            workspace = GitWorkspace.clone(str(source), root / "work")
            problem = ProblemSpec(
                repo_url=str(source),
                issue_url="https://github.com/example/example/issues/1",
                title="add() subtracts",
                body="add(2, 3) should be 5",
                verification_commands=((sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"),),
            )
            generator = StaticPatchGenerator(
                [[
                    PatchProposal("multiply", BAD_PATCH, "wrong hypothesis"),
                    PatchProposal("add", GOOD_PATCH, "repair operator"),
                ]]
            )
            result = CodingOneLogicSolver(workspace, generator, problem).solve()
            self.assertEqual(result.status, "verified")
            self.assertEqual(result.winning_proposal_id, "add")
            self.assertIn("return a + b", result.patch or "")
            self.assertEqual(len(result.trace.rounds), 1)
            self.assertEqual(len(result.trace.rounds[0].proposals), 2)
            failures = [p for p in result.trace.rounds[0].proposals if not p.passed]
            self.assertEqual([p.proposal.id for p in failures], ["multiply"])

    def test_failure_evidence_drives_expansion_round(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = make_repo(root)
            workspace = GitWorkspace.clone(str(source), root / "work")
            problem = ProblemSpec(
                repo_url=str(source),
                issue_url="https://github.com/example/example/issues/1",
                title="add() subtracts",
                body="add(2, 3) should be 5",
                verification_commands=((sys.executable, "-m", "unittest", "discover", "-s", "tests"),),
            )
            generator = StaticPatchGenerator([
                [PatchProposal("wrong-first", BAD_PATCH)],
                [PatchProposal("correct-after-evidence", GOOD_PATCH)],
            ])
            result = CodingOneLogicSolver(workspace, generator, problem, max_rounds=2).solve()
            self.assertEqual(result.status, "verified")
            self.assertEqual(result.winning_proposal_id, "correct-after-evidence")
            self.assertEqual(len(result.trace.rounds), 2)
            self.assertIn("wrong-first", result.trace.feedback())

    def test_solver_does_not_claim_success_when_every_patch_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = make_repo(root)
            workspace = GitWorkspace.clone(str(source), root / "work")
            problem = ProblemSpec(
                repo_url=str(source),
                issue_url="https://github.com/example/example/issues/1",
                title="add() subtracts",
                body="add(2, 3) should be 5",
                verification_commands=((sys.executable, "-m", "unittest", "discover", "-s", "tests"),),
            )
            generator = StaticPatchGenerator([[PatchProposal("wrong", BAD_PATCH)]])
            result = CodingOneLogicSolver(workspace, generator, problem, max_rounds=2).solve()
            self.assertEqual(result.status, "generator_empty")
            self.assertIsNone(result.patch)


if __name__ == "__main__":
    unittest.main()
