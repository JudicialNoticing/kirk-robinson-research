# DOCKET-WATCH routine prompt — DRAFT 2026-08-17 (Q-147: the route-RECOVERY trigger)

**Status:** ✅ **APPLIED 2026-08-21 ~08:57 EDT** on owner authorisation (given in-session; the 2026-08-20 close block had already recorded application as authorised by precedent). **Verified by an INDEPENDENT RE-FETCH, not from the write's own echo** — `updated_at` **2026-08-21T12:57:10Z**, and all six invariants re-read intact: `cron_expression` `0 13 * * 3,6` · `enabled: true` · `next_run_at` **2026-08-22T13:00:41Z** · `environment_id` `env_01W6FqrQNGVQ8RPsSsUapCHf` · `allowed_tools` `[Read, WebSearch, WebFetch]` · model `claude-opus-5`.
**Target:** cloud routine `trig_016faLfbQWCz72M463Dy8HsL` ("DOCKET-WATCH — State v. Robinson, Case 251403576 (report-only)").
**Supersedes:** `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md`, applied 2026-08-17 and confirmed live from the API (`updated_at` 2026-08-17T04:43:02Z).
**Next firing:** ~~**Wed 2026-08-19, 09:00 ET**~~ — **that firing came and went with this draft unapplied** (it ran egress-blind, day 15, and reported the reply filed T1-via-T3). The change instead landed before **Sat 2026-08-22, 09:00 ET**, with ~28 hours to spare.

> 🚨 **WHAT THE APPLICATION PASS FOUND, AND IT IS THE REASON STEP 1 OF THE CHECKLIST EXISTS: the live prompt was stale in FOUR places, not the two that `DOCKET-WATCH.md`, `CR-WATCH-log.md` and the vault's close block all named.**
>
> The two named: this draft's **ESCALATE** replacement (Q-147), and the **08-18 false premise** ("not yet due and not filed"). The two unnamed, both inside the SOURCING DISCIPLINE paragraph and neither in any queue row:
>
> 1. **The Fox-mirror baseline still read `55 PDFs`.** Run 7 refreshed it to **71** on 2026-08-20 after triage. This is the load-bearing one: the route's whole value is that detection there is a *diff*, so a diff against 55 would have re-flagged **the sixteen already-triaged PDFs as new** — a run reporting sixteen phantom newcomers eleven days out from oral argument.
> 2. **The route-status block was still stamped `as of 2026-08-16`**, predating both Run 6's HTTP 504 block and Run 7's recovery, and described the CDX index as flatly "open" when it has since been measured **blocked and open twice within ten minutes**.
>
> ⚠️ **Both were found by reading the whole live prompt before diffing — not by working the named list.** `DOCKET-WATCH.md` already carries "diff both ways" as a standing instruction from 2026-08-17; **what this pass adds is that the diff must cover the WHOLE prompt, because the queue only names the staleness someone happened to notice.** A queue row is a record of what was seen, never a census of what is wrong.
>
> ➕ **A fifth, additive change in the same pass:** the Q-45 bullet now records the 2026-08-20 July-folder enumeration as an **attempted null** (56 PDFs, no brief), so no future run reports that route as untried, and the 08-18 bullet now states plainly that Q-45 is the only bindover-cycle document held nowhere.

---

## Why this draft exists

**Q-147.** The escalation trigger list is **asymmetric**: it fires when a route that previously worked starts failing, and has **no trigger for a route that had been failing and has RECOVERED**. Run 5 (2026-08-16) had to notice DocumentCloud's recovery by reading a diff. **That recovery was operationally significant** — it put the cheap post-08-18 DocumentCloud sweep back on the table — and nothing in the spec would have surfaced it.

> **A watch that escalates only degradation silently under-reports its own capability. A capability nobody is told about is a capability nobody uses.**

### 🚨 And the pass found something the queue row did not: the drift runs the other way

**The live prompt already contains an "in either direction" trigger — for EGRESS:**

> `…or YOUR EGRESS HAS CHANGED in either direction since the last run.`

