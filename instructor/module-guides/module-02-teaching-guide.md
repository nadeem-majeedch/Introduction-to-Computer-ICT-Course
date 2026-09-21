# Teaching Guide — Module 2: Hardware: Inside the Machine

**Module 2** · Stage 1 · 4 lectures (L05–L08) · 8 contact hours
Companion to lecture pages `L05`–`L08` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] Lab 2 (hardware inventory) runs this module: confirm machines/OS screenshots are ready; the lab needs no special software beyond system-info tools.
- [ ] L05/L06 use Mermaid diagrams projected large — test the lecture-hall projector with dark theme off.
- [ ] Borrow or photograph: one dead HDD (platter visible) and one SSD; the L08 storage segment is far stronger with the real objects.

## Misconception warnings (module level)

1. **"Memory and storage are the same thing."** The L07 hierarchy exists to kill this; keep the words *volatile* and *persistent* doing distinct work all module.
2. **"A bigger GHz number means a faster computer."** L06 addresses it, but expect it again at L08 when students compare machines; reuse the cores/cache/IPB framing.
3. **"The CPU runs the whole program at once."** The fetch–decode–execute cycle is deliberately tiny; insist on one-instruction-at-a-time traces before any talk of pipelining.
4. **"More RAM always = faster."** Locality explains when it does and doesn't; keep L07's trade-off table visible.

---

## L05 — Von Neumann Architecture

**Teaching tips:**
- The "Human CPU" activity is the module's best 20 minutes; assign roles *before* explaining the cycle so students feel the coordination problem first.
- Keep "stored program" as the punchline: instructions are *data in memory* — the 1945 idea students already met historically in L02.
- Name the bottleneck honestly but briefly; it returns with real force in L07.

**Board / projector plan:**
- [Board] Five boxes (CU, ALU, memory, input, output) drawn empty, filled in as students place them; bus drawn as one shared road.
- [Slide] The Mermaid architecture diagram from the lecture page's "Visual explanation."
- [Board] A three-instruction program as numbered cards on the tray/board edge, reused in the activity.

**Suggested demonstration:** Physically pass three index cards (instructions) between "memory" and "control unit" students while the class calls out each step — the cards *are* the shared bus.

**Misconception warnings:**
- "The CPU and memory are one unit." Show the bus delay physically in the demo.
- "RAM is where programs go to die when you close them." Distinguish *running* (in memory) from *saved* (in storage) — the L07 bridge.
- "Von Neumann is the only design." Point to 5.4's honesty note (Harvard-style splits, modern caches) without going deep.

**Discussion prompts:**
1. What breaks if instructions and data share one bus? (Motivate the bottleneck before naming it.)
2. Your phone has several cores. Does the von Neumann model change? (No — it repeats.)
3. Where in this diagram does your mouse click live? (Input → memory as data.)

**Exit-ticket questions (with answers):**
1. *List the five organs and one job each.* — CU (directs), ALU (arith/logic), memory (holds programs+data), input, output.
2. *Why was "instructions are data" revolutionary?* — Programs reloadable/editable/swappable without rewiring hardware.
3. *What is the von Neumann bottleneck?* — The shared CPU–memory path limits throughput; data and instructions queue on one bus.
4. *Trace: where does an answer produced by the ALU go?* — Written back to memory (then possibly to output).

---

## L06 — CPU: The Instruction Cycle

**Teaching tips:**
- Run the paper cycle simulation *twice*: once slowly with narrated phases, once at speed to show why clocks exist.
- The spec-reading segment (6.2) is where CS and DS interests converge: everyone buys laptops. Have one real spec sheet projected.
- Moore's law: teach it as a *historical economic trend* with a defined end, not a physics law; the lecture page's phrasing is calibrated — mirror it.

**Board / projector plan:**
- [Board] Fetch → Decode → Execute as three columns; PC and IR written above, updated in a different colour each round.
- [Slide] The Mermaid cycle diagram from the lecture page's "Visual explanation."
- [Slide] One real CPU spec sheet (cores, clock, cache) with callouts.

**Suggested demonstration:** Two students "race": one does four additions sequentially (one core), one does them two-at-a-time (two cores); then a third interrupts with a memory fetch — the wait is the point.

**Misconception warnings:**
- "GHz alone measures speed." Cache misses, memory waits, and work-per-cycle dominate; the demo shows a wasted cycle.
- "More cores always help." Sequential tasks don't split; parallel needs parallel work.
- "Moore's law is a law." It's an observed trend (Moore, 1965) now flattening — physics and economics, not legislation.

**Discussion prompts:**
1. Where does a cycle *wait*, and what is it waiting for? (Memory — preview of L07.)
2. Why do phone chips advertise "big and little" cores?
3. What would a program need to look like to use 8 cores well?

