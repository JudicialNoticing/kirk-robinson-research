# CR-2026-08-01 — WIP STATE: session paused mid-write-back

**File ID:** CR-WIP-2026-08-01
**Scope:** a **paused** session. Five workstreams were *executed* on 2026-08-01 — Q-54, Q-52, Q-11, Q-06 and DOCKET-WATCH Run 2 — and **none of their outcomes has yet been integrated into the topic files.** This file exists so that nothing is lost and so the next session resumes from a written state rather than from a chat log. **Resume by executing §9, NEXT STEPS.**
**Case context:** Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. Preliminary hearing held 2026-07-06 → 07-10. **Tyler Robinson is presumed innocent and, as of 2026-08-01, has NOT been bound over for trial.** A preliminary hearing tests probable cause only; no court has found any fact below to be true.
**Prepared:** August 1, 2026
**Status:** v1.0 — **WIP. Findings `[PROVISIONAL]` except where §2 records an adversarial verdict.** This file is a staging post, not a topic file. **It must be superseded and moved to `~/.Trash` once §9 is executed** — never leave both.

**Raw artifacts — the primary record of this session's work.** Everything below is a summary, and **where a summary and an artifact disagree, the artifact governs.** Both are in `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/`:

- **`2026-08-01_verification-cycle-raw-output.json`** — all **39** agents' structured returns, verbatim (~1.1 MB).
- **`2026-08-01_verification-cycle-workflow-result.json`** — the workflow's own consolidated return (~1.1 MB), which additionally carries **the 213 unverified candidates** and the full text of each adversarial verdict. **This is the file to work from at write-back**, because it holds the verifiers' adopt-this wording.

---

## 0. Sourcing framework

**Tier 1** sworn testimony / primary filings · **Tier 2** named official statements · **Tier 3** named journalism · **Tier 4** anonymous or low-verification. Sworn testimony is Tier 1 **as to what the witness said**, never automatically as to the world. **T1 via T3** marks primary-document content known only through reporting.

## 1. WHAT RAN

**39 agents across four phases.** All transcript work was done from the banked Rev renderings in `CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/`, never from the write-ups.

| Phase | Agents | Output |
|---|---|---|
| Q-54 finders | **14/14 reporting** — 6 completeness readers over `day1.txt` in contiguous blocks, 8 proposition-testers over CR-E05 by section | **229 candidate findings** (125 rated material by their finders), **186 explicit confirmations** |
| Q-54 adversarial verification | **16** (capped) | **10 CONFIRMED · 6 REFUTED** |
| New reading | **6** — Q-52, Q-11 ×2, Q-06 ×3 | §§3–5 below |
| DOCKET-WATCH Run 2 | **3** — filings, calendar, transcripts | §6 below |

**Run cost, for pacing future sessions:** 39 agents, 0 errors, 847 tool calls, ~5.14M subagent tokens, ~71 minutes wall clock.

⚠ **A CAP WAS APPLIED AND IT IS NOT SILENT.** Only the 16 highest-severity candidates were adversarially verified. **The other 213 candidates are NOT findings** and must not be treated as such; they are in the workflow-result JSON under `not_verified_items` and need their own verification pass. Reporting this is the point — an undisclosed cap reads as coverage that does not exist.

⚠ **METHOD DEFECT IN THIS SESSION'S OWN ORCHESTRATION, recorded so it is fixed next time.** The dedup step collapsed **nothing** (229 → 229): the key was section-plus-evidence-prefix, which is too strict to catch the same hole described in two different agents' words. **It demonstrably missed at least one true duplicate** — the omitted campus-geography direct was found independently by two agents and consumed two of the sixteen verification slots (§2.1 rows 2 & 8). **The cap is therefore tighter than it looks**, and a smarter dedup would buy real verification coverage.

---

## 2. Q-54 — THE VERIFICATION OF CR-E05

**The headline findings of CR-E05 SURVIVE.** Nothing overturned the Exhibit 12.1 exclusion, Bagley's purposive casing search, State's Exhibit 11 as the ME report, or the Rule 1102 architecture. All 6 REFUTED verdicts were cases where **the file was right and the finder was wrong** — logged in both directions per the objectivity rule.

**But Day 1's opening was substantially under-read.** 8 of the 10 confirmed defects fall in §2.1 and the first stretch of Bagley's direct. **The pattern: CR-E05 read the witnesses well and the courtroom poorly** — strong on testimony, weak on the procedural architecture of offers, objections, grounds and rulings.

### 2.1 The ten confirmed defects

