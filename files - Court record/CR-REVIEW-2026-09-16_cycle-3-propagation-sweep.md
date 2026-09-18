# CR-REVIEW-2026-09-16 — Cycle 3: the propagation sweep of the 2026-08-30 corrections

**File ID:** CR-REVIEW-2026-09-16 · **Case:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo Department — Hon. **Tony F. Graf, Jr.** · **Prepared:** 2026-09-16 · **Status:** **v1.0 — `[PROVISIONAL]`.** This file reports a verification cycle and has not itself been read by anyone but its author. Unlike `CR-REVIEW-2026-08-30`, **every count here is re-auditable**: the 21 reader reports it rests on are banked as JSON in `verification/CR-E19-E20-E21-REVIEW-2026-09-16_verification-cycle-3/`, alongside the enumeration, the script hit lists and the worklists.

> 🚨 **CASE POSTURE, as of 2026-09-16.** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; pretrial conference 2026-10-23. **Presumption of innocence applies in full.** No court has found any fact in the files this cycle touched to be true; no court has ruled on the scientific reliability of any forensic method or result (Rule 1102 admissibility rulings are a different question and were made). Nothing in this file is a finding about the case — it is a finding about the library.

> **Living persons.** No living person is characterised here. Two names recur only because the corrections concern how the library writes about them: Matthew Robinson and Lance Twiggs are elimination-sample donors, accused of nothing, and a "support for inclusion" statement is not a source attribution — that sentence is one of the corrected forms this cycle propagated (`C-01`/`C-02`). The FBI latent-print personnel whose names the library withdrew are referred to by role only; three readers ran masked token checks and found no surviving surname in the origin files.

---

## §1 · What cycle 3 was, and how it was sized

`CR-REVIEW-2026-08-30` §10 set the brief: **sweep for PROPAGATION, not for claims** — three consecutive correction rounds on `CR-E19`, `CR-E20` and `CR-E21` had each introduced defects of the class they were fixing, and a corrected claim's WITHDRAWN form could stand anywhere in the library that had cited it. `VERIFICATION-PROTOCOL.md` §3 names the mechanism (taint propagation) and caps the process at **three iterations**; this is the third.

The first design, a 79-agent workflow, was stopped by the owner on 2026-09-16 (*"there should not be 79 agents"*). The cycle was re-sized **script-first, readers second, at most four or five readers at a time**:

1. **Enumeration** (done before the stop): four enumerators and one merge produced **74 corrected claims** (`C-01`…`C-74`), each with its withdrawn form, withdrawn terms, corrected form and record sites (`enumeration_merged-74-claims.json`).
2. **Script sweep:** the 74 claims' withdrawn terms were matched against every `.md` in the library's citation namespace plus the two published deliverables — **6,656 raw hits**, reduced by de-duplication and record-site exclusion to a **worklist of 912 hits across 34 files** (`script-sweep_hits.json`, `script-sweep_worklist.json`). A second sweep built the origin files' own hit lists (`script-sweep_origins.json`).
3. **Readers, under the isolation rule:** one reader per file (two small files shared one), given **the file and its hit list — never the corrections and never a diagnosis** — asked to classify each hit STALE / CONSISTENT / RECORD / UNRELATED / AMBIGUOUS, to quote the exact sentence and a minimal replacement for every STALE hit, and to flag OFF-LIST carriers seen on the full read. Twenty-one reader reports were banked (`reader_*.json`). Fourteen tail files with six hits or fewer were classified by the coordinator from the files.
4. **Application:** the coordinator applied every STALE and OFF-LIST fix in place with a revision-log row per file, and committed file by file (18 commits, `de2bc04..44ab0eb` and after).

---

## §2 · Results

