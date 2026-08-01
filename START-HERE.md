# START HERE — next session

**Written:** 2026-08-01 at session close. **Read this first, then [QUEUE.md](QUEUE.md).**
This is a snapshot with dates in it. **If you are reading this well after 2026-09-01 it is stale** — the docket section will have resolved one way or the other, and the work order should be re-derived from QUEUE.md.

---

## 1. First five minutes, in this order

```bash
cd ~/Documents/"Kirk Robinson Research"
git pull                 # nothing else has been writing here, but check
./queue-check.sh         # queue + register integrity; must print RESULT: clean
./tsearch.py --validate  # transcript search method still works
```

Then read **[QUEUE.md](QUEUE.md)** and the **standing hazards** at the bottom of it. ⚠ **Two of them changed on 2026-08-01 — hazard 10 was CORRECTED because it was wrong, and hazard 9 was WIDENED.** See §5.

**Expect `queue-check.sh` to list SIX files under "Provisional findings outstanding." THREE are real.**

| File | Real? |
|---|---|
| **CR-E06** (Bakker/Oliver) | ✅ **GENUINELY PROVISIONAL — and deliberately so, at v1.1.** Q-58 **did** run: **126 candidates, 8 tested, 6 CONFIRMED and corrected in place.** ⚠ **The marking was NOT cleared: a 6-of-8 hit rate with 61 material candidates untested is evidence the file has more.** **May not be cited elsewhere** → **Q-58 stays OPEN** |
| **CR-E03** (Days 2/3/5) | ✅ **GENUINELY PROVISIONAL as to its §5A** (Q-14 findings) |
| **CR-E05** (Day 1) | ❌ **FALSE POSITIVE — this file is now VERIFIED (v1.1).** Q-54 ran on 2026-08-01 and the marking was cleared; the validator matches the token in the historical revision log and in §9.4's *statement that it was cleared* |
| **START-HERE.md** | ❌ **FALSE POSITIVE** — this file merely discusses the marker |
| **CR-AUDIT-2026-08-01** | ❌ **FALSE POSITIVE** — same reason |
| **`2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md`** | ✅ **REAL, and stronger than provisional — it is UNREVIEWED.** A complete Losee draft whose adversarial review never ran. **Do not publish it, do not cite it, do not copy it into the topic folder. Run the review** (work order item 2) |

**The validator pattern-matches the token rather than reading the hit. That bug is still unfixed, deliberately:** a smarter matcher risks a false *negative*, which would let an unverified finding escape. **A noisy validator is the safe failure direction.**

## 2. The docket — the scheduler EXISTS now, and 08-11 is the next hard date

**A durable cloud routine was created 2026-08-01: `trig_016faLfbQWCz72M463Dy8HsL`, Wednesdays and Saturdays 09:00 ET, first firing 2026-08-05.** Wednesday/Saturday is deliberate — **all three briefing dates are Tuesdays**, so a Wednesday run lands the morning after each.

⚠ **IT IS REPORT-ONLY, AND THAT IS THE ONE THING STILL WAITING ON YOU.** The cloud environment was refused access to the private repo (`HTTP 403`). **The routine runs the checks and produces a report but cannot commit** — its output must be **pasted into `CR-WATCH-log.md` by hand** until the Claude Code GitHub App is granted access to `JudicialNoticing/kirk-robinson-research`.

| Date | Event | Status as of 2026-08-01 (Run 2) |
|---|---|---|
| 2026-07-06 → 07-10 | Preliminary hearing, five days | **held**; **all five days now read in full** |
| 2026-07-28 | State's opening brief | ✅ **filed** — now **multi-sourced across six outlets** (Run 1 had one). ⚠ **28 pp. is the LENGTH; 35 was the LIMIT.** **A public Scribd mirror now exists** → **Q-56** |
| **2026-08-11** | **Defence response** | **pending — THE NEXT CHECKPOINT**, and the likeliest vehicle for a continuance motion |
| 2026-08-18 | State's reply | pending |
| **2026-09-01, 10:00** | **Oral argument**, in person, 4 hours total | pending. **Still standing.** ⚠ Nester's trial-week conflict remains an open, named risk |
| after 09-01 | Bindover ruling | pending. **Robinson has NOT been bound over** |