**`DOCKET-WATCH.md` had no egress trigger at all.** Every prior reconciliation of these two copies has assumed the **prompt is the copy that lags the spec** — that is what the 2026-08-14 and 2026-08-16 drafts were both correcting. **Here the prompt LED the spec, and the divergence went unnoticed precisely because nobody was looking in that direction.**

✅ **`DOCKET-WATCH.md` was corrected 2026-08-17 to carry both limbs.** 🚨 **Standing instruction added there: when these two copies are reconciled, diff them BOTH WAYS.**

---

## The change, and nothing else

**One line changes. Everything else in the routine's prompt is carried across verbatim** — the calendar (as corrected 2026-08-17), the prohibitions, the sourcing discipline, the report headings.

### The ESCALATE line — REPLACE

**From:**

> `ESCALATE — put this at the very TOP of your report, in bold, if any trigger is met: a bindover ruling has issued; the 2026-09-01 date has moved; a filing has been sealed or unsealed; a route that previously worked has started failing; or YOUR EGRESS HAS CHANGED in either direction since the last run.`

**To:**

> `ESCALATE — put this at the very TOP of your report, in bold, if any trigger is met: a bindover ruling has issued; the 2026-09-01 date has moved; a filing has been sealed or unsealed; A ROUTE HAS CHANGED STATE IN EITHER DIRECTION — one that previously worked has started FAILING, or one that had been failing has RECOVERED; or YOUR EGRESS HAS CHANGED in either direction since the last run. A RECOVERY IS AN ESCALATION. Report it as prominently as a failure and say what it makes possible again — a route coming back changes what the next run can do, and if you do not say so, nobody finds out. Note also: a BLOCKED route is never a null and is never baselined; say "unattemptable", not "empty".`

---

## Application checklist 👤

The 2026-08-17 application of the previous draft established the safe procedure. Repeat it exactly:

1. **Read the live prompt from the API first** — do not apply a diff against a remembered copy.
2. **Apply only the ESCALATE-line replacement above.**
3. **Verify by an INDEPENDENT RE-FETCH after the write, not from the write's own echo.** Confirm the new text is present and that these are all unchanged:
   - `cron_expression` `0 13 * * 3,6`
   - `enabled: true`
   - `next_run_at` **2026-08-19T13:00Z**
   - `environment_id` `env_01W6FqrQNGVQ8RPsSsUapCHf`
   - `allowed_tools` `[Read, WebSearch, WebFetch]`
   - model `claude-opus-5`
4. **Record the confirmed `updated_at` in this file's status line and in `DOCKET-WATCH.md`.**

⚠️ **What this does NOT fix, restated so it is not mistaken for solved:** the routine is still **report-only** (`No sources configured`) and still **egress-blind**. **The 2026-08-18 by-hand local run remains the only document-capable cover for the State's reply.**

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-08-17** | Created (Q-147). One replacement: the ESCALATE line gains a **route-RECOVERY** limb, an instruction to report what a recovery makes possible, and the standing "a blocked route is not a null" rule. 🚨 **Found in the same pass: the live prompt already carried an egress "in either direction" trigger that `DOCKET-WATCH.md` LACKED** — the two copies were out of sync in the opposite direction to the one every prior reconciliation assumed. Spec corrected in place the same day; **"diff both ways" added there as a standing instruction.** ✅ **APPLIED 2026-08-21 — see the status block at the top.** |
| **1.1** | **2026-08-21** | **Applied, and it turned out to be four changes rather than one.** The ESCALATE replacement landed as drafted, plus three corrections this draft did not anticipate: the **08-18 false premise** (now FILED AND BANKED, with the 19-vs-18-page discrepancy marked do-not-resolve and the 08-18 miss recorded so no run re-derives it), the **Fox-mirror baseline `55` → `71`** (Run 7's post-triage figure — against 55 the diff detector would have reported **sixteen phantom newcomers**), and the **route-status stamp `2026-08-16` → `2026-08-20`** with the CDX index's measured intermittency written in. One additive change: Q-45's already-attempted routes. **Verified by independent re-fetch** (`updated_at` 2026-08-21T12:57:10Z; six invariants intact). 🚨 **Standing lesson strengthened: diff the WHOLE prompt, not the lines the queue names — a queue row records what someone saw, never a census of what is wrong.** Two of these four were invisible to every note in the repo. |
