# Module 2 Slide Decks — L05–L08

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L05 — Von Neumann Architecture (Slides + Speaker Notes)

**Resources:** projector; index cards for the Human CPU activity (module guide prep list); lecture page's architecture diagram.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Bridge from history + objectives | S1–S2 | 8 |
| The big idea: instructions are data | S3 | 12 |
| Five organs, drawn | S4–S6 | 25 |
| Human CPU activity | S7 | 25 |
| The bus and the bottleneck | S8–S9 | 12 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 14 |

### Slides

# L05 · Von Neumann Architecture
**Module 2 · Stage 1 · 2 hours**

## S1 · Bridge: from history to machinery
**Notes:** [~5] TALK: L02 ended at the stored-program idea; today we draw the machine it made possible. ASK: "In one sentence — what was the stored-program idea?" MISC: expect vague "computers got better" — re-anchor to instructions-as-data. TRAN: "Here is that idea as a machine."

## S2 · Today
- The stored-program model as hardware
- Five organs · one bus · one consequence
**Notes:** [~3] TALK: promise the Human CPU activity by name — attention rises. TRAN: the big idea first.

## S3 · The big idea: instructions are data
- Programs load, edit, and swap like any file — no rewiring
**Notes:** [~12] TALK: contrast with fixed-wiring machines; the loom (L02) needed new cards, not new threads — but ENIAC-class machines needed *re-cabling*. Stored instructions end that. ASK: "What does a 'software update' mean in a world where programs are wiring?" MISC: "so software is physical?" — partially yes: it *runs* physically, it *changes* by loading. TRAN: "The organs that run it."

## S4 · Five organs
- Control unit · ALU · memory · input · output
**Notes:** [~10] TALK: draw the five boxes empty; students place each from function ("who decides?", "who computes?", "who remembers?"). ASK: "Where would a running program physically be right now?" (Memory.) MISC: "CPU = the whole box" — separate the organs deliberately. TRAN: "Now the connections."

## S5 · One bus to rule them
- Shared road: instructions AND data travel the same path
**Notes:** [~8] TALK: draw the bus as one road; both directions, all cargo. ASK: "What happens at rush hour?" — the bottleneck preview. MISC: none. TRAN: "That traffic jam has a name."

## S6 · The von Neumann bottleneck
- Shared path limits throughput — the constraint the hierarchy manages
**Notes:** [~7] TALK: name it, promise L07 as the answer, do not solve today. ASK: "Why not just build memory as fast as the CPU?" — cost/volatility park, revisit L07. MISC: none. TRAN: "You are going to *be* the machine now."

## S7 · Activity — Human CPU (25 min)
Control unit · ALU · memory · the bus — three-instruction program, physically passed
**Notes:** [~25] TALK: assign roles *before* explaining the cycle (module guide); cards = instructions. ASK (during): "Memory, what are you holding? Control unit, what are you waiting for?" MISC: teams adding extra instructions — cap at three; the coordination is the lesson. TROUBLE: chaos is data — stop, ask what broke, resume. EXT: run a fourth instruction that jumps. TRAN: "What did the cards teach you about the bus?"

## S8 · What the activity showed
- One thing at a time · memory is the warehouse · the bus is busy
**Notes:** [~5] TALK: harvest three observations from students before showing these. ASK: "Where did the bottleneck appear *physically*?" MISC: none. TRAN: "The honest slide."

## S9 · Variations, honestly
- Harvard-style splits · modern caches — the model is a *base*, not a cage
**Notes:** [~5] TALK: one slide, awareness level, per the lecture page's 5.4. ASK: none. MISC: "so von Neumann is wrong?" — no: it's the reference frame; variations are refinements. TRAN: "Check yourselves."

## S10 · Quick check
1. List the five organs and one job each.
2. Why was "instructions are data" revolutionary?
3. What is the bottleneck, physically?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q3 — expect "the computer is slow" answers; insist on the *shared path* mechanism. TRAN: "Lock it down."

## S11 · Summary
- Stored program: five organs, one bus
- The bottleneck is a feature to manage, not a mistake
**Notes:** [~6] TALK: bullets as exam skeleton. TRAN: exit ticket.

## S12 · Exit ticket
**After the ALU computes an answer, which organ does the result visit next — and how does it get there?**
**Notes:** [~6] TALK: expected: memory, via the bus. Sort tonight; a "straight to output" majority means S5 needs re-teaching at L06's open.

---

## L06 — CPU: The Instruction Cycle (Slides + Speaker Notes)

