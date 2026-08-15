# Q-61 candidate bank — INDEX · 2026-08-14

**⚠️ THESE ARE CANDIDATES, NOT FINDINGS. NOTHING HERE MAY BE CITED.** Per LOOP.md §2 a finding hardens only when a **separate** cycle works from the **primary artifact, not the summary**. **No candidate below has been adversarially verified.** `DNA-E01` remains `[PROVISIONAL]`; `CR-E07`'s §§2–4 remain untested.

**Purpose of this file:** the harvest cost ~390k subagent tokens and the raw output is JSONL. This index says what exists, what it covers, and where the cycle stopped, so **the next session resumes at verification instead of re-harvesting.**

## What ran, and what did not

| Stage | Target | Status | Output |
|---|---|---|---|
| Finder A | `DNA-E01` §§0–5 | ✅ complete, full coverage declared (lines 1–529 of 888; §5 ends 525, §6 begins 527) | **187 candidates**, `F1-01`…`F1-187` |
| Finder B | `DNA-E01` §1 + §§6–14 | ✅ complete, full coverage declared (lines 1–178 and 527–888) | **147 candidates**, `F2-01`…`F2-147` |
| Completeness | `day2.txt` — Bakker + all Day-2 DNA passages | ✅ complete; read **lines 4400–9640 end to end**; 14 greps declared with hit counts | **60 items**, `C1-01`…`C1-60` |
| Completeness | `day5.txt` — Oliver (+ `day4.txt` greps) | ❌ **DIED — account spend limit** | none |
| **Verification** | **every candidate above** | ❌ **NEVER RAN — not one verdict exists** | none |

**Raw output, banked alongside this file:**
- `2026-08-14_Q61-finder-DNAE01-sections6-14_RAW-CANDIDATES.jsonl`
- `2026-08-14_Q61-completeness-day2-bakker_RAW-CANDIDATES.jsonl`
- `2026-08-14_CRE07-completeness-inventory_RAW-CANDIDATES.jsonl` *(CR-E07's completeness pass — the one that produced F-20; see below)*

⚠️ **Finder A's raw JSONL was not banked** — its result survives in the session transcript only. Its 187 candidates are recoverable from that transcript; **if a future session cannot find them, re-run Finder A rather than assuming the bank is complete.**

## The two structural gaps a resumer must respect

1. **`day5.txt` / Oliver was never read for completeness.** Every DNA-E01 claim sourced to Day 5 — the activity-level refusals, the consumption and retained-extract lists, the isoallele line, the "Oliver NNN" designators, the Dremel elimination results — **has no independent completeness check.** Finder B's candidates *about* those sections exist; the *"what did the file fail to record"* half does not.
2. **Finder A and Finder B split at §5/§6, and several candidates cross that seam.** Finder B flagged `F2-85, F2-90, F2-99, F2-103, F2-109, F2-128, F2-140` as having their decisive text inside §§2–5. **Join them with Finder A's set before testing.**

## Where to start — the finders' own top-ranked items

Both finders ranked their top 25. The highest-value cluster, by consequence rather than by count:

- **The D-53 core:** `F1-127` (both figures' propositions verbatim), `F1-131` (the conditioning universal), `F1-145`/`F2-101` (no unconditioned Robinson ratio anywhere — the over-hedge guard that runs *toward* the State), `F2-100`/`F1-143` (the ratio-of-1's exact scope; no Twiggs-alone run on item 8-1).
- **Counts that would embarrass the file if wrong:** `F1-17`/`F2-60` (six of eleven consumed), `F1-100`/`F2-61` (thirteen ratio-bearing ATF items), `F1-79`/`F2-44` ("only three paragraph-E sentences in the record"), `F1-67` ("Bakker never utters either figure", with its 2+3+2 breakdown).
- **Self-claims the file makes about itself** — the class that failed three times in CR-E06: `F1-54`/`F2-35` ("exactly six bare-figure sites"), `F2-133` (the §1.8 table's own row count — **Finder B counts 27 rows against the file's "twenty-six" and flags the mismatch**), `F2-134` (Day 3 "opened for one purpose only" vs the header's own second Day-3 citation), `F2-51` (§6.1's lead sentence vs its own receipt caveat), `F2-105` (F-10's "four Tier-1 closures", already wrong once).
- **Living persons:** `F1-09` (statement received in lieu of live testimony), `F1-12`/`F1-83` (the appears-only-as-donors universal and its corrected count), `F2-112` (five "testified under use immunity" instances across three files — **a library-wide phrasing error awaiting correction**), `F1-102` (no numeric Dremel elimination value anywhere).
- **Corrections DNA-E01 lodged against CR-E06, a VERIFIED file** — maximally sensitive in both directions: `F1-40`/`F2-23` (`/Losee/` = 25 vs 26), `F1-56` (the school-year locator), `F1-57` (the illustration attachment). **If any is wrong, this library wrongly impeached a verified file.**

## Carried nulls — the weakest perimeter

`F1-87`/`F2-50`: five nulls are **carried from CR-E06 and never re-run** (`/bind ?over|bound over/` day 5 = 0; `/contaminat/` days 1–5 = exactly one; `/voir dire|tender|qualified as an expert/` day 2 = 1 about another witness; `/overrul/` day 5 = 2; `/sustain/` day 5 = 3). DNA-E01's own §14 reports a **3-for-3 correction rate** on CR-E06 items it *did* re-check. **A 3-for-3 failure rate on the checked set is the reason to distrust the unchecked set.** These five are cheap to re-run and should go first.

## Method warnings for the resumer

- ⚠️ **Hazard 11 (new 2026-08-14):** these transcripts and any PDF extraction are **line-wrapped** — `grep` returns **false nulls** for phrases crossing a line break. Normalise whitespace before believing a null; open every hit before believing a positive. This bit three times in one session on the defence brief.
- **Hazard 9:** Rev speaker labels are not evidence; infer every speaker from content. Day 5 is worse than Day 1 — an advocate's argument can carry the opposing counsel's label.
- **Hazard 10:** timestamps are locators. Days 3–5 recess behaviour is **untested** — no duration measurement across a recess on those days.
- **Materiality gate, not an existence gate** (the Q-58 lesson): an omission-heavy candidate set collapses to a 1-in-60 refutal rate unless each verifier must state *what a reader would get wrong* without the item, and refute when the answer is "nothing."
- **Pass a PATH, never inline content, to a reviewer**, and make every reader **declare what it actually read** — Q-08's first review round was invalidated by a silent 120k truncation.

## Living-persons constraints binding every downstream verifier

Lance Twiggs was **granted use immunity by two offices** and his sworn statement was received **in lieu of live testimony** — never "testified under use immunity" (an error live in at least five places library-wide, per `F2-112`). Elimination-donor results carry the record's own **non-suspect framing** inline, never cross-referenced. Never a bare "Exhibit 30"/"Exhibit 31"; never a bare item designator — the two laboratories do not share a numbering series. Never either headline figure without both propositions attached. **Tyler Robinson is presumed innocent and has not been bound over.**

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-14 | Index created when a six-agent cycle was cut short by an account spend limit. Records what completed (two DNA-E01 finders, 334 candidates; one `day2.txt` completeness read, 60 items; the CR-E07 completeness inventory, 58 items), what did not (the `day5.txt` completeness read and **every verification verdict**), and where to resume. States plainly that nothing here is a finding and that DNA-E01 stays `[PROVISIONAL]`. ⚠️ Flags that Finder A's raw JSONL was not banked and survives in the session transcript only. |
