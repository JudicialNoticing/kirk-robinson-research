# CR-REVIEW-2026-08-16B — The XChange null audit: a tool failed silently, and it had been failing for weeks

**Scope:** execution of **Q-81** — re-running every null, count and absence claim in this library that rests on the two XChange docket printouts, after standing hazard 13 established that `grep` returns nothing at all on them. **26 claims tested to verdict. 14 CONFIRMED · 8 REFUTED · 2 QUALIFIED · 2 structural.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. Tyler Robinson has NOT been bound over; the presumption of innocence applies.**

**Method:** all re-runs in Python, `errors='replace'`, whitespace-normalised, stems not inflections, dates in **both** `MM-DD-YYYY` and `Month D, YYYY` forms, **every positive hit opened and read**. ✅ **The three largest refutations (R1, R2, R8) were independently re-verified by the orchestrator before any correction was applied** — *a refutal is a claim too*.

---

## 1. 🚨 The hazard is 25× larger than stated, and its published detector was wrong

**Hazard 13 as written this morning said: two files, detectable by `file(1)` reporting `data`. Both halves were wrong.**

**Scope — 50 files, not two.** A repo-wide NUL sweep of 193 files: **50 of the 59 `.txt` files in `CR-ACQ-2026-07-27_court-record-artifacts/` are silently skipped.** **Zero** `.md`, `.json`, `.jsonl`, `.html`, `.sh` or `.py` files anywhere are affected, and **zero** files in any other folder — including the five hearing transcripts.

🚨 **Detector — `file(1)` IS NOT A VALID TEST.** Two files that `file` calls *"Unicode text, UTF-8 text"* are **still silently skipped**, because `file` tolerates a single trailing NUL. **Auditing by the published predicate would have missed them.**

✅ **The correct predicate is `NUL count > 0`**, which matched the empirical skip behaviour on all 59 files with **zero error**:

```bash
for f in *.txt; do n=$(tr -dc '\0' < "$f" | wc -c); [ "$n" -gt 0 ] && echo "$n  $f"; done
```

**Root cause, both parts necessary:**
1. The PDF→text extractor emitted **`0x00`** where it should emit **`0x0C`** (form feed) at each page break — **31 pages → 31 NULs**, each sitting exactly at a `Page N of 31` footer boundary.
2. The harness `grep` is **`ugrep` invoked with `-I`**, which **skips binary files entirely — no output, no *"Binary file matches"*, exit 0.** ⚠️ **`/usr/bin/grep -ci` on the same file returns the right answer. The files are not universally grep-hostile; the wrapper is what silences them.**

✅ **Smoking gun — the same PDF, extracted twice:**

| file | page breaks | `file(1)` | grep-safe |
|---|---|---|---|
| `2026-08-11_defendant-prelim-hearing-briefing.txt` | 41 × `0x0C` | Unicode text, UTF-8 | ✅ |
| `…_ALT-EXTRACTION-dc28551955.txt` | 41 × `0x00` | data | ❌ **silently skipped** |

✅ **Integrity confirmed: all four banked SHA-256s match byte-for-byte. The NULs were present at acquisition — an extraction defect, not corruption or drift.**

---

## 2. 🚨 REFUTED — eight claims this library asserts that are false

### R1 — "no document numbers at all" is FALSE, and the library already relied on the contrary

**Both printouts contain four docket numbers, six occurrences each**, embedded in filing titles the parties themselves typed:

| number | maps to | docketed |
|---|---|---|
| **Dkt. #23** ×3 | *Protection Order RE: Pre-Trial and Trial Publicity* | 11-06, 11-28 ×2 |
| **Doc. 165** | *Motion for Limited Intervention* | 12-03-2025 |
| **Dkt 197** | *Response to the Motion for Limited Intervention* | 12-08-2025 |
| **Dkt. 325** | *News Media's Motion to Amend Standing Order* | 02-04-2026 |

🚨 **Why this is not cosmetic:** **CR-E12 grades Dkt. #23 at *High* citing "the State's own filing title as recorded on the docket"** — i.e. it takes a number from exactly the source three other files say can never supply one. **Two files asserted the register can never supply a number while a third supplied two from it.**

⚠️ **And one of the false assertions was written today and claimed a verification act that did not happen** — CR-ACQ-2026-08-16 §4 said *"now confirmed against the full 31-page file."*

**Corrected in place at six sites** (CR-ACQ-2026-08-14C, CR-ACQ-2026-08-16, CR-E12 ×2, CR-E13, QUEUE Q-80). **Q-80 was also mis-scoped** — it said the printouts *"cannot help"* audit `dkt<N>` filenames; they can, for a subset. ⚠️ **But read them under F-40:** `(Dkt 197)` sits in the title of the **response** to that motion, so a number in a docket title may name the filing being answered.

