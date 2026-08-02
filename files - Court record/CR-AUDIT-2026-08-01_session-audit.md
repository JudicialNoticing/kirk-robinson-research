# CR-AUDIT-2026-08-01 — Session Audit

**File ID:** CR-AUDIT-2026-08-01
**Scope:** the whole of the 2026-08-01 session — **Q-54, Q-52, Q-11, Q-06, DOCKET-WATCH Run 2**, and the integration of all of them into the topic files. Covers what changed, what was verified, what was **not** verified, and what a later reader must not assume.
**Case context:** Case No. 251403576, Fourth Judicial District Court, Provo. **Tyler Robinson is presumed innocent and, as of 2026-08-01, has NOT been bound over for trial.** **No case-posture statement in any topic file was altered in this session.**
**Prepared:** August 1, 2026
**Status:** **v1.3 — Part 10 added: Q-58 AND Q-59 COMPLETE; CR-E06 v1.2 VERIFIED and `[PROVISIONAL]` CLEARED.** ⚠ **Six places where that file asserted something the record contradicts — FIVE OF THE SIX WERE CAVEATS, NULLS OR HEDGES**, including one hazard-9 violation committed inside the hazard-9 warning. *(v1.2: Part 9, Q-58.)* *(Superseded status line:)* **Part 9 added: Q-58 COMPLETED.** 68 of 69 material candidates tested — **59 CONFIRMED · 3 REFUTED · 6 MOOT**. ⚠ **The findings passed; the account did not.** Seven core corrections applied at CR-E06 v1.2, including **a D-53 register cell left stale by v1.1's own scope correction.** **`[PROVISIONAL]` NOT cleared — 46 confirmed items remain unintegrated (Q-59).** *(v1.1: Part 8, the 45-agent round stopped at 15 returned.)*

---

## Part 1 — What ran, and what it cost

**39 agents, 0 errors, 847 tool calls, ~5.14M subagent tokens, ~71 minutes wall clock**, in four phases. All transcript work was done from the banked Rev renderings, never from the write-ups.

| Phase | Agents | Output |
|---|---|---|
| **Q-54 finders** | **14** — 6 completeness readers over `day1.txt` in contiguous blocks covering every line, 8 proposition-testers over CR-E05 by section | **229 candidate findings**, 125 rated material by their finders, **186 explicit confirmations** |
| **Q-54 adversarial verification** | **16** (capped) | **10 CONFIRMED · 6 REFUTED** |
| **New reading** | **6** — Q-52, Q-11 ×2, Q-06 ×3 | CR-E06, plus the D-52 resolution |
| **DOCKET-WATCH Run 2** | **3** — filings, calendar, transcripts | CR-WATCH-log Run 2 |

**Raw artifacts, which GOVERN where they disagree with any summary**, both in `CR-ACQ-2026-07-27_court-record-artifacts/`:
`2026-08-01_verification-cycle-raw-output.json` (all 39 agents' returns) · `2026-08-01_verification-cycle-workflow-result.json` (consolidated; carries **the 213 unverified candidates** and **the verifiers' adopt-this wording**).

## Part 2 — The finding that matters most about the *method*

**Q-54 was auditing CR-E05. It found an error in CR-E03 — and in QUEUE.md's own standing hazards.**

The claim that transcript timestamps "**jump across each recess**" is **wrong**. On Days 1 and 2 the recording runs *through* every recess as dead air; the Day 2 "~1 hour discontinuity" **is the lunch recess, recorded**; and two clock readings by the judge fix the same offset to within two seconds across an intervening recess. **A duration measured across a recess on Days 1–2 is real.**

That claim had propagated from **CR-E03 §1** into **CR-E05 §1.3**, into **QUEUE.md standing hazard 10**, and into **START-HERE.md**. It was stated as a *library-wide* caveat, applying to "**every** transcript in this corpus and to every file that cites one" — on the strength of **one** Day 2 example that was never checked.

