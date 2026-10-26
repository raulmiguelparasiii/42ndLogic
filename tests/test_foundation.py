import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "formal"))
from one_logic.core import *
from one_logic.falsifier import run


class FoundationTests(unittest.TestCase):
    def test_invariance(self):
        q = Query("q", {0: 1, 1: 1, 2: 0})
        self.assertEqual(categorical_consequences({0, 1}, [q]), frozenset({Assertion("q", 1)}))
        self.assertEqual(categorical_consequences({0, 2}, [q]), frozenset())

    def test_sharp_update(self):
        t = {Transition(0, "o", 2), Transition(1, "o", 3)}
        self.assertEqual(sharp_update({0, 1}, "o", t), frozenset({2, 3}))
        self.assertTrue(update_is_sound({0, 1}, "o", t, {2, 3, 4}))
        self.assertFalse(update_is_sound({0, 1}, "o", t, {2}))

    def test_deviation(self):
        d = deviation_from_ideal({1, 2}, {2, 3})
        self.assertEqual(d.unsupported_exclusion, frozenset({1}))
        self.assertEqual(d.unsupported_retention, frozenset({3}))

    def test_bridge_counterexample(self):
        personal = Query("dishonest", {0: True, 1: True})
        theorem = Query("theorem", {0: True, 1: False})
        self.assertFalse(bridge_valid({0, 1}, personal, True, theorem, False))

    def test_assumed_ignorance_is_generic_bridge_overreach(self):
        # Same premise is compatible with either having considered the objection
        # or not having considered it.  No debate-specific rule is needed.
        premise = Query("premise_given", {0: True, 1: True})
        considered = Query("considered_x", {0: True, 1: False})
        d = bridge_deviation({0, 1}, premise, True, considered, False)
        self.assertEqual(d.counterexamples, frozenset({0}))
        self.assertFalse(d.categorical)
        self.assertEqual(bridge_deviation_magnitude(d, {0: 1.0, 1: 1.0}), 0.5)

    def test_material_loss_is_exposed_not_named(self):
        welfare = Query("affected_state", {0: "harmed", 1: "safe"})
        representation = {0: "same", 1: "same"}
        losses = material_representation_losses({0, 1}, [welfare], representation)
        self.assertEqual(losses, frozenset({MaterialLoss(0, 1, "affected_state")}))
        self.assertFalse(representation_preserves_material_distinctions({0, 1}, [welfare], representation))

    def test_provisional_support_does_not_settle(self):
        q = Query("q", {0: True, 1: False})
        support = SupportOrder({0: 10.0, 1: 1.0})
        j = judge_query({0, 1}, q, support)
        self.assertEqual(j.status, "provisional")
        self.assertEqual(j.assertion, Assertion("q", True))
        self.assertEqual(categorical_consequences({0, 1}, [q]), frozenset())

    def test_correction_debt_is_generic(self):
        corrections = [
            CorrectionOpportunity("clarify-a", "speaker-model", integrated=False),
            CorrectionOpportunity("clarify-b", "speaker-model", integrated=True),
            CorrectionOpportunity("irrelevant", "other", material=False, integrated=False),
        ]
        self.assertEqual(correction_debt(corrections), frozenset({"clarify-a"}))

    def test_deviation_signature_composes_without_fallacy_names(self):
        premise = Query("p", {0: True, 1: True})
        conclusion = Query("latent", {0: True, 1: False})
        bridge = bridge_deviation({0, 1}, premise, True, conclusion, True)
        q = Query("material", {0: 0, 1: 1})
        losses = material_representation_losses({0, 1}, [q], {0: "x", 1: "x"})
        sig = deviation_signature(
            ideal={"nuanced"},
            proposed={"caricature"},
            bridges=[bridge],
            material_losses=losses,
            corrections=[CorrectionOpportunity("c", "frame", integrated=False)],
        )
        self.assertFalse(sig.exact)
        self.assertEqual(sig.unsupported_exclusion, frozenset({"nuanced"}))
        self.assertEqual(sig.unsupported_retention, frozenset({"caricature"}))
        self.assertTrue(sig.bridge_defects)
        self.assertTrue(sig.material_losses)
        self.assertEqual(sig.correction_debt, frozenset({"c"}))

    def test_actual_history_recurses(self):
        h0 = ActualHistory(("s0",))
        h1 = append_actual_history(h0, "e1", "s1")
        self.assertEqual(h1.states, ("s0", "s1"))
        self.assertEqual(h1.events, ("e1",))
        self.assertEqual(h1.current, "s1")

    def test_falsifier(self):
        report = run(max_worlds=4)
        self.assertEqual(report.failures, [])


if __name__ == "__main__":
    unittest.main()