| # | Section | Confirmed defect |
|---|---|---|
| 1 | §3.1 | Bagley's posting was **a response to a disturbance already under way**, not a pre-planned post. File states the assignment flatly |
| 2 & 8 | new §3.0 | **The campus-geography direct, including the parking structure, is omitted entirely.** *(Found independently by two agents — a dedup miss, same hole.)* File is **thin, not silent**, on geometry; the verifier rejected the finder's "silent" wording |
| 3 | §2.1 | The broadcast-security bullet **attributes the court's own phrase to the defence** and **bundles two separate colloquies** under one locator. The exhibit at issue was **State's Exhibit 2** |
| 4 | §1.3 | The court put on the record that **pointing at a monitor is not captured, because the record is audio.** This is a limit on the **certified** transcript, not just on Rev — the file treats Rev as the only problem |
| 5 & 10 | §2.1 | **All eight scene photographs were admitted over defence objection**, on a recurring **provenance** ground (no foundation for when, by whom, or how). The State won it on cited authority (*Purcell*, 711 P.2d 243, 245). Eight litigated admissions; the file records none of the litigation |
| 6 | §1.3 / §2 | ⚠ **"The clock jumps across each recess" DOES NOT HOLD on Day 1.** Verified against `day1.txt`. **The error is upstream in CR-E03 §1** and must move with the correction, or the fix will cite a bad authority |
| 7 | §4.1 | **Rev's "Falmina" IS Sgt. Jennifer Faumuina, and Day 1 itself supplies the name** at 24:19. The file's refusal to identify her was **over-hedging** — standing hazard 4. *(Verifier reduced severity to minor–moderate and rejected the finder's "roughly two hours of stream earlier" as a hazard-2 duration measurement.)* |
| 9 | §2.1 | **The State gave its entire roadmap before any witness was sworn** (23:50–24:39): four witnesses, all law enforcement, named — including Faumuina. Omitted |

### 2.2 What the verification cycle itself demonstrated

**The refuters did not rubber-stamp.** Several **confirmed the hole while rejecting the finder's stated reasoning** — catching finders who measured a duration across a recess (hazard 2), who wrote "silent" where the file was merely thin, and who mis-scoped materiality. **Adopt the verifiers' wording, never the finders'.** The JSON carries the exact adopt-this text for each.

---

## 3. Q-52 — D-52 RESOLVES, AND CR-E05's OWN HYPOTHESIS IS REFUTED

**The answer: nothing changed in the Rule 1102 paperwork overnight. What changed was a new exhibit.**

- **State's Exhibit 12.3 was NOT amended, supplemented or replaced.** It is the identical statement throughout, treated on Day 2 as already in evidence (`day2.txt` 531, 539, 1772).
- **The "only changes are some zooms and red highlights" sentence was ALREADY in the 12.3 admitted on Day 1** — and the State quoted that exact language in its Day 1 argument, *before* the ruling (`day1.txt` 10021, 10065).
- **CR-E05 §5's D-52 row is therefore wrong** where it hypothesises "most likely a revised or supplemental Rule 1102 statement, since… the 12.3 admitted on Day 1 evidently did not [address the alterations], or the objection could not have succeeded." **Both limbs fail.**
- **The premise was also wrong.** The Day 1 objection did not succeed because 12.3 was silent about the alterations. It succeeded because **no statement and no witness came from whoever MADE them** — the court: *"you don't have a person testifying 1102 saying, 'I made the alterations'"* (`day1.txt` 10033, 10061–10065).
- **What actually cured it:** **State's Exhibit 12.4**, the same compilation with circles, blurs and zooms stripped, built overnight exactly as the State said on the Day 1 record it would. 12.4 was admitted, played and broadcast; the witness then gave an **itemised sworn comparison** of 12.1 against 12.4; 12.1 was re-offered on "the foundation that was laid yesterday" and admitted.
- ⚠ **The Day 1 defect was never literally cured**, and **the court never stated a basis** for admitting 12.1 — the ruling addresses publication only (`day2.txt` 1817). That 12.4 was the operative cure is a **well-supported inference, not a stated holding. Confidence: Medium-high.**
- **The objection was RENEWED, not abandoned** (`day2.txt` 1780).
- **CR-E05 §5 is internally inconsistent** — its own narrative paragraph correctly records the State's undertaking to prepare an unaltered version, while the register row two paragraphs later hypothesises the opposite. **The library already held the answer.**

**→ D-52 resolves narrowly, on the foundation question. Correction-in-place required in CR-E05 §5, analyst layer. CR-E04 §3 needs a cross-reference, not a correction.**

---

## 4. Q-11 — OLIVER (DAY 5), AND CR-ACQ §8 ITEM 12 CLOSES

**CR-ACQ §8 item 12 is answered.** **State's Exhibit 12.1 — the enhanced version — WAS played in open court in its entirety on Day 5 (2026-07-10)**, courtroom-only: the court cut the livestream to audio for the duration and barred still photography of the monitors (`day5.txt` 2604–2636). The exhibit's history now runs across **four hearing days** — excluded Day 1, admitted-but-unpublished Day 2, reconsideration moved Day 4, played Day 5 — and **any file describing it must date-stamp which ruling it means.**

**Caitlin Oliver** is an **ATF DNA Section Chief and the author of the reports the State put in evidence — called by the DEFENCE.** On direct she stripped her own reports of everything they do not say:

- **"None of the testing that I performed could speak to activity or what activity led to the deposition of the DNA"** — stated three separate times, never qualified (`day5.txt` 1107, 1339, 1347).
- She agreed a headline of the form *"Mr. Robinson's DNA is found on this item"* would be a source attribution and **"would not be scientifically defensible."**
- Her lab reports **five conclusions and uses no verbal qualifier scale**; it **caps likelihood ratios at one trillion** — "the actual number could be a lot higher."
- **Samples entirely consumed**; her lab requires written permission-to-consume before any work begins.
- **Mixtures**: with the exception of known single-source samples, "the evidence samples were all mixtures," in many cases of four and five people.
- ⚠ **She refused the defence's framing of the NIST publication** — a point cutting **against** the party that called her, and logged as such: *"I don't know that I would call it a guidance document. NIST is not a regulatory body for DNA testing."*

⚠ **A living-person caution that governs any use of this material.** On the swabs of the rifle bolts there was "support for inclusion" of **Matthew Robinson, an elimination-sample donor identified in the question as the defendant's father, not a suspect.** This is **recording layer only.** It must not be extended, and **Q-50 remains human-gated.**

⚠ **CASE POSTURE — HUMAN GATE. Day 5 closed the evidentiary phase with NO bindover**: defence rested, the State offered no rebuttal, Robinson declined to testify, matter continued to 2026-09-01 at 10:00 for up to four hours of argument. **This is consistent with the library's existing posture and changes nothing** — but it is a case-posture statement and **LOOP.md §3 makes it human-gated in every mode. Do not write it into a topic file without the gate.** *(It also reconciles with CR-ACQ §5.1's "up to two hours per side.")*