> **The lesson, and it generalises past this case.** **A caveat is a claim, and claims need verification acts.** This project has been rigorous about grading its *findings* and careless about its *cautions* — a caveat felt safe because it only ever *restricted* what could be said. **It was still wrong, and being wrong in the cautious direction is still being wrong** (standing hazard 4). **Every standing hazard in QUEUE.md should be treated as an unverified claim until some cycle has actually tested it.** Hazards 1–8 have not been.

## Part 3 — Every file → version

| File | v1.0→ | Change |
|---|---|---|
| **CR-E05** *(Day 1)* | **1.0 → 1.1** | **Q-54 integrated; `[PROVISIONAL]` CLEARED.** New **§3.0** (campus geography, sight line, parking structure) restoring an omission **two readers found independently**. New §2.1 bullets: the State's pre-testimony roadmap; the photographic-foundation standard. Corrected: the recess caveat, the broadcast-security misattribution, the Faumuina over-hedge, Bagley's posting as reactive. **§5: D-52 RESOLVED and this file's own hypothesis corrected in place.** §§1.3, 3.1, 3.5, 4.1, 4.4, 6, 6A, 7, 8, 9 amended |
| **CR-E03** *(Days 2/3/5)* | **1.2 → 1.3** | ⚠ **SUPERSESSION.** The recess claim **withdrawn at its source**. Bakker and Oliver superseded by CR-E06, which governs on those two witnesses |
| **CR-E04** *(Hull, Day 2)* | **1.1 → 1.2** | Cross-reference: **State's Exhibit 12.4 exists because 12.1 failed on Day 1**; the Day 2 publication ruling was later superseded. **No substantive finding disturbed** |
| **CR-ACQ** | **1.7 → 1.8** | **§8 item 12 CLOSED** — 12.1 played in full on Day 5, courtroom-only. Precision correction: **Day 4 GRANTED the request and reserved only the TIMING** |
| **CR-WATCH-log** | **1.0 → 1.1** | **Run 2 logged** |
| **CR-E06** *(Bakker + Oliver)* | **— → 1.0** | **NEW.** Both DNA analysts read end to end. **D-53–D-58 assigned here.** `[PROVISIONAL]` |
| **DOCKET-WATCH.md** | **1.2 → 1.3** | The durable routine recorded, **with its report-only limitation** |
| **QUEUE.md** | — | **Hazard 10 CORRECTED, hazard 9 WIDENED.** Register ceiling → D-58. Q-06/Q-11/Q-52/Q-54 marked done; Q-32 **split**; Q-45 updated; **Q-55–Q-58 added** |
| **START-HERE.md** | — | Rewritten for the new state |
| `CR-2026-08-01_WIP-state.md` | — | **Superseded and sent to `~/.Trash`** — never leave both |

## Part 4 — What Q-54 actually decided about CR-E05

**All four headline results survive. Every one of the six refutals was a case where the file was right and the finder was wrong** — logged explicitly, because an audit trail that only ever weakens one side is itself a bias signal.

**The pattern in the ten confirmed defects: CR-E05 read the witnesses well and the courtroom poorly.** Eight of ten sit in §2.1 and the opening of Bagley's direct — the offers, objections, grounds and rulings, rather than the testimony. **That is a reading-method finding, not a CR-E05 finding, and it should shape how the remaining transcript work is done.**

**Two are worth carrying beyond this file:**
- ⚠ **An over-hedge presented as rigour is still a defect.** CR-E05 refused to identify Rev's "Falmina" as Sgt. Jennifer Faumuina and said so in bold — while **Day 1 names her correctly at 24:19**, four stream-hours earlier. The caution *read* as care. It was an error.
- ⚠ **The file mis-attributed a phrase to the defence that was the court's own**, in a section otherwise about how careful the court was being. **Standing hazard 1 applies to this library's own prose, not only to Rev's labels.**

## Part 5 — RESIDUAL SCOPE: what this session did NOT verify

