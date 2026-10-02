import unittest

from solver.notifications.github_api import action_marker
from solver.notifications.github_issue import render_action_required_issue
from solver.platforms import PlatformFacts, plan_platform_actions


class NotificationTests(unittest.TestCase):
    def test_marker_is_deterministic_and_url_safe(self):
        a = action_marker("https://example.test/bounty/1|claim")
        b = action_marker("https://example.test/bounty/1|claim")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("<!-- onelogic-action-required:"))
        self.assertNotIn(" ", a.split(":", 1)[1].rsplit("-->", 1)[0])

    def test_notice_contains_only_human_gate(self):
        plan = plan_platform_actions(
            PlatformFacts(
                platform="example",
                source_url="https://example.test/bounty/1",
                account_onboarding_required=True,
                can_claim_via_connected_github=True,
                claim_text="/attempt #1",
            )
        )
        notice = render_action_required_issue(
            "Target",
            "https://example.test/bounty/1",
            plan.human_actions,
        )
        self.assertIn("account onboarding", notice.body)
        self.assertNotIn("/attempt #1", notice.body)


if __name__ == "__main__":
    unittest.main()
