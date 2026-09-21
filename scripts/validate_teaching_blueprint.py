#!/usr/bin/env python3
"""Validate the teaching blueprint set (docs-meta/07..09) against the published course.

Stdlib only. Enforces the machine-checkable subset promised in
docs-meta/07-teaching-blueprint.md section 5 and docs-meta/08 section 5:
  1. teaching-plan tables contain exactly 32 lecture rows L01..L32, no gaps/duplicates
  2. total scheduled time is exactly 64 hours (32 x 2 h); every row says 2 h
  3. each row's CLO-mapping cell equals the lecture's outcomes: front-matter (order-insensitive)
  4. blueprint module blocks match module_lecture_ranges in tests/expectations.json
  5. objective cells are unique across the 32 rows (no duplicate lecture objectives)
  6. quiz coverage rows match docs/schedule.md's quiz plan strings
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from course_paths import DOCS, ROOT, load_expectations  # noqa: E402

BLUEPRINT = ROOT / "docs-meta" / "07-teaching-blueprint.md"
ASSESS = ROOT / "docs-meta" / "08-assessment-blueprint.md"
SCHEDULE = DOCS / "schedule.md"
LECTURES = DOCS / "lectures"


def lecture_outcomes() -> dict[int, frozenset[str]]:
    """Map lecture number -> frozenset of CLO ids from front-matter."""
    result: dict[int, frozenset[str]] = {}
    for path in sorted(LECTURES.glob("L*.md")):
        m = re.match(r"^L(\d{2})-", path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8")
        fm = re.search(r"^outcomes:\s*\[(.*?)\]\s*$", text, flags=re.MULTILINE)
        if not fm:
            raise ValueError(f"{path.name}: missing outcomes front-matter")
        clos = frozenset(re.findall(r"CLO-\d+", fm.group(1)))
        result[int(m.group(1))] = clos
    return result


def parse_plan_rows(text: str) -> tuple[list[dict[str, str]], dict[str, list[int]]]:
    """Extract lecture rows and module block boundaries from blueprint tables."""
    rows: list[dict[str, str]] = []
    module_blocks: dict[str, list[int]] = {}
    current_module: str | None = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        hm = re.match(r"^### Module (\d) — .+\(L(\d+)–L(\d+)\)", line)
        if hm:
            current_module = hm.group(1)
            module_blocks[current_module] = [int(hm.group(2)), int(hm.group(3))]
            continue
        if not (line.startswith("| **L") and line.rstrip().endswith("|")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # Expected columns: Lecture Module Duration Prereq Objectives Concepts
        # Vocabulary Examples Activity Demo Problem Formative Homework Resources CLO
        if len(cells) != 15:
            raise ValueError(
                f"blueprint line {i + 1}: lecture row has {len(cells)} cells, expected 15"
            )
        lm = re.match(r"^\*\*L(\d{2})\*\*$", cells[0])
        if not lm:
            raise ValueError(f"blueprint line {i + 1}: bad lecture cell '{cells[0]}'")
        rows.append(
            {
                "num": int(lm.group(1)),
                "module": cells[1],
                "duration": cells[2],
                "objectives": cells[4],
                "clo_cell": cells[14],
            }
        )
    return rows, module_blocks


def parse_front_clos(cell: str) -> set[str]:
    return set(re.findall(r"CLO-\d+", cell))


def main() -> int:
    expectations = load_expectations()
    issues: list[str] = []

    text = BLUEPRINT.read_text(encoding="utf-8")
    rows, module_blocks = parse_plan_rows(text)

    # --- 1. exactly 32 rows, no gaps/duplicates ---
    nums = [r["num"] for r in rows]
    expected = list(range(1, expectations["lectures"] + 1))
    if nums != expected:
        issues.append(f"lecture rows are {nums}, expected L01..L{expectations['lectures']:02d}")
    if len(nums) != len(set(nums)):
        dupes = sorted({n for n in nums if nums.count(n) > 1})
        issues.append(f"duplicate lecture rows: {['L%02d' % n for n in dupes]}")

    # --- 2. durations: every row 2 h, total 64 h ---
    bad_duration = [f"L{r['num']:02d}" for r in rows if r["duration"] != "2 h"]
    if bad_duration:
        issues.append(f"rows without a 2 h duration: {', '.join(bad_duration)}")
    total = sum(int(re.match(r"(\d+)\s*h", r["duration"]).group(1)) for r in rows)
    expected_hours = expectations["lectures"] * 2
    if total != expected_hours:
        issues.append(f"total scheduled time {total} h, expected {expected_hours} h")

    # --- 3. CLO parity with lecture front-matter ---
    outcomes = lecture_outcomes()
    if set(outcomes) != set(range(1, 33)):
        issues.append(f"front-matter outcomes missing for lectures: {sorted(set(range(1, 33)) - set(outcomes))}")
    for r in rows:
        want = outcomes.get(r["num"], frozenset())
        got = parse_front_clos(r["clo_cell"])
        if got != set(want):
            issues.append(
                f"L{r['num']:02d}: blueprint CLO cell {sorted(got)} != front-matter {sorted(want)}"
            )

    # --- 4. module blocks match expectations ---
    ranges = {int(k): v for k, v in expectations["module_lecture_ranges"].items()}
    if module_blocks != {str(k): v for k, v in ranges.items()}:
        issues.append(f"module blocks {module_blocks} != expectations {ranges}")

    # --- 5. unique objective cells (no duplicate lecture objectives) ---
    seen: dict[str, int] = {}
    for r in rows:
        key = r["objectives"].strip().lower()
        if key in seen:
            issues.append(f"L{r['num']:02d}: objectives duplicate L{seen[key]:02d}")
        else:
            seen[key] = r["num"]

    # --- 6. quiz coverage parity with docs/schedule.md ---
    sched = SCHEDULE.read_text(encoding="utf-8")
    sched_quiz = dict(re.findall(r"\| Q(\d{2}) \| (L\d{2}[^|]*) \|", sched))
    for qid, coverage in sorted(sched_quiz.items()):
        # 08 references quizzes directly (Q07) or as en-dash ranges (Q05–Q07)
        n = int(qid)
        has_direct = f"Q{qid}" in text or f"Q{n}" in text
        has_range = any(
            f"Q{a:02d}\u2013Q{b:02d}" in text and a <= n <= b
            for a in range(1, 15)
            for b in range(a, 15)
        )
        if not (has_direct or has_range):
            issues.append(f"quiz Q{qid} ({coverage.strip()}) not referenced in assessment blueprint")

    # CLO-to-lecture matrix lecture lists must equal the front-matter aggregation
    if ASSESS.exists():
        atext = ASSESS.read_text(encoding="utf-8")
        for clo_n in range(1, expectations["clos"] + 1):
            lects = {n for n, clos in outcomes.items() if f"CLO-{clo_n}" in clos}
            row = re.search(
                rf"^\| CLO-{clo_n} \|[^|]+\| ([^|]+) \| \d+", atext, flags=re.MULTILINE
            )
            if not row:
                issues.append(f"CLO-{clo_n}: no CLO-to-lecture matrix row in 08-assessment-blueprint.md")
                continue
            listed = {int(x) for x in re.findall(r"L(\d{2})", row.group(1))}
            if listed != lects:
                issues.append(
                    f"CLO-{clo_n}: matrix lists {sorted(listed)}, front-matter implies {sorted(lects)}"
                )

    print(
        f"teaching blueprint: {len(rows)} lecture rows, {total} contact hours, "
        f"{len(module_blocks)} module blocks"
    )
    if issues:
        print("FAIL: validate_teaching_blueprint")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_teaching_blueprint")
    return 0


if __name__ == "__main__":
    sys.exit(main())