**Stated plainly, because unstated scope reads as coverage that does not exist.**

1. ⚠ **213 of the 229 Q-54 candidates were never adversarially verified** — **125 of them rated material by their finders.** They are **not findings** and nothing in the library may cite them. → **Q-55.**
2. ⚠ **A defect in this session's own orchestration.** The dedup step **collapsed nothing (229 → 229)**: the key was too strict to catch the same hole described in two agents' different words. **It demonstrably burned two of sixteen verification slots on the omitted campus-geography direct, found twice.** **The cap was therefore tighter than it looked. Fix the dedup before re-running.**
3. **CR-E06 is `[PROVISIONAL]` and unchecked.** No cycle has run on it. Given Q-54's yield on a file of comparable care, **assume it contains defects.** → **Q-58.**
4. **No exhibit was obtained this session.** **State's Exhibit 31 — the decisive artifact for D-53 — has still never been read by this library.** The State's brief was **located, not banked.**
5. **The recess-continuity finding was verified for Days 1 and 2 ONLY.** **Days 3, 4 and 5 were not tested.**
6. **Days 3 and 4 were not re-read** against Bakker or Oliver; cross-day statements in CR-E06 rest on targeted validated searches, not a fresh full read.
7. **Q-54 did not re-verify CR-E05's §4 (Hull) as heavily as §§2–3** — the section allocation was by proposition density, and the Hull sections drew 2 of 8 proposition-testers.
8. **Case citations remain unverified against the reporters** — *Purcell*, *Wager*, *Ramirez*, *Merrill*, and "**State v. Drozbeck**," which does not resolve and **must not be cited from the transcript**.
9. ⚠ **A HUMAN READ IS STILL OWED, AND THIS SESSION MADE IT MORE URGENT, NOT LESS.** Every pass — including the adversarial one — was the same model checking itself. **A verification cycle run by the same system that produced the error is a consistency check, not an independent one.**

## Part 6 — Gates observed

