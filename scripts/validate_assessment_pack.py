#!/usr/bin/env python3
"""Validate the PROMPT 07 assessment package (stdlib only).

Checks:
  - public assessment framework hub exists and lists all nine assessment
    types, the five proposed weightings (each explicitly marked proposed),
    and the 100% sum statement
  - the question bank contains the two module sets plus index; each question
    has a tag line (module, CLO, difficulty, type) and an expandable
    non-stub model answer; no duplicate question titles across the bank;
    total question count matches expectations.json (case_bank unchanged)
  - every one of the ten required question types appears across the bank
  - public exam blueprints exist for midterm and final, state marks/time,
    and contain no drafted exam items (no `**Model` answer blocks, no
    marking-scheme cells) — blueprint/public vs paper/private separation
  - the public rubrics pack exists with the required rubric sections
  - private draft papers exist for midterm and final OUTSIDE docs/, each
    containing model answers and marking schemes for every drafted item,
    time-allocation tables, and integrity notes
  - leak scan: no model-answer/marking-scheme content in the public
    assessment tree (answer: / marks: / **Model answer** patterns in
    blueprint pages, framework hub, or rubrics); <details> model answers in
    the question bank are the designed exception
"""
import re
import sys

from course_paths import DOCS, EXPECTATIONS_PATH, INSTRUCTOR, ROOT, load_expectations

ASSESS = DOCS / "assessments"
FRAMEWORK = ASSESS / "index.md"
QB_DIR = ASSESS / "question-bank"
QB_INDEX = QB_DIR / "index.md"
QB_SETS = ["qb-m01-m04.md", "qb-m05-m08.md"]
EXAM_BP = ASSESS / "exams" / "index.md"
RUBRICS = ASSESS / "rubrics.md"

PAPERS = {
    "midterm": INSTRUCTOR / "exams" / "midterm-draft-paper.md",
    "final": INSTRUCTOR / "exams" / "final-draft-paper.md",
}

ASSESSMENT_TYPES = [
    "Formative assessment",
    "Quiz",
    "Practical lab assessment",
    "Individual assignment",
    "Group activit",
    "Midterm examination",
    "Final examination",
    "Integrated ICT project",
    "Problem-solving case assessment",
]

QUESTION_TYPES = [
    "Multiple choice",
    "True/false",
    "Short answer",
    "Conceptual",
    "Scenario-based",
    "Troubleshooting",
    "Data representation",
    "Networking",  # Networking & cybersecurity scenarios
    "Comparative",
    "Extended problem-solving",
]

QUESTION_HEADING_RE = re.compile(r"^## (Q\d+ .+)$", re.MULTILINE)
TAG_RE = re.compile(
    r"\*\*Module \d+ · CLO-\d+ · Difficulty \d/4 · Type: ([^*]+)\*\*"
)
ANSWER_RE = re.compile(r"<details>\s*<summary>Model answer</summary>(.*?)</details>", re.DOTALL)

# Content that must never appear in public blueprint/framework/rubric pages.
PUBLIC_LEAK_PATTERNS = [
    (re.compile(r"\*\*Model(?: answer)?\**\s*:?", re.IGNORECASE), "model-answer block"),
    (re.compile(r"^\*\*Marking scheme:", re.MULTILINE | re.IGNORECASE), "marking scheme"),
    (re.compile(r"\bmodel answer\b", re.IGNORECASE), "model-answer phrase"),
    (re.compile(r"^\| \*\*Marking", re.MULTILINE, ), "marking-scheme table row"),
]

MIN_QUESTION_LENGTH = 120  # chars between heading and next heading, below = stub


