# Teaching Guide — Module 1: Foundations: The Digital World

**Module 1** · Stage 1 · 4 lectures (L01–L04) · 8 contact hours
Companion to the lecture pages `L01`–`L04` under `docs/lectures/`. **Not published** — this tree exists only in the repository. Answers to exit tickets appear here and nowhere student-facing.

> Symbols used below: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] Load every lecture page in a browser once; check the two projector-visible fonts render (sections rely on the Mermaid diagrams).
- [ ] L02: print or project the timeline images referenced in the lecture; test in the actual lecture-hall projector (dark backgrounds often wash out).
- [ ] L01/L03/L04 need no lab software, but have the course website's [Schedule](docs/schedule.md) projected for the L01 course-map segment.
- [ ] Verify Lab 1 machines are ready for the same week (lab runs in Module 1 per the schedule).

## Misconception warnings (module level)

1. **"Computer = laptop/desktop."** Attacks it in L01 and never lets go; re-ask in L03 with embedded devices.
2. **"Older computers were just slower."** L02's generation story is about *mechanisms* (relays → vacuum tubes → transistors → ICs), not merely speed.
3. **"Bigger number = better computer."** L03's classification is by purpose and capability, not price.
4. **Ethics debates collapse into slogans.** L04's four-step reasoning method is the corrective; grade the method, not the stance.

---

## L01 — What Is a Computer?

**Teaching tips:**
- Open with a prop, not a slide: hold up a calculator and ask "is this a computer?" Collect votes *before* teaching anything. The vote split gives you the lecture's motivating tension.
- The four-part definition (input, processing, output, storage, programmable) is the module's anchor; write it large and never paraphrase it loosely.
- Watch the clock: L01 carries course-administration duty (course map, rhythm, help page). Give the map 10 focused minutes, not the whole opening.

**Board / projector plan:**
- [Board] Four-part definition with blank boxes, filled in from student examples.
- [Slide] The four-part flow diagram from the lecture page's "Visual explanation" section.
- [Board] Two-column table: hardware / software / data / user, filled with the messaging-app scenario.
- [Slide] Course website home → Schedule → Assessment, live navigation.

**Suggested demonstration:** Smartwatch vs mechanical alarm clock side by side (or photos if you lack devices). Walk each through the four parts; the mechanical clock fails at *processing data*, not at ticking.

**Misconception warnings:** See module level 1. Additionally, students conflate *data* with *information* — press the "34.2" vs "your balance is 34.2" contrast until someone rephrases it in their own words.

**Discussion prompts:**
1. Name a device you own that contains a computer but isn't called a computer.
2. Where is the computer in a supermarket checkout? (Expect: barcode scanner input, price-lookup processing, till output, inventory storage.)
3. Is a programmable microwave a computer? (Boundary case — accept reasoned positions.)

**Exit-ticket questions (with answers):**
1. *State the four parts of the definition of a computer.* — Input, processing, output, storage, under stored/programmable instructions.
2. *Classify: messaging app, photo being edited, CPU, photographer.* — Software; data; hardware; user.
3. *Why is a mechanical clock not a computer?* — No programmable processing of data; it models time mechanically.
4. *One example each of input, processing, output, storage in a supermarket checkout.* — Barcode scan; price lookup; till display/receipt; stock database update.
5. *Where do you find which topics a quiz covers?* — The course website's schedule/assessment pages.

---

## L02 — A Brief History of Computing

**Teaching tips:**
- Teach this as a *causal chain*, not a museum tour: each generation's mechanism failure motivates the next mechanism. If students leave able to explain "why did vacuum tubes give way to transistors," the lecture worked.
- Keep dates to the handful the timeline jigsaw uses; the skill being assessed is ordering and justification, not memorized years.
- The jigsaw (A1) needs the last ~30 minutes; front-load the concept segments.

**Board / projector plan:**
- [Board] Horizontal timeline skeleton; students place device cards as the lecture proceeds.
- [Slide] One portrait image per era (Jacquard loom; ENIAC room; transistor; microprocessor die; modern SoC).
- [Board] Three-word summary of each generation's enabling technology.

**Suggested demonstration:** If available, a physical punch card or a strip of film; otherwise a projector image plus the "pass the instruction card" gesture used later in L05's Human CPU — early preview.

