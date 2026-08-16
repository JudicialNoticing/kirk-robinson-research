# CR-REVIEW-2026-08-16E — Q-111: the legacy files, and a route null that outlived its own acquisition

**Scope:** completion of **Q-111** — re-running every null, count and absence claim in **CR-E01 … CR-E07**, **CR-WATCH-log** and the **five candidate banks**, the files the earlier Q-105 pass never reached. **~100 claims tested: ~75 CONFIRMED · 8 REFUTED · 8 QUALIFIED · 3 blocked-route-as-null.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. Tyler Robinson has NOT been bound over; the presumption of innocence applies.** ⚠️ **The turn-count and speaker-label findings below are facts about a transcription service's rendering and carry no implication about anyone named in it.**

---

## 1. The scope answer first: the extraction hazards barely touched these files

**Six of eight targets are not exposed at all.** CR-E01–CR-E06 run every null against `day1`–`day5.txt`, which carry **zero NULs and zero U+FFFE**. CR-E07's source — the banked defence brief — is one of the **nine** artifact `.txt` files that were never NUL-affected, and carries **zero U+FFFE**.

**Hazards 13 and 16 yielded 2 defects across ~9 targets.** ✅ **The auditor said so plainly rather than manufacturing findings to fill the gap.** The real yield was in the **count** and **absence** classes.

⚠️ **One census correction:** the published hazard-16 sweep covered 15 `.txt` files and **never looked at the `.jsonl` candidate banks. One is affected** (§3, A9).

---

## 2. 🚨 The finding that matters most: a route null outlived its own acquisition — in SEVEN places

**`day1.txt` was located and banked on 2026-07-28** at Rev's divergent slug `ut-v-tyler-robinson---day-1` (commit `536e2cc`, *"Locate Day 1 (new slug); REVERSE D-51"*), 327,506 bytes, 2,600 turns, and **read end to end at CR-E05 the same day.**

**Seven live sites across five files still said it had never been found:**

| file | what it said | aggravating fact |
|---|---|---|
| **CR-E02** | *"Day 1 never located"* | 🚨 **at v1.5, dated 2026-08-14 — seventeen days after the acquisition** |
| **CR-E03** | *"Day 1 — never located on Rev; date unfixed (D-51)"* | 🚨 **§7 of the SAME FILE records D-51 as reversed and the dates as fixed** |
| **CR-E04** ×2 | *"has never located (Rev has no Day 1)"* | 🚨 **the same v1.2 edit cross-references CR-E05 — the Day 1 file** |
| **CR-E01** | *"Day 1 was never located"* | — |
| **CR-ACQ-2026-07-27** | *"Day 1 never located"* | the founding acquisition record itself |

🚨 **This is the mirror image of the day's other structural finding.** At CR-E12 a **docket observation was promoted into a claim about our holdings**. Here a **route null was left standing after the artifact was acquired**. Both are the same failure viewed from opposite ends: **the library's statements about what it has are not being reconciled against what it has.**

✅ **All seven corrected in place, and verified to zero live sites afterwards.** ⚠️ Revision-log rows carrying the phrase were deliberately **not** touched — a revision row is a true account of what that version said.

---

## 3. 🚨 The other seven refutations

**A1 — CR-WATCH-log: the two extractions of the defence brief are NOT identical.** The file said *"identical … 91,729 characters on both sides."* Re-measured: banked **91,729**, DocumentCloud re-render **91,715**, **first diverging at character 671** where the two-column caption is read in a different order (*"vs. Plaintiff,"* against *"Plaintiff, vs."*). The re-render also carries three `U+FFFE` splits the banked extraction does not.
⚠️ **The claim was load-bearing** for *"same document, same page count, same text"* — and it contradicts the library's own later finding that two extractions of one PDF differ in ways that produce false nulls. ⚠️ **A subtlety worth keeping: the re-render's normalised length CHANGED on 2026-08-16** when its 41 NULs became form feeds — a NUL is not whitespace, a form feed is — **so pre- and post-repair figures are each correct at their own date.**