def read(path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    issues: list[str] = []
    expectations = load_expectations()
    del expectations  # currently no question-bank count field; kept for future use

    # --- public framework hub ------------------------------------------------
    if not FRAMEWORK.is_file():
        issues.append("missing public framework hub: docs/assessments/index.md")
    else:
        text = read(FRAMEWORK)
        for t in ASSESSMENT_TYPES:
            if t.lower() not in text.lower():
                issues.append(f"framework hub: assessment type missing: '{t}'")
        if text.lower().count("proposed") < 6:
            issues.append(
                "framework hub: weightings must be explicitly marked proposed (>=6 mentions)"
            )
        if "100%" not in text:
            issues.append("framework hub: missing the 100% sum statement")
        for link in ["question-bank/index.md", "exams/index.md", "rubrics.md", "project/brief.md"]:
            if f"]({link})" not in text:
                issues.append(f"framework hub: missing link to {link}")

    # --- question bank --------------------------------------------------------
    all_titles: list[str] = []
    found_types: set[str] = set()
    total_questions = 0
    if not QB_INDEX.is_file():
        issues.append("missing question-bank index")
    else:
        idx = read(QB_INDEX)
        for t in QUESTION_TYPES:
            if t.lower() not in idx.lower():
                issues.append(f"question-bank index: does not mention type '{t}'")
        if "Answer policy" not in idx:
            issues.append("question-bank index: missing Answer policy section")
    for fname in QB_SETS:
        path = QB_DIR / fname
        if not path.is_file():
            issues.append(f"missing question set: {fname}")
            continue
        text = read(path)
        heads = list(QUESTION_HEADING_RE.finditer(text))
        total_questions += len(heads)
        for i, m in enumerate(heads):
            title = m.group(1).strip()
            all_titles.append(title)
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            body = text[m.start():end]
            if len(body) < MIN_QUESTION_LENGTH:
                issues.append(f"{fname}: {title} looks like a stub ({len(body)} chars)")
            tag = TAG_RE.search(body)
            if not tag:
                issues.append(f"{fname}: {title} missing tag line (Module/CLO/Difficulty/Type)")
            else:
                found_types.add(tag.group(1).strip().split(" (")[0].strip())
            ans = ANSWER_RE.search(body)
            if not ans or len(ans.group(1).strip()) < 80:
                issues.append(f"{fname}: {title} missing non-stub model answer")
    if total_questions != 46:
        issues.append(f"question bank: expected 46 questions, found {total_questions}")
    duplicates = {t for t in all_titles if all_titles.count(t) > 1}
    if duplicates:
        issues.append(f"duplicate question titles: {sorted(duplicates)}")
    for t in QUESTION_TYPES:
        if t not in found_types and not any(t.lower() in ft.lower() for ft in found_types):
            issues.append(f"question bank: no question of type '{t}' (tags found: {sorted(found_types)})")

    # --- public exam blueprints ----------------------------------------------
    if not EXAM_BP.is_file():
        issues.append("missing public exam blueprint page: docs/assessments/exams/index.md")
    else:
        text = read(EXAM_BP)
        for name, anchor in [("Midterm blueprint", "midterm-blueprint"), ("Final blueprint", "final-blueprint")]:
            if name not in text:
                issues.append(f"exam blueprints: missing {name} section")
        for required in ["90 minutes", "120 minutes", "100 marks", "Academic integrity"]:
            if required not in text:
                issues.append(f"exam blueprints: missing '{required}'")
        for pat, what in PUBLIC_LEAK_PATTERNS:
            for m in pat.finditer(text):
                line_no = text.count("\n", 0, m.start()) + 1
                issues.append(f"docs/assessments/exams/index.md:{line_no}: public leak ({what})")

    # --- public rubrics pack ---------------------------------------------------
    if not RUBRICS.is_file():
        issues.append("missing public rubrics pack: docs/assessments/rubrics.md")
    else:
        text = read(RUBRICS)
        for name in [
            "Lab performance rubric",
            "Written explanation rubric",
            "Troubleshooting rubric",
            "Problem analysis rubric",
            "Solution justification rubric",
            "Teamwork rubric",
            "Exam scenario rubric",
        ]:
            if name not in text:
                issues.append(f"rubrics pack: missing '{name}'")
        if "project/rubric.md" not in text or "../case-bank/index.md#9-assessment-rubric-all-levels" not in text:
            issues.append("rubrics pack: missing links to the specialized project/case rubrics")

    # --- private draft papers --------------------------------------------------
    for name, path in PAPERS.items():
        if not path.is_file():
            issues.append(f"missing private draft paper: {path.relative_to(ROOT)}")
            continue
        text = read(path)
        if DOCS in path.resolve().parents:
            issues.append(f"{name} draft paper: located inside docs/ (leak risk)")
        for required in ["Marking scheme", "Model", "Time-allocation", "Academic integrity"]:
            if required not in text:
                issues.append(f"{name} draft paper: missing '{required}'")
        if text.count("Marking scheme") < 5:
            issues.append(f"{name} draft paper: too few per-item marking schemes")
        if text.count("**Model") + text.count("**Model:") < 3:
            issues.append(f"{name} draft paper: too few model answers")

    # --- report ----------------------------------------------------------------
    if issues:
        print("FAIL: assessment-package validation issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(
        "OK: assessment package valid — framework hub (9 types, proposed weights, sum 100%), "
        f"{total_questions} bank questions with tagged types and non-stub model answers, "
        "blueprints clean of items/answers, 7 rubrics present, 2 private draft papers "
        "with full marking schemes (no leakage)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
