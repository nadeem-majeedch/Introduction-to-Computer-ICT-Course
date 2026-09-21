# Master Course Architecture — Introduction to Computer (ICT)

**Version:** 1.0 (initial architecture)
**Date:** 2026-09-18
**Status:** Approved for implementation; see `docs-meta/06-open-questions.md` for instructor decisions
**Audience:** Instructor, teaching assistants, future course maintainers

---

## 1. Course description

**Introduction to Computer (ICT)** is a first-semester, 64-contact-hour course (32 lectures × 2 hours) that builds a rigorous yet beginner-friendly foundation in computing. Students progress from everyday computer literacy — what a computer is, how it evolved, and how it is used — to a working conceptual model of hardware, software, data representation, digital logic, networks, the Internet and cloud, databases and data science, intelligent systems, and the security, privacy, and ethical responsibilities of digital citizenship. Weekly hands-on labs, in-class activities, case studies, and a semester-long integrated project convert conceptual understanding into practical capability. The course prepares students for subsequent coursework in programming, data structures, computer organization, and data science.

**Credit framing:** 64 contact hours; mapping to credit units (e.g., 3+1) is an institutional decision — see OQ-02.

## 2. Prerequisites

- **Formal:** None. Open to all first-semester students.
- **Assumed background:** Basic arithmetic (addition, multiplication, exponents); secondary-school reading and writing proficiency in the language of instruction.
- **Assumed resources:** Regular access to a computer (Windows, macOS, or Linux) with internet; a spreadsheet application (any of Microsoft Excel, Google Sheets, or LibreOffice Calc) from Week 1.
- **Helpful but not required:** Prior experience installing software or using cloud storage.
- **Support bridge:** Because the cohort has mixed computer literacy, Lectures 1–3 and Lab 1 deliberately cover basics (mouse/keyboard efficiency, file navigation) that experienced users may test out of via the Lab 1 self-check.

## 3. Target audience

| Group | Notes |
|---|---|
| First-semester BS Computer Science | Foundation for programming and computer-organization courses |
| First-semester BS Data Science | Emphasis tracks on data representation, spreadsheets, databases, and data-science foundations (Modules 4, 5, 7) |
| Students with mixed computer literacy | Every module begins from concrete, everyday examples before formal theory; all jargon is defined on first use |
| Transfer/non-major students | Syllabus, schedule, and references are self-contained on the public website |

## 4. Course learning outcomes (CLOs)

By the end of the course, a successful student will be able to:

| # | Outcome (measurable verb in bold) | Bloom level |
|---|---|---|
| CLO-1 | **Describe** the historical evolution of computing and **classify** types of computers by capability and application domain | Understand |
| CLO-2 | **Explain** the von Neumann model and the function of CPU, memory hierarchy, storage, and peripherals | Understand |
| CLO-3 | **Distinguish** system software from application software and **demonstrate** operating-system and file-management operations | Understand / Apply |
| CLO-4 | **Convert** numbers among binary, octal, decimal, and hexadecimal, and **explain** how text, images, audio, and video are encoded | Apply / Understand |
| CLO-5 | **Construct** truth tables and **predict** the behaviour of simple combinational circuits built from AND, OR, NOT, XOR, NAND, NOR | Apply / Analyze |
| CLO-6 | **Use** word-processing, spreadsheet, and presentation tools, including formulas and charts, to complete realistic digital workflows | Apply |
| CLO-7 | **Explain** networking, Internet, and Web fundamentals (protocols, IP/DNS, HTTP) and the cloud service models IaaS/PaaS/SaaS | Understand |
| CLO-8 | **Explain** relational database concepts (tables, keys, queries, integrity) and **demonstrate** elementary queries | Understand / Apply |
| CLO-9 | **Apply** computational thinking — decomposition, pattern recognition, abstraction, and algorithm design with flowcharts — to small problems | Apply / Analyze |
| CLO-10 | **Identify** common security and privacy threats and **apply** safe, legal, ethical practices, including critical evaluation of AI-generated output | Apply / Evaluate |
| CLO-11 | **Synthesize** course concepts in an integrated semester project (design document + working artefact + presentation) | Create |

## 5. Course learning objectives (module level)

Each module contributes a distinct strand of the outcomes above:

