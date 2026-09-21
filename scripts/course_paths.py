"""Shared paths and expectations for the ICT course validators (stdlib only)."""
import json
import sys
from pathlib import Path

# Windows consoles default to cp1252 and crash on Unicode in failure messages;
# replace unencodable characters instead of raising.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS_YML = ROOT / "mkdocs.yml"
INSTRUCTOR = ROOT / "instructor"
DOCS_META = ROOT / "docs-meta"
TESTS = ROOT / "tests"
EXPECTATIONS_PATH = TESTS / "expectations.json"


def load_expectations() -> dict:
    with EXPECTATIONS_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)["expectations"]


def docs_markdown_files():
    """All .md files under docs/, as repo-root-relative POSIX paths."""
    return sorted(
        p.relative_to(ROOT).as_posix()
        for p in DOCS.rglob("*.md")
    )