**Exit-ticket questions (with answers):**
1. *Name the three phases and the register that holds the current instruction.* — Fetch, decode, execute; instruction register (IR).
2. *What does the program counter do?* — Holds the address of the next instruction; advances (or jumps) each cycle.
3. *Two specs you'd read beyond GHz when comparing CPUs.* — Core count, cache size (accept also workload fit).
4. *State Moore's observation in one sentence and its current status.* — Transistor counts roughly doubled on a cadence historically; the trend has slowed toward its physical/economic limits.

---

## L07 — The Memory Hierarchy

**Teaching tips:**
- Open with the four-way trade-off as a *tension*, not a table: "you cannot max all four columns — prove it." Let students try.
- The card-sorting activity from the lecture page needs ~15 minutes; collect two team orderings on the board and let the class reconcile them.
- Virtual memory: one intuition only (disk pretending to be RAM when needed), flag as "revisited in Module 3."

**Board / projector plan:**
- [Board] The speed/capacity/cost/volatility table built one row at a time, bottom (storage) to top (registers).
- [Slide] The pyramid diagram from the lecture page's "Visual explanation."
- [Board] A library analogy sketch: desk (registers), bookshelf (cache), library (RAM), off-site warehouse (storage).

**Suggested demonstration:** If you built the L05 card-passing, repeat it *with a cache student* standing between memory and CPU holding the two most-recently-used cards — count the avoided trips.

**Misconception warnings:**
- "RAM and storage are interchangeable." Volatility demo: power off ↔ programs vanish from RAM, files persist on storage.
- "Cache is a backup." It's a *staging* copy; originals live below.
- "The hierarchy is about capacity only." It's about latency distance — each level is orders of magnitude apart.

**Discussion prompts:**
1. Why not build the whole computer from fast memory? (Cost per bit, heat, volatility.)
2. When you reopen yesterday's document instantly, which level did the OS use?
3. Why does browsing feel fast even though RAM is slower than cache? (Locality.)

**Exit-ticket questions (with answers):**
1. *Order by speed: SSD, registers, DRAM, L2 cache.* — Registers > L2 cache > DRAM > SSD.
2. *What does volatile mean, and which levels have it?* — Contents vanish without power; registers, SRAM/DRAM (RAM family) — not SSD/HDD.
3. *Define locality of reference in one sentence.* — Programs cluster access to the same small set of addresses (temporal + spatial), so small fast caches pay off.
4. *Why does the hierarchy "work"?* — Locality keeps the working set in fast levels; misses are rare relative to hits.

---

## L08 — Storage and Peripherals

**Teaching tips:**
- Pass the physical HDD/SSD around *during* the comparison table, not after — the platter vs chips contrast anchors the durability row.
- The requirements workshop (three scenario cards) is the assessment-relevant skill: justify every line against the requirement, not against "gaming is cool."
- Close the module by connecting storage here to files in L11: "next module, the OS turns this hardware into folders."

**Board / projector plan:**
- [Board] Storage comparison table (speed, durability, capacity, cost) filled from student knowledge, corrected in place.
- [Board] Peripheral classification: three columns (input / output / both) populated by rapid-fire round.
- [Slide] Port gallery: USB-A/C, HDMI, audio jack, network port.

**Suggested demonstration:** The open HDD spin-up (if a sacrificial drive is available) — hearing seek clicks while explaining random vs sequential access is unforgettable; otherwise the photo series.

**Misconception warnings:**
- "SSDs are just faster HDDs." Different mechanism (flash vs magnetism), different failure modes and wear behaviour.
- "Delete = gone." Storage semantics and the path to L11's backups; keep it brief but plant it.
- "Any port fits any device." Speed and protocol differences across same-shaped ports (USB 2 vs USB 3 vs Thunderbolt-class).

**Discussion prompts:**
1. Why does the field researcher card demand SSD even though HDD is cheaper per GB? (Durability, power, vibration.)
2. Which peripherals are both input and output? (Touchscreens, headset combos, all-in-one printers.)
3. Where should the 3-2-1 rule's second copy physically live? (Preview of L11.)

**Exit-ticket questions (with answers):**
1. *Two rows where HDD beats SSD and one where SSD wins outright.* — Capacity per unit cost, archival sequential reads; speed/durability/power for SSD (any two rows HDD, justification for SSD).
2. *Classify: barcode scanner, projector, touchscreen.* — Input; output; both.
3. *Why does a spec's port generation matter?* — Same connector shape can carry very different bandwidth/protocol versions.
4. *Recommend a storage split for an office assistant scenario and justify.* — Small SSD for OS/apps + large HDD for documents/archives, cost-balanced (accept any justified split).
