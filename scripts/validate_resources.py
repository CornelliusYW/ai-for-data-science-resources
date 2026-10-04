#!/usr/bin/env python3
"""Validate the curated resource database."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "resources.yaml"

REQUIRED_FIELDS = {
    "id",
    "name",
    "url",
    "category",
    "type",
    "description",
    "use_case",
    "level",
    "free",
    "hands_on",
    "github",
    "last_verified",
    "status",
}
ALLOWED_TYPES = {
    "Book",
    "Course",
    "Example Project",
    "GitHub Curriculum",
    "Guide",
    "Interactive Learning",
    "Notebook Collection",
    "Official Documentation",
    "Template",
    "Tool",
    "Tutorial",
    "Video Course",
    "Workshop",
}
ALLOWED_LEVELS = {"beginner", "intermediate", "advanced", "all-levels"}
ALLOWED_STATUSES = {"active", "needs-review", "archived"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def normalized_url(value: str) -> str:
    parts = urlsplit(value.strip())
    host = (parts.hostname or "").lower()
    if parts.port:
        host = f"{host}:{parts.port}"
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), host, path, parts.query, ""))


def valid_date(value: object) -> bool:
    if isinstance(value, dt.date):
        return True
    if not isinstance(value, str):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"Could not read valid YAML: {exc}"]

    if not isinstance(data, dict):
        return ["Top-level YAML value must be a mapping."]

    categories = data.get("categories")
    resources = data.get("resources")
    if not isinstance(categories, list) or not categories:
        errors.append("categories must be a non-empty list.")
        categories = []
    if not isinstance(resources, list) or not resources:
        errors.append("resources must be a non-empty list.")
        resources = []

    category_slugs: list[str] = []
    category_pages: list[str] = []
    for index, category in enumerate(categories, start=1):
        label = f"category #{index}"
        if not isinstance(category, dict):
            errors.append(f"{label} must be a mapping.")
            continue
        missing = {"slug", "title", "page", "summary", "try_this"} - set(category)
        if missing:
            errors.append(f"{label} is missing: {', '.join(sorted(missing))}.")
        slug = category.get("slug")
        page = category.get("page")
        if not isinstance(slug, str) or not ID_RE.fullmatch(slug):
            errors.append(f"{label} has an invalid slug: {slug!r}.")
        else:
            category_slugs.append(slug)
        if isinstance(page, str):
            category_pages.append(page)
        else:
            errors.append(f"{label} has an invalid page path.")

    for value, count in Counter(category_slugs).items():
        if count > 1:
            errors.append(f"Duplicate category slug: {value}.")
    for value, count in Counter(category_pages).items():
        if count > 1:
            errors.append(f"Duplicate category page: {value}.")

    ids: list[str] = []
    names: list[str] = []
    urls: list[str] = []
    known_categories = set(category_slugs)
    for index, resource in enumerate(resources, start=1):
        if not isinstance(resource, dict):
            errors.append(f"resource #{index} must be a mapping.")
            continue
        label = f"resource #{index} ({resource.get('name', 'unnamed')})"
        missing = REQUIRED_FIELDS - set(resource)
        if missing:
            errors.append(f"{label} is missing: {', '.join(sorted(missing))}.")

        resource_id = resource.get("id")
        if not isinstance(resource_id, str) or not ID_RE.fullmatch(resource_id):
            errors.append(f"{label} has an invalid id: {resource_id!r}.")
        else:
            ids.append(resource_id)

        name = resource.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label} has an invalid name.")
        else:
            names.append(name.strip().casefold())

        url = resource.get("url")
        if not isinstance(url, str):
            errors.append(f"{label} has an invalid URL.")
        else:
            parts = urlsplit(url)
            if parts.scheme != "https" or not parts.netloc:
                errors.append(f"{label} must use a complete HTTPS URL: {url!r}.")
            else:
                urls.append(normalized_url(url))

        if resource.get("category") not in known_categories:
            errors.append(f"{label} uses an unknown category: {resource.get('category')!r}.")
        if resource.get("type") not in ALLOWED_TYPES:
            errors.append(f"{label} uses an unknown type: {resource.get('type')!r}.")
        if resource.get("level") not in ALLOWED_LEVELS:
            errors.append(f"{label} uses an unknown level: {resource.get('level')!r}.")
        if resource.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{label} uses an unknown status: {resource.get('status')!r}.")
        if not valid_date(resource.get("last_verified")):
            errors.append(f"{label} has an invalid last_verified date.")
        if "last_updated" in resource and not valid_date(resource["last_updated"]):
            errors.append(f"{label} has an invalid last_updated date.")
        for field in ("free", "hands_on", "github"):
            if not isinstance(resource.get(field), bool):
                errors.append(f"{label} field {field!r} must be true or false.")
        for field in ("description", "use_case"):
            value = resource.get(field)
            if not isinstance(value, str) or len(value.strip()) < 20:
                errors.append(f"{label} field {field!r} is too short or missing.")

    for label, values in (("resource id", ids), ("resource name", names), ("resource URL", urls)):
        for value, count in Counter(values).items():
            if count > 1:
                errors.append(f"Duplicate {label}: {value}.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()
    errors = validate(args.data)
    if errors:
        print(f"Resource validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    data = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    print(f"Validated {len(data['resources'])} resources in {len(data['categories'])} categories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

