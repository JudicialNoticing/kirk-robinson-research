# START HERE — next session

**Written:** 2026-08-01 at session close. **Read this first, then [QUEUE.md](QUEUE.md).**
This is a snapshot with dates in it. **If you are reading this well after 2026-09-01 it is stale** — the docket section will have resolved one way or the other, and the work order should be re-derived from QUEUE.md.

---

## 0. SESSION CLOSE — 2026-08-14 (read this first; it supersedes the 2026-08-01 snapshot below wherever they disagree)

**Sixteen commits. Working tree clean and pushed. `queue-check.sh`: RESULT clean.**
**Register: ceiling D-61, next free D-62. Queue runs to Q-78. Standing hazards now run to 12.**

### 🚨 THREE THINGS NEED YOU BEFORE ANYTHING ELSE

| | What | Why it's yours |
|---|---|---|
| ~~**1**~~ | ✅ ~~**Q-53 — the body-camera duration**~~ — **RESOLVED 2026-08-16 (owner decision): the figure is RESTORED at a stated grade and this LOOP §4 hard stop is CLOSED.** The "27 minute and 35 second" duration stands as **defence counsel's characterisation assented to by the witness — not a measurement and not the witness's own words** (`day1.txt` 04:12:40, line 5771, answered "Yes" at 04:12:54). Restored at all five sites; **CR-E05 is v1.3**. | ⚠️ **The ACQUISITION half of Q-53 stays open** — only the recording establishes the actual length. **Two lessons kept:** the refutal failed on an *inflectional* false null (plural searches, singular transcript, a numeral missed by a word search) → **hazard 12**; and its evidence was *sound* — the `27:35` at line 6577 really is a Rev stream timestamp in Hull's testimony, so the error was concluding the figure was **nothing but** that. **A refutal is a claim, and this library verified its findings hard and its refutals not at all.** |
| **2** | **The docket-watch routine** still has **no repository source** in its config. | The prompt is updated and applied; ⚠️ **the GitHub App grant was NEVER the blocker** — `/web-setup` syncs the `gh` token you already have. Then add the repo via `/schedule update`. **And fix the egress**: Edit routine → environment → Network access → Custom/Full. |
| **3** | **Q-60** (register collision) · **Q-62** (file-ID convention — blocks the Losee file ID) · **Q-42** (chamber-case re-grade) · **Q-31** ($10 XChange — would close Q-45 + Q-63 at once) | Standing decisions, unchanged. |

### What the library gained today

- ✅ **THE STATE'S OWN FILINGS → [CR-E08](files%20-%20Court%20record/CR-E08_state-information-and-pc-affidavit-2025-09-16.md)** — the 2025-09-16 Information and PC affidavit. **CR-E07's F-15 is partly cured** (limit: these are the Sept-2025 charging documents, **not** the still-unheld 2026-07-28 brief) and **A-4 upgraded Medium → High: the Information pleads EXACTLY ONE aggravating circumstance** — verified by a cycle that found *"circumstance"* appears **once** in ten pages.
- ✅ **THE FIRST DOCKET → [CR-ACQ-2026-08-14C](files%20-%20Court%20record/CR-ACQ-2026-08-14C_xchange-docket.md)**, coverage **case-filing → 2026-03-14 only**. Q-03 partially executed. The seven charges are now Tier 1.
- ✅ **[CR-E09](files%20-%20Court%20record/CR-E09_evidence-preservation-order-and-pretrial-practice.md)** — the evidence-preservation order. ⚠️ **F-27: it postdates the DNA consumption**, which reframes DNA-E01 §6's open question. **[CR-E10](files%20-%20Court%20record/CR-E10_publicity-order-and-record-classification.md)** — the publicity order located as **docket #23**, and **F-35/F-36: closure in this case is GRANULAR** — a whole hearing sealed on 2025-10-24, and a **witness-specific** partial closure on 2026-02-03. **That bounds every transcript ambition the library has (→ Q-75).**
- ✅ **Q-07's review, fix pass AND re-gate all ran → [CR-REVIEW-2026-08-14](files%20-%20Court%20record/CR-REVIEW-2026-08-14_losee-draft-Q07.md).** Gate: **FAIL** → fixes → re-gate **PASS WITH FIXES**. Draft is **v1.2 and still does not publish**.
- ✅ **Q-61 round 1** (DNA-E01 v4.1): 31 claims tested, **the D-53 headline survives intact**. `[PROVISIONAL]` deliberately not cleared.
- ✅ **The "Twiggs testified under use immunity" error — seven instances across five files, all fixed.**

### ⚠️ What today should teach the next session

**Every verification pass run today found real defects — including three passes run against my own work.** Four errors are worth carrying:

1. 🚨 **A guard can point at the wrong risk.** CR-E10's F-34 named a living attorney beside an adverse judicial finding, under three disclaimers saying no inference was drawn — **and the inference WAS the finding.** Both halves were false: the letter was signed by someone else, and the identification was never verified (the library's own record says only *"a Deputy Utah County Attorney"*). **Test: strip the guards and read the sentence alone. If what remains is an argument, the guards are decoration.**
2. 🚨 **A refutal is a claim too.** See item 1 in the table above. This library has verified its findings hard and its refutals **not at all**.
3. ⚠️ **Writing the instruction is not performing the edit.** Three "fixes" in the Losee pass were parentheticals saying *"is restated as…"* with the text untouched — **and the revision log recorded them as done.**
4. ⚠️ **A search for one artifact does not inventory a corpus.** The docket, the Information and the PC affidavit sat in a DocumentCloud project **enumerated three times** by sweeps hunting the State's brief.

