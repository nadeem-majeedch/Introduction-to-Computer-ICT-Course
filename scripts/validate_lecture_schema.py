#!/usr/bin/env python3
"""Validate the 32 lecture pages against the fixed template (stdlib only).

Checks per lecture file:
  - front-matter: lecture, module, title, stage, outcomes present and well-formed
  - single h1 matching 'LNN — Title'
  - required sections present
  - 3-5 learning objectives, each mapping to a CLO
  - at least 2 misconceptions, 3-5 check questions
"""
import re
import sys

from course_paths import DOCS, INSTRUCTOR, ROOT, load_expectations

LECTURES_DIR = DOCS / "lectures"
GUIDES_DIR = INSTRUCTOR / "module-guides"

REQUIRED_SECTIONS = [
    "## Learning objectives",
    "## Key terms",
    "## Common misconceptions",
    "## Check your understanding",
    "## References & further reading",
    "## Looking ahead",
]

# PROMPT 03 additions — full teaching-material contract per lecture.
REQUIRED_PROMPT03_SECTIONS = [
    "## Visual explanation",
    "## Summary",
    "## Homework",
]

# Lines that must never appear in student-facing files (answer keys live only
# in instructor/). Matched at line start to avoid false positives in prose.
KEY_LEAK_PATTERNS = [
    re.compile(r"^\s*Answer(s| key)?\s*:", re.IGNORECASE),
    re.compile(r"^\s*Model answer\s*:", re.IGNORECASE),
    re.compile(r"^\s*With answers\s*:", re.IGNORECASE),
    re.compile(r"^\s*Marking scheme\s*:", re.IGNORECASE),
]

FRONT_MATTER_KEYS = ["lecture", "module", "title", "stage", "outcomes"]


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    body = text[end + 4:]
    fm: dict = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip()
    return fm, body


