#!/usr/bin/env python3
"""Generate a quarterly human-review report from local resource metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def github_metadata(url: str, token: str | None) -> dict:
    parts = url.rstrip("/").split("/")
    owner, repository = parts[-2], parts[-1]
    request = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repository}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-for-data-science-resources-quarterly-review/1.0",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def parse_date(value: object) -> dt.date:
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data" / "resources.yaml")
    parser.add_argument("--output", type=Path, default=ROOT / "reports" / "quarterly-curation-review.md")
    parser.add_argument("--stale-days", type=int, default=120)
    args = parser.parse_args()

    data = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    resources = data["resources"]
    categories = {category["slug"]: category["title"] for category in data["categories"]}
    counts = Counter(resource["category"] for resource in resources if resource["status"] != "archived")
    today = dt.datetime.now(dt.timezone.utc).date()
    quarter = (today.month - 1) // 3 + 1
    stale = [
        item
        for item in resources
        if (today - parse_date(item["last_verified"])).days > args.stale_days
    ]
    flagged = [item for item in resources if item["status"] != "active"]
    paid = [item for item in resources if not item["free"]]
    github_signals: list[tuple[dict, dict]] = []
    github_errors: list[tuple[dict, str]] = []
    token = os.environ.get("GITHUB_TOKEN")
    for item in resources:
        if not item["github"] or not item["url"].startswith("https://github.com/"):
            continue
        try:
            github_signals.append((item, github_metadata(item["url"], token)))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            github_errors.append((item, str(exc)))

    inactive_cutoff = today - dt.timedelta(days=365)
    archived_repositories = [(item, meta) for item, meta in github_signals if meta.get("archived")]
    quiet_repositories: list[tuple[dict, dict]] = []
    for item, meta in github_signals:
        pushed_at = meta.get("pushed_at")
        if not pushed_at:
            continue
        pushed_date = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00")).date()
        if pushed_date < inactive_cutoff:
            quiet_repositories.append((item, meta))

    lines = [
        f"# Quarterly Resource Curation - {today.year}-Q{quarter}",
        "",
        "This report proposes review work. It does not remove or add resources automatically.",
        "",
        "## Collection overview",
        "",
        "| Category | Active listing count |",
        "|---|---:|",
    ]
    for slug, title in categories.items():
        lines.append(f"| {title} | {counts[slug]} |")
    lines.extend(
        [
            "",
            "## Review queue",
            "",
            f"- Resources not verified in the last {args.stale_days} days: {len(stale)}",
            f"- Resources already marked needs-review or archived: {len(flagged)}",
            f"- Paid or account-dependent resources to recheck: {len(paid)}",
            "",
            "### Stale verification dates",
            "",
        ]
    )
    lines.extend([f"- [{item['name']}]({item['url']}) - last verified {item['last_verified']}" for item in stale] or ["- None"])
    lines.extend(["", "### Flagged resources", ""])
    lines.extend(
        [f"- [{item['name']}]({item['url']}) - {item['status']}: {item.get('maintenance_note', 'Review manually.')}" for item in flagged]
        or ["- None"]
    )
    lines.extend(["", "### Access checks", ""])
    lines.extend([f"- [{item['name']}]({item['url']}) - confirm current free tier, price, and account requirements" for item in paid] or ["- None"])
    lines.extend(["", "### GitHub maintenance signals", ""])
    lines.append(f"- GitHub repositories checked: {len(github_signals)}")
    lines.append(f"- Archived upstream repositories: {len(archived_repositories)}")
    lines.append(f"- No upstream push in the last 365 days: {len(quiet_repositories)}")
    lines.append(f"- GitHub API checks that need retrying: {len(github_errors)}")
    if archived_repositories:
        lines.extend([f"  - [{item['name']}]({item['url']}) is archived upstream" for item, _ in archived_repositories])
    if quiet_repositories:
        lines.extend(
            [f"  - [{item['name']}]({item['url']}) - last upstream push {meta.get('pushed_at', 'unknown')}" for item, meta in quiet_repositories]
        )
    if github_errors:
        lines.extend([f"  - [{item['name']}]({item['url']}) - API check failed: {error}" for item, error in github_errors])
    lines.extend(
        [
            "",
            "## Maintainer decisions",
            "",
            "For each proposed change, record keep, update, replace, merge, or archive, with a short reason. Also review categories that are too broad, too small, or duplicative.",
            "",
        ]
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Wrote quarterly review to {args.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

