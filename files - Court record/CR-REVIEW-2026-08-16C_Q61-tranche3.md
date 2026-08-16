# CR-REVIEW-2026-08-16C — Q-61 tranche 3: the self-claims cluster, and a revision log that lied about itself

**Scope:** Q-61 verification tranche 3 — the three assigned self-claims (`F2-134`, `F2-105`, `F2-51`) plus nine of the 48 banked `C2-*` completeness candidates. **12 claims resolved: 1 REFUTED · 4 PARTLY · 1 MOOT · 1 CONFIRMED · 5 verified already-covered.** Plus **three defects that were in no candidate at all.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, Fourth Judicial District Court, Provo — case type FS. · **Prepared:** 2026-08-16 · **Status:** v1.0

**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. Tyler Robinson has NOT been bound over; the presumption of innocence applies.** ⚠️ **Lance Twiggs was GRANTED use immunity by two offices and his sworn statement was received in lieu of live testimony; he is accused of nothing.**

**Method validation, first:** `./tsearch.py --validate` → ✅ *"method validated — known positive `/use pliers/` found in day4.txt"*, re-run before every search. All file parsing in Python with `errors='replace'` (hazard 13 — **no bare `grep` null is relied on anywhere below**). **Every claim worked from `day1–5.txt`, not from the write-up.**

---

## 1. Verdicts

| ID | Claim | Verification act | VERDICT |
|---|---|---|---|
| **F2-134** | §14 item 3: *"Day 3 was opened here for one purpose only — the immunity question"* | 8 pattern families swept for unlabelled Day-3 content; both cited passages verified verbatim | 🚨 **REFUTED** |
| **F2-105** | §9 `F-10`: *"four resolve outright on Tier 1 (#1, #2, #3 and #8a)"* | all 11 §7.4 rows parsed on unescaped pipes; #1/#2/#3/#9 verified verbatim | ⚠️ **PARTLY** |
| **F2-51** | §6.1's lead sentence versus its own receipt caveat | §6.1 read as it now stands; both Day-2 hits opened; five wider stems run | **MOOT** *(with a live residual)* |
| **C2-47** | *"Day 4 delivered the trillion figures with none of the qualifications"* | all 7 patterns re-run, then each on a wider stem; every hit opened | ⚠️ **PARTLY** |
| **C2-43** | *"no exhibit was displayed on any monitor during her testimony"* | the Day-5 sanction ruling and the court's mid-testimony clarification read in full | ⚠️ **PARTLY** |
| **C2-44** | The State misstated the DNA report exhibit numbers on Day 5 | 9 hits across `day4/day5`, all opened | ✅ **CONFIRMED** *(low materiality)* |

---

## 2. 🚨 The most consequential result is about this file's own process

**The revision log records corrections that were never applied to the body — and it has done so at least three times.**

DNA-E01 **v4.1** (2026-08-14) announces **"SIX CORRECTIONS APPLIED HERE"** and lists (1)–(6). Verified against the body:

| | status |
|---|---|
| (2), (3), (4) | ✅ applied |
| (5) | ⚠️ **not applied until v4.2, two days later** |
| (1) | ⚠️ **half-applied** — it fixed the safety defect but not the count it identified (§1.5 rule (3) still said "exactly six" where the log itself named a **seventh** site) |
| **(6)** | 🚨 **NEVER applied until v4.3, today** |

🚨 **Second-order effect, and it is the expensive one: tranche 2 re-derived `F2-133` from scratch on 2026-08-16 without noticing that v4.1's own log had already stated the same correction on 08-14.** Work was done twice because a log entry was trusted as evidence that a fix had landed.

✅ **Standing rule adopted: diff the revision log's CLAIMED corrections against the body before treating any log entry as evidence.** This is [[annotating-is-not-editing]] at scale → **Q-106** extends the check to every file.

---

## 3. Detail

### F2-134 — REFUTED. Day 3 was opened for two purposes, not one.

**Steelman considered and rejected.** The strongest reading is that both Day-3 citations concern one subject — Twiggs and the disposition of his out-of-court statement. **It fails on three grounds:** the passages are 1h40m apart, by different speakers, on different questions — at `01:05:09` a witness testifies that use immunity was granted **by two offices**; at `02:45:18` **the Court rules**, on a Rule 403 objection, that a span of Exhibit 16 may not be published in the courtroom or on camera *"to protect the jury pool."* One is testimony about a prosecutorial grant; the other is a judicial publication order. **The file itself separates them elsewhere**, and its own v4.1 log names them as two.

