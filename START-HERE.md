# START HERE — next session

**Written:** 2026-07-28 at session close (second session that day). **Read this first, then [QUEUE.md](QUEUE.md).**
This is a snapshot with dates in it. **If you are reading this well after 2026-09-01, it is stale** — the docket section will have resolved one way or the other, and the work order should be re-derived from QUEUE.md.

---

## 1. First five minutes, in this order

```bash
cd ~/Documents/"Kirk Robinson Research"
git pull                 # nothing else has been writing here, but check
./queue-check.sh         # queue + register integrity; must print RESULT: clean
./tsearch.py --validate  # transcript search method still works
```

Then read **[QUEUE.md](QUEUE.md)** and the **standing hazards** at the bottom of it. **There are now ten; hazards 9 and 10 are new and hazard 9 is the most dangerous one this project has found** (§5 below).

**Expect `queue-check.sh` to report three files under "Provisional findings outstanding" — and only two of them are real.**
- **CR-E03 and CR-E05 genuinely carry `[PROVISIONAL]` findings.** **Neither may be cited elsewhere until a verification cycle clears it** (LOOP.md §2). **CR-E05 is the urgent one — see §4.1.**
- **This file is a false positive.** `queue-check.sh` **pattern-matches the token rather than reading the hit**, so it fires on any file that merely *discusses* the marker. CR-AUDIT-2026-07-28 §7 recorded this bug — "standing hazard 6 living inside the validator that enforces the other hazards" — and it is **still unfixed, deliberately**: a smarter matcher risks a false *negative*, which would let an unverified finding escape unnoticed. **A noisy validator is the safe failure direction here.**

## 2. The docket — the State's brief LANDED, and the watch has run once

**`DOCKET-WATCH.md` was executed for the first time on 2026-07-28.** It had been a spec with no runner attached since it was written. **Run 1 is logged at [`files - Court record/CR-WATCH-log.md`](files%20-%20Court%20record/CR-WATCH-log.md).**

| Date | Event | Status as of 2026-07-28 |
|---|---|---|
| 2026-07-06 → 07-10 | Preliminary hearing, five days | **held** |
| **2026-07-28** | State's opening probable-cause brief, 35 pp. | ✅ **REPORTED FILED** — T1 via T3, **one** independent source (Fox News, pub. 20:38 EDT). **The document is NOT held and its contents are deliberately unrecorded** → **Q-45.** The court-reporter conditional did not bite |
| **2026-08-11** | Defense response, 35 pp. | pending — **the next checkpoint, and the likeliest vehicle for a continuance motion** |
| **2026-08-18** | State's reply, 18 pp. | pending |
| **2026-09-01, 10:00** | **Oral argument**, in person | pending. **Still standing as of Run 1**; no continuance motion found. ⚠ **Nester's trial-week conflict remains an open, named risk** |
| after 09-01 | Bindover ruling | pending. **Robinson has NOT been bound over** |

**Run 1 also turned up a proceeding the library did not know existed:** a **contempt hearing c. 2026-06-22** (Rev page dated 06-23) → **Q-46**. And a **Kirk-family motion of 2026-07-10** asking for a probable-cause determination by Sept. 1 → **Q-47**.

**Route changes:** `legacy.utcourts.gov` **now retrieved** and holds nothing after 07-06; **abc4.com is newly 403 bot-blocked**; DocumentCloud 224251 still bot-gated.

## 3. Still only you can decide these

| | What | What it needs from you |
|---|---|---|
| **The durable docket routine** | `DOCKET-WATCH.md` now has a log and a proven method, but **still no scheduler**. Session crons expire in 7 days and cannot reach September | **A `/schedule` cloud routine** — weekly to 08-11, then twice-weekly to 09-01. **This is the one failure that cannot be caught up later.** I did not create it: it is durable and outward-facing, and wanted your explicit go |
| **Q-42** | Re-grade the chamber-case identity from "Medium-high inference" to sworn testimony | A yes/no. **D-48's direction is unaffected either way** |
| **Q-51** | **State's Exhibit 11 — the nine-page ME report — has been in evidence since 2026-07-06.** It is **Q-15 / D-49's decisive artifact** (the fragment count) and the library did not know | Q-15 is `human`-gated; this inherits |
| **Q-50** | Does Oliver's household-transfer explanation reach the towel and screwdriver, which were **not** in the household? | Bears on a living person under use immunity who is not accused |
| **Q-41** | The claude.ai project material | Export, paste, or artifact URLs |
| **Q-26** | The ~35-episode Owens programme | A programme, not a task |
| **Q-31 / Q-32** | Utah XChange ($10) · DocumentCloud (needs a browser you drive) | Money · a live session |

## 4. Recommended work order

