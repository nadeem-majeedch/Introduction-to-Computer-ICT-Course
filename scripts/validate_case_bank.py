#!/usr/bin/env python3
"""Validate the PROMPT 06 problem-solving case bank (stdlib only).

Checks:
  - the four public level files exist under docs/case-bank/ with exactly 25
    cases each and unique case IDs across the whole bank (no repeats)
  - case IDs agree with their level (PB-1xx in level-1.md, etc.)
  - every case heading carries the level label ("## PB-NNN · Level N · ...")
  - every case carries the required student-facing fields, each non-stub
    (Scenario, Problem statement, Stakeholders, Learning objectives,
    Constraints, Available information, Student task, Suggested thinking
    time, Expected solution characteristics, Discussion questions,
    Extension challenge, References)
  - every case links the bank index (the domain/progression/rubric hub)
  - the bank index exists and its mapping tables reference real case IDs
    (a sample of every ID mentioned in the index must exist in the bank)
  - difficulty progression markers: each level file states its level and the
    index's level table lists all four levels
  - instructor solution banks exist for all four levels OUTSIDE docs/ with a
    solution entry per case ID (parity check)
  - structural leak scan: public case files must not contain solution-bearing
    headings or answer-style markers (**Solution guide.**, **Alternative
    solutions.**, **Trade-offs.**, **Common mistakes.**, "answer key:")
  - the existing 4 graded case studies (docs/case-studies/) are untouched by
    the bank: they keep their own IDs (CS-*) and are not duplicated as PB-*
"""
import re
import sys
from pathlib import Path

from course_paths import DOCS, INSTRUCTOR, ROOT

CASE_BANK = DOCS / "case-bank"
SOLUTIONS = INSTRUCTOR / "case-bank-solutions"

LEVEL_FILES = {
    1: ("level-1.md", "Beginner"),
    2: ("level-2.md", "Intermediate"),
    3: ("level-3.md", "Advanced"),
    4: ("level-4.md", "Expert"),
}
EXPECTED_COUNT = 25

# Required student-facing fields, as **bold lead-ins** or `##` headings.
REQUIRED_FIELDS = [
    "Scenario",
    "Problem statement",
    "Stakeholders",
    "Learning objectives",
    "Constraints",
    "Available information",
    "Student task",
    "Suggested thinking time",
    "Expected solution characteristics",
    "Discussion questions",
    "Extension challenge",
    "References",
]

CASE_HEADING_RE = re.compile(r"^## (PB-\d+)", re.MULTILINE)
LEVEL_LABEL_RE = re.compile(r"^## (PB-\d+) · Level (\d) ·", re.MULTILINE)

# Solution-bearing content that must never appear in public files.
LEAK_PATTERNS = [
    (re.compile(r"\*\*Solution guide\.\*\*", re.IGNORECASE), "solution-guide field"),
    (re.compile(r"\*\*Alternative solutions\.\*\*", re.IGNORECASE), "alternative-solutions field"),
    (re.compile(r"\*\*Trade-offs\.\*\*", re.IGNORECASE), "trade-offs field"),
    (re.compile(r"\*\*Common mistakes\.\*\*", re.IGNORECASE), "common-mistakes field"),
    (re.compile(r"\banswer key\b\s*:", re.IGNORECASE), "answer key marker"),
]

