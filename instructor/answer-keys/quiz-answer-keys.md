# Quiz Answer Keys (Graded Weekly Quizzes — Q01–Q14)

**Instructor-only.** These are the *graded* quizzes (5–10 min, 4–6 items, taken in lecture). The public practice quizzes use different questions — do not copy items across.

Marking convention: each item 1 point unless noted; half points for method-with-arithmetic-slip in numeric items.

---

## Q01 — L01–L02 (graded)

1. Four-part definition: input, processing, output, storage (+programmable/stored instructions for full credit). Application must show *all four* in the student's own example; credit the analysis, not the recall.
2. Hardware/software/data/user classification: accept any 4 correct mappings (e.g., browser app=software, bookmark file=data, CPU=hardware, user=user).
3. Desktop, laptop, phone, tablet = personal/mobile classes; credit any argument using *general-purpose + interactive* as criteria.
4. History ordering: abacus→Jacquard→Babbage→ENIAC→transistor→IC→microprocessor; half mark if only the electronic era ordered correctly.
5. Anything demonstrating "computers are inside other devices" (embedded systems accepted as the key insight).

## Q02 — L03–L04

1. Classification items: weather=supercomputer; payroll=batch/mainframe or server (accept either with justification); hearing aid=embedded; degree coursework=personal computer.
2. General vs special purpose: the criterion is *range of tasks programmable*, not size.
3. Divide layers: access / skills / outcomes — one example each; credit any real, checkable example.
4. Task reallocation example: accept any pair where the *task* (not the job) moved or was created.
5. Ethics item: grade the four-step structure (stakeholders→harms→rule→hard case), not the position.

## Q03 — L05–L06

1. Diagram: CPU (CU, ALU, registers) + memory + I/O + buses; all four labels required for full credit.
2. Stored program: program held in memory as data; consequence = program switchability/software industry.
3. Cycle order: fetch→decode→execute; PC advance must be placed at fetch for full credit.
4. GHz caveat: any two of work-per-cycle, cache, memory speed, core efficiency.
5. Moore's law: transistor *density* doubling ≈ every two years; must call it an observed trend (not physical law) for full credit.

## Q04 — L07–L08

1. Hierarchy ordering (fast→slow): registers, cache, RAM, SSD, HDD; half mark per correct adjacent pair.
2. Locality: temporal = reuse of recent items; spatial = use of neighbours; both defined with one example each.
3. RAM vs storage: volatility + speed roles; "16 GB vs 1 TB" style answers need the *why*.
4. 3-2-1: three copies, two media, one offsite; the "media" distinction is the usual miss — note it in feedback.
5. Peripheral classification: accept defensible classifications; touch screen must be "both."

## Q05 — L09–L10

1. Stack placement: applications on top; drivers/firmware below OS; antivirus = system software (utility). Firmware placement is the discriminator.
2. License comparison: freedom-to-modify for FOSS vs restrictions for proprietary; "no cost" alone earns half.
3. Boot sequence: firmware→POST→bootloader→kernel→login; bootloader/kernel order is the discriminator.
4. OS responsibilities: any four of process/memory/device/file/UI management.
5. CLI task: any bulk/precise/repeatable task with a reason; "programmers use it" is not a reason.

## Q06 — L11–L12

1. Path construction: full tree from root; watch for missing drive letter (Windows) or leading slash (Unix).
2. Relative path: `..` resolution must land on the correct sibling directory.
3. Extension question: extension = label/convention, content decides; renaming does not convert.
4. Backup: 3-2-1 mapping to the student's *own* data; generic answers earn half.
5. Troubleshooting ordering: define→reproduce→isolate→hypothesis/test→escalate; "restart" accepted only as an isolate step, not the whole answer.

## Q07 — Module 3 cumulative

1. Integration items graded against the L09–L12 thread; each of the five sentences carries its lecture's key term (layer, process, path, patching, isolate).
2. Driver-failure analysis: isolation + rollback = full credit; "reinstall Windows" earns half at most.
3. Permission red flags: purpose-alignment test must be named.
4. Update priority: *known, exploited vulnerability* mechanism required.

## Q08 — L13–L14

1. Conversions: check *method* (division chains/nibble grouping) — correct answers without method earn half.
2. Two's complement encoding: flip-and-add-one shown; the −128 edge case is the discriminator.
3. Overflow: identify wrapped result AND the lost carry; either missing = half.
4. Hex colour: byte-per-channel mapping; accept either #RRGGBB byte order interpretation only if consistent.
5. "Why binary": two-state hardware reliability/cost argument; "computers are digital" is not an explanation.

## Q09 — L15–L16

1. ASCII values: A=65, a=97, 0=48; the +32 offset rationale earns the third point.
2. Unicode vs UTF-8: map vs encoding distinction is the discriminator; "UTF-8 is backwards compatible with ASCII" earns the second point.
3. Mojibake: wrong-encoding interpretation, not corruption; fix = re-decode.
4. Sampling: rate×depth×channels×seconds setup correct = most of the credit; unit slips lose the rest.
5. Lossy/lossless choice: content-type reasoning (text/code/archives lossless; photos/audio lossy at adequate quality).

## Q10 — L17–L18

1. Truth table completeness: all 2^n rows; every intermediate column for compound expressions.
2. De Morgan: AND↔OR flip on negation distribution; accept either law correctly applied.
3. XOR vs OR: the both-true row is the discriminator.
4. Half adder: Sum=XOR, Carry=AND; full-adder carry-in mention for full credit.
5. Circuit trace: left-to-right evaluation with intermediate wire values; the trace *is* the answer.

## Q11 — L19–L21

1. Relative/absolute reference: post-copy formula exact; `$` reasoning stated.
2. IF nesting: boundary order must make ranges disjoint; accept XLOOKUP-era alternatives in lookups.
3. Chart choice: message-to-type match; truncated-axis or 3-D acceptance = no credit.
4. Network classes: PAN/LAN/WAN mapping with scale reasoning.
5. Bandwidth vs latency: definitions AND the "which application needs which" judgement.

## Q12 — L22–L24

1. DNS chain: resolver→root→TLD→authoritative; caching rationale for repeats.
2. Packet switching: independence + reassembly; "TCP reorders" earns the second point.
3. URL anatomy: all four parts; query-string purpose bonus.
4. HTTPS guarantees: confidentiality + authentication; "safe site" conflation = no credit (see A5).
5. Cloud models: responsibility-boundary mapping; SaaS data ownership noted.

## Q13 — L25–L28

1. DBMS justification: concurrency + integrity (both named); "bigger" earns nothing.
2. PK/FK identification + the guarantee each provides.
3. SQL reading: FROM→JOIN→WHERE→SELECT order; join predicate presence is the discriminator.
4. Bias mechanism: data→model→outcome chain; "bad data" alone earns half.
5. AI verification habit: verify-against-source (any two concrete output types).

## Q14 — L29–L31

1. Threat classes: worm/phishing/ransomware/trojan mapped correctly.
2. MFA: knowledge+possession categories; "extra security" alone earns half.
3. Password guidance: length+uniqueness+change-on-compromise; contrast with periodic expiry.
4. Privacy: incognito ≠ anonymity; local vs network distinction.
5. Computational thinking: decomposition applied to a *new* problem (not the lecture's example); algorithm has finite, unambiguous steps.

---

## Common-mistakes log (grows each semester)

*(Record recurring wrong answers here; migrate confirmed patterns into each lecture's "Common misconceptions" section at semester end.)*