**Resources:** projector; real CPU spec sheet (guide prep); lecture page's cycle diagram.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Bottleneck recap + objectives | S1–S2 | 8 |
| The cycle, phase by phase | S3–S5 | 22 |
| Paper cycle simulation | S6 | 20 |
| Reading a spec honestly | S7–S9 | 18 |
| Moore's law, calibrated | S10–S11 | 14 |
| Concept check | S12 | 10 |
| Summary + exit ticket | S13–S14 | 10 |
| Buffer | — | 18 |

### Slides

# L06 · CPU: The Instruction Cycle
**Module 2 · Stage 1 · 2 hours**

## S1 · Where L05 left us
**Notes:** [~5] TALK: bottleneck recap via two exit-ticket reads. ASK: "Which organ did we say the result visits?" MISC: none. TRAN: "Today: what the organs *do*, one instruction at a time."

## S2 · Today
- Fetch → decode → execute, and the two registers that run it
- What GHz, cores, and cache actually predict
**Notes:** [~3] TALK: promise that ads will become readable. TRAN: the cycle.

## S3 · FETCH
- Program counter names the address; instruction lands in the IR
**Notes:** [~8] TALK: one phase per slide; narrate the registers as roles, not acronyms. ASK: "Who decides what to fetch?" (The PC.) MISC: "the PC is a physical box" — it's a register; small, fast, in the CPU. TRAN: "Fetched. Now what?"

## S4 · DECODE
- The control unit works out what the instruction means
**Notes:** [~6] TALK: decoding = consulting the instruction's meaning; this is the CU's whole job. ASK: "Why a separate phase at all?" (Different circuitry — translation vs execution.) MISC: none. TRAN: "Meaning established — do it."

## S5 · EXECUTE — then repeat
- ALU or memory acts; the PC advances; the loop closes
**Notes:** [~8] TALK: close the loop on the board; billions per second — the clock *is* the drumbeat. ASK: "What would a jump instruction do to the PC?" (Overwrite it.) MISC: "everything happens at once" — not in this model; insist on the sequential discipline first. TRAN: "Paper machine time."

## S6 · Activity — Cycle simulation (20 min)
Pairs: 5-instruction program · PC/IR table · walk each other's
**Notes:** [~20] TALK: per the lecture page's activity; swap sheets so decoding *someone else's* sloppy table becomes the debugging lesson. ASK (circulating): "Show me where your PC is right now." MISC: teams writing programs too clever — cap complexity; the trace is the skill. TROUBLE: stuck pairs — hand them your own three-instruction starter. EXT: add one jump and re-trace. TRAN: "The cycle in silicon — what do the numbers mean?"

## S7 · Reading a spec: GHz
- Cycles per second — the drumbeat, not the whole song
**Notes:** [~7] TALK: project the real spec sheet; GHz is *rate*, not *work per cycle*. ASK: "Can a slower-clocked chip do more work per second?" (Yes — work per cycle varies.) MISC: "GHz = speed, full stop" — the core misconception; L07 will deepen it with memory waits. TRAN: "Two more numbers."

## S8 · Cores and cache
- Cores: independent cycles in parallel · Cache: keeps the queue fed
**Notes:** [~7] TALK: the two-student race demo (module guide) for cores; cache as the waiter who keeps the chef cooking. ASK: "When do 8 cores not help?" (Sequential work.) MISC: "more cores = proportionally faster" — false for sequential tasks; the demo shows it. TRAN: "The trend that packed all this in."

## S9 · Spec sheet, honestly read
- What the numbers predict · what they cannot
**Notes:** [~4] TALK: three predictions from the sheet, three things it hides (workload, thermals, memory). ASK: none. MISC: none. TRAN: "Moore's law."

## S10 · Moore's law: the observation
- Transistor counts doubled on a cadence — an economic trend, not physics
**Notes:** [~7] TALK: 1965 paper, historical framing (cited on the lecture page); trend, not law. ASK: "What would *end* such a trend?" MISC: "Moore's law is a law" — say "observation" twice. TRAN: "Its current status."

## S11 · Moore's law: today
- Flattening — physics and economics both bite
**Notes:** [~7] TALK: calibrated honesty per the lecture page's 6.3; connect to the multi-core turn (why cores went sideways). ASK: "If transistors stop shrinking, where does more speed come from?" (Cores, specialization, software.) MISC: none. TRAN: "Check the hour."

## S12 · Quick check
1. Name the phases and the register holding the current instruction.
2. The PC's job in one sentence.
3. Two spec numbers beyond GHz — and what each predicts.
**Notes:** [~10] TALK: write-pair-resolve; Q3 is the ad-reading skill. MISC: Q2 — "counts instructions" is close; sharpen to *address of the next*. TRAN: "Summary."