**The two files written on 2026-07-28 are `[PROVISIONAL]` and one of them is large and unchecked.** That, not new reading, is the top of the queue.

1. **Q-54 — verify CR-E05.** The Day 1 file is ~10× the size of the CR-E03 section whose verification found **6 defects and 14 omissions**. **Assume it contains both.** Run **two** passes — proposition-testing *and* completeness. The session that wrote it learned the hard way that the first cannot find what the file never said.
2. **Q-52 — resolve D-52.** Read the Day 2 re-offer of Exhibit 12.1: what foundation was supplied after Day 1's exclusion, and whether Exhibit 12.3 was amended or replaced. **Cheap, and it closes a register entry opened today.** Deliberately left for an independent reader.
3. **Q-06 — Bakker past her opening** (~384 turns). Now more valuable than before: her cross already yielded the DOJ verbal-scale answer and a clean restatement of the 7.1 figure.
4. **Q-11 — the rest of Oliver (Day 5)**, which also settles CR-ACQ §8 item 12.
5. **Then feed the topic folders — Q-07 to Q-10.** Losee, DNA, Twiggs, arrest chronology. **CR-E05 has just made Q-07 much richer** — Bagley is a first-officer-on-the-roof account the Losee file has nothing like.

## 5. Traps — hazard 9 is new and it is the worst one yet

1. ⚠ **REV'S SPEAKER LABELS ARE NOT EVIDENCE.** *(New 2026-07-28.)* On **Day 1**, **Officer Bagley's sworn answers carry defence counsel Richard Novak's label** — Rev merged witness and cross-examiner into one label. **There is no "Sturgill" label at all**, though he conducts Hull's direct. The **oath is administered under defence counsel's name** on Days 1 and 2, and on Day 5 under **the witness's own name**, which is impossible. One **ruling** is labelled as a prosecutor. **Infer every speaker from content. Where a label and the content disagree, the content wins.**
2. ⚠ **Timestamps are recording-stream time, not time of day** *(new 2026-07-28)* — the clock jumps across every recess. They are identifiers. **Never convert one to a clock time or measure a duration across a recess.** Part-seams can also fall mid-question with words duplicated either side.
3. **Exhibit numbers are not unique across parties.** Always write "State's" or "the defence's."
4. **Over-hedging is a defect too** — three corrections have now run *toward* the State.
5. **Rev page dates are publication dates**, lagging one business day. The hearing ran **2026-07-06 → 07-10**.
6. **Selective quotation** — reliable as to the words, never as to the document.
7. **Provenance is a separate verification act.**
8. **Keyword sampling finds topics and misses conclusions.**
9. **A search null is a claim about the search.** ⚠ **This bit again today**: CR-E03 said two likelihood ratios were "unknown" when they were sitting in a banked transcript the file had declared unread.
10. **Grep, then read the hit** — and note this cost something today too: `queue-check.sh` reports a "highest string" that counts forward-looking "next is D-nn" notes, and CR-AUDIT-2026-07-28 had copied that number into its own register-integrity finding.

## 6. Where things stand as of 2026-07-28 (end of second session)

- **Register: D-1 – D-52, no gaps. Next is D-53.** **D-52 was assigned today and is OPEN** — Exhibit 12.1's Day 1 exclusion (CR-E05 §5).
- **Transcripts: ALL FIVE HEARING DAYS ARE NOW READ AT LEAST IN PART, AND DAY 1 IS READ IN FULL.** Day 4 end to end; Day 1 end to end; Days 2/3/5 in substantial part. **The largest remaining unread body is Bakker's ~384 turns (Q-06).**
- **Files: seven in `files - Court record`** — CR-ACQ, CR-E01…**CR-E05**, two audits, and **CR-WATCH-log**.
- **Exhibits: still none obtained.** But two acquisition targets sharpened today: **Exhibit 11** (the ME report, in evidence) and **Exhibit 31** (published to the broadcast camera in a known 6-minute window, so Day 2 courtroom video may show its pages).
- **Audits: three passes, plus two verification cycles run today** on the Q-14 section. **A human read is still owed** — every pass has been the same model checking itself.
- **The loop is still DISARMED.** Zero cycles have run. **`DOCKET-WATCH` has now run once, by hand.**
- **Working tree clean, pushed to `origin/main`.**

## 7. What today actually changed, in one paragraph

The docket half of this project stopped being theoretical: the watch ran, and the State's brief landed. The evidence half gained **the last unread hearing day**, which turned out to hold **a witness nobody knew about**, **the medical examiner's report in evidence**, and **an exclusion of the central surveillance exhibit that the library's account of that exhibit did not contain**. And the method half learned that **verifying what a file says cannot find what it never said** — the completeness pass found more than the quotation pass, and the transcripts' speaker labels turned out to be unsafe at any speed.
