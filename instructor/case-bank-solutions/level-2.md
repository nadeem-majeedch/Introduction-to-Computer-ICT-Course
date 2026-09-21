# Case Bank — Instructor Solutions: Level 2 (PB-201–225)

**Private.** Never publish, never paste into `docs/`. Each case: solution guide, defensible alternatives, trade-offs, common mistakes. Pair with the public *Expected solution characteristics* in `docs/case-bank/level-2.md`.

---

## PB-201 — The update loop that ate the workday

**Solution guide.** The loop has two failing states and the student is making a third: (a) the update cannot complete — the available-information row points to disk-space starvation (updates need workspace to download, extract, and stage); (b) the rollback at boot marks it uninstalled, so the scheduler retries — the loop is *systematic*, not random. Recovery order: protect work first (copy critical files out — cheap insurance before any repair), free space (move media to external/cloud, empty caches), then run the update deliberately on AC power with uninterrupted time, then verify (update history shows success; reboot cleanly once more). Wall-switching is worse in a specific way: it skips the OS's safety writes at shutdown, so the rollback state itself becomes unreliable — the machine can end in a state neither "updated" nor "cleanly rolled back", which is how update loops turn into recovery-mode visits. Prevention: a scheduled update window (L12's deliberate patching) so the loop never gets a toehold.
**Alternatives.** Escalating to a support forum/vendor tool after the free-space fix is defensible if the loop persists (the diagnosis then needs the error code, which is why the extension asks for a help-desk script with a measurement step).
**Trade-offs.** Time spent diagnosing properly vs the exam-week pressure that produced the wall-switch habit; deferral (waiting for a quieter week) vs the security cost of an unpatched machine.
**Common mistakes.** Fixing the symptom by disabling updates (over-correction that leaves the machine exposed); backing up *after* attempting repair; treating the rollback as a bug rather than the system protecting itself; no verification step (declaring victory when the boot is quiet once).

---

## PB-202 — Why does 19.99 + 19.99 come to 40.00?

**Solution guide.** Mechanism, honestly bounded: 19.99 is not exactly representable in binary floating point (only sums of powers of two are), so the stored values are *approximations* a whisker off; sums of many approximations accumulate; and display rounding can either mask the drift (most rows) or expose it (some combinations) — whether *this* sheet produces exactly 40.00 depends on the tool's rounding mode, and a good answer says so rather than overclaiming the specific arithmetic. The fix is representation, not precision theatre: store money as *integer cents* (or apply a stated rounding rule at defined points), sum integers exactly, format for display only. Verification: recompute a batch whose correct total is independently known (bank statement, till roll) and compare.
**Alternatives.** Higher-precision decimal types (real, but a spreadsheet's default is float — the *discipline* of integer cents is the transferable lesson); leaving it and accepting ±1 cent drift (defensible for a café, not for an exam answer — say the tolerance explicitly).
**Trade-offs.** Integer-cents discipline costs formula hygiene (every entry ×100) vs exact totals; the "just add decimals" fix costs nothing and fixes nothing (the approximation happens at *storage*, not display).
**Common mistakes.** Blaming the spreadsheet ("computers can't add") instead of the representation; repeating the cousin's anecdote as fact; fixing display without fixing storage; not verifying the fix against a known-good total.

---

## PB-203 — The lift that answers two floors at once

**Solution guide.** Model first: with three inputs (buttons 3, 4, 5), "indicator should light" = *exactly one* pressed (XOR-family validity) — "at least one" (OR) would light the indicator for a double-press, which is precisely the misbehaviour observed. Truth table: eight rows; the faulty panel lights the 3∧5 row that validity says must be dark. Hypothesis: the pair's inputs are being OR-ed somewhere an exclusivity check was intended — wiring bleed (signal from one button leaking onto the other's line) and a wrong-gate fault are both consistent; the discriminative test is 1-and-7: if *any* pressed pair lights the indicator, the fault is in the OR-ing logic path; if only the 3-and-5 pair does, it's physical bleed specific to those wires. Safe test discipline: observations only, no panel opening — the case's constraint exists because mains-voltage lift panels are not student territory.
**Alternatives.** Either input polarity convention works if declared (pressed = 1 is the natural one); modelling only floors 3–5 (rather than the whole panel) is the right scope — say why.
**Trade-offs.** Model simplicity (3 inputs) vs completeness (the panel has more floors) — the teaching point is the method, and good answers name what they left out.
**Common mistakes.** Writing only the all-true row and calling it a truth table; forgetting the 000 row (which is where the fault-sensor reasoning lives); concluding "the button is broken" without explaining why *pairs* matter; proposing invasive testing despite the constraint.

