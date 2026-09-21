# Problem-Solving Case Bank — Level 1: Beginner

**25 cases** · PB-101–PB-125 · The first step of the four-stage problem-solving progression: **understand** the problem before anything else. Use the [bank index](index.md) for the classroom method, the shared [rubric](index.md#9-assessment-rubric-all-levels), and discussion tips. Introductory notes point to the full method; case scenarios sit below.

**How to read a case:** the Scenario and Problem statement are what you reason from; Inputs/outputs/constraints and Available information are the boundaries; the Student task is the deliverable. Solutions live with your instructor — the learning is in your reasoning, not in a revealed answer.

---

## PB-101 · Level 1 · Which laptop for a first semester?

**Domain:** Personal computer selection · **Related lectures:** L01, L03, L08

**Scenario.** Amara is starting a data-science degree. Her budget is tight, her department lists "any recent laptop that runs a spreadsheet and a browser," and a classmate insists she needs "at least 32 GB RAM for data science."

**Problem statement.** Choose a defensible laptop *class* (not a brand) for Amara's first year, given budget pressure and her actual first-year workload.

**Stakeholders.** Amara (budget, coursework needs); her family (financing); the department (minimum requirements); course instructors (software demands).

**Inputs:** budget cap, first-year course list, classmate's claim. **Outputs:** a chosen class + justification. **Constraints:** budget cap; software must run; no purchased software assumed.

**Learning objectives.** Turn an ambiguous "which laptop?" into stated requirements; justify with workload evidence rather than marketing numbers.

**Available information.** Course pages list assignments (browser, spreadsheet, document tools); no course requires local heavy computation in year one; university labs exist for anything heavier.

**Student task.** Write a one-paragraph requirement list, the laptop class that meets it, and one sentence on what the classmate's 32 GB figure would *actually* buy Amara.

**Suggested thinking time.** 10 minutes; then pair discussion.

**Expected solution characteristics.** Requirements-first reasoning (workload → class); explicit statement that year-one workloads are light; labs named as the release valve; the 32 GB figure labelled as an assumption about future work, not a requirement now.

**Discussion questions.**

1. Whose requirement is the 32 GB claim — Amara's today, or someone's idea of her future?
2. What changes if she wins a small scholarship? (Constraint change, not requirement change.)
3. When would re-visit this decision, and what evidence would trigger it?

**Extension challenge.** Write the one-line spec you would put in a first-year advising leaflet, and what you would *not* say on it.

**References.** B&B ch. 1 (classes of machines); course L08 (requirements→recommendation).

---

## PB-102 · Level 1 · The document that won't open

**Domain:** File and backup management · **Related lectures:** L11, L15

**Scenario.** Tariq receives `results_final.docx` by chat, but his machine opens it as garbled text in a basic editor.

**Problem statement.** Explain what is most likely wrong and give a safe order of steps to open it correctly.

**Stakeholders.** Tariq (needs the results); the sender (expects him to read it); IT help desk (time).

**Inputs:** file name, wrong-app behaviour, no error message. **Outputs:** diagnosis + ordered steps. **Constraints:** do not install random software; do not alter the file.

**Learning objectives.** Reason from observable symptoms; rank hypotheses by simplicity before acting.

**Available information.** Chat apps sometimes rename or truncate; a `.docx` is a document-format file; basic editors show bytes.

**Student task.** List three hypotheses ranked by likelihood, and the safe check for each.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Simplest causes first (wrong app offered by the OS; truncated name during transfer; genuinely wrong bytes); the safe check for each is *read-only*; no reinstalling as a first move.

**Discussion questions.**

1. Which hypothesis can you eliminate without opening anything?
2. Why is "the file is corrupted" the *last* conclusion, not the first (L15's lesson)?

**Extension challenge.** Write the two-sentence chat reply to the sender that gets you a readable file fastest.

**References.** Course L11 (extensions), L15 (encoding).

---

## PB-103 · Level 1 · Storage nearly full, assignments due

**Domain:** File and backup management · **Related lectures:** L07, L08, L11

**Scenario.** Zainab's laptop warns "storage almost full" during exam week. Downloads holds duplicate lecture PDFs, phone backups, and old instal files.

**Problem statement.** Free space *safely* without risking coursework, and state a rule that prevents recurrence.

**Stakeholders.** Zainab (deadlines, data); the OS (needs free space to function); future-Zainab (who will need the archive).

**Inputs:** disk warning, folder contents (described), exam timeline. **Outputs:** a safe cleanup order + a prevention rule. **Constraints:** nothing coursework-related may be lost; no purchases.

**Learning objectives.** Distinguish volatile caches from valuable data; sequence risky actions last; connect free space to virtual memory (L07).

**Available information.** Duplicates exist in Downloads; the phone backs up to the cloud already; coursework lives in the course folder tree.

**Student task.** Produce a 5-step cleanup order (safest first) and one-line prevention rule.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Order: caches/temp → duplicates (verify before delete) → downloads already in cloud → empty trash last (recovery window); coursework folders untouched; prevention rule references the L11 convention. Bonus insight: a *full* disk slows the machine via memory pressure — link stated.

**Discussion questions.**

1. Why is "empty the trash" last rather than first?
2. What makes a cleanup step *risky*, and where does that risk rank it?

**Extension challenge.** Draft the storage-check reminder calendar entry that makes your prevention rule actually run.

**References.** Course L07 (virtual memory), L11 (3-2-1).

---

## PB-104 · Level 1 · The printer that prints half a page

**Domain:** Hardware troubleshooting · **Related lectures:** L12, L21

**Scenario.** The dorm's shared printer outputs the top half of each page, then stops. Different students, same result.

**Problem statement.** Isolate the fault: printer, driver, or the students' files?

**Stakeholders.** Dorm residents (printing deadline); the printer's owner; the help desk.

**Inputs:** symptom is consistent across users; printer model unknown; everyone prints from the same app. **Outputs:** isolation steps + the most likely fault. **Constraints:** no disassembly; no driver installs without approval.

**Learning objectives.** Apply the isolation method: change one variable, classify the fault's scope.

**Available information.** Multiple users see identical output; the app is the same; paper and ink levels unknown.

**Student task.** Write the ordered isolation steps (each with what its result would prove) and the leading hypothesis.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Scope question first ("does it fail from *every* app?"), then a second machine (or a different app) to separate file vs printer; consistent-failure evidence points at printer/driver, not files; steps are read-only/low-risk.

**Discussion questions.**

1. Why does the *same symptom across users* change your hypothesis list?
2. Which single test would eliminate the largest number of hypotheses at once?

**Extension challenge.** Rewrite your steps as a note to tape on the printer for future dorm residents.

**References.** Course L12 (troubleshooting loop).

---

## PB-105 · Level 1 · Wi-Fi shows connected, but nothing loads

**Domain:** Networking · **Related lectures:** L12, L21, L22

**Scenario.** Musa's laptop shows full Wi-Fi bars but no page loads. His roommate, on the same network, is fine.

**Problem statement.** Diagnose the layer: wireless link, local IP/DNS, or the destination?

**Stakeholders.** Musa (assignment upload); roommate (co-diagnostician); campus IT (queue length).

**Inputs:** "connected" status; roommate works; no error page. **Outputs:** layer diagnosis + ordered checks. **Constraints:** stay within your own device and account.

**Learning objectives.** Name network layers (link, IP, DNS, destination); test them in order from the bottom.

**Available information.** One machine affected; the network is shared; campus portals exist that never leave campus.

**Student task.** Give the three checks you'd run in order and what each result implies.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Bottom-up: link (can you reach the router/gateway?), DNS (does a *numeric* address work when a name fails?), destination (does another site work?); roommate-evidence narrows to the device; "connected but no DNS" is the classic cause to surface.

**Discussion questions.**

1. Why test DNS with a numeric address — what does that isolate?
2. Which layer does "full bars" actually vouch for?

**Extension challenge.** Turn your checks into a three-question flowchart a non-specialist could follow.

**References.** Course L21 (layers), L22 (DNS).

---

## PB-106 · Level 1 · A phishing-shaped message in your inbox

**Domain:** Cybersecurity and privacy · **Related lectures:** L23, L29

**Scenario.** Priya gets an SMS: "Your student account will be suspended in 2 hours. Confirm your password here: `uni-portal-verify.com`."

**Problem statement.** Decide the safe response and explain the red flags using the three-question triage.

**Stakeholders.** Priya (account, money, identity); the university IT (needs the report); the attacker (wants credentials).

**Inputs:** message text, deadline pressure, lookalike domain. **Outputs:** response decision + red-flag list. **Constraints:** nothing is clicked; the platform's report path is used.

**Learning objectives.** Apply L29's triage (domain match? urgency? verifiable out-of-band?); act through sanctioned reporting.

**Available information.** The university's real portal domain differs; IT's guidance says it never asks for passwords by message.

**Student task.** List the red flags, write the safe response (including the out-of-band check), and one sentence on *why* the padlock myth fails here.

**Suggested thinking time.** 6 minutes.

**Expected solution characteristics.** All three red flags named (domain mismatch, urgency, unverifiable sender); response = don't click, report via the platform, verify by typing the university's real address; the " HTTPS = honest" fallacy explicitly countered.

**Discussion questions.**

1. Which red flag would survive if the attacker had cloned the university's domain *perfectly*?
2. Why is "report" part of the defence, not just an administrative step?

**Extension challenge.** Write the 3-line warning you would post in your class group chat — without pasting the link itself.

**References.** CISA Secure Our World (course L29 references).

---

## PB-107 · Level 1 · Group assignment, five versions of the truth

**Domain:** Digital productivity · **Related lectures:** L11, L20

**Scenario.** A four-student team submits the wrong file: the deck named `final.pptx` was overwritten by an older draft. Three copies exist across email and a USB stick.

**Problem statement.** Recover the correct deck and redesign the team's file workflow so this cannot recur.

**Stakeholders.** Team members (grades, trust); the instructor (deadline); future teams (your workflow becomes their template).

**Inputs:** naming chaos, scattered copies, a deadline. **Outputs:** recovery plan + workflow rules. **Constraints:** the instructor accepts one submission; no new tools required.

**Learning objectives.** Apply versioning and naming conventions (L11/L20); separate *sync* from *history*.

**Available information.** Email attachments preserve sent states; the USB copy may be older; the cloud folder has version history nobody has opened.

**Student task.** Recovery order (which copy first and why) + three workflow rules with your team's names attached to roles.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Cloud version history first (richest history), then email sent-items (timestamps), USB last; rules: versioned names (`v01`…), one authoritative location, a named "owner of the final"; insight that sync would have *propagated* the mistake — history is the protection.

**Discussion questions.**

1. Which copy could be *newest* while looking least authoritative — and how do timestamps settle it?
2. Which of your three rules would have prevented, rather than merely detected, this?

**Extension challenge.** Write the 5-line "team charter" clause that encodes your rules.

**References.** Course L20 (workflows), L11 (naming).

---

## PB-108 · Level 1 · A spreadsheet of 300 students, one wrong row

**Domain:** Database and information organization · **Related lectures:** L19, L25, L26

**Scenario.** A registry export lists students; one row shows age 999, two rows are duplicates, and some names have trailing spaces that break matching.

**Problem statement.** Plan the cleaning pass: which defects first, and why does order matter?

**Stakeholders.** The registrar's office (correct exports); students (correct records); the analyst (trustworthy results).

**Inputs:** defect list (sentinel, duplicates, whitespace). **Outputs:** cleaning order + check plan. **Constraints:** original file preserved untouched.

**Learning objectives.** Apply L26's defect-species checks in a safe order; defend keeping an untouched original.

**Available information.** The export repeats monthly; duplicates are full-row copies; the 999 appears in three rows, not one.

**Student task.** Cleaning order with a one-line justification per step + the sentence you'd add to next month's export request.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Order: keep original → deduplicate (so fixes don't double) → normalize whitespace (before matching) → sentinel handling last with a *decision* (treat as missing vs verify with source); monthly-recurrence insight: fix the export, not just the file.

**Discussion questions.**

1. Why deduplicate before whitespace-normalization rather than after?
2. What is lost if you "fix" 999 by deleting the rows? (Evidence of a systematic export fault.)

**Extension challenge.** Write the two-sentence note to the registrar that prevents 999 at the source.

**References.** Course L26 (cleaning species), L25 (why constraints prevent this).

---

## PB-109 · Level 1 · The strongest password policy you can actually keep

**Domain:** Cybersecurity and privacy · **Related lectures:** L29, L30

**Scenario.** A friend's password is `University2026!` — complex-looking, reused across five sites, written in a phone note titled "passwords".

**Problem statement.** Rank the friend's three real risks and design the smallest set of habit changes that fixes the biggest one first.

**Stakeholders.** The friend (accounts, identity); the sites' other users (credential-stuffing ripple); you (the persuader).

**Inputs:** the password's properties (complex-looking, reused, recorded in notes). **Outputs:** ranked risks + minimal habit plan. **Constraints:** the plan must survive a busy exam week (adoptability).

**Learning objectives.** Apply L29's properties over theatre: uniqueness, length, manager, MFA; rank by blast radius.

**Available information.** Email is among the five sites (it resets the others); a free manager is available; MFA is offered on the email account.

**Student task.** Ranked risk list + three-step plan (smallest effective set) + the one sentence that motivates without shaming.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Blast-radius ranking: reuse first (one breach → five accounts), email-first priority stated; plan = manager adoption, email MFA, then rewrite worst two passwords; motivation sentence uses the friend's own goals; "2026 in a password" vanity flagged as complexity theatre.

**Discussion questions.**

1. Why does email MFA come before MFA on a shopping site?
2. What makes a security habit *survive* exam week — and what makes it fail?

**Extension challenge.** Turn your plan into the four-bullet "start here" card your university's help desk could hand out.

**References.** CISA Secure Our World; NIST SP 800-63B (course L29 references).

---

## PB-110 · Level 1 · Two-factor code arrives unrequested

**Domain:** Cybersecurity and privacy · **Related lectures:** L29

**Scenario.** Danil receives an MFA code on his phone at 3 a.m. He did not try to log in.

**Problem statement.** Interpret the event, choose tonight's actions, and decide tomorrow's.

**Stakeholders.** Danil (accounts); the unknown actor; the service provider (abuse team).

**Inputs:** one unrequested code; the hour; no other symptoms. **Outputs:** interpretation + immediate/next-day actions. **Constraints:** do not panic-delete accounts; evidence preserved for reports.

**Learning objectives.** Reason about what an MFA code *proves* (someone has the password — the first factor); respond proportionately.

**Available information.** The code is single-use and expires; the account offers "sign out of all devices"; a password change requires the old password.

**Student task.** The interpretation (what happened, most likely), tonight's two actions, tomorrow's two, and one sentence on why the code *saved* him.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Interpretation: someone used a stolen/ guessed password — MFA stopped them; tonight: change that password (from a trusted device), sign out all sessions; tomorrow: check recovery options and enable manager-generated unique password; the "code saved you" sentence is the MFA thesis.

**Discussion questions.**

1. What would the same event mean if he had *no* MFA — and would he even know?
2. Which is the bigger lesson: this code, or the reused password that probably caused it?

**Extension challenge.** Write the 2-sentence text you would send the friend from PB-109 after this experience.

**References.** CISA Secure Our World (MFA guidance).

---

## PB-111 · Level 1 · The group chat rumour about the portal outage

**Domain:** Digital citizenship · **Related lectures:** L23, L28

**Scenario.** "Portal is down for everyone, reset your password NOW!!!" spreads in a 200-member class group, with a link. Nobody knows who sent it first.

**Problem statement.** Decide what to do before sharing or acting, and design the group's norm for next time.

**Stakeholders.** Group members (accounts); the original poster (unknown intent); the university (real status page).

**Inputs:** anonymous origin, urgency, a link, a fear hook. **Outputs:** your action + a group norm. **Constraints:** verify without spreading further.

**Learning objectives.** Apply L23's credibility criteria under social pressure; design a citizenship norm.

**Available information.** The university runs an official status page; IT never asks for passwords via chat; forwarding adds reach regardless of intent.

**Student task.** Your three-step response (verify, decide, if-warn-then-how) + one written group norm.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Verify at the official status page (typed, not the shared link); sharing decision separated from belief ("I don't know" is a valid verdict); norm = "status-page links only, no password requests ever, origin-check before reposting"; urgency noted as the manipulation vector.

**Discussion questions.**

1. Which credibility criterion (L23) fails hardest here — authority, evidence, currency, or purpose?
2. Why does *forwarding with a warning* still spread harm?

**Extension challenge.** Rewrite the rumour as a *safe* message that warns without the link.

**References.** Course L23 (criteria), L30 (citizenship).

---

## PB-112 · Level 1 · Choosing where the year's work lives

**Domain:** File and backup management · **Related lectures:** L11, L24

**Scenario.** A first-year keeps coursework on the desktop of a shared family laptop, "because it's always right there."

**Problem statement.** Redesign where (and how many copies of) the work lives, using the 3-2-1 rule, given the sharing and risk realities.

**Stakeholders.** The student (grades); family members (shared machine); the university (submission integrity).

**Inputs:** shared device, desktop habit, cloud option available. **Outputs:** storage design + sharing rules. **Constraints:** zero budget; family must not be locked out.

**Learning objectives.** Apply 3-2-1 concretely; separate *access convenience* from *durability*.

**Available information.** The laptop is old; the family shares one login; free cloud storage suffices for documents; the university LMS keeps submissions.

**Student task.** The storage design (locations, what goes where) + two rules that keep family peace.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Design: dedicated cloud folder (offsite copy #3) + local course tree (copy #1) + monthly external/export copy (copy #2); desktop demoted to a *shortcut*, not storage; rules: separate folder family may see, no password-in-note; insight: LMS submissions are a partial backup with a deadline blind spot.

**Discussion questions.**

1. Which of your three copies dies with the laptop — and does that break 3-2-1?
2. Why is a shortcut-on-desktop different from desktop storage in risk terms?

**Extension challenge.** Write the one-line status footer for your folder ("last verified backup: …") and say what would make you trust it.

**References.** Course L11 (3-2-1), L24 (sync ≠ backup).

---

## PB-113 · Level 1 · The free app that wants everything

**Domain:** Cybersecurity and privacy · **Related lectures:** L12, L30

**Scenario.** A photo-collage app requests contacts, location, microphone, and file access — on install, all at once.

**Problem statement.** Decide which permissions to grant, which to refuse, and how to tell the difference.

**Stakeholders.** The student (privacy, function); the app vendor (data appetite); contacts (who never consented).

**Inputs:** permission list, app's stated purpose (collages). **Outputs:** grant/deny decisions + a rule. **Constraints:** app must still be usable for its stated job.

**Learning objectives.** Apply purpose-limitation (L30) and least privilege at personal scale.

**Available information.** Collage-making needs files/photos only; contacts appear in the app's social features; OS allows per-permission grants.

**Student task.** Grant/refuse table with one-line justification per permission + your general rule.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Files/photos: grant (core purpose); location: refuse (no purpose stated); microphone: refuse; contacts: refuse or grant-with-alternative (social feature ≠ core purpose); rule = "purpose first, refusal reversible"; contacts-as-third-parties insight noted.

**Discussion questions.**

1. Which permission risks *other people's* privacy, not just yours?
2. Why is "refuse now, grant later" usually better than the reverse?

**Extension challenge.** Write the app-store review you'd leave after a year of using it with minimal permissions.

**References.** Course L30 (purpose limitation, minimization).

---

## PB-114 · Level 1 · Reading a laptop ad like an examiner

**Domain:** Personal computer selection · **Related lectures:** L06, L07, L08

**Scenario.** An ad headline: "16 GB RAM! Blazing i7! Huge 2 TB HDD!" — the price is suspiciously low.

**Problem statement.** Identify what the ad *emphasizes* vs what it hides, and name the two questions that reveal the catch.

**Stakeholders.** The buyer (value); the vendor (sales); the reviewer (truth).

**Inputs:** the three headline specs; price signal. **Outputs:** hidden-spec list + two killer questions. **Constraints:** no purchase needed; reasoning from the ad alone.

**Learning objectives.** Apply L06–L08: cache/SSD/storage-type awareness; spot omission as a persuasion device.

**Available information.** Ads lead with RAM size and CPU family; storage *type* and screen/battery are commonly omitted; suspicious price = older parts.

**Student task.** The likely-hidden list (three items) + your two questions + one sentence on why "2 TB HDD" is a warning sign, not a feature.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Hidden list: storage *type* (HDD not SSD — the catch), screen quality/battery, CPU *generation* ("i7" ≠ new i7); questions: "SSD or HDD?" and "which CPU generation?"; HDD-as-warning insight ties to L07/L08 access-time reasoning.

**Discussion questions.**

1. Why lead with RAM instead of storage type — what does the ordering do?
2. Which hidden item most affects *daily feel* for a first-year?

**Extension challenge.** Rewrite the ad honestly — same product, no lies, one line.

**References.** Course L06 (specs), L08 (storage types).

---

## PB-115 · Level 1 · One shared email for a five-person club

**Domain:** Small business ICT / University administration · **Related lectures:** L09, L11, L20

**Scenario.** The robotics club shares one login: `robotics-club@…`. Password is passed by chat; the treasurer's messages are indistinguishable from anyone's.

**Problem statement.** Redesign access so the club is functional, accountable, and secure — with zero budget and officer turnover each year.

**Stakeholders.** Club members; the university's IT policy (account rules); next year's officers (handover).

**Inputs:** shared credential, chat password-passing, annual turnover. **Outputs:** access design + handover procedure. **Constraints:** no paid tools; university policy limits account types.

**Learning objectives.** Connect shared credentials to accountability and security failures; design role-based access at club scale.

**Available information.** The platform offers delegation/alias features; officers are president, treasurer, secretary; chat history is searchable.

**Student task.** The access design (who gets what kind of access) + a 4-step handover ritual.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Design: keep the club address as an *alias/brand*, delegate to role-holders' own accounts (named individuals = accountability), MFA per person; handover: remove leaver, add successor, rotate the alias password, document in a one-pager; chat password-passing eliminated as a category.

**Discussion questions.**

1. What does "who sent this?" become when five people share one login — and why does that matter in a dispute?
2. Which single handover step most reduces risk after graduation scatters the officers?

**Extension challenge.** Draft the club-constitution clause (three sentences) that makes your design permanent.

**References.** Course L09 (licensing/accounts), L29 (least privilege).

---

## PB-116 · Level 1 · The exam-results screenshot asked for by "the department"

**Domain:** Digital citizenship · **Related lectures:** L23, L29, L30

**Scenario.** A classmate DMs: "Send a screenshot of your results portal — the department is collecting averages." No official announcement exists.

**Problem statement.** Decide what to share, what to verify first, and what the *classmates'* data rights are in your screenshot.

**Stakeholders.** You (your data); classmates visible in the screenshot (their data); the department (may not exist as claimed).

**Inputs:** DM origin, no official notice, portal shows others' group-work names. **Outputs:** sharing decision + verification step + redaction rule. **Constraints:** screenshots are hard to un-share.

**Learning objectives.** Apply purpose-limitation and minimization to *sharing*, not just collecting; verify authority before disclosure.

**Available information.** The portal displays group members' names; screenshots carry metadata and reach beyond recipients; official channels exist for genuine surveys.

**Student task.** The decision + the verification step + what you would redact and why.

**Suggested thinking time.** 6 minutes.

**Expected solution characteristics.** Verify authority first (department announcement via official channel); default: don't share grades privately; redaction rule: any non-consenting person's data (names, IDs) is cropped; "screenshots outlive context" insight stated.

**Discussion questions.**

1. Why does *your* consent not cover classmates visible in your screenshot?
2. Which is riskier: sharing your own grade, or the screenshot that includes others — and why the asymmetry?

**Extension challenge.** Write the group-chat reply that declines helpfully and points to the official route.

**References.** Course L30 (consent, minimization).

---

## PB-117 · Level 1 · The presentation that fails on the hall's computer

**Domain:** Digital productivity · **Related lectures:** L20

**Scenario.** A team's slides render perfectly on their laptop and terribly on the lecture-hall machine: fonts substituted, videos won't play, and two slides overflow.

**Problem statement.** Plan the fix before their presentation slot tomorrow, and the habit that prevents a repeat.

**Stakeholders.** The team (grade, nerves); the audience (readability); the hall's technician (queue).

**Inputs:** symptom list (fonts, video, overflow); time pressure; hall machine restrictions. **Outputs:** tonight's fix plan + a portable-deck habit. **Constraints:** no admin rights on the hall machine; no purchases.

**Learning objectives.** Apply L20's contrast/hierarchy/one-message principles plus portability practices.

**Available information.** The hall machine has standard office software and PDF reader; no internet for codec downloads; rehearsal room available.

**Student task.** Tonight's fix list (ordered) + the two-item habit for every future talk.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Fixes: embed/convert media (or re-encode to a standard codec), embed fonts or switch to universally available ones, export a PDF fallback, re-test overflow with the hall's aspect ratio; habits: "export PDF twin" + "test on a non-own machine"; the PDF-fallback insight is the robust core.

**Discussion questions.**

1. Why does *rehearsal on the actual machine* beat any checklist item?
2. Which fix is a workaround, and which is a root-cause repair — and when is a workaround the right call?

**Extension challenge.** Write the pre-talk checklist card (five ticks) the technician would endorse.

**References.** Course L20 (design principles, accessibility).

---

## PB-118 · Level 1 · The group project that divides the work badly

**Domain:** University administration / Digital productivity · **Related lectures:** L31, L20

**Scenario.** Four students split a project "by chapter" — then discover every chapter needs the same missing dataset, and two members finish a week early while two stall.

**Problem statement.** Re-plan the decomposition so the parts actually fit, and give the stalled pair a path.

**Stakeholders.** The four members (grades, fairness); the instructor (milestones); the dataset's provider (access rules).

**Inputs:** chapter-split failure, one shared dependency, unequal progress. **Outputs:** re-decomposition + dependency plan. **Constraints:** deadline unchanged; skills vary.

**Learning objectives.** Apply L31's decomposition honestly: dependencies before divisions; abstraction to hide skill gaps.

**Available information.** The dataset needs one person-hours' cleaning (L26 skills); chapters share formatting conventions; milestones exist.

**Student task.** The re-plan (who does what, in what order) + the one dependency you'd surface to the instructor.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Re-plan: dataset work becomes a shared first deliverable (one owner, others review) *before* chapter splits; stalled pair absorbs cleaning+charts (skill-matched); dependency surfaced to instructor with a mitigation plan; insight: chapter-splits are output-splits, not *work*-splits.

**Discussion questions.**

1. Why do dependency-blind splits always surface *late* rather than early?
2. Which member's skills were mis-assigned first, and by what evidence?

**Extension challenge.** Draw the 5-box dependency diagram you'd have drawn on day one.

**References.** Course L31 (decomposition), L20 (workflows).

---

## PB-119 · Level 1 · The USB stick from a friend

**Domain:** Cybersecurity and privacy · **Related lectures:** L12, L29

**Scenario.** A friend lends a USB stick with course notes. On insertion, your machine asks to run an "installer" stored on it.

**Problem statement.** Decide what to do — and what that request itself tells you.

**Problem note.** The mere *offer to run* a program from removable media is information: notes are documents, not installers.

**Stakeholders.** You (machine, accounts); the friend (whose stick may be infected without their knowledge); the class (if malware spreads).

**Inputs:** unexpected installer prompt; friend's clean intent; your protections. **Outputs:** decision + friend-advice + report path. **Constraints:** no execution; no accusations.

**Learning objectives.** Apply least privilege and the authorized-boundary mindset; treat anomalies as evidence.

**Available information.** Documents don't need installers; the OS offers scan-before-open; campus IT accepts suspicious-media reports.

**Student task.** Your action sequence (scan? open? report?) + the two-sentence message to the friend.

**Suggested thinking time.** 6 minutes.

**Expected solution characteristics.** Sequence: do not run; scan; open only documents (not executables); consider reporting if something executable is hidden; friend-message is blame-free and instructive ("your stick may be infected — here's how to clean it"); the anomaly-as-evidence reasoning is explicit.

**Discussion questions.**

1. Why is the friend more likely a victim than a threat — and how does your message reflect that?
2. What would make you *report* rather than just decline?

**Extension challenge.** Write the three-line "how to hand out notes safely" rule for your class group.

**References.** Course L29 (malware, social engineering adjacent).

---

## PB-120 · Level 1 · The professor's handwritten diagrams, digitized badly

**Domain:** Digital productivity / Accessibility · **Related lectures:** L16, L20, L28

**Scenario.** A lecturer photographs whiteboard diagrams and shares blurry JPGs. Students who rely on screen readers get nothing; everyone gets unreadable images before exams.

**Problem statement.** Propose the lecturer-side and student-side fixes that make the material accessible and exam-ready.

**Stakeholders.** Students (incl. screen-reader users); the lecturer (workload); the accessibility office (standards).

**Inputs:** current practice (photos); standard tools; the L20 alt-text principle. **Outputs:** two-sided fix + the minimal-change version for a busy lecturer. **Constraints:** lecturer time is scarce; no new mandatory software.

**Learning objectives.** Apply accessibility-as-design (alt text, structure); balance ideal against adoptable.

**Available information.** The diagrams are mostly flowcharts and labelled sketches; students already take notes; the LMS supports text.

**Student task.** The lecturer-side minimal fix + the student-side immediate fix + one sentence on why "the image says it all" fails.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Minimal lecturer fix: a 3-line text description posted beside each photo (meaning, not decoration — L20); better fix: re-draw as simple diagrams with real text; student fix: collaborative text-transcription rota pre-exams; the screen-reader failure is named as a *structural* omission, not a user problem.

**Discussion questions.**

1. Whose responsibility is accessibility when the tool makes it easy to skip — and what does L20's "habit" framing say?
2. Which fix survives the lecturer's busiest week, and why design for that week?

**Extension challenge.** Write the 3-line alt-text for one of your own lecture sketches.

**References.** WCAG 2.1 (course references), L20 (alt text).

---

## PB-121 · Level 1 · Two cloud drives, one "current" file

**Domain:** Cloud computing · **Related lectures:** L20, L24

**Scenario.** A student saves coursework to two cloud drives "for safety," edits on both at different times, and now neither copy matches the submitted one.

**Problem statement.** Reconcile the copies and design a single-authority arrangement that keeps the safety benefit.

**Stakeholders.** The student (grades); any collaborator; the submission record.

**Inputs:** two drives, divergent versions, one submission. **Outputs:** reconciliation order + authority design. **Constraints:** keep redundancy without divergence.

**Learning objectives.** Distinguish backup (copies with history) from dual-master editing; design one authoritative source.

**Available information.** The LMS holds the submitted version (with timestamp); both drives keep version histories; edits are self-contained documents.

**Student task.** Reconciliation order (newest-truth discovery) + the design that prevents recurrence.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Reconciliation: LMS submission = ground truth anchor → drive version histories → manual diff of remaining deltas; design: one *authoritative* drive, the second demoted to scheduled backup (one-way), version history as the safety net; the "safety without divergence" principle stated.

**Discussion questions.**

1. Why does "save everywhere" create *more* risk than "one place, backed up"?
2. Which artifact — submission record, drive A, or drive B — wins a timestamp tie, and why?

**Extension challenge.** Draw the one-way backup arrow diagram for your own coursework.

**References.** Course L20 (versioning), L24 (sync semantics).

---

## PB-122 · Level 1 · The calendar that double-books every week

**Domain:** Digital productivity / University administration · **Related lectures:** L20, L31

**Scenario.** A student's phone and laptop calendars both sync to the university account — but events created offline duplicate on merge, and lab sessions appear twice weekly.

**Problem statement.** Diagnose the duplication mechanism and design the minimal fix.

**Stakeholders.** The student (missed classes?); lab partners (who arrive at the wrong time); the calendar service.

**Inputs:** two-device setup; duplicate pattern (lab only); offline creation habit. **Outputs:** mechanism explanation + fix. **Constraints:** keep offline capture (that's when ideas happen).

**Learning objectives.** Reason about sync conflicts as a systems problem; minimal-intervention fixes.

**Available information.** Duplicates affect only events created offline; the lab schedule also exists on the university's own calendar feed.

**Student task.** The diagnosis (why labs only) + the two-step fix + the rule for offline events.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Diagnosis: offline-created events sync as *new* items rather than updates (no shared identity), and lab sessions are the ones created offline on the phone; fix: subscribe to the university's lab feed instead of re-creating events; rule: offline events go in one designated calendar that syncs first; the "identity vs copy" insight is the systems lesson.

**Discussion questions.**

1. Why do *manually recreated* events duplicate while *edited* ones mostly don't?
2. Which fix removes the cause rather than the symptom?

**Extension challenge.** Write the 3-step "new semester calendar setup" recipe.

**References.** Course L20 (workflows), L24 (sync).

---

## PB-123 · Level 1 · The lab machine that logs you out every 30 minutes

**Domain:** Operating systems / University administration · **Related lectures:** L10, L11, L20

**Scenario.** University lab PCs auto-logout after 30 minutes of "inactivity," deleting unsaved work. A student loses a lab report draft twice.

**Problem statement.** Design the student-side defense (and one policy suggestion) given that the timeout is a security control.

**Stakeholders.** Students (work loss); lab security (why the timeout exists); instructors (submission integrity).

**Inputs:** 30-minute timeout; unsaved-work pattern; the control's purpose. **Outputs:** workflow defense + one proportionate policy suggestion. **Constraints:** cannot change lab policy; no circumvention allowed.

**Learning objectives.** Respect security controls while designing around constraints; autosave/versioning habits.

**Available information.** The lab image includes office autosave; cloud drafts version automatically; logout is on *input* inactivity, not file activity.

**Student task.** The workflow defense (three habits) + the policy suggestion with its trade-off stated.

**Suggested thinking time.** 8 minutes.

**Expected solution characteristics.** Defense: cloud-first drafting (versions persist across logouts), save+export every 15 minutes, compose on personal device and use lab machines for submission-only; policy suggestion: extend timeout for machines with unsaved documents *or* a warning dialog — trade-off stated (convenience vs abandoned-session security); circumvention explicitly rejected.

**Discussion questions.**

1. What attack does the 30-minute logout mitigate — and does that threat exist in your bedroom?
2. Why is "keep typing to stay alive" the wrong lesson to teach freshers?

**Extension challenge.** Draft the two-sentence proposal you'd email to the lab manager.

**References.** Course L10 (sessions), L29 (controls).

---

## PB-124 · Level 1 · The app update that arrived during the demo

**Domain:** Operating systems · **Related lectures:** L12

**Scenario.** Mid-presentation, the demo laptop pops "Restart required to finish installing updates." The demo has four minutes left.

**Problem statement.** Choose the in-the-moment response and the preparation habit that makes the moment impossible next time.

**Stakeholders.** The presenter (credibility); the audience (time); IT policy (patch compliance).

**Inputs:** update pending; no admin rights; a deadline. **Outputs:** now-response + future habit. **Constraints:** postpone, never disable updates.

**Learning objectives.** Separate emergency handling from prevention; respect patch discipline (L12/L29).

**Available information.** OS allows a postpone; the demo file is saved and exportable; a second device is in the bag.

**Student task.** The now-response (two options ranked) + the prevention habit + one sentence on why "never update" is the wrong lesson.

**Suggested thinking time.** 6 minutes.

**Expected solution characteristics.** Now: postpone (least disruptive) and switch to the PDF twin (L20's habit) if the demo machine fights back; prevention: patch *before* travel, presentation-machine checklist; the "updates are security" sentence ties to L29 — the lesson is scheduling, not avoidance.

**Discussion questions.**

1. Why is the PDF twin the professional's escape hatch, not a sign of failure?
2. What does "postpone" have to mean about *when*, for it not to become "never"?

**Extension challenge.** Write the three-item pre-presentation patch ritual.

**References.** Course L12 (updates), L20 (portable decks).

---

## PB-125 · Level 1 · The dataset with three spellings of "Cairo"

**Domain:** Data science workflows · **Related lectures:** L15, L26

**Scenario.** A class survey exports 200 rows where the city field reads `Cairo`, `cairo`, and `CAIRO` — and one row says `Kayro`.

**Problem statement.** Plan the normalization: what to standardize, what to verify, and what to never assume.

**Stakeholders.** The class (survey results); the analyst (you); the respondent who typed `Kayro` (a real person's answer).

**Inputs:** the variant list; unknown ground truth for `Kayro`; the survey's purpose. **Outputs:** normalization plan + verification step. **Constraints:** preserve the original; don't fabricate certainty.

**Learning objectives.** Apply L26 cleaning with L15's encoding awareness; separate normalization from *guessing*.

**Available information.** Case variants are safe to merge; `Kayro` could be a typo *or* a different place; the survey allows re-contact via anonymized re-survey.

**Student task.** The plan (which merges are safe, which need verification) + the sentence that reports `Kayro` honestly.

**Suggested thinking time.** 10 minutes.

**Expected solution characteristics.** Safe: case-normalization (`Cairo`/`cairo`/`CAIRO` → `Cairo`) with the original preserved; `Kayro`: not safely mergeable — flag as unknown/verify, report as its own category with a count, never silently "corrected"; the honesty sentence: "1 response ('Kayro') was not confidently matched and is reported separately."

**Discussion questions.**

1. What makes case-merging safe but spelling-merging unsafe — name the property.
2. What does silently "fixing" `Kayro` do to your results' trustworthiness?

**Extension challenge.** Write the survey-form change (one line) that prevents the whole problem next year.

**References.** Course L26 (cleaning), L15 (encoding adjacent).