**Executed** (`verify`): Q-54, Q-52, Q-11, Q-06, DOCKET-WATCH Run 2 — findings recorded, CR-E06 marked `[PROVISIONAL]`.
**NOT executed, human-gated, and untouched:** **Q-42** (chamber-case re-grade — D-48 has moved four times, past LOOP §4's third-movement stop) · **Q-50** (whether the household-transfer explanation reaches the towel and screwdriver — **recorded in CR-E06 §3.4 and expressly NOT answered**) · **Q-51 / Q-15** (the ME report) · **Q-41** (claude.ai material) · **Q-31** (money) · **Q-32(b)** (live browser) · **Q-26** (the corpus programme) · **Q-40** (identity inference).

⚠ **One case-posture item was reached and deliberately not written into any topic file:** Day 5 closed the evidentiary phase with **no bindover** — defence rested, no State rebuttal, Robinson declined to testify, continued to 2026-09-01. **It is consistent with the library's existing posture and changes nothing**, but case posture is a `human` gate in every mode and **D-51 is the reason.** It is recorded at **CR-E06 §4.3** at the recording layer only.

**No register entry was resolved against any named person.** **D-52 was resolved on a question of exhibit foundation.** **D-53–D-58 were opened, not resolved** — opening an entry records a question and decides nothing.

## Part 7 — The state of the register

**D-1 – D-58, no gaps. Next is D-59.** Ceiling verified **by grep AND by reading every hit**, per standing hazard 10 — `queue-check.sh` again reported a "highest string" one above the true ceiling, exactly as predicted. **Do not trust the validator's number.**

**D-52: RESOLVED.** **D-53–D-58: OPEN**, all in CR-E06 §7.

---

## Part 8 — ROUND 2, STOPPED PART-WAY (added v1.1)

A second workflow of **45 agents** was launched after the integration and **stopped at 17 started / 15 returned** when the session was closed. **Only one phase completed, and it is the only thing that landed.**

### 8.1 Q-58 — CR-E06 verified, and DELIBERATELY NOT CLEARED

**6 readers over `day2.txt`/`day5.txt` → 126 candidates (69 material), 139 confirmations. 8 adversarially tested → 6 CONFIRMED.**

⚠ **The `[PROVISIONAL]` marking was NOT cleared, and the reasoning should be reused.** CR-E05 cleared on 10-of-16; CR-E06 was **6-of-8 with 61 material candidates untested**. **A high hit rate against a small sample is evidence the file has more, not evidence it is sound.** **Clearing is a judgement about the untested remainder, not a tally of the tested part.**

**Two of the six were places where the file asserted something the record contradicts** — the failure mode that matters most:

| | Defect |
|---|---|
| **1** | §2.5 said "which person is the 5% and which the 95% is **NOT stated on the record**." **It is** — elicited by the **State on cross**: Twiggs aligned with the 5% contributor, Robinson with the 95%. **A scoped null that was simply wrong** — hazard 5, from the inside |
| **2** | §5.3 said the defence attacked "the **propriety** of the assumption, not its **magnitude**." **It attacked magnitude too** — "astronomical," "whether you've got accurate numbers in front of you." ⚠ **But through the number-of-contributors input, never naming Twiggs, never asserting a direction of effect, and never asking what the figure would be without the assumption — so the guard survives in corrected form** |

The other four: the LR-of-1 run covered **item 7-1 only** (a scope the file had left open); a **second communication-log entry of 2025-09-13** showing the earliest oral communication already used the compliant "possible contributor" formula (**a confirmation running toward the State**); the out-of-order call was **by prior arrangement previewed by the State**; and the witness testified **a portion of extract was returned "on all of the items"** — counsel said "we'll get to that in a minute" and never did, so it stands **unrebutted and untested**, logged because it cuts against the section's own direction of travel.

### 8.2 What did NOT run

**Q-07 (Losee) produced a complete draft that was never reviewed** — banked as `2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md`. ✅ **Worth recording: the drafter respected LOOP.md §2 rigorously**, excluding CR-E06 in its entirety and enumerating every exclusion — the costliest being the six consumed northeast-corner swabs that yielded no DNA, and Exhibit 31's "Screwdriver from perch" description. **That is the rule working as designed: the DNA folder must clear before the Losee folder can be complete.**

**Not started at all:** Q-08 (DNA), Q-10 (arrest chronology), **Q-55** (18 verifiers over the Q-54 residue), **Q-56** (the brief and its provenance), **Q-46/Q-47/Q-48/Q-57** (unheld documents).

### 8.3 A method note worth keeping

**The Q-55 dedup was rebuilt before this round and the rebuild proved the original defect.** Replacing the prefix key with Jaccard clustering over content tokens **collapsed 20 duplicates the old key had missed entirely** (18 clusters with >1 member). **The old key had collapsed zero.** That left **103 material clusters** from the 213 residue — of which this round was to test 18. **None were tested.**

---

## Part 9 — Q-58 COMPLETED (added v1.2)

**68 of 69 material candidates adversarially tested** (31 agents over the remaining 60; the 69th a dedup duplicate). **Final: 59 CONFIRMED · 3 REFUTED · 6 MOOT · 0 UNCERTAIN**, against **139 logged confirmations**.

### 9.1 The findings passed; the account did not

⚠ **Not one confirmation defeated a headline result, a §5 finding, or a register entry.** The core-touching confirmations **narrowed scope**. On LOOP.md §2's own test — *do the findings harden when a separate cycle works from the primary artifact?* — **they hardened.**

⚠ **But `[PROVISIONAL]` was NOT cleared, and the reason CHANGED.** At v1.1 it stayed because candidates were **untested**. They are now tested, and **46 confirmed material items remain UNINTEGRATED** (→ **Q-59**). **The cycle established that CR-E06 is a sound account, not a complete one** — and a marking whose function is to stop other files citing an incomplete account must stay while 46 confirmed omissions sit outside it. **This is a distinction worth keeping: "its findings are verified" and "it may be cited as an account" are different questions, and this file currently answers them differently.**

### 9.2 The error the cycle caught that matters most

⚠ **A REGISTER CELL WENT STALE UNDER A CORRECTION.** At v1.1 the "item 7-1 only" scope was applied to headline 2 and §5.2 — **and not propagated to the D-53 register cell**, which is precisely the cell written to be carried by other files. **Four independent verifiers caught it.** So a correction made *to reduce* an overclaim left the overclaim standing in the one place most likely to be quoted downstream.

> **The generalisable rule: when a scope is narrowed, the register row is the FIRST place to check, not the last.** A register entry is the file's export surface. **A correction that does not reach it has not really been made.**

Two further core corrections are worth carrying: **§5.3's null was a claim about the laboratory** ("no unconditioned ratio was ever computed") when the record can only support a claim about the transcript — **hazard 5 committed from the inside, again**; and **§5.2's "only ratio of 1" is true of Bakker's FBI work only** — ATF reported support-for-inclusion conclusions involving Mr. Twiggs on Dremel samples, so **the sentence would be false if written across both laboratories.**

⚠ **Three of the seven corrections cut TOWARD the State or the witness** — the restored affirmative-observation clause, the internal-review origin of the additional statistic, and the explained report-language asymmetry. **The both-directions rule is doing real work here, not decorating.**

### 9.3 ⚠ A signal about the verification method itself

**Refutal rates across this session: Q-54 refuted 6 of 16 (38%) · Q-58 batch 1, 2 of 8 (25%) · Q-58 batch 2, 1 of 60 (1.7%).**

**The collapse is explained by candidate TYPE, not by weaker verifiers.** Batch 2 was almost entirely **omissions**, where the question reduces to "is this in the file?" — close to mechanical. Their reasoning was in fact strong: hazard checks run, finder framing corrected, several returning PARTLY-MOOT/PARTLY-LIVE distinctions.

**But a pass that refutes 1 in 60 is not exerting much adversarial pressure.** ⚠ **The fix for the next omission-heavy cycle is a MATERIALITY gate, not an EXISTENCE gate:** require the verifier to state what a reader of the file alone would get *wrong* without the item, and refute where the answer is "nothing." **Recorded in QUEUE.md so the next cycle inherits it.**

---

## Part 10 — Q-58 AND Q-59 COMPLETE: CR-E06 CLEARED (added v1.3)

**68 of 69 material candidates tested — 59 CONFIRMED · 3 REFUTED · 6 MOOT · 0 UNCERTAIN — and every confirmed item integrated.** **CR-E06 v1.2 is VERIFIED; `[PROVISIONAL]` is cleared; the DNA topic folder (Q-08) is unblocked.**

**The findings passed on LOOP.md §2's own test.** Not one confirmation defeated a headline result, a §5 finding, or a register entry. The corrections were **omissions, scope refinements and both-directions balance.**

### 10.1 ⚠ The pattern in the six factual errors, and it is the session's most important result

**Six places where CR-E06 asserted something the record contradicts. FIVE OF THE SIX WERE CAVEATS, NULLS OR HEDGES — not assertions of fact:**

| | What it said | What the record shows |
|---|---|---|
| §2.5 | a scoped null: the 5%/95% assignment "is **NOT stated on the record**" | **It is** — elicited by the **State on cross** |
| §5.3 | a characterisation: the defence attacked "propriety, **not magnitude**" | **It attacked magnitude too** |
| §1.2 | a speaker **reattribution with no stated basis** | ⚠ **A hazard-9 violation committed inside the hazard-9 warning.** Row withdrawn; the widening now rests on **one** instance |
| §1.4 | "State v. Drozbeck **does not resolve**" | **Day 5 renders it "State v. Droesbeke, Utah Ct. App. 2010" — inside the file's own declared read range** |
| §9.8 | residual scope: genotype data is "**summarised, not reproduced**" | **§2.6 reproduces three loci.** A residual-scope statement that **denies what the file does** |
| §6 | admitted-exhibit list, closing with "**only**" | **Omitted a sixth admission its own §2.10 records** |

> ⚠ **THE RULE THIS SESSION EARNED THREE TIMES OVER.** QUEUE.md hazard 10 was a wrong caveat. CR-E05 §5's D-52 hypothesis was a wrong hedge. Now five of six CR-E06 errors are cautions. **A caveat, a null and a hedge are CLAIMS, and claims need verification acts.** ⚠ **And the sharper form: the §1.2 failure was committed *while invoking* the very hazard it broke. A warning is not a shield — it is the place you are least likely to check.**

### 10.2 What the additions changed

**Four new sections that did not exist:** **§3.0** (the pre-testimony colloquy every Day 5 ruling rests on — including **the arrangement by which the State had interviewed Oliver and agreed not to object**, so headline 3's "called by the defence" posture was **scheduled and agreed, not an ambush**); **§2.11** (the redirect and re-cross, carrying **the sharpest form of the defence's attack on the elimination assumption AND her denial — recorded together, because v1.1 had the insinuation without the answer**); **§3.6** (the two analysts answered the same question **differently** — a divergence resolved against neither, which **strengthens** the §5.3 guard); and **§3.7** — ⚠ **the number-of-contributors line WAS allowed, over objection, and it is the ONLY objection overruled in the whole of Day 5. v1.0/v1.1 recorded all three sustainings and not the one overruling, which misstated the court's posture toward the defence's methodological line.**

**A stale register cell.** v1.1's "item 7-1 only" scope reached headline 2 and §5.2 **but not the D-53 cell — the one written to be cited by other files.** **Four verifiers caught it independently.** → **when a scope is narrowed, the register row is the FIRST place to check.**

### 10.3 Residual, stated plainly

**57 MINOR candidates were never tested at all** and are banked unexamined. The cycle tested **candidates its own finders raised**; different readers would raise different ones. ⚠ **And the refutal rate remains the open method question (§9.3) — 1 in 60 on an omission-heavy pass.** **A cycle that clears a file's assertions does not clear its cautions unless it is aimed at them, and this one had to be pointed at them explicitly before it found them.**

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.3** | **2026-08-01** | **Part 10 added — Q-58 AND Q-59 COMPLETE.** 68 of 69 material candidates tested (**59 CONFIRMED · 3 REFUTED · 6 MOOT · 0 UNCERTAIN**), **every confirmed item integrated**, and **CR-E06 v1.2 CLEARED of `[PROVISIONAL]`** — which unblocks the DNA topic folder. **The findings passed**: nothing defeated a headline result, §5 finding or register entry. ⚠ **THE SESSION'S MOST IMPORTANT RESULT IS THE PATTERN IN THE SIX FACTUAL ERRORS: FIVE OF SIX WERE CAVEATS, NULLS OR HEDGES** — a false scoped null, a wrong characterisation of the defence's attack, a speaker reattribution with no stated basis, a flat "does not resolve" refuted by the file's own read range, a residual-scope statement that denied what the file does, and an admitted-exhibit list that contradicted its own §2.10. **A caveat, a null and a hedge are CLAIMS, and claims need verification acts** — earned three times this session (QUEUE hazard 10, CR-E05 §5's D-52 hypothesis, and these). ⚠ **Sharper still: the §1.2 failure was committed WHILE INVOKING the very hazard it broke. A warning is not a shield; it is the place you are least likely to check.** **Four new sections added** (§3.0, §2.11, §3.6, §3.7), including ⚠ **the only objection OVERRULED in the whole of Day 5, which v1.0/v1.1 omitted while recording all three sustainings.** **A stale D-53 register cell** — v1.1's scope fix never reached the one cell written to be cited by other files; four verifiers caught it. **Residual: 57 minor candidates never tested.** |
| **1.2** | **2026-08-01** | **Part 9 added — Q-58 COMPLETED.** 68 of 69 material candidates adversarially tested: **59 CONFIRMED · 3 REFUTED · 6 MOOT · 0 UNCERTAIN** against 139 logged confirmations. ⚠ **The findings PASSED — not one confirmation defeated a headline result, §5 finding or register entry, and the core-touching ones narrowed scope.** **Seven core corrections applied at CR-E06 v1.2.** ⚠ **`[PROVISIONAL]` NOT cleared, and the reason changed: 46 confirmed material items remain UNINTEGRATED (→ Q-59).** **The distinction is worth keeping — "its findings are verified" and "it may be cited as an account" are different questions, and CR-E06 currently answers them differently.** ⚠ **The catch that matters most: a REGISTER CELL WENT STALE UNDER A CORRECTION** — v1.1's "item 7-1 only" scope reached headline 2 and §5.2 but never the D-53 cell, the one written to be carried by other files; four verifiers caught it independently. **Rule recorded: when a scope is narrowed, the register row is the FIRST place to check, not the last — a correction that does not reach the export surface has not really been made.** Also logged: **§5.3's null was hazard 5 committed from the inside** (a claim about the laboratory where the record supports only a claim about the transcript), and **§5.2's "only ratio of 1" is true of Bakker's FBI work alone** — it would be false across both laboratories. **Three of the seven corrections cut toward the State or the witness.** ⚠ **A method signal recorded at §9.3: refutal rates fell 38% → 25% → 1.7% across the session, explained by candidate TYPE (omissions, not defects) rather than weaker verifiers — but the next omission-heavy cycle needs a MATERIALITY gate, not an existence gate.** |
| **1.1** | **2026-08-01** | **Part 8 added — round 2, stopped part-way.** A 45-agent workflow was launched after the integration and **stopped at 17 started / 15 returned** on session close. **Only Q-58 completed**: 6 readers → **126 candidates (69 material), 139 confirmations; 8 tested, 6 CONFIRMED** and corrected into CR-E06 v1.1. ⚠ **CR-E06's `[PROVISIONAL]` marking was DELIBERATELY NOT CLEARED — a 6-of-8 hit rate against 61 untested material candidates is evidence the file has more, not evidence it is sound. Clearing is a judgement about the untested remainder, not a tally of the tested part.** **Two of the six were assertions the record contradicts** — a scoped null that was simply wrong (§2.5), and a characterisation of the defence's attack that was wrong in a way that had made the over-hedge guard look cleaner than it was (§5.3, now corrected and surviving). **Q-07 produced a complete but UNREVIEWED draft, banked and marked DO-NOT-PUBLISH**; its reviewer was in flight when the run stopped. ✅ **Logged as the rule working: the drafter excluded CR-E06 entirely under LOOP.md §2 and enumerated every exclusion.** **Q-08, Q-10, Q-55, Q-56 and Q-46/47/48/57 did not run.** Also records that **the rebuilt Q-55 dedup proved the original defect** — Jaccard clustering collapsed 20 duplicates the prefix key had missed, where the old key collapsed zero. |
| 1.0 | 2026-08-01 | **Session audit created.** Records a 39-agent, four-phase session and its integration into eight files. **Q-54 cleared CR-E05's `[PROVISIONAL]` marking** on the strength of 16 adversarially verified findings — **10 confirmed, 6 refuted, every refutal a case where the file was right** — while **213 candidates remain untested and are expressly not findings.** **The session's most consequential result is about method, not about Day 1: a caveat this library had propagated library-wide was itself never verified, and was wrong.** Also records **D-52 resolved against CR-E05's own hypothesis**, **CR-ACQ §8 item 12 closed**, **CR-E06 created** with **D-53–D-58 opened**, **DOCKET-WATCH Run 2 logged** and the durable routine recorded with its report-only limitation. **Residual scope stated at Part 5, including a defect in this session's own orchestration.** **No case-posture statement altered; no register entry resolved against any named person; a human read still owed.** |
