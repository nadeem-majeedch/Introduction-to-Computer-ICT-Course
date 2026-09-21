---
lab: SB-3
title: Computational Thinking Gym
related: L31
duration: 30–40 min
graded: false
---

# SB-3 — Computational Thinking Gym

> **Related lecture:** L31 · **Duration:** 30–40 min · **Practice (completion-marked)**

## Learning outcomes

1. **Apply** decomposition, pattern recognition, abstraction, and algorithm design to three small unfamiliar problems. (L31)
2. **Express** one solution as a flowchart and one as pseudocode, before any code exists. (L31)
3. **Trace** a peer's algorithm and isolate a planted bug by systematic testing. (L12's method, L31's practice)

## Prerequisites and equipment

Pen and paper, or any flowchart tool you already have (including pencil). **No software, no installs.** Accessibility alternative: fully paper-based; flowcharts may be submitted as numbered step lists with decision points labelled — shape-drawing is never the assessed skill.

## Setup

Three problem cards (your instructor provides them, or use these):

- **A. Print quota:** a student gets 100 free pages per semester; each print job deducts; when the balance hits zero, jobs are refused. Design the balance machine.
- **B. Late-plate:** the university cafeteria charges full price until 14:00, then 50% off until 15:30, then closes. Design the price decider for a given arrival time.
- **C. Group maker:** split 23 students into project groups of 3 or 4, as evenly as possible, with no one left out. Design the splitter.

## Step-by-step tasks

1. **Decompose (10 min).** For card A and card B: list the inputs, outputs, and rules separately before any flowchart. Label each rule with the pillar it exercises.
2. **Abstract (5 min).** For card C: what must the algorithm *know* (student count, group sizes) and what may it *ignore* (names, friendships)? Write the abstraction boundary in two sentences.
3. **Design (10 min).** Flowchart card B end-to-end (decisions, paths, closure). Pseudocode card C — language-independent, reviewable by a classmate who hasn't seen the card.
4. **Trace and break (10 min).** Swap pseudocode with a partner (or your instructor's seeded version). Trace it with: 23, 24, 25 students. Find one input where it misbehaves; isolate the faulty step by systematic testing — name the step, don't guess.

## Expected observations

Card C is where decomposition earns its keep: the even-split rule (23 = 5×4 + 1×3) hides an edge case that tracing exposes — most first versions handle 24 and fail 23 or 25. That failure *is* the curriculum.

## Questions

1. Which pillar did card C exercise most, and which did your card B flowchart skip the first time?
2. Your partner's pseudocode "worked" for the sample input but failed another. What does that say about testing with one input?

## Troubleshooting

- *Partner absent* → trace your instructor's seeded buggy version (provided with the cards) instead; the seeded bug is the same exercise.
- *Flowchart tool unavailable* → numbered step lists with labelled decisions are accepted — see the accessibility alternative.

## Submission and assessment

Completion-marked practice: submit decompositions, the flowchart (or labelled step list), the pseudocode, and your bug-isolation note naming the faulty step. Feedback against the "excellent" descriptors; not weighted into the final grade. The integrated project (coverage area 22) is where these pillars are graded for real.
