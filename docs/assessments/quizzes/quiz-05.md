---
quiz: Q05
covers: L09-L10
---

# Practice Q05 — L09–L10 (Software Landscape · Operating Systems)

## Q1

Place in the software stack and justify the two trickiest: Photoshop, Linux kernel, GPU driver, printer firmware, antivirus utility.

<details>
<summary>Self-check</summary>

Applications: Photoshop (user task), antivirus (utility — *system software* because it maintains/runs the machine, not a user task — the tricky one). OS: Linux kernel. Below OS: GPU driver (translates OS commands to device signals), printer firmware (software burned into the device itself — trickiest because it's software that ships *inside* hardware).
</details>

## Q2

Give one practical reason FOSS license terms (like GPL) matter to a business beyond "it's free."

<details>
<summary>Self-check</summary>

Copyleft terms can *require* derivative works to carry the same license — e.g., shipping modified GPL code inside a closed product may obligate source disclosure. License choice is a legal/compliance decision, not just a price tag.
</details>

## Q3

Name the boot stages from power-on to login, in order.

<details>
<summary>Self-check</summary>

Power-on → firmware (BIOS/UEFI) runs, POST self-test → firmware finds and runs the **boot loader** on the boot drive → boot loader loads the OS **kernel** → kernel starts drivers and services → login/lock screen. Diagnosis value: each stage failing looks different.
</details>

## Q4

Why can one crashing app not corrupt another app's memory, and who enforces it?

<details>
<summary>Self-check</summary>

The OS enforces **memory isolation**: each process gets its own protected address space (user mode has no privilege to touch others). A rogue pointer crashes *its own* process; the kernel survives. (Kernel-space bugs are the exception that proves the rule.)
</details>

## Q5

Give one task where CLI beats GUI and one where GUI beats CLI — argue from the interface's mechanics, not habit.

<details>
<summary>Self-check</summary>

CLI wins bulk/precise/repeatable work: "rename 200 files by pattern" is one command vs 200 GUI interactions; it's also scriptable. GUI wins discovery/spatial work: finding an unfamiliar setting by browsing menus, or photo layout by seeing — the CLI has no "browse," only exact names.
</details>
