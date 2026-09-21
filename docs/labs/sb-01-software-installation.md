---
lab: SB-1
title: Software Installation and Package Awareness
related: L12
duration: 30–40 min
graded: false
---

# SB-1 — Software Installation and Package Awareness

> **Related lecture:** L12 · **Duration:** 30–40 min · **Practice (completion-marked)**

## Learning outcomes

1. **Read** an installer's choices and permissions as claims about behaviour. (L12)
2. **Distinguish** store/marketplace installs, vendor downloads, and package managers as distribution channels. (L12)
3. **Verify** what an installation actually changed on your system. (L12)

## Prerequisites and equipment

Lab 1's workspace; your own machine or a lab machine; **nothing needs installing from outside trusted sources** — the trusted-source drill below uses what your institution already sanctions. Accessibility alternative: all steps are readable as text; screenshots optional.

## Setup

Note your OS's package story before touching anything: Windows (Microsoft Store, `winget`), macOS (App Store, Homebrew *if already present*), Linux (`apt`/`dnf`/`pacman`). One line each: who vets software in each channel?

## Step-by-step tasks

1. **Channel inventory (10 min).** For three applications already on your machine, record: name, channel used (store / vendor download / package manager / bundled), and how you'd verify the publisher. No installs.
2. **Installer reading drill (10 min).** Open (do not complete) any installer your institution distributes for coursework; screenshot the permission/option screens; write one sentence per screen: what is this screen *claiming*? Compare against SB-1's guidance on bundleware: which default would you change?
3. **Package-manager awareness (10 min).** Where a package manager exists on your machine, run its *search* command for a tool you use (`winget search`, `brew search`, `apt search`) — read the output: version, source. Where none exists, read your OS store's listing for the same tool and answer: who updates it, and how would you know?
4. **Post-install verification habit (5 min).** Write your own three-check routine for after any install (e.g., Start-menu entry, default-app change, startup items) — the L12 habit, personalized.

## Expected observations

Channels differ in *who vets*: stores vet lightly and sandbox; package managers vet via repositories and update centrally; vendor downloads vet nobody but the vendor. Installers bundle optional extras in defaults — that's where attention pays.

## Questions

1. Which channel gives the user the *most* control over updates, and what is the cost of that control?
2. Why do vendors bundle extras as defaults rather than opt-ins? (One economic sentence.)

## Troubleshooting

- *No package manager on your machine* → the store-route comparison satisfies task 3; note the substitution.
- *Installer unavailable in your institution* → any vendor's publicly documented installer walkthrough (screenshots in their help pages) substitutes; cite it.

## Submission and assessment

Completion-marked practice: submit the channel inventory + installer-reading sentences via LMS for feedback. Rubric: the standard three criteria apply unweighted; feedback uses the "excellent" descriptors only. If you cannot access any required tool, the written-walk-through substitution above keeps every outcome reachable.