- **M1 Foundations:** Explain what a computer is, trace the history of computing devices, and classify computers by scale and purpose. (CLO-1)
- **M2 Hardware:** Explain how the von Neumann architecture executes a program and how CPU, memory, storage, and peripherals interact. (CLO-2)
- **M3 Software & OS:** Differentiate software categories, describe OS responsibilities, and demonstrate file-system proficiency. (CLO-2, CLO-3)
- **M4 Data representation:** Perform base conversions and explain integer, character, and multimedia encoding. (CLO-4)
- **M5 Logic & productivity:** Reason with Boolean logic, read gate-level circuits, and produce professional documents, spreadsheets, and presentations. (CLO-5, CLO-6)
- **M6 Networks & cloud:** Trace a web request end-to-end and compare cloud service and deployment models. (CLO-7)
- **M7 Data & intelligent systems:** Design small relational schemas, query them, prepare data, and evaluate AI claims critically. (CLO-8, CLO-10, part of CLO-11)
- **M8 Security, society & synthesis:** Apply security/privacy practices, design algorithms with computational thinking, and complete the integrated project. (CLO-9, CLO-10, CLO-11)

Full lecture-level objectives (3–5 per lecture, each mapped to a CLO) appear in the header block of every lecture page.

## 6. Eight coherent modules — 32-lecture structure

| Module | Lectures | Theme |
|---|---|---|
| 1 | L01–L04 | Foundations: The Digital World |
| 2 | L05–L08 | Hardware: Inside the Machine |
| 3 | L09–L12 | Software and Operating Systems |
| 4 | L13–L16 | Data and Digital Representation |
| 5 | L17–L20 | Digital Logic and Productivity Tools |
| 6 | L21–L24 | Networks, Internet, and Cloud |
| 7 | L25–L28 | Data, Databases, and Intelligent Systems |
| 8 | L29–L32 | Security, Society, and Synthesis |

### Module 1 — Foundations: The Digital World (L01–L04)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L01 | What Is a Computer? | Definition, hardware vs software vs data vs users, ICT in daily life, course map | 1 |
| L02 | A Brief History of Computing | From manual/ mechanical devices (abacus, Jacquard loom, Babbage) through ENIAC, transistors, ICs, microprocessors, to smartphones; computer generations | 1 |
| L03 | Types of Computers and Their Applications | Supercomputers → mainframes → servers → PCs → mobile → embedded/IoT; special-purpose vs general-purpose; where each is used today | 1 |
| L04 | Computers, Society, and You | Impact on work/education/health, digital divide, ICT careers and pathways, ethics preview, study strategies for this course | 1, 10 |

### Module 2 — Hardware: Inside the Machine (L05–L08)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L05 | The von Neumann Architecture | CPU, memory, I/O, buses; stored-program concept; the instruction cycle at overview level | 2 |
| L06 | The CPU: How Instructions Execute | Fetch–decode–execute, registers, ALU/CU, clock speed, multi-core, cache intuition, Moore's law and its limits | 2 |
| L07 | Memory and the Hierarchy | RAM vs ROM, SRAM/DRAM intuition, cache levels, virtual memory, volatility, capacity vs speed vs cost trade-offs | 2 |
| L08 | Storage and Peripherals | HDD/SSD/optical/flash, RAID awareness, input devices, output devices, ports and connectors, choosing a machine by requirements | 2 |

### Module 3 — Software and Operating Systems (L09–L12)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L09 | The Software Landscape | System vs application software; OS, utilities, drivers, firmware; categories of application software; licensing (proprietary, FOSS, trials) | 3 |
| L10 | Operating System Fundamentals | Booting, processes, scheduling, memory management, user interfaces (CLI vs GUI), popular OS families, virtual machines preview | 3 |
| L11 | File Systems and File Management | Files, folders, paths, extensions, file formats, metadata, search, naming conventions, backup discipline (3-2-1 rule) | 3 |
| L12 | Installing, Updating, and Troubleshooting | Safe installation practices, updates and patching, permissions, task/process managers, structured troubleshooting methodology, getting help effectively | 3 |