### R2 — "the February entries run 02-12 → 02-19" is a false characterisation

**February 2026 actually runs 02-02 → 02-26 — fourteen distinct dates.** The true fact is a **gap** between 02-12 and 02-19. ⚠️ **The conclusion survives (there is no 02-13 entry) but its stated basis is wrong**, and **12 of the 14 February dates fall outside the range as written — including 02-23 and 02-24, which carry the disqualification denial** (CR-E11 F-48, Q-86). A reader would conclude the docket is silent 02-01→02-11 and 02-20→02-28. **It is not.** Corrected at five sites.

### R3 — a false null from searching the assumed phrase instead of the stem

A pass concluded *"No withdrawal or substitution of counsel found… **the roster appears stable**."* `withdraw` = 0 ✅, `substitut` = 0 ✅, `Notice of Appearance` = 0 ✅ — **but `Notice of Limited Appearance` = 7 in BOTH files, all dated 09-30-2025.** Searching the bare stem **`Appearance`** returns 14 per file. ⚠️ **The conclusion is not supported by the search performed.** Hazard 12, live.

### R4 — the founding measurement of hazard 13 was itself miscounted, and corrected silently

The raw report recorded *"Python found **two** occurrences"* of `judd`. **The true count is four.** Downstream files all say four — **the figure was superseded without a revision row on either end**, contrary to *corrections in place, never silent*. ⚠️ **The irony is the point: this is the measurement that founded the hazard.** *(The raw bank is preserved verbatim and deliberately not edited; the correction lives here.)*

### R5 — "Attorney General" count is 4, not 3
The substance stands (all four concern the referral request). **The count does not — and the count was offered as the verification act.**

### R6 — `/preserve/` = 12, but not "all" one matter
Count confirmed at 12; **11**, not 12, concern the preservation motion. The 12th is unrelated minute-entry narrative **outside the stated date window**. ⚠️ *The file's own "open every hit" rule, applied to itself.*

### R7 — the coverage ceiling stated as 2026-03-15 in one place
`CR-WATCH-log.md` said the printouts are *"current only to 2026-03-15."* **The last docket entry is 2026-03-14**; 03-15 03:18/03:21 is the **generation stamp**, not coverage. Every other file says 03-14. Corrected.

### R8 — "they overlap heavily and corroborate each other" is FALSE for narrative content

The **event lists** do corroborate (506 vs 505). 🚨 **The short history contains no minute-entry narrative whatsoever.** Independently re-verified:

| term | FULL | SHORT |
|---|---|---|
| `Minute Entry` | 12 | **0** |
| `Tape Number` | 10 | **0** |
| `Clerk:` | 10 | **0** |
| `contempt` | 9 | **0** |
| `under oath` | 5 | **0** |

⚠️ **Any null tested against the short history alone is a FALSE NULL for narrative content — and the old wording licensed exactly that error.** Corrected.

---

## 3. ⚠️ Two qualifications that change what an existing finding means

**Q1 — the contempt null is literally correct and materially incomplete.** All 9 `contempt` hits are Rule 4-401.02 boilerplate, exactly as recorded. **But the docket records enforcement proceedings the file does not mention:** a **2025-12-11** finding that *"a violation of the decorum order has occurred"* with the State referring it for sanctions and a camera ordered moved; and a **2026-01-16** finding of a violation *"specifically to paragraph 48"* with **"the court sanctions the media."** (`decorum` = 11, `violat` = 13, `sanction` = 2.) 🚨 **Consequently CR-ACQ-2026-08-14C's "Q-65 — Unaffected: the 2026-06-26 contempt/OSC ruling post-dates this docket" is questionable: the docket holds two antecedent judicial findings of media decorum violation, one with sanctions imposed, bearing directly on the June contempt matter.** → **Q-109.**

**Q2 — the Burt/Novak claim is accurate but draws the wrong lesson.** It is right that the PARTIES block omits them, but the moral offered was *"a party's representation is a moving fact."* **The same printout records their admission precisely** — pro hac vice motions 09-25-2025, orders admitting them signed 09-26 and 09-27, first appearance 09-29 (`Burt` = 17, `Novak` = 29 occurrences). **The real finding is structural: the XChange PARTIES block lists only counsel of record and omits pro hac vice counsel whose admission the same document records.**

---

## 4. ✅ CONFIRMED — fourteen claims that survived, logged deliberately

*Per the verify-in-both-directions rule these are findings, not non-events. **Fourteen of twenty-six survived intact.***