---

## PB-204 — The café that remembers every device

**Solution guide.** Mechanism: the captive portal keys "remember me" on the Wi-Fi hardware (MAC) address; older phones present a stable one, newer phones randomize per network, so the café's system sees each visit of a modern phone as a *new device*. The address is a stronger tracker than a cookie — it survives cookie clearing and browser changes — which is exactly why platforms added randomization. Both goods are real and should be named: the café's greeting is genuine convenience; persistent hardware-address tracking across visits (and across *other* networks' datasets) is genuine surveillance capability. A defensible position either way — the marks are in the trade-off being argued, not the verdict. The design that reconciles: make "remember me" *opt-in and login-tied* — an account or one-time code the customer chooses to associate, so persistence is a service the customer granted, not a property their hardware leaks.
**Alternatives.** Per-network stable-but-not-global addresses (the middle path several OSes actually implement — worth noting it exists); refusing convenience entirely (defensible, costs the café its feature).
**Trade-offs.** Convenience vs unlinkability; the café's marketing value vs customer trust if tracking is discovered.
**Common mistakes.** Treating randomization as a malfunction ("new phones are broken"); arguing privacy as a slogan without naming the café's legitimate interest; missing that the padlock/login analogy (PB-109) recurs here; designing "fix the phones" instead of "fix the portal's keying".

---

## PB-205 — The image that always loads last

**Solution guide.** Separate *order* from *speed* first — the symptom is sequencing, not bandwidth, which is why "slow Wi-Fi" is the least informative hypothesis. Ranked hypotheses: (1) the image is served from a CDN whose edge node serving the student's region is cold (first-byte delay on cache miss) while the text is served from a warm origin/edge; (2) the image is deliberately lazy/lower-priority (progressive rendering: text paints first so the page is usable); (3) cache-state difference — the other network's user had the image cached. Evidence plan, named by panel and column: dev-tools *Network* panel — the **Timing** breakdown separates waiting (server/edge response) from content download; the **Initiator/Priority** column reveals lazy-loading and priority; the response's cache headers (`cf-cache-status`, `age`, `x-cache`-class fields) reveal hit/miss. The cross-network datum mostly rules out "the site is globally slow" — the failure is localized to path or policy.
**Alternatives.** A/B the same URL directly (bypasses render order — isolates delivery from page policy); ask the site's status page (some publish CDN incidents).
**Trade-offs.** Depth of investigation (opening dev-tools) vs time; the read-only constraint is not a limitation but the *ethics* of diagnosis.
**Common mistakes.** Conflating order with speed throughout; no discriminating evidence ("probably the CDN" with no plan to check); measuring from a single load (cache state varies — reload twice, note the difference); blaming the nearest cause (Wi-Fi) because it's visible.

---

## PB-206 — The breach email about a site you forgot

**Solution guide.** Verify before acting: the breach email itself must pass L29's triage (sender domain, link-hover, urgency pressure) — a breach announcement is a perfect phishing costume. Exposure assessment: the hottest account is any *still* sharing the old password *and* lacking MFA; the one changed last month is cooler but not cold (it shared the credential for months); MFA-on-email-only means the email account is vaulted but the others are naked. Ordered response: (1) verify breach via the service's official status/notification channel (not the email's link); (2) change reused passwords, most-exposed first; (3) enable MFA, email first (it's the recovery hub for everything else); (4) check recovery options (backup codes, phone number) on each account; (5) expect targeted phishing — breach lists feed *personalized* attacks, so raise suspicion for a while. The sentence on "exposed": exposure creates *risk*, not certainty of compromise — no evidence of login is not evidence of safety, and vice versa.
**Alternatives.** A breached-credential checking service (course-safe: have-not-been-pwned-class sites) to scope which other accounts shared the password.
**Trade-offs.** Thoroughness (changing everything) vs triage (hottest first) under exam-week time; the verification step costs minutes and defeats the phishing costume.
**Common mistakes.** Clicking the email's link to "check the breach"; treating the changed-last-month account as safe; stopping at password changes without MFA and recovery-options review; ignoring the phishing-spike consequence of the breach list.

---

## PB-207 — The membership sheet that can't answer simple questions

**Solution guide.** The tick-mark columns fail in L25 terms because each is a *fact about time fused into the table's shape* — adding a month means adding a column, and "attendees since October" requires a human to scan twelve columns. The redesign separates facts into tables anchored by keys: MEMBERS (member_id, name, join_date), ATTENDANCE (member_id, event_date or event_id), FEES (member_id, term, paid_date) — one fact per row, IDs as the anchors, so any question becomes a filter-and-join rather than an eyeball-scan. Query-shaped sentence: `SELECT name FROM members JOIN fees ON members.id = fees.member_id WHERE fees.term = 'Autumn' AND fees.paid IS NULL AND members.id NOT IN (SELECT member_id FROM attendance WHERE date >= 'October 1')`. Migration order that keeps the club running: freeze edits on the old sheet → export MEMBERS first (the anchor entity everything references) → backfill attendance and fees → verify counts (members in old sheet == members in new table) → retire the old sheet to read-only archive.
**Alternatives.** A relational-shaped cloud spreadsheet (two linked sheets) is fully defensible at this scale — the constraint is *discipline*, not software; a real database is not yet justified (PB-112's over-engineering warning still applies).
**Trade-offs.** Migration effort (a weekend of careful copying) vs the hour-per-question status quo; rigour vs the volunteer committee's spreadsheet comfort.
**Common mistakes.** Designing three tables but keeping free-text status columns (the disease persists); no unique member_id (name collisions destroy the join); migrating fees before members (orphaned keys); no verification step before retiring the old sheet.

---

## PB-208 — The free-tier cloud scare

**Solution guide.** Triage by what free tiers actually measure: the VM is the suspect if it ran hours beyond the free allowance (free tiers usually cover *small* instances for *limited hours*); the disk and snapshot bill *independently of the VM* — storage is measured whether or not anything is attached or running, which answers the "stopped still costs?" question (a stopped instance stops compute billing; its disks, snapshots, and sometimes addresses keep billing). Teardown, in order: stop the instance → decide snapshot data (export anything needed to local) → delete the instance → delete the disk → delete the snapshot → verify: console shows zero resources *and* the billing page's estimate shows zero running-rate. Two guards: a budget/billing alert at a trivial threshold (catches day 2, not week 2), and a teardown ritual with a screenshot proving empty (Lab 7's culture, made personal).
**Alternatives.** Disputing the charge is available but weak without evidence; the honest path is pay-the-small-amount-and-log-the-lesson — disputing a few currency units of *correctly metered* usage teaches the wrong lesson.
**Trade-offs.** Keeping the snapshot (future lab convenience) vs its monthly cost (the exact trap just sprung); deleting immediately vs end-of-break cleanup (delay is how this happened).
**Common mistakes.** Stopping the VM and calling it done (the storage keeps billing — the scenario's own trap); deleting the instance but not its disk; no verification step; no alert (the guard that would have caught it at day 2).

---

## PB-209 — The attendance chart that shamed the wrong group

**Solution guide.** Diagnosis: the aggregation merged populations with different session counts (day students' full schedule; evening students' rescheduled-and-unmarked sessions) into one percentage — the denominator differs per group and the chart hides it, so the 40% compares unlike with unlike (a Simpson's-adjacent effect, at concept level). Redesign: per-cohort bars (or small multiples), each with its denominator shown, rescheduled sessions excluded *until re-marked* — exclusion stated, not silent. Caption: "Attendance by cohort, Term 1; evening-cohort sessions pending re-marking after room changes excluded — see note." The deeper point: the corrected chart may *still* show 40%, and the caveat still matters — honest design separates "this is what we measured" from "this is what we claim". The rep's intent was good; the failure was method, which is fixable — say that too.
**Alternatives.** Publishing raw session-level data with the chart (transparency, but harder to read); a two-chart panel (raw + adjusted).
**Trade-offs.** Granularity (honest) vs simplicity (readable) — resolvable by caption and small multiples, not by choosing one; speed of posting an apology-chart vs doing the correction properly.
**Common mistakes.** Defending the chart as "technically true" (the weakest position in data presentation); fixing numbers without fixing the *denominator statement*; assuming bad faith by the rep (it was aggregation ignorance, the course's recurring villain); no correction message to the shamed group.

---

## PB-210 — The chatbot's confident citation to nowhere

**Solution guide.** The workflow is designed for *adoption under deadline*, which is the actual engineering constraint: (1) list the page's checkable claims (numbers, dates, definitions, citations); (2) verify **citations and numbers first** — a fake citation poisons the reader's trust budget for everything else, and fabricated references are the AI's most characteristic failure; (3) mark what couldn't be verified *as* unverifiable (an honest gap beats a silent guess); (4) write the disclosure line: tool name, role (drafting aid), what was verified, what was changed. Time budget ~5 minutes per page of notes — sized so a busy first-year actually does it; a 45-minute archival-quality process would be ignored, and an ignored process protects nobody.
**Alternatives.** Asking the tool for sources and checking *those* (good instinct; must name the fake-citation risk — the tool inventing a plausible-looking source); using AI only for explanation, never facts (the safest split, but harder to hold under exam pressure).
**Trade-offs.** Speed vs reliability (the 5-minute design threads it); using AI for *understanding* (low risk — errors surface in discussion) vs *facts* (high risk — errors surface in the exam).
**Common mistakes.** Verifying only what *feels* wrong (fluency is not accuracy; the confident wrong ones are exactly what feels right); skipping the disclosure (integrity exposure, not just accuracy); treating one verified claim as a licence for the rest.

---

## PB-211 — Forty slides for a five-minute talk

**Solution guide.** Design from the decision: the talk exists to get the budget approved, so the deck carries *the decision path*: title → income summary → the three biggest spends → reserve status → the ask → Q&A. Six slides, one message each; the one chart that earns its place is income-vs-spend (or the reserve trend) with honest axes — it carries more than any three transaction slides. The 34 cut slides are *demoted, not deleted*: the full transaction ledger already lives in the spreadsheet; the deck gets a linked appendix (or a "backup slides" section) so any question in Q&A has an answer — the audit trail is preserved because it never lived in the deck in the first place. The principle: a slide deck is the *presentation layer*; the records live in the *record layer*; confusion between them produces 40-slide budget talks.
**Alternatives.** A one-page handout with the table + a 3-slide deck (defensible for a business meeting; the 6-slide version keeps presentation momentum).
**Trade-offs.** Completeness (every transaction visible) vs attention (the audience's capacity to approve anything); appendix weight vs deck clarity.
**Common mistakes.** Cutting to 6 slides but deleting the numbers entirely (auditability lost); keeping all 40 but talking faster; a chart that aggregates so much it shows nothing (or one with a truncated axis — the honest-axes rule from L19); no rehearsal, so the ask slide surprises even the speaker.

---

## PB-212 — The laptop that's fast in the shop, slow in the library

**Solution guide.** Fair test design, Lab 2's discipline applied to thermals: same workload (a fixed compile task or stress script), same power state (AC, battery settings identical), two environments (shop-like cool room; the library), measuring **clock speed and temperature over 20+ minutes** — sustained, not instantaneous, because throttling is a sustained-load phenomenon; multiple runs, background load noted, results tabulated. Mechanism: CPUs throttle when silicon hits temperature limits; the library's warmth plus restricted airflow slows the fans' effectiveness; clocks drop under sustained load and the machine *feels* sluggish while benchmarks (short bursts, cool start) never see it. The spec question for next time: not "what benchmark score" but "what sustained clock under load" — reviews measuring sustained performance and cooling design are the honest spec source; peak numbers are a marketing default because they're higher.
**Alternatives.** A cheaper diagnostic first (feel the exhaust, listen for fan ramp) — no tools, weak evidence, but free; vendor thermal documentation if published.
**Trade-offs.** Test rigour (controlled runs) vs the student's time; the buying lesson arrives after the money is spent — the case's real deliverable is the *question to ask next time*.
**Common mistakes.** Comparing single-point measurements (a 10-second clock reading proves nothing about sustained behaviour); uncontrolled variables (background updates, different power plans); concluding "the laptop is defective" (thermal behaviour under sustained load is a *design* property, not a fault); not recording ambient temperature — the hardest variable to hold constant.

---

## PB-213 — The backup that had never been asked to work

**Solution guide.** Failure-mode table first: cloud-sync folder — sync semantics *faithfully propagate deletions* (the deleted folder was "backed up" into deletion), so it is a copy, not a backup; external drive — never restore-tested, so its readiness is a hypothesis (and it has now failed its first real request); university storage — unexamined (does it snapshot? on what schedule?). The taxonomy: *sync* mirrors what you do (including mistakes); *backup* preserves what you had (with history). Redesign with zero budget: versioned cloud snapshots (the ~30-day version history most services keep — turn it on, note the window) as one copy; the external drive becomes a scheduled *one-way* backup (copy →, never ←), not a sync; university storage as the offsite third copy. Test cadence with dates: quarterly, restore **one file per component**, calendar-anchored — a backup is a restore that has already worked; anything untested is a hypothesis with good posture.
**Alternatives.** Free-tier backup tools with scheduling (fine if the tool is understood); a second cheap drive instead of cloud versions (weaker offsite, stronger physical control).
**Trade-offs.** Effort (quarterly tests) vs the certainty they buy; automation (set-and-forget) vs drift (scripts rot — the calendar anchor is the drift guard).
**Common mistakes.** Confusing sync with backup *again* (the case's own trap — name the distinction explicitly in the redesign); testing by "opening the drive" instead of restoring a file; no cadence (a one-time test is already going stale); forgetting the ransomware angle: versioned copies survive encryption events; live-synced ones don't.

---

## PB-214 — The CAPTCHA that locked out the student it was protecting

**Solution guide.** Three levels, each with its trade-off named: **form** — replace the visual-only challenge with modern invisible/behavioural checks or add an audio alternative (trade-off: behavioural signals are weaker against determined bots; audio has its own accessibility gaps for deaf-blind users); **process** — asynchronous verification (request now, receive a code/link by email with a deadline) so the 9-to-5 phone window stops being the bottleneck (trade-off: slightly slower onboarding, a new email-delivery dependency); **policy** — extend phone hours or route exceptions through the accessibility office (trade-off: staffing the office didn't budget). Prioritize the **process** level: it helps *everyone* outside office hours — disabled students, commuters, carers — not just the student who complained; form-level fixes help this case, process-level fixes change the class. WCAG's "alternatives" principle is the compliance anchor, but the design argument stands without it. Bots remain a real threat — the answer is *proportionate* defence, not zero friction.
**Alternatives.** Institution-wide SSO (kills most bot-signup risk at the source — bigger project, better answer if the university has it).
**Trade-offs.** Security strength vs access breadth at every level; the priority call itself (help-one vs help-many) is the case's deepest judgement.
**Common mistakes.** Treating "add audio CAPTCHA" as complete (it isn't — and audio CAPTCHAs are their own accessibility problem); framing accessibility vs security as a slogan-war instead of a design tension with named trade-offs; no priority justified (lists all three levels, chooses none); forgetting the bots are real — a plan with no defence isn't a plan.

---

## PB-215 — The computer lab that runs all night

**Solution guide.** The proposal, mechanism by mechanism: sleep (not shutdown) after X minutes idle — sleep preserves Wake-on-LAN and morning readiness while cutting the 50–100 W login-screen draw to a few watts; updates in a scheduled 02:00–04:00 window with wake-from-sleep (patching stays deliberate, L12); a monthly power-state audit (a walk-past at 22:00 catches machines stuck awake and the one broken-fan casualty). Trade-offs per mechanism: sleep still draws standby power (vs shutdown's zero — but WoL and morning speed win); scheduled windows vs vendor patch timing (occasionally a critical patch lands outside the window — the audit catches stragglers); automation vs the staff's "switching is annoying" (that's the habit the policy replaces, gently). The broken-fan machine is a *different category*: not an energy line-item but a safety escalation (fire risk) — report today, not at the next audit. Keep the proposal honest with a measurement plan: meter one circuit before/after for a month.
**Alternatives.** Shutdown-with-WoL-only (deeper savings, slower mornings — defensible if users accept it); thin-client conversion (out of budget scope here, PB-404's territory).
**Trade-offs.** Energy vs morning readiness; automation vs control; the order-of-magnitude estimate (state assumptions: ~40 machines × ~75 W saved × 8 h × ~200 nights ≈ 4,800 kWh/yr — an estimate, not a claim).
**Common mistakes.** Shutdown-everything (kills updates and morning readiness — the over-correction PB-116 warned about); treating the broken fan as an energy stat; no baseline measurement (savings claims without before-data are exactly the dishonest-chart pattern); forgetting wake-on-LAN exists and assuming sleep breaks morning use.

---

## PB-216 — The clinic's appointment sheet (conceptual)

**Solution guide.** Risks ranked: (1) **integrity** — two receptionists editing separate copies produced the wrong-day arrival; there is no single authority for "what is the appointment book"; (2) **privacy** — full names, phone numbers, and visit reasons sit on unattended printouts at a reception desk; (3) **auditability** — nobody can say who changed what, so errors are undiagnosable and unattributable. Minimal redesign a two-desk clinic adopts: the shared drive file becomes the *only live* copy ("the drive copy is the only live one — print is a snapshot" as the one rule); printouts carry time + initials only (minimization — reception needs "10:00, J.O.", not the diagnosis); the evening printout is shredded, not binned; keep paper for the day-list because the staff trust it — *adoptability is part of the design*, not a concession. The boundary sentence: a real clinic's compliance regime (health-privacy law, audit systems, professional record-keeping) exceeds this scope — the case is about *thinking at the right scale*, and knowing where the scale ends.
**Alternatives.** A shared calendar tool (the drive file's natural upgrade — defensible if the clinic's connectivity supports it); print-locking (a technology answer to a policy problem — weaker).
**Trade-offs.** Paper familiarity vs single-authority integrity; minimization vs reception convenience (they can't glance at the sheet for the reason anymore — deliberate).
**Common mistakes.** Proposing an enterprise system (budget + adoptability ignored — the case's constraint says two desks); fixing copies without fixing the printouts (the privacy risk walks out the door at closing); no rule stated (a redesign without an operating rule reverts in a week); inventing compliance claims beyond the case's information.

---

## PB-217 — The LMS quiz with the wrong answer key

**Solution guide.** Three separable issues, three processes: **prevention** — a key-validation step before publishing: a second reader, or a canary question (a question whose answer is known with certainty, to catch a shifted key), because the failure was *systemic* (no check existed), not personal; **regrade** — automatic, complete, and *communicated*: a system error means students did nothing wrong, so the fix is silent-to-students only if the announcement is also silent — tell the six (and the class) what happened and that grades were corrected; **the appeal** — process it by the syllabus's integrity procedure, not instinct: LMS logs give timestamps, the screenshot is evidence to be examined, and the presumption is good faith until the evidence says otherwise. The meta-lesson is the decomposition itself: a messy incident *looks* like one angry blob but is three different problems with different stakeholders, and each deserves its own answer — PB-225 will reuse this move.
**Alternatives.** Voiding the question for everyone (defensible if the key error affected many — proportionality decides); harder quizzes (irrelevant to the actual failure — process theatre).
**Trade-offs.** Transparency (announcing the error) vs institutional embarrassment — transparency wins because the six students talk anyway; procedure-following vs instructor instinct — procedure wins because instinct is exactly what appeals exist to guard against.
**Common mistakes.** Blending the three issues into one announcement; prejudging the screenshot student before the log check; "fixing" prevention with blame ("be more careful") instead of a process check; over-apologizing or under-informing — the announcement drafts fail at both extremes.

---

## PB-218 — The city form that only exists on paper

**Solution guide.** Benefits/risks with bearers named: benefits — access for time-poor and mobility-limited residents, queue-cost reduction, staff time freed (bearer: residents and the office); risks — digital exclusion of offline residents (bearer: precisely the residents who most need the service), staff displacement fear (bearer: office staff), integration cost realism (bearer: taxpayers, if the claim is real). The plan in three phases: **pilot** with the assist desk integrated (two days/week, the existing resource); **full digital with paper coexistence** — never a cutover; **review with usage data by demographic** — the only way to know whether access *widened* or the queue merely moved. The deliberate paper sentence: "Paper remains available to anyone, indefinitely" (or a named sunset criterion) — either is defensible; *having* the sentence is the mark. The blocker claim gets tested, not absorbed: "integration cost" is checkable (what integration? quoted by whom? would the existing app platform actually need it?).
**Alternatives.** Phone-assisted digital submission (the assist desk by phone — extends reach cheaply); third-sector partnerships (libraries running assisted access).
**Trade-offs.** Equity vs efficiency is the headline, but the quiet one is *pilot patience vs political demand for launch*; phased beats big-bang here specifically because trust, once lost, is the expensive thing.
**Common mistakes.** Digitize-everything enthusiasm with no exclusion analysis; treating "integration cost" as either gospel or fiction instead of a testable claim; paper "temporarily" (sunset without criterion = exclusion with a delay); no demographic measurement (the review phase degenerates into anecdote).

---

## PB-219 — The bakery's five dead laptops in three years

**Solution guide.** Environment first, because it's the killer: relocate the workstation to the back-office nook (out of oven heat and flour-dust paths — the failures *cluster* near ovens and the flour shelf, which is the data telling you the cause), plus a sealed keyboard cover and a wipe routine for the till's inevitable counter presence. Hardware second, requirements-first: the purchase question is *not* "which laptop" but "what survives this environment" — a fanless/sealed small machine, or tablet-at-the-till, justified by environment; brand loyalty has been buying the same failure every seven months. Data third, decoupled from devices entirely: cloud accounting (offsite by design — the next laptop death costs hardware, not records) plus a weekly export. The three-year cost comparison: environment fix + one proper machine (few hundred) vs a fourth consumer laptop on the same schedule — the estimate needs *stated* assumptions (failure rate unchanged without the fix; that's the point of the fix).
**Alternatives.** Tablet + till stand (sealed, cheap, fits the workload — a genuinely strong answer); a used business-class machine as interim (buys time while the nook is prepared).
**Trade-offs.** Upfront cost (nook prep, proper machine) vs the replacement treadmill; the owner's habit change (working from the nook) vs machine lifespan — the cheapest failure is the one the environment prevents.
**Common mistakes.** "Buy a better laptop" (same environment, same death, more money); fixing hardware while the customer records stay device-bound (the *data* risk is untouched by any purchase); no environment analysis (the failure pattern was handed to you — use it); hiding costs in assumptions.

---

## PB-220 — The results-release email storm

**Solution guide.** The load mechanism: the portal's capacity problem isn't volume but *synchronization* — 8,000 requests in the first minute is a coordination artifact (a release time), not a capacity ceiling; steady-state load all day would be fine. Redesign, two changes: **staggered release by faculty** (or a queue/holding page that meters entry) flattens the spike; **a status page** ("results live for Law; Arts opens 09:20") converts retry-storms into patience — most load during outages is people refreshing blindly. The email critique applies L30 minimization directly: grade summaries as attachments sit in inboxes *forever*, on shared devices, forwardable — a link to the authenticated portal (per-student, session-bound, revocable) delivers the same information with access control and no permanent payload. The 200 bounces are a data-quality finding (stale contact records — L25-adjacent), not an email bug: the registry's records need a maintenance process, or next term's storm has the same wet grass.
**Alternatives.** "Just add servers" for one morning a term (defensible for the biggest university; costs idle capacity the other 364 days — name the trade); pre-scheduled portal publication with no email at all (the endpoint the critique points toward).
**Trade-offs.** Staggering (fairness of order) vs simultaneous release (the emotional experience of everyone finding out together); link-vs-attachment (control vs inbox permanence) — minimization wins on privacy, say why.
**Common mistakes.** Diagnosing "underpowered servers" (the spike pattern is the diagnosis — use the evidence given); redesigning the portal while leaving the email payload (the bigger privacy leak unexamined); treating bounces as noise; no status-page/communication layer (the retry storm is half the load).

---

## PB-221 — Five family members, one administrator account

**Solution guide.** The design: standard accounts for each person's daily use; one admin account used *deliberately* for installs (not "because installing games needs it" — elevation prompts per-app from a standard account cover the legitimate need); per-user document folders; the tax files owned by the parents' account with their own backup (L11) — the sensitivity and the ownership should align. Habit changes: elevation prompts get *read* before approval (the mod installed itself through an unattended yes); installs happen from the admin account, with intent, from source sites. Containment mechanism, three sentences: malware running as a standard user touches that user's files and that user's privileges; to reach the tax files or system settings it needs an elevation event; an unattended "yes" at an admin session is what the old design provided constantly. The framing that keeps family peace: least privilege is *containment*, not punishment — everyone can still do everything they did, the blast radius is just smaller.
**Alternatives.** Device-level separation (a "family" machine and a "parents" machine — stronger, costs money and space); Microsoft/Google family-account tooling on top (complementary).
**Trade-offs.** Convenience (one account, everything shares) vs containment; the teen's autonomy vs parental control — the design threads it by constraining *capability*, not behaviour.
**Common mistakes.** "Admin for everyone but be careful" (PB-104's mistake, re-learned at higher stakes); moving tax files but adding no backup (the redesign creates a new single point); framing the change as distrust of the teenager (politics kill the design); no explanation of *why* separation contains (the mechanism is the learning, not the account list).

---

## PB-222 — The poster QR code that scans from paper but not from the projector

**Solution guide.** Mechanism: a phone camera *samples* whatever it's pointed at; a QR is readable when the sampled image resolves each module (the little squares) with enough contrast. Print gives crisp ink edges — high signal. Projection composites the slide through projector resolution, hall lighting, and screen surface: blur softens module edges, small on-screen size shrinks modules below resolvable sampling, and colour/contrast shift (washed blacks, projector gamma) cuts the margin — the code falls below its error-correction tolerance. Print "works on my laptop" proves nothing about the hall because the sampling chain differs. Three display rules: minimum size (≈ one-tenth of slide width as a floor — more for big halls); maximum contrast (dark-on-light or light-on-dark with no gradient/animation nearby); test from the back row of *the actual room* at talk lighting. The fallback that saves every talk: a short human-typable URL beside the code — redundancy at the *information* level (two independent encodings of the same destination), which is the deepest lesson: the QR's built-in error correction has limits, so add redundancy where it fails.
**Alternatives.** Bigger-is-only-answer (defensible for tiny codes, but contrast and testing still bind); URL shortener for the fallback (careful — PB-224 is literally this trap; own-domain short path only).
**Trade-offs.** Slide real estate (a big QR dominates the slide) vs scan reliability; test-time investment vs event-night risk.
**Common mistakes.** Scaling the QR by eye without the back-row test; low-contrast "branded" codes (design trends eat function); no fallback (single point of failure at the worst moment); blaming the phone.

---

## PB-223 — The dorm door that needs three of five conditions

**Solution guide.** The expression: `UNLOCK = VALID ∧ (PIN ∨ SUPERVISOR) ∧ ¬LOCKOUT`. Friday's evaluation: LOCKOUT = true forces ¬LOCKOUT = false, so UNLOCK = false *regardless* of the stuck SUPERVISOR flag — the door should not open, and if it did open, the expression wasn't the door's actual rule (challenge the implementation, not the algebra). The AND-placement of `¬LOCKOUT` is what makes lockout absolute: no combination of the other inputs can bypass it — that's the design intent of a maintenance lockout, preserved by the operator structure. The stuck flag is the real teaching payload: SUPERVISOR's value is *stale state* — asserted Thursday, never re-asserted, silently rewriting Friday's policy. Flag hygiene: state that outlives its assertion needs expiry or a heartbeat (re-asserted presence — a badge-tap, a periodic ping); any flag consumed by a security decision must be *fresh* to count. The habit: evaluate the expression before trusting the mechanism — the Friday scenario is exactly the check.
**Alternatives.** Adding priority levels (supervisor-override-bypasses-lockout — a policy change, not a modelling choice; if intended, the expression changes to show it explicitly).
**Trade-offs.** Security (lockout absolute) vs flexibility (override exists somewhere?) — the *policy* question behind the algebra; flag freshness vs system simplicity (heartbeats cost infrastructure).
**Common mistakes.** Evaluating with the stuck flag as true and concluding the door opens (the whole AND-chain is the point); treating the stuck flag as a one-off glitch instead of a class (stale state is everywhere — badges, sessions, caches); no hygiene rule stated; mis-parenthesizing the expression (operator precedence is the algebra's first trap).

---

## PB-224 — The short link that rotted before graduation

**Solution guide.** Dependency analysis: 500 flyers encoded a promise that the *shortener company* would exist, keep its domain, and keep redirecting — a third party's survival became load-bearing for the society's publicity, for zero benefit the university's own domain couldn't provide. The flyer's real dependency should have been the society's persistent URL (the university hosts it; universities outlast link-shortener startups). Policy, three rules: (1) printed/QR links point at the society's own domain only; (2) paths are stable and semantic (`/join`, `/flyer` — chosen once, kept forever); (3) redirects change *targets*, never the printed string — where the link *goes* is mutable infrastructure; what's *printed* is permanent. Remediation: create `/flyer2026` on the society's site → redirect to wherever recruitment actually lives this year (the printed stocks become valid again, no reprint). The principle, stated: a printed link is a permanent promise — only make it from infrastructure you control.
**Alternatives.** Reprint with a new QR (costs money, fixes nothing — the next service dies too); QR at the old shortener *plus* own-domain redirect (the correct layering had it been designed in: shortener as the mutable target behind the stable printed URL).
**Trade-offs.** Shortener analytics/renames (the convenience that justified the dependency) vs institutional permanence — the analytics were never worth the single point of failure.
**Common mistakes.** "Just get a new shortener" (the dependency persists, renamed); changing the flyer URL instead of adding a redirect (reprints, and the same death awaits); no policy output (the case's deliverable is the *rule*, not the fix); missing that the university domain was available all along.

---

## PB-225 — The AI-generated study guide that half the class used

**Solution guide.** Three questions, separated the PB-217 way: **the author** — "I made it in five minutes, obviously check it" names the effort but not the responsibility: sharing *at scale* (half the class) is a publication act, and unverified AI content published before a quiz carries responsibility even without malice; disclaimers set expectations, they don't transfer duty (a disclaimer helps when content is *labelled* unverified and stakes are low — "my rough notes" — not when it functions as the class's study guide). **The class** — consuming unverified content is also a choice; L28's verification loop applies to shared notes, not just submitted work; the two subtle errors were *findable* in minutes against lecture pages. **Fairness** — the quiz question born from an error is the instructor's integrity process (regrade/exclude per policy — PB-217's pattern), a separate issue from the group's norms. The standing rule: "AI-shared content is labelled and verified — or marked unverified — and never the night before." The day-of post: own it, correct it, link the lecture page.
**Alternatives.** Banning AI content in the group (unenforceable and drives it underground — norms beat prohibitions); appointing a verifier role (concentrates labour; the norm distributes it).
**Trade-offs.** Openness of sharing (the group's value) vs verification friction (the norm's cost) — the rule threads it by *timing and labelling*, not prohibition; the author's reputation absorbs a real cost here — that's the lesson landing, not an excuse to pile on.
**Common mistakes.** Treating it as a cheating scandal (nobody cheated — the failure is epistemic, not integrity-procedural); mob-piling on the author (chilling future sharing — the opposite of the norm's goal); "obviously check it" accepted at face value (test the disclaimer logic); no standing rule (the next guide arrives quiz-eve, unverified, again).