---

## 5. Q-06 — BAKKER (DAY 2): THE CONDITIONING IS THE FINDING

**Both headline statistics are conditional likelihood ratios that ASSUME Lance Twiggs is one of exactly two contributors — in BOTH competing propositions.** 1.7 octillion (item 7-1, the towel swab) and 30 quintillion (item 8-1, the screwdriver handle). **The Twiggs term is common to numerator and denominator, so the statistic never tests whether he is there.**

- ⚠ **The only STRmix statistic ever run on Twiggs alone returned a likelihood ratio of ONE** — which Bakker classified as **"uninformative,"** below her own stated threshold of 2 for even *limited* support (`day2.txt` 8093, 8105–8109).
- **She reported him as a contributor anyway, and said so plainly**: not from the calculation, but from **visual inspection of the peaks plus the field having submitted him as an elimination sample** (8117, 8122).
- **The elimination designation came from the investigators, not from her own knowledge** (7500).
- ⚠ **Towel-provenance concession:** she was aware the towel was **found in a bush at the university**, not in the home — and the elimination designation stood regardless (7504–7516).
- **PCAST 20% threshold conceded for both items** — 5% minor on item 7, 11% on item 8 — with her rebuttal that PCAST's concern is confined to three-or-more-person mixtures (6695–6699).
- ⚠ **The circularity, recorded as an analyst observation and NOT as a resolution:** that PCAST escape depends on the mixture being two-person; **the two-person call on item 7 was itself reached only by assuming Twiggs**, changed from three contributors on 2025-09-13 after his elimination sample arrived.
- ⚠ **OVER-HEDGE GUARD, running toward the State** (hazard 4): **the record does NOT establish that assuming Twiggs inflated the Robinson likelihood ratio.** No alternative unconditioned ratio was computed, offered or requested anywhere. The defence attack was on propriety, not on magnitude.
- **Steelman logged:** her account is a recognised practice claim — STRmix run to give *weight* to an inclusion already judged plausible, not to make the include/exclude call; elimination samples handled differently from suspect samples.
- **Losee northeast corner: six swabs, consumed, NO DNA.** **Stairwell railing (item 55): two swabs combined, consumed, mixture of >5 individuals, NO CONCLUSION.** Any existing statement in the library about DNA at either location must be reconciled with this.
- **Never write a bare "Exhibit 31"** — it appears as State's / People's / plaintiff's within Day 2 alone.

