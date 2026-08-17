# DOCKET-WATCH routine prompt — DRAFT 2026-08-17 (Q-147: the route-RECOVERY trigger)

**Status:** ⏸ **NOT APPLIED — awaiting owner authorisation**, as the 2026-08-14 and 2026-08-16 drafts were. 👤
**Target:** cloud routine `trig_016faLfbQWCz72M463Dy8HsL` ("DOCKET-WATCH — State v. Robinson, Case 251403576 (report-only)").
**Supersedes:** `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md`, applied 2026-08-17 and confirmed live from the API (`updated_at` 2026-08-17T04:43:02Z).
**Next firing:** **Wed 2026-08-19, 09:00 ET** — the morning after the State's reply is due. **This change should land before it.**

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
| **1.0** | **2026-08-17** | Created (Q-147). One replacement: the ESCALATE line gains a **route-RECOVERY** limb, an instruction to report what a recovery makes possible, and the standing "a blocked route is not a null" rule. 🚨 **Found in the same pass: the live prompt already carried an egress "in either direction" trigger that `DOCKET-WATCH.md` LACKED** — the two copies were out of sync in the opposite direction to the one every prior reconciliation assumed. Spec corrected in place the same day; **"diff both ways" added there as a standing instruction.** **Not applied — awaiting owner authorisation.** |