### Module 4 — Data and Digital Representation (L13–L16)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L13 | Number Systems: Binary and Hexadecimal | Positional notation; base 2, 8, 10, 16; conversions in both directions; why computers use binary | 4 |
| L14 | Representing Numbers in Hardware | Unsigned vs signed integers, two's complement, overflow, fixed-point intuition, real-number limits and floating-point awareness | 4 |
| L15 | Character Encoding | Bits to characters; ASCII; Unicode and UTF-8; escaping mojibake; keyboard → screen journey | 4 |
| L16 | Multimedia and Compression | Pixels, resolution, raster vs vector; sampling, bit depth, audio; video; lossless vs lossy compression (Huffman intuition, JPEG/MP3 awareness) | 4 |

*Midterm examination window follows L16 (covers Modules 1–4).*

### Module 5 — Digital Logic and Productivity Tools (L17–L20)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L17 | Boolean Logic and Truth Tables | Propositions, AND/OR/NOT, XOR, truth tables, Boolean expressions, everyday decision logic, De Morgan's laws (intuition) | 5 |
| L18 | Logic Gates and Simple Circuits | Gates as physical devices, building half/full adders, multiplexers awareness, from circuits to CPU (bridging back to L05–L06) | 5 |
| L19 | Productivity Tools I: Documents and Spreadsheets | Word-processing craft (styles, TOC, track changes); spreadsheet anatomy, formulas, cell references, core functions (SUM, AVERAGE, IF, VLOOKUP/XLOOKUP), charts | 6 |
| L20 | Productivity Tools II: Presentations and Workflows | Slide design principles, accessibility in documents/slides, version control for files, collaboration tools, cloud sync, templates and standards in team workflows | 6 |

### Module 6 — Networks, Internet, and Cloud (L21–L24)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L21 | Computer Networking Concepts | Network types (PAN/LAN/MAN/WAN), topologies, switches/routers, bandwidth vs latency, wired vs wireless, protocol layering intuition | 7 |
| L22 | The Internet: How It Works | Packet switching, TCP/IP, IP addresses, DNS, traceroute journey of a request, ISPs, undersea cables, net neutrality awareness | 7 |
| L23 | The Web: HTTP, Browsers, and Search | Client–server, URLs, HTTP/HTTPS, browsers and rendering, how search engines work, evaluating information credibility, safe browsing | 7, 10 |
| L24 | Cloud Computing and Virtualization | Service models IaaS/PaaS/SaaS, deployment models, virtual machines and containers intuition, cost/scaling trade-offs, everyday cloud services, case study | 7 |

### Module 7 — Data, Databases, and Intelligent Systems (L25–L28)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L25 | Databases and Information Systems | Data vs information, relational model, tables/keys/relationships, basic SQL SELECT intuition, integrity, spreadsheet vs database | 8 |
| L26 | Data Science Computing Foundations | Data lifecycle, data cleaning, spreadsheets as analysis tools, visualization principles, privacy in datasets, tools landscape (from spreadsheets toward Python/R awareness) | 6, 8, 10 |
| L27 | Artificial Intelligence Fundamentals | What AI/ML are (and are not), learning from examples, everyday AI systems, model training intuition, generative AI awareness | 10 |
| L28 | Responsible AI Literacy | Bias and fairness, hallucinations and verification, data provenance, academic integrity with AI tools, evaluating AI output claims | 10 |

### Module 8 — Security, Society, and Synthesis (L29–L32)

| Lec | Title | Key topics | CLO |
|---|---|---|---|
| L29 | Cybersecurity Fundamentals | Threats (malware, phishing, social engineering), defences (updates, backups, least privilege), passwords and MFA per current guidance, **authorized-learning boundaries** | 10 |
| L30 | Privacy and Digital Citizenship | Digital footprints, tracking basics, data protection concepts, legal/ethical responsibilities, accessibility and inclusion online | 10 |
| L31 | Computational Thinking and Problem Solving | Decomposition, pattern recognition, abstraction, algorithms, flowcharts and pseudocode, applying the method to the final project | 9 |
| L32 | Emerging Technologies and Course Synthesis | IoT, blockchain awareness, quantum-computing awareness, societal implications, course recap, final project showcase and reflection | 1–11 |

## 7. Practical activities

| Type | Cadence | Inventory |
|---|---|---|
| Lecture activities (5–15 min) | Most lectures | `content/activities/` — 5 reusable in-class activities (A1–A5) referenced from lectures |
| Labs (structured handouts) | One per module, scheduled in the second lecture of each module week pair | `content/labs/` — 8 graded labs (Lab 1–8) |
| Case studies (discussion-driven) | 4 across the semester | `content/case-studies/` — CS-01…CS-04 |
| Integrated semester project | Assigned L08, milestone-checked L16 and L24, showcased L32 | Brief and rubric in `content/assessments/project/` |

