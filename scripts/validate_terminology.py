#!/usr/bin/env python3
"""Terminology and consistency validator (stdlib only).

Checks:
  - no TODO/TBD/FIXME/XXX markers anywhere under docs/
  - no placeholder markers like '[Institution policy]' in student-facing
    pages *other than* the syllabus (where the instructor fills them)
  - 'click here' phrasing is absent from prose
  - glossary exists and references at least 40 defined terms
"""
import re
import sys

from course_paths import DOCS, docs_markdown_files, ROOT

TODO_RE = re.compile(r"\b(TODO|TBD|FIXME|XXX)\b")
CLICK_HERE_RE = re.compile(r"\bclick here\b", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\[Institution policy[^\]]*\]")
PLACEHOLDER_ALLOWED = {"docs/syllabus.md"}
GLOSSARY = DOCS / "glossary.md"
MIN_GLOSSARY_TERMS = 40


def main() -> int:
    issues: list[str] = []
    files = docs_markdown_files()

    for rel in files:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for m in TODO_RE.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            issues.append(f"{rel}:{line_no}: placeholder marker '{m.group(0)}'")
        for m in CLICK_HERE_RE.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            issues.append(f"{rel}:{line_no}: non-inclusive phrasing 'click here'")
        if rel not in PLACEHOLDER_ALLOWED:
            for m in PLACEHOLDER_RE.finditer(text):
                line_no = text.count("\n", 0, m.start()) + 1
                issues.append(f"{rel}:{line_no}: unfilled institutional placeholder")

    if not GLOSSARY.exists():
        issues.append("docs/glossary.md is missing")
    else:
        glossary_text = GLOSSARY.read_text(encoding="utf-8")
        term_count = len(
            re.findall(r"^\*\*(.+?)\*\*", glossary_text, flags=re.MULTILINE)
        )
        print(f"glossary bolded term definitions: {term_count}")
        if term_count < MIN_GLOSSARY_TERMS:
            issues.append(
                f"glossary has {term_count} terms; expected at least {MIN_GLOSSARY_TERMS}"
            )

    print(f"checked files: {len(files)}")
    if issues:
        print("FAIL: validate_terminology")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_terminology")
    return 0


if __name__ == "__main__":
    sys.exit(main())
