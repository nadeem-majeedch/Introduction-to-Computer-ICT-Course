# Case Bank — Instructor Solutions: Level 1 (PB-101–125)

**Private.** Never publish, never paste into `docs/`. Each case: solution guide, defensible alternatives, trade-offs, common mistakes. Pair with the public *Expected solution characteristics* in `docs/case-bank/level-1.md`.

---

## PB-101 — The coursework laptop

**Solution guide.** Reframe from "best laptop" to "requirements": (1) workload = browser + documents + video calls + light IDE/data tools → any current mid-range machine suffices; (2) the binding constraints are budget and reliability, not CPU muscle; (3) decision inputs that actually matter: RAM ≥ 8 GB (16 preferred for DS tools), SSD storage, battery through a lecture day, service/warranty availability locally. Recommend a mid-range machine from a brand with local service, declining both the cheapest (battery/build) and premium (paying for GPU power the workload never uses).
**Alternatives.** Refurbished business-class machine (better build per currency unit — defensible if warranty exists); tablet+laptop trade-off rejected because IDE/data work needs a real keyboard/OS.
**Trade-offs.** Paying for headroom (future-proofing) vs budget now; local serviceability vs marginally better specs online.
**Common mistakes.** Spec-chasing (CPU benchmarks for a browser workload); ignoring service availability; treating DS requirements as generic "gaming laptop" needs; no battery criterion.

---

## PB-102 — The no-POST laptop

**Solution guide.** Sequence: power source (adapter/LED) → display (external monitor, brightness) → memory reseat (classic no-POST cause) → peripheral disconnect → final: service. The key teaching point is the *order*: cheapest, most-likely, least-invasive first; stop before anything destructive; data is on the storage device and unaffected by no-POST, which reframes the panic.
**Alternatives.** If under warranty: skip all user-side steps and claim immediately (cost of self-service ≠ 0).
**Trade-offs.** Time spent diagnosing vs warranty turn-around; risk of reseat procedure vs its diagnostic value.
**Common mistakes.** Opening the machine first; assuming display failure = total failure; ignoring the external-monitor test; forgetting AC-only test with battery removed (if removable).

---

## PB-103 — The backup plan

**Solution guide.** Map to 3-2-1: thesis (cloud + local), photos (cloud + external), code (Git remote = offsite by design, plus local). The distinctive marks: an *automated* schedule (manual backups die), and a test — "restore one file today" — because an untested backup is a hypothesis. Distinguish *sync* from *backup* explicitly (a sync service faithfully propagates deletions).
**Alternatives.** University-provided storage as the offsite copy (defensible if quota suffices).
**Trade-offs.** Cloud convenience vs privacy/cost; external drive's offline safety vs its physical co-location risk.
**Common mistakes.** Confusing sync with backup; single-copy plans; no automation; never testing restore; backing up the device but not the *photos* (the irreplaceable class).

---

## PB-104 — The shared family PC

**Solution guide.** Separation as the mechanism: standard accounts per person, admin password held by the parent, per-user document folders, shared folder for common files. Explain blast radius: a standard user's damage and malware land in their own space and require elevation to spread. Tie to L10 (user management) and L29 (least privilege).
**Alternatives.** Parent-managed family-controls tooling on top (complementary); separate machines (out of scope, cost).
**Trade-offs.** Convenience of one account vs containment; the teen's autonomy vs the parents' peace of mind.
**Common mistakes.** Admin-for-everyone "because installs"; ignoring per-user folders; treating the solution as technical-only (the family *agreement* is part of the design).

---

## PB-105 — The 3,000-word essay

**Solution guide.** Phased workflow with *separate* files/dates: research-notes file (sources with links at capture time — the reference-list cure), then an outline, then drafting in sections, then a formatting-only pass. Distinguish *content* problems from *formatting* problems (fixing both at once causes both). Timeline backward from the deadline.
**Alternatives.** Reference manager (Zotero) for source capture — recommend as an extension, don't require.
**Trade-offs.** Rigid structure vs flexibility for discovery-writing styles.
**Common mistakes.** Writing and formatting interleaved; sources captured "from memory" at 2 a.m.; no intermediate deadline plan; one giant document with no version history.

