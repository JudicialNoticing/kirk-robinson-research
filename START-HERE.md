# START HERE — next session

**Written:** 2026-07-28 at session close. **Read this first, then [QUEUE.md](QUEUE.md).**
This is a snapshot with dates in it. **If you are reading this well after 2026-09-01, it is stale** — the docket section below will have resolved one way or the other, and the work order should be re-derived from QUEUE.md.

---

## 1. First five minutes, in this order

```bash
cd ~/Documents/"Kirk Robinson Research"
git pull                 # nothing else has been writing here, but check
./queue-check.sh         # queue + register integrity; must print RESULT: clean
./tsearch.py --validate  # transcript search method still works
```

Then read **[QUEUE.md](QUEUE.md)** — the dispatchable work graph — and the **standing hazards** at the bottom of it. There are eight; two were added on 2026-07-28 and are new to you (§5 below).

**The loop is DISARMED.** Cron `28cde284` was cancelled on 2026-07-28 before it ever fired. **Zero cycles have run**; every queue item is in its authored state. Re-arming spec is inline at the top of QUEUE.md.

## 2. TIME-CRITICAL — do the docket check before anything else

This is the only part of the project with real deadlines, and **nothing is watching it**. `DOCKET-WATCH.md` is a written spec with no runner attached — session crons expire in 7 days and cannot reach September.

| Date | Event | What to check |
|---|---|---|
| **2026-07-28** | **State's opening probable-cause brief was due** — the day this file was written | **Did it land?** ⚠ The date was **expressly conditional** on the court reporter delivering the transcript by 2026-07-13 (CR-ACQ §5.1). **A slip may mean the reporter, not the case** — do not read anything into it without evidence |
| **2026-08-11** | Defense response due, 35 pages | filed? |
| **2026-08-18** | State's reply due, 18 pages | filed? |
| **2026-09-01, 10:00 a.m.** | **Oral argument** — in person, ~2 hrs/side | ⚠ **Check specifically for a defence motion to continue.** Ms. Nester told the court she is in trial that week and asked to move it; Graf declined. **A named continuance risk is on the record** |
| after 09-01 | Bindover ruling | escalate immediately if it issues |

**Also still unobtained and still wanted:** the ruling on the bullet-fragment / VCM motion (CR-ACQ §8 item 4). It has been open since the first acquisition pass.

**Read `DOCKET-WATCH.md` for what a run may and may not do.** The hard rule: acquire and bank freely; **never change a case-posture statement** — that is a `human` gate in every mode, and D-51 is why.

## 3. Three things only you can decide

These are `human`-gated. They will sit here forever until you rule on them.

| | What | What it needs from you |
|---|---|---|
| **Q-42** | The chamber-case identity is **sworn testimony**, not the "Medium-high inference" CR-E02 §4 records — Faumuina mapped ATF Exhibits 2, 3–5 and 18A to provenance outright (day4 05:39:52). Re-grading would relax a caveat on **D-48** | A yes/no. It is gated because **D-48 has already moved four times**, past LOOP.md §4's hard stop. **The direction of D-48 does not change either way** — only the strength of a caveat |
| **Q-41** | The claude.ai project material — files and ~3 chats, last seen 2026-07-28 | **Not reachable from this environment.** Export to disk, paste the text, or give artifact URLs (those *are* fetchable) |
| **Q-26** | Inventory the Owens post-series corpus — **~35 case-relevant episodes** at roughly BOC-E08 cost each | This is **a programme, not a task**. If yes, start with the Q-20 carrier check, then Eps 319/320/327/328/360/361/362 — not chronologically |

Two smaller ones: **Q-31** (Utah XChange — $10 one-time or $25 + $40/mo, would open the docket directly) and **Q-32** (DocumentCloud project 224251, bot-gated, needs a live browser session you drive).

## 4. Recommended work order, and why

The last two sessions built a **court-record corpus** — five files on primary filings and sworn testimony. **None of it has been fed into the topic folders it was gathered for.** That gap is now the most valuable thing in the queue, because CLAUDE.md is unambiguous that *the deliverable is the files*, and five topic folders are still thin or unsourced.

**Suggested sequence:**