| ID | Activity | Used in |
|---|---|---|
| A1 | History timeline jigsaw | L02 |
| A2 | Number-system relay | L13 |
| A3 | Truth-table design sprint (voting-system circuit on paper) | L17 |
| A4 | "Anatomy of a web request" protocol role-play | L22 |
| A5 | Phishing red-flag audit (simulated, educational samples) | L29 |

| ID | Case study | Used in |
|---|---|---|
| CS-01 | Moore's Law and the smartphone in your pocket | L06 / L08 |
| CS-02 | A small university migrates services to the cloud | L24 |
| CS-03 | Data-driven decision making in public health | L26 / L27 |
| CS-04 | Ransomware incident at a fictional college: preparedness and response | L29 / L30 |

## 8. Assessment plan

| Component | Weight | Timing | Notes |
|---|---|---|---|
| Quizzes (best 10 of 14) | 15% | Weekly, announced | Short conceptual checks; keys in `instructor/` |
| Labs (8) | 20% | Per-module | Rubric-graded; self-contained handouts |
| Midterm examination | 20% | After L16 | Modules 1–4 |
| Integrated semester project | 25% | L08 → L32 | Milestones: proposal (L08), design (L16), working check (L24), showcase + report (L32) |
| Final examination | 20% | End of term | Comprehensive, emphasis on Modules 5–8 |

**Grading policy hooks** (scale, attendance, academic-integrity procedure) are institution-specific and left configurable in `docs/syllabus.md` — see OQ-03. All assessment instruments and keys live **only** in `instructor/`; the public site publishes weights, schedules, and rubric criteria without answers.

## 9. Problem-solving progression

The course deliberately sequences cognitive demand in four stages:

1. **Stage 1 — Describe & identify (M1–M2):** Students build accurate mental models and vocabulary (what is this component, what does it do?).
2. **Stage 2 — Represent & manipulate (M3–M4):** Students operate on concrete artefacts (files, settings) and symbolic representations (numbers, encodings) — the bridge from user to analyst.
3. **Stage 3 — Build & connect (M5–M6):** Students construct small artefacts (truth tables, circuits, spreadsheets, workflows) and trace system behaviour across components and networks.
4. **Stage 4 — Evaluate & design (M7–M8):** Students weigh trade-offs, evaluate claims (data, AI, security), and design an integrated solution to an open-ended problem.

Every lecture page marks its stage; every assessment samples from the stages cumulatively (the final exam and project assess Stage 4 behaviours built on Stage 1–3 skills).

## 10. Recommended textbooks and reliable online references

**Primary textbook (instructor should confirm edition/availability — OQ-04):**

- Brookshear, J. G., & Brylow, D. *Computer Science: An Overview*, 13th ed., Pearson. — Conceptual backbone for Modules 1–6.
- Sinha, P. K., & Sinha, P. *Computer Fundamentals*, BPB Publications. — Accessible coverage aligned with ICT curricula.
- Bourgeois, D. T. *Information Systems for Business and Beyond* (open textbook, CC BY-NC) — Modules 6–7 supplement.

**Supplementary (choose per lecture; listed on `docs/references/index.md`):**

- White, R., & Downs, T. *How Computers Work*, Que. — Visual intuition for Module 2.
- Patt, Y. N., & Patel, S. J. *Introduction to Computing Systems*, McGraw-Hill. — Instructor reference for Modules 4–5 depth.
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*, Morgan Kaufmann. — Instructor reference only.

**Online (vetted, stable):**

- Khan Academy — *Computers and the Internet* course
- Code.org — *How Computers Work* video series
- CS Unplugged (University of Canterbury) — offline activities for A1–A3
- CrashCourse Computer Science (YouTube) — lecture-aligned overviews
- MDN Web Docs — *How the Web works* (Module 6)
- Cloudflare Learning Center — networking/TLS explainers (Module 6)
- NIST publications and guidance for password/MFA fundamentals (Module 29 security content references current NIST SP 800-63 guidance concepts)
- Bureau of Labor Statistics *Occupational Outlook Handbook* — ICT careers (L04)

Each lecture page carries a "References & further reading" block citing sources for its technical and historical claims. Citation format is defined in `docs-meta/04-documentation-standards.md`.

