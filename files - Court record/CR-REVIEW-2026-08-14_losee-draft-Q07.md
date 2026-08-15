# CR-REVIEW-2026-08-14 — The Q-07 Losee draft review

**File ID:** CR-REVIEW-2026-08-14 · **Scope:** the three-reviewer adversarial review of `2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md`, required by LOOP.md §2 and never run until now · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-14 · **Status:** v1.1 — the fix pass and the re-gate are recorded at §8

> ⚠️ **AS OF 2026-08-14, TYLER ROBINSON HAS NOT BEEN BOUND OVER FOR TRIAL. PRESUMPTION OF INNOCENCE APPLIES THROUGHOUT.**

---

## 1. Verdict, stated first

**THE DRAFT DOES NOT PUBLISH. The legal/ethical gate returned FAIL on three BLOCKING living-persons items**, and the claim verifier refuted five substantive claims including **one tier error and one figure with no support in the transcript at all.** The draft's `DO-NOT-PUBLISH` marking stands and is now **earned rather than precautionary**.

**But the draft's core survives, and that is the other half of the verdict.** All four headline results were tested against the transcripts and **all four hold** — including the three scoped nulls, which were re-run under a method the older nulls did not use. The defects are concentrated in the draft's *apparatus* — its speaker key, its living-persons caveat, its provenance labels — not in its findings.

| Reviewer | Coverage declared | Result |
|---|---|---|
| **Claim verifier** (transcripts only) | draft 519/519 lines; `tsearch.py` validated; every null re-run raw **and** whitespace-normalised | **5 REFUTED · 5 PARTLY**; 4 headline results CONFIRMED; 16 of 18 spot-checked quotes verbatim |
| **Conventions + currency** | draft 519/519; CR-E06 navigated by heading; CLAUDE.md, `queue-check.sh`, QUEUE.md read | **10 convention defects · 5 exclusion rulings · 10 staleness items** |
| **Legal/ethical gate** | draft 518/518 lines, two passes, no gap; targeted greps for names, posture, designators, contact details | **FAIL — 3 BLOCKING, 9 fix-before-publish, 7 notes** |

⚠️ **All three coverage declarations were required and checked.** Q-08's first review round was invalidated in this project because an orchestrator silently truncated a file at 120,000 characters; **every reviewer here was passed a path, not content, and made to state what it actually read.**

## 2. The three BLOCKING items — all living-persons, all localised