**Standing instruction for every downstream file: the 1.7 octillion and 30 quintillion figures must never appear without their two propositions attached.**

---

## 6. DOCKET-WATCH RUN 2 (retrieval date 2026-08-01)

**NO ESCALATION TRIGGER MET.** No bindover ruling; the 2026-09-01 argument still stands; nothing sealed or unsealed; no previously-working route newly failed.

| Finding | Status |
|---|---|
| **A PUBLIC MIRROR OF THE STATE'S BRIEF NOW EXISTS** — "Memorandum in Support of Preliminary Hearing Bindover," **28 pp.**, hosted on Scribd by The Post Millennial, HTTP 200 | **Closes Run 1's "no public mirror" null. → Q-45 has an acquisition route.** Contents deliberately unrecorded until banked and provenance-verified |
| ⚠ **28 pp. is the ACTUAL length; 35 was the court's page LIMIT** | The two were being conflated. `DOCKET-WATCH.md` line 13 already says "35-page limit" correctly — **no library file needs correcting**, but no file may write "35 pp." as a page count |
| **The 2026-07-28 filing date is now multi-sourced** — Fox, Reavy, KUTV, ABC, Washington Examiner, Deseret/KSL | Run 1 rested on **one** source. Still **T1 via T3** — the document remains unheld |
| **DocumentCloud API is no longer bot-gated** (403 at Run 1 → HTTP 200 + JSON) | **Project 224251 positively enumerated for the first time: 46 documents.** Q-32 should be **split**, not closed — the web UI remains JS-gated |
| **New artifact the library does not hold** — "Supplemental Notice Concerning Access to Evidence Presented in Open Court," 4 pp., filed **2026-07-09, during hearing week** | Adjacency to the Exhibit 12.1 publication question rests on **title only**; not retrieved, contents uncharacterised |
| **Second source for Q-47** (KUTV) on the Kirk-family motion | Still T1 via T3 |
| ⚠ **CONFLATION TRAP for the next run** | Searches for the bullet-fragment ruling repeatedly surface the **2026-06-26 contempt ruling** instead. **Two dates now in play for Q-46** — the Rev page (proceeding c. 06-22) and the 06-26 ruling. Establish whether they are the same event |
| ⚠ **Machine extraction was unreliable again**, on four counts — including three extractions asserting a filing date of "Tuesday, July 29" (a Wednesday) | Run 1 logged this hazard for this same article set **and it repeated** |
| **Blind spot, stated** | No located source is dated after 2026-07-29. This run has a **three-day gap at its own leading edge** |
| **Deliberate non-recording** | Outlets characterise and quote the brief's argument; the search layer surfaced this unprompted. **None of it is recorded**, per DOCKET-WATCH's prohibition |

---

## 7. REGISTER — NOTHING WAS ASSIGNED

**Ceiling verified independently of `queue-check.sh`, per standing hazard 10.** Both `D-53` hits in the library (`START-HERE.md:77`, `QUEUE.md:4`) were **read** and are forward-looking prose. **Highest ASSIGNMENT is D-52. Next number is D-53. No number was assigned this session.**

**Candidates awaiting assignment** (each needs the grep-and-read check again at write-back time):

