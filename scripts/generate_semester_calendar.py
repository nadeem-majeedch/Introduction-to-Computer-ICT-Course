#!/usr/bin/env python3
"""Generate the published semester calendar page from semester.yml.

Instructor workflow: edit semester.yml (semester start, lecture days, breaks,
holidays, assessment anchors), then run:

    python scripts/generate_semester_calendar.py

Outputs:
  - docs/schedule-calendar.md   (published; linked from the site nav)
  - docs-meta/semester-calendar-log.md  (internal generation log)

Design rules:
  - Lecture dates follow the configured lecture_days pattern, skipping
    break weeks and holidays — no academic-calendar assumptions are baked in.
  - Assessment milestones are anchored to LECTURE NUMBERS, so their dates
    move automatically when the semester start changes.
  - Sessions dated before the generation date are marked COMPLETED;
    later sessions are PLANNED (distinguishing the two is a render-time
    snapshot — regenerate to refresh).
  - The generator is idempotent and validated afterwards by
    scripts/validate_semester_calendar.py.
"""
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    import yaml  # PyYAML is already a mkdocs-material dependency
except ImportError:
    print("FAIL: PyYAML is required (it ships with the mkdocs-material install)")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "semester.yml"
LECTURES_DIR = ROOT / "docs" / "lectures"

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def parse_date(value: str) -> date:
    return datetime.strptime(str(value).strip(), "%Y-%m-%d").date()


