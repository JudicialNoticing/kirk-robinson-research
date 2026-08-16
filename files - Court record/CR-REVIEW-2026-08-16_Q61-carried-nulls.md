# CR-REVIEW-2026-08-16 — Q-61 verification, tranche 1: the five carried nulls

**Status:** ✅ **COMPLETE for the five items in scope. 5 of 5 CONFIRMED.**
**Scope:** the five scoped nulls carried from **CR-E06** (a VERIFIED file) into **DNA-E01** and the blocked Q-08 draft **without ever being re-run**. Identified as the first thing to test by `2026-08-14_Q61-candidate-bank_INDEX.md` § *Carried nulls — the weakest perimeter* (`F1-87`/`F2-50`).
**Method:** `./tsearch.py`, which flattens whitespace before matching — **method validated against its known positive (`/use pliers/`, day4) before any null below was believed**, per QUEUE hazard 5. Every count was then re-run against a **wider stem** per hazard 12, and **every positive hit was opened and read**, never counted.
**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. No filing's contents characterised. Tyler Robinson has NOT been bound over; presumption of innocence applies.**

> ⚠️ **This is the FIRST Q-61 verdict of any kind.** The 2026-08-14 cycle harvested ~390k tokens of candidates and its verification stage **never ran — "not one verdict exists."** These five are verdict 1–5.

---

## 1. Why these five went first

The index's own reasoning, and it was a good one: DNA-E01 §14 reports a **3-for-3 correction rate** on the CR-E06 items it *did* re-check. **A 3-for-3 failure rate on the checked set is a reason to distrust the unchecked set** — and these five were the unchecked set, propagated into two downstream files on CR-E06's authority alone.

**The prediction was that they would fail. They did not.**

## 2. Results

| # | Null, as the source file states it | Claimed | Re-run | Wider stem | Verdict |
|---|---|---|---|---|---|
| 1 | `/bind ?over\|bound over/` · day 5 | **0** | **0** | `/b(ind\|ound)\w*\s*over/` → **0** | ✅ **CONFIRMED**, robust |
| 2 | `/contaminat/` · days 1–5 | **exactly 1** | **1** | `/contamin/` → **1** | ✅ **CONFIRMED**, robust |
| 3 | `/voir dire\|tender\|qualified as an expert\|as an expert/` · day 2 | **1, another witness** | **1** | see §3 — ⚠️ **a trap** | ✅ **CONFIRMED** |
| 4 | `/overrul/` · day 5 | **2** | **2** | — | ✅ **CONFIRMED** |
| 5 | `/sustain/` · day 5 | **3** | **3** | — | ✅ **CONFIRMED** |

**Hits read, not merely counted:**

- **#2** — the single `/contaminat/` hit is on **day 5**, in Oliver's testimony, and is **methodological**: an explanation of *why* elimination samples are requested from investigators — "in case they could have contaminated the evidence." ⚠️ **It is not an allegation that contamination occurred in this case**, and must never be cited as one. *(The passage also lists elimination-sample donors by name; per this library's standing rule those results carry the record's own non-suspect framing inline and are not reproduced here.)*
- **#3** — the one hit is **Ms. Nester tendering Agent Hull** at day 2 `02:11:48` ("I tender the witness, Your Honor"), functioning as passing the witness. **A different witness, exactly as claimed.**
- **#4** — one hit concerns objections to media/broadcast requests; one is the Judge overruling an objection during Mr. Burt's examination. Neither bears on any DNA finding.
- **#5** — all three are the Judge **sustaining** objections during Mr. Burt's examination of Oliver (`01:58:48`, `02:00:23`, `02:02:17`). Neither #4 nor #5 disturbs anything downstream.

## 3. ⚠️ NEW TRAP on null #3 — the claim survives, but only just, and for a reason worth writing down

Searching the **stem** rather than the phrase changes the picture: `/voir dire|tender|qualif/` over day 2 returns **10 hits, not 1**. Five of them (hits 6–10) are **Ms. Bakker describing her own qualification** — and one is a single word away from the searched phrase:

