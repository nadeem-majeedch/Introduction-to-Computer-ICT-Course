#!/usr/bin/env python3
"""Instructor-material leak guard (stdlib only).

Guarantees:
  1. instructor/ exists OUTSIDE docs/ and contains no files inside docs/
  2. no file under docs/ references 'instructor/' in any form
  3. mkdocs.yml nav contains no instructor entries
  4. instructor/ does not contain HTML that could be mistaken for published site output
"""
import re
import sys

from course_paths import DOCS, INSTRUCTOR, MKDOCS_YML, ROOT, docs_markdown_files

# Matches path-style references ('instructor/…') only — the plain English word
# 'instructor' appears legitimately throughout student-facing prose (e.g.
# 'ask the instructor'), which must not fail the guard.
REFERENCE_RE = re.compile(r"\binstructor/(?:[A-Za-z0-9_\-./]+)?", re.IGNORECASE)


def main() -> int:
    issues: list[str] = []

    if not INSTRUCTOR.is_dir():
        print("FAIL: instructor/ directory not found at repository root")
        return 1

    docs_resolved = DOCS.resolve()
    for path in INSTRUCTOR.rglob("*"):
        if path.is_file() and docs_resolved in path.resolve().parents:
            issues.append(f"instructor file found inside docs/: {path}")

    for rel in docs_markdown_files():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for m in REFERENCE_RE.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            line = text.splitlines()[line_no - 1].strip()
            issues.append(f"{rel}:{line_no}: reference to instructor material: {line[:80]}")

    nav_text = MKDOCS_YML.read_text(encoding="utf-8")
    if REFERENCE_RE.search(nav_text):
        issues.append("mkdocs.yml references instructor material in nav/config")

    for path in INSTRUCTOR.rglob("*.html"):
        issues.append(f"unexpected HTML file in instructor/: {path.relative_to(ROOT)}")

    instructor_files = sum(1 for p in INSTRUCTOR.rglob("*") if p.is_file())
    print(f"instructor/ files (private): {instructor_files}")
    if issues:
        print("FAIL: check_instructor_exclusion — leaked instructor material detected")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS: check_instructor_exclusion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
