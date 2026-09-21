---
case-study: CS-03
title: Data-Driven Public Health Decisions
lecture: L26 (extends to L27)
duration: 35 minutes
---

# CS-03 — Data-Driven Public Health Decisions

> **Lecture:** L26 (extends to L27) · **Duration:** 35 min · **Format:** evidence review → dashboard critique → recommendation

## The scenario

A provincial health department publishes a vaccination-coverage dashboard. This week it shows district A at **94% coverage** (the national target) while neighbouring district B shows 71%. A newspaper headline follows: *"District A shows the way — B must copy its model."* A health official proposes redirecting next quarter's entire outreach budget to district B's "model adoption."

Your analytics team is asked to advise — honestly.

## The evidence packet (instructor-provided or reconstructed in class)

1. District A's 94% comes from **clinic-registered** doses; district B serves many remote villages where doses are given by mobile teams that **report on paper, digitized weekly**.
2. The dashboard's map uses **colour gradients without numbers** and a legend spanning 60–100%.
3. A footnote nobody read: A's figure is a **projection**, B's is **recorded actual**.
4. Denominator check: A's population figure comes from an old census; B's was updated last year.

## Guiding questions

1. **Lifecycle placement (L26):** At which lifecycle stage does the *real* problem live — collection, cleaning, analysis, visualization, or communication? Justify with the evidence item numbers.
2. **Chart honesty (L26/L19):** What does the gradient-without-numbers map make a reader *feel* that the data doesn't *support*? Redesign the display in three bullet points (what you'd show instead and why).
3. **Data quality (L26):** Name two cleaning/validity checks that would have caught this: one on denominators, one on reporting channels.
4. **Decision integrity:** The official's budget proposal is *reacting to a visualization*, not to vaccination. Write the one-paragraph memo you send: what the data actually shows, what's unknown, and what you recommend measuring next quarter.
5. **AI extension (L27/L28):** The department wants an AI model to "predict low-coverage districts from the same data." What must be true of the training data before such a model is worth anything — and what bias risk does evidence item 1 create?

## Debrief

The case's spine: *decisions inherit the quality and honesty of the data pipeline* — the lifecycle stage where the defect lives determines the fix. Most public-data scandals are L26 defects (measurement, denominators, display), not exotic statistics.

## Notes for self-study

The re-identification and minimum-collection principles from [L26 §26.4](../lectures/L26-data-science-foundations.md) also apply: the dashboard contains district-level aggregates — the safe end of the spectrum; patient-level releases would need aggregation before publication.