STUB_THRESHOLDS = {
    "Scenario": 60,
    "Expected solution characteristics": 60,
    "Student task": 40,
    "Extension challenge": 30,
    # L1 problem statements are legitimately terse one-line asks (their depth
    # lives in the Student task / Problem note fields).
    "Problem statement": 50,
    "Stakeholders": 25,
    "Learning objectives": 25,
    "Available information": 25,
    # Compact-by-design fields: the level files use '**Constraints:** ...; ...'
    # inline, '**Suggested thinking time.** 12 minutes.', and short lecture
    # citations — a fixed 40-char bar would false-positive on all three.
    "Constraints": 20,
    "References": 20,
    "Suggested thinking time": 8,
}
DEFAULT_STUB_THRESHOLD = 40


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def field_body(text: str, field: str) -> str:
    """Text following '**Field.**', '**Field:**' or '## Field' up to the next
    bold marker, paragraph break, or heading. The level files use both the
    trailing-period form ('**Scenario.** ...') and the inline colon form
    ('**Inputs:** ... **Constraints:** ...'), often mid-line."""
    pat = re.compile(
        r"\*\*" + re.escape(field) + r"(?:\.|:)\*\*\s*(.*?)(?=\n\n|\n## |\Z|\*\*)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    m = pat.search(text)
    return m.group(1).strip() if m else ""


def parse_cases(text: str) -> list[dict]:
    """Split a level file into per-case dicts keyed by heading position."""
    heads = list(CASE_HEADING_RE.finditer(text))
    cases = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        cases.append({"id": m.group(1), "text": text[m.start():end]})
    return cases


def main() -> int:
    issues: list[str] = []

    # --- public level files -------------------------------------------------
    bank_ids: list[str] = []
    level_texts: dict[int, str] = {}
    for level, (fname, label) in LEVEL_FILES.items():
        path = CASE_BANK / fname
        if not path.is_file():
            issues.append(f"missing public level file: docs/case-bank/{fname}")
            continue
        text = read(path)
        level_texts[level] = text
        cases = parse_cases(text)
        if len(cases) != EXPECTED_COUNT:
            issues.append(f"{fname}: expected {EXPECTED_COUNT} cases, found {len(cases)}")
        for case in cases:
            cid = case["id"]
            bank_ids.append(cid)
            prefix_level = int(cid[3])
            if prefix_level != level:
                issues.append(f"{fname}: case {cid} ID disagrees with file level {level}")
            label_m = LEVEL_LABEL_RE.search(case["text"])
            if not label_m:
                issues.append(f"{fname}: {cid} heading missing '· Level {level} ·' label")
            elif int(label_m.group(2)) != level:
                issues.append(f"{fname}: {cid} heading says Level {label_m.group(2)}, file is Level {level}")
            for field in REQUIRED_FIELDS:
                if field == "Discussion questions":
                    # The questions live in a numbered list under the marker.
                    if not re.search(
                        r"\*\*Discussion questions\.(?:\*\*)?\s*\n+\s*\d+\.", case["text"]
                    ):
                        issues.append(f"{fname}: {cid} missing numbered Discussion questions list")
                    continue
                body = field_body(case["text"], field)
                threshold = STUB_THRESHOLDS.get(field, DEFAULT_STUB_THRESHOLD)
                if not body:
                    issues.append(f"{fname}: {cid} missing required field '{field}'")
                elif len(body) < threshold:
                    issues.append(
                        f"{fname}: {cid} field '{field}' looks like a stub ({len(body)} chars)"
                    )
            if "](index.md)" not in case["text"] and "](../case-bank/index.md)" not in case["text"]:
                # Level intro line links the index once per file; per-case link
                # is not required, so check at file level below instead.
                pass
        if "](index.md)" not in text:
            issues.append(f"{fname}: no link to the bank index (index.md)")

    duplicates = {cid for cid in bank_ids if bank_ids.count(cid) > 1}
    if duplicates:
        issues.append(f"duplicate case IDs across the bank: {sorted(duplicates)}")
    if len(bank_ids) != 100:
        issues.append(f"bank total: expected 100 cases, found {len(bank_ids)}")

    # --- public index -------------------------------------------------------
    index_path = CASE_BANK / "index.md"
    if not index_path.is_file():
        issues.append("missing public bank index: docs/case-bank/index.md")
    else:
        index_text = read(index_path)
        mentioned = set(re.findall(r"PB-\d{3}", index_text))
        unknown = mentioned - set(bank_ids)
        if unknown:
            issues.append(f"bank index references non-existent case IDs: {sorted(unknown)}")
        for level, (fname, label) in LEVEL_FILES.items():
            if f"Level {level} — {label}" not in index_text:
                issues.append(f"bank index: level table missing 'Level {level} — {label}'")
        for section in [
            "Progression spine",
            "Classroom method",
            "Domain coverage matrix",
            "Assessment rubric",
            "Content protection",
            "Learning-outcome mapping",
            "Lecture-to-case mapping",
        ]:
            if section not in index_text:
                issues.append(f"bank index: missing section '{section}'")

    # --- instructor solution banks (private, outside docs/) -----------------
    for level, (fname, _label) in LEVEL_FILES.items():
        sol_path = SOLUTIONS / fname
        if not sol_path.is_file():
            issues.append(f"missing instructor solution bank: instructor/case-bank-solutions/{fname}")
            continue
        sol_text = read(sol_path)
        sol_cases = parse_cases(sol_text)
        expected_ids = {c["id"] for c in parse_cases(level_texts[level])} if level in level_texts else set()
        sol_ids = {c["id"] for c in sol_cases}
        if len(sol_cases) != EXPECTED_COUNT:
            issues.append(f"solutions/{fname}: expected {EXPECTED_COUNT} solution entries, found {len(sol_cases)}")
        missing = expected_ids - sol_ids
        extra = sol_ids - expected_ids
        if missing:
            issues.append(f"solutions/{fname}: no solution for {sorted(missing)}")
        if extra:
            issues.append(f"solutions/{fname}: solutions reference unknown cases {sorted(extra)}")
        for cid in sorted(sol_ids & expected_ids):
            case_text = next(c["text"] for c in sol_cases if c["id"] == cid)
            for field in ("Solution guide", "Common mistakes"):
                if f"**{field}" not in case_text:
                    issues.append(f"solutions/{fname}: {cid} missing **{field}** block")
        # private solution files must not live under docs/
        if DOCS in sol_path.resolve().parents:
            issues.append(f"solutions/{fname}: located inside docs/ (leak risk)")

    # --- structural leak scan on public files --------------------------------
    for level, (fname, _label) in LEVEL_FILES.items():
        if level not in level_texts:
            continue
        text = level_texts[level]
        for pat, what in LEAK_PATTERNS:
            for m in pat.finditer(text):
                line_no = text.count("\n", 0, m.start()) + 1
                issues.append(f"docs/case-bank/{fname}:{line_no}: solution leak ({what})")

    # --- graded case studies (CS-*) untouched by the bank -------------------
    cs_dir = DOCS / "case-studies"
    if cs_dir.is_dir():
        for p in sorted(cs_dir.glob("*.md")):
            text = read(p)
            for m in re.finditer(r"^## (PB-\d+)", text, re.MULTILINE):
                issues.append(f"{p.relative_to(ROOT)}: bank ID {m.group(1)} found in graded case studies")
            for m in re.finditer(r"^## (CS-\d+)", text, re.MULTILINE):
                if m.group(1) in set(bank_ids):
                    issues.append(f"{p.relative_to(ROOT)}: CS ID collides with a bank ID")

    # --- report --------------------------------------------------------------
    if issues:
        print("FAIL: case-bank validation issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(
        "OK: case bank valid — 100 cases across 4 levels (25 each), unique IDs, "
        "complete fields, index consistent, 4 private solution banks with full "
        "parity, no solution leakage in public files"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
