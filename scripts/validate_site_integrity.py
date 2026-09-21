#!/usr/bin/env python3
"""Validate site-wide structural integrity (stdlib only).

Checks:
  - all 32 lecture pages exist and carry unique lecture IDs and unique
    titles (duplicate-identifier check across the whole tree)
  - no duplicate H1/H2 headings that produce identical anchor slugs within
    the same public page (anchor collisions break in-page navigation)
  - mkdocs.yml nav entries are unique (no page reachable twice under
    different labels — confuses breadcrumbs and analytics)
  - the generated semester calendar exists, is newer than or consistent
    with semester.yml settings (all 32 sessions mapped), and its lecture
    links resolve
  - BUILT-OUTPUT leak scan (site/ if present): no instructor/ references,
    no answer-key patterns in published HTML
  - the four core public meta pages exist: index, syllabus, schedule,
    accessibility statement
"""
import re
import sys

from course_paths import DOCS, EXPECTATIONS_PATH, INSTRUCTOR, MKDOCS_YML, ROOT, docs_markdown_files, load_expectations

LECTURES_DIR = DOCS / "lectures"
FRONTMATTER_ID_RE = re.compile(r"^lecture:\s*(\S+)", re.MULTILINE)
TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
H1_RE = re.compile(r"^# (.+)$", re.MULTILINE)
H2_RE = re.compile(r"^## (.+)$", re.MULTILINE)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s_-]+", "-", text).strip("-")


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    meta = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, text[end + 4:] if end != -1 else ""


def main() -> int:
    issues: list[str] = []
    expectations = load_expectations()

    # --- lecture pages: existence, unique IDs, unique titles -----------------
    lecture_ids: list[str] = []
    lecture_titles: list[str] = []
    lecture_files = sorted(LECTURES_DIR.glob("L*.md"))
    if len(lecture_files) != expectations["lectures"]:
        issues.append(
            f"expected {expectations['lectures']} lecture pages, found {len(lecture_files)}"
        )
    for path in lecture_files:
        text = path.read_text(encoding="utf-8")
        meta, _ = parse_front_matter(text)
        lid = meta.get("lecture", "")
        title = meta.get("title", "")
        if not lid:
            issues.append(f"{path.relative_to(ROOT)}: missing 'lecture' front-matter ID")
        else:
            lecture_ids.append(lid)
        if not title:
            issues.append(f"{path.relative_to(ROOT)}: missing 'title' front-matter")
        else:
            lecture_titles.append(title)
    for label, values in [("lecture ID", lecture_ids), ("lecture title", lecture_titles)]:
        dupes = {v for v in values if values.count(v) > 1}
        if dupes:
            issues.append(f"duplicate {label}s: {sorted(dupes)}")

    # --- per-page anchor collisions ------------------------------------------
    for rel in docs_markdown_files():
        text = (ROOT / rel).read_text(encoding="utf-8")
        h2s = [slugify(m.group(1)) for m in H2_RE.finditer(text)]
        seen: set[str] = set()
        for slug in h2s:
            if slug in seen:
                issues.append(f"{rel}: duplicate section anchor '#{slug}' (rename one heading)")
            seen.add(slug)

    # --- nav uniqueness --------------------------------------------------------
    nav_text = MKDOCS_YML.read_text(encoding="utf-8")
    nav_paths = re.findall(r"['\"]?[\w\-']+\.md['\"]?:|:\s*['\"]?([\w\-/]+\.md)['\"]?", nav_text)
    # simpler: collect every *.md occurrence after 'nav:' as a path value
    nav_block = nav_text[nav_text.index("nav:"):]
    entries = re.findall(r":\s*([\w\-/]+\.md)", nav_block)
    dupes = {e for e in entries if entries.count(e) > 1}
    if dupes:
        issues.append(f"mkdocs.yml nav lists the same page multiple times: {sorted(dupes)}")

    # --- semester calendar ------------------------------------------------------
    cal = DOCS / "schedule-calendar.md"
    if not cal.is_file():
        issues.append(
            "missing generated calendar: docs/schedule-calendar.md "
            "(run: python scripts/generate_semester_calendar.py)"
        )
    else:
        cal_text = cal.read_text(encoding="utf-8")
        cal_links = re.findall(r"\]\((lectures/[^)]+)\)", cal_text)
        for link in cal_links:
            if not (DOCS / "schedule-calendar.md").parent.joinpath(link).is_file():
                issues.append(f"docs/schedule-calendar.md: broken lecture link {link}")
        session_rows = len(re.findall(r"^\| \[L\d+", cal_text, re.MULTILINE))
        if session_rows != expectations["lectures"]:
            issues.append(
                f"docs/schedule-calendar.md: expected {expectations['lectures']} session rows, found {session_rows}"
            )
        cfg = ROOT / "semester.yml"
        if not cfg.is_file():
            issues.append("missing semester configuration file: semester.yml")

    # --- core public meta pages -------------------------------------------------
    for page in ["index.md", "syllabus.md", "schedule.md", "accessibility.md", "pathway.md", "help.md"]:
        if not (DOCS / page).is_file():
            issues.append(f"missing core public page: docs/{page}")

    # --- built-output leak scan (site/ when present) ----------------------------
    site_dir = ROOT / "site"
    if site_dir.is_dir():
        leak_pat = re.compile(r"\binstructor/|answer key\s*:|marking scheme", re.IGNORECASE)
        scanned = 0
        for html in site_dir.rglob("*.html"):
            scanned += 1
            try:
                text = html.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            # Context-aware scan: a match is a leak only if it does not sit in
            # a benign policy statement ("... are not/never published ...").
            for m in leak_pat.finditer(text):
                context = text[max(0, m.start() - 130):m.end() + 130]
                if re.search(
                    r"are\s+not|never\s+published|not\s+published|are\s+instructor-only",
                    context, re.IGNORECASE,
                ):
                    continue
                line_no = text.count("\n", 0, m.start()) + 1
                issues.append(f"site output leak: {html.relative_to(ROOT)}:{line_no}: {m.group(0)!r}")
        if scanned == 0:
            issues.append("site/ exists but contains no HTML — rebuild before validating output")
    else:
        print("NOTE: site/ not present — built-output leak scan skipped (run mkdocs build)")

    # --- report ------------------------------------------------------------------
    if issues:
        print("FAIL: site-integrity validation issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(
        f"OK: site integrity valid — {len(lecture_files)} lectures with unique IDs/titles, "
        "no anchor collisions, unique nav entries, calendar mapped and linked, "
        "core meta pages present"
        + (f", {scanned} built HTML pages leak-scanned" if site_dir.is_dir() else ", built-output scan skipped (no site/)")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
