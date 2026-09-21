---
quiz: Q14
covers: L29-L31
---

# Practice Q14 — L29–L31 (Security · Privacy · Computational Thinking)

## Q1

Classify: self-spreading network pest; fake login page; file-encrypting extortion; disguised useful tool.

<details>
<summary>Self-check</summary>

Worm (spreads unaided); phishing (credential-harvesting site — a social-engineering artifact, not malware *per se*); ransomware; trojan (malware behind a legitimate front).
</details>

## Q2

Why does MFA defeat a phished password? Name the two factor categories.

<details>
<summary>Self-check</summary>

The attacker harvested only *something you know*; login also requires *something you have* (authenticator app code, security key) — which the phish didn't collect. Two independent categories: knowledge + possession. (Biometrics are the third category.)
</details>

## Q3

State current password guidance in three rules; contrast one with old advice.

<details>
<summary>Self-check</summary>

(1) **Length over complexity** (long passphrases beat `P@ssw0rd!` gymnastics); (2) **unique per account** (breach dominoes); (3) **change on compromise, not on a calendar** — old advice mandated periodic expiry, which drove weaker predictable passwords (NIST SP 800-63B direction, L29 §29.3).
</details>

## Q4

"Incognito mode makes me anonymous." Give the two-sentence correction.

<details>
<summary>Self-check</summary>

Private browsing clears *local* traces (history, cookies after the session) — it is tidiness on your device. Websites, networks, and providers still see your traffic and identity as usual; anonymity needs different tools entirely (and has its own trade-offs).
</details>

## Q5

Write pseudocode for linear search (find `x` in list `L`; return position or "not found"), then state why binary search needs sorted input.

<details>
<summary>Self-check</summary>

```
FOR i FROM 0 TO LENGTH(L)-1:
    IF L[i] = x THEN
        OUTPUT i
        STOP
OUTPUT "not found"
```
Binary search *halves the range by comparing against the middle element* — that logic assumes ordering (left half = all smaller). Unsorted input makes the middle comparison meaningless: it would discard the half containing the answer.
</details>
