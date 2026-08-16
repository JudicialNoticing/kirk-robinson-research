# CR-REVIEW-2026-08-16 — Q-61 verification: the five carried nulls, and the file's count of its own table

**Status:** ✅ **Tranche 1 — the five carried nulls: 5 of 5 CONFIRMED.** ✅ **Tranche 2 — `F2-133`: CONFIRMED, and DNA-E01 is corrected to v4.2.**
**Scope:** the five scoped nulls carried from **CR-E06** (a VERIFIED file) into **DNA-E01** and the blocked Q-08 draft **without ever being re-run**. Identified as the first thing to test by `2026-08-14_Q61-candidate-bank_INDEX.md` § *Carried nulls — the weakest perimeter* (`F1-87`/`F2-50`).
**Method:** `./tsearch.py`, which flattens whitespace before matching — **method validated against its known positive (`/use pliers/`, day4) before any null below was believed**, per QUEUE hazard 5. Every count was then re-run against a **wider stem** per hazard 12, and **every positive hit was opened and read**, never counted.
**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. No filing's contents characterised. Tyler Robinson has NOT been bound over; presumption of innocence applies.**

> 🛠 **CORRECTED IN SESSION — an earlier form of this line called these "the FIRST Q-61 verdicts of any kind." THAT WAS WRONG and is retracted.** It was taken from the candidate-bank index's *"Verification — NEVER RAN — not one verdict exists,"* which is true **only of the ~360 banked candidates**. **DNA-E01 v4.1's own revision log records Q-61 ROUND 1 on 2026-08-14: 31 claims tested by four adversarial clusters, 21 CONFIRMED / 4 REFUTED / 6 PARTLY — expressly including these five nulls** (*"All five nulls CARRIED from CR-E06 reproduce identically raw and whitespace-normalised"*).
>
> ✅ **What this pass therefore is: an INDEPENDENT SECOND replication, and that is worth more here than a first.** This library's standing complaint about itself is that *"every pass, including the adversarial one, has been the same model checking itself."* Round 1 and this pass ran in different sessions, by different routes, and **agree**. **What is genuinely new here is not the five verdicts but the three defects and one trap found alongside them** (§3, §4) — none of which round 1 caught, because round 1 tested the nulls **as written** and did not test the **stem**.

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

