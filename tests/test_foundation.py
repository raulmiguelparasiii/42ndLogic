import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "formal"))
from one_logic.core import *
from one_logic.falsifier import run

class FoundationTests(unittest.TestCase):
    def test_invariance(self):
        q = Query("q", {0: 1, 1: 1, 2: 0})
        self.assertEqual(categorical_consequences({0,1}, [q]), frozenset({Assertion("q",1)}))
        self.assertEqual(categorical_consequences({0,2}, [q]), frozenset())

    def test_sharp_update(self):
        t = {Transition(0,"o",2), Transition(1,"o",3)}
        self.assertEqual(sharp_update({0,1},"o",t), frozenset({2,3}))
        self.assertTrue(update_is_sound({0,1},"o",t,{2,3,4}))
        self.assertFalse(update_is_sound({0,1},"o",t,{2}))

    def test_deviation(self):
        d = deviation_from_ideal({1,2},{2,3})
        self.assertEqual(d.unsupported_exclusion, frozenset({1}))
        self.assertEqual(d.unsupported_retention, frozenset({3}))

    def test_bridge_counterexample(self):
        personal = Query("dishonest", {0: True, 1: True})
        theorem = Query("theorem", {0: True, 1: False})
        self.assertFalse(bridge_valid({0,1}, personal, True, theorem, False))

    def test_falsifier(self):
        report = run(max_worlds=4)
        self.assertEqual(report.failures, [])

if __name__ == "__main__":
    unittest.main()
