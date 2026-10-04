#!/usr/bin/env python3
"""Find review candidates through the GitHub Search API."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
QUERIES = [
    ("ai-assisted-analysis-and-sql", '"text to sql" tutorial in:name,description,readme'),
    ("data-preparation-and-extraction", '"structured extraction" llm in:name,description,readme'),
    ("ai-assisted-machine-learning", 'automl tutorial in:name,description,readme'),
    ("tabular-foundation-models", '"tabular foundation model" in:name,description,readme'),
    ("coding-agents-and-context", '"coding agent" data science in:name,description,readme'),
    ("data-science-agents", '"data science agent" in:name,description,readme'),
    ("evaluation-and-reproducibility", 'llm evaluation tutorial in:name,description,readme'),
    ("mlops-and-production", 'llmops course in:name,description,readme'),
    ("visualization-and-communication", 'ai data visualization tutorial in:name,description,readme'),
    ("time-series-foundation-models", '"time series foundation model" in:name,description,readme'),
    ("end-to-end-courses", 'ai data science course notebooks in:name,description,readme'),
]


def github_search(query: str, token: str | None, per_page: int) -> list[dict]:
    params = urllib.parse.urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": per_page})
    request = urllib.request.Request(
        f"https://api.github.com/search/repositories?{params}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-for-data-science-resources-discovery/1.0",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response).get("items", [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data" / "resources.yaml")
    parser.add_argument("--output", type=Path, default=ROOT / "reports" / "monthly-resource-review.md")
    parser.add_argument("--per-query", type=int, default=5)
    args = parser.parse_args()

    data = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    existing = {item["url"].rstrip("/").casefold() for item in data["resources"]}
    token = os.environ.get("GITHUB_TOKEN")
    candidates: list[dict] = []
    seen: set[str] = set()
    errors: list[str] = []

    for category, query in QUERIES:
        try:
            items = github_search(query, token, args.per_query)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            errors.append(f"{category}: {exc}")
            continue
        for item in items:
            url = item["html_url"].rstrip("/")
            key = url.casefold()
            if key in existing or key in seen or item.get("archived"):
                continue
            seen.add(key)
            candidates.append(
                {
                    "name": item["full_name"],
                    "url": url,
                    "category": category,
                    "description": item.get("description") or "No repository description provided.",
                    "updated": item.get("pushed_at") or item.get("updated_at") or "Unknown",
                    "license": (item.get("license") or {}).get("spdx_id") or "Unknown",
                }
            )
        time.sleep(0.25)

    month = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m")
    lines = [
        f"# Monthly Resource Review - {month}",
        "",
        "These are discovery candidates, not approved resources. A maintainer must inspect the material, run examples where practical, check affiliation, and compare it with existing entries.",
        "",
    ]
    if not candidates:
        lines.append("No new candidates were returned by the configured GitHub searches.")
    for candidate in candidates:
        lines.extend(
            [
                f"## {candidate['name']}",
                "",
                f"- **URL:** {candidate['url']}",
                f"- **Suggested category:** {candidate['category']}",
                "- **Type:** GitHub repository, requires review",
                "- **Free/Paid:** Likely free; confirm licensing and any hosted-service costs",
                "- **Hands-on:** Unknown; inspect examples, notebooks, and assignments",
                f"- **Last updated:** {candidate['updated']}",
                f"- **What it teaches:** {candidate['description']}",
                "- **Why it could be useful:** It matched a targeted practical-learning query and has recent repository activity.",
                "- **Similar existing resource:** Compare manually before accepting",
                f"- **License:** {candidate['license']}",
                "",
            ]
        )
    if errors:
        lines.extend(["## Discovery errors", ""] + [f"- {error}" for error in errors] + [""])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {len(candidates)} candidates to {args.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

