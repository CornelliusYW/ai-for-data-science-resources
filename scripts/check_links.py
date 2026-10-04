#!/usr/bin/env python3
"""Check curated URLs and write a review-friendly report."""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import ssl
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "ai-for-data-science-resources-link-check/1.0 (+https://github.com/)"


@dataclass
class Result:
    name: str
    url: str
    category: str
    outcome: str
    status_code: int | None
    final_url: str | None
    detail: str


def check(resource: dict, timeout: float) -> Result:
    request = urllib.request.Request(
        resource["url"],
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,*/*"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            code = response.getcode()
            final_url = response.geturl()
            outcome = "redirect" if final_url.rstrip("/") != resource["url"].rstrip("/") else "ok"
            return Result(resource["name"], resource["url"], resource["category"], outcome, code, final_url, "")
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 429}:
            detail = "The server blocked or rate-limited the automated check; review manually."
            outcome = "blocked"
        else:
            detail = str(exc.reason)
            outcome = "broken"
        return Result(resource["name"], resource["url"], resource["category"], outcome, exc.code, exc.geturl(), detail)
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError) as exc:
        return Result(resource["name"], resource["url"], resource["category"], "broken", None, None, str(exc))


def markdown_report(results: list[Result]) -> str:
    problems = [result for result in results if result.outcome != "ok"]
    lines = [
        "# Broken Resource Links",
        "",
        f"Checked: {dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}",
        f"Resources checked: {len(results)}",
        f"Items for review: {len(problems)}",
        "",
    ]
    if not problems:
        lines.append("No broken links, blocked checks, or redirects were found.")
        return "\n".join(lines) + "\n"
    lines.extend(
        [
            "| Resource | Category | Problem | Suggested action |",
            "|---|---|---|---|",
        ]
    )
    for result in problems:
        if result.outcome == "redirect":
            problem = f"Redirects to {result.final_url}"
            action = "Update the stored URL if the destination is canonical."
        elif result.outcome == "blocked":
            problem = f"Automated check blocked ({result.status_code})"
            action = "Open manually before changing the resource."
        else:
            suffix = f" ({result.status_code})" if result.status_code else ""
            problem = f"Request failed{suffix}: {result.detail}"
            action = "Verify manually; update or mark needs-review."
        lines.append(f"| [{result.name}]({result.url}) | {result.category} | {problem} | {action} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data" / "resources.yaml")
    parser.add_argument("--output", type=Path, default=ROOT / "reports" / "link-check.md")
    parser.add_argument("--json-output", type=Path, default=ROOT / "reports" / "link-check.json")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=0, help="Check only the first N resources; 0 checks all.")
    args = parser.parse_args()

    data = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    resources = [item for item in data["resources"] if item["status"] != "archived"]
    if args.limit:
        resources = resources[: args.limit]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(check, resource, args.timeout) for resource in resources]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    results.sort(key=lambda item: (item.outcome == "ok", item.category, item.name.casefold()))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown_report(results), encoding="utf-8", newline="\n")
    args.json_output.write_text(
        json.dumps([asdict(result) for result in results], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    broken = sum(result.outcome == "broken" for result in results)
    blocked = sum(result.outcome == "blocked" for result in results)
    redirects = sum(result.outcome == "redirect" for result in results)
    print(f"Checked {len(results)} links: {broken} broken, {blocked} blocked, {redirects} redirects.")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())

