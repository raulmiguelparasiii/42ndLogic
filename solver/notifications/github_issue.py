from __future__ import annotations

from dataclasses import dataclass

from solver.platforms import OperatorAction


@dataclass(frozen=True)
class ActionRequiredNotice:
    title: str
    body: str
    assignee: str | None = None


def render_action_required_issue(
    target_title: str,
    target_url: str,
    actions: tuple[OperatorAction, ...],
    *,
    assignee: str | None = None,
) -> ActionRequiredNotice:
    """Render the single interruption the operator should receive.

    The intended delivery sink is a GitHub issue in 42ndLogic, assigned to the repo
    owner. GitHub then supplies whatever push/email/web notification the owner has
    configured. Routine solver progress does not create notifications.
    """
    if not actions:
        raise ValueError("action-required notice needs at least one human action")

    lines = [
        "<!-- onelogic-action-required -->",
        f"Target: {target_title}",
        f"Source: {target_url}",
        "",
        "OneLogic can continue after the following account-holder action(s):",
        "",
    ]
    for action in actions:
        lines.append(f"- [ ] **{action.description}**")
        lines.append(f"  - Why: {action.reason}")
        if action.url:
            lines.append(f"  - Open: {action.url}")
    lines += [
        "",
        "Do not post banking details, identity documents, API keys, wallet secrets, or tax identifiers in this issue.",
        "",
        "When completed, close this issue. The solver can then resume from the recorded target state.",
    ]

    return ActionRequiredNotice(
        title=f"[ACTION REQUIRED] {target_title}",
        body="\n".join(lines),
        assignee=assignee,
    )
