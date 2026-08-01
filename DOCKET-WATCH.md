# DOCKET WATCH — *State of Utah v. Robinson*, Case No. 251403576

**Why this is separate from [LOOP.md](LOOP.md):** the research queue is paced by work available. **This is paced by a court calendar** (LOOP.md §5). Missing a filing window is the one failure here that cannot be caught up later.
**Prepared:** 2026-07-28 · **Runs until:** the bindover ruling, then re-scope. · **Status:** **v1.3 — Runs 1 and 2 executed (2026-07-28, 2026-08-01)**; log at [CR-WATCH-log.md](files%20-%20Court%20record/CR-WATCH-log.md)

> ### ⏰ THE SCHEDULER NOW EXISTS — and its one limitation
> **Cloud routine `trig_016faLfbQWCz72M463Dy8HsL`**, created 2026-08-01 on user authorisation. **Wednesdays and Saturdays, 09:00 ET** (`0 13 * * 3,6` UTC), Opus 5, connectors stripped. **First firing: 2026-08-05.** Wednesday/Saturday is deliberate: **all three briefing dates fall on Tuesdays**, so a Wednesday run lands the morning after each one.
> ⚠ **IT IS REPORT-ONLY.** The cloud environment was refused access to the private repository (`HTTP 403 — You don't have access to a repository this routine uses`). **The routine runs the checks and produces a report, but cannot commit its run log.** Its output must be **pasted into `CR-WATCH-log.md` by hand** until the Claude Code GitHub App is granted access to `JudicialNoticing/kirk-robinson-research`. **Granting that access is a user action and is the one outstanding step.**
> **The spec below is inlined into the routine's prompt**, so the routine carries the prohibitions even without the repo. **If this file changes, the routine's prompt must be updated to match** — they are not automatically in sync.

## The calendar

**Source: Tier 1, read directly** — set in open court at the close of Day 4 and recorded verbatim at **[CR-ACQ §5.1](files%20-%20Court%20record/CR-ACQ-2026-07-27_court-record-acquisition.md)**, the library's canonical statement. *(Upgraded 2026-07-28, Q-43. Through v1.0 this table carried a news report's dates at Medium-high while the transcript sat banked and unread — see the note at the foot of this section.)*

| Date | Event | Status |
|---|---|---|
| 2026-07-06 → 07-10 | Preliminary hearing, five days | **held** (D-51, as reversed) |
| **2026-07-28** | **State's opening probable-cause brief due**, 35-page limit | ✅ **REPORTED FILED 2026-07-28.** **Run 2 (2026-08-01) upgraded this from one independent source to six** (Fox, Reavy, KUTV, ABC, Washington Examiner, Deseret/KSL) — **source independence for the FILING EVENT only; it stays T1 via T3 and the document is still not held** (→ Q-45). ⚠ **A public 28-page mirror now exists on Scribd**, giving Q-45 a route; **contents remain deliberately unrecorded until banked and provenance-verified.** ⚠ **28 pp. is the LENGTH; 35 is the LIMIT — do not conflate.** The conditional on the court reporter did not bite |
| **2026-08-11** | Defense response due, 35-page limit | pending |
| **2026-08-18** | State's reply due, **18**-page limit | pending |
| **2026-09-01, 10:00 a.m.** | **Oral argument** — **in person**, "up to two hours per side" | pending. ⚠ **Known conflict — see below.** **Still standing as of Run 1 (2026-07-28)**; no continuance motion found, but see the run's scope caveat |
| after 09-01 | Bindover ruling; death-penalty posture | pending |

⚠ **A continuance precursor is already on the record.** When Graf set 09-01, **Ms. Nester asked to move it** — "I'm going to be in trial that week and I'd really like to be here for this argument. Is there any way we could just do it the next week?" The court declined ("This is a fortunate opening") and she accepted. **The date is firm as set, but lead defence counsel has a stated trial conflict with it.** Treat any defence filing between now and 09-01 as a possible motion to continue, and check for one specifically. *(Day 4, 08:19:13–08:19:31.)*

**Also outstanding from Day 4:** the Kirk family's request to display the **full Exhibit 12.1** in open court was reserved to the end of the defence case. Whether it was played on Day 5 is unknown (CR-ACQ §8 item 12).

**As of 2026-07-28 Tyler Robinson has NOT been bound over for trial.** Presumption of innocence applies throughout.

## What each run checks

1. **New filings** on the docket or in public mirrors — the three briefs above, and **the ruling on the bullet-fragment motion** (CR-ACQ §8, still unobtained).
2. **New transcripts** — Rev, for any further proceedings. **Note the slug trap:** Day 1 sat at `ut-v-tyler-robinson---day-1`, not the `...-preliminary-hearing-day-N` pattern the other four use. Do not conclude "not published" from a 404 on a guessed slug (QUEUE.md hazard 5).
3. **Rulings or scheduling changes** — anything moving the 09-01 date. **Check specifically for a defence motion to continue**: lead counsel stated a trial conflict with that week on the record and was declined (see the calendar note). This is a named, expected risk, not a hypothetical.
4. **Nothing else.** This is not a news watch. Media coverage of the case belongs to the Owens corpus work (QUEUE.md Q-20…Q-26), not here.