---

## PB-106 — The file-size paradox

**Solution guide.** Two mechanisms layered: (1) binary vs decimal prefixes — GiB vs GB ≈ 7% gap; (2) folder *overhead* — thousands of small files consume more space than their content bytes (block/allocation overhead). Both are L13/L14-adjacent. The tool's number can be right and still not match your expectation.
**Alternatives.** None needed; this is a mechanism case.
**Trade-offs.** Not applicable — but note the *investigation* trade-off: how long to probe before asking.
**Common mistakes.** Blaming "hidden files" without checking; stopping at the prefix explanation (the folder-overhead half is the deeper lesson); unit confusion (GB/GiB) repeated uncritically.

---

## PB-107 — The lift indicator

**Solution guide.** Truth table with three inputs (A, B, C): L = A∧B∧C. Evaluate all 8 rows; exactly one produces light. Then the fun part: row 000 means "light with nobody pressing" → fault sensor/wiring hypothesis, and the panel's *own* indicator must be excluded as a variable. The pedagogical payload: every input combination is a *state* the system must classify correctly.
**Alternatives.** Either input polarity (pressed = 1 vs unpressed = 1) — both fine if declared.
**Trade-offs.** None — but note the physical-world caveat: real panels bounce, so hardware tests edges; our abstraction is fine at this level.
**Common mistakes.** Listing only the all-true row and calling it a table; forgetting a row; treating the fault case as impossible rather than a state to explain.

---

## PB-108 — The hostel network map

**Solution guide.** Separation of concerns: each floor gets its own router (a cheap mesh or AP-per-floor), all cabled back to a single switch; one network name (SSID) so devices roam; guest isolation so residents' devices can't probe each other.ISP line → switch → APs. Label the diagram with the data path a packet takes from a resident's laptop to the internet.
**Alternatives.** Single powerful router (fails: range/walls); full mesh nodes (viable, more expensive).
**Trade-offs.** Cost vs coverage; one SSID's convenience vs interference management between APs.
**Common mistakes.** Daisy-chaining routers without switch/cabling plan; ignoring guest isolation (a security answer); diagram without the internet path; treating walls as a non-issue.

---

## PB-109 — The scholarship page