def load_config() -> dict:
    with CONFIG.open(encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    for key in ("semester_start", "lecture_days", "lecture_count"):
        if key not in cfg:
            print(f"FAIL: semester.yml missing required key '{key}'")
            sys.exit(1)
    cfg["semester_start"] = parse_date(cfg["semester_start"])
    cfg["lecture_days"] = [int(d) for d in cfg["lecture_days"]]
    cfg["lecture_count"] = int(cfg["lecture_count"])
    cfg["break_weeks"] = [int(w) for w in cfg.get("break_weeks") or []]
    cfg["holidays"] = [parse_date(h) for h in (cfg.get("holidays") or [])]
    cfg["assessments"] = cfg.get("assessments") or []
    cfg["session_overrides"] = cfg.get("session_overrides") or []
    return cfg


def read_lectures() -> list[dict]:
    """Lecture metadata (number, module, title) from front matter."""
    lectures = []
    for path in sorted(LECTURES_DIR.glob("L*.md")):
        meta = {}
        with path.open(encoding="utf-8") as fh:
            text = fh.read()
        if text.startswith("---"):
            end = text.find("\n---", 3)
            for line in text[3:end].splitlines():
                if ":" in line:
                    key, _, value = line.partition(":")
                    meta[key.strip()] = value.strip()
        lectures.append(
            {
                "number": meta.get("lecture", path.stem),
                "module": int(meta.get("module", 0)),
                "title": meta.get("title", path.stem),
                "file": path.name,
            }
        )
    lectures.sort(key=lambda l: l["number"])
    return lectures


def session_dates(cfg: dict, count: int) -> list[date]:
    """The first `count` teaching dates: configured weekdays, skipping break
    weeks and holidays. Week 1 is the calendar week (Mon-based) containing the
    first teaching session."""
    dates: list[date] = []
    current = cfg["semester_start"]
    week1_monday = current - timedelta(days=current.weekday())
    holidays = set(cfg["holidays"])
    while len(dates) < count:
        week_number = ((current - week1_monday).days // 7) + 1
        if (
            current.weekday() in cfg["lecture_days"]
            and current >= cfg["semester_start"]
            and week_number not in cfg["break_weeks"]
            and current not in holidays
        ):
            dates.append(current)
        current += timedelta(days=1)
        # Guard: if a break skips everything, still advance year-by-year max
        if current.year > cfg["semester_start"].year + 2:
            print("FAIL: could not place all sessions within two years — check semester.yml")
            sys.exit(1)
    return dates


def apply_overrides(cfg: dict, mapping: dict[str, date]) -> None:
    for raw in cfg["session_overrides"]:
        try:
            lecture, _, value = str(raw).partition(":")
            mapping[lecture.strip()] = parse_date(value)
        except ValueError:
            print(f"WARN: unparseable session override ignored: {raw!r}")


def status_for(session_date: date, generated_on: date) -> str:
    return "COMPLETED" if session_date < generated_on else "PLANNED"


def fmt(d: date) -> str:
    return d.strftime("%a %d %b %Y")


def render_page(cfg: dict, lectures: list[dict], mapping: dict[str, date],
                module_bounds: dict[int, tuple[date, date]], generated_on: date,
                assessment_rows: list[tuple[str, str, str]]) -> str:
    lines: list[str] = [
        "# Semester Calendar — Lecture Dates",
        "",
        f"*Generated from `semester.yml` on {generated_on.isoformat()}. "
        "Dates are teaching dates for each lecture, mapped onto the configured "
        "semester pattern (see the note at the bottom). Instructors: edit "
        "`semester.yml` and re-run `python scripts/generate_semester_calendar.py` "
        "to change any date on this page.*",
        "",
        "| Lec | Module | Lecture title | Date | Week | Status |",
        "|---|---|---|---|---|---|",
    ]
    for lec in lectures:
        d = mapping.get(lec["number"])
        if d is None:
            continue
        week = ((d - (cfg["semester_start"] - timedelta(days=cfg["semester_start"].weekday()))).days // 7) + 1
        status = status_for(d, generated_on)
        lines.append(
            f"| [{lec['number']}](lectures/{lec['file']}) | {lec['module']} "
            f"| {lec['title']} | {fmt(d)} | {week} | {status} |"
        )
    lines += [
        "",
        "## Assessment milestones",
        "",
        "| Milestone | Anchored to | Date |",
        "|---|---|---|",
    ]
    for milestone, anchor, when in assessment_rows:
        lines.append(f"| {milestone} | {anchor} | {when} |")
    lines += [
        "",
        "## Module windows",
        "",
        "| Module | First session | Last session |",
        "|---|---|---|",
    ]
    for mod in sorted(module_bounds):
        first, last = module_bounds[mod]
        lines.append(f"| Module {mod} | {fmt(first)} | {fmt(last)} |")
    lines += [
        "",
        "---",
        "",
        "**How the dates were derived.** Teaching sessions fall on the weekdays "
        "configured in `semester.yml` ("
        + ", ".join(WEEKDAY_NAMES[d] for d in cfg["lecture_days"])
        + "), starting "
        + cfg["semester_start"].isoformat()
        + "; the generator skips configured break weeks ("
        + (", ".join(str(w) for w in cfg["break_weeks"]) or "none")
        + ") and holidays ("
        + (", ".join(d.isoformat() for d in cfg["holidays"]) or "none")
        + "). Assessment milestones are anchored to lecture numbers, so they "
        "shift automatically with the semester start. COMPLETED/PLANNED status "
        "reflects the generation date, not live tracking.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    cfg = load_config()
    lectures = read_lectures()
    if len(lectures) != cfg["lecture_count"]:
        print(f"WARN: semester.yml lecture_count={cfg['lecture_count']} but {len(lectures)} lecture pages found; using the pages.")
        cfg["lecture_count"] = len(lectures)

    dates = session_dates(cfg, cfg["lecture_count"])
    mapping = {lec["number"]: d for lec, d in zip(lectures, dates)}
    apply_overrides(cfg, mapping)

    raw = cfg.get("generated_on", "auto")
    generated_on = date.today() if str(raw).strip() == "auto" else parse_date(raw)

    module_bounds: dict[int, tuple[date, date]] = {}
    for lec in lectures:
        d = mapping.get(lec["number"])
        if d is None:
            continue
        lo, hi = module_bounds.get(lec["module"], (d, d))
        module_bounds[lec["module"]] = (min(lo, d), max(hi, d))

    # Assessment anchors: lecture-anchored dates (+optional session_offset days)
    assessment_rows: list[tuple[str, str, str]] = []
    for item in cfg["assessments"]:
        milestone = str(item.get("milestone", "")).strip()
        anchor = str(item.get("lecture", "")).strip()
        if not milestone or anchor not in mapping:
            print(f"WARN: assessment milestone skipped (unknown lecture anchor): {item}")
            continue
        when = mapping[anchor] + timedelta(days=int(item.get("session_offset", 0)))
        assessment_rows.append((milestone, anchor, fmt(when)))

    page = render_page(cfg, lectures, mapping, module_bounds, generated_on, assessment_rows)
    out_page = ROOT / cfg.get("output_page", "docs/schedule-calendar.md")
    out_page.write_text(page, encoding="utf-8")

    log_lines = [
        "# Semester Calendar — Generation Log (internal)",
        "",
        f"*Generated: {generated_on.isoformat()} from `semester.yml`*",
        "",
        f"- Semester start: `{cfg['semester_start'].isoformat()}`",
        f"- Lecture days: {', '.join(WEEKDAY_NAMES[d] for d in cfg['lecture_days'])}",
        f"- Break weeks: {cfg['break_weeks'] or 'none'} · Holidays: {[d.isoformat() for d in cfg['holidays']] or 'none'}",
        f"- Sessions mapped: {len(mapping)}/{len(lectures)}",
        f"- Overrides applied: {cfg['session_overrides'] or 'none'}",
        f"- Assessment milestones: {len(assessment_rows)}",
        f"- Output: `{cfg.get('output_page', 'docs/schedule-calendar.md')}`",
        "",
        "## Session map",
        "",
        "| Lecture | Date | Status |",
        "|---|---|---|",
    ]
    for lec in lectures:
        d = mapping.get(lec["number"])
        if d:
            log_lines.append(f"| {lec['number']} | {d.isoformat()} | {status_for(d, generated_on)} |")
    (ROOT / cfg.get("output_log", "docs-meta/semester-calendar-log.md")).write_text(
        "\n".join(log_lines) + "\n", encoding="utf-8"
    )

    print(f"OK: wrote {out_page.relative_to(ROOT)} ({len(mapping)} sessions, {len(assessment_rows)} milestones)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
