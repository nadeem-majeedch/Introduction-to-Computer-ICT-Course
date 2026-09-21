---
lab: 2
title: Hardware Inventory and Benchmarking
assigned: L06
due: End of Week 4
---

# Lab 2 — Hardware Inventory and Benchmarking

> **Assigned:** L06 · **Due:** end of Week 4 · **Module 2**

## Purpose

Hardware specs are marketing until you measure them. This lab makes you inventory your machine precisely (L05–L08 vocabulary), observe the memory hierarchy in action, and recommend hardware from requirements — the three exam-ready skills of Module 2.

## Before you start

- 90 minutes; no software installation beyond a browser.
- Use built-in system information tools only.

## Part 1 — Precise inventory (20 min)

| Component | To record | Where to look (any OS) |
|---|---|---|
| CPU | Model, cores/threads, base clock | System info / About |
| RAM | Size, type if visible (DDR generation) | System info |
| Cache | L1/L2/L3 if reported | CPU spec page (vendor site) |
| Storage | Type (HDD/SSD), size, interface | Disk utility / Device Manager |
| GPU | Model, VRAM | Display settings / About |
| OS | Version, 64-bit? | About |

Then classify your machine on the L03 taxonomy and justify the class in two sentences.

## Part 2 — Observing the hierarchy (30 min)

Design a **fair test** and run it (any stopwatch or a simple browser-based JS timing page your instructor provides):

1. **Sequential read:** read a 500 MB file from disk (copy to RAM disk or measure copy time) vs reading 50 × 10 MB files (random-ish pattern). Record both times; explain the gap using L08's access-time table.
2. **RAM pressure:** open applications until the OS reports memory pressure (Task Manager / Activity Monitor / `top`). Note: at what point did the system feel slower? Connect to virtual memory (L07).
3. Record observations in a table: *test · condition · time/observation · hierarchy explanation*.

Honesty rule: report anomalies (background updates, thermal throttling) rather than deleting them — real benchmarks include environment notes.

## Part 3 — Requirements → recommendation (25 min)

Three briefs (write one paragraph each, justifying against *workload*):

1. **Data-science first-year:** runs spreadsheet + browser + statistics courseware; budget-tight laptop.
2. **Field researcher:** long battery, rough handling, offline notes; no gaming.
3. **Lab workstation:** video editing for course media; fixed power, shared by teams.

For each: choose CPU tier, RAM size, storage type/size, GPU need — and cite the workload property that drove each line ("because the workload does X").

## Part 4 — Reflection questions (15 min)

1. Which hierarchy observation surprised you most, and which locality type (L07) explains it?
2. Why is your CPU's cache size more informative than its GHz alone (L06)?
3. For brief #1, which single component upgrade gives the most real-world speed, and why?

## Expected observations and troubleshooting

**You should see:** a copy of many small files taking visibly longer than one large file of the same total size (sequential vs scattered access); memory pressure causing system-wide sluggishness before any application fails; an inventory where every row names its source.

**If something goes wrong:**
- *Copy times wildly inconsistent* → that's data: record the inconsistency, close background apps, run again, and report both runs — anomalies are content here (the honesty rule).
- *Memory pressure never appears* → machines with lots of RAM may resist; open more browser tabs or note the ceiling you hit and analyse why (L07's capacity axis).
- *Vendor spec page unreachable* → any manufacturer-database mirror your instructor lists; or record "cache not reported" for your CPU row — a honest gap beats an invented number.

**Accessibility alternative:** all timings can be taken by a screen-reader-friendly stopwatch web page or a partner reading the clock aloud; tables submit as text. If your machine lacks a second display or a copy-speed test target, the lab-machine image provides both.

## Submission checklist

- [ ] Inventory table complete with sources
- [ ] Hierarchy experiments recorded with environment notes
- [ ] Three justified recommendations
- [ ] Reflections answered
- [ ] Submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); §2's fair-test design carries the demonstration weight.