> **Mr. McBride:** "…Do you have a certification?"
> **Ms. Bakker:** "**I'm not certified. I'm qualified as an examiner.**" *(day 2, `07:53:30`)*

**The claim nevertheless HOLDS, and the distinction is substantive rather than lucky.** *"Qualified as an examiner"* is Bakker's **FBI-laboratory credential** — she draws the contrast with certification herself, in the same breath, and the surrounding passage is about training records, a competency examination, moot-court exercises, annual continuing education and outside-vendor proficiency testing. **None of that is a court tendering a witness and ruling her qualified as an expert.** The procedural event the null denies did not occur; the credential the record describes is a different thing wearing a similar phrase.

🚨 **But a future reader searching the stem WILL land on this, and could reasonably conclude the opposite.** The trap is now named on the claim itself so that the next pass inherits the answer instead of re-deriving it — or worse, "correcting" a claim that is right. **This is the hazard-12 shape (search the stem, not the inflected form) producing, for once, a false *positive* rather than a false null.**

✅ **Corroborated in passing:** CR-E06's accompanying observation — that Bakker's qualifications were **elicited by the STATE on cross, not by the defence on direct** — is borne out by the same hits. The qualification testimony runs under **Mr. McBride**, State counsel per the docket's counsel-of-record list; the defence direct is **Mr. Burt**. A defence expert whose credentials were drawn out by the prosecution.

## 4. 🚨 A defect in the INDEX, not in the finding

**The index states null #3 as `/voir dire|tender|qualified as an expert/` — dropping `|as an expert` from the pattern.** CR-E06 §6 and DNA-E01 §6 both carry the fuller four-alternative form. Verified this session: the **full** pattern also returns exactly **1** on day 2, so no result changes — **but a resumer working from the index would have tested a weaker claim than the library actually made**, and a narrower pattern returning the same count is exactly the coincidence that hides a real gap.

⚠️ **Generalisation for the resumer: the index is a summary, and summaries of search patterns lose alternatives.** Test the pattern as the **source file** states it, not as the index restates it.

## 5. What this does and does not license

- ✅ **The five nulls may now be cited as re-run**, dated 2026-08-16, with the trap at §3 attached to #3 whenever it is used.
- ❌ **This clears nothing else.** `DNA-E01` remains `[PROVISIONAL]`; CR-E07 §§2–4 remain untested; the ~360 remaining candidates (147 `F2-*`, 60 `C1-*`, 66 CR-E08 items, Finder A's 187 recoverable from transcript) have **no verdicts**.
- ⚠️ **Clearing is a judgement about the untested remainder, not a tally of the tested part** (the Q-58 lesson). Five confirmations do not make the other 360 safe — they make the *carried-null class* look sturdier than DNA-E01's 3-for-3 correction rate predicted, which is itself worth one line of caution: **the two sets were found by different means and need not behave alike.**

## 6. Queued by this pass

1. **Correct the index's rendering of null #3** (restore `|as an expert`), and record these five as re-run. → done this session.
2. **The Day-5/Oliver completeness read is RETRYABLE and should be re-run** — see the index correction: it died on a **429 rate-limit**, not a spend limit.
3. **Next tranche:** the index's *"self-claims the file makes about itself"* cluster — the class that failed three times in CR-E06 — starting with **`F2-133`**, where Finder B counts **27 rows against the file's own "twenty-six."** That is a pure arithmetic check against a primary artifact and needs no network.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-16 | File created. **The first Q-61 verdicts ever recorded: the five carried nulls, 5 of 5 CONFIRMED**, method validated before any null was believed and every hit opened rather than counted. **New trap named on null #3** — the stem `/qualif/` returns 10 hits on day 2 including Bakker's own *"I'm qualified as an examiner,"* which is an FBI-lab credential and **not** a court qualification, so the claim holds but is one word from looking false. **Defect found in the candidate-bank INDEX** — it drops `\|as an expert` from null #3's pattern, stating a weaker claim than the source file makes. Corroborated CR-E06's "qualifications elicited by the State on cross." No register entry assigned or moved; no case-posture statement altered; no filing's contents characterised. |