| | Item | Why it blocks |
|---|---|---|
| **L3-01** | The draft says **"Lance Twiggs testified under use immunity."** | He was **granted** use immunity by two offices; his sworn statement was received **in lieu of live testimony** and **was never cross-examined.** The formulation invents a live-testimony event *and*, by fusing "testified" to "immunity," implies personal exposure for a man the same sentence says is not accused. **This is the library-wide error catalogued at DNA-E01 §10 item 12** — the draft is one of its carriers. |
| **L3-02** | §1.6 row 1 names Twiggs inside a row about likelihood ratios for **the towel** (the alleged weapon's wrapping) and **the screwdriver handle**, with **no non-suspect framing at the point of use.** | **The canonical juxtaposition harm, found again.** No single sentence asserts anything false; the row does. A reader landing on §1.6 — a table, highly quotable, sixty lines below the protective caveat — gets "Twiggs + weapon items + DNA statistic" with nothing saying that his presence in *both* propositions is **the analyst's modelling choice, not a finding that his DNA is on either item.** |
| **L3-03** | The protective header names **Matthew Robinson and Amber Robinson** as elimination-sample donors — and **both names appear nowhere else in the file.** | **The caveat causes the harm it exists to prevent.** No elimination-donor material is in the body at all, so the header *introduces* two private family members, by name, as DNA contributors, into a file about the alleged firing position. Fix: delete both names, keep the generic rule. |

⚠️ **L3-03 is the sharpest methodological result in this review, and it generalises: a protective caveat is not automatically protective. It is a claim, it has a cost, and here the cost was borne entirely by two people who had no other reason to appear in the file.** This is the fourth time in this library that a rule was broken inside the passage stating it.

## 3. What the claim verifier refuted

| id | The draft's claim | Verdict |
|---|---|---|
| **L1-04** | Bagley's body camera produced a **"27-minute-35-second"** recording, cited to `day1.txt` 04:12 | ⚠️ **REFUTED — no duration for that recording exists anywhere in Day 1.** `/27 minutes/`, `/twenty-seven/`, `/35 seconds/`, `/minutes and 35/` all return **zero, raw and normalised.** The one `27:35` in the day is a **Rev stream timestamp inside Sgt. Hull's testimony about being directed to the university** — different witness, different subject. **A LOCATOR READ AS A MEASUREMENT.** What the record has is *"I think the battery went dead."* **This figure had propagated to CR-E05 (VERIFIED) and QUEUE Q-53; both corrected 2026-08-14.** ⚠️🚨 **THIS WITHDRAWAL IS ITSELF UNDER CHALLENGE — DO NOT RELY ON IT, AND DO NOT ACT ON IT WITHOUT THE OWNER.** On 2026-08-14, re-reading `day1.txt` directly for an unrelated repair, the figure was found **on the record after all**, at **04:12:40**, in defence counsel's question: *"So that **27 minute and 35 second** body cam that starts when you're at the Hall of Flags and ends while you're still on the roof but haven't put the crime tape up yet, that's the only body cam you have that day?"* — answered **"Yes."** **So the duration IS in the record — as counsel's characterisation, assented to by the witness — and the passage independently confirms the start point, the end point and that it was his only footage that day.** ⚠️ **Why the refutal failed: the searches ran `27 minutes`, `35 seconds` and `minutes and 35` — ALL PLURAL. The transcript is SINGULAR ("27 minute and 35 second"), and `twenty-seven` missed because the figure is a numeral. A FALSE NULL FROM INFLECTION, not from line-wrapping** — a class standing hazard 11 does not cover. ⚠️ **LOOP.md §4 HARD STOP: "a correction would reverse a prior correction." The reversal is therefore NOT EXECUTED. This note records the evidence so nothing false stands unmarked; restoring the figure — and the grade it should carry as counsel's assented characterisation rather than the witness's own words — is an OWNER decision.** |
| **L1-05** | *"There is not, Judge"* — no footage captures the shooting — treated as an answer **within Hull's testimony**, graded **High** | ⚠️ **REFUTED as testimony. The speaker is Mr. Sturgill, the State's counsel**, during pre-testimony argument, **before Hull was sworn.** It is a **Tier 2 representation of counsel**, not Tier 1 sworn testimony, and Finding 9 grades it High beside Hull's sworn "No." ✅ **CR-E04 §3 already attributes it correctly to the State — the error is the draft's alone and did not propagate.** |
| **L1-01** | Of seven `measurement` hits, **"not one concerns the perch-to-tent measurement"** | **REFUTED.** Hit #1 (`day4.txt` 04:37:11) is exactly that: *"Were measurements taken from that sniper position to the tent…"* — *"Yes."* **The derived conclusion survives** — the exchange is passive-voice, so no witness said *who, when or how* — but the search claim as written is false and contradicts the draft's own citation. |
| **L1-02** | The examining prosecutor **"has no label at all"** on Day 1 | **REFUTED.** He is labelled 498 times — **under the wrong name.** The judge addresses him as "Mr. Sturgill"; Rev labels the turns `Ryan McBride`. **Mislabelled ≠ unlabelled**, and the distinction matters because the draft's speaker key is built on it. |
| **L1-03** | Day 1 quoted question-turns are labelled **"Kathy Nestor"** | **REFUTED as an incomplete key.** Day 1 carries **487 `Chad Grunander` turns** — the State's direct examiner, a label the draft never names — and **most passages the draft actually quotes are Grunander-labelled.** The stated speaker key does not cover the passages relying on it. |

**Five PARTLY findings**, none defeating a conclusion: a communication-log quote **verbatim-exact but sourced to the wrong hearing day** (Bakker testified Day 2, not Days 3/5); a `Converse` count correct at four with one hit unaccounted; three silent wording departures inside a block-quoted stipulation; a dropped intervening exchange without ellipsis; and the header's **"fifteen direct verification searches"** against a table of **twenty**.

## 4. What survived — and it is the load-bearing half

- **Headline (a), the purposive no-casing finding — CONFIRMED verbatim, both witnesses.** Bagley: *"being around guns and snipers all the time, I was looking for a spent shell casing. I couldn't see one. I was looking over the edge, looking all over the place."* Hull, independently: *"Not to my knowledge, no,"* twice — roof and immediate surroundings.
- **Headline (b), the three scoped nulls plus the shoe-impression null — CONFIRMED at ZERO across all five days, raw *and* whitespace-normalised.** `/gunshot residue|GSR|primer residue/`, `/trajector/`, `/reconstruct/`, and the shoe-comparison pattern. ⚠️ **This is the first null set in this library re-tested under hazard 11, and it held.** So the finding stands: **the rooftop case as presented to the magistrate contains no forensic test of the roof for a firing event.**
- **Headline (c), the sight line with its immediate qualification — CONFIRMED verbatim**, including the Sorensen Center obstruction on the very next question and the confinement to the far south of the roof.
- **Headline (d), perch graded separately from geometry — CONFIRMED**, including the Pythagoras check (√(410²+68²) = 415.60) and that **no witness stated who took the measurements, when, or how** — this last surviving despite L1-01, because the one relevant exchange is passive-voice.
- **16 of 18 spot-checked quotations verbatim**, including Bagley's disclaimer of the primary rooftop photograph — *"I saw a distinct impression in the gravel and this does not show that."*
- **12 of 20 search-table rows re-run; 12/12 hit counts matched exactly.**
- ✅ **One finding was UNDERSTATED:** the draft says an ATF analyst disclaimed activity-level opinion "three times"; the verifier found **four** substantive instances.

## 5. Conventions, currency, and the exclusions that are now importable

**The single most consequential convention defect (L2-C02): the draft carries no `[PROVISIONAL]` token.** It states in §13 that its findings have not been through a verification cycle, but marks that only in an HTML comment and the filename. **`queue-check.sh` greps for the literal token and nothing else — so on publication this file would report clean while carrying un-cycled findings.** *(The same structural gap was found in CR-E07 this week and queued as Q-68. It is now a pattern, not an incident.)*

**Other convention defects:** a self-contradicting search count (fifteen vs twenty vs twenty); **Tier 3 material carried with no URL and no retrieval date** — including two articles the draft's corrections turn on that are **never named**, so no reader can check them; a **missing supersession row on the other end** (the superseded Losee file has no revision log at all); one layer blend; an unflagged garble inside a quotation; two grades attached to evaluative judgments rather than to verification acts; and one null reported with no hit count. **No invented tokens were found**, and the §0 framework, access-path caveats, header and revision log are correctly formed.

**The exclusions are now largely importable, which was the point of running this after CR-E06 cleared:**

| §1.6 exclusion | Now carried by | Importable? |
|---|---|---|
| The two FBI likelihood ratios + the Twiggs conditioning | **CR-E06 §2.1, §2.2, §5.1–5.3, D-53** | ✅ **YES** — CR-E06 is v1.2 VERIFIED. **Constraints must travel verbatim:** never either figure without both propositions; never a bare item designator; the ratio-of-1 may not be carried against the 30 quintillion figure; the over-hedge guard; and State's Exhibit 31 has never been read. |
| Exhibit 31's *"Screwdriver from perch"* description of Item 8 | **CR-E06 §2.1** | ✅ **YES** — this is the §8.2 check the draft flagged as "run first." ⚠️ **It is the parent Item 8 label as read aloud, NOT a witness placing the screwdriver at the perch, and NOT a description of the sub-item where the statistic attaches.** It does not displace Bagley's Tier 1 *"10–15 feet in from the guardrail"*; both must be stated and the conflict graded, not resolved on a label. |
| **The six consumed northeast-corner swabs that yielded no DNA**, and the stairwell railing sample | **CR-E06 §2.8, §5.5** | ✅ **YES — the costliest exclusion, now released.** Must travel with its counterweight: extract *was* said to have been returned "on all of the items," counsel never returned to it, so it **stands unrebutted and untested**; and **no DNA obtained ≠ nobody was there.** |
| Faumuina's Day 2 chain-of-custody, detailed form | CR-E03 §5A | ❌ **NO** — §5A is still `[PROVISIONAL]`. The Day 4 substitute stands. |
| CR-E03 §5A entire | — | ❌ **NO, with a carve-out:** material CR-E06 independently carries is available **cited to CR-E06, never to CR-E03 §5A.** |

**Ten staleness items**, of which the operative ones: the **register-ceiling statement is stale in both halves** (ceiling is now D-59, next free D-60); **"awaiting Q-58" is stale in six places**; **DNA-E01 now exists** and must be named *and* marked `[PROVISIONAL]`; **`LOSEE-E01` is no longer the drafter's call** — Q-62 is open and human-gated, so the self-assigned ID must not be published ahead of it; the **case-posture stamp reads "as of 2026-08-01"** and must be re-verified and re-stamped at publication; and the file inventory predates **three** files created since.

⚠️ **A precise hazard-11 position, worth keeping because it is narrower than the hazard as first written:** the draft's nulls were produced with `tsearch.py`, which flattens whitespace before matching — so they were **protected**, and the re-runs confirmed it. **The Rev transcripts store each utterance on one long line, so phrase-crossing false nulls do not arise in them at all.** Hazard 11 bites on **PDF text extractions**, where it bit three times this week. What remains exposed in the draft is its **register-ceiling sweep**, done with a plain grep.

## 6. What this review did NOT do

- **It did not re-write the draft.** Every fix above is specified but unapplied; the draft remains `DO-NOT-PUBLISH` and now also `DO-NOT-CITE` on the five refuted claims.
- **The claim verifier did not reach:** §1.2's oath-attribution and ruling-label claims; the Day 5 opposing-counsel-label claim; §1.3's exhibit-collision claims; §1.4's recess/dead-air finding; §1.5's eight admission-over-objection claims; §2 rows 2, 10 and 12; §7's northeast-drop passage; §9.4's bystander-video items; §10's ceiling grep; §12 item 11. **These are unreached, not confirmed.**
- **No reviewer opened CR-E05, CR-E02, CR-E03, CR-E04 or CR-ACQ** — every verdict works from the transcripts alone. The draft's *derivations from those files* are therefore untested.
- **No exhibit was obtained.** Every exhibit claim remains a witness's account of a document.
- **No register entry is assigned, resolved or moved by this review.** No case-posture statement is altered.

## 7. What Q-07 needs next

1. **Apply the three BLOCKING fixes** (all single-sentence edits at the header caveat and §1.6) — then a **targeted re-gate** of those lines, not a full cycle.
2. **Apply the nine fix-before-publish items**, the five refutals, and the ten staleness corrections.
3. **Import the three now-unblocked CR-E06 exclusions** with their constraints attached verbatim.
4. **Add a literal `[PROVISIONAL]` token** until a cycle clears the file, or run the cycle.
5. **Re-verify and re-stamp case posture** at the actual publication date — 👤 human gate.
6. **Resolve Q-62** before any `LOSEE-E01` ID ships — 👤 human gate.

## 8. The fix pass and the RE-GATE — added 2026-08-14

**The fixes were applied (draft v1.1) and a re-gate was run. Verdict: PASS WITH FIXES.** All three BLOCKING living-persons items **CURED**; **no new living-persons harm introduced**. Coverage declared over all 523 lines, both ends quoted.

⚠️ **But the re-gate's most valuable finding was about the fix pass, not the draft — and it is the reason this section exists.**

**THREE OF THE "FIXES" WERE ANNOTATIONS, NOT EDITS, AND THE REVISION LOG REPORTED THEM AS DONE.** Where the fix pass wrote *"is restated as…"* inside a parenthetical, it left the underlying text untouched: the trial-presupposing phrase survived in §11 Finding 3's *"what would change it"* cell, *"during trial preparation"* survived at §12 item 11, and a gender descriptor of an unnamed officer survived at §7 — **while the log recorded all three as removed.**

**The lesson, stated plainly because it is this project's own and it was committed by the person applying its own review: writing the instruction is not performing the edit, and a revision log that records intent as completion is a false account of the file.** ⚠️ **It is a close cousin of the failure class this library already tracks** — a caveat that only *restricts* feels safe and goes unchecked; here, a note that only *describes* a fix felt like the fix.

Five further defects, all applied at draft **v1.2**:

| id | Defect | Why it mattered |
|---|---|---|
| **RG-04** | The corrected hearing-end date was **not propagated** — §2 row 13 still read 2026-07-13 after the header was fixed to 07-10 | **The file contradicted itself on the very fact the pass advertised fixing** |
| **RG-05** | The fix pass's **own new text** used a bare *"Exhibit 31"* | It broke the file's §1.3 rule **inside text written to enforce that rule** |
| **RG-06** | The de-named elimination donor was **gendered five times** in the new text, and the L3-03 note **restated the relationship category** | With names removed, both remained **re-identification vectors** |
| **RG-07** | The L3-06 note went **stale the moment L3-05 paraphrased §2 row 8** | And it obscured that one instance of the forbidden formulation legitimately survives at §8.3 — a cross-examination question the witness rejected — which is now a **stated choice**, not an oversight |
| **RG-08** | A bare lab designator *"6A"* | Agencies do not share numbering series |

**And the disclosure itself was under-counting:** the Status line listed three outstanding items where the revision log listed seven. Corrected — the Status line now carries all five classes and defers to the log.

**Publication remains barred.** Outstanding: a fresh case-posture verification and re-stamp (👤), the Q-62 file-ID decision (👤), repair of two block quotations against the transcript, the residual convention defects, and **an independent verification cycle, which has still never run.**

---

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-14 | File created. **The Q-07 review, in flight when the 2026-08-01 session closed and never completed, has now run** — three reviewers, each declaring coverage against the full 519-line draft. **Verdict: FAIL, do not publish.** Three BLOCKING living-persons items, all localised: the "testified under use immunity" formulation; §1.6 row 1's Twiggs/weapon-item juxtaposition with no non-suspect framing at the point of use; and a protective caveat that **names two private family members who appear nowhere else in the file** — the caveat causing the harm it exists to prevent, the fourth time in this library a rule has been broken inside the passage stating it. **Five substantive refutals**, of which two matter: a **"27-minute-35-second" body-camera duration with no support anywhere in Day 1** — a Rev stream timestamp from a different witness read as a measurement, which **had propagated into CR-E05 (VERIFIED) and QUEUE Q-53, both corrected the same day** — and a **tier error**, *"There is not, Judge"* graded High as sworn testimony when it is the State's counsel arguing before the witness was sworn (CR-E04 already had it right). **All four headline results survived**, including the three scoped nulls **re-tested under the new hazard 11 and holding at zero across five days**, and one finding proved **understated**. Ten convention defects (the governing one: **no literal `[PROVISIONAL]` token, so the validator cannot see the file's own admission that no cycle has run** — the same gap found in CR-E07 and queued as Q-68), five exclusion rulings (**three of the four blocked imports are now released by CR-E06 v1.2, with their scope constraints recorded verbatim**), and ten staleness items. **Unreached scope is itemised at §6 rather than left silent. No register entry assigned or moved; no case-posture statement altered. Robinson has not been bound over; presumption of innocence applies.** |
| 1.1 | 2026-08-14 | **§8 added — the fix pass and the RE-GATE.** Verdict **PASS WITH FIXES**: all three BLOCKING living-persons items **CURED**, no new living-persons harm. ⚠ **The re-gate's most valuable finding was about the FIX PASS: three "fixes" were ANNOTATIONS, NOT EDITS, and the revision log reported them as done** — *"writing the instruction is not performing the edit, and a revision log that records intent as completion is a false account of the file."* Five further defects recorded and applied at draft v1.2, including a corrected date **the pass failed to propagate** and a bare exhibit designator **inside text written to enforce the rule against bare designators**. The draft's Status line was **under-counting its own outstanding items** and now defers to its log. **Publication remains barred; the independent verification cycle has still never run.** |
