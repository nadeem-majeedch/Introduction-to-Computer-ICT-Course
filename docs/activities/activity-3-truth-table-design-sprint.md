---
activity: A3
title: Truth-Table Design Sprint
lecture: L17
duration: 25 minutes
---

# A3 — Truth-Table Design Sprint

> **Lecture:** L17 · **Time:** 25 min · **Groups:** pairs, then cross-attack

## Goal

Translate a realistic rule into a Boolean expression and defend its truth table — the exact skill Module 5's exam questions and real-world system rules both demand.

## Setup

Each pair receives one rule card (below). Deliverable on one sheet: variables defined → Boolean expression → full truth table.

Rule cards (sample set):

1. A student may enrol in ICT-lab-advanced **iff** they passed ICT basics **and** have no outstanding dues.
2. The lab door unlocks **iff** a valid card is scanned **or** the supervisor's key is used — but never if the alarm is armed.
3. A warning light shows **iff** temperature is high **or** pressure is high, but **not** both (to distinguish which fault).
4. A discount applies **iff** the customer is a member **and** (spends over 100 **or** has a coupon), and the coupon doesn't combine with the sale items flag.
5. The printer queues **iff** paper is loaded **and** (toner is OK **or** draft mode is set).
6. Bonus card: an XOR-heavy rule of the instructor's choice (e.g., exactly-one-of-three-conditions).

## Round 1 — Design (12 min)

Variables, expression, complete truth table ($2^n$ rows — no skipped rows; that's the exhaustiveness habit).

## Round 2 — Cross-attack (8 min)

Pairs swap sheets with a neighbouring pair and try to *break* the design: find a real-world case the truth table gets wrong (a row that violates the plain-English rule). Found bugs go back for repair.

## Round 3 — Defend (5 min)

One pair presents its rule, expression, and the row most often misunderstood. Class votes: does the table *mean* the same thing the words *say*?

## Debrief

The classic failures: OR read as XOR (card 1 "and" trouble), De Morgan slips in card 4's negation. Both recur in Q10 and the midterm.

## Solo variant (revision)

Take any rule card; produce variables → expression → table; then write the negation of your expression using De Morgan *without* parentheses around NOT of the whole thing.
