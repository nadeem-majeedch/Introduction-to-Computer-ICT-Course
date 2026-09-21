#!/usr/bin/env python3
"""Validate the PROMPT 05 practical lab workbook (stdlib only).

Checks:
  - the workbook hub exists and its mapping table lists exactly the 8 graded
    labs and 4 skill builders (SB-1..SB-4)
  - the 22-area coverage matrix is present with 22 numbered rows, each naming
    a lab/builder/project
  - each graded lab handout: front-matter (lab, title, assigned, due) and the
    full PROMPT 05 section contract (Purpose/learning outcomes, prerequisites/
    equipment, expected observations, troubleshooting, accessibility
    alternative, questions, submission checklist, grading)
  - each skill builder: front-matter (lab SB-N, title, related, duration,
    graded) with the compact contract (outcomes, prerequisites, tasks,
    observations, questions, troubleshooting, submission)
  - the consolidated rubric appears in the workbook (60/25/15 weights)
  - safety rules section present in the workbook
"""
import re
import sys

from course_paths import DOCS, load_expectations

LABS_DIR = DOCS / "labs"
WORKBOOK = LABS_DIR / "workbook.md"

GRADED_LABS = {
    1: "lab-01-digital-basics-orientation.md",
    2: "lab-02-hardware-inventory-benchmarking.md",
    3: "lab-03-file-system-scavenger-hunt.md",
    4: "lab-04-number-systems-workshop.md",
    5: "lab-05-logic-circuit-simulator.md",
    6: "lab-06-spreadsheet-data-workshop.md",
    7: "lab-07-networking-cloud-lab.md",
    8: "lab-08-security-habits-lab.md",
}
BUILDERS = {
    1: "sb-01-software-installation.md",
    2: "sb-02-database-thinking.md",
    3: "sb-03-computational-thinking-gym.md",
    4: "sb-04-responsible-ai.md",
}

GRADED_SECTIONS = [
    "## Purpose",
    "## Before you start",
    "## Expected observations and troubleshooting",
    "## Submission checklist",
    "## Grading",
]
GRADED_QUESTION_HEADING = re.compile(
    r"^## (Reflection questions|Questions)|^## Part \d+ — Reflection questions", re.MULTILINE
)
ACCESSIBILITY_PARA = re.compile(r"^\*\*Accessibility alternative:\*\*", re.MULTILINE)
BUILDER_SECTIONS = [
    "## Learning outcomes",
    "## Prerequisites and equipment",
    "## Step-by-step tasks",
    "## Expected observations",
    "## Questions",
    "## Troubleshooting",
    "## Submission and assessment",
]


def parse_front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm: dict = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm


def _ascii(s: str) -> str:
    return s.encode("ascii", "replace").decode("ascii")


def main() -> int:
    load_expectations()
    issues: list[str] = []

    if not WORKBOOK.is_file():
        print("FAIL: validate_lab_workbook — workbook.md missing")
        return 1
    wb = WORKBOOK.read_text(encoding="utf-8")

    # mapping table: 8 graded + 4 builders
    labs_listed = {int(m.group(1)) for m in
                   re.finditer(r"^\| \[Lab (\d+)\]", wb, flags=re.MULTILINE)}
    builders_listed = {int(m.group(1)) for m in
                       re.finditer(r"^\| \[SB-(\d+)\]", wb, flags=re.MULTILINE)}
    if labs_listed != set(GRADED_LABS):
        issues.append(f"workbook mapping graded labs mismatch: {sorted(labs_listed)}")
    if builders_listed != set(BUILDERS):
        issues.append(f"workbook mapping skill builders mismatch: {sorted(builders_listed)}")

    # coverage matrix: 22 numbered rows
    matrix_rows = re.findall(r"^\| (\d+) \| .+?\|$", wb, flags=re.MULTILINE)
    nums = [int(n) for n in matrix_rows]
    if nums != list(range(1, 23)):
        issues.append(f"coverage matrix rows not exactly 1..22: {nums[:5]}…{nums[-5:] if len(nums) > 5 else ''}")

    # rubric weights + safety rules
    if "60%" not in wb or "25%" not in wb or "15%" not in wb:
        issues.append("workbook rubric weights (60/25/15) not found")
    if "## Safety rules" not in wb:
        issues.append("workbook missing '## Safety rules'")
    if "## Accessibility and fallbacks" not in wb:
        issues.append("workbook missing '## Accessibility and fallbacks'")

    # graded handouts
    for num, fname in sorted(GRADED_LABS.items()):
        path = LABS_DIR / fname
        if not path.is_file():
            issues.append(f"missing graded lab handout: {fname}")
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        for key in ("lab", "title", "assigned", "due"):
            if key not in fm or not fm[key]:
                issues.append(f"{fname}: front-matter missing '{key}'")
        if fm.get("lab") != str(num):
            issues.append(f"{fname}: front-matter lab={fm.get('lab')!r}, expected {num}")
        for section in GRADED_SECTIONS:
            if section not in text:
                issues.append(f"{fname}: missing section '{section}'")
        if not GRADED_QUESTION_HEADING.search(text):
            issues.append(f"{fname}: no reflection/questions section")
        if not ACCESSIBILITY_PARA.search(text):
            issues.append(f"{fname}: missing '**Accessibility alternative:**' paragraph")
        if "## Submission checklist" in text and "- [ ]" not in text:
            issues.append(f"{fname}: submission checklist has no items")

    # skill builders
    for num, fname in sorted(BUILDERS.items()):
        path = LABS_DIR / fname
        if not path.is_file():
            issues.append(f"missing skill builder: {fname}")
            continue
        text = path.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        for key in ("lab", "title", "related", "duration", "graded"):
            if key not in fm or not fm[key]:
                issues.append(f"{fname}: front-matter missing '{key}'")
        if fm.get("lab") != f"SB-{num}":
            issues.append(f"{fname}: front-matter lab={fm.get('lab')!r}, expected SB-{num}")
        if fm.get("graded", "").lower() != "false":
            issues.append(f"{fname}: skill builders must be graded: false")
        for section in BUILDER_SECTIONS:
            if section not in text:
                issues.append(f"{fname}: missing section '{section}'")

    print(
        f"lab workbook: 8 graded handouts + {len(BUILDERS)} skill builders; "
        f"coverage matrix rows: {len(nums)}"
    )
    if issues:
        print("FAIL: validate_lab_workbook")
        for issue in issues:
            print(f"- {_ascii(issue)}")
        return 1
    print("PASS: validate_lab_workbook")
    return 0


if __name__ == "__main__":
    sys.exit(main())
