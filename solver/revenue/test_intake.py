import unittest

from solver.revenue import Evidence, TargetStatus, evaluate_target


def base(**overrides):
    data = dict(
        source_url="https://github.com/example/repo/issues/1",
        source_open=True,
        reward_amount=100.0,
        reward_currency="USD",
        payment_explicit=True,
        payout_path_explicit=True,
        acceptance_criteria_explicit=True,
    )
    data.update(overrides)
    return Evidence(**data)


class RevenueIntakeTests(unittest.TestCase):
    def test_clean_target_is_cash_near(self):
        d = evaluate_target(base())
        self.assertEqual(d.status, TargetStatus.VERIFIED_CASH_NEAR)
        self.assertTrue(d.economically_live)

    def test_advertised_amount_without_payout_path_is_not_verified(self):
        d = evaluate_target(base(payout_path_explicit=False))
        self.assertEqual(d.status, TargetStatus.PAYMENT_UNVERIFIED)
        self.assertFalse(d.economically_live)

    def test_assignment_to_someone_else_is_blocking(self):
        d = evaluate_target(base(assigned_to_other=True))
        self.assertEqual(d.status, TargetStatus.COMPETED)
        self.assertFalse(d.economically_live)

    def test_claim_required_is_not_silently_treated_as_available(self):
        d = evaluate_target(base(assignment_required=True))
        self.assertEqual(d.status, TargetStatus.NEEDS_CLAIM)
        self.assertTrue(d.economically_live)
        self.assertFalse(d.solve_before_claim)

    def test_paid_infra_does_not_get_hidden_by_large_reward(self):
        d = evaluate_target(base(reward_amount=10000, requires_paid_infra=True))
        self.assertEqual(d.status, TargetStatus.REQUIRES_PAID_INFRA)
        self.assertFalse(d.economically_live)

    def test_hardware_gate_is_preserved(self):
        d = evaluate_target(base(requires_special_hardware=True))
        self.assertEqual(d.status, TargetStatus.REQUIRES_SPECIAL_HARDWARE)

    def test_competition_is_explicit(self):
        d = evaluate_target(base(active_competing_implementations=2))
        self.assertEqual(d.status, TargetStatus.COMPETED)
        self.assertTrue(d.economically_live)
        self.assertTrue(d.solve_before_claim)
        self.assertIn("2 active competing implementation(s) observed", d.warnings)


if __name__ == "__main__":
    unittest.main()
