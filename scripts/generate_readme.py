#!/usr/bin/env python3
"""Update generated sections without touching editorial prose."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "resources.yaml"
README_PATH = ROOT / "README.md"


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"Expected exactly one marker pair: {start} / {end}")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{replacement.rstrip()}\n{end}{after}"


def access_label(resource: dict) -> str:
    return "Free" if resource["free"] else "Paid or account required"


def activity_label(resource: dict) -> str:
    return {
        "active": "Active",
        "needs-review": "Check compatibility",
        "archived": "Archived",
    }[resource["status"]]


def resource_table(resources: list[dict]) -> str:
    lines = [
        "| Resource | Type | Access | Practice | Level | Status |",
        "|---|---|---|---|---|---|",
    ]
    for item in resources:
        practice = "Hands-on" if item["hands_on"] else "Reading"
        lines.append(
            f"| [{item['name']}]({item['url']}) | {item['type']} | "
            f"{access_label(item)} | {practice} | {item['level'].title()} | {activity_label(item)} |"
        )
    return "\n".join(lines)


def category_table(categories: list[dict], counts: Counter) -> str:
    lines = ["| Workflow area | What it covers | Resources |", "|---|---|---:|"]
    for category in categories:
        lines.append(
            f"| [{category['title']}]({category['page']}) | {category['summary']} | "
            f"{counts[category['slug']]} |"
        )
    return "\n".join(lines)


def update_readme(text: str, data: dict) -> str:
    resources = data["resources"]
    categories = data["categories"]
    counts = Counter(item["category"] for item in resources if item["status"] != "archived")
    status = (
        f"**Last reviewed:** {data['last_reviewed']}  \n"
        f"**Resources:** {sum(counts.values())}  \n"
        f"**Categories:** {len(categories)}"
    )
    text = replace_between(text, "<!-- STATUS_START -->", "<!-- STATUS_END -->", status)
    text = replace_between(
        text,
        "<!-- CATEGORY_TABLE_START -->",
        "<!-- CATEGORY_TABLE_END -->",
        category_table(categories, counts),
    )
    return text


def update_category_page(text: str, category: dict, resources: list[dict]) -> str:
    current = [r for r in resources if r["category"] == category["slug"] and r["status"] != "archived"]
    return replace_between(
        text,
        "<!-- RESOURCE_LIST_START -->",
        "<!-- RESOURCE_LIST_END -->",
        resource_table(current),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated content is stale.")
    args = parser.parse_args()

    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    pending: list[tuple[Path, str, str]] = []
    original = README_PATH.read_text(encoding="utf-8")
    pending.append((README_PATH, original, update_readme(original, data)))

    for category in data["categories"]:
        path = ROOT / category["page"]
        original = path.read_text(encoding="utf-8")
        pending.append((path, original, update_category_page(original, category, data["resources"])))

    changed = [path for path, before, after in pending if before != after]
    if args.check:
        if changed:
            print("Generated sections are stale:", file=sys.stderr)
            for path in changed:
                print(f"- {path.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print("Generated sections are current.")
        return 0

    for path, before, after in pending:
        if before != after:
            path.write_text(after, encoding="utf-8", newline="\n")
    print(f"Updated {len(changed)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