def validate_lecture(path) -> list[str]:
    issues: list[str] = []
    name = path.name
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)

    for key in FRONT_MATTER_KEYS:
        if key not in fm or not fm[key]:
            issues.append(f"{name}: front-matter missing '{key}'")
    if fm:
        m = re.match(r"^L(\d{2})$", fm.get("lecture", ""))
        if not m:
            issues.append(f"{name}: front-matter 'lecture' not in LNN format")
        lecture_num = int(m.group(1)) if m else None
        expected_fname = f"L{lecture_num:02d}-" if lecture_num else None
        if expected_fname and not name.startswith(expected_fname):
            issues.append(f"{name}: file name does not match lecture {fm['lecture']}")
        if fm.get("outcomes", "").startswith("["):
            inner = fm["outcomes"].strip("[]")
            ids = [part.strip() for part in inner.split(",") if part.strip()]
            if not ids:
                issues.append(f"{name}: empty outcomes list")
            for clo in ids:
                if not re.match(r"^CLO-\d+$", clo):
                    issues.append(f"{name}: bad outcome id '{clo}'")
        else:
            issues.append(f"{name}: outcomes must be a YAML list")

    h1s = re.findall(r"^# (.+)$", body, flags=re.MULTILINE)
    if len(h1s) != 1:
        issues.append(f"{name}: expected exactly one h1, found {len(h1s)}")
    elif fm:
        h1 = h1s[0].strip()
        if not re.match(r"^L\d{2} — .+$", h1):
            issues.append(f"{name}: h1 must match 'LNN — Title' pattern")
        elif not h1.endswith(fm.get("title", "").strip()):
            issues.append(
                f"{name}: h1 '{h1}' does not end with front-matter title "
                f"'{fm.get('title', '')}'"
            )

    for section in REQUIRED_SECTIONS:
        if section not in body:
            issues.append(f"{name}: missing required section '{section}'")
    for section in REQUIRED_PROMPT03_SECTIONS:
        if section not in body:
            issues.append(f"{name}: missing teaching-material section '{section}'")

    # Prerequisites & motivation: the NN.0 bridge section
    lecture_num = int(m.group(1)) if (m := re.match(r"^L(\d{2})-", name)) else 0
    if lecture_num:
        bridge = f"## {lecture_num}.0 Before we start"
        if bridge not in body:
            issues.append(f"{name}: missing prerequisites/motivation section '{bridge}'")

    # Visual explanation must carry a Mermaid diagram and a text alternative
    if "## Visual explanation" in body:
        block = body.split("## Visual explanation", 1)[1]
        block = block.split("\n## ", 1)[0]
        if "```mermaid" not in block:
            issues.append(f"{name}: 'Visual explanation' has no mermaid diagram")
        if not re.search(r"\*Figure:\s*\S", block):
            issues.append(
                f"{name}: 'Visual explanation' lacks a '*Figure: …' text alternative (alt text)"
            )

    # Summary/Homework must be non-empty
    for section in ("## Summary", "## Homework"):
        if section in body:
            block = body.split(section, 1)[1].split("\n## ", 1)[0]
            if len(block.strip()) < 40:
                issues.append(f"{name}: '{section.strip('# ')}' section is empty or a stub")

    # Answer-key leak scan (student-facing pages must not carry answers)
    for line in body.splitlines():
        for pattern in KEY_LEAK_PATTERNS:
            if pattern.match(line):
                issues.append(f"{name}: possible answer-key leak: {line.strip()[:70]}")

    # Learning objectives: 3-5 numbered items each mapping to a CLO
    m = re.search(
        r"## Learning objectives\n(.*?)(?=\n## )", body, flags=re.DOTALL
    )
    if m:
        block = m.group(1)
        items = re.findall(r"^\d+\.\s+(.+)$", block, flags=re.MULTILINE)
        if not (3 <= len(items) <= 5):
            issues.append(f"{name}: expected 3-5 learning objectives, found {len(items)}")
        for item in items:
            if not re.search(r"\([^)]*CLO-\d+[^)]*\)", item):
                issues.append(f"{name}: objective without CLO mapping: '{item[:60]}…'")
    else:
        issues.append(f"{name}: cannot parse Learning objectives section")

    # Misconceptions: at least 2 numbered items
    m = re.search(
        r"## Common misconceptions\n(.*?)(?=\n## )", body, flags=re.DOTALL
    )
    if m:
        items = re.findall(r"^\d+\.\s+", m.group(1), flags=re.MULTILINE)
        if len(items) < 2:
            issues.append(f"{name}: expected >=2 misconceptions, found {len(items)}")
    else:
        issues.append(f"{name}: cannot parse Common misconceptions section")

    # Check your understanding: 3-5 questions
    m = re.search(
        r"## Check your understanding\n(.*?)(?=\n## )", body, flags=re.DOTALL
    )
    if m:
        items = re.findall(r"^\d+\.\s+", m.group(1), flags=re.MULTILINE)
        if not (3 <= len(items) <= 5):
            issues.append(f"{name}: expected 3-5 check questions, found {len(items)}")
    else:
        issues.append(f"{name}: cannot parse Check your understanding section")

    return issues


def main() -> int:
    expectations = load_expectations()
    expected = expectations["lectures"]
    files = sorted(LECTURES_DIR.glob("L*.md"))
    all_issues: list[str] = []

    numbering = sorted(
        int(m.group(1))
        for f in files
        if (m := re.match(r"^L(\d{2})-", f.name))
    )
    if numbering != list(range(1, expected + 1)):
        all_issues.append(
            f"lecture numbering is not a gap-free 1..{expected} sequence: {numbering}"
        )

    for path in files:
        all_issues.extend(validate_lecture(path))

    # PROMPT 03: every module must have its instructor teaching guide (private tree)
    for module_num in range(1, 9):
        guide = GUIDES_DIR / f"module-{module_num:02d}-teaching-guide.md"
        if not guide.is_file():
            all_issues.append(
                f"missing instructor module guide for module {module_num}: {guide}"
            )

    print(f"lecture pages found: {len(files)} (expected {expected})")
    if len(files) != expected:
        all_issues.append(f"expected {expected} lecture pages, found {len(files)}")
    if all_issues:
        print("FAIL: validate_lecture_schema")
        for issue in all_issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_lecture_schema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