**Wider-stem re-run before refuting**, as required: `/02:4\d:\d\d/`, `/01:0\d:\d\d/`, `/Davis/`, `/1102/`, `/Exhibit ?16/`, `/jury pool/`, `/publish|publication/`. **No third Day-3 passage exists** — so the refutal is exactly two, not more.

⚠️ **The error ran in the direction of UNDERSTATING this file's own coverage**, which is worth noting: not every defect inflates.

### F2-105 — PARTLY. The count is right; the membership is wrong on two, and the errors cancel.

**Parsed all 11 §7.4 rows.** `#8a` is **out** — its own row grades the residual *"unverified"* and **§12 names it one of "the two live survivors"**; an entry the file calls a live survivor cannot simultaneously resolve outright. **`#9` is in** — discharged on the witness's **own direct testimony** at `day2.txt` 05:54:50 (*"one of the contributors was 11% and the other was approximately 89%"*), verified verbatim, no residual stated.

**Steelman for the file's version:** that *"resolve"* means the **media conflict** is adjudicated, and #9 was a self-inconsistency within one outlet, hence *"discharged"* rather than *"resolved."* ⚠️ **Coherent, but it does not survive §13's own sentence**, which puts *discharged* in a separate bucket while still counting four — **and it cannot rescue #8a**, which §12 classifies as unresolved.

**A defect found alongside, in no candidate:** §13's §7 row enumerates buckets summing to **10 against 11 rows** and calls the tail class *"three"* where it is **four**. **Off by one, low — the same signature as `F2-133`.**

### F2-51 — MOOT as banked, with a live residual that ran the other way

The banked wording was already corrected at v4.1. ✅ **The correction was verified rather than accepted:** both Day-2 hits opened; `/permission/` = 5 (only two concern this witness, both about *requesting*), `/consent/` = 0, `/granted/` = 0, `/approv/` = 3 (all unrelated), `/authoriz/` = 1 (unrelated). **Nowhere does the witness testify that permission was received.**

⚠️ **But §6.1 carried the caveat TWICE at two different strengths**, because the v4.1 text was inserted in front of the v4.0 text without removing it. The retained narrow form — *"whether permission was RECEIVED **before the samples themselves arrived**"* — **presupposes receipt occurred**, and so understates the correction standing two sentences earlier. **Removed at v4.3.**

⚠️ **A recording-layer note kept for its own sake:** §6.1 renders an exchange as *"…before you even saw any of the evidence, correct?" — "Yes."* The record shows the witness interposed a clarifying question before answering. The elision does not change the proposition — **but it compresses a witness's own narrowing, which is the exact move §6.1 criticises another file for two paragraphs later.**

### C2-47 — PARTLY, and it produced a new standing hazard

All seven banked nulls **hold** on `day4.txt`, each re-run on a wider stem. **But the inference does not.** `/likel/` = **10**, and eight are paragraph D read **verbatim in full two-proposition conditional form** at eight separate timestamps.

🚨 **So "Day 4 delivered the trillion figures with none of the qualifications" is wrong, and wrong in the direction that matters most** — it would license a downstream file to say Day 4 gave **bare** figures. It did not. **The conditioning IS on Day 4; the witness-level caveats are not** (activity-level disclaimers, degradation, secondary transfer, contributor-count caution, STRmix — all genuinely zero).

✅ **New standing hazard 14: a null battery cannot test an inference its patterns cannot reach.** Not one of the seven patterns contains the string `likel`. **No pattern in the set could ever have seen the thing the set concluded was absent.**

### C2-43 — PARTLY, and the reader reversed its own first reading

**The first read refuted this item.** The sanction as issued bars *media capture* of exhibits *"displayed by the parties"* — which presupposes display continues, and exhibits plainly were displayed.

✅ **The wider re-run reversed it**, finding the court's clarification delivered **during the testimony**: *"The order of the court based as a sanction is **no exhibits will be displayed**"* — *"In the courtroom entirety?"* — *"**As it stands right now, yes, that's correct**"* — and *"This monitor is not on either. So **it's only the attorneys.**"*

⚠️ **The accurate statement distinguishes two things the banked wording merged: display to counsel and witness CONTINUED; publication to the courtroom and capture by the media camera did NOT.**

🚨 **Why this is the most useful new thing in the tranche:** the ATF analyst was called **after** the ruling. **Every document counsel navigated during her testimony was never published to the courtroom and never captured by any camera** — so **the transcript is the only record of their content, and an acquisition route the roadmap treated as open is closed.** Added to DNA-E01 §1.1 at v4.3 (caveats go first). → **Q-108.**

