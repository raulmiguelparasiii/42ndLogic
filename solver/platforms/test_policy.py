import unittest

from solver.notifications import render_action_required_issue
from solver.platforms import ActionClass, PlatformFacts, plan_platform_actions


class PlatformPolicyTests(unittest.TestCase):
    def test_plain_github_claim_does_not_interrupt_user(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="github-native",
                source_url="https://github.com/example/repo/issues/1",
                can_claim_via_connected_github=True,
                claim_text="/attempt #1",
            )
        )
        self.assertTrue(plan.can_continue_without_interrupting_user)
        self.assertEqual(plan.auto_actions[0].id, "claim")

    def test_binding_terms_force_per_action_approval(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="example",
                source_url="https://example.test/bounty/1",
                can_claim_via_connected_github=True,
                claim_text="/claim #1",
                claim_accepts_program_terms=True,
            )
        )
        self.assertFalse(plan.can_continue_without_interrupting_user)
        self.assertIn("claim_terms", [a.id for a in plan.human_actions])

    def test_payout_setup_is_one_time_not_per_bounty(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="example",
                source_url="https://example.test",
                payout_onboarding_required=True,
            )
        )
        action = next(a for a in plan.human_actions if a.id == "payout_onboarding")
        self.assertEqual(action.action_class, ActionClass.HUMAN_ONCE)

    def test_wallet_signature_and_spend_require_user(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="crypto-platform",
                source_url="https://example.test",
                wallet_signature_required=True,
                spend_or_bond_required=True,
            )
        )
        self.assertEqual(
            {a.id for a in plan.human_actions},
            {"wallet_signature", "spend_or_bond"},
        )

    def test_notification_collapses_human_actions_into_one_issue(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="example",
                source_url="https://example.test/bounty/7",
                account_onboarding_required=True,
                payout_onboarding_required=True,
            )
        )
        notice = render_action_required_issue(
            "Example bounty",
            "https://example.test/bounty/7",
            plan.human_actions,
            assignee="owner",
        )
        self.assertEqual(notice.title, "[ACTION REQUIRED] Example bounty")
        self.assertEqual(notice.assignee, "owner")
        self.assertIn("account onboarding", notice.body)
        self.assertIn("payout method", notice.body)


if __name__ == "__main__":
    unittest.main()
