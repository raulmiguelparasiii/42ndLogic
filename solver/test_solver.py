import unittest

from solver.agent import (
    Candidate,
    Inquiry,
    OneLogicSolver,
    StaticGenerator,
    TableReality,
    UNKNOWN,
    exact_update,
    forced_answer,
)


class SolverTests(unittest.TestCase):
    def test_exact_update_keeps_undefined(self):
        live = [
            Candidate("a", 1, {"q": "yes"}),
            Candidate("b", 2, {}),
            Candidate("c", 3, {"q": "no"}),
        ]
        survivors = exact_update(live, Inquiry("q"), "yes")
        self.assertEqual([c.id for c in survivors], ["a", "b"])

    def test_forced_answer(self):
        live = [
            Candidate("a", "x", {}),
            Candidate("b", "x", {}),
        ]
        self.assertEqual(forced_answer(live), "x")
        self.assertIs(forced_answer([Candidate("a", "x", {}), Candidate("b", "y", {})]), UNKNOWN)

    def test_solver_identifies_answer(self):
        candidates = [
            Candidate("h1", "A", {"x": 0, "y": 0}),
            Candidate("h2", "B", {"x": 1, "y": 0}),
            Candidate("h3", "C", {"x": 1, "y": 1}),
        ]
        solver = OneLogicSolver(
            StaticGenerator(candidates),
            TableReality({"x": 1, "y": 1}),
            [Inquiry("x"), Inquiry("y")],
        )
        result = solver.solve("demo")
        self.assertEqual(result.status, "forced")
        self.assertEqual(result.answer, "C")
        self.assertEqual(result.live_candidate_ids, ("h3",))

    def test_non_identifiable_is_not_guessed(self):
        candidates = [
            Candidate("h1", "A", {"x": 0}),
            Candidate("h2", "B", {"x": 0}),
        ]
        solver = OneLogicSolver(
            StaticGenerator(candidates),
            TableReality({"x": 0}),
            [Inquiry("x")],
        )
        result = solver.solve("demo")
        self.assertEqual(result.status, "non_identifiable")
        self.assertIsNone(result.answer)


if __name__ == "__main__":
    unittest.main()
