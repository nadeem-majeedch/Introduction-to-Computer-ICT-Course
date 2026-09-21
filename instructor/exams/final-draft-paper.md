# Final Examination — Draft Paper (Cumulative, Modules 5–8 weighted)

**Instructor-only. Do not publish.** Assembled from `final-exam-bank.md` per the public blueprint (120 min, 100 marks; ~75% Modules 5–8, ~25% Modules 1–4 feeders). Every item verified against lecture content; model answers below each item. Coverage guarantee met: CLO-5 (A1, B1), CLO-6 (A4/A5, B3), CLO-7 (A6, A8, B4), CLO-8 (A10, B4), CLO-9 (A19, B5, C), CLO-10 (A13–A18, C) — each with ≥2 graded appearances; feeders cover CLO-1–4 (A21–A24, B6).

---

## Section A — Concepts (40 marks, ~40 min)

### A1. Truth table + simplification insight *(3 marks · CLO-5)*

Evaluate `(A AND NOT B) OR C`; state the row that distinguishes it from `A OR C`.

**Model:** discriminating row A=1,B=1,C=0 (`(A∧¬B)∨C`=0, `A∨C`=1). **Marking scheme:** 2 for the full table; 1 for the row.

### A2. NAND universality *(3 marks · CLO-5)*

Build NOT/AND/OR from NANDs.

**Model:** NOT = NAND(A,A); AND = NOT(NAND(A,B)); OR = NAND(NAND(A,A),NAND(B,B)). **Marking scheme:** 1 each.

### A3. Adder roles *(3 marks · CLO-5)*

Half adder outputs' expressions; why half adders can't chain.

**Model:** SUM = XOR, CARRY = AND; no carry-in input → full adder needed for ripple. **Marking scheme:** 1 + 1 + 1.

### A4. Reference mechanics *(3 marks · CLO-6)*

Predict the copied-formula behaviour; explain `$`.

**Model:** relative refs shift on copy (B2×H1 → B3×H2…); `$H$1` locks both axes. **Marking scheme:** 2 prediction, 1 lock rule.

### A5. Chart honesty *(3 marks · CLO-6)*

Fix a truncated-axis "doubling" chart.

**Model:** axis from 0, values labelled, delta stated (47→52, +11%). **Marking scheme:** 2 redesign, 1 principle (bar length encodes magnitude).

### A6. Trace the web request *(4 marks · CLO-7)*

DNS → TCP → TLS → HTTP, one sentence each; where plain HTTP fails.

**Model:** name→IP; reliable connection; certificate+encryption; request/response in tunnel; interception at any hop without TLS (confidentiality *and* integrity lost). **Marking scheme:** 4 × 1.

### A7. Bandwidth vs latency *(3 marks · CLO-7)*

Why the call lags while the backup doesn't care.

**Model:** interactive media needs low latency/jitter; bulk transfer needs throughput over time; queue-fill from the backup adds call latency. **Marking scheme:** 1 + 1 + 1.

### A8. Cloud model assignment *(3 marks · CLO-7)*

Three workloads → IaaS/SaaS/PaaS + one renter-kept responsibility each.

**Model:** dataset crunch = IaaS (keep OS hardening); browser essay = SaaS (keep data governance); legacy migration = PaaS (keep app code). **Marking scheme:** 1.5 per correct pair (model + responsibility).

### A10. Schema reading *(3 marks · CLO-8)*

PK/FK identification; what the FK blocks.

**Model:** FK prevents orphan rows/restricts parent deletion (referential integrity). **Marking scheme:** 1 + 2.

### A11. Reading order of a query *(3 marks · CLO-8)*

Given a SELECT…JOIN…WHERE, state the reading/evaluation order and what `IS NULL` is not.

**Model:** FROM/JOIN → WHERE → SELECT projection; NULL ≠ 0 ≠ empty ≠ "failed"; `=` never matches NULL. **Marking scheme:** 2 order, 1 NULL.

### A13. Bias mechanism *(4 marks · CLO-10)*

Data → model → outcome with a concrete domain; why "the computer did it" is not neutrality.

**Model:** e.g., course-recommendation trained on past enrolments encodes past sorting; outputs narrow exploration; the feedback loop entrenches it. **Marking scheme:** 2 mechanism chain, 2 domain concreteness.

### A14. Hallucination verification order *(4 marks · CLO-10)*

Three output types to verify first; why that order.

**Model:** citations/numbers → definitions → explanations; citations are fastest to falsify and poison trust; distribution/stakes beat averages. **Marking scheme:** 3 order+items, 1 why.

### A15–A18. Threat set, MFA factors, password guidance, data-protection principles *(4 × 2.5 = 10 marks · CLO-10)*

Per the bank items: threat classification (worm/ransomware/trojan/phishing — 1 per correct class), MFA categories + why phished password fails (1.5 + 1), NIST-direction password guidance vs periodic expiry (1.5 + 1), principles mapped to a university app (minimization/retention/access — 1 per principle applied, not named).

### A19. Decompose a novel problem *(3 marks · CLO-9)*

Decompose one unseen task; express one sub-problem in pseudocode.

**Marking scheme:** 2 decomposition (tractable parts, ordered), 1 pseudocode.

### A20. Emerging-tech claim evaluation *(2 marks · CLO-1/CLO-10)*

Evaluate one marketing claim with the course's four questions.

**Marking scheme:** 2 for questions applied to the specific claim (generic list: 1).

### Feeders A21–A24 *(4 × 1.5 = 6 marks · CLO-1–4)*

One-line conversion with method (CLO-4); hierarchy ordering + locality (CLO-2); stack placement (CLO-3); one history causal link (CLO-1). **Marking scheme:** 1.5 each, method required on the conversion.

