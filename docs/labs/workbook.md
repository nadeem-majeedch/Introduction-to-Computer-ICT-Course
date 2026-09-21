# Practical Lab Workbook

The workbook view of the course's practical work: eight **graded labs** (the assessment spine) plus four ungraded **skill builders** that close the remaining practical topics — one hub page, eight full handouts, four compact builders. Start from the mapping below; read the [safety rules](#safety-rules) and [fallbacks](#accessibility-and-fallbacks) once.

---

## Lab-to-lecture mapping

| Lab | Related lecture | Title | Duration | Graded |
|---|---|---|---|---|
| [Lab 1](lab-01-digital-basics-orientation.md) | L01–L04 | Digital Basics and System Orientation | 60–90 min | Yes |
| [Lab 2](lab-02-hardware-inventory-benchmarking.md) | L05–L08 | Hardware Inventory and Benchmarking | 90 min | Yes |
| [Lab 3](lab-03-file-system-scavenger-hunt.md) | L09–L12 | File System Scavenger Hunt | 90 min | Yes |
| [Lab 4](lab-04-number-systems-workshop.md) | L13–L16 | Number Systems Workshop | 90 min | Yes |
| [Lab 5](lab-05-logic-circuit-simulator.md) | L17–L20 | Logic Circuit Simulator Lab | 60–75 min | Yes |
| [Lab 6](lab-06-spreadsheet-data-workshop.md) | L19 (L26 bridge) | Spreadsheet Data Workshop | 90 min | Yes |
| [Lab 7](lab-07-networking-cloud-lab.md) | L21–L24 | Networking and Cloud Lab | 90–120 min | Yes |
| [Lab 8](lab-08-security-habits-lab.md) | L29–L30 | Security Habits Lab | 90 min | Yes |
| [SB-1](sb-01-software-installation.md) | L12 | Software Installation and Package Awareness | 30–40 min | Practice |
| [SB-2](sb-02-database-thinking.md) | L25 | Database Thinking with Flat Tables | 30–40 min | Practice |
| [SB-3](sb-03-computational-thinking-gym.md) | L31 | Computational Thinking Gym | 30–40 min | Practice |
| [SB-4](sb-04-responsible-ai.md) | L27–L28 | Responsible AI Use Trial | 30–40 min | Practice |

## Coverage matrix — 22 practical areas

| # | Practical area | Covered by |
|---|---|---|
| 1 | Computer hardware identification | Lab 1 · Lab 2 |
| 2 | CPU, RAM, storage, device specifications | Lab 2 |
| 3 | Operating-system navigation | Lab 1 · Lab 3 |
| 4 | File and folder management | Lab 1 · Lab 3 |
| 5 | File permissions and basic security awareness | Lab 3 (forensics part) · SB-1 · Lab 8 |
| 6 | Software installation concepts and package awareness | SB-1 · Lab 8 (manager adoption) |
| 7 | Binary and number-system exercises | Lab 4 |
| 8 | Text and character encoding | Lab 4 (forensics) |
| 9 | Basic logic and truth tables | Lab 5 |
| 10 | Productivity software | Lab 6 (documents habits via styles/tracked changes) |
| 11 | Spreadsheet data organization | Lab 6 |
| 12 | Basic data visualization | Lab 6 (honest chart) |
| 13 | Network configuration awareness | Lab 7 |
| 14 | IP address and DNS concepts | Lab 7 |
| 15 | Browser and web investigation | Lab 7 (HTTPS inspection) |
| 16 | Password and authentication security | Lab 8 |
| 17 | Privacy and phishing awareness | Lab 8 · Lab 3 (metadata forensics) |
| 18 | Cloud storage and collaboration | Lab 7 (cloud hands-on) · Lab 3 (3-2-1 offsite) |
| 19 | Database concepts and simple data organization | SB-2 |
| 20 | AI literacy and responsible use | SB-4 · Lab 8 (tool settings audit) |
| 21 | Computational thinking | SB-3 · integrated project |
| 22 | Integrated ICT project | [Project brief](../assessments/project/brief.md) — the showcase deliverable |

No practical area is silently omitted: every row names the lab or skill builder that delivers it.

## Skill builders — the ungraded four

Thirty-to-forty-minute practice pieces, completion-marked with feedback, closing the four coverage gaps the graded spine doesn't reach. Each is platform-neutral, needs no installs, and states its own fallback:

- [SB-1 — Software Installation and Package Awareness](sb-01-software-installation.md) (with L12): channels, installer-reading, verification habits.
- [SB-2 — Database Thinking with Flat Tables](sb-02-database-thinking.md) (with L25): keys, constraints, and a query-by-hand in any spreadsheet.
- [SB-3 — Computational Thinking Gym](sb-03-computational-thinking-gym.md) (with L31): three problem cards, paper-first, peer bug-tracing.
- [SB-4 — Responsible AI Use Trial](sb-04-responsible-ai.md) (with L27–L28): tool audit, claim verification, disclosure rehearsal.

## Safety rules

1. **Your own systems only.** Every lab operates on your machine, your accounts, or the course's provided samples. Probing, scanning, or logging into systems you don't own is out of scope everywhere in this course (L29's boundary).
2. **No system modifications required.** Nothing here needs administrator rights, registry edits, OS reconfiguration, or hardware changes. If a step ever seems to require one, stop — you've left the lab.
3. **Simulated materials only.** Phishing samples are fabricated by your instructor; encoding-corrupted files are made for the course; the cloud VM is created and *destroyed by you* in Lab 7.
4. **If a step asks you to install anything**, the handout says what and why. SB-1 studies installers — it installs nothing beyond the tools the course already names as optional.

## How labs are graded (consolidated rubric)

All eight graded labs share one rubric; each handout names which part carries the demonstration weight.

| Criterion | Weight | What "excellent" looks like |
|---|---|---|
| Correct completion of required tasks | 60% | All steps executed; *method shown* where the handout demands it (answers without method score half) |
| Working demonstration or artifact | 25% | The named artifact exists, is yours, and matches your environment (screenshots consistent with your machine, transcripts in your OS's dialect) |
| Reflection questions answered thoughtfully | 15% | Answers connect to lecture concepts by name, not generic prose |

- **Submission:** per-handout checklist, via the course LMS, by the due date on the handout.
- **Late policy:** 10% per day ([Assessment](../assessment.md#3-labs-20)).
- **Collaboration:** discuss approach freely; execute and submit your own work. Watch-points (recycled screenshots, shared simulator accounts) are handled under the integrity procedure.
- **Skill builders (SB-1–SB-4) are practice**: completion-marked, feedback given, not weighted into the final grade — they exist so no practical area goes untried.

## Accessibility and fallbacks

- **Every handout carries an "Accessibility alternative"** paragraph naming its own text-based, screen-reader-friendly, or no-install route to the same outcome.
- **University lab machines satisfy every requirement**; if your personal machine can't run something, [Help](../help.md#3-getting-help) lists how to get access.
- **No expensive or proprietary software is required anywhere**: spreadsheets accept Excel, Google Sheets, or LibreOffice; the logic simulator is a free browser tool; cloud work uses free tiers or sanctioned institutional sandboxes.
- **Tool blocked or unavailable?** The handout's troubleshooting section names the substitution; if none fits, submit a written walk-through plus your analysis and note the barrier — instructors grade the understanding, and the equipment checklist (instructor side) tracks institutional gaps.
- **Large-print conversion tables and the password-audit worksheet** are available from your instructor on request.

---

*Instructor side: the delivery guide, equipment/software checklist, and validation checklist for this workbook live in the private instructor tree (not published), per the course's student/instructor separation.*
