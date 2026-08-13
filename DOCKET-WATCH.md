# DOCKET WATCH — *State of Utah v. Robinson*, Case No. 251403576

**Why this is separate from [LOOP.md](LOOP.md):** the research queue is paced by work available. **This is paced by a court calendar** (LOOP.md §5). Missing a filing window is the one failure here that cannot be caught up later.
**Prepared:** 2026-07-28 · **Runs until:** the bindover ruling, then re-scope. · **Status:** **v1.4 — Runs 1, 2 and 3 executed (2026-07-28, 2026-08-01, 2026-08-13)**; log at [CR-WATCH-log.md](files%20-%20Court%20record/CR-WATCH-log.md)

> 🚨 **THE WATCH WENT DARK 2026-08-01 → 2026-08-13 AND DID NOT NOTICE.** Three scheduled firings (Wed 08-05, Sat 08-08, Wed 08-12) wrote no rows, and **the 2026-08-11 defence deadline — this file's own named "next checkpoint" — passed unchecked.** Run 3 (2026-08-13) is a catch-up pass; no rows were backfilled. **The case did not suffer for it** (the brief is now banked, 09-01 stands, no continuance motion surfaced) — **but that was luck, not the system working.** Two owner actions close the hole: **(1) confirm `trig_016faLfbQWCz72M463Dy8HsL` is still alive in `/schedule` — next firing Sat 2026-08-15, next hard date Tue 2026-08-18; (2) grant the Claude Code GitHub App access to `JudicialNoticing/kirk-robinson-research`**, without which the routine stays report-only and every run depends on a human remembering to paste.
> ⚠ **This file changed on 2026-08-13** (calendar row 08-11 → observed status; new escalation trigger). **The routine's inlined prompt is now out of sync and must be updated to match** — they are not automatically in sync, per the box below.

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
| **2026-08-11** | Defense response due, 35-page limit | ✅ **FILED AND BANKED — observed status set by Run 3 (2026-08-13).** *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* signed and served **Tue 2026-08-11** (certificate of service: e-filed that date). **41 PDF pp.; internal printed numbering to 35.** ⚠ **35 is ALSO the page limit here — length and limit coincide; do not read the coincidence as a finding.** **This is the first primary filing the project holds as a document rather than through reporting** — banked at `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.pdf`. ⚠ **Provenance is two-of-three: signature block ✅, certificate of service ✅, clerk file-stamp ❌ not visible** — outlet-hosted, carrying the defence's own attestation. **Contents deliberately unread** (→ a CR-E evidence file, not a watch row) |
| **2026-08-18** | State's reply due, **18**-page limit | pending — **THE NEXT HARD DATE.** Corroborated as Tue 2026-08-18 by the reported briefing schedule and by CR-ACQ §5.1 |
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

> 🚨 **NEW TRIGGER, added 2026-08-13 after the watch went dark for 12 days: THE WATCH ITSELF HAS STOPPED.**
> **Escalate if `CR-WATCH-log.md` has no new row within 4 days of a scheduled firing.** Every other trigger on this list describes an event *in the case*; none described a failure *of the watch* — which is exactly why three consecutive firings (2026-08-05, 08-08, 08-12) produced nothing and **the 2026-08-11 defence deadline, named in this file as the next checkpoint, passed unchecked.** The gap was found from outside this repository, by file mtime, during an unrelated session. **A watch that cannot detect its own silence is not a watch.**
> ⚠ **This trigger is checkable by anyone from the log's mtime alone and does not depend on the routine working.**

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
| **1.4** | **2026-08-13** | **Run 3 logged, and the spec gained the trigger whose absence let the watch go dark for 12 days.** 🚨 **Three scheduled firings (2026-08-05, 08-08, 08-12) produced no rows**, and the **2026-08-11 defence deadline named in this file as "the next checkpoint" passed unchecked**; the gap was found from outside this repository by file mtime, not by the watch. **New escalation trigger added — "the watch itself has stopped": escalate if `CR-WATCH-log.md` has no new row within 4 days of a scheduled firing.** Every prior trigger described an event *in the case*; none described a failure *of the watch*, and the new one is deliberately checkable from the log's mtime alone so it does not depend on the routine working. **Calendar updated with an observed status, as §"What each run may and may not do" expressly permits: the 2026-08-11 defence response is FILED AND BANKED** — *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* signed and served Tue 2026-08-11, 41 PDF pp. / 35 printed, **the first primary filing this project holds as a document rather than through reporting.** ⚠ **Provenance two-of-three — signature block and certificate of service present, no clerk file-stamp visible** — so it is recorded as outlet-hosted document text carrying the defence's own attestation, **not silently promoted** to a stamped filing. ⚠ **Length 35 coincides with the 35-page limit; recorded, explicitly not read as a finding** (the inverse of Run 2's conflation hazard). **The 09-01 argument stands, upgraded to a Tier 2 named-official source** dated 2026-08-11. **No continuance motion found, scope stated** (open routes only; no docket; a filing in the last 48 hours would likely not yet be reported — not evidence of absence). **The brief's contents are deliberately unread**, and a second restraint is logged over material touching a private individual's gender identity that the extraction surfaced incidentally. **No case-posture statement altered; no register entry moved.** ⚠ **The routine's inlined prompt is now out of sync with this file and must be updated.** |
| **1.2** | **2026-07-28** | **Run 1 executed — the spec has a log for the first time** (`files - Court record/CR-WATCH-log.md`). Calendar table updated with two **observed statuses**, which is what §"What each run may and may not do" expressly permits: the **State's opening brief is reported filed 2026-07-28** (T1 via T3, single independent source, document not held, contents deliberately unrecorded → **Q-45**), and the **09-01 argument still stands** with no continuance motion found. Access-route table updated on three counts: **`legacy.utcourts.gov` retrieved for the first time** (route works; nothing after 2026-07-06), **abc4.com newly 403 bot-blocked**, and the **Utah County Attorney media page** added as an open route that does not carry the briefs. **A previously unknown proceeding surfaced** — a contempt hearing c. 2026-06-22, absent from the library's five-day inventory (→ Q-46). **No case-posture statement in any topic file was altered and no register entry moved.** |
| **1.1** | **2026-07-28** | **Q-43 — the calendar is now sourced from a Tier 1 artifact instead of a news report.** v1.0 carried these dates at Medium-high from Deseret while the transcript that set them sat banked and unread in this repository. **This file's own prohibition — "Must NOT, ever: change a case-posture statement in any topic file" — was written on the strength of D-51, and the same file's calendar was itself second-hand.** Canonical source is now **CR-ACQ §5.1**. Added to the table: **page limits (35 / 35 / 18)**; oral argument **in person, "up to two hours per side"**; and the fact that **the State's 07-28 date was expressly conditional** on the court reporter delivering by 2026-07-13, so a slip there may signify nothing. ⚠ **Most operationally significant:** **Ms. Nester asked to move the 09-01 argument** — she is in trial that week — **and the court declined.** §"What each run checks" item 3 was watching for "anything moving the 09-01 date" while not knowing a named precursor already existed; it now instructs a specific check for a defence motion to continue. Also flagged: the reserved Exhibit 12.1 publication request, unresolved on the portion of Day 5 read. |
| 1.0 | 2026-07-28 | Initial spec. Calendar through the bindover ruling; per-run checks with the Rev slug trap called out; hard prohibition on touching case posture, written directly out of the D-51 failure; escalation triggers; logging rule that a null run still writes a row. |
