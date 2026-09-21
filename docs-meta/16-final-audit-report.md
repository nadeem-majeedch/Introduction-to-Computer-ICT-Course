# Final Course Audit — PROMPT 09

**Date:** 2026-09-19 · **Auditor role:** independent final QA (curriculum, content, website, automation)
**Verdict: PASS WITH WARNINGS** — no critical or high-severity defects remain in the repository; all warnings are either instructor decisions or non-blocking items with documented workarounds. Detail below.

---

## 1. Test execution report (only executed tests are listed as executed)

| # | Test | Command | Result |
|---|---|---|---|
| T1 | Full validation suite (12 validators) | `python scripts/run_all_checks.py` | **PASS** (nav sync, lecture schema ×32, CLO mappings, accessibility, terminology, leak guard ×28 private files, teaching blueprint 32×16, slide decks 32 decks, lab workbook, case bank 100×2, assessment package, site integrity) |
| T2 | Strict site build | `mkdocs build --strict` (pinned venv) | **PASS** — 105 pages, zero warnings |
| T3 | Built-output leak scan | `validate_site_integrity.py` over `site/` | **PASS** — 105 HTML pages, no instructor paths/answer keys/marking schemes in public output (context-aware) |
| T4 | Placeholder sweep (public tree) | grep for TBD/LOREM/PLACEHOLDER/FIXME/[insert | **PASS** — zero hits |
| T5 | Duplicate-content sweep (lectures) | objective/summary block uniq-count + banner count | **PASS** — 32/32 lecture banners; no duplicated bold-lead blocks across lectures |
| T6 | Heading discipline | H1-per-page count + level-skip scan over all 104 public pages | **PASS** — every page exactly one H1; zero heading-level skips |
| T7 | Technical recomputation | conversions (200→`11001000`→`C8`; `0x2F`=47; `144₈`=100), two's complement (−45→`11010011`; `10110110`→−74; 100+50→−106 overflow), mojibake (`C3 A9`→é), half adder, GiB/GB≈1.0737 | **PASS** — every recomputed answer matches the published model answers |
| T8 | Cross-file weighting consistency | assessment.md ↔ syllabus.md ↔ assessments/index.md | **PASS** — 15/20/20/25/20 = 100% identical in all three, all marked *proposed* (OQ-13) |
| T9 | Website runtime sanity (built HTML) | search index present, `lang="en"`, skip-link, viewport meta, in-page anchors | **PASS** |
| T10 | Workflow YAML parse | PyYAML safe_load both workflows | **PASS** (mkdocs.yml's `!!python/name` tags are mkdocs-loader-specific; the strict build is that file's parser verdict) |
| T11 | Workflow↔disk alignment | step names vs scripts on disk | **PASS** after fix F-01 (calendar regeneration added to both workflows) |
| T12 | References integrity | L16 [2] block + references index | **PASS WITH WARNING** — see W-01: the previously-logged "L16 reference [2] substitution" issue is now *closed*: the entry itself discloses the fallback rule and cites MDN for cross-checking; acceptable for first publication |

**Not executed (honestly stated):** no live GitHub Pages deploy (requires the instructor's push + repo settings); no browser-based WCAG audit (validators + built-HTML inspection only); no classroom trialling; no lab-environment execution of student tasks.

## 2. Findings register

| ID | Severity | Category | Location | Description | Impact | Recommended fix | Status | Verification |
|---|---|---|---|---|---|---|---|---|
| F-01 | High | Automation | `.github/workflows/ci.yml`, `deploy-pages.yml` | Workflows validated content but never regenerated the semester calendar — a stale committed `docs/schedule-calendar.md` would ship silently | Students could see outdated dates | Add a `generate_semester_calendar.py` step before validators (done) | ✅ **Fixed this audit** | T11 re-run; suite green |
| F-02 | Medium | Curriculum policy | `docs/assessment.md`, `syllabus.md`, framework hub | All weightings are proposals; no instructor confirmation exists in-repo | None until a weighting is assumed | Instructor confirms (OQ-13) → edit all three files in one change | 🔴 Open — instructor decision | Docs consistency T8 |
| F-03 | Medium | Publication | GitHub repo settings | OQ-01 (repo visibility) and the Pages→Actions source selection are unresolved | Free Pages requires a public repo; deploy fails without the setting | Instructor: make repo public + select Source: GitHub Actions | 🔴 Open — instructor action (UI) | Cannot be tested locally |
| F-04 | Medium | Legal | repository root | No LICENSE file (OQ-05); footer says "pending license decision" | Reuse terms undefined; some institutions block publication without one | Instructor picks a license; add LICENSE + update footer + OQ-05 | 🔴 Open — instructor decision | Absence verified |
| F-05 | Low | Content | `semester.yml` | Shipped calendar uses placeholder start (2026-10-05) and Mon/Wed pattern | Published dates are illustrative until regenerated | Instructor sets real term dates; workflows now regenerate automatically (F-01) | 🟡 Documented (by design) | Calendar generation log |
| F-06 | Low | Testing | lab handouts, question bank | No practical task was executed in a real lab environment (no such environment exists in-repo) | First-cohort calibration unknown | Instructor runs the delivery-guide §5 per-window checklist on a real lab image | 🔴 Open — requires real environment | Honest scope statement in reports 12–15 |
| F-07 | Low | Content | homework time estimates | Estimated times are uncalibrated (first cohort pending) | Possible under/over-load in year 1 | Calibrate after semester 1; adjust lecture Homework blocks | 🟡 Accepted risk | — |
| F-08 | Low | Content | L16 reference [2] | Original reference target unverifiable at write time; entry discloses fallback rule + MDN cross-check | Minimal — citation integrity maintained by disclosure | Replace with a stable print source when the instructor identifies one | 🟡 **Downgraded/closed** — disclosed self-correcting entry (was open in prior reports) | T12 |
| F-09 | Low | Content | MkDocs 2.0 banner | Upstream Material-for-MkDocs notice appears in build logs | Cosmetic; no build impact | None (external project banner) | 🟡 Accepted (upstream) | T2 logs |
| F-10 | Low | Accessibility | diagrams site-wide | Mermaid diagrams render client-side; non-visual path is the paired text alternative (verified present ×32) | Acceptable, documented | Keep the Figure-alternative contract (validator-enforced) | 🟡 Accepted, documented | Accessibility statement + T1 |

**No Critical findings.** No high-severity findings remain open.

## 3. Coverage summary (curriculum audit)

| Requirement | Evidence | Result |
|---|---|---|
| Exactly 32 lectures × 2 h = 64 contact hours | `validate_teaching_blueprint.py` (rows, durations, sum) + lecture schema | ✅ Enforced, passing |
| Logical progression | Stage-gated blueprint (§6 dependency map) + pathway page; prerequisites cross-checked by validator (objective uniqueness) | ✅ |
| First-semester level | Blueprint validator + instructor-review checklist rubric; open-verdict question design | ✅ with human-review caveat (W: pedagogical feel is not machine-checkable) |
| CS + DS relevance | Every lecture carries CS/DS-relevant examples (coverage report `docs-meta/10`); question bank tags apply both tracks | ✅ |
| Comprehensive ICT coverage | 15 mandated areas → 32 lectures mapped (`07-teaching-blueprint.md` §4); 22-area lab matrix; 23-case domains | ✅ |
| Objectives ↔ activities ↔ assessments alignment | CLO→lecture parity (validator), CLO→assessment matrix with ≥2-primary-evidence guarantee, blueprint quiz-parity check | ✅ Enforced |
| Case bank | 100 unique IDs, 4 levels, private solutions with parity, leak-scanned | ✅ Enforced |
| Public/instructor separation | 28 private files outside docs/; path-reference guard; 4 in-page leak scans; built-output scan | ✅ Enforced |

## 4. Instructor decision list (nothing silently chosen)

1. **OQ-13 — confirm assessment weightings** (F-02): keep 15/20/20/25/20, or rebalance (options documented in the blueprint); edit the three files together.
2. **OQ-05 — choose a license** (F-04): options range from CC BY (maximum reuse) to CC BY-NC-SA (non-commercial, share-alike) to institution-default terms; affects the footer and reuse rights.
3. **OQ-01 + Pages setting** (F-03): repo visibility + Settings → Pages → Source: GitHub Actions.
4. **OQ-04 — textbook editions/availability** confirmed in Week 1 (references index states this).
5. **Semester dates** (F-05): set `semester.yml` and let CI regenerate.
6. **First-cohort calibration** (F-06/F-07): lab image pre-flight + homework-time calibration after term 1.

## 5. Publication readiness

**Ready to publish once the instructor actions above are done.** Concretely: the build is clean and deterministic (pinned deps), the site is complete (105 pages, all nav valid), separation is machine-enforced at four layers, URLs are configured for `nadeem-majeedch/Introduction-to-Computer-ICT-Course`, and CI both validates content and gates deployment. The only blockers are instructor-side settings/decisions (F-02/F-03/F-04), not repository defects.

## 6. Handover summary

| Layer | State |
|---|---|
| Public site (`docs/`, 104 pages) | Complete: home, syllabus, schedule + generated calendar, pathway, assessment framework, question bank (46), exam blueprints, rubrics, project pack, 14 practice quizzes, 8 labs + 4 skill builders + workbook, 5 activities, 4 case studies, 100-case problem bank, 32 lectures, modules, references, glossary, help, accessibility |
| Instructor package (`instructor/`, 30 files, ~5,400 lines) | 8 module guides, 8 slide decks + delivery guide, exam banks + 2 assembled draft papers with model answers, 4 case-bank solution banks, lab delivery guide + answer notes, quiz keys |
| Automation (16 scripts, 12 CI checks) | Structure, pedagogy-contract, privacy, and built-output layers; calendar generator; `run_all_checks.py` as the single gate used by both workflows |
| Docs-meta (15 planning/QA reports) | Architecture → standards → per-prompt reports → this audit |
| Git | **Never initialized by the agent** — instructor performs init/commit/push per README |

**Recommended instructor sequence:** decide license + weightings → set semester dates + regenerate calendar → init/commit/push → select Pages source → verify first deploy → schedule the pre-semester lab-image checklist.
