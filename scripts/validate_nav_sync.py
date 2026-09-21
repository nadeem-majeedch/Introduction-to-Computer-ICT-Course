#!/usr/bin/env python3
"""Validate that mkdocs.yml nav and the docs/ tree are in lock-step (stdlib only).

Checks:
  1. Every .md file under docs/ appears exactly once in the nav.
  2. Every nav entry resolves to an existing file.
"""
import re
import sys

from course_paths import DOCS, MKDOCS_YML, ROOT, docs_markdown_files


def extract_nav_entries(yaml_text: str) -> list[str]:
    """Minimal YAML-subset reader scoped to this repository's nav format."""
    lines = yaml_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^nav:\s*$", line):
            start = i + 1
            break
    if start is None:
        raise ValueError("mkdocs.yml: no top-level 'nav:' key found")

    entries: list[str] = []
    for line in lines[start:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0:
            break  # next top-level key: nav section ended
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        content = stripped[1:].strip()
        # Section titles ('- Modules:') have no file path — skip them.
        if content.endswith(":") and ".md" not in content:
            continue
        # Quoted-or-plain title: path/lectures/L01-....md  (title may contain ':')
        m = re.search(r":\s*([A-Za-z0-9_./\-]+\.md)\s*$", content)
        if m:
            entries.append(m.group(1))
            continue
        # Bare path entry: - lectures/L01-....md
        if re.match(r"^[A-Za-z0-9_./\-]+\.md$", content):
            entries.append(content)
            continue
        raise ValueError(f"mkdocs.yml: unrecognised nav entry: {stripped!r}")
    return entries


def main() -> int:
    try:
        nav_entries = extract_nav_entries(MKDOCS_YML.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    docs_files = docs_markdown_files()  # 'docs/…' repo-relative paths
    failures: list[str] = []

    # MkDocs nav paths are relative to docs_dir — resolve against docs/.
    missing_on_disk = [e for e in nav_entries if not (DOCS / e).exists()]
    if missing_on_disk:
        failures.append(
            "Nav entries pointing to non-existent files:\n  "
            + "\n  ".join(missing_on_disk)
        )

    nav_set = set(nav_entries)
    missing_from_nav = [
        f for f in docs_files if f.removeprefix("docs/") not in nav_set
    ]
    if missing_from_nav:
        failures.append(
            "Files under docs/ missing from nav:\n  " + "\n  ".join(missing_from_nav)
        )

    duplicated = sorted({e for e in nav_entries if nav_entries.count(e) > 1})
    if duplicated:
        failures.append("Duplicated nav entries:\n  " + "\n  ".join(duplicated))

    # Nav must never escape the public docs tree.
    escaping = [
        e
        for e in nav_entries
        if e.startswith("/") or ".." in e
        or e.startswith(("instructor/", "docs-meta/", "scripts/", "tests/"))
    ]
    if escaping:
        failures.append(
            "Nav entries escaping docs/ (privacy/build guard):\n  "
            + "\n  ".join(escaping)
        )

    print(f"nav entries: {len(nav_entries)}; docs/ markdown files: {len(docs_files)}")
    if failures:
        print("FAIL: validate_nav_sync")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS: validate_nav_sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
