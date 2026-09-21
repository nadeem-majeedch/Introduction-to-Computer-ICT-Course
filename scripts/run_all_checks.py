#!/usr/bin/env python3
"""Run all course validators; exit non-zero if any fail (CI entry point)."""
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

CHECKS = [
    "validate_nav_sync.py",
    "validate_lecture_schema.py",
    "validate_clo_mappings.py",
    "validate_accessibility.py",
    "validate_terminology.py",
    "check_instructor_exclusion.py",
    "validate_teaching_blueprint.py",
    "validate_slide_decks.py",
    "validate_lab_workbook.py",
    "validate_case_bank.py",
    "validate_assessment_pack.py",
    "validate_site_integrity.py",
]


def main() -> int:
    failures: list[str] = []
    for script in CHECKS:
        print(f"\n=== {script} ===")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / script)],
            cwd=str(SCRIPTS.parent),
        )
        if result.returncode != 0:
            failures.append(script)

    print("\n=== summary ===")
    if failures:
        print("FAILED checks:")
        for name in failures:
            print(f"- {name}")
        return 1
    print(f"all {len(CHECKS)} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
