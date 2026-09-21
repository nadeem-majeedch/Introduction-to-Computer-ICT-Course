# Problem-Solving Case Bank — Level 2: Intermediate

**25 cases** · PB-201–PB-225 · Now the progression shifts from *understand* to **decompose and compare**: these cases need multi-step reasoning, at least one quantified comparison, and an explicit trade-off. Method and rubric: [bank index](index.md).

---

## PB-201 · Level 2 · The update loop that ate the workday

**Domain:** Operating systems · **Related lectures:** L10, L12

**Scenario.** Every evening, an update installs at shutdown and "undoes changes" at boot. Three days running. The student has started switching the laptop off at the wall to avoid the cycle.

**Problem statement.** Break the cycle *safely*: diagnose the likely states, restore a working update path, and keep security intact.

**Stakeholders.** The student (time, security); IT support (fix backlog); the vendor (update integrity).

**Inputs:** undo-loop symptom; wall-switch habit; exam-week workload. **Outputs:** diagnosis + recovery order + prevention. **Constraints:** updates must end up enabled; no data loss.

**Learning objectives.** Decompose a failure loop into states; sequence recovery (backup → diagnose → repair) rather than react.

**Available information.** Free disk space is low (updates need workspace); the rollback happens at boot; a restore point exists.

**Student task.** State the loop's two failing states, the recovery order, and why wall-switching makes things worse.

**Suggested thinking time.** 12 minutes; then group.

**Expected solution characteristics.** States: (a) update can't complete — likely disk-space starvation; (b) rollback marks it uninstalled, so it retries; recovery: free space → run update on AC power with time → verify; wall-switching corrupts the cycle further and skips safety writes; prevention: scheduled update windows (L12's deliberate patching).

**Discussion questions.**

1. Which single measurement (disk space, error code, update log) would confirm the diagnosis fastest?
2. What does the wall-switch habit cost *beyond* this loop?

**Extension challenge.** Write the five-line "safe recovery from an update loop" help-desk script.

**References.** Course L12 (patching), vendor update documentation (instructor-provided).

---

## PB-202 · Level 2 · Why does 19.99 + 19.99 come to 40.00?

**Domain:** Data representation · **Related lectures:** L14, L19

**Scenario.** A shop's spreadsheet adds two 19.99 items and displays 40.00 — the "should be 39.98" story a cousin swears proves computers can't add.

**Problem statement.** Explain what binary floating point actually did here, and design the cent-safe way to run the shop's totals.

**Stakeholders.** The shop owner (accounts); customers (fair totals); the spreadsheet author (you).

**Inputs:** two prices, a displayed total, binary rounding behaviour. **Outputs:** mechanism explanation + design fix. **Constraints:** keep the tool (spreadsheet); keep prices in major units for display.

**Learning objectives.** Connect L14's approximation to a real workflow; choose representation (integer cents) over luck.

**Available information.** Prices are two-decimal values; the sheet sums many rows; display rounding hides sub-cent drift until it doesn't.

**Student task.** The two-sentence explanation (approximation, not stupidity) + the design fix + how you'd verify it.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Explanation: 19.99 isn't exactly representable in binary; sums accumulate tiny errors; display rounding can mask or expose them; fix: store *integer cents* (or round at the right points per a stated rule), sum integers, format at display; verification: recompute a known batch and compare to bank totals. Honest caveat: the exact 40.00 outcome depends on the tool's rounding — the *class* of failure is the point.

**Discussion questions.**

1. Why does "just add more decimals" not fully fix it?
2. Where else in a student's life does this class of error lurk? (Currency, percentages, averages.)

**Extension challenge.** Write the one-cell formula pattern that implements integer-cent totals in any spreadsheet.

**References.** Course L14 (IEEE 754 awareness); Goldberg, D. (1991). *What Every Computer Scientist Should Know About Floating-Point Arithmetic* (advanced, optional).

---

## PB-203 · Level 2 · The lift that answers two floors at once

**Domain:** Binary and logical reasoning · **Related lectures:** L17, L18

**Scenario.** A dorm lift's call panel has a fault: pressing floor 3 *and* floor 5 lights the "door open" indicator as if floor 4 were called. Floors 4's own button works fine.

**Problem statement.** Model the panel's inputs/indicator as a Boolean function; propose the likely internal fault; describe the safe test.

**Stakeholders.** Residents (safety, annoyance); building management (repair cost); the technician (diagnosis time).

**Inputs:** button states (per floor), indicator behaviour. **Outputs:** Boolean model + fault hypothesis + test. **Constraints:** no opening the panel; observations only.

**Learning objectives.** Map a physical anomaly onto truth-table reasoning; use De Morgan-style thinking to explain "wrong operator" faults.

**Available information.** The fault appears only for the 3-and-5 pair; single presses behave; the indicator is supposed to light only on a *valid* call.

**Student task.** The truth table for "indicator should light" (per floor, three inputs: 3, 4, 5), the observed misbehaviour expressed as a changed row, and the operator-level hypothesis (e.g., an OR where an AND/XOR belongs).

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Model: indicator = "exactly one of 3,4,5 pressed" (XOR-style validity); the 3∧5 row lighting wrongly suggests OR-like leakage across wires/inputs (an OR-ed pair where exclusivity was intended); safe test: try 1-and-7 (does any *pair* trigger it, or only adjacent-ish pairs?) — the answer discriminates wiring-bleed vs logic fault.

**Discussion questions.**

1. Why is "exactly one" (XOR-family) the right validity rule rather than "at least one"?
2. What does your 1-and-7 test distinguish that 3-and-5 alone cannot?

**Extension challenge.** Sketch the gate diagram that would produce the faulty behaviour.

**References.** Course L17–L18 (truth tables, gates).