## What each run may and may not do

**May, without asking:** acquire and bank filings, transcripts and orders; log the retrieval with date and URL; note failed routes as access-path caveats; update the table above with an observed status.

**Must NOT, ever:** change a case-posture statement in any topic file; resolve a register entry; characterise a filing's contents beyond its title and date; or infer an outcome from a filing's existence. **Case posture is a `human` gate in every mode** (LOOP.md §3) — and D-51 is the reason: a posture "correction" made from a transcript service's page metadata propagated into five files before it was caught.

**Escalate immediately** (do not wait for the next run) if: a bindover ruling issues; the 09-01 date moves; a filing is sealed or unsealed; or a route that previously worked starts failing.

## Output

Append to `files - Court record/CR-WATCH-log.md` — one row per run: date, what was checked, what was found, what failed. **A run that finds nothing still writes a row.** A watch with gaps in its log is indistinguishable from a watch that was not running.

## Access routes

| Route | Status |
|---|---|
| Utah XChange | **paywalled** — $10 one-time / $25 + $40 mo. **Human gate; no account exists** (QUEUE.md Q-31) |
| Outlet-mirrored filings | open; how both banked motions were obtained |
| Rev transcripts | open; mind the slug trap |
| DocumentCloud project 224251 | bot-gated (403/JS); needs an interactive browser (Q-32) |
| Utah Courts press notices | `legacy.utcourts.gov/utc/news/` — **Tier 2, RETRIEVED 2026-07-28 (Run 1); route works.** One Robinson entry only (2026-07-06, hearing-week logistics); nothing after 07-10 |
| abc4.com | ⚠ **NEWLY BOT-BLOCKED (403)** as of Run 1 — article text and the case timeline both unretrievable |
| Utah County Attorney media page | `atty.utahcounty.gov/media` — **open, retrieved 2026-07-28.** Latest Robinson item 2026-06-26; briefs not posted there |

## Scheduling note

`CronCreate` in this harness is **session-only and auto-expires after 7 days** — it cannot carry a watch to 2026-09-01. Durable execution needs a **cloud routine** (`/schedule`). This file is the spec either runs from; if neither is running, the file is still the checklist for doing it by hand.

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.2** | **2026-07-28** | **Run 1 executed — the spec has a log for the first time** (`files - Court record/CR-WATCH-log.md`). Calendar table updated with two **observed statuses**, which is what §"What each run may and may not do" expressly permits: the **State's opening brief is reported filed 2026-07-28** (T1 via T3, single independent source, document not held, contents deliberately unrecorded → **Q-45**), and the **09-01 argument still stands** with no continuance motion found. Access-route table updated on three counts: **`legacy.utcourts.gov` retrieved for the first time** (route works; nothing after 2026-07-06), **abc4.com newly 403 bot-blocked**, and the **Utah County Attorney media page** added as an open route that does not carry the briefs. **A previously unknown proceeding surfaced** — a contempt hearing c. 2026-06-22, absent from the library's five-day inventory (→ Q-46). **No case-posture statement in any topic file was altered and no register entry moved.** |
| **1.1** | **2026-07-28** | **Q-43 — the calendar is now sourced from a Tier 1 artifact instead of a news report.** v1.0 carried these dates at Medium-high from Deseret while the transcript that set them sat banked and unread in this repository. **This file's own prohibition — "Must NOT, ever: change a case-posture statement in any topic file" — was written on the strength of D-51, and the same file's calendar was itself second-hand.** Canonical source is now **CR-ACQ §5.1**. Added to the table: **page limits (35 / 35 / 18)**; oral argument **in person, "up to two hours per side"**; and the fact that **the State's 07-28 date was expressly conditional** on the court reporter delivering by 2026-07-13, so a slip there may signify nothing. ⚠ **Most operationally significant:** **Ms. Nester asked to move the 09-01 argument** — she is in trial that week — **and the court declined.** §"What each run checks" item 3 was watching for "anything moving the 09-01 date" while not knowing a named precursor already existed; it now instructs a specific check for a defence motion to continue. Also flagged: the reserved Exhibit 12.1 publication request, unresolved on the portion of Day 5 read. |
| 1.0 | 2026-07-28 | Initial spec. Calendar through the bindover ruling; per-run checks with the Rev slug trap called out; hard prohibition on touching case posture, written directly out of the D-51 failure; escalation triggers; logging rule that a null run still writes a row. |
