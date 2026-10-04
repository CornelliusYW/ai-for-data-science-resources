#!/usr/bin/env python3
"""Check relative Markdown links and local HTML image sources."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_SOURCE = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']", re.IGNORECASE)


def local_target(raw: str, source: Path) -> Path | None:
    target = raw.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    path_text = unquote(target.split("#", 1)[0])
    if not path_text:
        return None
    return (source.parent / path_text).resolve()


def main() -> int:
    errors: list[str] = []
    files = sorted(ROOT.rglob("*.md"))
    for source in files:
        text = source.read_text(encoding="utf-8")
        candidates = MARKDOWN_LINK.findall(text) + HTML_SOURCE.findall(text)
        for raw in candidates:
            target = local_target(raw, source)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)} points outside the repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)} has a missing target: {raw}")
    if errors:
        print(f"Internal link check failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Checked relative links in {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

