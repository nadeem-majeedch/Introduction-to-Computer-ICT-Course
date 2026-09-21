---
lab: 8
title: Security Habits Lab
assigned: Week 15 (L27/L29 window)
due: End of Week 16
---

# Lab 8 — Security Habits Lab

> **Assigned:** Week 15 · **Due:** end of Week 16 · **Modules 7–8**

## Purpose

Security content becomes security *habits* only by doing. This lab audits and hardens **your own** digital life — accounts, credentials, backups, footprints, and AI-tool settings — ending with a personal security plan you can actually follow. Every exercise is performed on accounts and devices **you own**; probing anyone else's systems remains out of bounds (L29's authorized-learning boundary).

## Before you start

- 90 minutes, spread over the fortnight if needed.
- Some steps change account settings — that's the point. Nothing in this lab disables protections.

## Part 1 — Credential audit (25 min)

1. Inventory your five most important accounts (email first — it resets everything else).
2. For each: unique password? (Y/N — don't record the passwords themselves!) MFA enabled? Recovery option current?
3. Enable MFA on at least your email and university accounts if not already; screenshot the *setting page* (never codes/QRs).
4. Adopt a password manager (your OS/vendor's built-in or a reputable free one); migrate your two worst passwords. One sentence: why length + uniqueness beats complexity theatre (L29/NIST guidance).

## Part 2 — Backup drill (20 min)

1. Pick one folder you care about; confirm your 3-2-1 status (Lab 3's plan — is it *actually running*?).
2. Perform a **test restore**: recover one file from your backup/cloud version history to a new location; screenshot. A backup that's never been restored is a hypothesis.

## Part 3 — Phishing self-defence (20 min)

1. Complete your platform's security-awareness exercise if offered; otherwise re-run A5's red-flag list from memory on three real emails in your inbox (delete nothing suspicious — report via the platform's report button).
2. Write your personal "verify out-of-band" script: what you'll do before trusting any urgent money/credential/login email.

## Part 4 — Footprint and AI-tool audit (20 min)

1. Search your own name (normal + quoted); note what a stranger learns in the first page (L30).
2. Review one social platform's privacy settings; change one thing that surprised you; screenshot the setting.
3. For each AI tool you use: check its data-use settings (is your input used for training? can you opt out?) and record the answer — L28's §28.3 checklist applied to yourself.
4. Strip location metadata from one photo you'd share publicly; note the tool you used.

## Part 5 — Personal security plan (15 min)

One page: **threats you actually face** (three, ranked), **controls you've now enabled**, **habits with triggers** ("when an email urgencies me → verify out-of-band"), and **review date** next semester. Honesty over heroics — a plan you'll follow beats one that sounds good.

## Reflection questions

1. Which audit finding scared you most, and which control fixed it fastest?
2. Why does MFA on email come before MFA anywhere else?
3. How do L29's layers appear concretely in your plan? Name one control per layer.

## Expected observations and troubleshooting

**You should see:** a credential table with a Y/N in the MFA column and **no passwords anywhere** (if a password appears, remove it before submitting — then read the syllabus integrity note); at least two MFA settings-page screenshots; a test-restore screenshot showing the recovered file in its *new* location; an AI-tool table naming each tool's data-use answer.

**If something goes wrong:**
- *MFA unavailable on an account* → record that and enable it on the next account; the audit's honest gap analysis is the skill — forcing a fake screenshot is the only failure mode.
- *A platform hides its data-use settings* → record where you looked and what you found; "not findable" is a finding (L28's provenance question applies to platforms too).
- *Test restore fails* → that is the most valuable result in the lab: your backup is a hypothesis, now falsified — fix one layer, retest, and document both attempts.
- *You find a real phishing email* → use the platform's report button; never click links to "check" — your verify-out-of-band script is the response.

**Accessibility alternative:** all audit steps are settings-navigation and text; screen readers handle the relevant pages. If any account control is inaccessible to you (e.g., captcha-locked flows), document the barrier and the alternative action you took — the plan (Part 5) is fully writable without any screenshot.

## Submission checklist

- [ ] Credential audit table (no passwords recorded — ever)
- [ ] MFA screenshots (settings pages only)
- [ ] Test-restore screenshot
- [ ] Footprint/AI-tool audit notes
- [ ] Personal security plan; submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); the security plan and test restore carry the demonstration weight.