**A2 — the candidate-bank index over-corrected and discarded a true fact.** It said the Oliver leg *"is also **not a spend limit**: a rate limit is transient and retryable."* The `429`'s **type** is `rate_limit_error`; its **message body** is *"You've hit your **monthly spend limit**"*, and the coordinator's own resume message reads *"cut off by an **account spend limit**."* ✅ **The leg did complete and returned 48 of 48 — that half was right.** ⚠️ **But clearing it was an OWNER action, and "retryable" is the wrong lesson for a resumer.** ⚠️ **This project propagated the wrong form into START-HERE and QUEUE; corrected in all four places.**

**A3 — `/qualif/` on day 2 is 9, not 10.** Verified under four counting methods, all nine opened. ✅ **The trap itself is confirmed.**

**A5 — four witness turn counts, all low, all from one defect.** Hull **347 → 376**, Bakker **391 → 407**, Davis **174 → 175**, Oliver **184 → 196**. **Root cause, and it is reusable: the condensed transcripts merge some speaker labels onto the tail of the previous line** (`day5_condensed.txt` contains `Correct. Michael Burt:` ×50), so **a `^Name:` count over a condensed file is systematically low.** Counting `Name:` anywhere reproduces the full transcript exactly in all four cases.
⚠️ **Fifth through eighth instances of standing hazard 15** — one low, always the same direction. ✅ **Counter-examples logged:** two other counts in the same files are right, because none of those labels got merged.

**A6 — CR-E07's corrected exhibit list DROPPED a designator the superseded list had.** The brief prints **`St.Ex. 16`**, a form the file's own stated sweep cannot match, in its most-quoted sentence. 🚨 **The struck v1.0 list had "16"; the v1.3 correction that grew the list from 7 to 21 removed it — while §5 continued to call StEx 16/16.1 load-bearing for three of four arguments.** ✅ The count 21 held only because the printed range *"19-22"* was counted as two; expanded, the brief names **twenty-four** distinct exhibits. ✅ **F-20 predicted this exact failure mode and is credited.**

**A7 — a corrected date was never propagated back.** CR-WATCH-log still said the supplemental notice was *"created 2026-07-09 — filed DURING hearing week, between Day 4 and Day 5"* in four places. **The document's own certificate reads *"e-filed … on July 8, 2026"*** — the evening of Day 3 — and **CR-ACQ-2026-08-14B corrected it on 2026-08-14 and said so in terms.** ⚠️ **The project rule is that supersessions get matching rows on BOTH ends; only one end had one.**

**A8 — CR-E05 cites a §3.6 that does not exist** (sections run §3.0–§3.5). **Introduced by today's v1.3 restoration.** *A locator that cannot be re-found is a broken citation.*

**A9 — hazard 16 has propagated INTO a candidate bank.** `…CRE08-completeness…jsonl` carries `low￾crawling`; `low-crawling`, `low crawling` and `lowcrawling` all return **0**. A three-way false null **inside a bank**, and the published census never looked at `.jsonl`.

---

## 4. 🚨 Three corrections to CR-E06 — a VERIFIED file

⚠️ **Each was independently re-verified by the orchestrator against the transcript BEFORE the edit** — the discipline the 2026-08-14 false-refutal episode exists to enforce, since a false refutal reached a verified file then and had to be reversed by the owner.

- **§6's *"Zero occurrences in lines 5070–8862"* is false** as a claim about magnitude words: `quadrillion` sits at **L6899**, in range. ✅ **The headline survives and is now exact** — `octillion` and `quintillion` are both zero there.
- **§1.2's *"Jeff Dyer (9×)"* is 7 strings / 6 labels**, all Day 5 — and **"Jeffrey Neiman" appears on Day 3 as well as Day 4.** ✅ **The finding is untouched; its day-scope was one day too narrow.**
- **§2.6/§9.8's `THO1` appears nowhere** — the transcript reads bare **`THO`** and the value **`79.3`**. ⚠️ **Third member of a garble class this file already documents** (`BWA` for vWA; `D3S-loci` for D3S1358).

**CR-E06 → v1.4. No headline result, no register entry and no case-posture statement moves.**

---

## 5. ⚠️ Blocked-route-logged-as-null — three instances, against a strong record

✅ **The credit is the dominant pattern and must be stated first.** CR-WATCH-log flags unattemptable routes correctly at least six times — *"unattemptable, not empty — no evidential weight"*, *"⛔ UNAVAILABLE… Not a null"*, *"NOT ATTEMPTED — a scope statement, not a null"* — and flags a `429` three separate times as *"a rate-limit is NOT an absence."*