---

## PB-204 · Level 2 · The café that remembers every device

**Domain:** Networking / Cybersecurity and privacy · **Related lectures:** L21, L30

**Scenario.** A café's Wi-Fi requires re-login every visit for some customers but greets others by name instantly. The difference: newer phones randomize their Wi-Fi hardware address; older devices don't.

**Problem statement.** Explain the mechanism (device tracking via stable hardware addresses), then argue the trade-off: privacy from randomization vs the café's legitimate "remember my device" convenience.

**Stakeholders.** Customers (privacy, convenience); the café (loyalty features); the access-point vendor.

**Inputs:** two customer experiences; the randomization feature's behaviour. **Outputs:** mechanism explanation + a position with trade-offs named. **Constraints:** conceptual analysis only — no configuration changes to others' equipment.

**Learning objectives.** Link L21's link-layer identity to L30's tracking persistence; practise defending *both* sides of a trade-off.

**Available information.** Hardware addresses uniquely identify devices on a network; randomized addresses rotate (often per network); captive portals key on that address.

**Student task.** The two-paragraph analysis (mechanism; then your position) + the one design that gives the café convenience *without* permanent tracking.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Mechanism: stable address = tracker that survives cookies; position must name both goods (privacy vs convenience) — either defensible; design: per-network stable-but-not-global addresses or opt-in "remember me" tied to a login, not the hardware address; the re-identification theme (L26/L30) noted.

**Discussion questions.**

1. Why is a hardware address *stronger* persistence than a cookie — and what breaks that strength?
2. Who else, beyond the café, benefits from stable addresses on open networks?

**Extension challenge.** Draft the two-line Wi-Fi login page text that offers "remember me" honestly.

**References.** Course L21 (link layer), L30 (tracking); Wi-Fi Alliance randomized-MAC overview (instructor-provided).

---

## PB-205 · Level 2 · The image that always loads last

**Domain:** Internet and web technologies · **Related lectures:** L22, L23

**Scenario.** A news page's headline photo consistently appears two seconds after the text. A classmate blames "slow Wi-Fi"; the same photo from the same site loads instantly on another network.

**Problem statement.** Investigate the likely causes across the delivery chain (request order, caching, CDN) and design the evidence that would settle it.

**Stakeholders.** The reader; the site's operators (performance team); the CDN.

**Inputs:** symptom (order, not raw speed); cross-network difference. **Outputs:** hypothesis list + evidence plan. **Constraints:** read-only investigation (dev-tools, no attacks).

**Learning objectives.** Use L22/L23's chain (DNS, cache, CDN, render order) as a diagnostic framework; separate *order* symptoms from *speed* symptoms.

**Available information.** Text renders before images by design (progressive rendering); images often come from separate domains (CDNs); browsers cache aggressively.

**Student task.** Three ranked hypotheses + the dev-tools evidence (which panel, which column) that would discriminate.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Hypotheses: (1) image on a colder CDN edge for your region (first-byte delay), (2) render-blocking sequence — the image is lazy/lower priority by design, (3) cache state difference across networks; evidence: dev-tools Network panel — timing breakdown (waiting vs download), initiator/priority column, cache header (hit/miss); the cross-network datum mostly *rules out* the site being globally slow.

**Discussion questions.**

1. Why is "the Wi-Fi is slow" the least informative hypothesis here?
2. Which header would tell you the image was cached — and what would its absence imply?

**Extension challenge.** Screenshot-free: describe the three columns of the Network panel you'd compare, in words.

**References.** Course L22 (caching/CDN), L23 (rendering); MDN HTTP caching guide (instructor-provided).

---

## PB-206 · Level 2 · The breach email about a site you forgot

**Domain:** Cybersecurity and privacy · **Related lectures:** L29

**Scenario.** A service you used once in 2023 emails: "We had a breach; emails and passwords were exposed." You reused that password on two other accounts until last month.

**Problem statement.** Assess your real exposure, sequence the response, and decide which notifications matter.

