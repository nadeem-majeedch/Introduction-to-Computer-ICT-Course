# Midterm Examination — Draft Paper (Modules 1–4)

**Instructor-only. Do not publish.** Assembled from `midterm-exam-bank.md` per the public blueprint (90 min, 100 marks). Every item verified against lecture content; model answers and marking scheme below each item. Coverage: CLO-1 ×2 (A1, A2), CLO-2 ×2 (A5, B3), CLO-3 ×2 (A9, B2), CLO-4 ×4 (B1, B2, A13, B4-method) — meets the blueprint's twice-per-CLO guarantee. CLO-5 appears only as the clearly-labelled bonus item per the bank's note.

---

## Section A — Short conceptual (40 marks, ~35 min)

### A1. The four-part definition *(6 marks · CLO-1)*

Define a computer with the four-part definition, then classify: (i) a programmable washing machine, (ii) a server, (iii) a pocket calculator.

**Marking scheme:** 2 marks for the definition (input, processing, output, storage — all four named); 1 mark per correct classification + 1 mark for the best-argued classification. Model: washing machine = embedded special-purpose computer (all four parts present, program fixed); server = general-purpose computer at server scale; pocket calculator = special-purpose computer (processing/input/output, minimal storage).

### A2. Timeline with one causal link *(4 marks · CLO-1)*

Order: stored-program concept, transistor, Jacquard loom, Intel 4004, ENIAC. State one causal link.

**Marking scheme:** 3 marks for correct order (loom → ENIAC → stored-program → transistor → 4004); 1 mark for a valid causal link (e.g., transistor miniaturization → single-chip CPU).

### A3. Digital divide layers *(4 marks · CLO-1/CLO-10)*

Name the three layers; one intervention per layer.

**Marking scheme:** 1 mark per layer named (access, skills, usage/outcome); 1 mark for a coherent intervention set (any reasonable pairing).

### A5. Von Neumann with buses *(6 marks · CLO-2)*

Sketch the organization; label what travels on the buses.

**Marking scheme:** 2 marks for correct blocks (CPU with control+ALU, memory, I/O); 2 marks for the three buses named; 2 marks for correct bus contents (addresses / data / control signals).

### A6. Stored-program significance *(4 marks · CLO-2)*

One-sentence-plus explanation of why the stored-program concept changed computing.

**Marking scheme:** 2 marks for "program in memory as data"; 2 marks for the consequence (loadable/changeable software → the modern software ecosystem).

### A7. Memory hierarchy ranking *(5 marks · CLO-2)*

Rank registers, cache, RAM, SSD, HDD, tape/cloud-archive; justify with one principle.

**Marking scheme:** 3 marks for correct order; 2 marks for the locality/latency principle (faster = smaller/closer because of physics and economics; hierarchy exists to hide latency).

### A8. RAID vs backup *(4 marks · CLO-2)*

Scenario: mirrored drives; which failure classes does mirroring survive, which does it not?

**Marking scheme:** 2 marks for "survives single-drive failure"; 2 marks for naming a non-surviving class (deletion/ransomware/theft — mirrors propagate deletions).

### A9. Stack placement *(5 marks · CLO-3)*

Place: word processor, Linux kernel, file manager, device driver, browser, BIOS/UEFI.

**Marking scheme:** 4 marks for correct placement (apps / OS / drivers / firmware); 1 mark for any justified tricky placement.

### A10. Boot sequence diagnosis *(5 marks · CLO-3)*

Power on, fans spin, no logo. Which stage failed; what do you test first?

**Marking scheme:** 3 marks for placing the fault pre-POST/display (firmware/POST or display path — *not* storage); 2 marks for a safe first test (other monitor/cable, beep codes, reseat RAM unplugged).

### A11. Paths *(4 marks · CLO-3)*