1. **Docket check** (§2) — minutes, time-critical, do it first regardless.
2. **Q-01 — read Day 1.** The only hearing day never read; 327k chars. Contains **Hull's first tranche** — he "resumed" direct on Day 2, so an earlier block of the surveillance-video testimony exists that the library has never seen. Highest single unknown left in the transcripts.
3. **Q-14 — Faumuina's Day 2 turns.** Cheap (58 turns) and **re-ranked upward on 2026-07-28**: she reads FBI DNA results into the record at 05:10:57, including the towel-and-screwdriver material CR-E03 §5 flags as having unknown likelihood ratios. Best value-per-minute in the queue.
4. **Q-11 — the rest of Oliver (Day 5).** Short, and it also settles **whether the full Exhibit 12.1 was ever played in open court** — a ruling Graf reserved at the close of Day 4 that nobody has tracked.
5. **Q-06 — Bakker past her opening + Exhibit 31.** ~384 turns; the likelihood ratios behind the towel and screwdriver inclusions.
6. **Then feed the topic folders — Q-07 to Q-10.** Losee building (62 lines, still no primary sourcing), DNA evidence, the Twiggs profile, arrest chronology. **This is where the reading turns into the library.** Q-09 is `human`-gated (living person; must record the use immunity from both offices).

**If you only have one short session:** do §2, then Q-14. **If you have a long one:** Q-01.

## 5. Traps — two of these are new since you last worked here

1. **Exhibit numbers are not unique across parties.** The State and the defence each have an "**Exhibit 19**" on Day 4 and the transcript renders both bare. State's 19 = the fired cartridge case from the chamber. The defence's 19 = three bullet-comparison photographs, **unadmitted** when shown. **Always write "State's" or "the defence's."** *(New 2026-07-28.)*
2. **Over-hedging is a defect too.** Two corrections have now run *toward* the State — the Dremel identification and the chamber-case identity — both because a summary graded down what the record states outright. **A caveat the evidence does not support is as much an error as a claim it does not support.** *(New 2026-07-28.)*
3. **Rev page dates are publication dates**, lagging each proceeding by one business day. The hearing ran **2026-07-06 → 07-10**. This has been wrong once (D-51) and is now confirmed three ways.
4. **Selective quotation** — a quotation by an interested party is reliable as to the words, never as to the document.
5. **Provenance is a separate verification act** — a forensic report is silent about where its exhibits came from.
6. **Keyword sampling finds topics and misses conclusions.** It has cost this project real accuracy twice; the answer usually sits a few questions past the keyword that located the subject.
7. **A search null is a claim about the search** until validated against a known positive. Use `./tsearch.py`, which does that automatically before every query.
8. **Grep, then read the hit** — forward-looking "next is D-nn" notes have matched the pattern five times without yet causing an error.

## 6. Where things stand as of 2026-07-28

- **Register:** D-1 – D-51, no gaps, next number **D-52**. Nothing was assigned or moved on 2026-07-28.
- **Transcripts:** Days 2–5 banked; Day 4 read end to end; Days 2/3/5 read in part; **Day 1 banked and entirely unread**.
- **Exhibits:** none obtained. 30, 31, 32, 33, 34, the surveillance compilations and Karner's case file are all known only through witnesses describing them.
- **Certified transcript:** not obtained (Q-36). Every quotation in the library is against Rev's commercial rendering.
- **Audits:** three passes done. CR-AUDIT-2026-07-27 and BOC-AUDIT-2026-07-27B were **self-audits**; **CR-AUDIT-2026-07-28 (Q-02)** was run independently and found six defects, three material. **A human read is still owed** — every pass so far has been the same model checking itself.
- **Last two commits:** `ebf3345` (Q-02, the independent pass) and `a12377a` (Q-43, briefing schedule promoted to Tier 1). Working tree clean, pushed to `origin/main`.

## 7. One thing worth doing that is not in the queue

**Set up a durable docket routine.** `DOCKET-WATCH.md` is a good spec with nothing running it. A cloud routine via `/schedule` — weekly until 2026-08-11, then twice-weekly through 2026-09-01 — would cover the whole briefing window. **This is a user action; it cannot be done from inside a session**, and it is the one failure in this project that cannot be caught up later.
