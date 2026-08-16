# CR-REVIEW-2026-08-16D — Q-105: re-running every null recorded under a broken tool

**Scope:** execution of **Q-105** — the remediation of standing hazard 13 across all 50 affected artifacts, and the re-running of every null previously recorded against them by three independent readers. **~70 nulls and counts re-tested. The load-bearing null HELD. The worst defect found was not a null at all.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

**Register:** no entry assigned, resolved or moved. **No case-posture statement altered. Tyler Robinson has NOT been bound over; the presumption of innocence applies. All allegations are attributed, never adopted.**

---

## 1. Why this ran, and what turned out to be wrong with the hazard itself

Standing hazard 13 was written on the morning of 2026-08-16: `grep` returns nothing on the two XChange docket printouts. **By the end of the day it had been corrected three times, and the third correction invalidated the remedy it had prescribed.**

| | as first written | as established |
|---|---|---|
| **Scope** | 2 files | **50 files** — every `.txt` in the artifacts folder but nine |
| **Detector** | `file(1)` reports `data` | 🚨 **invalid** — `file` tolerates a single trailing NUL, so two affected files read as clean text. **Use `NUL count > 0`** |
| **Remedy** | read in Python, normalise whitespace | 🚨 **insufficient** — `\x00` is **not whitespace to `\s`**. **953 NULs sat adjacent to non-space characters and ALL 50 files carried NULs surviving normalisation**, so phrases spanning a page break returned false nulls **in Python too** |

⚠️ **Every reader dispatched on 2026-08-16 was given the insufficient method.** That is why this re-run exists.

**Root cause, isolated:** the PDF→text extractor emitted `0x00` where `0x0C` (form feed) belonged at page breaks, **and** the harness `grep` is `ugrep -I`, which skips binary files with no output and exit 0. `/usr/bin/grep` answers correctly — **the wrapper is what silenced them.**

## 2. The remediation, and why substitution rather than re-extraction

**1,189 NULs across 50 files replaced with `0x0C`.**

| verification | result |
|---|---|
| `grep -ci judd` on the full history | **4** — matches Python for the first time |
| files classified `data` | **0** |
| NULs remaining in any `.txt` | **0** |
| content identical modulo the separator, vs `git HEAD` | **50 of 50 — zero content changed** |
| form feeds vs `pdfinfo` page counts | match on every file spot-checked |

⚠️ **Substitution was a judgement, not a necessity, and is recorded as one.** `pdftotext` was tested on five affected documents and returns ~equivalent text, so re-extraction was available. **It was rejected because re-extraction produces DIFFERENT text**, and CR-ACQ-2026-08-16 §6.2 had already measured that two extractions of one PDF differ in ways that produce false nulls — **it would have invalidated every verification act already performed.** The substitution was unambiguously safe because **zero affected files contained any pre-existing `0x0C`**.

**Artifacts:** `docket-artifacts_2026-08-16_NUL-repair.py` (with its invariants) and `..._SUPERSESSION.json` (old and new SHA-256 for all 50).

---

## 3. ✅ The load-bearing null HELD

**CR-E13 §8 N-1** — *no reference to the FBI, the ATF, or any federal agency in the eight preservation-chain documents* — supports the qualification that the evidence-preservation order **names no federal agency**, which governs how it can be applied to the September 2025 consumptive testing. **If it were false, a headline qualification would be wrong.**

✅ **CONFIRMED, by a stronger method than the one recorded:** a **23-pattern stem battery** (adding `federa`, `quantico`, `beltsville`, `crime lab`, `SBI`, `DPS`, `laborator`, `NIBIN`, `CODIS`, `JTTF`, `marshal`, `DEA`, `homeland` and more) **plus a pattern-independent ENTITY CENSUS** — all-caps acronyms, capitalised multi-word runs, and an organisation-suffix scan — which enumerates every organisation regardless of whether its name was anticipated.

**The complete list of every organisation named in the eight documents:** the Utah County Attorney's Office; three defence firms; the Fourth Judicial District Court; and generic classes only (*"any law enforcement agency involved in the investigation of this case,"* *"prosecuting agency,"* *"an evidence collecting or retaining entity"*). **No law enforcement agency of any kind — federal, state or local — is named.** The single `United States` hit is a constitutional citation.

⚠️ **Its honest scope caveat is preserved unchanged:** these eight documents only; **the search space would not necessarily contain such a reference**; docket #107, the 2025-11-03 stipulated motion and the entered discovery order are unheld. **This remains absence of evidence with a narrow scope, not evidence of absence.**

**Three other high-stakes items also held:**

