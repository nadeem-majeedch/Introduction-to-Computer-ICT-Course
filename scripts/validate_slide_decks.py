#!/usr/bin/env python3
"""Validate the PROMPT 04 slide-deck package (stdlib only).

Checks:
  - all 8 module deck files exist under instructor/slides/
  - a '## LNN — …' section with a '# LNN · …' title slide exists for every
    lecture L01..L32
  - each lecture has a '### Run sheet (120 min)' block stating 120 minutes
  - required slide types: a 'Today'/'Objectives' slide, an 'Activity' slide,
    a 'Quick check' slide, a 'Summary' slide, and exactly one 'Exit ticket'
    slide (the final numbered slide)
  - every slide has a '**Notes:**' line with a '[~minutes]' target and at
    least a TALK cue (TRAN required on all slides except the exit ticket)
  - slide headings follow the '## S# · …' grammar with clean S1..Sn numbering
  - no answer-key markers leak into decks (keys live in module guides)
"""
import re
import sys

from course_paths import INSTRUCTOR, load_expectations

SLIDES_DIR = INSTRUCTOR / "slides"
MODULE_RANGE = range(1, 9)

SLIDE_RE = re.compile(r"^## (S\d+) · (.+)$", re.MULTILINE)
SECTION_RE = re.compile(r"^## L(\d{2}) — .+$", re.MULTILINE)
TITLE_SLIDE_RE = re.compile(r"^# L(\d{2}) · .+$", re.MULTILINE)
RUN_SHEET_RE = re.compile(r"^### Run sheet \(120 min\)", re.MULTILINE)
NOTES_RE = re.compile(r"\*\*Notes:\*\*")
TIME_RE = re.compile(r"\[~\d+\]")
CUE_ALWAYS = ("TALK",)
CUE_NON_FINAL = ("TRAN",)

REQUIRED_SLIDE_KINDS = [
    ("objectives/today", re.compile(r"^(Today|Objectives|.*Learning objectives)", re.IGNORECASE)),
    ("activity", re.compile(r"^.*Activity", re.IGNORECASE)),
    ("quick check", re.compile(r"^Quick check", re.IGNORECASE)),
    ("summary", re.compile(r"^Summary", re.IGNORECASE)),
    ("exit ticket", re.compile(r"^Exit ticket", re.IGNORECASE)),
]

LEAK_PATTERNS = [
    re.compile(r"^\s*Answer(s| key)?\s*:", re.IGNORECASE),
    re.compile(r"^\s*Model answer\s*:", re.IGNORECASE),
    re.compile(r"^\s*With answers\s*:\s*$", re.IGNORECASE),
    re.compile(r"^\s*Marking scheme\s*:", re.IGNORECASE),
]

EXPECTED_LECTURES = set(range(1, 33))


def _ascii(s: str) -> str:
    """Keep CI logs ASCII-safe on all consoles."""
    return s.encode("ascii", "replace").decode("ascii")


def validate_lecture_section(num: int, section: str) -> list[str]:
    issues: list[str] = []
    if not RUN_SHEET_RE.search(section):
        issues.append(f"L{num:02d}: missing run sheet '### Run sheet (120 min)'")
    elif "120 min" not in section:
        issues.append(f"L{num:02d}: run sheet does not state 120 minutes")

    if not TITLE_SLIDE_RE.search(section):
        issues.append(f"L{num:02d}: missing deck title slide '# L{num:02d} · …'")

    slides = SLIDE_RE.findall(section)
    if len(slides) < 11:
        issues.append(f"L{num:02d}: only {len(slides)} slides (expected >= 11)")

    numbered = [s[0] for s in slides]
    expected_seq = [f"S{i}" for i in range(1, len(slides) + 1)]
    if numbered != expected_seq:
        issues.append(f"L{num:02d}: slide numbering not a clean S1..S{len(slides)} sequence")

    for kind, rx in REQUIRED_SLIDE_KINDS:
        if not any(rx.search(title) for _, title in slides):
            issues.append(f"L{num:02d}: no {kind} slide")

    if slides and "exit ticket" not in slides[-1][1].lower():
        issues.append(
            f"L{num:02d}: exit ticket is not the final slide (last is '{_ascii(slides[-1][1])}')"
        )

    # per-slide notes checks (slides are the only '## S# ·' blocks in the section)
    slide_blocks = re.split(r"^## ", section, flags=re.MULTILINE)[1:]
    for block in slide_blocks:
        header = block.splitlines()[0]
        m = re.match(r"(S\d+) · (.+)", header)
        if not m:
            continue
        title = m.group(2).strip()
        body = "\n".join(block.splitlines()[1:])
        notes = NOTES_RE.search(body)
        if not notes:
            issues.append(f"L{num:02d} · {_ascii(title)}: slide has no **Notes:** line")
            continue
        segment = body[notes.start():]
        if not TIME_RE.search(segment):
            issues.append(f"L{num:02d} · {_ascii(title)}: notes lack a [~minutes] target")
        cues = CUE_ALWAYS
        if "exit ticket" not in title.lower():
            cues += CUE_NON_FINAL
        missing = [c for c in cues if f"{c}:" not in segment]
        if missing:
            issues.append(f"L{num:02d} · {_ascii(title)}: notes missing cues {', '.join(missing)}")
        for pattern in LEAK_PATTERNS:
            if any(pattern.match(line) for line in body.splitlines()):
                issues.append(f"L{num:02d} · {_ascii(title)}: possible answer-key marker")

    return issues


def validate_deck(path) -> tuple[set[int], list[str]]:
    text = path.read_text(encoding="utf-8")
    positions = [(m.start(), int(m.group(1))) for m in SECTION_RE.finditer(text)]
    covered: set[int] = set()
    issues: list[str] = []

    for i, (start, num) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        section = text[start:end]
        if num in covered:
            issues.append(f"{path.name}: duplicate section for L{num:02d}")
        covered.add(num)
        issues.extend(validate_lecture_section(num, section))

    return covered, issues


def main() -> int:
    load_expectations()
    all_issues: list[str] = []
    covered: set[int] = set()

    files = sorted(SLIDES_DIR.glob("module-*-slides.md"))
    if len(files) != len(MODULE_RANGE):
        all_issues.append(
            f"expected {len(MODULE_RANGE)} module deck files, found {len(files)}: "
            f"{[f.name for f in files]}"
        )

    for path in files:
        lectures, issues = validate_deck(path)
        covered |= lectures
        all_issues.extend(f"{path.name}: {issue}" for issue in issues)

    missing = EXPECTED_LECTURES - covered
    if missing:
        all_issues.append(f"no deck found for lectures: {sorted(missing)}")
    unexpected = covered - EXPECTED_LECTURES
    if unexpected:
        all_issues.append(f"decks reference unknown lectures: {sorted(unexpected)}")

    print(f"slide decks: {len(files)} module files; lectures covered: {len(covered)}/32")
    if all_issues:
        print("FAIL: validate_slide_decks")
        for issue in all_issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_slide_decks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
