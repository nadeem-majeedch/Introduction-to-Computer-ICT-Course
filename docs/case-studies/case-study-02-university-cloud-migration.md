---
case-study: CS-02
title: A University Moves to the Cloud
lecture: L24
duration: 40 minutes
---

# CS-02 — A University Moves to the Cloud

> **Lecture:** L24 · **Duration:** 40 min · **Format:** stakeholder role debate → class decision

## The scenario

A mid-size university runs its student portal, email, and learning-management system on 12 aging servers in a basement room. The servers are 6 years old, out of warranty; one failed hard drive last semester took the portal down for two days. The IT director proposes migrating everything to a public cloud. The university must decide by next board meeting.

## Stakeholder roles (assign one per group)

| Role | Core interests |
|---|---|
| IT director | Reliability, patching burden, headcount |
| Finance officer | Capex vs opex, multi-year cost predictability |
| Registrar | Data protection of student records, legal compliance |
| Faculty representative | Downtime tolerance, tool freedom, support quality |
| Student council rep | Access speed, fees, privacy of their data |
| Cloud vendor (observer) | What the provider actually guarantees vs what the university still owns |

## Guiding questions

1. **Service models (L24):** Which parts fit SaaS (email?), which IaaS (custom portal?), which stay on-premises and why? Draw the division-of-responsibility line per workload.
2. **Cost shape:** Compare three-year capex (new servers + UPS + cooling + staff) vs opex (subscription + migration project). Which *hidden* costs does each side omit? (Egress fees? Staff retraining? Downtime during migration?)
3. **Risk inventory:** For each of — data breach, vendor lock-in, price escalation, outage, compliance violation — name who owns the mitigation under the proposed split.
4. **Shared responsibility (L24, L29):** The provider secures the infrastructure. What — concretely — does the *university* still have to secure? (Accounts/MFA, configurations, backups of SaaS data?)
5. **Decision:** Produce a one-paragraph board recommendation: what moves, what stays, what conditions apply (pilot? exit clause? data-residency requirement?), and the two metrics you'd review after the first semester.

## Debrief

The winning answers rarely say "all in" or "never": they *split workloads* by service model and ownership. Connect back to L24's table — the boundary line you drew per workload *is* the answer.

## Notes for self-study

The NIST definition of cloud computing (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service — [L24 references](../lectures/L24-cloud-computing-virtualization.md)) is the checklist the board will test your recommendation against.
