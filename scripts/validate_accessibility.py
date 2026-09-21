#!/usr/bin/env python3
"""Accessibility validator for docs/ (stdlib only).

Checks:
  - every image has non-empty, non-generic alt text
  - no bare-URL or "click here" link text
  - heading levels never skip (h1 -> h3)
"""
import re
import sys

from course_paths import docs_markdown_files, ROOT

GENERIC_ALT = {"image", "img", "picture", "photo", "logo", "icon", "screenshot"}
BAD_LINK_TEXT = re.compile(r"^\s*(click here|here|link|this)\s*$", re.IGNORECASE)
IMAGE_RE = re.compile(r"!\[(.*?)\]\((.*?)\)")
LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")


def heading_levels_jump(body: str) -> str | None:
    last = 1
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s", line)
        if not m:
            continue
        level = len(m.group(1))
        if level > last + 1:
            return f"skips from h{last} to h{level} at: {line[:50]!r}"
        last = level
    return None


def validate_file(rel_path: str) -> list[str]:
    issues: list[str] = []
    text = (ROOT / rel_path).read_text(encoding="utf-8")

    for alt, _target in IMAGE_RE.findall(text):
        if not alt.strip():
            issues.append(f"{rel_path}: image with empty alt text")
        elif alt.strip().lower() in GENERIC_ALT:
            issues.append(f"{rel_path}: generic alt text {alt.strip()!r}")

    for label, target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://")) and BAD_LINK_TEXT.match(label):
            issues.append(f"{rel_path}: non-descriptive link text {label!r}")
        if label.strip().startswith("http"):
            issues.append(f"{rel_path}: bare URL used as link text ({label[:40]}…)")
        if not target.strip():
            issues.append(f"{rel_path}: link with empty target ({label!r})")

    fm_len = 0
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_len = end + 4
    jump = heading_levels_jump(text[fm_len:])
    if jump:
        issues.append(f"{rel_path}: heading level jump — {jump}")

    return issues


def main() -> int:
    all_issues: list[str] = []
    files = docs_markdown_files()
    for rel in files:
        all_issues.extend(validate_file(rel))
    print(f"checked files: {len(files)}")
    if all_issues:
        print("FAIL: validate_accessibility")
        for issue in all_issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_accessibility")
    return 0


if __name__ == "__main__":
    sys.exit(main())
