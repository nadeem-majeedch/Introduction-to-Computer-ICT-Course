---
case-study: CS-04
title: Ransomware Incident at a Fictional College
lecture: L29 (response drills extend to L30)
duration: 40 minutes
---

# CS-04 — Ransomware Incident at a Fictional College

> **Lecture:** L29 (extends to L30) · **Duration:** 40 min · **Format:** incident walkthrough → post-mortem → policy rewrite
> **Fictional scenario for authorized educational discussion — all names, systems, and events invented.**

## The scenario (fictional)

Monday, 08:20. Northfield College's IT helpline floods with calls: file shares show `RESTORE-FILES-HERE.txt`, every office PC's documents are encrypted, and the student-records application won't start. A note demands payment in cryptocurrency within 72 hours.

The post-incident timeline (later reconstruction):

- **Three weeks earlier:** a finance employee received a "shipping problem" email with an attachment (`INVOICE_8821.pdf.exe` — extension hidden by default). She opened it. Nothing visibly happened.
- **Two weeks earlier:** the malware spent days quietly copying credentials and mapping file shares (dwell time — no alarms existed to trip).
- **Sunday, 23:40:** mass encryption began, spreading via the file shares *and* the (unsegmented) Wi-Fi network.
- **The backups:** a NAS attached to the same network, **mapped as a drive on every PC** — encrypted along with everything else. The cloud sync account synced the *encrypted* files happily.
- **The response:** IT isolated the network within an hour; the college refused payment; **three weeks of data were restored from an offsite backup taken by a department that ignored the central IT policy**; classes continued on paper. The registrar disclosed the student-data exposure per regulation.

## Guiding questions

1. **Attack path (L29):** Identify the threat classes at each stage — the entry (which class of malware? which human failure?), the dwell, the propagation. Which *one* control at entry would have stopped everything downstream?
2. **Layer autopsy (L29):** For each defence layer — prevention, access, recovery, detection, behaviour — state what was present, what was missing, and the cheapest missing control.
3. **Backup post-mortem (L11):** Why did the "backup" fail? Map its failures onto the 3-2-1 rule (which of the three copies/two media/one offsite properties were violated?). What does "test restore" mean operationally?
4. **Response order (L29/L30):** Rank the first five actions after detection (isolate, identify patient zero, notify regulator/affected people, restore, preserve evidence) and justify the ordering trade-offs.
5. **Policy rewrite:** Produce the college's new one-page policy: five controls, each assigned to a *role* (IT, department, individual staff), each testable. Budget-brainstorm: which control is *free* (behaviour), which is cheap (configuration), which needs capital?

## Debrief

Ransomware is a *people-and-process* failure wearing a technical costume: one unauthorised execution (L29 §29.4's boundary in reverse — the attacker ignored every rule you're taught to respect) met unmapped dependencies (backups reachable from user PCs). The defence is the layered table from L29, *practised*, not posted.

## Notes for self-study

- CISA's individual guidance (updates, MFA, backups — [L29 references](../lectures/L29-cybersecurity-fundamentals.md)) maps one-to-one onto the missing controls above.
- The disclosure question belongs to [L30](../lectures/L30-privacy-digital-citizenship.md): data-protection principles make breach notification the *holder's obligation*, not a courtesy.