## S13 · Summary
- Fetch → decode → execute; PC and IR run the loop
- GHz, cores, cache: three different levers; Moore's law was the trend that fit them in
**Notes:** [~5] TALK: exam skeleton. TRAN: exit ticket.

## S14 · Exit ticket
**Where does a cycle *wait*, and what is it waiting for?**
**Notes:** [~5] TALK: expected: waiting on memory — the bus from L05. That answer is L07's front door; keep the slips sorted for Monday.

---

## L07 — The Memory Hierarchy (Slides + Speaker Notes)

**Resources:** projector; L05's index cards reused with a "cache" student; lecture page's pyramid.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Wait-for-memory recap + objectives | S1–S2 | 8 |
| The four-way tension | S3–S4 | 15 |
| The ladder, built | S5–S6 | 15 |
| Locality: why it works | S7 | 12 |
| Sorting-cards activity | S8 | 18 |
| RAM/ROM/virtual memory, honestly | S9–S10 | 14 |
| Concept check | S11 | 10 |
| Summary + exit ticket | S12–S13 | 10 |
| Buffer | — | 18 |

### Slides

# L07 · The Memory Hierarchy
**Module 2 · Stage 1 · 2 hours**

## S1 · The wait from L06
**Notes:** [~5] TALK: exit-ticket tally — most of you wrote "waiting on memory." Today explains that wait and what engineers did about it. ASK: none. TRAN: "The impossible wishlist."

## S2 · Today
- Fast, huge, cheap, permanent — pick three, lose one
- The ladder and the locality that pays for it
**Notes:** [~3] TALK: frame as engineering's truce. TRAN: the tension.

## S3 · The four-way tension
- Speed · capacity · cost per bit · volatility
**Notes:** [~8] TALK: define volatility precisely now — it carries the whole module and Lab 2. ASK: "Which of the four do you *feel* as a user?" (Speed and capacity; cost decides what ships.) MISC: "RAM and storage are the same thing" — today's target; name it as the misconception to kill. TRAN: "Prove you can't max all four."

## S4 · Try to max all four
- Teams attempt it; every attempt fails somewhere
**Notes:** [~7] TALK: short challenge from the module guide — let the failure happen in the room. ASK: "Where did your design cheat?" MISC: none. TRAN: "The truce: a ladder."

## S5 · The ladder
- Registers → cache (SRAM) → main memory (DRAM) → storage (SSD/HDD)
**Notes:** [~8] TALK: build bottom-up, one row at a time per the guide; each rung trades down speed for the other three. ASK: "Which rung did L05's cards live on?" (DRAM — with cache students intercepting.) MISC: none. TRAN: "One rung more, honestly."

## S6 · Volatility column, filled
- RAM family forgets · ROM and storage persist
**Notes:** [~7] TALK: power-off thought experiment; connect to "delete vs save" semantics. ASK: "Where does your unsaved essay live — and what does a crash cost?" MISC: "ROM is 'read-only memory' so nothing can read it" — read-*only*, not unreadable. TRAN: "Why a ladder beats a single perfect memory."

## S7 · Locality of reference
- Programs cluster access — temporal + spatial
**Notes:** [~12] TALK: the lecture's conceptual centre; library analogy (desk/shelf/library/warehouse). ASK: "Give one temporal and one spatial locality in your own browsing." MISC: "caching is a backup" — it's staging; originals live below. TRAN: "Prove it with cards."

## S8 · Activity — Sorting cards (18 min)
Teams order the levels · defend against a rival ordering
**Notes:** [~18] TALK: per the lecture page's activity; collect two orderings on the board and reconcile. ASK (circulating): "Which axis made your ordering hard?" MISC: cost-per-GB confusion — units on the board help. EXT: add cloud storage and tape; argue their rungs. TRAN: "Three honest asides."

## S9 · SRAM, DRAM, ROM
- Who lives where, and why each exists
**Notes:** [~7] TALK: awareness level per the lecture page's 7.3; SRAM = cache speed, DRAM = density, ROM = firmware home (L09 preview). ASK: none. MISC: none. TRAN: "When RAM runs out."

## S10 · Virtual memory, in one slide
- The OS borrows storage as extra RAM — with a cost
**Notes:** [~7] TALK: intuition only; the OS details are Module 3's. ASK: "What happens to speed when the borrowing is heavy?" MISC: "virtual memory = cloud" — no; it's local disk pretending. TRAN: "Check the ladder."

## S11 · Quick check
1. Order by speed: SSD, registers, DRAM, L2 cache.
2. Which levels are volatile?
3. Locality in one sentence — and why it pays.
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q2 — registers count as volatile; expect disagreement, resolve with the power-off test. TRAN: "Summary."

## S12 · Summary
- Four axes, no winner; the ladder; locality makes it work
**Notes:** [~5] TALK: exam skeleton; restate the L06 promise: the wait is now explained. TRAN: exit ticket.