| | claim | measurement |
|---|---|---|
| C1 | No contempt **proceeding** before 2026-03-14 | `contempt` = 9, all opened, all boilerplate — **the count was exactly right** *(see Q1 for scope)* |
| C2 | No bullet-fragment matter in the period | `bullet` = 0, `fragment` = 0, `ballistic` = 0, both files |
| C3 | No docket entry dated 2026-02-13 | 0 in **both** date formats ⚠️ *the short history uses long-form dates — a numeral-only search would have been a false null* |
| C4 | "161" nowhere in the register | 0 in both. **D-69 / Q-95 stand** |
| C5 | Coverage ceiling 2026-03-14 | all 506 entry dates parsed; max = 2026-03-14 |
| C6 | 31 pp. / 13 pp. | `Page N of` markers: 31 and 13 |
| C7 | The Q-66 notice, 02-02-2026, in both printouts | 1 in each, both 02-02-2026 — *"independently confirmed in both"* is exact |
| C8 | The title correction — not *"Notice re Media Access"* | that string = 0 in both |
| C9 | Docs. 525, 570, 625, 631, 678 unresolvable here | all five = 0, both files |
| C10 | Sturgill in no minute entry | 0 in both |
| C11 | Dyer / Nyman / Neiman / Moss absent | all 0, both files |
| C12 | Skordas — a single 2025-09-16 entry | 2 occurrences, both inside one minute entry |
| C13 | `judd` = 4 full / 0 short | ✅ **including "0 *(a true null)*" for the short history** |
| C14 | All four banked SHA-256s | match byte-for-byte |

✅ **A methodological confirmation worth logging:** CR-E12 states *"Every [X] row here was read in Python, not grepped,"* and its N-1 null re-ran clean. **The post-discovery remediation is working** — the surviving defects are concentrated in files written **before** hazard 13 was found, plus one propagated wording error.

---

## 5. The docket, computed rather than assumed

| | full history | short history |
|---|---|---|
| **Docket entries** | **506** *(authoritative)* | 505 date-leading rows |
| **Date range** | **2025-09-15 → 2026-03-14** | same |
| **Distinct entry dates** | 113 | — |
| **Generated** | 2026-03-15 03:18 | 2026-03-15 03:21 |
| **Date format** | `MM-DD-YYYY` | ⚠️ **`Month D, YYYY`** |

**Entries per month:** 2025-09 **80** · 10 **97** · 11 **55** · 12 **75** · 2026-01 **94** · 02 **66** · 03 **39**.

**Two facts worth surfacing:**
- 🚨 **The earliest entry is 2025-09-15 — one day BEFORE the Information.** It is an order for electronic media coverage. **Media-access litigation predates the charging document**, and the library's framing *"case filing → 2026-03-14"* understates the start.
- ✅ **The printout carries forward-scheduled dates `04/17/2026` and `05/18–05/22/2026`** — **independent corroboration of CR-E14's F-84 chain** from a different source. `bind over` / `bound over` = **0** in both files.

**Classification markers:** `**** PRIVATE ****` **28** · `**** SEALED ****` **3**. *(CR-E12's third state, `PROTECTED`, does not appear as a marker in these two files — a scope note, not a contradiction.)*

⚠️ **PII: the full history's `DEFENDANT INFORMATION` block contains a date of birth and an offense-tracking number. Location flagged; contents not reproduced.**

---

## 6. Residual scope — and the largest piece of unfinished work

🚨 **The other 48 affected files were characterised but their nulls were NOT re-run.** The same silent-skip hazard applies to every null ever taken from them — including the **Information**, the **PC affidavit**, the **disqualification motion**, the **State's opposition** and the **663-NUL federal extraction**. ⚠️ **One scope claim is already void:** a pass asserted *"Searched all `.txt` files in the artifacts folder"* — run against a folder where **50 of 59 silently fail.** → **Q-105.**

**Also not done:** the PDFs were not read — **if the extractor dropped or garbled text at page boundaries, a null could be false in the PDF even where the `.txt` confirms it. Not tested.** Recommended: re-extract all 50 with `pdftotext` and diff ⚠️ **the SHA-256s will change, so log the supersession on both ends.** XChange provenance remains unconfirmed (Q-31). The third XChange artifact (the case-search printout, 2 NULs — also affected) was not audited, nor its F-41 four-row claim. **No docket number was verified against a court source:** R1 establishes the four numbers are **present and usable**, not that each is correctly attributed.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-81 executed.** 26 claims tested: **14 CONFIRMED, 8 REFUTED, 2 QUALIFIED.** 🚨 **Standing hazard 13 corrected and widened the same day it was written — 50 files not two, and `file(1)` is not a valid detector; the correct predicate is `NUL count > 0`.** Root cause isolated to a `0x00`-for-`0x0C` page-separator defect plus a `ugrep -I` wrapper that skips binary files silently. **R1 corrected at six sites across five files; R2 at five sites; R7 and R8 in place.** Q-105, Q-109 raised; hazards 14 and 15 added from the parallel Q-61 tranche. **Integrity confirmed: banked hashes match; the NULs were present at acquisition.** |