**Hits classified (readers): STALE 124 · CONSISTENT 258 · RECORD 345 · UNRELATED 339 · AMBIGUOUS 25** — over 1,091 reader-reviewed hits on 20 library files plus the deliverables; **off-list stale carriers found on full reads: about 60** (the script's terms miss hyphenations, re-orderings and the highest-frequency phrases).

| Reader | Hits | STALE | CONSISTENT | RECORD | UNRELATED | AMBIGUOUS | Off-list entries |
|---|---|---|---|---|---|---|---|
| DELIVERABLES (docx + live artifact) | 63 + 58 | 13 + 39 | — | — | — | — | (structured differently; see the bank README) |
| CR-E06 | 106 | 16 | 30 | 14 | 45 | 1 | 0 |
| TJR-P01 | 95 | 9 | 40 | 15 | 29 | 2 | 0 |
| DNA-E01 | 180 | 28 | 27 | 43 | 79 | 3 | 0 |
| CR-E15 | 50 | 10 | 15 | 12 | 13 | 0 | 0 |
| CR-E14 | 47 | 5 | 8 | 15 | 7 | 12 | 5 |
| CR-E03 | 42 | 2 | 12 | 21 | 7 | 0 | 0 |
| CR-E02 | 41 | 9 | 7 | 13 | 12 | 0 | 0 |
| CR-E07 | 29 | 0 | 5 | 7 | 17 | 0 | 5 |
| CR-E01 | 24 | 4 | 4 | 9 | 6 | 1 | 0 |
| LT-P01 | 22 | 4 | 3 | 5 | 9 | 1 | 0 |
| CR-E05 | 22 | 0 | 11 | 6 | 5 | 0 | 4 |
| SEC-E01 | 19 | 1 | 8 | 0 | 10 | 0 | 3 |
| CR-E16 | 15 | 1 | 5 | 1 | 8 | 0 | 6 |
| CR-E12 | 12 | 0 | 1 | 1 | 10 | 0 | 4 |
| CR-E08 | 12 | 0 | 0 | 0 | 0 | 0 | 1 |
| SEC-E02 | 11 | 1 | 7 | 1 | 2 | 0 | 3 |
| CR-E17 | 11 | 2 | 1 | 1 | 7 | 0 | 3 |
| ORIGIN_CR-E19 | 132 | 13 | 24 | 63 | 30 | 2 | 6 |
| ORIGIN_CR-E20 | 108 | 10 | 17 | 59 | 21 | 1 | 0 |
| ORIGIN_CR-E21 | 125 | 9 | 33 | 59 | 22 | 2 | 7 |

**Files corrected, with their new versions:** `CR-E06` v1.9 · `TJR-P01` v2.7 · `DNA-E01` v4.11 · `CR-E15` v1.4 · `CR-E14` v1.5 · `CR-E03` v1.7 · `CR-E02` v1.10 · `CR-E07` v1.8 · `CR-E01` v1.5 · Twiggs profile v1.6 · `CR-E05` v1.6 · `SEC-E01` v1.3 · `CR-E16` v1.3 · `CR-E12` v1.4 · `CR-E08` v1.3 · `SEC-E02` v1.3 · `CR-E17` v1.3 · `CR-E18` v1.3 · `CR-AUDIT-2026-08-20` v1.1 · the Erika Kirk dossier v1.4 · `zinn-george-evidence` v1.3 · the official timeline (dated entry) · the superseded 2026-07-15 DNA audit (dated entry) · **the three origin files: `CR-E19` v2.5, `CR-E20` v1.8, `CR-E21` v1.5** · the Word deliverable (`Forensic-Sampling-Summary_2026-08-30.docx`, ten replacements, re-hashed). Status lines regularised without other change in `BOC-ROUTE` v1.3, `CR-ACQ-2026-07-27` v2.1, `CR-ACQ-2026-08-16B` v1.1, `CR-E04` v1.3, `CR-E11` v1.3, `CR-E13` v1.3. **No finding's grade was raised anywhere; one was lowered to match its own head (`CR-E19 F-3`, Medium).**

**Not corrected, by rule or gate:** the live artifact *"What Was Swabbed"* — its 14-replacement patch is banked (`artifact-patch_2026-09-16.json`) and publishing is owner-gated; `CR-E10`, `CR-E11`, `CR-E09`, `CR-E13`, `ZINN-ACQ` and the roadmaps — every script hit there was a term collision or a true statement about the file.

---

## §3 · Findings — about the library, not the case

**`R-1` — The widest carrier of the cycle was not one of the enumeration's headline claims. It was the posture clause.** *"2026-09-01 is its last day — argument only, on a closed evidentiary record"* is an inference `CR-E20` v1.4 withdrew on 2026-08-30 (the court said only that the matter was continued for argument). It still stood in **thirteen live files** — including `CR-E19`'s own header, a graded finding in `CR-E17` (`A-2`), and the Twiggs profile at four sites — and the 2026-09-16 posture note appended beneath each banner (*"retained as written, true as of its date"*) **ratified it rather than curing it**: a note appended under a sentence does not check the sentence. Every site is corrected in place with an inline 🛠. (`C-57`; the residual is `TJR-P01` §1's post-hoc description of 09-01, left as its reader graded it.)

**`R-2` — In the origin files, the corrections of 2026-08-30 were applied to the paragraphs that were wrong and not to the paragraphs that summarised them.** `CR-E20`'s §5 FINDINGS summaries (`F-1`, `F-3`, `F-4`'s grounds) and its §6/§8 items still carried the withdrawn forms its §3/§4 had corrected; `CR-E19`'s §9 lead, §12 and the header's dangling *"until one has"* still said no cycle had run; `CR-E21`'s §3 box still marked as *owed* a correction `CR-E20` had executed the same day. **A correction has a footprint inside its own file too** — findings summaries, residual lists, open-items lists, status lines — and none of the 08-30 rows swept it.

**`R-3` — A revision-log row can assert changes the body does not carry, and this library wrote one on 2026-09-16.** `CR-E19`'s row 2.3, reconstructed *from the in-body stamps*, recorded *"F-7 carried into §9"* and *"§0/§1 updated for v2.2's two new sources"*; neither had been done. Both are done now (v2.5), so the row is true — but the lesson is the memory note's: **annotating is not editing**, and a row written from stamps inherits the stamps' claims. A second record-site defect, in `CR-E20` §4: a global replace on 08-30 had overwritten the withdrawn wording *inside the quotation of the earlier form*, so the sentence denied the corrected bound. Restored.

**`R-4` — The script found the sites the readers could not have read, and the readers found the sites the script could not match.** 124 STALE hits came off the list; about 60 more came off full reads — *"the record's own framing"* variants, *"submission-one"* hyphenated, *"State's Exhibit 32"* used flat as a name (every `C-38` site in `CR-E15` had that one shape), the hearing-designator/laboratory-item collision in `SEC-E02` (*"State's Exhibit 6"* for the ATF report's own item 6). Neither pass alone would have done.

**`R-5` — Status lines lag their logs whenever a script writes rows.** The 2026-09-16 posture-row script appended a row to 32 files and bumped no header; `CR-E07`'s row was stamped with a number already used. Thirteen files read v1.x against a newer row; every one is regularised, and the check (`scripts/` owes it — see §5) belongs in `queue-check.sh`.

**`R-6` — Files make stale statements about *other* files' status, and no sweep had a term for it.** `SEC-E01` §1.7 called `SEC-E02` PROVISIONAL a month after it was VERIFIED; `SEC-E01` §9.2 said `Q-172` was *"STILL UNCORRECTED"* after its own `F-117` recorded the execution; `CR-E14` §1/§12/§13 said no laboratory report was held after its own §5 note said one was; `CR-E12` §1/§11/§12 kept an absolute null its own `N-4` had narrowed. **A file's statements about its siblings and about itself age exactly like its statements about the record.**

**`R-7` — Both directions.** The corrected forms WERE present at their home sites in every origin file: `CR-E20` 23/23 claims, `CR-E19` all but `C-31` (`F-7` missing from §9) with three partial, `CR-E21` all but `C-23`. The 08-30 corrections were made; what failed was their propagation, inside and outside the file — which is exactly what §10 of the previous review predicted and is the reason this cycle had to run.

---

## §4 · The `[PROVISIONAL]` flag — decided by judgement (`DECISIONS.md` R1)

The protocol caps verification at three iterations and says: *publish what is labeled; what is unchecked at the cap is published as unchecked.* This was the third. **`CR-E19`, `CR-E20` and `CR-E21` remain `[PROVISIONAL]`, on a restated ground:** each origin file still carried withdrawn forms in its own body when this cycle opened (13, 10 and 9 STALE sites), so the 08-30 corrections were not fully applied; today's corrections are themselves unread; and the cap is reached. **The flag no longer means "another cycle is owed." It means the files are published as labeled and may be cited only with their labels, and clearing it is the owner's reading of the cycle-3 rows, not a fourth sweep.** `CR-REVIEW-2026-08-30` v2.1 and this file carry the same flag for the same reason. No file certifies itself.

---

## §5 · Residual — what this cycle did not do

1. **The live artifact** was not republished (owner gate); link-holders still see a pinned pre-correction version. The patch is banked.
2. **The profile deliverable** `deliverables/Tyler-Robinson_Comprehensive-Profile_2026-09-14.html` was **not in the sweep's scope** and mirrors `TJR-P01` v1.x; it carries at least the `C-57` sentence. Regenerating it from v2.7 is a separate act.
3. **Twenty-five AMBIGUOUS hits stand**, each named in its file's cycle-3 row: chiefly whether the carry-both-grades rule for `CR-E20 F-4` / `CR-E15 F-139` is per file or per citation (`DNA-E01` ×3, `CR-E21` §9), whether a cross-file pointer counts as a guard travelling (`C-09` in `CR-E19` §6A.3, `CR-E21` §5), and headings that are true-but-weaker than their boxes.
4. **The scope was the `.md` citation namespace plus two deliverables.** `START-HERE.md`, `QUEUE.md`, `DOCKET-WATCH.md`, the vault and the routine prompt were not swept; `START-HERE` §0AH still describes `CR-E21` as *"fifteen items … of which the library holds one"* in its own voice.
5. **Log-row slips noted, not edited** (a row records what a version said): `CR-E19` row 2.2 *"68-PAGE"*; `CR-E03` row 1.1 *"(bolt, 1.6)"*; the withdrawn `C-01` sentence in `CR-E03` v1.5, `CR-E14` v1.3 and `DNA-E01` v4.8 rows.
6. **`CR-E20`'s bare-designator disclaimer** (Rule 2 compliance withdrawn at v1.6) stands; fifteen sites were owned this pass, and the file still does not claim compliance.
7. **This file's own counts** were produced by a script over the banked JSON (`scratchpad/cycle3_tally.py`, not banked); the per-reader figures are the readers' own and were not re-derived.

---

## §6 · P10 — session close log

- **P1 before drafting:** every replacement carried a corrected form from the enumeration or a reader's quoted sentence; one suspected defect outside the claims (the timeline's *"Sgt. Faumuina read the FBI report's findings"*) was checked against `day2.txt` 05:10:57 before touching it and found correct.
- **P8 (numbers):** the manifest count re-derived (361, 2026-09-16); the hearing interval re-derived (three months and eleven days); `TJR-P01`'s set totals removed under its own §16 SINK rule rather than re-counted.
- **Isolation:** readers saw files and hit lists only. Confirmation rates were not 100%: the readers returned 339 UNRELATED and 258 CONSISTENT against 124 STALE, and two readers' proposals were declined or narrowed by the coordinator (a `CR-E14` F-100 pointer re-worded to what `F-100` says; `CR-E02`'s reader chose `CR-E15`'s bound where others chose `CR-E20`'s — both allowed by the rule).
- **Names:** no withheld personnel name was written by any reader or in any file; the Twiggs-profile reader was told to flag, not reproduce, any private detail, and found none.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-09-16** | File created at the close of cycle 3. 21 reader reports banked; 27 library files and one deliverable corrected in place; three origin files at `CR-E19` v2.5 / `CR-E20` v1.8 / `CR-E21` v1.5; the `[PROVISIONAL]` flag restated (§4). |

*End of file.*
