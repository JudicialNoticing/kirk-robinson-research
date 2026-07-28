# DOCKET WATCH — *State of Utah v. Robinson*, Case No. 251403576

**Why this is separate from [LOOP.md](LOOP.md):** the research queue is paced by work available. **This is paced by a court calendar** (LOOP.md §5). Missing a filing window is the one failure here that cannot be caught up later.
**Prepared:** 2026-07-28 · **Runs until:** the bindover ruling, then re-scope.

## The calendar

| Date | Event | Status |
|---|---|---|
| 2026-07-06 → 07-10 | Preliminary hearing, five days | **held** (D-51, as reversed) |
| **2026-07-28** | **State's opening probable-cause brief due** | **due today — unverified** |
| **2026-08-11** | Defense response due | pending |
| **2026-08-18** | State's reply due | pending |
| **2026-09-01, 10:00** | **Oral argument** | pending |
| after 09-01 | Bindover ruling; death-penalty posture | pending |

**As of 2026-07-28 Tyler Robinson has NOT been bound over for trial.** Presumption of innocence applies throughout.

## What each run checks

1. **New filings** on the docket or in public mirrors — the three briefs above, and **the ruling on the bullet-fragment motion** (CR-ACQ §8, still unobtained).
2. **New transcripts** — Rev, for any further proceedings. **Note the slug trap:** Day 1 sat at `ut-v-tyler-robinson---day-1`, not the `...-preliminary-hearing-day-N` pattern the other four use. Do not conclude "not published" from a 404 on a guessed slug (QUEUE.md hazard 5).
3. **Rulings or scheduling changes** — anything moving the 09-01 date.
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
| Utah Courts press notices | `legacy.utcourts.gov` — Tier 2, unretrieved (Q-?) |

## Scheduling note

`CronCreate` in this harness is **session-only and auto-expires after 7 days** — it cannot carry a watch to 2026-09-01. Durable execution needs a **cloud routine** (`/schedule`). This file is the spec either runs from; if neither is running, the file is still the checklist for doing it by hand.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-28 | Initial spec. Calendar through the bindover ruling; per-run checks with the Rev slug trap called out; hard prohibition on touching case posture, written directly out of the D-51 failure; escalation triggers; logging rule that a null run still writes a row. |