1. **The conditioning of the FBI likelihood ratios** — structural, not a source conflict (§5).
2. **The NoC 3→2 revision and its dependence on the elimination assumption** — distinct from 1.
3. **"Exhibit 30" designates two different documents** within one witness's Day 5 direct.
4. **Three unreconciled exhibit-numbering systems** on Day 5 (State's 30/34 · "Oliver 157" · "154").
5. **State's / People's / plaintiff's "Exhibit 31"** — a direct instantiation of standing hazard 3.
6. **Item 8 mixture proportion put as 89% and answered as 79%** within one Q-and-A (likely transcription, but a live trap).
7. **Two competing in-laboratory attributions of the backpack**, neither adopted by the examiner.
8. **The court admitted a defence chart as "Baker 34" immediately after staff twice corrected it to "Baker 35"** — a defect created by the record itself, not the transcription.
9. **The Day 2 non-publication ruling for 12.1 was superseded on Day 5** — no analysis file records this.

**Transcript-integrity items that may belong as library-wide caveats rather than D-numbers:** a **~3m51s gap in Oliver's direct** (`day5.txt` 708–715, at the point of the only Tyler-Robinson inclusion assent); an impossible date in the court's own findings ("September 16th, 2026", `day5.txt` 503); part-seams falling mid-answer inside the single most consequential answer of Bakker's direct.

⚠ **Standing hazard 9 should be WIDENED.** Day 5 supplies a **previously unrecorded type**: a party's advocate's argument carried under the **opposing** party's counsel label. The caveat currently reads as being about witness answers; it is broader than that.

---

## 8. WHAT THIS SESSION DID NOT DO

1. **Nothing was integrated into any topic file.** CR-E05, CR-E03, CR-E04, CR-ACQ, QUEUE.md and the register are **unchanged**.
2. **213 of the 229 candidate findings were never adversarially verified** (§1 cap). They are **not findings**. 125 were rated material by their finders, so the unverified remainder is not merely a tail of trivia.
3. **No exhibit was obtained.** The Scribd brief is a **located route**, not a banked artifact.
4. **No human has read any of this.** Every pass remains the same model checking itself — including this one.
5. **Q-06 covered Bakker; State's Exhibit 31 itself has still never been read by this library.**
6. **Human-gated and untouched:** Q-42, Q-50, Q-51, Q-41, Q-31, Q-32, Q-26, Q-40, and the Day 5 case-posture statement at §4.

---

## 9. NEXT STEPS — execute in this order

1. **Integrate §2 into CR-E05.** Use the **verifiers'** adopt-this wording from the JSON, not the finders'. New §3.0; corrections to §1.3, §2.1, §3.1, §4.1. Bump to v1.1, one combined revision row. **Then clear the `[PROVISIONAL]` marking** — the cycle Q-54 required has now run.
2. **Correct CR-E03 §1** — the "clock jumps across each recess" claim originates there (§2.1 #6). **Supersession rows on both ends.**
3. **Resolve D-52 in CR-E05 §5** (§3). Correction-in-place, analyst layer, matching row. **Cross-reference in CR-E04 §3.**
4. **Close CR-ACQ §8 item 12** (§4) and record 12.1's four-day history with date-stamped rulings.
5. **Write the Day 5 Oliver material and the Day 2 Bakker material into files** — new CR-E06 (Oliver) and an extension of the Bakker section, or one combined file. **These enter `[PROVISIONAL]`; they have had no verification cycle.**
6. **Log DOCKET-WATCH Run 2** to `CR-WATCH-log.md` with a revision row.
7. **Assign register numbers** from §7 — grep and **read the hit** first.
8. **Update QUEUE.md**: Q-54 done · Q-52 resolved · Q-11 done · Q-06 done · Q-45 has a route · Q-32 split. Add the new items.
9. **Write `CR-AUDIT-2026-08-01`** listing every file → version change.
10. **Rewrite START-HERE.md**, then **delete this WIP file to `~/.Trash`.**

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-01 | **File created — session paused before write-back.** Records the outcome of 39 agents across five workstreams, none yet integrated into the topic files. **Q-54's verification cycle on CR-E05 ran in full**: 14 finders produced **229 candidates and 186 confirmations**, of which **16 were adversarially verified — 10 confirmed, 6 refuted**, all six refutals being cases where the file was right. **213 candidates remain unverified and are not findings**; a dedup defect in this session's own orchestration is recorded at §1. **CR-E05's headline findings all survive**; the confirmed defects cluster in §2.1 and the opening of Bagley's direct, the pattern being that the file read the witnesses well and the courtroom poorly. **A library-wide caveat was found to be wrong** — "the clock jumps across each recess" does not hold on Day 1, and the error originates upstream in CR-E03 §1. **Q-52 resolves D-52 and refutes CR-E05 §5's own hypothesis**: State's Exhibit 12.3 was never amended, already contained the alterations sentence on Day 1, and what actually changed was the creation of State's Exhibit 12.4 — though the Day 1 defect was never literally cured and the court stated no basis for admitting 12.1. **Q-11 closes CR-ACQ §8 item 12** — Exhibit 12.1 was played in full on Day 5, courtroom-only, livestream cut to audio — and records Oliver, the defence-called ATF author of the State's own DNA reports, testifying that her testing cannot speak to how or when any DNA was deposited. **Q-06 establishes that both headline DNA statistics are conditioned on Lance Twiggs in both propositions**, that the only likelihood ratio ever run on Twiggs alone was 1 ("uninformative"), and that he was assumed in on visual inspection plus the investigators' designation — with an over-hedge guard logged in the State's favour, since nothing on the record establishes that the assumption inflated the Robinson figure. **DOCKET-WATCH Run 2 met no escalation trigger**, multi-sourced the 07-28 filing date, found a public 28-page mirror of the State's brief, and reopened the DocumentCloud API. **No register number was assigned; no case-posture statement was altered; no topic file was touched.** |