- 🚨 **CR-E08's `circumstance` = 1 — CONFIRMED TWICE, on two independent extraction tools**, on a file that had carried 10 NULs, **and against a battery built specifically to find a second aggravator written differently** (`aggravat*` = 8, all opened; every roman-numeral designator enumerated — `(iii)` occurs once and only in Count 1). **This closes the single largest exposure the NUL discovery created: F-23 stands at High.**
- **CR-E08 F-25's affidavit-DNA null** — confirmed and widened: zero on `\bDNA\b`, zero on the bare `/dna/i` substring (**the *kidnaped* trap affirmatively clean**), and zero on eight further forensic-vocabulary patterns never previously run.
- **CR-E09 F-29's bullet/jacket/fragment null** — confirmed and widened to `ballistic`, `projectil`, `slug`, `casing`: **49 cells, all zero**, against a comparator document returning 145 hits.

**Across all three readers: ~55 nulls CONFIRMED, several on batteries widened well beyond the originals.** Logged deliberately — an audit trail that only ever finds errors is itself a bias signal.

---

## 4. 🚨 The worst defect was not a null battery

**CR-E12 §6.1 listed the 2025-10-24 hearing as *structurally unobtainable* — while this library has held a 97-page Tier 1 redacted transcript of it since 2026-07-27.**

`oct24_clean.txt`, 176,171 characters, captioned *"REDACTED TRANSCRIPT OF: SEALED MOTION HEARING BEFORE THE HONORABLE TONY GRAF … OCTOBER 24, 2025"*, reported by a certified court reporter, banked and SHA-256-verified, summarised at CR-ACQ-2026-07-27 §4 — **and cited by no evidence file in the library.** *(Verified directly by the orchestrator before any correction was made.)*

🚨 **Root cause, and it is the most transferable finding of the day: a docket-derived observation was promoted into a claim about this library's HOLDINGS.** The docket is evidence of what the court **filed and classified**. It is **not** evidence of what this project **possesses**. **Two other nulls in the same file failed the same way** (N-6, N-4). **A completeness pass against the artifacts folder would have caught all three; a pass against the docket never could.** → **Q-110.**

**It already pays out:** on 2025-10-24 the court stated that *"these hearings, unless there is mention of it needing to be a closed hearing, **the assumption is they will be open hearings** unless the parties bring compelling reasons to close them,"* and defence counsel proposed *"just have everybody leave and **seal like a portion of the hearing**."* ⚠️ **F-63's origin dating for the witness-by-witness RULE survives — this is a precursor, not an instance — but the open-by-default presumption and sub-hearing granularity were on the record twelve weeks earlier than recorded.**

---

## 5. 🚨 A second extraction defect, needing the OPPOSITE remedy → standing hazard 16

**`U+FFFE` — a Unicode noncharacter used as a line-break soft hyphen — sits inside words in 15 files: 131 occurrences, 83 distinct split words, 43 existing only in split form.** It is not whitespace, so it survives normalisation exactly as the NULs did.

🚨 **Independent `pdftotext` re-extraction establishes that at every position the PDF holds a HYPHEN followed by a line break. The banked extractor destroyed the hyphen.** ⚠️ **So `Pre-Trial`, `Pre Trial` and `PreTrial` all miss — a three-way false null.**

**A demonstrated corruption of an evidence file, not a hypothetical:**

| document | search | as banked | true |
|---|---|---|---|
| **Motion to Preserve Evidence** | `77-11c-302` | **0** | **1** |
| Information | `low-crawling` | **0** | 1 |
| State's disqualification opposition | `Opposing` | **0** | 1 |
| XChange full history | `Pre-Trial` | 7 | **8** |
| State's Response | `77-11c-401(3)(a)` | 3 | **5** |

🚨 **The first row corrupted CR-E13.** The motion cites **four statutes in sequence — §§ 77-11c-301, -302, -303, -401** — and **CR-E13 v1.0's citation list omitted -302**, because a plain search for it returns zero. **The omission of one item from a sequence was visible only by reading, never by searching.** Corrected at CR-E13 v1.1. ⚠️ **And the missing `Pre-Trial` row is the motion to amend the very publicity order CR-E10 F-31 is about.**

✅ **It must NOT be repaired in the data.** Hazard 13's fix was safe because `0x0C` was unambiguously correct. **Here the expansion differs per word** — `addi￾tional` → *"additional"* (join) but `death￾penalty` → *"death-penalty"* (hyphen) — **so no single substitution is right and mutating would corrupt the record.** ✅ **The remedy is the method: `./artifact_search.py` searches both readings and refuses to load a file whose NULs have reappeared.**

> **The transferable rule: repair the DATA only where the correct value is unambiguous; otherwise repair the METHOD and leave the evidence alone.**

---

## 6. Corrections applied in place