✅ **This is precisely why the "re-run wider before refuting" rule exists, and it earned its keep here** — an honest reversal by the checker, not by a later reviewer.

---

## 4. ✅ Twelve confirmations, logged deliberately

*Per the verify-in-both-directions rule.* §1.8's `/immunity/` row reproduces exactly and is robust to stem-widening · the `/destructive testing/` day-2 count of 2 reproduces, both hits opened as one exchange · three Day-3 nulls hold on wider stems · both Day-3 citations verbatim · §7.4 **#1**, **#2** (including *"item seven is the towel"*), **#3** (**stronger than the file states** — the sequence explains why both media labels were right *at the times they described*) and **#9** all verbatim · §1.5's *"Bakker never utters either figure"* holds — the two `/octillion/` hits are another witness reading and the prosecutor re-reading · **§1.4's 79%-garble note and its D-57 assignment verified on all three limbs**, with §7.4 #1 correctly stopping its quotation before the garble · and **five completeness candidates found no gap** — the file already covers them.

---

## 5. New traps, beyond the two promoted to standing hazards

1. **Four self-counts in one file now run one low, in the same direction** — 26→27, 15→16, "three"→four, "six"→seven. **A class, not a coincidence** → standing hazard 15.
2. **A count's UNIT must be stated.** §7.4's *"ten discrepancies"* occupy **eleven rows** because one splits a/b — the same shape that produced `F2-133`'s 27-rows-vs-29-patterns.
3. **A v4.2 fix did not sweep the whole file:** the v4.0 revision-log row still asserted *"Twenty-six verification searches are tabled at §1.8"* in the present tense. ✅ **Fixed by annotation rather than falsification** — the row is preserved as a record of what v4.0 asserted, with the true figure noted.
4. 🚨 **The banked-remainder figure is stated three incompatible ways.** Parsing every bank on disk: **F2 147 · C1 60 · C2 48 · CR-E07 58 · CR-E08 66 = 379**, plus Finder A's **187** held only in a session transcript = **566**. DNA-E01 said *"~360+"*; CR-REVIEW-2026-08-16 §5 itemised **508**, **omitting CR-E07's 58** — possibly deliberate (they are M-numbers, roadmap mechanics rather than Q-61 candidates) **but the omission is not stated.** **No file on disk carries a defensible total** → **Q-107**.

---

## 6. Coverage and residual scope, stated honestly

**Tested:** 3 of 3 assigned claims to verdict; **9 of 48** `C2-*` reached — three to verdict against the transcript with wider-stem re-runs, six verified as already covered. **39 `C2-*` items remain untested.** **Total resolved this tranche: 12.** New defects found that were in no candidate: **3**.

**Not reached:** `C1-*` (60), the remaining `F2-*` (144), CR-E08 (66), CR-E07 (58), Finder A's 187.

**Not re-verified:** DNA-E01 §§3, 4, 5, 8; the **D-53/D-54 cores**; the 11/6/5 consumption arithmetic; the thirteen-ratio count; the isoallele and paragraph-E counts; every §9 grade other than `F-10`. **Q-61 round 1's verdicts on those stand untested by this pass.**

**Not read:** `day1.txt` at all; `day3.txt` end to end. **No hearing day was read end to end for this tranche.** **No exhibit was obtained — every figure still reaches this library through a witness reading an unread report.**

⚠️ **The C2-43 sanction finding is scoped to Day 5.** Whether the sanction was later modified, and whether Day-1–Day-4 footage of displayed exhibits exists, is **unchecked — a checkable, not a finding.**

⚠️ **Hazard 9 respected:** the speaker of the Day-5 exhibit-number line was not resolved beyond *"a party, not the media attorney"*; the banked item's *"the State said"* is plausible from content and **is not adopted here.**

**No headline finding moved. D-53 and D-54 are untouched. DNA-E01 remains `[PROVISIONAL]`.**

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. Q-61 tranche 3: **12 claims resolved, 3 defects found that were in no candidate.** 🚨 **The headline result is procedural: DNA-E01's v4.1 revision log announced six corrections and only three had been applied — one stood unapplied for two days, and tranche 2 re-derived a correction the log had already recorded, doing the work twice.** → Q-106. **Two standing hazards promoted: 14** (a null battery cannot test an inference its patterns cannot reach) and **15** (self-counts run one low as a class). **DNA-E01 → v4.3** with six corrections applied and a new §1.1 access-path caveat that **closes an acquisition route** (Q-108). |