## 11. Accessibility requirements

The course commits to WCAG 2.1 AA on the published site and inclusive practice in class:

1. **Structure:** One `h1` per page; strictly nested headings; meaningful link text (no "click here").
2. **Images:** Alt text mandatory for every image; decorative images marked as such; diagrams get both alt text and a text description in the body or a `<details>` transcript.
3. **Math:** Rendered via MathJax with the expression also available as plain text.
4. **Colour:** Never the sole carrier of meaning; contrast ≥ 4.5:1 for body text.
5. **Media:** Any linked video must be accompanied by title, duration, and a caption/transcript statement; no autoplay.
6. **Tables:** Header rows used for all data tables.
7. **Language:** Plain-language first sentences for every section; jargon defined at first use; a course glossary is maintained.
8. **In-class:** Materials shared in advance for screen-reader users; labs have keyboard-only paths; large-print versions of handouts on request.
9. **Automated enforcement:** The QA validator checks heading structure, alt text, and link text (see `docs-meta/05-qa-strategy.md`).

## 12. Website information architecture

```text
docs/
├── index.md                     # Course home (descriptive landing page)
├── syllabus.md                  # Syllabus (student-facing)
├── schedule.md                  # 32-lecture schedule table
├── assessment.md                # Assessment plan + policies (no keys)
├── help.md                      # FAQ, study tips, support resources
├── modules/
│   ├── module-01-foundations.md            # 8 module overview pages
│   ├── module-02-hardware.md
│   ├── module-03-software-operating-systems.md
│   ├── module-04-data-representation.md
│   ├── module-05-logic-productivity.md
│   ├── module-06-networks-internet-cloud.md
│   ├── module-07-data-databases-ai.md
│   └── module-08-security-society-synthesis.md
├── lectures/
│   ├── L01-what-is-a-computer.md           # … 32 lecture pages (L01–L32)
│   └── …
├── labs/
│   ├── index.md and lab-01 … lab-08        # 8 graded lab handouts
├── activities/index.md + A1–A5             # in-class activities
├── case-studies/index.md + CS-01…CS-04
├── assessments/
│   ├── project/ (brief, milestones, rubric criteria — no answers)
│   └── quizzes/ (practice quizzes — keys stay in instructor/)
├── references/index.md                     # textbooks + vetted links
└── glossary.md                             # course glossary
instructor/                       # OUTSIDE docs/ — never published
docs-meta/                        # design documents (this set) — not in site nav
scripts/                          # validators
tests/                            # expectations + QA runner config
.github/workflows/                # CI: build + QA + instructor-leak guard
```

`mkdocs.yml` nav mirrors this tree explicitly so that adding a file without a nav entry fails the strict build (orphan detection).

## 13. Quality assurance strategy

Two validation layers, both enforced locally and in CI (details in `docs-meta/05-qa-strategy.md`):

- **Layer 1 — structural validators (Python stdlib):** nav/file sync, front-matter and lecture-header schema, objective-to-CLO mapping, alt-text and heading checks, terminology consistency, instructor-file leak guard.
- **Layer 2 — real build:** `mkdocs build --strict` in a pinned venv; any warning fails the build, exactly as CI does.

## 14. Publication workflow

1. Instructor initializes git (`git init`, first commit) and creates the GitHub repository.
2. Work happens on feature branches; changes are reviewed (self-review checklist in QA doc).
3. Push to `main` triggers GitHub Actions:
   - **CI (all branches):** validators + `mkdocs build --strict` + instructor-leak guard.
   - **Deploy (main only):** site build artefacts published to GitHub Pages via `actions/deploy-pages`.
4. Pages is configured to "GitHub Actions" source (repo Settings → Pages).
5. Local preview before pushing: `mkdocs serve` and run `python scripts/run_all_checks.py`.

Nothing in this workflow was executed by the scaffolding agent: **no `git init`, no commits, no pushes** (rules 1–3).

## 15. Quality assurance sign-off and evolution

- Architecture reviewed against the mandated coverage list in the project brief; every listed topic maps to at least one lecture (traceability table in `docs-meta/02-repository-plan.md`).
- Unresolved instructor decisions are tracked in `docs-meta/06-open-questions.md` (OQ-01…OQ-12).
- The architecture is versioned; changes require updating the lecture table, nav, and validators together.
