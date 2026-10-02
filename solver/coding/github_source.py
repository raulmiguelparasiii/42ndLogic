from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

from .models import ProblemSpec

ISSUE_RE = re.compile(
    r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/issues/(?P<number>\d+)(?:[/?#].*)?$"
)
REWARD_PATTERNS = (
    re.compile(r"\$\s?[\d,.]+(?:\s?(?:USD|CAD))?", re.I),
    re.compile(r"[\d,.]+\s?(?:USD|USDC|CAD)\b", re.I),
)


@dataclass(frozen=True)
class GitHubIssue:
    owner: str
    repo: str
    number: int
    title: str
    body: str
    html_url: str
    default_branch: str
    reward_text: str | None

    @property
    def clone_url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}.git"


def parse_issue_url(url: str) -> tuple[str, str, int]:
    match = ISSUE_RE.match(url.strip())
    if not match:
        raise ValueError("expected a public GitHub issue URL")
    return match.group("owner"), match.group("repo"), int(match.group("number"))


def _github_get(url: str, token: str | None = None) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "42ndLogic-OneLogic-Solver",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub request failed ({exc.code}): {detail[-2000:]}") from exc


def _extract_reward(title: str, body: str) -> str | None:
    text = title + "\n" + body
    for pattern in REWARD_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0)
    return None


def fetch_public_issue(issue_url: str, *, token: str | None = None) -> GitHubIssue:
    owner, repo, number = parse_issue_url(issue_url)
    token = token or os.environ.get("GITHUB_TOKEN")
    quoted_owner = urllib.parse.quote(owner, safe="")
    quoted_repo = urllib.parse.quote(repo, safe="")
    issue = _github_get(
        f"https://api.github.com/repos/{quoted_owner}/{quoted_repo}/issues/{number}",
        token,
    )
    repository = _github_get(
        f"https://api.github.com/repos/{quoted_owner}/{quoted_repo}",
        token,
    )
    body = str(issue.get("body") or "")
    title = str(issue.get("title") or "")
    return GitHubIssue(
        owner=owner,
        repo=repo,
        number=number,
        title=title,
        body=body,
        html_url=str(issue.get("html_url") or issue_url),
        default_branch=str(repository.get("default_branch") or "main"),
        reward_text=_extract_reward(title, body),
    )


def problem_from_issue(
    issue: GitHubIssue,
    verification_commands: tuple[tuple[str, ...], ...],
) -> ProblemSpec:
    return ProblemSpec(
        repo_url=issue.clone_url,
        issue_url=issue.html_url,
        title=issue.title,
        body=issue.body,
        verification_commands=verification_commands,
        base_ref=issue.default_branch,
        reward_text=issue.reward_text,
    )