**Misconception warnings:** See module level 2. Also: students attribute the PC revolution to microprocessors alone; name the co-factors (mass storage, software ecosystems, falling prices).

**Discussion prompts:**
1. Which single invention in the timeline most changed *who could use* computers, and why?
2. The loom stored instructions as holes in cards. What is the modern equivalent in your phone?
3. Why did time-sharing matter for universities specifically?

**Exit-ticket questions (with answers):**
1. *Order: microprocessor, transistor, integrated circuit, vacuum tube.* — Vacuum tube → transistor → integrated circuit → microprocessor.
2. *What made the stored-program idea powerful?* — Programs become data: reloadable, editable, swappable without rewiring.
3. *Name one way each of two eras shows up in your phone.* — e.g., transistor-scale integration (SoC), stored program (apps), touch I/O from mobile-era designs.
4. *Why did transistors enable integrated circuits?* — Solid-state switching is small, reliable, mass-fabricable — many can live on one wafer.

---

## L03 — Types of Computers

**Teaching tips:**
- This is a classification lecture; the risk is rote list-memorization. Force *justification* language: throughput, reliability, cost — the three axes the objectives name.
- "Classify the room" works best with a hard-case reveal at the end: the projector, the smart speaker, the door-access controller.

**Board / projector plan:**
- [Board] Six-class ladder (supercomputer → mainframe → server → workstation/PC → mobile → embedded) with the three axes as columns.
- [Slide] One real system photo per class, captioned with the domain that buys them.

**Suggested demonstration:** Phone teardown photo series or a dead laptop's board vs a Raspberry-Pi-class board: same concepts, wildly different scale envelope.

**Misconception warnings:** See module level 3. Also: "servers are just computers in racks" — true but incomplete; the interesting part is the *service* framing and 24/7 reliability engineering.

**Discussion prompts:**
1. Your university's results portal: which classes of computers touch it between "you click" and "grade appears"?
2. Is a smart TV embedded or general-purpose? Defend with the definition.
3. Why do banks still run mainframes alongside cloud servers?

**Exit-ticket questions (with answers):**
1. *Match: weather forecasting; university transcript database; car engine timing.* — Supercomputer; server/mainframe; embedded system.
2. *General- vs special-purpose: ATM.* — Special-purpose with a general-purpose computer inside (boundary case, reasoned positions accepted).
3. *Two axes that separate a workstation from a phone.* — Sustained compute/thermal envelope; I/O breadth; price point (any two, justified).
4. *Where does a smart speaker sit, and why?* — Embedded system built around networked voice services; mostly fixed-purpose.

---

## L04 — Computers, Society, and You

**Teaching tips:**
- The structured debate is the module's climax. Invest the 25 minutes; the four-step method (state the claim, identify stakeholders, weigh evidence, state the trade-off) is examinable and reused in Module 8.
- Guard against anecdote-driven generalization: every "in my country…" claim should be sharpened into "access / skills / outcomes" divide vocabulary.
- Career map: keep it concrete — name the course's own modules that feed each family (networks → Module 6, data → Module 7).

**Board / projector plan:**
- [Board] Four-step reasoning method as a numbered scaffold, visible during the whole debate.
- [Board] Digital divide as three concentric rings: access, skills, outcomes.
- [Slide] ICT career family map tied to course modules.

**Suggested demonstration:** Project two screenshots of the *same* government service: one via smartphone app, one via a dial-in menu. The divide becomes visible without preaching.

**Misconception warnings:** See module level 4. Also: "automation eliminates jobs" as a totalizing claim — replace with task-level automation evidence and transition costs.

**Discussion prompts:**
1. Which jobs in this city are *most* automatable by task, and what happens to the people?
2. Whose responsibility is closing the divide: individuals, companies, or the state? Use the four-step method.
3. Which ethical principle from today applies to next semester's data-science work?

**Exit-ticket questions (with answers):**
1. *Name the three dimensions of the digital divide with one example each.* — Access (no device/bandwidth), skills (can't use effectively), outcomes (differential benefit).
2. *Apply the four-step method to one automation claim.* — Full claim → stakeholders → evidence → trade-off (graded on structure, not stance).
3. *Which course module maps to the career family that interests you?* — Any defensible mapping (e.g., Module 7 → data analyst).