### Where to pick up

1. **B2 — Q-61.** ⚠ **STARTED 2026-08-16: the verification stage has run for the first time.** Tranche 1 — the five carried nulls — is **5 of 5 CONFIRMED** → [CR-REVIEW-2026-08-16](files%20-%20Court%20record/CR-REVIEW-2026-08-16_Q61-carried-nulls.md). **~360 candidates still have no verdict.** ✅ **The banks are intact and resumable, verified by parsing rather than assumed:** Finder B **147** `F2-*`, day-2 completeness **60** `C1-*`, plus a **66**-item CR-E08 harvest the index had left off its own list. ⚠ **The Day-5/Oliver leg is RETRYABLE — it died on a `429` rate limit, not a spend limit** (the index said spend limit and that discouraged the retry). **Next tranche: the self-claims cluster, starting `F2-133`** — Finder B counts 27 rows against the file's own "twenty-six"; pure arithmetic against a primary artifact, no network.
2. **C — finish Q-07:** two quotation repairs, residual convention defects, and **a verification cycle that has never run**.
3. ⛔ **D — Q-70 is BLOCKED, and this is new.** **The DocumentCloud API returns HTTP 403 behind a Cloudflare challenge from LOCAL sessions** (three endpoints, two user agents, re-tested twice on 2026-08-16) — **reversing Run 2's "no longer bot-gated" and the 08-13 46/46 enumeration.** 30 of 46 filings remain unread and **cannot currently be fetched.** ⚠ **Do not log a silent sweep as a null: the route is unattemptable, not empty.** Re-test each session.
4. **B3 (Q-78)** unblocks the moment CR-E09 clears its cycle.
5. 🚨 **A1 — Tue 2026-08-18: run the watch BY HAND. This is the day after tomorrow.** The State's reply is due, the routine's next firing is **Wed 08-19 — after the deadline** — and it is egress-blind, so there is **no document-capable scheduled cover at all.** ✅ **Run 4 (2026-08-16) left a baseline that makes it cheap:** the Fox outlet-mirror directory is enumerated at **55 PDFs / exactly one case item**, so detection is a **diff, not a search**. Rev is enumerable from its sitemap. DocumentCloud is not available (item 3).

## 1. First five minutes, in this order

```bash
cd ~/Documents/"Kirk Robinson Research"
git pull                 # nothing else has been writing here, but check
./queue-check.sh         # queue + register integrity; must print RESULT: clean
./tsearch.py --validate  # transcript search method still works
```

Then read **[QUEUE.md](QUEUE.md)** and the **standing hazards** at the bottom of it. ⚠ **Two of them changed on 2026-08-01 — hazard 10 was CORRECTED because it was wrong, and hazard 9 was WIDENED.** See §5.

**Expect `queue-check.sh` to list SIX files under "Provisional findings outstanding." THREE are real.** *(CR-E06 has since cleared; DNA-E01 and the blocked Q-08 draft have joined.)*

| File | Real? |
|---|---|
| **CR-E06** (Bakker/Oliver) | ❌ **FALSE POSITIVE — this file is now VERIFIED (v1.2) and MAY be cited.** Q-58 and Q-59 both complete: 68 of 69 material candidates tested → **59 CONFIRMED · 3 REFUTED · 6 MOOT**, **all confirmed items integrated.** **The findings passed** — nothing defeated a headline result, §5 finding or register entry. The validator matches the token in the historical revision log and in §9.2's *statement that it was cleared* |
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

**Q-58, Q-59 and Q-08 all completed on 2026-08-01.** Everything below is what remains, in order.

1. ✅ **Q-08 IS DONE — the DNA folder now has `DNA-E01_DNA-evidence-what-it-can-bear.md` (v4.0).** Findings `[PROVISIONAL]` → **Q-61** is the verification cycle, and ⚠ **aim it at CAVEATS, NULLS AND HEDGES specifically**: five of six factual errors found in CR-E06 were of that kind, and the Q-08 draft invented a `[UNVERIFIED BY CYCLE]` token that `queue-check.sh` could not see.
2. ⚠ **Q-60 IS WAITING ON YOU AND IS THE MOST STRUCTURAL THING OPEN.** The DNA folder has run its own **D-1…D-10 since 2026-07-15, duplicating numbers already assigned in the *Bride of Charlie* series.** Both DNA files now carry a **do-not-cite-by-number** restriction so nothing breaks meanwhile, and **nothing was renumbered.** Two proposals at **DNA-E01 §12**. ⚠ **Executing either edits files across two topic folders including a register cell inside CR-E06, a VERIFIED file — a change to the library's spine, not an assignment.**
3. **Q-07 — run the Losee review** (the 85.6k draft is banked and marked DO-NOT-PUBLISH; its reviewer never ran) · **Q-10** — arrest chronology, never started · ⚠ **Q-09 (Twiggs) remains human-gated.**
4. **Q-55** (the 213 Q-54 residue — dedup already rebuilt and proven) · **Q-56** (bank the State's brief; provenance is a separate act) · **Q-62** (ratify or reject the `DNA-E01` file-ID convention — a yes/no).
5. **Q-48, Q-46, Q-47, Q-57** — the unheld primary documents. ⚠ Q-46 has **two dates in play**.

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