Given `C:\Users\sami\Documents` and file in `courses\ict\`, write absolute + relative paths.

**Marking scheme:** 2 marks each, correct syntax; note relative path depends on the current directory (accept with working directory stated).

### A12. Update priority *(4 marks · CLO-3)*

Why security updates outrank feature updates, mechanically.

**Marking scheme:** 2 marks for "known, public vulnerabilities → exploits exist"; 2 marks for the deferral risk stated as exposure-with-a-clock.

### A13. Why base 2 *(4 marks · CLO-4)*

The hardware-economics argument.

**Marking scheme:** 2 marks for two-state noise tolerance; 2 marks for the cost/density trade-off stated honestly (multi-level cells exist where density wins).

### A14. Encoding relationship *(4 marks · CLO-4)*

ASCII vs Unicode vs UTF-8; identify a mojibake pattern.

**Marking scheme:** 2 marks for the relationship (Unicode = the character set/code points; UTF-8 = the variable-length byte encoding; ASCII ⊂ UTF-8); 2 marks for mojibake (bytes decoded as the wrong encoding; `Ã©`-class example).

### Objective items A15–A20 *(6 × 1.5 = 9 marks · mixed CLOs)*

Six true/false + one-line why, drawn fresh per sitting from the bank's concept items (suggested: two's complement sign convention; sync-vs-backup; SSD vs HDD mechanism; kernel role; path syntax; delete semantics).

**Marking scheme:** 1 mark for the verdict, 0.5 for a correct reason. No reason, half credit.

## Section B — Worked problems (40 marks, ~40 min)

### B1. Conversions with method *(10 marks · CLO-4)*

(a) 200 → binary → hex. (b) `0x2F` → decimal. (c) `144₈` → decimal.

**Marking scheme:** method marks dominate — (a) 4 marks: 3 for shown division-by-2 (or sum-of-powers) working, 1 for `11001000₂`/`C8₁₆`; (b) 3 marks: 2 positional expansion, 1 answer (47); (c) 3 marks: 2 expansion, 1 answer (100). Correct answers without method: half credit at most.

### B2. Two's complement *(10 marks · CLO-4)*

(a) Encode −45 in 8-bit. (b) Decode `1011 0110`. (c) 100 + 50 in 8-bit signed; name the phenomenon.

**Model answers:** (a) +45 = `0010 1101` → invert `1101 0010` → +1 = **`1101 0011`**. (b) MSB=1 → negative: invert `0100 1001` → +1 = `0100 1010` = 74 → **−74**. (c) 150 needs 9 bits; result `1001 0110` = **−106** → **overflow** (range −128…+127; hardware flag notes it; language/runtime decides whether software checks).

**Marking scheme:** (a) 3 (1 method, 2 answer); (b) 3 (1 method, 2 answer); (c) 4 (2 computation, 1 naming overflow, 1 for the range statement).

### B3. Truth table with intermediate columns *(10 marks · CLO-2 justification item — see bank note; treat as the memory-budget alternative below if CLO-5 must be excluded)*

Three-variable expression `(A AND NOT B) OR C`, intermediate columns required.

**Model answer:** 000→0, 001→1, 010→0, 011→1, 100→1, 101→1, 110→0, 111→1 (intermediates ¬B and A∧¬B shown).

**Marking scheme:** 2 marks per correct intermediate column pair; 4 marks for the final column; −1 per wrong row, max 2 rows penalized.

> **Assembly note:** per the bank's CLO-5 rule, either include this as clearly-labelled *bonus* (recommended: +4 bonus) or substitute the **memory-budget allocation** item from bank B4 (workload + prices → allocate cache/RAM/SSD budget with justification; model: match budget to working set; 10 marks, CLO-2). Do not count B3 toward the core 100.

### B4. Memory-budget allocation *(10 marks · CLO-2 · the non-bonus B-slot)*

Scenario: office PC, workload = browser + documents; budget fixed; choose between more cache-class speed, more RAM, or faster storage; justify with locality.

**Model answer:** allocate to RAM first (working set > RAM is what causes swapping — the dominant felt slowness); SSD second (I/O latency); cache is not purchasable at this scale (bundled with CPU). Justification must cite the workload's working-set size vs RAM and the swap mechanism.

**Marking scheme:** 4 for the ranked allocation with amounts; 4 for locality/swapping justification; 2 for explicitly rejecting the mis-allocated option.

## Section C — Mini-scenario (20 marks, ~15 min)

### C1. The small office that limps *(20 marks · CLO-2, CLO-3)*

"Slow PC: 4 GB RAM, HDD 92% full, no backups, updates disabled, two staff sharing one account." Diagnose the three most consequential problems, order fixes by impact, write the 3-2-1 plan.

**Model answer (shape):** Problems: (1) memory pressure → swapping (dominant felt slowness); (2) disk nearly full on HDD (update/scratch starvation, latency); (3) update-disabled + no backups + shared admin account (risk cluster). Order: free/upgrade memory path first (RAM), disk cleanup/SSD second, then patching + backup habit — impact-ordered because swapping dominates observed slowness and is cheapest to relieve. 3-2-1: 3 copies (working + external drive + cloud/university storage), 2 media classes, 1 offsite; automated and restore-tested.

**Marking scheme:** 6 diagnosis (2 each, evidence-linked); 8 ordered fixes (2 per fix, 2 for the *ordering rationale* — lists without rationale cap at half); 6 for the 3-2-1 plan (3 copies/2 media/1 offsite named, automation + test mentioned for full marks).

---

## Time-allocation check (for the invigilation copy)

| Section | Marks | Minutes | Marks/min |
|---|---|---|---|
| A | 40 | 35 | 1.14 |
| B | 40 | 40 | 1.00 |
| C | 20 | 15 | 1.33 |
| Buffer (reading, review) | — | ~5 | — |
| **Total** | 100 | 90 | — |

Marks/min stays ≤ 1.4 — students attempting top-to-bottom at normal pace finish with review time. C's rate is higher by design: it is one scenario, not 20 items.

## Academic integrity notes (invigilator copy)

- Closed book, no devices; the arithmetic is deliberately calculator-free.
- Section A objective items are refreshed per sitting from the bank; do not reuse last year's paper.
- Wrong-answer logging: after marking, log the three most common wrong mechanisms into `../answer-keys/quiz-answer-keys.md` and feed misconceptions back into lecture "Common misconceptions" sections (post-exam actions from the bank).
