# LOOP — Autonomous Execution Protocol

**Purpose:** let this project advance without a human typing the obvious next step each time, **without** letting it harden mistakes into the record while nobody is watching.
**Reads:** [QUEUE.md](QUEUE.md) · **Writes:** the topic files, the register, a session audit, and QUEUE.md itself.
**Prepared:** 2026-07-28 · **Status:** v1.0

---

## 0. Why this document is cautious

On 2026-07-27 this project produced four findings that were each **wrong in a way only a later step caught**:

| Error | Caught by |
|---|---|
| The ATF report read through a defense filing's selective quotation | reading the report directly |
| The `source identification` over-weighted — the case came from the rifle's own chamber | reading a *different* witness on provenance |
| The Dremel thread bounded as "class-level" when the tool had been **identified** | reading past the keyword sample |
| **D-51** — a hearing date "corrected" from a transcript service's page date | locating Day 1 |

**Every one of those would have propagated unattended**, and D-51 would have silently corrupted case posture in five files. That history is the reason for §3.

A loop that runs this project is not doing clerical work. It is doing evidence handling in a live capital case. **The default posture is: acquire freely, conclude slowly.**

---

## 1. The cycle

Each iteration:

1. **Read QUEUE.md.** Take the highest-priority item whose `Status` is `ready` and whose `Blocked by` is clear. Ties break toward the **cheaper** item.
2. **Re-read the standing hazards** (QUEUE.md, bottom). They are there because each one already cost this project a finding.
3. **Check the gate** (§3). If `human`, do not execute — write the question into `QUEUE.md` under the item and move to the next `ready` item.
4. **Execute**, following the project's file conventions (CLAUDE.md): two layers never blended, sourcing tier declared, confidence graded to an actual verification act, scope stated plainly.
5. **Record.** Update the topic file(s); one version bump and one combined revision row per file per cycle; assign register numbers only after `grep -rhoE "D-[0-9]+" --include="*.md" . | sort -n` **and reading the highest hit**.
6. **Update QUEUE.md** — mark done, add any items the work surfaced, re-rank if priorities moved.
7. **Log** to the current session audit. If none exists for today, create `<PREFIX>-AUDIT-<date>`.
8. **Commit** — but only what the gate allows (§3). Push only if the cycle produced a committed change.
9. **Schedule the next cycle** or stop (§5).

## 2. Findings are provisional until independently checked

**A finding produced in a loop cycle enters the record marked `[PROVISIONAL]`.**

It hardens only when a **separate** cycle, working from the primary artifact rather than from the summary, confirms it. The confirming cycle must be able to fail — it is not a proofread. Standing rule from BOC-AUDIT-2026-07-27B: **an adversarial pass is bounded by the completeness of what it re-reads**, so the verification cycle must go back to the source, not to the write-up.

Practical consequence: **no `[PROVISIONAL]` finding may be cited by another file, propagated into a topic folder, or used to resolve a register entry.** Q-02 exists because both of this project's audits to date were self-audits.

## 3. Gates — not advisory

| Gate | Meaning |
|---|---|
| `auto` | Execute and commit. Mechanical acquisition, re-polls, carrier checks, indexing. |
| `verify` | Execute and commit **the acquisition**; record findings as `[PROVISIONAL]`. Do not let them leave the file they were written in until a verification cycle clears them. |
| `human` | **Stop.** Write the question into QUEUE.md and move on. |

**Always `human`, whatever the queue says:**

- Anything that changes **case posture** — dates, charges, bindover status, hearing outcomes. This is the one thing in the library that must be right and current, and it is the thing D-51 got wrong.
- Anything asserting or implying **conduct by a living person** — including Robinson, Twiggs, family members, witnesses, officers, and Owens.
- **Spending money** (Q-31), **entering credentials**, or **subscribing** to anything.
- **Publishing anywhere outside this repository.**
- Creating or deleting a **topic folder**, or moving files between them.
- Any conclusion that would **resolve a register entry against a named person**.
- Anything the loop has already **failed twice**.

**Never, in any mode:** infer identity from partial information (Q-40 is the live example — an early detainee expressly not treated as a suspect must not be matched to a named person); adopt an allegation; reproduce a private individual's contact or location details; or use Tier 4 material to resolve anything.

## 4. Hard stops

The loop stops itself and waits for a human when:

- **A register entry would move for the third time.** D-48 moved four times in one day. That is a signal the record is still arriving, not that the analysis is converging.
- **A correction would reverse a prior correction** (the D-51 shape). Two reversals on one fact means the project does not yet understand the fact.
- **A cycle produces no committed change twice running** — it is spinning.
- **An acquisition route starts failing** where it previously worked (bot-blocks, paywalls appearing, 403s) — the environment changed and the assumptions may have too.
- **The queue has no `ready` item** that is not `human`-gated.

## 5. Pacing

Two different clocks, and they should not be confused:

- **Research work** (Q-01, Q-02, Q-06…) is not time-sensitive. Pace it by *work available*, not by wall clock. Long intervals are correct; there is no reason to wake up hourly to read a transcript that will still be there.
- **The docket is time-sensitive.** Defense response **2026-08-11**, State's reply **08-18**, oral argument **09-01**, bindover ruling thereafter. That belongs on a **calendar trigger**, not on the research loop. See `.claude/` cron config.

## 6. What "done" means

A cycle is done when the deliverable is a **file**, not a chat message. CLAUDE.md is unambiguous: *the deliverable is always the files*. A cycle that produced only analysis has produced nothing.

## 7. Stopping it

- `/loop` with `stop: true`, or simply say so.
- Delete or empty QUEUE.md — the loop has nothing to dispatch and halts on the §4 condition.
- `git revert` any cycle's commit; each cycle is one commit with its Q-ID in the subject line.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-28 | Initial protocol. Cycle defined (§1); provisional-findings rule (§2) written directly out of the fact that both existing adversarial passes were self-audits; three gates with an always-human list (§3) covering case posture, living persons, money and identity inference; hard stops (§4) keyed to the failure shapes actually observed — third register movement, reversal-of-a-reversal, spinning, environment change; pacing split between untimed research and the calendar-driven docket (§5). |
