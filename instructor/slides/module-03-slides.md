# Module 3 Slide Decks — L09–L12

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L09 — The Software Landscape (Slides + Speaker Notes)

**Resources:** projector; one proprietary + one open-source tool's About/license panel (guide prep); students near machines for the autopsy.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Hardware recap + objectives | S1–S2 | 8 |
| The stack, invented by the room | S3–S4 | 18 |
| Licensing models | S5–S6 | 15 |
| Firmware and drivers | S7 | 8 |
| Software autopsy activity | S8 | 25 |
| Debrief + concept check | S9–S10 | 14 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 20 |

### Slides

# L09 · The Software Landscape
**Module 3 · Stage 1 · 2 hours**

## S1 · Hardware, recapped in one breath
**Notes:** [~5] TALK: Module 2 drew the machine; Module 3 makes it *behave*. ASK: "What was the von Neumann one-line summary?" MISC: none. TRAN: "What separates your essay from transistors?"

## S2 · Today
- The stack, from silicon to you
- Who owns what you run: licensing
**Notes:** [~3] TALK: promise the upside-down opening on the next slide. TRAN: stack first.

## S3 · Build the stack yourselves
- Hardware at the top — what's between it and your essay?
**Notes:** [~10] TALK: draw hardware at top, applications absent; students invent the layers (guide's teaching tip). ASK: "Name the layer you'd add next." MISC: students skipping utility/driver layers — that gap *is* the next slide. TRAN: "The official version."

## S4 · The official stack
- Hardware → OS → utilities/drivers → applications → users
**Notes:** [~8] TALK: each layer hides the one below; the spreadsheet user never meets a driver. ASK: "Which layer breaks when a printer 'isn't recognized'?" (Driver/OS boundary.) MISC: "apps run on hardware directly" — only the OS may touch hardware; say it absolutely. TRAN: "Who owns each layer?"

## S5 · Licensing: the 2×2
- Proprietary · free/open-source · freemium · trial — price vs freedom
**Notes:** [~8] TALK: the 2×2 axes (guide's plan); "free" carries two meanings in English — say which each time. ASK: "Where does your own browser sit?" MISC: "free = worthless" — module-level warning; maintenance practice is the real signal. TRAN: "Two special residents."

## S6 · Firmware and drivers
- Software stored on/in the device it serves · the OS's hardware translators
**Notes:** [~7] TALK: one slide, one story each (printer firmware update; GPU driver) — resistance to over-teaching, per the guide. ASK: "Why does firmware survive when everything else became apps?" MISC: "drivers are applications" — they're OS-layer translators. TRAN: "Autopsy time."

## S7 · Activity — Software autopsy (25 min)
Pairs: one installed program · layer + license · evidence required
**Notes:** [~25] TALK: per the lecture page's activity; evidence = About panels, license screens, install logs. ASK (circulating): "What *evidence* places it in that layer?" MISC: phone-app autopsies are equally valid (guide tip). TROUBLE: machines missing — pre-load two candidates on the projector machine for shared autopsy. EXT: classify a *driver* from the device manager. TRAN: "What did you find?"

## S8 · Debrief: the board table
- System / application / not-software — with evidence
**Notes:** [~7] TALK: three-column debrief per the guide's plan; celebrate hardest classifications. ASK: "Which classification are you *least* sure of — why?" MISC: none. TRAN: "Quick check."

## S9 · Quick check
1. Classify: driver, spreadsheet, OS, backup utility.
2. One practical proprietary-vs-open difference for *you*.
3. Why is firmware firmware?
**Notes:** [~10] TALK: write-pair-resolve; Q1 is the layer skill. MISC: Q1 — backup utility lands in system-software/utility layer; expect "application" answers, accept with utility-layer reasoning. TRAN: "Summary."

## S10 · Summary
- The stack; licensing as price-vs-freedom; firmware and drivers in place
**Notes:** [~5] TALK: exam skeleton; the stack model is the course's most reused idea — say so. TRAN: exit ticket.

## S11 · Exit ticket
**Name the layers between your fingerprint and your bank's server.**
**Notes:** [~12] TALK: expected: app → OS → drivers → network stack (forward link to Module 6). Collect slips, then hold questions in the remaining time — parking-lot items open L10. Sort slips tonight; missing driver layers are the diagnostic.

---

## L10 — Operating System Fundamentals (Slides + Speaker Notes)

**Resources:** projector machine with working CLI (tested pre-class); same file listing GUI+CLI side by side.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Stack recap + objectives | S1–S2 | 8 |
| The five responsibilities | S3–S4 | 18 |
| Boot: five beats | S5–S6 | 14 |
| CLI vs GUI + race activity | S7–S8 | 28 |
| OS families | S9 | 10 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 18 |

### Slides

# L10 · Operating System Fundamentals
**Module 3 · Stage 1 · 2 hours**

## S1 · The OS is a program too
**Notes:** [~5] TALK: yesterday's frame — the OS is *just* a program with special powers; today, what it does all day. ASK: "Which layer did we place the OS in?" TRAN: "Its five jobs."

## S2 · Today
- Five responsibilities · five boot beats · two interfaces
**Notes:** [~3] TALK: promise the race — timekeeping will be competitive. TRAN: jobs.

## S3 · The five jobs
- Processes · memory · devices · files · interface
**Notes:** [~10] TALK: the guide's labels (traffic police, hotel manager, translators, librarian, front desk) — retire them as real terms land. ASK: "Which job runs when 40 tabs slow the machine?" MISC: "the OS is the windows" — GUI is one interface; the kernel does the five jobs. TRAN: "The daily miracle."

## S4 · Boot: five beats
- Power → firmware self-test → bootloader → kernel → login
**Notes:** [~8] TALK: five-beat story per the guide; students place "Wi-Fi joins" and "virus scan starts" on the timeline. ASK: "Which beat fails with a dead disk?" MISC: "boot = pressing the button" — the button is beat zero; the *handoffs* are the story. TRAN: "Two ways to talk to it."

## S5 · Two interfaces
- GUI: discoverable · CLI: precise, automatable
**Notes:** [~7] TALK: same file listing side by side; neither is obsolete — the race will measure it. ASK: "Which would you script at 2 a.m. for 300 files?" MISC: "CLI is obsolete" — the race data will rebut; let it. TRAN: "Prove it with a stopwatch."

## S6 · Activity — Dual-interface race (20 min)
Same five file operations · GUI vs CLI · time and errors
**Notes:** [~20] TALK: per the lecture page's activity; enforce the five-op cap and strict timing (guide tip). ASK (during): "Why is that operation faster by keyboard?" MISC: racing without reading results — disqualify style; correctness *and* time count. TROUBLE: terminal broken — the shared projector terminal is the backup stage. TRAN: "Who won what, and why."

## S7 · Race debrief
- Which tasks each interface won — and the pattern behind it
**Notes:** [~8] TALK: harvest times to the board; the pattern: bulk/repeatable → CLI, exploratory/visual → GUI. ASK: "State the pattern in one sentence." MISC: none. TRAN: "The families."

## S8 · OS families
- Windows · macOS · Linux · Android/iOS — same five jobs, different philosophies
**Notes:** [~10] TALK: philosophy, not fandom; every kernel does the same five jobs differently. ASK: "Which family runs your university's servers — and why?" MISC: brand wars — redirect to job-by-job comparison. TRAN: "Check the five."

## S9 · Quick check
1. Name the five responsibilities.
2. Second boot beat — and its job.
3. Which race operation did CLI win, and why?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "the BIOS" is close; sharpen to firmware *self-test* of hardware. TRAN: "Summary."

## S10 · Summary
- Five jobs · five beats · two interfaces, chosen per task
**Notes:** [~5] TALK: exam skeleton. TRAN: exit ticket.

## S11 · Exit ticket
**A file was deleted by mistake. Which of the five jobs does 'undelete' live in — and why might recovery be partial?**
**Notes:** [~12] TALK: expected: file management; partial recovery because space was marked free (guide's misconception note). Collect slips, then hold questions in the remaining time — Lab 3 launches next lecture and CLI practice continues there. Bridges to L11; keep slips.

---

## L11 — File Systems and File Management (Slides + Speaker Notes)

**Resources:** projector; one badly named file for the live rename; Lab 3 checklist ready to launch.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Five-jobs recap + objectives | S1–S2 | 8 |
| The tree; paths on three OSes | S3–S5 | 20 |
| Names, extensions, metadata | S6–S7 | 14 |
| 3-2-1 backup discipline | S8–S9 | 14 |
| Lab 3 launch + reorganize activity | S10 | 30 |
| Concept check | S11 | 10 |
| Summary + exit ticket | S12–S13 | 12 |
| Buffer | — | 12 |

### Slides

# L11 · File Systems and File Management
**Module 3 · Stage 1 · 2 hours**

## S1 · Yesterday's deletion question
**Notes:** [~5] TALK: exit-ticket harvest — recovery is partial because space is marked free; today is the file job's hour. ASK: none. TRAN: "The tree."

## S2 · Today
- Trees and paths · conventions · 3-2-1 · Lab 3 launches today
**Notes:** [~3] TALK: today's skills are tonight's homework — say it. TRAN: the tree.

## S3 · The tree
- One root, branches, leaves — the same shape on every OS
**Notes:** [~7] TALK: draw the course-folder tree from the lecture page's figure. ASK: "Why a tree and not a pile?" (Uniqueness, findability.) MISC: "the desktop is a filing system" — a folder like any other; conventions beat desktop-piles. TRAN: "Addresses in the tree."

## S4 · Absolute paths
- Full address from the root — works from anywhere
**Notes:** [~7] TALK: construct two live, Windows-style and root-style. ASK: "What does `C:\` mean that `/` doesn't?" (Drive letters — a Windows quirk.) MISC: none. TRAN: "And from where you stand."

## S5 · Relative paths + the three-OS table
- From the current directory · Windows vs macOS/Linux notation
**Notes:** [~6] TALK: project the lecture page's three-OS table; drill two constructions. ASK: "When is relative safer than absolute?" (Moveable folders/projects.) MISC: none. TRAN: "Names carry meaning."

## S6 · Names and extensions
- Conventions that scale · extensions drive behaviour · keep them visible
**Notes:** [~8] TALK: the live rename (`Doc2 (3) final FINAL.docx` → convention) while narrating the check. ASK: "Why is hiding extensions the default — and why fight it?" MISC: "extensions are decoration" — they drive OS behaviour and safety checks. TRAN: "The file's own diary."

## S7 · Metadata
- Properties panels: author, timestamps, history
**Notes:** [~5] TALK: open properties live; connect to tracked-changes privacy (L19 preview). ASK: "Which metadata would embarrass a submitted document?" MISC: none. TRAN: "The insurance slide."

## S8 · 3-2-1
- Three copies · two different devices/media · one off-site
**Notes:** [~8] TALK: students write *their own* three locations first (guide tip); the gap between their answer and the rule is the moment. ASK: "Why does 'two copies on one disk' fail the rule?" MISC: "one backup = backed up" — the same-disk copy dies with the disk. TRAN: "Practice time."

## S9 · Cloud sync ≠ backup (one line)
- Sync propagates deletions; backups keep history
**Notes:** [~6] TALK: one line now, full treatment in Module 6 (L24); plant it. ASK: none. MISC: none. TRAN: "Lab 3 is live."

## S10 · Activity — Lab 3 launch + reorganize (30 min)
Scavenger hunt starts · one folder reorganized to convention
**Notes:** [~30] TALK: launch per the lab handout; in-lecture portion = one real folder reorganized to convention. ASK (circulating): "Which convention rule are you breaking on purpose, and why?" MISC: students reorganizing irrelevant folders — redirect to course folders. TROUBLE: machines short — pairs share; the hunt continues in the lab session. TRAN: "Check the grammar."

## S11 · Quick check
1. Absolute vs relative — one sentence each.
2. `C:\` vs `/` — what differs?
3. 3-2-1, in the rule's own numbers.
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q3 — "3 copies, 2 media, 1 off-site" verbatim earns full credit; paraphrases must keep the two-distinctions idea. TRAN: "Summary."

## S12 · Summary
- Tree + paths; conventions; 3-2-1
**Notes:** [~5] TALK: exam skeleton; the convention is a *professional* habit, not course bureaucracy. TRAN: exit ticket.

## S13 · Exit ticket
**Write the absolute path of your course folder on your machine — then the same address as a relative path from your home directory.**
**Notes:** [~7] TALK: two-line slips; wrong-root confusion (missing `C:\` or leading `/`) is the diagnostic to sort for. TRAN: Lab 3 continues this week.

---

## L12 — Installing, Updating, Troubleshooting (Slides + Speaker Notes)

**Resources:** projector; installer screenshots with permissions highlighted; three broken-scenario slides; one real troubleshooting story of your own.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Paths recap + objectives | S1–S2 | 8 |
| Installing safely | S3–S4 | 16 |
| Updates and patching | S5–S6 | 12 |
| The troubleshooting method | S7–S8 | 18 |
| Troubleshooting relay | S9 | 28 |
| Help requests + concept check | S10–S11 | 14 |
| Summary + exit ticket | S12–S13 | 10 |
| Buffer | — | 14 |

### Slides

# L12 · Installing, Updating, Troubleshooting
**Module 3 · Stage 1 · 2 hours**

## S1 · Paths recap, one question
**Notes:** [~5] TALK: read one good relative-path slip from L11 aloud; Module 3 closes today with the survival skills. ASK: none. TRAN: "Getting software in."

## S2 · Today
- Install safely · update deliberately · troubleshoot by method
**Notes:** [~3] TALK: promise the relay — teams' *isolation trees* are graded, not guesses. TRAN: installation.

## S3 · Trusted sources
- Official stores/vendor sites · the cost of 'free' installers
**Notes:** [~8] TALK: bundleware economics in one minute; the source decides most risk. ASK: "Where do you *actually* download from — honestly?" MISC: "any download site is fine" — bundled installers are the classic trap. TRAN: "The permission conversation."

## S4 · Permissions: read before you click
- A 10-second habit · one suspicious-permission example
**Notes:** [~8] TALK: the flashlight-app-demanding-contacts example (guide tip); permission lists are *claims* about behaviour. ASK: "What would YOU flag on this installer?" (projected screenshot). MISC: permission fatigue/paranoia both wrong — the habit is *reading*, duration 10 seconds. TRAN: "After install."

## S5 · Updates: why they matter
- Most patches close security holes — delay is exposure
**Notes:** [~6] TALK: link forward to L29 deliberately; deliberate patching beats reactive fear both ways. ASK: "What did the last update on your machine fix — do you know?" MISC: "updates are optional nudges" — module-level warning; say the security sentence twice. TRAN: "When things break anyway."

## S6 · Patch Tuesday, one slide
- Batched patches: testing cost vs exposure window
**Notes:** [~6] TALK: the vendor's trade-off (guide's discussion prompt) — makes update cadence legible. ASK: "Would you patch-at-discovery if you were the vendor?" MISC: none. TRAN: "The method."

## S7 · Troubleshooting = isolation
- Scope → one variable → observe → repeat
**Tags:** loop diagram from the lecture page
**Notes:** [~10] TALK: the scientific method in work clothes; every loop pass is evidence. ASK: "What's wrong with changing three things at once?" (You learn nothing from success.) MISC: "restart is for amateurs" — it's diagnosis by simplification; professionals do it first. TRAN: "Watch me get it wrong, productively."

## S8 · Demo: printer offline, my story
- My two wrong paths first — then the real cause
**Notes:** [~8] TALK: the guide's demonstration; narrate the *dismissal* of each cause — modelling productive wrong paths matters more than a clean run. ASK: "Which of my wrong paths would your tree have caught first?" MISC: none. TRAN: "Your trees now."

## S9 · Activity — Troubleshooting relay (28 min)
Broken scenario per round · teams write ordered isolation steps · reveal
**Notes:** [~28] TALK: per the lecture page's activity; three rounds (print, Wi-Fi, vanishing app); grade the tree's *order and falsifiability*. ASK (between rounds): "Which step would you drop if allowed only three?" MISC: guess-first teams — require written steps *before* the reveal. TROUBLE: silence after a round — run the first round collectively on the board as a model. TRAN: "When your tree fails: ask for help."

## S10 · Asking for help effectively
- Context · expected · observed · exact message
**Notes:** [~6] TALK: the four-part template (guide's board plan); "exact message" means screenshot. ASK: "What's the difference between 'it doesn't work' and a report fixed in one reply?" MISC: none. TRAN: "Check the method."

## S11 · Quick check
1. First two isolation questions for any fault.
2. Why updates matter — security terms.
3. One danger sign in a permission list.
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q1 — "restart" is a step, not a *question*; the questions are scope (others affected?) and change (what changed?). TRAN: "Summary."

## S12 · Summary
- Install safely · patch deliberately · isolate methodically · ask effectively
**Notes:** [~5] TALK: exam skeleton; the method returns in every later module — name three (networks, data, AI). TRAN: exit ticket.

## S13 · Exit ticket
**Your friend's laptop: Wi-Fi 'connected, no internet'. Write your first three isolation steps in order.**
**Notes:** [~6] TALK: expected shape: scope (other devices?) → layer isolation (router vs machine) → change question. This exact scenario returns in Lab 7 — keep the slips sorted.
