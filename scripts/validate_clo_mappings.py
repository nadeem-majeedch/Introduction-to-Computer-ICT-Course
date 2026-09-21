#!/usr/bin/env python3
"""Validate CLO mappings and module/lecture consistency (stdlib only).

Checks:
  - lecture front-matter outcomes reference only CLO-1..CLO-N
  - module pages reference exactly their lecture range
  - module count matches expectations
"""
import re
import sys

from course_paths import DOCS, load_expectations

MODULES_DIR = DOCS / "modules"
LECTURES_DIR = DOCS / "lectures"


def lecture_module_map() -> dict[int, int]:
    result: dict[int, int] = {}
    for path in sorted(LECTURES_DIR.glob("L*.md")):
        m = re.match(r"^L(\d{2})-", path.name)
        if not m:
            continue
        num = int(m.group(1))
        text = path.read_text(encoding="utf-8")
        fm = re.search(r"^module:\s*(\d+)\s*$", text, flags=re.MULTILINE)
        if not fm:
            raise ValueError(f"{path.name}: missing front-matter 'module'")
        result[num] = int(fm.group(1))
    return result


def main() -> int:
    expectations = load_expectations()
    n_clos = expectations["clos"]
    n_modules = expectations["modules"]
    ranges = {int(k): tuple(v) for k, v in expectations["module_lecture_ranges"].items()}
    issues: list[str] = []

    clo_pattern = re.compile(r"CLO-(\d+)")
    lecture_mods = lecture_module_map()

    for path in sorted(LECTURES_DIR.glob("L*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^outcomes:\s*\[(.*?)\]\s*$", text, flags=re.MULTILINE)
        if not m:
            issues.append(f"{path.name}: missing outcomes front-matter")
            continue
        for clo in re.findall(r"CLO-\d+", m.group(1)):
            n = int(clo.split("-")[1])
            if not (1 <= n <= n_clos):
                issues.append(f"{path.name}: outcome '{clo}' outside CLO-1..CLO-{n_clos}")

    module_files = sorted(MODULES_DIR.glob("module-*.md"))
    if len(module_files) != n_modules:
        issues.append(f"expected {n_modules} module pages, found {len(module_files)}")

    for path in module_files:
        m = re.match(r"^module-(\d{2})-", path.name)
        if not m:
            issues.append(f"{path.name}: bad module file name")
            continue
        mod = int(m.group(1))
        if mod not in ranges:
            issues.append(f"{path.name}: module {mod} not in expectations")
            continue
        lo, hi = ranges[mod]
        text = path.read_text(encoding="utf-8")
        refs = {
            int(x)
            for x in re.findall(r"L(\d{2})-", text)
        }
        expected_refs = set(range(lo, hi + 1))
        missing = expected_refs - refs
        extra = refs - expected_refs
        if missing:
            issues.append(
                f"{path.name}: module {mod} is missing lecture links for: "
                + ", ".join(f"L{n:02d}" for n in sorted(missing))
            )
        if extra:
            issues.append(
                f"{path.name}: module {mod} references out-of-range lectures: "
                + ", ".join(f"L{n:02d}" for n in sorted(extra))
            )
        for n in expected_refs:
            if lecture_mods.get(n) != mod:
                issues.append(
                    f"{path.name}: lecture L{n:02d} front-matter says module "
                    f"{lecture_mods.get(n)}, expected {mod}"
                )

    print(f"CLOs: {n_clos}; modules: {len(module_files)}; lectures mapped: {len(lecture_mods)}")
    if issues:
        print("FAIL: validate_clo_mappings")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS: validate_clo_mappings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