| file | correction |
|---|---|
| **CR-E12 → v1.1** | §6.1 (the held transcript); **N-6** (the preliminary hearing and June contempt matter are established **open** by held records the file already relies on; only the 2026-04-17 limb survives); **N-4** narrowed (`dkt413` **is** a held signed order recording two closure dispositions — the steelman that saves the null is that both requests were **oral**); §6.2 (`PROTECTED` appears twice and **the two printouts disagree about the same record**); F-68's char count; `(Dk. 23)`; pin-cite count |
| **CR-E13 → v1.1** | §3's *"or described"* limb narrowed (**no pattern battery can test it**, and it contradicted §7's own correct formulation); **N-6 refuted** (`dkt74` carries *"Approved March 13, 2025"* twice, and the null was self-contradicting on its face); D-69's parenthetical; F-79 narrowed to three DNA passages and its cross-reference fixed (N-2, not N-1); **§ 77-11c-302 added** |
| **CR-E14 → v1.1** | §1's stated method (insufficient — hazard 16); **N-3**'s basis (it attached *"Zero"* to a battery including `Dkt`/`Doc.`, which are **not** zero — contradicting this file's own F-95); **N-7**'s `competen` sentence (1 of 6, not all); **N-8**'s parenthetical |
| **CR-E10 → v1.4** | **F-34's letterhead count: NINE, not eight.** ⚠️ The substance of F-34-as-restated is unaffected, and the correction runs **in the same direction F-34 was withdrawn in** |
| **CR-REVIEW-2026-08-16B** | 🛠 **Two of my own figures corrected.** **R3**: the seven limited-appearance filings are **5 on 09-30, 1 on 10-13, 1 on 10-14** — not all on 09-30; the 10-14 row is the only one that names its attorney. **R8**: `Minute Entry` = 12 is the case-insensitive count; **there are 10 minute entries**, so the Sturgill null's denominator is 10 |
| **QUEUE Q-96** | the roster pass's *"the roster appears stable"* **refuted as an inference** — the literal null holds, but counsel were repeatedly **added**. ⚠️ **Absence of withdrawal is not stability.** ✅ The *"no second McBride"* null, previously **void**, is now **CONFIRMED** on 4,171 occurrences across three corpora. The AG gloss narrowed — **the Utah AG appears in four capacities**, including as the sworn officer's own agency field on the probable-cause affidavit |

---

## 7. Residual scope — stated plainly

🚨 **The re-runs covered the nulls of CR-E08, E09, E10, E11, E12, E13, E14, CR-ACQ-2026-08-14C and the counsel roster. They did NOT cover: DNA-E01, CR-E01–E07, CR-WATCH-log, or the four raw candidate banks.** Nulls in those files were recorded under the same broken condition and **remain untested**.

**Also not done:** the PDFs were not read page-by-page — **four of 57 were independently re-extracted**; the 08-16 warning that a null true in the `.txt` could be false in the PDF **remains untested for the other 53**. No docket number was verified against a court source. Nothing after the printouts' **2026-03-14** ceiling was tested, so every docket-derived null here is bounded there. `oct24_clean.txt` was not read in full, and **its bearing on CR-E10, CR-E11 and the publicity-order track is entirely unassessed** (Q-110). XChange provenance remains unconfirmed (Q-31).

**Living persons:** both charging documents print a street address and date of birth in their caption region; a subpoena and a minute order each print a date of birth; a restitution notice carries private claimants' details. **Locations flagged; none reproduced.** Attorney roles are reported as the documents state them, with **no adverse characterisation attached to any named person** — the McBride finding is a fact about a surname's distribution in a corpus and carries no implication about the attorney who bears it.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-105 executed: hazard 13 remediated across 50 files (1,189 NULs → `0x0C`, content verified unchanged against git on 50/50), and ~70 nulls re-run by three independent readers.** ✅ **The load-bearing null (CR-E13 N-1) HELD**, confirmed by stem battery *and* entity census; **CR-E08's `circumstance` = 1 held on two independent extraction tools**, closing the largest exposure the discovery created; **~55 nulls confirmed overall.** 🚨 **The worst defect was not a null: CR-E12 listed as structurally unobtainable a 97-page Tier 1 transcript the library has held since 2026-07-27 — root cause, a docket-derived observation stated as a claim about our holdings (→ Q-110).** 🚨 **Standing hazard 16 opened:** `U+FFFE` destroyed hyphens at line breaks, producing three-way false nulls — **demonstrated to have corrupted CR-E13's statute list** — and it must **not** be repaired in the data, because unlike the NULs its correct expansion is ambiguous per word. **`artifact_search.py` added as the method fix.** Corrections applied in place across six files, including two of this reviewer's own figures. |