Searching the **stem** rather than the phrase changes the picture: `/voir dire|tender|qualif/` over day 2 returns **9 hits, not 1** 🛠 *(CORRECTED 2026-08-16, Q-111: this read **10**; the true count is **9**, verified under four counting methods — raw/flattened × case-sensitive/insensitive — with all nine opened. ✅ **The trap itself is CONFIRMED**: Bakker's *"I'm not certified. I'm qualified as an examiner"* is among them, and it is an FBI-laboratory credential rather than a court qualification.)*. Five of them (hits 6–10) are **Ms. Bakker describing her own qualification** — and one is a single word away from the searched phrase:

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
- ❌ **This clears nothing else.** `DNA-E01` remains `[PROVISIONAL]`; CR-E07 §§2–4 remain untested. **Banked candidates with no verdict, recounted 2026-08-16 by parsing each bank rather than trusting the index:** 147 `F2-*` · 60 `C1-*` · **48 `C2-*` (the Oliver harvest the index wrongly recorded as lost — see §7)** · 66 CR-E08 items · Finder A's 187, recoverable from the session transcript only.
- ⚠️ **Clearing is a judgement about the untested remainder, not a tally of the tested part** (the Q-58 lesson). Five confirmations do not make the other 360 safe — they make the *carried-null class* look sturdier than DNA-E01's 3-for-3 correction rate predicted, which is itself worth one line of caution: **the two sets were found by different means and need not behave alike.**

## 7. Tranche 2 — `F2-133`: the file's count of its own table is WRONG, and so is one of its per-day tallies

**Candidate:** Finder B flagged DNA-E01 §14 item 3, which says *"**fifteen** of this file's **twenty-six** tabled searches run on those two days alone… **Day 5** is reached through CR-E06 (VERIFIED) plus **nine** tabled searches touching it… **four** further tabled searches sweep [Day 1]."* Finder B counted 27 rows and 16 for Days 2+4.

**Method:** counted §1.8's table directly, parsing on unescaped `|` only — ⚠️ **a first parse split on every `|` and was corrupted by the escaped pipes inside the regexes themselves, returning a day-tally that summed to 12 of 27 rows.** It was discarded rather than reported. The convention question the candidate flags — rows or patterns? — **settles itself**, because two of the four claims match exactly on rows and neither matches on patterns.

| The file's claim | Counted | |
|---|---|---|
| **twenty-six** tabled searches | **27 rows** (29 patterns; rows 19 and 26 carry two each) | ❌ **off by one** |
| **fifteen** on Days 2+4 alone | **16** (11 Day-2 + 5 Day-4) | ❌ **off by one** |
| **nine** touching Day 5 | **9** (5 Day-5-only + 4 all-days) | ✅ |
| **four** further sweeping Day 1 | **4** (the four all-days rows) | ✅ |

✅ **`F2-133` CONFIRMED. Finder B was right on both numbers, and on the 27/29 row-versus-pattern split.**

**Both errors run in the same direction and by the same amount**, which points at a single row added after the counts were written — and the arithmetic locates it in the Day-2/Day-4 block, since the totals for Day 5 and Day 1 both still hold. ⚠️ **Stated as the inference it is, not as a finding:** the `/destructive testing/` row (Day 2) is the visible candidate, because its "what it settled" text is the **v4.1 §6.1 correction** (Q-61 item S4, 2026-08-14) — i.e. that row was written or rewritten at v4.1, while §14's counts appear to have been left at their v4.0 values. **Not verified; a diff against v4.0 would settle it, and no v4.0 copy is on disk.**

⚠️ **Materiality, stated plainly because the gate demands it:** this changes **no** evidentiary finding. What a reader gets wrong without it is **the file's account of its own coverage** — and this file's §14 exists precisely to state coverage honestly. **A file that miscounts its own audit trail by one is not thereby wrong about DNA; it is wrong about how hard it looked**, which is the claim §14 makes. That is the *"self-claims the file makes about itself"* class — the class that failed three times in CR-E06.

## 6. Queued by this pass

1. **Correct the index's rendering of null #3** (restore `|as an expert`), and record these five as re-run. → done this session.
2. **The Day-5/Oliver completeness read is RETRYABLE and should be re-run** — see the index correction: it died on a **429 rate-limit**, not a spend limit. 🛠 **CORRECTED 2026-08-16 (Q-111): AN OVER-CORRECTION THAT DISCARDED A TRUE FACT.** The `429`'s error **type** is `rate_limit_error`, but its **message body is a spend cap** — *"You've hit your **monthly spend limit**"* — and the coordinator's own resume message in the same bank reads *"cut off by an **account spend limit**… Credits are restored."* ✅ **The leg DID complete and returned 48 of 48 with no gaps — that half was right.** ⚠️ **But it was NOT transient-and-self-retryable: clearing it was an OWNER action, and "retryable" is the wrong lesson for a resumer to carry.**
3. **Next tranche:** the index's *"self-claims the file makes about itself"* cluster — the class that failed three times in CR-E06 — starting with **`F2-133`**, where Finder B counts **27 rows against the file's own "twenty-six."** That is a pure arithmetic check against a primary artifact and needs no network.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-16 | File created. **The first Q-61 verdicts ever recorded: the five carried nulls, 5 of 5 CONFIRMED**, method validated before any null was believed and every hit opened rather than counted. **New trap named on null #3** — the stem `/qualif/` returns 10 hits on day 2 including Bakker's own *"I'm qualified as an examiner,"* which is an FBI-lab credential and **not** a court qualification, so the claim holds but is one word from looking false. **Defect found in the candidate-bank INDEX** — it drops `\|as an expert` from null #3's pattern, stating a weaker claim than the source file makes. Corroborated CR-E06's "qualifications elicited by the State on cross." No register entry assigned or moved; no case-posture statement altered; no filing's contents characterised. |

| **1.1** | **2026-08-16** | **Tranche 2 added (`F2-133`) and two self-corrections recorded.** ✅ **`F2-133` CONFIRMED:** DNA-E01 §14 item 3 claimed *"fifteen of this file's twenty-six tabled searches"*; §1.8 holds **27 rows / 29 patterns**, with **16** on Days 2+4. The convention is settled by the same sentence's *"nine"* and *"four"*, which are correct on rows and wrong on patterns. **DNA-E01 corrected to v4.2**; no evidentiary finding or register entry moves. ⚠ **A first parse of the table was corrupted by escaped pipes inside the regexes and returned a tally summing to 12 of 27 — discarded, not reported.** 🛠 **SELF-CORRECTION 1:** this file's claim to hold "the FIRST Q-61 verdicts of any kind" was **wrong and is retracted** — DNA-E01 v4.1 records Q-61 round 1 (31 claims, 21/4/6) on 2026-08-14, including these five nulls. This pass is an **independent second replication that agrees**, which given the library's standing complaint that every pass has been the same model checking itself is worth more than a first. 🛠 **SELF-CORRECTION 2, in the candidate-bank index:** an edit made earlier in this same session asserted the Day-5/Oliver leg "produced no candidates before it died." **False** — it completed and returned **48 items, `C2-01`…`C2-48`, no gaps**, and DNA-E01 v4.1 had already said so on 08-14 while the index was never updated. The false assertion came from a parse reading only one message shape, missing two ~37 KB payloads. **A null about this project's own work asserted from an incomplete search — the exact failure class this cycle hunts, now committed by two different passes including this one.** |