## Section B — Problems (35 marks, ~45 min)

### B1. Four-variable truth table with XOR-discriminating row *(6 marks · CLO-5)*

**Model:** e.g., `A XOR (B AND C)` — full 16-row table; the discriminating row is B=1,C=1 (A=0: `0 XOR 1`=1 vs `A AND (B∧C)`-class comparisons). *Set the exact expression on assembly; verify the row by hand before printing.* **Marking scheme:** 4 table, 2 row + one-line justification.

### B2. Half → full adder *(6 marks · CLO-5)*

Half-adder table; extend to full adder for input triple (1,1,1) → SUM=1, CARRY=1 with the XOR-of-XORs reasoning.

**Marking scheme:** 2 table, 2 extension, 2 reasoning.

### B3. Spreadsheet grading sheet *(6 marks · CLO-6)*

Nested IF + absolute references for a grading sheet; predict one copy-down behaviour.

**Model:** `=IF(B2>=$H$1,"A",IF(B2>=$H$2,"B","F"))`-class; relative/absolute mix explained. **Marking scheme:** 4 formula (2 logic, 2 refs), 2 prediction.

### B4. SQL read + write *(6 marks · CLO-8)*

Given the two-table schema (STUDENTS/ENROLMENTS), read one JOIN query in plain English; write one ("names of students enrolled in 'ICT' this term with no grade").

**Model read:** "names of students with an Autumn enrolment lacking a grade." **Model write:**

```sql
SELECT name FROM students
JOIN enrolments ON students.student_id = enrolments.student_id
WHERE course_code = 'ICT' AND term = 'Autumn' AND grade IS NULL;
```

**Marking scheme:** 3 reading, 3 writing (2 logic, 1 syntax tolerance — `IS NULL` required; accept minor keyword-case variance).

### B5. Flowchart: best-10-of-14 grade computation *(7 marks · CLO-9)*

Standard shapes required (terminal/process/decision/arrows); every branch drawn.

**Model:** input 14 scores → loop (validate, collect) → sort desc → take 10 → sum/scale → combine weights → output. The decision diamond's both branches must be drawn (the honesty discriminator). **Marking scheme:** 3 shapes+structure, 2 loop correctness, 2 branch completeness.

### B6. Two's complement + overflow chain *(4 marks · CLO-4 feeder)*

Encode −1; add `0111 1111 + 0000 0001`; name the result and phenomenon.

**Model:** −1 = `1111 1111`; sum = `1000 0000` = −128 (no overflow — the *valid* result) OR the 100+50-class overflow variant per assembly; verify whichever variant is printed. **Marking scheme:** 2 computation, 2 phenomenon with range statement.

## Section C — Long scenario (25 marks, ~35 min; choose ONE variant)

### C1 — Variant 1: Phishing-led ransomware at a small business

Scenario sheet: employee clicks an invoice attachment; files encrypt; a note demands payment; the only backup is the same machine's external drive, connected always; no MFA on email.

**Required analysis:** incident ordering (disconnect → assess → restore path → report); layer autopsy (human: phishing; endpoint: attachment execution; data: no tested backup); backup post-mortem mapping to 3-2-1 (always-connected drive = same failure domain — not an offsite copy); policy rewrite with role assignment (MFA on email, attachment filtering, restore-tested offline backup, phishing-report culture).

**Marking scheme (rubric per bank):** diagnosis 30% — classes named with discriminating evidence; ordered response 30% — order *rationale* credited (a fix list caps at half); prevention/policy 25% — structural recurrences prevented, roles named; communication 15% — course frameworks by name (3-2-1, isolation, least privilege), claims calibrated.

### C1 — Variant 2: AI tool adopted by a student-services office

Scenario sheet: an office adopts an AI assistant to draft student-facing replies; a reply confidently misstates a deadline; staff vary in verification habits; the vendor claims "95% accuracy".

**Required analysis:** data-use questions (what student data enters prompts — minimization, retention); bias risk in outputs (whose questions get good answers); verification workflow (citations/numbers first, human sign-off for student-facing text); disclosure policy for staff use.

**Marking scheme:** same rubric weights — diagnosis of failure modes with mechanisms (30%), ordered mitigation (30%), policy design (25%), communication (15%). Open-verdict: credit any defensible policy that assigns human responsibility for the high-stakes class.

---

## Time-allocation check (invigilation copy)

| Section | Marks | Minutes | Marks/min |
|---|---|---|---|
| A | 40 | 40 | 1.00 |
| B | 35 | 45 | 0.78 |
| C | 25 | 35 | 0.71 |
| Buffer | — | ~10 | — |
| **Total** | 100 | 120 | — |

B and C are deliberately slower-rate (multi-step work); the buffer absorbs variant-choice reading time in C.

## Academic integrity and assembly notes (instructor copy)

- **Variants:** Section C ships with both variants on the paper (choice announced on it). Randomize variant order between print runs if the room layout permits.
- **Do not reuse** last semester's objective items; the bank supports refresh.
- **Pre-print verification:** recompute B1's discriminating row and B6's chosen variant by hand before printing — an answer-key error is the course's own named failure mode (PB-217); the key-validation habit applies to *us*.
- **Post-exam actions:** log common wrong mechanisms into `../answer-keys/quiz-answer-keys.md`; feed misconceptions into lecture misconception sections; compare grade distribution against the blueprint's difficulty mix and report anomalies in the semester review.
- Publishing restriction: the blueprint (sections, weights, timing) is public; this paper, its model answers, and the marking schemes are not — the site's leak guard and this file's placement outside `docs/` enforce it.