## S13 · Exit ticket
**A program is slow. Name one memory-level question you'd ask before blaming the CPU.**
**Notes:** [~5] TALK: any hierarchy-aware answer earns credit; the best ones mention working-set vs RAM. Keep slips — L10's memory-management segment reuses them.

---

## L08 — Storage and Peripherals (Slides + Speaker Notes)

**Resources:** dead HDD + SSD (or photo series); three scenario cards; port gallery slide.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Hierarchy recap + objectives | S1–S2 | 8 |
| Storage technologies, compared | S3–S5 | 22 |
| Peripherals classified | S6–S7 | 14 |
| Ports and protocols | S8 | 8 |
| Requirements workshop | S9 | 28 |
| Concept check | S10 | 10 |
| Summary + exit ticket | S11–S12 | 10 |
| Buffer | — | 20 |

### Slides

# L08 · Storage and Peripherals
**Module 2 · Stage 1 · 2 hours**

## S1 · The ladder's bottom rung
**Notes:** [~5] TALK: L07 ended at storage; today opens the box — technologies, peripherals, and how to *choose*. ASK: "Which axis did storage win last time?" (Capacity, cost per bit; permanence.) TRAN: "The two giants."

## S2 · Today
- HDD vs SSD vs the niches · peripherals in and out · choosing from requirements
**Notes:** [~3] TALK: promise the workshop is assessment-shaped — justifications graded, not parts lists. TRAN: spinning rust first.

## S3 · HDD: the mechanical librarian
- Platters, heads, seek time — and pass the platter around
**Notes:** [~8] TALK: the object sells the lecture (module guide demo); random vs sequential access = *why seeks hurt*. ASK: "Why is 'don't drop it' in the spec?" MISC: none. TRAN: "No moving parts."

## S4 · SSD: the flash warehouse
- Chips, no seek, fast — wear and price are the trade
**Notes:** [~8] TALK: contrast failure *kinds* (sudden wear vs mechanical death); different mechanism, not "faster HDD". ASK: "Which would survive a field researcher's backpack?" MISC: "SSD = faster HDD" — name the mechanism difference explicitly. TRAN: "The niches that survive."

## S5 · Everything else, briefly
- Optical · flash media · tape: each alive where its trade-off fits
**Notes:** [~6] TALK: the point is *niches survive* — archive tape is not nostalgia. ASK: "Where does your university archive transcripts?" MISC: none. TRAN: "Now everything that plugs in."

## S6 · Peripherals: in, out, both
- Three-way classification with rapid-fire examples
**Notes:** [~8] TALK: round-the-room naming; the "both" column is where the argument lives (touchscreen, MFP). ASK: "Is a headset mic+phones one peripheral or two?" MISC: none. TRAN: "How they connect."

## S7 · Ports: shape ≠ speed
- Same plug, different generation — protocol matters
**Notes:** [~8] TALK: port gallery slide; the USB-2-in-USB-3-shaped-port trap. ASK: "Why would a vendor do that?" (Cost/back-compat.) MISC: "if it fits, it works at full speed" — the misconception of the day. TRAN: "Requirements first — now you choose."

## S8 · Activity — Requirements workshop (28 min)
Three scenario cards · spec + justification · then attack another team's
**Notes:** [~28] TALK: per the lecture page's activity and guide's scenario cards; the swap-and-attack is the assessment moment. ASK (circulating): "Which requirement *forces* that choice?" MISC: spec-sheet shopping without justification — return it; requirements first. TROUBLE: teams stuck — re-read the scenario aloud slowly; the budget usually decides. EXT: add a fourth constraint (noise, power). TRAN: "One hour check."

## S9 · Quick check
1. Two rows where HDD wins; one where SSD wins outright.
2. Classify: barcode scanner, projector, touchscreen.
3. Why does port generation matter?
**Notes:** [~10] TALK: write-pair-resolve; Q1 is the justified-trade-off skill. MISC: Q3 — "newer is faster" is incomplete; *same shape, different protocol* is the point. TRAN: "Summary."

## S10 · Summary
- Technologies by trade-off; peripherals by direction; choices by requirements
**Notes:** [~5] TALK: exam skeleton; note the module is complete — hardware drawn end to end. TRAN: exit ticket.

## S11 · Exit ticket
**For the office-assistant scenario: one SSD choice and one HDD choice, one justification each.**
**Notes:** [~5] TALK: expected: SSD for OS/responsiveness, HDD for document mass — but *any* justified split earns credit. TROUBLE: slips short on justification — the workshop rubric applies here too; note who needs the L11 bridge (files live on these disks).
