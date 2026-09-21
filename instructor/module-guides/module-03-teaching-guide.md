# Teaching Guide — Module 3: Software and Operating Systems

**Module 3** · Stage 2 · 4 lectures (L09–L12) · 8 contact hours
Companion to lecture pages `L09`–`L12` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] Lab 3 (file-system scavenger hunt) launches at L11: prepare the hunt checklist and confirm the lab machines' OS mix (the handout is platform-neutral).
- [ ] L10's dual-interface race needs a working CLI on the projector machine *before class*: test terminal + one file operation.
- [ ] L12's troubleshooting relay uses three broken-scenario slides; prepare a real "can't print" story of your own — authenticity sells the method.
- [ ] Keep one installer package (from a trusted vendor) ready for L12's walkthrough screenshot.

## Misconception warnings (module level)

1. **"The operating system is the thing with windows."** GUI is one interface to the OS; the kernel's five jobs are the substance. L10 exists for this.
2. **"Free software = worthless."** The licensing segment must separate *price* from *freedom*; the word "free" carries both meanings in English — say which you mean each time.
3. **"Installation is a double-click."** Permissions, sources, and post-install verification are the professional habit; L12's relay drills it.
4. **"Files live 'in the cloud or in the computer'."** Files live in *file systems*; cloud sync is a (Module 6) replication service — keep L11's tree model primary.

---

## L09 — The Software Landscape

**Teaching tips:**
- Open with the stack picture *upside down*: draw hardware at top and applications at bottom, then ask "what separates your essay from the transistors?" Every layer students invent themselves is a layer they'll keep.
- The "software autopsy" activity needs each student near a machine; pairs without one should autopsy a phone app instead — the classification transfers.
- Firmware: one slide, one story (printer or router update), resistance to over-teaching. It returns naturally in L12's update segment.

**Board / projector plan:**
- [Board] The four-layer stack (hardware → OS → utilities/drivers → applications) drawn once and annotated all lecture; keep it visible.
- [Slide] Licensing-model comparison (proprietary / free & open-source / freemium / trial) as a 2×2: price vs freedom.
- [Board] Three-column board: system / application / not-software, for the autopsy debrief.

**Suggested demonstration:** Open the About/license panel of one proprietary tool and one open-source tool side by side; show where each names its license and what the license permits.

**Misconception warnings:**
- "Apps are software but the OS is 'the computer'." Force every scenario through the stack: naming the layer is the assessment skill.
- "Open-source means unsupported/insecure." Point to published-maintenance practice as the real signal, not price.
- "Drivers are applications." They're the OS's translators for specific hardware — a utility/driver-layer concept, not end-user software.

**Discussion prompts:**
1. Your bank's app: name the layers between your fingerprint and the server.
2. When is freemium the *right* model for a student, and when is it a trap?
3. Why does firmware still exist when everything else moved to apps?

**Exit-ticket questions (with answers):**
1. *Classify: driver, spreadsheet, OS, backup utility.* — Driver = system (utility/driver layer); spreadsheet = application; OS = system; backup utility = utility (system software).
2. *One practical difference between proprietary and open-source licensing for you.* — Source availability/modification rights vs vendor license terms (any concrete difference, stated plainly).
3. *Why is firmware firmware?* — It's software stored on/in the device it operates, low-level and device-specific.
4. *Where does a mobile OS sit in the stack, and what runs on it?* — System software layer; applications run on it, mediated by its services.

---

## L10 — Operating System Fundamentals

**Teaching tips:**
- The five responsibilities deserve one memorable label each (processes = traffic police, memory = hotel manager, devices = translators, files = librarian, UI = front desk). Labels are scaffolding — retire them once students use the real terms.
- Boot: teach it as a *story in five beats* (power → firmware self-test → bootloader → kernel loads → login). The beats structure, not the vendor names, is what transfers.
- Dual-interface race: cap it at five operations and enforce time-keeping; the data (GUI vs CLI times) is the discussion fuel.

**Board / projector plan:**
- [Board] Five responsibility boxes; each gains its label and one example command/screenshot as the lecture proceeds.
- [Board] Boot timeline as a horizontal line with five beats; students place "virus scan starts" and "Wi-Fi joins" on it.
- [Slide] Same file listing in GUI and CLI, side by side.

**Suggested demonstration:** Live terminal: `mkdir`, `cd`, `cp`, `del`/`rm`, `tasklist`/`ps` — five commands, one per responsibility where possible; deliberately mistype one and read the error message aloud as *evidence*.

**Misconception warnings:**
- "Deleting a file deletes the data." The OS marks space free; content persists until overwritten — links to L11's backups and L30's privacy.
- "CLI is obsolete." It's the automation and remote-administration surface; the race data shows which tasks it wins.
- "Multitasking = the CPU runs everything at once." Scheduling shares the CPU in slices; perception of simultaneity is the design goal.

**Discussion prompts:**
1. Where in the five responsibilities does "Wi-Fi connected but no internet" fall? (Device management — a driver/network configuration question.)
2. Which boot beat fails if a key is stuck on the keyboard? (Firmware self-test, sometimes.) Which if the disk is dead? (Kernel load.)
3. Why do servers run headless (no GUI)?