**Stakeholders.** You (three accounts' worth of risk); the breached service (obligations); the other two services (their users).

**Inputs:** breach facts as stated; your reuse history; current MFA status per account. **Outputs:** exposure assessment + ordered response. **Constraints:** verify the breach email itself first (it could be phishing — L29 triage).

**Learning objectives.** Reason about credential-stuffing exposure timelines; sequence containment (verify → contain → monitor).

**Available information.** Password changes last month on one account; MFA on the email account only; breach-notification emails can be spoofed.

**Student task.** The exposure assessment (which account is hottest and why) + the ordered response (five steps) + one sentence on what "exposed" does *not* mean.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Hottest account: any still sharing the old password without MFA (the one changed last month is cooler); sequence: verify breach via official channel (triage the email), change reused passwords (most-exposed first), enable MFA (email first), check recovery options, watch for targeted phishing (breach lists feed attacks); "exposed ≠ used" stated — exposure creates *risk*, not certainty of compromise.

**Discussion questions.**

1. Why do breached lists make the *phishing* risk spike, not just the login risk?
2. Which is the better habit: unique passwords everywhere, or MFA everywhere — and why is the question a trap?

**Extension challenge.** Write the 3-item "new account" checklist that makes 2023-you's mistake impossible.

**References.** CISA Secure Our World; course L29.

---

## PB-207 · Level 2 · The membership sheet that can't answer simple questions

**Domain:** Database and information organization · **Related lectures:** L25

**Scenario.** A society's spreadsheet has one giant sheet: member names, event attendance (as tick marks in month-columns), and fees paid (as notes). Answering "who owes fees and attended nothing since October?" takes an hour.

**Problem statement.** Redesign the data into tables that make such questions answerable in minutes, and write the question as a query-shaped sentence.

**Stakeholders.** Committee members (admin time); members (accurate fee status); next year's committee (inheritance).

**Inputs:** the current one-sheet design; three example questions the committee needs. **Outputs:** table design + one query-shaped sentence + migration order. **Constraints:** no database server required (spreadsheets acceptable if relational-shaped).

**Learning objectives.** Apply L25's relational thinking: entities, keys, one fact per table; translate questions into query shapes.

**Available information.** Members have stable IDs; attendance events are dated; fees are per-term.

**Student task.** The table design (two-three tables with keys), the example question as `SELECT…WHERE` pseudocode, and the migration order that keeps the club running.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Design: MEMBERS (id, name, join date), ATTENDANCE (member_id, event_id/date), FEES (member_id, term, paid-date) — facts separated, IDs as anchors; query: SELECT name FROM members JOIN fees WHERE term='Autumn' AND paid IS NULL AND id NOT IN (attendees since October); migration: freeze old sheet → export members first (the anchor entity) → backfill events → verify counts before retiring the old sheet.

**Discussion questions.**

1. What makes the tick-mark columns unable to answer the question — express it in L25 terms.
2. Which table would you migrate first, and what breaks if you start elsewhere?

**Extension challenge.** Add the constraint sentence that prevents "fees paid with no member ID" ever entering the system.

**References.** Course L25 (relational model); Bourgeois ch. 4 (course reference).

---

## PB-208 · Level 2 · The free-tier cloud scare

**Domain:** Cloud computing · **Related lectures:** L24, L07 (Lab 7 adjacent)

**Scenario.** A student leaves a lab VM running over a two-week break. The "free tier" shows a balance due — a small amount, but real. The dashboard lists: one running VM, one extra disk, one forgotten snapshot.

**Problem statement.** Triage the costs, clean up completely, and design the two-habit guard that makes this impossible next time.

**Stakeholders.** The student (money, confidence); the provider (billing correctness); the course (its cloud policy).

**Inputs:** the three resources; free-tier rules; the break's dates. **Outputs:** triage + teardown checklist + guard habits. **Constraints:** no dispute without evidence; everything eventually deleted.

**Learning objectives.** Map L24's "measured service" onto real billing line-items; design guards (alerts, teardown checklists).

**Available information.** Free tiers usually cover *small* instances for limited hours; disks and snapshots bill separately; billing alerts exist.

**Student task.** Which of the three items likely incurred cost and why + the teardown checklist + the two habits.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Triage: the VM (hours beyond free allowance) and the snapshot/disk (storage bills even when idle) are the suspects; teardown: stop → snapshot-data-decision → delete instance → delete disk → delete snapshot → verify console empty + billing page zero-estimate; habits: budget/billing alert at a low threshold, teardown screenshot ritual (Lab 7's culture); the "measured service means *what* is measured" insight explicit.

**Discussion questions.**

1. Why does a *stopped* instance sometimes still cost money — which resource class is that?
2. Which of your two guards would have caught this at day 2 rather than week 2?

**Extension challenge.** Write the 4-line teardown checklist card for next year's lab handout.

**References.** Course L24 (service models, measured use); provider free-tier docs (instructor-provided).

---

## PB-209 · Level 2 · The attendance chart that shamed the wrong group

**Domain:** Data science workflows · **Related lectures:** L19, L26

**Scenario.** A class rep charts "attendance by department" to argue for better scheduling. One department shows 40% — but its numbers include evening students whose sessions were rescheduled and never marked.

**Problem statement.** Diagnose what the chart hides, redesign it honestly, and draft the caption that prevents misreading.

**Stakeholders.** The shamed department's students; the class rep (good intent); the scheduling committee (decision-makers).

**Inputs:** the aggregated chart; the rescheduling fact; the raw attendance possibility. **Outputs:** diagnosis + redesign + caption. **Constraints:** no new data collection needed (the marking record exists).

**Learning objectives.** Apply L26's aggregation ethics and L19's chart craft; write captions that carry the caveat.

**Available information.** Session-level records exist (who was marked, when, where); evening sessions' rescheduling is documented; percentages hide denominators.

**Student task.** The diagnosis (what aggregation destroyed) + the redesigned chart's spec + the one-sentence caption.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Diagnosis: mixing populations with different session counts into one percentage (Simpson's-adjacent effect, concept-level); redesign: per-cohort attendance or a small-multiples breakdown, denominators shown; caption: "Excluding rescheduled evening sessions pending re-marking; see note"; the *honest chart is a design deliverable* framing from L19/L26.

**Discussion questions.**

1. What would you do if the corrected chart *still* showed 40% — does the caveat matter then?
2. Why is "the data is technically true" the weakest defence of a misleading chart?

**Extension challenge.** Write the two-sentence message to the shamed department that shares the correction.

**References.** Course L19 (charts), L26 (aggregation ethics).

---

## PB-210 · Level 2 · The chatbot's confident citation to nowhere

**Domain:** AI literacy · **Related lectures:** L23, L27, L28

**Scenario.** An AI tool answers a course question with three sources — one real, one real-but-misattributed, one that does not exist. All three look equally confident.

**Problem statement.** Design a verification workflow for AI-assisted study notes that a busy first-year would actually follow.

**Stakeholders.** The student (grades, integrity); the course (standards); the tool's vendor (claims).

**Inputs:** the mixed-citation outcome; L28's checklist; exam pressure. **Outputs:** a lightweight workflow + the disclosure line. **Constraints:** workflow must fit in minutes, not hours.

**Learning objectives.** Operationalize L28's verification (per-claim, named source); design for adoption, not perfection.

**Available information.** Course pages and the official textbook exist as ground truth; the tool cites without links; the rubric grades disclosure.

**Student task.** The four-step workflow (with time budget) + which claim class to verify *first* and why + the one-line disclosure.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Workflow: (1) list claims, (2) verify numbers/dates/citations first (fastest to falsify), (3) mark unverifiable as such, (4) write the disclosure (tool, role, verified, changed); citations-first because a fake citation poisons trust in everything else; workflow sized to ~5 minutes per page — adoptability named as a design constraint.

**Discussion questions.**

1. Why verify citations before explanations — what does a fake citation do to the reader's trust budget?
2. Which step would students skip first under deadline pressure, and how does your design survive that?

**Extension challenge.** Turn your workflow into a 3-row checklist table others can paste into their notes.

**References.** Course L28 (verification loop), L23 (criteria); NIST AI RMF (course reference).

---

## PB-211 · Level 2 · Forty slides for a five-minute talk

**Domain:** Digital productivity · **Related lectures:** L20

**Scenario.** A society's treasurer prepares 40 slides for a 5-minute budget report: every transaction has a slide. The audience will see 6 seconds per slide.

**Problem statement.** Redesign the deck to serve the talk's *purpose* (decision: approve the budget), and decide what happens to the 34 cut slides.

**Stakeholders.** The treasurer; the audience (voters); the audit trail (finance records).

**Inputs:** the transaction list; the decision needed; L20's principles. **Outputs:** deck design (slide count, per-slide message) + appendix plan. **Constraints:** the numbers must remain auditable *somewhere*.

**Learning objectives.** Design decks top-down from the decision; separate presentation layer from record layer.

**Available information.** Three budget lines matter for the decision (income, big spends, reserve); the full ledger exists in the spreadsheet; questions will come after.

**Student task.** The new deck's outline (≤6 slides, one message each) + where the 34 slides' content goes + the one chart that earns its place.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Outline: title→income→three biggest spends→reserve status→the ask→Q&A; the full ledger moves to a linked appendix/backup deck (record layer preserved — auditability named); the one chart: income-vs-spend bar or reserve trend, honest axes; the "slides support the speaker" thesis applied to *purpose*, not just aesthetics.

**Discussion questions.**

1. What is the talk's single decision, and which slide carries it?
2. Why is deleting content different from *demoting* it to an appendix?

**Extension challenge.** Write the 25-word speaker script for your "ask" slide.

**References.** Course L20 (principles, hierarchy).

---

## PB-212 · Level 2 · The laptop that's fast in the shop, slow in the library

**Domain:** Hardware troubleshooting · **Related lectures:** L06, L07; Lab 2 adjacent

**Scenario.** A new laptop benchmarks well at purchase but feels sluggish in the warm library during long compile sessions. The spec sheet mentions neither temperature nor sustained load.

**Problem statement.** Design a fair comparison test (shop conditions vs library conditions) and the likely mechanism, using only free tools.

**Stakeholders.** The student (purchase regret, coursework); the vendor (spec honesty); other buyers.

**Inputs:** two environments; workload (long CPU-heavy sessions); no special software. **Outputs:** fair-test design + mechanism hypothesis + a buying lesson. **Constraints:** no hardware modification; readings must be repeatable.

**Learning objectives.** Apply Lab 2's fair-test discipline to a thermal hypothesis; read specs for *sustained* vs *peak* performance.

**Available information.** CPUs throttle when hot; libraries are warm and fan airflow differs; free monitoring tools show clock speeds and temperatures.

**Student task.** The test design (variables, conditions, measurements) + the mechanism hypothesis + the one spec question to ask next time.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Test: same workload, same battery/AC state, two environments, measure clock speed + temperature over 20 minutes (multiple runs, notes on background load); mechanism: thermal throttling — sustained clocks drop as temperature limits hit; buying lesson: ask for sustained-load reviews/cooling design, not peak benchmarks; the Lab 2 honesty rule (anomalies reported) carries over.

**Discussion questions.**

1. Which variable is hardest to hold constant between the two environments — and how do you record it?
2. Why do peak benchmark numbers survive as the marketing default?

**Extension challenge.** Write the 4-row results table with the columns that make the comparison fair.

**References.** Course L06 (clocks), Lab 2 (fair tests); vendor thermal documentation (instructor-provided).

---

## PB-213 · Level 2 · The backup that had never been asked to work

**Domain:** File and backup management · **Related lectures:** L11; Lab 8 adjacent

**Scenario.** A student's 3-2-1 plan looked perfect on paper: cloud sync, external drive, university storage. Then the external drive failed — and the restore to *it* had never been tested. Worse: the "backup" was a sync job that had faithfully propagated a deleted folder months ago.

**Problem statement.** Audit the plan's failure modes, distinguish sync from backup, and redesign with a test cadence.

**Stakeholders.** The student; the coursework; the university storage admins (quotas).

**Inputs:** the plan's components; the deletion-propagation event; one failed drive. **Outputs:** failure-mode audit + redesign + test cadence. **Constraints:** zero budget; minimal manual effort.

**Learning objectives.** Separate sync semantics from backup semantics (L24 at personal scale); design *testable* backups.

**Available information.** Cloud services keep ~30-day version histories; university storage offers scheduled snapshots; the external drive is replaceable.

**Student task.** The failure-mode table (component → its failure mode) + the redesign + the test cadence with dates.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Failure modes: sync propagates deletions (not a backup), untested drive = hypothesis, single-physical-location copies die together; redesign: versioned cloud snapshots (30-day window) as one copy, external drive as scheduled one-way backup (not sync), university storage as offsite; cadence: quarterly test-restore of one file per component, calendar-anchored; the "a backup is a restore that has already worked" principle stated.

**Discussion questions.**

1. Why does the deletion-propagation failure hide until you need the file *back*?
2. Which component of your redesign survives a ransomware-style encryption event — and which doesn't?

**Extension challenge.** Write the calendar-invitation text for your quarterly restore test.

**References.** Course L11 (3-2-1), L24 (sync semantics).

---

## PB-214 · Level 2 · The CAPTCHA that locked out the student it was protecting

**Domain:** Accessibility and inclusive computing · **Related lectures:** L20, L30

**Scenario.** A course's registration form uses an image-distortion CAPTCHA. A visually impaired student cannot pass it; the alternative (phone verification) runs only in office hours — while she is in class.

**Problem statement.** Diagnose the accessibility failure, propose fixes at three levels (form, process, policy), and name the trade-off each makes.

**Stakeholders.** The student (access); the university (bot defence, compliance); other users (friction).

**Inputs:** the CAPTCHA type; the alternative's availability window; accessibility standards. **Outputs:** three-level fixes + trade-offs. **Constraints:** bots remain a real threat — the defence cannot simply vanish.

**Learning objectives.** Reason about accessibility vs security as a *design* tension, not a slogan; propose proportionate alternatives.

**Available information.** Accessibility standards require alternatives to visual challenges; modern bot defence uses behavioural/invisible checks; the phone line's hours are a policy choice.

**Student task.** The three-level fix list, each with its trade-off + which level you'd prioritize and why.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Form level: audio alternative / modern invisible checks (trade-off: weaker bot signal); process level: asynchronous verification (email/code with deadline) (trade-off: slightly slower onboarding); policy level: extend phone hours or route to the accessibility office (trade-off: staffing); prioritize process level — it helps *everyone*, not only this student; WCAG's "alternatives" principle named.

**Discussion questions.**

1. Why is "add an audio CAPTCHA" not automatically the full answer?
2. Which stakeholder's needs are invisible in the current design — and how does your priority fix that?

**Extension challenge.** Draft the two-sentence change request to the course administrator.

**References.** WCAG 2.1 (course references); course L20 (accessibility as habit).

---

## PB-215 · Level 2 · The computer lab that runs all night

**Domain:** Sustainability and energy efficiency · **Related lectures:** L03, L10

**Scenario.** A 40-machine lab stays fully powered overnight "for updates and because switching is annoying." Machines idle at login screens; one is left with a broken fan running for weeks.

**Problem statement.** Design the power-management proposal: what to automate, what to schedule, and how to answer the security/energy trade-off.

**Stakeholders.** The university (energy bills, sustainability targets); lab users (morning availability); IT (update windows); the broken-fan machine (fire risk).

**Inputs:** lab size, usage pattern (empty nights), update needs. **Outputs:** proposal with schedule + the trade-off analysis + the anomaly report. **Constraints:** morning availability must not degrade; updates still happen.

**Learning objectives.** Apply trade-off reasoning to an operational policy; connect hardware state to energy and risk.

**Available information.** Wake-on-LAN exists; updates can run in a scheduled window; usage logs show near-zero night use.

**Student task.** The proposal (three automated behaviours + schedule) + the trade-off sentence for each + what to do about the broken-fan machine.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Proposal: sleep after X minutes idle (not shutdown — Wake-on-LAN preserved), updates in a 02:00–04:00 window with wake, monthly power-state audit; trade-offs: sleep still draws standby power vs instant morning readiness; update window vs unpredictable patches; anomaly: the broken-fan machine is a *safety* report, not an energy line-item — escalate immediately; measurement suggestion (meter before/after) to keep the proposal honest.

**Discussion questions.**

1. Which stakeholder loses the most under your proposal, and why accept that?
2. Why is the broken fan a different *category* of finding than the energy waste?

**Extension challenge.** Compute (order-of-magnitude, stated assumptions) the annual kWh saved by sleeping 40 machines for 8 hours nightly.

**References.** Course L03 (scale), L10 (power states); ENERGY STAR computer guidance (instructor-provided).

---

## PB-216 · Level 2 · The clinic's appointment sheet (conceptual)

**Domain:** Healthcare information systems (conceptual) · **Related lectures:** L25, L26, L30

**Scenario.** A small fictional clinic tracks appointments in one shared spreadsheet printed daily at reception. Two receptionists edit different copies; a patient once arrived on the wrong day; the sheet shows full names and phone numbers beside reasons for visit.

**Problem statement.** Identify the information-management risks (integrity, privacy), and sketch the minimal redesign that a two-desk clinic could adopt.

**Stakeholders.** Patients (privacy, correct appointments); receptionists (workflow); the clinic owner (compliance, reputation).

**Inputs:** the workflow; the error event; the printed-copy habit. **Outputs:** risk list + minimal redesign. **Constraints:** conceptual only — no real data, no assumption of budget for new systems; changes must survive a power cut and a non-technical staff.

**Learning objectives.** Apply L25/L26/L30 concepts to a *small-practice* scale; resist enterprise answers where a two-desk fix fits.

**Available information.** Two editing desks; one shared drive exists; printers at both desks; staff comfortable with a spreadsheet.

**Student task.** The risk list (three, ranked) + the minimal redesign (what changes, what stays paper) + the one rule that prevents the two-copies problem.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Risks: conflicting copies (integrity), personal data on unattended printouts (privacy), no audit trail; redesign: single shared file *on the drive* (one authority), printouts show time+initials only (minimization), evening printout shredded; keep paper for the day-list (adoptability); rule: "the drive copy is the only live one — print is a snapshot"; explicitly note what a real clinic would need beyond this scope (compliance regimes, audit systems) — boundary awareness.

**Discussion questions.**

1. Which risk would you fix first if you could change only *one* thing — and why that one?
2. What does this scenario share with PB-115's club problem, and where does it differ *categorically*? (Privacy stakes.)

**Extension challenge.** Write the one-page "clinic data rules" poster for the staff room.

**References.** Course L25 (integrity), L30 (minimization); fictional scenario — no real clinic data involved.

---

## PB-217 · Level 2 · The LMS quiz with the wrong answer key

**Domain:** Education technology · **Related lectures:** L10, L20; Course policy adjacent

**Scenario.** An auto-graded LMS quiz marked six students wrong because the key itself had an error. The instructor regrades, but students want to know how it was prevented — and one student's appeal arrives citing a screenshot of the correct answer *during* the quiz window.

**Problem statement.** Separate the three issues (systemic prevention, fair regrade, the integrity question) and propose the process for each.

**Stakeholders.** The six students; the instructor; the course's integrity policy; future cohorts.

**Inputs:** the key error; the regrade; the appeal with screenshot. **Outputs:** three-part process proposal. **Constraints:** decisions must be explainable to all parties; policy exists — apply it, don't invent.

**Learning objectives.** Decompose a messy incident into separable problems; apply stated policy rather than ad-hoc judgement.

**Available information.** The course syllabus defines integrity procedure; LMS logs timestamps; the key error is confirmed.

**Student task.** The three issues as separate paragraphs + the prevention suggestion (one change) + how the screenshot appeal should be *processed* (not prejudged).

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Prevention: key-validation step (a second reader or a canary question) — process, not blame; regrade: automatic + communicated (it's a *system* error, students did nothing wrong); appeal: follow the syllabus procedure — timestamps and logs examined, presumption of good faith until evidence otherwise; the meta-lesson: messy incidents decompose (L31), and each sub-problem gets its own stakeholder-aware answer.

**Discussion questions.**

1. Why should the appeal be processed by *procedure* rather than by the instructor's instinct?
2. Which of the three issues would you fix first for next term, and why is it not the appeal?

**Extension challenge.** Draft the announcement to the six students that is honest without over-apologizing.

**References.** Course syllabus integrity section; L31 (decomposition).

---

## PB-218 · Level 2 · The city form that only exists on paper

**Domain:** Public service systems · **Related lectures:** L04, L30

**Scenario.** A city service requires a paper form, in person, 9-to-4 — while the city's own app offers eight *other* services digitally. Residents without daytime availability or with mobility limits queue; the office cites "system integration cost."

**Problem statement.** Build the case for digitizing this one service: benefits, risks, who might be *harmed* by digitization, and the phased plan.

**Stakeholders.** Residents (diverse: workers, caregivers, disabled, offline); office staff; the city (cost, equity commitments).

**Inputs:** the service's paper process; the existing app platform; the queue reality. **Outputs:** benefits/risks analysis + phased plan + the offline-preservation decision. **Constraints:** some residents must never be excluded — design for them explicitly.

**Learning objectives.** Apply L04's divide framework to a service-design case; weigh efficiency against exclusion.

**Available information.** The form's fields are simple (address change); the app platform supports forms; the office has digitalskills gaps; an assist desk exists two days a week.

**Student task.** The benefit/-risk table (name who bears each risk) + the three-phase plan + the sentence that keeps paper alive deliberately.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Benefits: access for time-poor/mobility-limited; lower queue costs; risks: digital-exclusion of offline residents, staff displacement fear, integration cost realism; plan: phase 1 pilot with assist-desk integration, phase 2 full digital with paper coexistence, phase 3 review with usage data *by demographic*; the deliberate paper-preservation sentence ("paper remains for anyone, indefinitely" or a sunset criterion — either defensible, named); harm-naming (elderly/offline residents) is the ethical core.

**Discussion questions.**

1. Whose interests are served by "integration cost" as the stated blocker — and how would you test that claim?
2. What data would tell you whether digitization *widened* access rather than just moved the queue?

**Extension challenge.** Write the 100-word council-brief pitch for phase 1.

**References.** Course L04 (divide dimensions); fictional/generalized city scenario.

---

## PB-219 · Level 2 · The bakery's five dead laptops in three years

**Domain:** Small business ICT · **Related lectures:** L08, L11

**Scenario.** A bakery's till-and-bookkeeping laptop fails about every seven months: flour dust, heat by the ovens, drops. Each replacement repeats the pattern; the owner keeps buying cheap consumer machines; customer records live only on each dying laptop.

**Problem statement.** Break the replace-on-death cycle: environment analysis, requirements-first purchase or arrangement, and the data-survival plan.

**Stakeholders.** The owner (money, continuity); customers (their records); staff (workflow).

**Inputs:** failure history; environment (dust, heat, drops); data location. **Outputs:** environment fixes + purchase/arrangement decision + data plan. **Constraints:** small-business budget; no IT staff.

**Learning objectives.** Requirements-first hardware reasoning (L08) under environmental constraints; decouple data from devices (L11).

**Available information.** Failures cluster near the ovens (heat) and the flour shelf (dust); a back-office nook exists; cloud accounting costs little monthly.

**Student task.** Environment fixes (two) + the hardware decision (what to buy or rearrange, justified) + the data-survival plan.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Environment: relocate the workstation to the back-office nook (heat/dust away), sealed keyboard cover/wipe routine; hardware: a business-class small machine or a fanless/sealed device justified by *environment* not brand — or tablet+stand at the till; data: cloud accounting (offsite by design) + weekly export; the "stop buying the same failure" insight made explicit as requirements-first thinking.

**Discussion questions.**

1. Which is cheaper over three years: the environment fix or a fourth laptop — and what does your estimate assume?
2. Why does "buy a better laptop" alone leave the *data* risk untouched?

**Extension challenge.** Draft the one-paragraph pitch to the owner with your three-line plan and its cost.

**References.** Course L08 (requirements), L11 (backups); generalized small-business scenario.

---

## PB-220 · Level 2 · The results-release email storm

**Domain:** University administration / Networking · **Related lectures:** L22, L23, L30

**Scenario.** Results day: 8,000 students hit the portal at 09:00. The portal slows to a crawl; the IT office also emails every student their grade summary — and 200 emails bounce because students changed addresses without updating records.

**Problem statement.** Diagnose the load problem (why simultaneous access hurts), evaluate the email-storm design, and propose the release plan for next term.

**Stakeholders.** Students (anxiety, access); IT (load, bounces); the registry (accuracy, privacy).

**Inputs:** the 09:00 spike; the email-attachment design; the bounce count. **Outputs:** mechanism explanation + release redesign. **Constraints:** results must remain private per-student; no new infrastructure assumed.

**Learning objectives.** Connect L22's bursty-load reasoning to operational design; apply L30 minimization to bulk email.

**Available information.** The portal can handle steady load but not the synchronized spike; grades are also visible in the portal per-student; the email contains full summaries as attachments.

**Student task.** The load explanation (why simultaneity, not volume, kills it) + the redesign (two changes) + the email design's privacy critique.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Mechanism: synchronized demand exceeds burst capacity — the spike is a coordination artifact, not a capacity problem; redesign: staggered release windows by faculty (or queue page), status-page communication to reduce retry storms; email critique: attachments with full summaries sit in inboxes forever (L30 minimization — a link to the authenticated portal beats a payload), bounce list signals stale records as a data-quality issue (L25 adjacent).

**Discussion questions.**

1. Why does staggering by faculty work when "just add servers" may not — name the cost trade-off of each?
2. Which L30 principle does the email redesign apply, exactly?

**Extension challenge.** Draft the status-page banner text for results morning.

**References.** Course L22 (packet/load bursts), L30 (minimization); generalized institutional scenario.

---

## PB-221 · Level 2 · Five family members, one administrator account

**Domain:** Operating systems / Cybersecurity · **Related lectures:** L10, L12, L29

**Scenario.** A family PC runs everyone as administrator "because installing games needs it." A teenager's game mod infected the machine; recovery took a weekend; the parents' tax files were on the same account.

**Problem statement.** Design the account structure and habits that would have contained the infection, and explain the containment mechanism.

**Stakeholders.** Parents (financial data); teenager (games, autonomy); the machine (shared resource).

**Inputs:** single-admin pattern; the mod-infection event; mixed data sensitivity. **Outputs:** account design + habit changes + containment explanation. **Constraints:** family peace — the design must not feel punitive; software installs still possible.

**Learning objectives.** Apply least privilege and user separation (L10/L29) in a domestic setting; explain *why* separation contains damage.

**Available information.** OSes support standard users with per-app elevation prompts; documents can live per-user; the tax files need one owner.

**Student task.** The account design (who gets what) + the two habit changes + the containment explanation in three sentences.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Design: standard accounts for daily use, one admin account for deliberate installs, per-user documents, tax files on the parent account with backup (L11); habits: elevation prompts read before approval, installs only from the admin account with intent; containment: malware under a standard user touches that user's files and needs *another* approval to escalate — blast radius shrinks; the "least privilege without punishment" framing keeps family peace.

**Discussion questions.**

1. What exactly did the admin-everything design let the infection reach that it otherwise couldn't?
2. Which habit change is hardest to keep — and what makes it stick?

**Extension challenge.** Write the 15-minute "family PC reset" checklist (accounts, folders, backups).

**References.** Course L10 (user management), L29 (least privilege).

---

## PB-222 · Level 2 · The poster QR code that scans from paper but not from the projector

**Domain:** Data representation · **Related lectures:** L13, L16

**Scenario.** A society's poster QR code scans from the printed flyer but fails on the projected slide: too small, low contrast, and the projector's blur eats the fine squares.

**Problem statement.** Explain why the same code behaves differently across media, and design the display rules that make slide QRs reliable.

**Stakeholders.** Society members (can't join); the presenter (embarrassment); the venue (projection quality).

**Inputs:** two media; the failure pattern (size, contrast, blur). **Outputs:** mechanism explanation + display rules. **Constraints:** the destination URL is fixed; no re-branding.

**Learning objectives.** Connect L13/L16 ideas (discrete symbols, sampling, contrast) to a real encoding's robustness limits.

**Available information.** QR codes tolerate some damage via redundancy but need minimum module size and contrast; projection adds blur and colour shift; phones vary in camera focus.

**Student task.** The mechanism explanation (sampling the projection vs the print) + three display rules + the on-slide fallback that saves every talk.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Mechanism: the camera *samples* the projected image; blur + small modules + weak contrast push the sampling below the code's tolerance — the print's ink edges carry more signal; rules: minimum on-screen size (e.g., at least a tenth of slide width), dark-on-light or light-on-dark with strong contrast, no animation/neighbour clutter, test from the room's back row; fallback: a short human-typable URL beside the code (redundancy at the *information* level — the deepest lesson).

**Discussion questions.**

1. Where does redundancy appear in your fallback, and where in the QR itself?
2. Why does "it worked on my laptop screen" prove nothing about the hall?

**Extension challenge.** Write the one-line poster guideline for all society slides next year.

**References.** Course L13 (discrete symbols), L16 (sampling); QR error-correction overview (instructor-provided).

---

## PB-223 · Level 2 · The dorm door that needs three of five conditions

**Domain:** Binary and logical reasoning · **Related lectures:** L17

**Scenario.** A lab door unlocks when: card valid AND (PIN entered OR supervisor present) AND NOT maintenance-lockout. One Friday, maintenance-lockout is on, but the supervisor's "present" flag stuck on from Thursday.

**Problem statement.** Express the access rule as a Boolean expression; evaluate Friday's states; decide whether the door *should* open and what the stuck flag teaches about flag hygiene.

**Stakeholders.** Lab users (access); security (the rule's purpose); maintenance (their lockout right).

**Inputs:** the rule; the Friday state (card valid, PIN unknown, supervisor-stuck, lockout on). **Outputs:** expression + evaluation + hygiene lesson. **Constraints:** safety first — if the expression says open, challenge it.

**Learning objectives.** Translate a policy into Boolean algebra (L17); evaluate systematically; reason about stale state.

**Available information.** The rule as stated; the Friday state (card valid, PIN unknown, supervisor-stuck, lockout on); nothing about the door controller's internal wiring — the model must work from the policy, not the hardware.

**Student task.** The expression, the truth evaluation for Friday, the verdict (and whether you'd trust the door), plus the flag-hygiene rule.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Expression: UNLOCK = VALID ∧ (PIN ∨ SUPervisor) ∧ ¬LOCKOUT; Friday: lockout forces ¬UNLOCK regardless of the stuck flag — the door *should not* open (lockout's design intent wins); hygiene: flags need expiry/heartbeat (a "present" flag must be re-asserted), because stale state silently rewrites policy; the verification habit: evaluate the expression *before* trusting any door.

**Discussion questions.**

1. Which operator in the expression makes lockout absolute — and would AND-placement anywhere else change that?
2. What other systems do you use daily that trust stale flags?

**Extension challenge.** Rewrite the rule adding a "supervisor override requires card AND presence" clause — and show the new expression.

**References.** Course L17 (Boolean expressions, De Morgan adjacent).

---

## PB-224 · Level 2 · The short link that rotted before graduation

**Domain:** Internet and web technologies · **Related lectures:** L23

**Scenario.** A student society printed 500 flyers with a URL-shortener link. The shortener service shut down; the flyers now lead nowhere. The society's own website was perfectly capable of hosting a redirect.

**Problem statement.** Analyze why the link died (dependency on a third party's persistence), design the durable-link policy, and decide what to do with the flyers.

**Stakeholders.** Society members (recruitment); the university (its URLs persist); future flyer-printers.

**Inputs:** the dead shortener; the society's own domain; the flyer stock. **Outputs:** dependency analysis + policy + flyer remediation. **Constraints:** budget zero; the URL's *stability* is the asset.

**Learning objectives.** Reason about dependencies and link rot (L23's web as mutable infrastructure); design persistence policies.

**Available information.** The university hosts society pages on a long-lived domain; redirects are trivial to create; QR codes can encode any URL.

**Student task.** The dependency analysis (which party's survival the flyer bet on) + the durable-link policy (three rules) + the cheapest flyer remediation.

**Suggested thinking time.** 12 minutes.

**Expected solution characteristics.** Analysis: the shortener was a single point of failure outside institutional control — the flyer's *real* dependency should have been the society's own persistent domain; policy: own-domain URLs only, stable paths (`/join`), redirects change *targets*, never the printed link; remediation: create `/flyer2026` on the own domain → redirect wherever needed (print stocks stay valid); the "printed links are permanent promises" principle stated.

**Discussion questions.**

1. What was the shortener giving you that your own domain couldn't — and was it worth the dependency?
2. Which is more durable: the domain or the *path convention*? Design so you never have to choose.

**Extension challenge.** Write the society's "link policy" card (three lines) for next year's publicity officer.

**References.** Course L23 (URLs, web persistence); link-rot literature (instructor-provided).

---

## PB-225 · Level 2 · The AI-generated study guide that half the class used

**Domain:** AI literacy / Digital citizenship · **Related lectures:** L27, L28

**Scenario.** Before the quiz, one student generates a study guide with an AI tool and shares it in the class group. It contains two subtle errors. Half the class studies from it; the quiz asks about one of the errors. The author says: "I just made it in five minutes, obviously check it."

**Problem statement.** Separate the questions — the author's responsibility, the class's verification norms, the quiz fairness — and propose the group's standing rule.

**Stakeholders.** The author (intent vs impact); the quiz-takers (grades); the instructor (assessment integrity); the course's AI policy.

**Inputs:** the error propagation; the sharing act; the policy's disclosure rules. **Outputs:** three-part analysis + a standing group rule. **Constraints:** policy applies to *submitted* work — sharing is a grey zone the group must norm themselves.

**Learning objectives.** Apply L28's verification and disclosure thinking to *informal* sharing; design citizenship norms for AI content.

**Available information.** The course policy governs submissions; the group chat has no norms; the affected quiz question is identified.

**Student task.** The three-part analysis (author/class/fairness) + the standing rule (two sentences) + what you'd post in the group the day this happens.

**Suggested thinking time.** 15 minutes.

**Expected solution characteristics.** Author: five-minute effort is a *choice* — sharing unverified AI content at scale carries responsibility even without malice; class: consuming unverified content is also a choice — verification norms (L28's loop) apply to shared notes, not just submissions; fairness: one affected question is a quiz-integrity issue for the *instructor's* process (PB-217 pattern — separate issue, own procedure); rule: "AI-shared content is labelled + verified or marked unverified — and never the night before"; the day-of post: own the error, correct it, link the lecture page.

**Discussion questions.**

1. Why does "obviously check it" not transfer the responsibility fully — and when *would* a disclaimer help?
2. Where's the line between a study group's informal help and an unvetted publication?

**Extension challenge.** Draft the group-chat "AI content norm" — three lines everyone would actually follow.

**References.** Course L28 (verification, disclosure), L30 (citizenship); course AI policy (syllabus).