**Three genuine misses (→ Q-121):** **C1**, a bot-gated route folded into a *"NOT FOUND"* verdict beside three genuinely-attempted ones — and the null later proved false. **C2**, *"NONE EXISTS, on positive enumeration"* overstating its method, with the file now contradicting itself about which transcript null was the first with real weight. **C3 → Q-120**, below.

**Q-120 is the one with an artifact behind it.** Run 4's Rev null filters the sitemap on the slug **`robinson`** — a filter that **cannot reach a case page slugged otherwise** — and **Run 1 of the same file names exactly such a page: a 2025-09-17 press briefing.** Measured: *"press briefing"* occurs **once in the entire repository**, in that row. **Not among the six, not banked, not queued.** 🚨 **And Run 4 logs the mirror-image trap in the same run** — *"match on the case, not on the surname"* — written for false positives and never applied to false negatives.

---

## 6. ✅ ~75 confirmations, logged deliberately

**The great majority of what was tested was right, and several nulls proved stronger than the files claimed.** CR-E05's eight universal absences all hold on stems with the substring traps run affirmatively clean (`wood` = 15, every one opened, every one *"Woodbury"*). **Its distance null survived a battery far wider than its own** — ten patterns including word-numbers and elevation terms — with the *"elbows, knees, and feet"* body-part trap excluded by reading. The seven-live-witness roster is exact, including that two of nine oath hits are **audio inside a played video exhibit**. Day 1's turn count is **2,600 exactly**.

**The `27 minute and 35 second` restoration was independently re-confirmed by the hazard-12 method** — numerals and words, singular and plural — landing on exactly two hits, exactly where v1.3 says. **v1.2's refutal really was an inflectional false null.**

**CR-E03's recess-continuity working reproduces to the second.** **CR-E01's counts are all exact** — and the auditor logged that **its own first pass was 88 turns low** because some turns render `MM:SS`, and that **its own first `Erika Kirk` search returned a false null** because the pattern could not match the garble `Erica`. *A false null of exactly the class the audit exists to find, committed while running it.*

**Every candidate-bank count verified by parsing, with no gaps** — 58 · 66 · 60 · 48 · 147 — the single cleanest result in the audit. **The five carried nulls re-run a second time, all five confirmed.** **CR-E07 held on both readings**, including the DNA null with the *kidnaped* trap affirmatively clean and SHA-256 `c3f39437…`. **Two CR-E06 nulls proved stronger than claimed** when widened to phrasings that avoid the searched word.

---

## 7. Residual scope — stated plainly

🚨 **Every route and retrieval claim in CR-WATCH-log is unre-runnable from here and was NOT audited** — the 55 Fox PDFs, the Wayback results, the seven Scribd endpoints, the 403s, the byte counts, the DocumentCloud enumeration. **What was audited is what those claims say about each other and about artifacts on disk, not what the network returned on the day.**

**Also not done:** CR-E07's external verifications (the *Murphy* retrievals, CourtListener/Justia) remain single-sourced. **No PDF was re-extracted** except the defence brief, where two extractions were compared **and found to differ**. **No exhibit is held**, so every claim that a witness read a document accurately remains untested against that document. Days 1, 3 and 4 were not re-read end to end. **Register-ceiling claims are historic assertions and cannot be re-run retroactively.** The 2025-09-17 press briefing was **not retrieved** — only established as named once, unbanked and unqueued.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-111 executed.** ~100 claims tested across CR-E01–E07, CR-WATCH-log and the five candidate banks: **~75 CONFIRMED · 8 REFUTED · 8 QUALIFIED · 3 blocked-route-as-null.** ✅ **Scope answer: the extraction hazards barely reached these files — 2 defects across ~9 targets, and the auditor said so rather than manufacturing findings.** 🚨 **The finding that matters is structural: a route null outlived its own acquisition in SEVEN places across five files — the mirror image of the day's docket-versus-holdings failure.** 🚨 **Three corrections to CR-E06, a VERIFIED file, each independently re-verified before the edit.** Corrections applied in place to CR-E01, E02, E03, E04, E05, E06 (→v1.4), E07 (→v1.5), CR-ACQ-2026-07-27, CR-WATCH-log, the candidate-bank INDEX, and this project's own START-HERE and QUEUE. **Q-120 and Q-121 raised.** |
