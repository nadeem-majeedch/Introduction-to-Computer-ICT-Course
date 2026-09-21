---
activity: A5
title: Phishing Red-Flag Audit
lecture: L29
duration: 30 minutes
---

# A5 — Phishing Red-Flag Audit

> **Lecture:** L29 · **Time:** 30 min · **Groups:** pairs

## Goal

Build the reflexes: spot phishing red flags, rank their reliability, and respond correctly. All samples are **simulated, educational examples** created for this course — no real credentials, links are non-functional screenshots.

## Ethics frame (1 minute, every time)

We study *recognition and defence only*. Techniques for crafting attacks are not taught here — they're also exactly what distinguishes authorized education from misuse (L29 §29.4). What you learn: the defender's checklist.

## Setup

The instructor projects four simulated messages (or hands out printed screenshots):

1. **"IT Support"** — "Your account will be deleted in 24h. Confirm password." Sender: `it-support@university-portal-verify.com`.
2. **"Bank alert"** — "Unusual login from Moscow. Click to secure." Genuine-looking logo; link hover target is `bank-secure-login.example.tk`.
3. **"Professor"** — "I'm in a meeting, buy 4 gift cards for the department" — from a lookalike personal Gmail account.
4. **"Parcel"** — SMS: "Your parcel is held: small customs fee via this link."

## Round 1 — Flag and rank (12 min)

Each pair audits all four messages. For each: list **red flags** and rank them:

- **Reliable flags:** sender domain mismatch, urgency + threat, unexpected attachment/login demand, payment in gift cards, lookalike domains (`rn` vs `m`), free-TLD link targets.
- **Weak flags:** typos (modern phishing is flawless), logos (trivially copied), formatting.

## Round 2 — Response (8 min)

For each message, write the correct user action:

- Report via the platform's report button; **never** click; **verify out-of-band** — contact the claimed sender via a *known-good* channel (the number on your card, the official site you typed yourself).
- For message 3, the verification call to the professor's department number is the whole game.

## Round 3 — Debrief (8 min)

Class consensus: which single flag catches the most real phish? (Sender/link mismatch — hence hover-before-click.) Connect to L29's layers: MFA makes even a *successful* credential harvest mostly useless; reporting protects everyone else.

## Solo variant (revision)

From memory: list five reliable red flags and the four-step response script. Then audit your own inbox's latest two "urgent" emails (report, don't click).
