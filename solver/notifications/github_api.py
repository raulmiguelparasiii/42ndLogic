from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

from .github_issue import ActionRequiredNotice

MARKER_PREFIX = "<!-- onelogic-action-required:"


@dataclass(frozen=True)
class NotificationResult:
    created: bool
    issue_url: str
    issue_number: int


def _request(url: str, token: str, *, method: str = "GET", payload: dict | None = None):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "42ndLogic-OneLogic-Solver",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, headers=headers, data=data, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub notification request failed ({exc.code}): {detail[-2000:]}") from exc


def action_marker(key: str) -> str:
    safe = urllib.parse.quote(key, safe="")
    return f"{MARKER_PREFIX}{safe} -->"


def ensure_action_required_issue(
    repository: str,
    token: str,
    notice: ActionRequiredNotice,
    *,
    dedupe_key: str,
) -> NotificationResult:
    """Create one operator issue, deduplicated by an embedded target/action key."""
    marker = action_marker(dedupe_key)
    api = f"https://api.github.com/repos/{repository}"

    existing = _request(f"{api}/issues?state=open&per_page=100", token)
    for issue in existing:
        if issue.get("pull_request"):
            continue
        body = str(issue.get("body") or "")
        if marker in body:
            return NotificationResult(
                created=False,
                issue_url=str(issue["html_url"]),
                issue_number=int(issue["number"]),
            )

    body = marker + "\n" + notice.body
    payload: dict[str, object] = {"title": notice.title, "body": body}
    if notice.assignee:
        payload["assignees"] = [notice.assignee]

    issue = _request(f"{api}/issues", token, method="POST", payload=payload)
    return NotificationResult(
        created=True,
        issue_url=str(issue["html_url"]),
        issue_number=int(issue["number"]),
    )