**Run 2 also:** re-opened the **DocumentCloud API** (project 224251 enumerated for the first time — 46 documents) while the web UI stays gated, so **Q-32 is now SPLIT, not closed**; found a **new unheld filing of 2026-07-09**, made *during* hearing week → **Q-57**; and put **two dates in play for Q-46** (a contempt *hearing* c. 06-22 and a contempt *ruling* 06-26 — **not established to be the same event**).

## 3. Still only you can decide these

| | What | What it needs from you |
|---|---|---|
| ⚠ **The repo grant** | The docket routine can't commit | **Install/grant the Claude Code GitHub App** on the private repo. Until then, paste its reports in by hand |
| **Q-42** | Re-grade the chamber-case identity to sworn testimony | A yes/no. **D-48 has moved four times — past LOOP §4's third-movement stop** |
| **Q-50** | Does Oliver's household-transfer explanation reach the towel and screwdriver, which were **not** in the household? | Bears on a living person under use immunity who is not accused. **Recorded at CR-E06 §3.4 and expressly NOT answered** |
| **Q-51 / Q-15** | State's Exhibit 11, the ME report — in evidence since 07-06 | Q-15 is human-gated; this inherits |
| **Q-41** | The claude.ai project material | Export, paste, or artifact URLs |
| **Q-26** | The ~35-episode Owens programme | A programme, not a task |
| **Q-31 · Q-32(b)** | Utah XChange ($10) · DocumentCloud web UI | Money · a browser you drive |

## 4. Recommended work order

⚠ **A 45-agent round was launched on 2026-08-01 and STOPPED at 15 returned. Only Q-58 completed.** Everything below is what remains, in order.

1. ⚠ **Q-58 — FINISH IT. 61 material candidates are untested.** The 8 that were tested returned **6 confirmed defects**, two of them assertions the record contradicts. **Until this completes, CR-E06 is `[PROVISIONAL]` and NOTHING may cite it — which is what currently blocks the DNA folder.** Candidates are in `CR-ACQ-.../2026-08-01_round2-Q58-raw-output.json`.
2. ⚠ **Q-07 — RUN THE REVIEW, do not publish the draft.** A complete 85.6k-char Losee draft exists at `CR-ACQ-.../2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md`; **its adversarial review was in flight when the session closed and never ran.** An unreviewed draft is not a finding.
3. **Q-08 (DNA) and Q-10 (arrest chronology)** — never started. ⚠ **Q-08 is gated behind item 1**: the drafter cannot carry D-53, the consumption record or the LR-of-1 while CR-E06 is provisional. **The Losee drafter already proved this bites** — it excluded the six consumed northeast-corner swabs, which is literally "what was recovered at the drop point."
4. **Q-55 — the second cycle on Q-54's residue.** ✅ **The dedup is already rebuilt and verified**: Jaccard clustering collapsed **20 duplicates the old prefix key missed** (it collapsed zero). **103 material clusters; 18 were selected and none tested.** Candidate list at `scratchpad/q55-candidates.json`; regenerate if the scratchpad is gone.
5. **Q-56 — bank the State's brief** from the Scribd mirror. ⚠ **Provenance is a SEPARATE act**: file-stamp, signature block, certificate of service. Until then it is an upload, not a filed document.
6. **Q-48, Q-46, Q-47, Q-57** — the unheld primary documents. ⚠ **Q-46 now has TWO dates in play** (a contempt *hearing* c. 06-22, a contempt *ruling* 06-26) — **not established to be the same event.**

## 5. Traps — two changed on 2026-08-01