**Solution guide.** URL check first (lookalike domain? padlock ≠ legitimacy), then the *authority channel* check (does the university's own site or office list this scholarship?), then the asks: no legitimate scholarship demands fees or OTPs. The padlock point deserves its own paragraph — encryption certifies the *connection*, not the *honesty* of the other end.
**Alternatives.** Directly contacting the university's financial-aid office is the gold standard and should be stated.
**Trade-offs.** Time spent verifying vs the (small) chance it's real — cheap verification wins.
**Common mistakes.** Trusting the padlock icon; clicking the link in the message rather than typing the portal URL; ignoring the urgency-pressure signal; not reporting the page.

---

## PB-110 — The phishing email

**Solution guide.** The triage: (1) sender domain vs display name; (2) hover the link — does it match the story?; (3) the credential request itself (a bank never asks); (4) urgency as manipulation signal. Then the *response* ladder: report (per institution's process), delete, and if clicked: change the password immediately, enable MFA, watch the account. The deep lesson: phishing is social engineering — the technical signs vary, the *pressure* pattern doesn't.
**Alternatives.** Verifying via an independently sourced phone number (fine, but the report-first habit matters more).
**Trade-offs.** Time verifying vs the report button; silence vs reporting (reporting protects others).
**Common mistakes.** Reading grammar as the detector (modern phish is clean); clicking to "check" the link; replying to the sender; missing that *the attachment* is as dangerous as the link.

---

## PB-111 — The anonymous poster

**Solution guide.** Separate the act (leaking minutes) from the concern (valid), from the method (breach). Full anonymity online is weaker than intuition suggests (metadata, style, timing) — a real lesson, not a scare. Then the legitimate channels: the society's constitution likely has a complaints route; university student-affairs mediates; leaking that *does* expose wrongdoing may still be protected in some frameworks — flag that this is jurisdiction-dependent, don't resolve it.
**Alternatives.** Anonymous submission via an office (identity known to one office only); collective raising (safety in numbers).
**Trade-offs.** Anonymity's safety vs its credibility; speed of a leak vs the durability of a channel fix.
**Common mistakes.** Conflating "they can't find out" with "they can't"; skipping the constitution's own process; treating the leak as the only possible act; moralizing instead of analyzing.

---

## PB-112 — The club member list

**Solution guide.** The insight is *choice of tool = choice of guarantees*: a spreadsheet is fine until multiple editors, growing rows, and derived questions appear. Minimal fix: one table, one fact per column, unique IDs, no free-text status (use fixed values). Then the honest boundary: when multi-editor conflicts and per-member histories appear, that's L25's relational signal — a small database (or relational-shaped sheet with linked tables) becomes the right answer.
**Alternatives.** Cloud spreadsheet with edit history (defensible at this size; the constraint is discipline, not software).
**Trade-offs.** Simplicity vs integrity guarantees; migration cost vs accumulating debt.
**Common mistakes.** Designing a full database for 40 rows (over-engineering is also a mistake); keeping free-text columns; no unique member key; ignoring the *questions the sheet must answer* when designing.

---

## PB-113 — The cloud storage choice

**Solution guide.** Build a small comparison: free quota, sync-vs-backup semantics (the recurring theme), sharing controls, expiry/dormancy policies (PB-312 foreshadow), and where university-provided storage fits. The decision follows from *what's stored* (coursework: institutional first for continuity; photos: consumer cloud + local).
**Alternatives.** Any defensible split is fine — the marks are in the criteria, not the vendor.
**Trade-offs.** Free-tier limits vs subscription cost; convenience vs dormancy risk; institutional storage's continuity vs its quota.
**Common mistakes.** Picking by brand loyalty; ignoring sync-deletion semantics again (it keeps being the trap); forgetting that "free" tiers can end; storing the only copy anywhere.

---

## PB-114 — The AI study note error

**Solution guide.** The habit: verify *claims*, not vibes. Concrete loop: identify checkable claims (dates, definitions, formulas), check against the lecture page or textbook, mark unverifiable as unverifiable. Then the disclosure line and the boundary rule: AI output is a *draft to be checked*, never a source. Set the workload expectation honestly — verification takes minutes and is part of studying, not an extra.
**Alternatives.** Asking the tool for sources and checking those (good habit, but the fake-citation risk — see PB-210 — must be named).
**Trade-offs.** Speed vs reliability; using AI for *understanding* (low risk) vs for *facts* (high risk).
**Common mistakes.** Verifying only what feels wrong; trusting fluent prose; no disclosure; copying AI errors into submission work (integrity exposure, not just accuracy).

---

## PB-115 — The attendance chart

**Solution guide.** The mechanism is aggregation hiding denominators and populations: 40% of *what*? Total sessions? Distinct students? Registered members? Each gives a different honest number, and the misleading one (percentage of registered members across events they never knew about) is the most common. Redesign: state the denominator, show attendance per event or per cohort, and if comparing, compare like with like. The caption carries the definition.
**Alternatives.** Per-event bar chart (simplest honest form); cohort-normalized view if the audience needs comparison.
**Trade-offs.** Granularity (honest) vs simplicity (readable) — solvable by caption, not by choosing one.
**Common mistakes.** Percentages with unstated denominators; mixing populations; the chart's *design* implying claims the data can't support; assuming bad faith instead of asking what the rep computed.

---

## PB-116 — The update that reboots

**Solution guide.** Mechanism first: some updates patch system components that only swap on restart — the reboot is the update completing, and deferral has a security cost (patching is deliberate, L12). The tools: active hours (so reboots land at 3 a.m., not mid-essay), scheduled restart times, save discipline (autosave + cloud docs make reboots survivable).
**Alternatives.** Deferral windows (defensible if scheduled, not if indefinite — state the security trade).
**Trade-offs.** Interruption now vs unpatched exposure later; control vs automation defaults.
**Common mistakes.** Killing update services permanently (the classic over-correction); treating autosave as optional; never scheduling (so the OS chooses the worst moment).

---

## PB-117 — The forgotten password (authorized recovery)

**Solution guide.** Frame first: this is *authorized recovery on your own machine* — the exercise exists to teach recovery paths, not bypass techniques. Route by recovery order: built-in reset disk/answers → another admin account on the machine → OS-documented reset flows → cloud-account recovery where the OS ties to one → last resort: documented OS-specific reset media procedure (L12's competence includes this, safely) → recovery of *data* via live-USB copy if reset is refused. Data survives in almost every path — say so early; panic drives bad choices.
**Alternatives.** Institutional IT for university machines (the *correct* answer on managed devices — flag it).
**Trade-offs.** Speed of reset media vs its misuse risk; local admin convenience vs policy on managed machines.
**Common mistakes.** Aiming at bypass tools before exhausting documented recovery; forgetting data is separate from credentials; attempting any of this on a machine they don't own (name the line explicitly).

---

## PB-118 — The slides that die

**Solution guide.** Design *for failure*: fonts embedded or text converted to curves/images for headings; images inside the deck file (not linked); a PDF export as the universal fallback; and the 5-minute-early ritual (open, advance through slides, check projector resolution). The deep principle: the presentation must not depend on the venue's machine having your fonts, your network, or your codec.
**Alternatives.** Present from own laptop + adapter set (equally valid; the checklist still applies); cloud-deck with offline copy.
**Trade-offs.** PDF's fidelity vs lost animations (usually a fine trade; note it).
**Common mistakes.** Linking images from a local folder that isn't copied; relying on venue Wi-Fi for a video; no PDF fallback; rehearsing only on the room where it worked.

---

## PB-119 — The binary-comparison game

**Solution guide.** The mechanism, not luck: positional weight — leftmost bits dominate because each leftward position doubles all the value to its right; so any 6-digit binary beats any 5-digit binary automatically, and among equal lengths, compare from the left (first differing bit decides). Then the practice pattern: chunking into nibbles (4-bit groups → hex fluency emerges naturally), converting via powers of two rather than counting.
**Alternatives.** Hex-bridge technique (teach as the speed tool once binary comparison is understood).
**Trade-offs.** Counting-on-fingers honesty (fine for L1) vs chunking speed.
**Common mistakes.** Comparing strings left-to-right *without* the length rule; memorizing tables instead of the positional insight; decimal-size intuition smuggled into binary ("9 is bigger than 8" is true, but "1001 > 1000" needs the leftmost-bit rule).

---

## PB-120 — The data science toolkit

**Solution guide.** Sequence, not shopping list: spreadsheet fluency *first* (the honest tool for the first two years of coursework and most of life), then a notebook environment (Python + pandas via a free local or browser-based distribution) *second*, then structured-data practice (download a public dataset — the city open-data examples from the course — and answer a real question). Free-only constraint honored throughout; the course's own references list anchors tool choices.
**Alternatives.** R-first pathway (equally defensible for DS-track students; note the course's Python bias and justify).
**Trade-offs.** Depth in one tool vs breadth across many; local install vs browser-based (institution machines may block installs — the fallback is the answer).
**Common mistakes.** Starting with ML libraries before data literacy; tool-hopping; treating the toolkit as complete (data *ethics* and provenance are also toolkit — PB-314/419 foreshadowed).

---

## PB-121 — The one-handed portal

**Solution guide.** Mechanisms: hover-revealed menus (pointer-bound), small click targets, drag-only interactions, keyboard traps. Fixes: click-and-stick menus, generous targets, click alternatives for every drag, full keyboard operability. The meta-lesson: constraints like this are *design tests*, not niche accommodations — every fix above also helps touch users, and the "everyone benefits" framing is why inclusive design sticks.
**Alternatives.** Text-only fallback page (defensible as an interim, but the goal is the main path being usable).
**Trade-offs.** Visual elegance vs pointer independence — resolvable, not sacrificial, with click-and-stick patterns.
**Common mistakes.** Assuming a small user group ("someone else's problem"); fixing hover menus but leaving keyboard traps; never testing with keyboard alone (the 10-minute test that finds most of it).

---

## PB-122 — The travel photos

**Solution guide.** Strategy = redundancy + hierarchy: originals to external drive + cloud (3-2-1 honored: phone = working copy, drive = local, cloud = offsite); *selections* shared to the album; a named public set with location-stripping decision (L30: geotags reveal home patterns — the caption point). Schedule: while travelling, nightly hotel sync; after, the archive pass.
**Alternatives.** Fully public album with stripped metadata (defensible for the selection set; originals stay private).
**Trade-offs.** Sharing joy vs location/face exposure; upload cost on the road vs risk until synced.
**Common mistakes.** Phone-as-only-copy until "later"; geotags stripped from public but not from shared originals; no selection hierarchy (1000 photos dumped on classmates is a different social problem).

---

## PB-123 — The password

**Solution guide.** The passphrase pattern: length dominates, four unrelated common words beat complex-but-short; a *written* unique root kept in a physical wallet is *better* than reuse (physical theft is a different, lower-scale threat than database breaches — say this explicitly, it's counter-intuitive). Password manager as the upgrade path: one strong master passphrase, unique generated passwords everywhere, MFA on the manager. Uniqueness ≥ complexity — the insight weak answers miss.
**Alternatives.** Manager-first immediately (fine; the master passphrase still needs the passphrase rule).
**Trade-offs.** Memorability vs uniqueness (passphrases thread the needle); manager trust vs written-wallet scope.
**Common mistakes.** Site-specific "clever" transformations (Spring2026!-family patterns); treating written passwords as always-wrong; ignoring the manager's own MFA; complexity theatre over length.

---

## PB-124 — The browser profiles

**Solution guide.** Mechanism: separate profiles isolate cookies/sessions/logins — coursework profile stays logged into university tools, personal profile untouched, plus a *clean* profile for testing (the developer habit, introduced here). Practical layer: pin different themes/colors per profile so the wrong window is visually obvious.
**Alternatives.** Separate browsers per context (equally valid, heavier); container extensions (extension of the same idea, note it).
**Trade-offs.** Profile juggling vs accidental cross-contamination (the Visual Theme trick is the cheap fix).
**Common mistakes.** One profile with 30 tabs and six identities; no visual distinction between profiles; forgetting that incognito ≠ a profile (no persistence either way — different purposes).

---

## PB-125 — The navigation app

**Solution guide.** Decompose: inputs (where am I — GPS/fixed beacons indoor; where do I want to go; what constraint — step-free), processing (path search over a floor-graph; the lecture-hall specificity means the *data model* is the hard part, not the algorithm), outputs (turn list, estimated time, step-free flag). Then the honest scale-down: full GPS-indoor positioning is research-grade; the achievable L1 version is floor-map + fixed landmarks ("from the north entrance"). The teaching payload: *decomposition reveals which sub-problem is genuinely hard* — and that's the deliverable, not a working app.
**Alternatives.** QR-code checkpoints (positioning solved by infrastructure — a legitimate scope-down).
**Trade-offs.** Ambition vs semester reality; beacon infrastructure cost vs GPS-indoor inaccuracy.
**Common mistakes.** Starting with the algorithm instead of the data model; treating indoor positioning as solved; no step-free constraint in v1 (accessibility as afterthought — the exact habit PB-121 attacks); scope-blind "just build it" answers.