**Exit-ticket questions (with answers):**
1. *Name the OS's five core responsibilities.* — Process, memory, device, and file management; user interface.
2. *Second boot beat in order and its job.* — Firmware self-test (POST): verifies essential hardware before loading anything.
3. *CLI won which race operation, and why?* — Bulk/repeatable file operations (renames, moves, filters): scriptable, precise, fast.
4. *What does "kernel" mean in one sentence?* — The OS core that runs privileged, managing the five responsibilities above the hardware.

---

## L11 — File Systems and File Management

**Teaching tips:**
- Paths are this module's grammar; drill absolute-vs-relative until students can *construct*, not just recognize. The three-OS comparison table on the lecture page is the projection anchor.
- The scavenger hunt (Lab 3) starts today — launch it *after* the naming-convention segment so the hunt immediately enforces the convention.
- 3-2-1: make students write *their own* three locations before showing the canonical diagram; the gap between their answer and the rule is the learning moment.

**Board / projector plan:**
- [Board] A file tree drawn as a real tree; two students walk to "leaves" as absolute and relative paths are read aloud.
- [Slide] Same path on Windows / macOS / Linux (the lecture page's table).
- [Board] 3-2-1 drawn as three boxes with arrows labelled "different device" and "different place."

**Suggested demonstration:** Rename one badly named file live (`Doc2 (3) final FINAL.docx` → convention) while narrating the convention check; then show the same file's properties panel for extensions/metadata.

**Misconception warnings:**
- "The desktop is a filing system." It's a folder like any other; conventions beat desktop-piles (gently — many instructors share this habit).
- "Extensions are decoration." They drive OS behaviour and safety checks; hiding them (defaults!) hides evidence.
- "One backup = backed up." A copy on the same disk dies with the disk; the rule's "different device, different place" is the point.

**Discussion prompts:**
1. What breaks first in a shared team drive with no naming convention? (Trust in search; then duplicates; then correctness.)
2. Why do cloud-sync services not satisfy 3-2-1 alone? (Same account/place, sync not backup — deletions propagate.)
3. Which metadata would embarrass you in a submitted document? (Author history, tracked changes — bridge to L19.)

**Exit-ticket questions (with answers):**
1. *Absolute vs relative path, one sentence each.* — Absolute: full address from the root; relative: from the current working directory.
2. *Windows root vs macOS/Linux root notation.* — `C:\` (drive-letter) vs `/` (single tree).
3. *3-2-1 in the rule's own numbers.* — 3 copies, 2 different media/devices, 1 off-site.
4. *Why does a .exe renamed to .jpg not become a picture?* — Extension is a name hint, not the content; format lives in the bytes (preview of L16).

---

## L12 — Installing, Updating, Troubleshooting

**Teaching tips:**
- The troubleshooting relay is the module's capstone assessment-style activity; grade the *isolation tree*, not the guess. Teams must write steps as ordered, falsifiable checks.
- Permission fatigue is real: teach "read before you click" as a 10-second habit, not paranoia. Name a legitimate-sounding permission that should trigger suspicion (a flashlight app demanding contacts).
- End the module with the help-request template: effective help-seeking is a graded professional skill and it previews the project's milestone write-ups.

**Board / projector plan:**
- [Board] Troubleshooting tree template: Symptom → (does it affect others? → scope) → one-variable check → repeat.
- [Slide] Installer screenshot with permissions panel highlighted.
- [Board] The four-part help-request template: context, expected, observed, exact message.

**Suggested demonstration:** Walk one real troubleshooting scenario end-to-end on the projector (e.g., printer offline): narrate the isolation steps *as you dismiss each cause*, including the two you got wrong first — modelling productive wrong paths matters more than a clean run.

**Misconception warnings:**
- "Restarting is for amateurs." It clears state across all five OS responsibilities; it's diagnosis by simplification, and professionals do it first.
- "Updates are optional nudges." Most patch security holes; delay is exposure — link forward to L29's patching habit.
- "The error message is noise." Exact text (screenshot!) is the single most diagnostic artefact; vague reports get vague help.

**Discussion prompts:**
1. Why do vendors ship Patch Tuesday batches rather than patch-at-discovery? (Testing/regression cost — and what that trade-off means for users.)
2. An app asks for your location "to serve you better." Apply today's method: what would you check before allowing?
3. What's the difference between "it doesn't work" and a report that gets fixed in one reply?

**Exit-ticket questions (with answers):**
1. *First two isolation questions for any software fault.* — Does it affect others/other accounts? Did anything change (update, install, settings) before it started?
2. *Why updates matter, in security terms.* — They patch known vulnerabilities; unpatched software is the easiest attack surface (L29 link).
3. *One danger sign in an installer's permission list.* — Permissions unrelated to the stated function (accept reasoned examples).
4. *Name the four parts of an effective help request.* — Context, what you expected, what you observed, exact error message/steps to reproduce.
