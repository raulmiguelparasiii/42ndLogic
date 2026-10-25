import pathlib, sys, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "formal"))

from one_logic.core import (
    Assertion,
    EvidenceRecord,
    InquiryProfile,
    Query,
    ResponseProfile,
    SupportOrder,
    categorical_consequences,
    independent_ancestry_roots,
    judge_query,
    mature_response_frontier,
    proportionate_inquiry_frontier,
    provisional_consequences,
    representation_preserves_material_distinctions,
    robust_categorical_consequence,
)


class MatureJudgmentTests(unittest.TestCase):
    def test_best_supported_does_not_become_truth(self):
        q = Query("interpretation", {0: "benign", 1: "hostile"})
        support = SupportOrder({0: 9.0, 1: 1.0})
        self.assertEqual(categorical_consequences({0, 1}, [q]), frozenset())
        self.assertEqual(
            provisional_consequences({0, 1}, [q], support),
            frozenset({Assertion("interpretation", "benign")}),
        )
        judgment = judge_query({0, 1}, q, support)
        self.assertEqual(judgment.status, "provisional")
        self.assertNotEqual(judgment.status, "forced")

    def test_equal_support_preserves_open_judgment(self):
        q = Query("intent", {0: "careless", 1: "malicious"})
        judgment = judge_query({0, 1}, q, SupportOrder({0: 1.0, 1: 1.0}))
        self.assertEqual(judgment.status, "open")
        self.assertIsNone(judgment.assertion)

    def test_affected_welfare_can_be_materially_required(self):
        welfare = Query("affected_welfare", {0: "preserved", 1: "harmed"})
        collapsed = {0: "same", 1: "same"}
        preserved = {0: "a", 1: "b"}
        self.assertFalse(
            representation_preserves_material_distinctions({0, 1}, [welfare], collapsed)
        )
        self.assertTrue(
            representation_preserves_material_distinctions({0, 1}, [welfare], preserved)
        )

    def test_source_weight_can_shift_provisional_without_settling(self):
        q = Query("claim", {0: True, 1: False})
        before = judge_query({0, 1}, q, SupportOrder({0: 1.0, 1: 1.0}))
        after = judge_query({0, 1}, q, SupportOrder({0: 3.0, 1: 1.0}))
        self.assertEqual(before.status, "open")
        self.assertEqual(after.status, "provisional")
        self.assertEqual(categorical_consequences({0, 1}, [q]), frozenset())

    def test_duplicate_transmission_does_not_create_new_ancestry(self):
        records = [
            EvidenceRecord("original", frozenset({"obs:A"})),
            EvidenceRecord("copy-1", frozenset({"obs:A"})),
            EvidenceRecord("copy-2", frozenset({"obs:A"})),
            EvidenceRecord("independent", frozenset({"obs:B"})),
        ]
        self.assertEqual(independent_ancestry_roots(records), frozenset({"obs:A", "obs:B"}))

    def test_encoding_robustness_prevents_adverse_closure(self):
        q = Query("motive", {0: "unknown", 1: "malicious", 2: "malicious"})
        self.assertIsNone(robust_categorical_consequence([{1, 2}, {0, 1}], q))
        self.assertEqual(
            robust_categorical_consequence([{1, 2}, {1}], q),
            Assertion("motive", "malicious"),
        )

    def test_inquiry_frontier_prefers_more_gain_with_no_more_burden(self):
        inquiries = [
            InquiryProfile("clarify", frozenset({"intent"}), {"cost": 1.0, "risk": 0.0}),
            InquiryProfile("broad-check", frozenset({"intent", "provenance"}), {"cost": 1.0, "risk": 0.0}),
            InquiryProfile("dangerous", frozenset({"intent", "provenance"}), {"cost": 0.5}, admissible=False),
        ]
        frontier = proportionate_inquiry_frontier(inquiries, {"intent", "provenance"})
        self.assertEqual(tuple(i.inquiry for i in frontier), ("broad-check",))

    def test_tragic_choice_keeps_nondominated_residue(self):
        responses = [
            ResponseProfile("protect-A", frozenset({"welfare:B"}), True),
            ResponseProfile("protect-B", frozenset({"welfare:A"}), True),
            ResponseProfile("worse", frozenset({"welfare:A", "welfare:B"}), True),
            ResponseProfile("sealed", frozenset(), False),
        ]
        frontier = mature_response_frontier(responses)
        self.assertEqual(
            {r.response for r in frontier},
            {"protect-A", "protect-B"},
        )
        self.assertTrue(all(r.unresolved_pressures for r in frontier))


if __name__ == "__main__":
    unittest.main()