1. ⚠ **HAZARD 10 WAS WRONG AND IS NOW CORRECTED.** It said "the clock jumps across every recess." **It does not.** On **Days 1 and 2 the recording runs *through* every recess as dead air** — the Day 2 "~1 hour discontinuity" **is the lunch recess, recorded** — so **a duration measured across a recess is REAL** (this is why Day 1's "ten-minute" break genuinely ran twenty-two minutes). **What remains forbidden: converting a timestamp to a time of day** — good only to ±5 min, and must be marked approximate. ⚠ **Days 3–5 UNTESTED.**
2. ⚠ **HAZARD 9 IS WIDER THAN IT SAID.** Not only do witness answers carry counsel's label — **a party's advocate's argument can carry the OPPOSING party's counsel label** (Day 5: one "Mr. McBride" label covers both the prosecutor and media counsel, in adjacent turns the judge distinguishes). **More dangerous than the Day 1 failures**, because an argument's content does not announce whose it is the way an answer does. **Infer every speaker from content; where label and content disagree, content wins.**
3. **Exhibit numbers are not unique across parties — and now not across witnesses either.** "Exhibit 30" is both a NIST publication and a DNA report; "Exhibit 31" appears as State's, People's and plaintiff's. ⚠ **One court ruling admits a chart under the wrong number on its face** (D-55).
4. ⚠ **Over-hedging is a defect too — it bit again.** CR-E05 refused in bold to identify "Falmina" as Sgt. Jennifer Faumuina; **Day 1 names her correctly at 24:19.** Caution that reads as rigour is still error.
5. **A search null is a claim about the search.** Validate the method first — `./tsearch.py --validate`.
6. **Grep, then read the hit.** ⚠ **`queue-check.sh` reports a "highest string" one above the true register ceiling. It counts strings, not assignments.**
7. **Selective quotation** is reliable as to the words, never as to the document. **Provenance is a separate verification act.** **Keyword sampling finds topics and misses conclusions.** **Rev page dates are publication dates.**
8. ⚠ **NEW, and it generalises: A CAVEAT IS A CLAIM, AND CLAIMS NEED VERIFICATION ACTS.** Hazard 10 was wrong for weeks because a *caution* felt safe — it only ever restricted what could be said. **Hazards 1–8 have never been tested either.** Treat every standing hazard as unverified until some cycle has actually checked it.

## 6. Where things stand as of 2026-08-01

- **Register: D-1 – D-58, no gaps. Next is D-59.** **D-52 RESOLVED**; **D-53–D-58 opened** (CR-E06 §7), all OPEN.
- **Transcripts: ALL FIVE HEARING DAYS ARE NOW READ IN FULL.** The last two large unread bodies — **Bakker's ~384 turns and Oliver's Day 5 testimony** — were closed on 2026-08-01. **There is no longer a large unread transcript body.**
- **Files: ten in `files - Court record`** — CR-ACQ, CR-E01…**CR-E06**, CR-WATCH-log, and three audits.
- **Exhibits: still none obtained.** ⚠ **State's Exhibit 31 — the decisive artifact for D-53 — has never been read.** The State's brief is **located, not banked**.
- **CR-E05 is VERIFIED.** ⚠ **But on 16 of 229 candidates — 213 are untested** (Q-55).
- **CR-E06 is v1.1 and STILL `[PROVISIONAL]`, deliberately.** Q-58 tested 8 of 69 material candidates and **6 were confirmed defects.** ⚠ **The reasoning is worth reusing: clearing is a judgement about the UNTESTED remainder, not a tally of the tested part.**
- ⚠ **Two of this session's own files asserted things the record contradicts** — CR-E05 §5's D-52 hypothesis, and CR-E06 §2.5's scoped null. **Both were caught only by a cycle reading the primary source.** Neither would have been caught by re-reading the write-up.
- **The loop is still DISARMED.** Zero cycles. **DOCKET-WATCH has run twice, both by hand**, and now has a scheduler.
- **Working tree clean, pushed to `origin/main`.**

## 6A. ⚠ The single most reusable lesson of 2026-08-01

**Every substantive error found this session was an assertion that felt safe.** The recess caveat felt safe because it only ever *restricted* what could be said. CR-E05's D-52 hypothesis felt safe because it was hedged as "most likely." CR-E06's "not stated on the record" felt safe because it was a null. **All three were wrong, and all three were caught only by a cycle that went back to the transcript rather than re-reading the write-up.**

**The operational rule:** a caveat, a hedge and a null are all **claims**, and claims need verification acts. **Verifying what a file *says* cannot find what it never said, and cannot test what it merely assumed.**

## 7. What 2026-08-01 actually changed, in one paragraph

The evidence half of this project ran out of unread transcript: **all five hearing days are now read in full**, and the last two witnesses turned out to carry the most consequential evidentiary finding the library has — that **both headline DNA statistics assume Lance Twiggs is a contributor in both of their competing propositions**, so the statistic never tests his presence, while **the only likelihood ratio ever run on him alone was 1, "uninformative."** The verification half learned that **CR-E05's headline findings all survive** but that it **read the witnesses well and the courtroom poorly** — and, more usefully, that **a caveat this library had propagated to every file was itself never verified, and was wrong.** The docket half acquired a scheduler and a route to the State's brief. **And the thing that has been owed since the beginning is still owed: every pass, including the adversarial one, has been the same model checking itself.**
