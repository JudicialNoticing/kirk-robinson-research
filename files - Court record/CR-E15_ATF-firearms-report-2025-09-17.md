# CR-E15 — The ATF firearms laboratory report of 2025-09-17, read directly

**File ID:** CR-E15 · **Scope:** the **ATF Forensic Science Laboratory report, case 2025-W-000401, dated 2025-09-17**, read **directly from the document** — not through a party's characterisation of it — together with the defence motion it is attached to. Executes **Q-101** and bears on **Q-35**. · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Revised:** 2026-08-30 · **Status:** **v1.1 — `[PROVISIONAL]`** *(v1.0 — 2026-08-16, Q-101 executed. v1.1 lands the `CR-E20 F-4` join: this report is, on the best available reading, **State's Exhibit 32** at the preliminary hearing — see **§4A `F-139`**, ⚠ **split-graded, anchor High / identity Medium-high**.)*

⚠️ **Findings `[PROVISIONAL]`.** No independent verification cycle has run → **Q-113**.

🚨 **CASE POSTURE: Tyler James Robinson has NOT been bound over for trial. The presumption of innocence applies throughout.** ⚠️ **This file records forensic findings that cut in more than one direction. It adopts none of them as proof of anything, and it is not an argument for or against any party.**

> ### 🚨 §0.0 · NAMING DISCIPLINE — READ THIS BEFORE CITING ANYTHING BELOW
> 🛠 *(ADDED v1.1, 2026-08-30. `CR-E20` — the canonical forensic exhibit map — governs; this block reproduces its rules, it does not restate its findings.)*
>
> **This file is about the ATF FIREARMS / TOOLMARK report, and it is therefore the file in this library most likely to be mis-cited against the wrong exhibit.** There are **four ATF reports on this record and they split two-and-two across disciplines** (`CR-E20 F-1`): DNA/biology on one side, firearms/toolmark on the other, across two evidence groups.
>
> 🚨 **STATE'S EXHIBIT 30 IS THE ATF *DNA* REPORT. IT IS A DIFFERENT DOCUMENT FROM THE ONE THIS FILE READ.** On the record: *"This is the ATF report that I received regarding **the DNA testing** on the gun and cartridge case and cartridges"* — Sgt. Faumuina, `day4.txt` **05:18:35**; the prosecutor, moving its admission: *"This Exhibit deals with **DNA testing** on the rifle and the cartridges"* (**05:19:09**). 🚨 **NOTHING IN THIS FILE MAY BE CITED TO STATE'S EXHIBIT 30** — not `F-96`, not `F-97`, not `F-98`, not `F-99`, not the exhibit list at §2, not the appendix definitions at §3. The consumption page, the seven likelihood-ratio calculations and the ATF item 1.x / 2.1 / 3.1 / 4.1 / 5.1 series belong to **Exhibit 30** and appear nowhere in this file.
>
> ⚠ **`CR-E20`'s writing rules apply to every future edit of this file:** never write *"the ATF report"* or *"the ATF firearm report"* bare; never write a bare *"Exhibit 30"* — **it has three referents** (`CR-E20 F-3`); write **number and discipline every time** — *"State's Exhibit 32 (the ATF firearms/toolmark report)."*
>
> ✅ **CHECKED, NOT ASSUMED — scoped null run 2026-08-30 (`N-6`).** ⚠️ **Scope is `CR-E15` AT v1.0**, before this block existed: `/Exhibit 30/` = **0 hits**, `/ATF firearm report/` = **0 hits**. **This file had never implied that its report is Exhibit 30, and nothing needed correcting on that head.** 🚨 **The null does NOT hold over v1.1 and is not asserted to** — this block names Exhibit 30 repeatedly, on purpose. 🛠 **Two bare *"ATF report"* usages at §6 were nevertheless disambiguated in place at v1.1** under rule 1 — see the revision log.

> ### ⚠️ §0.1 · PROVISIONAL DEPENDENCIES — LOOP §2 discipline
> ✅ **§1–§4 depend on no other provisional file.** The report was **read directly from the primary document** (rendered pages, not a text layer). The outbound correction at §4 is to **CR-E14 F-87**, which was itself explicitly recording-layer. **Clearing item: Q-113.**
> 🛠 🚨 **CHANGED AT v1.1 — §4A INTRODUCES THIS FILE'S FIRST PROVISIONAL DEPENDENCY, AND IT IS DECLARED RATHER THAN LEFT TO BE DISCOVERED.** **`CR-E20` is `[PROVISIONAL]`** (v1.0, 2026-08-30; no verification cycle has run on it). ⚠️ **What depends on it:** §0.0's exhibit-map framework, and the fact that **`F-139` executes `CR-E20 F-4`** rather than originating the join. ✅ **What does NOT depend on it:** **every item of evidence carrying `F-139` was re-verified directly this pass** against `day4.txt` and the rendered pages of the motion attachment — **none is imported from `CR-E20`**, and one of `CR-E20 F-4`'s locators is corrected at §4A. ⚠️ **Consequence under LOOP §2: `F-139` and `F-140` may not clear `CR-E20`, and `CR-E20` may not clear them.** **Two provisional files agreeing is not a verification act.**

---

## §0 · Sourcing framework (project standard)

**Tier 1** — sworn testimony and primary court filings/documents · **Tier 2** — named official statements · **Tier 3** — named journalistic reporting/analysis · **Tier 4** — anonymous-source or low-verification material.

**This report is Tier 1 and is held.** It is a **laboratory report of a federal forensic laboratory**, digitally signed by its examiner and two reviewers, filed as an exhibit to a court motion. ⚠️ **Tier 1 establishes what the laboratory concluded and in what terms. It does not make the conclusion true, and this file does not treat it as more than a laboratory's stated result.**

---

## §1 · 🚨 Access-path caveats — and how this sat unread for three weeks

| | |
|---|---|
| 🚨 **THE LIBRARY HAS HELD THIS SINCE 2026-07-27** | It is **Exhibit 2**, at **PDF pages 25–29**, of `CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.pdf` — banked in the project's **founding acquisition pass**. **Q-101 named it the library's highest-value acquisition target on 2026-08-16 while it was already on disk.** |
| 🚨 **WHY NOBODY SAW IT — A THIRD EXTRACTION DEFECT** | **The report's text layer is corrupted by a broken font encoding.** `pdftotext` renders pages 26–29 as mojibake — *"$%ÿ'%ÿ()*+,-.)/-ÿ01ÿ234-56)"* for *"U. S. Department of Justice"*. ⚠️ **Every text search over the banked corpus therefore missed it**: `Mauser` = 0, `30-06` = 0, `casing` = 0, `unable to identify` = 0 in the `.txt`. **The document was fully present and completely invisible to the method.** |
| ✅ **How it was read** | **By rendering the PDF pages as images.** No text-layer search of any kind can reach this document. |
| **Provenance** | Three of three, and unusually strong: **ATF letterhead and laboratory address**, an **ANAB ISO/IEC 17025:2017 accreditation mark**, a **case and submission number**, and **three digital signatures with timestamps** (examiner 16:11:16, technical reviewer 16:23:17, administrative reviewer 16:30:32, all 2025-09-17, −04'00'). Filed as an exhibit to a signed, served defence motion. |
| ⚠️ **Restriction on its face** | Each page carries **"FOR OFFICIAL USE ONLY"** and a **"LAW ENFORCEMENT INFORMATION — Further dissemination to any unauthorized person or agency may result in both civil and criminal liability"** watermark. ⚠️ **It nonetheless entered the public court record as an exhibit to a public filing, and — per Tier 3 reporting — was the subject of an unsealing in April 2026.** This file records its content because it is in the public record; **the restriction is noted, not ignored.** |
| **The vehicle** | *"MOTION FOR AN ORDER PROHIBITING ANY FURTHER ALTERATION OR TESTING OF A BULLET JACKET FRAGMENT…"*, defence, **dated 9 January 2026**, 19 printed pp. / 29 PDF pp. 🚨 **This is the "bullet-fragment motion" the library has tracked as Q-35 — also held, also since 2026-07-27.** |

---

## §2 · What the report is

| field | value |
|---|---|
| Issuing body | **Bureau of Alcohol, Tobacco, Firearms and Explosives — Forensic Science Laboratory, Washington** (Ammendale Road, Beltsville, MD) |
| **Date of report** | **2025-09-17** |
| **Case number** | **2025-W-000401** · Submission(s): **1** · Reference: **25-24969** |
| Title on its face | **"Homicide of Charlie Kirk"** |
| Type of exam | **Firearms** |
| Addressed to | an ATF Special Agent, Salt Lake City |
| Authors | a **Firearm and Toolmark Examiner**, with a **technical reviewer** (also a Firearm and Toolmark Examiner) and an **administrative reviewer** (Chief, Firearms & Identification Section). ⚠️ *Named on the face and in the defence's 2026-03-27* Touhy *letters (CR-E14 R-5); recorded here in official capacity only, with no characterisation attached.* |
| Disclosed to defence | **2025-12-18** *(per the motion, p.5)* |

**Exhibits examined, as listed:** (1) one **Mauser, model 98, 30-06 Springfield calibre rifle, serial number 8863, with an optical accessory**; (2) one 30-06 Springfield calibre **cartridge case**; (3)–(5) three 30-06 Springfield calibre **cartridges**; (6) one **bullet jacket fragment and four lead fragments**, designated 6A through 6E.

---

## §3 · RESULTS — the report's own words, and both directions

**F-96 — 🚨 THE CARTRIDGE CASE IS A MATCH, AT THE HIGHEST CONFIDENCE IN THE ATF'S OWN TAXONOMY. Confidence: High as to what the report concludes.**

> *"The Exhibit 2 cartridge case was identified as having been fired in the Exhibit 1 rifle. **[Source identification]**"*

The report's own appendix defines **source identification** as the examiner's conclusion that two toolmarks **originated from the same source** — the strongest of its three conclusions. The rifle was **test fired and found to be in operable condition**.

**F-97 — 🚨 THE BULLET JACKET FRAGMENT IS INCONCLUSIVE — WHICH IS NEITHER A MATCH NOR AN EXCLUSION. Confidence: High as to what the report concludes.**

> *"The Exhibit 6A bullet jacket fragment **could not be identified or excluded** as having been fired from the Exhibit 1 rifle based on an **agreement of all discernible class characteristics** and **neither sufficient agreement nor sufficient disagreement of individual characteristics**. The result of the comparison was inconclusive. **[Inconclusive]**"*

And the report's **own appendix** defines the term:

> **'Inconclusive'** — *"all observed class characteristics are in agreement but there is insufficient quality and/or quantity of corresponding individual characteristics such that the examiner is unable to identify or exclude."*

⚠️ **Two further limbs must travel with it or the finding is misstated:**
- *"Firearms that produce general rifling characteristics similar to those observed on the Exhibit 6A bullet jacket fragment include **numerous makes and models**."*
- *"The Exhibit 6B through 6E **lead fragments are not suitable for microscopic comparison**."*

**F-98 — Rotary-tool scribe marks were found on the cartridge case and the unfired cartridges. Confidence: High as to what the report states.**

> Toolmarks located on the exterior of the Exhibit 2 cartridge case and Exhibit 3 cartridges *"(scribe marks) that are consistent with being produced by engraving and/or rotary cutting tips commonly found installed in handheld rotary tools (such as a **Dremel tool**). These toolmarks **contain marks of value for comparison if a suspect tool is located**."*

⚠️ **"Consistent with" is a class-level statement, not an identification**, and the report expressly frames a comparison as **contingent on a suspect tool being located**. This bears on the library's existing Dremel thread and **must not be read as linking any particular tool**.

**F-99 — The report states its own methodological frame. Confidence: High.** Conclusions *"conform with the relevant Department of Justice policy on Uniform Language for Testimony and Reports."* Techniques: **microscopic comparison, visual/physical examination, and product (make/model) determination.** The report expressly limits itself: *"The following results only apply to the items tested."*

---

## §4 · 🚨 What this does to CR-E14's F-87 — the library's caution was right, and the picture is bigger

**CR-E14 F-87** recorded the defence's assertion that *"an ATF summary report indicates ATF was unable to identify the bullet recovered at autopsy to the rifle allegedly tied to Mr. Robinson,"* held it strictly in the **recording layer**, and gave **four reasons it could not be promoted**. ✅ **Reading the report vindicates all four — and the third exactly.**

**F-100 — The defence's characterisation is ACCURATE AS FAR AS IT GOES AND MATERIALLY INCOMPLETE. Confidence: High.**

| | |
|---|---|
| ✅ **Accurate** | The ATF did not identify the bullet jacket fragment to the rifle. |
| 🚨 **Incomplete — the same report, same page, identifies the CARTRIDGE CASE to the rifle at "[Source identification]"** | A reader given only the defence's sentence would not know a match exists in the very report being described. |
| 🚨 **Incomplete — "unable to identify" is not the report's own term.** The report says **"could not be identified OR EXCLUDED"** and designates the result **"[Inconclusive]"**, a term it defines in its own appendix | ⚠️ **"Inconclusive" carries an affirmative element the shorter phrasing loses: ALL observed class characteristics were IN AGREEMENT.** |
| ⚠️ **Incomplete — the class-characteristic agreement is compatible with "numerous makes and models"** | So the agreement is **not** itself probative of this rifle. **Both halves must travel together.** |

🚨 **THE OPERATIVE RULE FOR THIS LIBRARY, STATED PLAINLY: no file may say the bullet was "not matched to the rifle" without saying in the same breath that the result was INCONCLUSIVE — neither identification nor exclusion — and that the cartridge case WAS identified to the rifle.** To state the first without the second two is to reproduce a party's framing as a finding. **That is the cardinal error of this project.**

⚠️ **And the converse is equally barred:** the casing identification does **not** establish that this rifle fired the fatal bullet. **The report does not say so, and its own limiting sentence — *"the following results only apply to the items tested"* — forecloses the inference.**

**F-101 — This is the third instance in one day of the same failure, and the pattern is now the finding. Confidence: High.** The library held (a) `oct24_clean.txt`, a 97-page Tier 1 transcript of a hearing CR-E12 called *"structurally unobtainable"*; (b) this ATF report, named the same day as the **highest-value acquisition target** while sitting on disk; and (c) the **bullet-fragment motion** (Q-35). **All three were acquired in the founding pass of 2026-07-27 and never cited by an evidence file.** ⚠️ **In this case a fourth factor hid it: an extraction defect made the document unreachable by every search the library runs.** → **Q-110** is not housekeeping; it is the highest-yield item open. 🛠 *(v1.1, 2026-08-30: **`F-101` is EXTENDED, not superseded.** A fourth instance of the same class — and a distinct sub-shape of it — was found on 2026-08-30 and is stated separately at **§4A `F-140`**: not a held document nobody cited, but **two held halves in different folders that nobody joined**. `F-101`'s three instances and its Q-110 pointer stand unchanged.)*

---

## §4A · 🚨 THE JOIN: this report is State's Exhibit 32 at the preliminary hearing

🛠 *(ADDED v1.1, 2026-08-30.)* **`CR-E20` — the canonical forensic exhibit map — is the authority for this section.** Its **`CR-E20 F-4`** states the join; this section executes it on the `CR-E15` end, with the evidence re-verified here rather than imported.

> ⚠️ **WHY THIS SECTION EXISTS AT ALL.** This file read the ATF firearms report at Tier 1 on 2026-08-16 and **named State's Exhibit 32 nowhere.** *(Scoped null, re-run independently 2026-08-30: `/Exhibit 32/` over this file at v1.0 = **0 hits** — see §5 `N-5`.)* **The library therefore held the best-read version of this report and the hearing's designator for it in two files that did not know about each other.**

**`F-139` — THE ATF FIREARMS REPORT THIS FILE READ AT TIER 1 FROM A COURT FILING IS THE SAME DOCUMENT AS STATE'S EXHIBIT 32, IDENTIFIED, ADMITTED AND EXAMINED ON DAY 4 OF THE PRELIMINARY HEARING. ⚠️ SPLIT GRADE — ANCHOR: High · IDENTITY: Medium-high, AND IT IS AN INFERENCE, NOT A FINDING OF IDENTITY.** 🚨 **Any summary of this finding must carry the split as a split.** *(Grade held at `CR-E20 F-4`'s level — see `F-139(c)` for why it is not raised here even though this pass strengthened it.)*

### `F-139(a)` · The anchor — the record, verbatim and located

All locators are `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day4.txt`, read directly this pass. ⚠️ **Uncertified Rev machine transcript**; speaker attributions inferred from content, never from labels (`CR-E16`).

| `day4.txt` | Verbatim | Corresponds to |
|---|---|---|
| **05:26:25** | *"This is an ATF report that I received in relation to the gun as well as cartridge case and cartridges."* — Sgt. Faumuina | The document at §2: an ATF **firearms** exam on a rifle, one cartridge case and three cartridges |
| **05:27:06** | *"As it relates to **State's Exhibit 32**, is accepted into evidence and may be published in the gallery as well as electronic, the media camera can capture it."* — the court | **Admission.** Published at all three levels |
| **05:28:32** | *"The Exhibit 1 rifle was test fired and found to be in operable condition. The test fires were designated as Exhibit 1.11."* | **This file's `F-96`**, which records the same sentence's content from the document |
| **05:29:01** | *"The Exhibit 2 cartridge case was identified as having been fired in the Exhibit 1 rifle."* | **This file's `F-96`** — the `[Source identification]` |
| **05:29:53 → 05:30:22** | the toolmark paragraph, read across a page break: *"Tool marks were located on the exterior of the Exhibit 2 cartridge case and Exhibit 3 cartridges," in parentheses, "(inscribed marks)…"* → *"Installed in handheld rotary tools such as a Dremel tool. These tool marks contain marks of value for comparison if a suspect tool is located."* | **This file's `F-98`** |
| **05:31:18** | *"The Exhibit 6 bullet jacket fragment cannot be identified or excluded as having been fired from the Exhibit 1 rifle … The results of the comparison was inconclusive."* | **This file's `F-97`** |
| **05:31:54** | *"The Exhibit 6B through 6E lead fragments are not suitable for microscopic comparison."* | **`F-97`'s second limb — verbatim, word for word** |
| **05:27:20** | the court: *"And I note that this has been previously disclosed publicly from an earlier filing, I believe from either late last year or early this year."* | **The motion this file read is dated 9 January 2026** — inside the court's window |
| **05:26:42 → 05:26:50** | the court: *"So question for you, was this the report that was previously disclosed in one of the early motions?"* — Mr. McBride: *"Yes."* | ⚠️ **Counsel's representation on the record, NOT sworn testimony, and it does not name which motion** |

⚠️ **TWO DESIGNATORS ON THE DOCUMENT WERE NEVER READ ALOUD.** Neither **`[Source identification]`** nor **`[Inconclusive]`** appears in the transcript of the reading; they are on the page this file rendered. **`F-96` and `F-97` therefore do not rest on the transcript and are not weakened by it.**

🛠 **LOCATOR CORRECTION, made rather than carried.** `CR-E20 F-4` places the source-identification reading at *"roughly `day4.txt` 05:29:5x."* **It is at 05:29:01.** **05:29:53 is the toolmark paragraph — this file's `F-98`, not `F-96`.** *(Correction stated here because this file is the one that must be right about its own findings' locators; the matching repair on the `CR-E20` end is owed and is NOT made by this pass.)*

### `F-139(b)` · Four verification acts run by this project on 2026-08-30

**None of these is imported from `CR-E20`. Each was run directly against `day4.txt` and against the rendered pages of the motion attachment.**

**(1) The report's author authenticated State's Exhibit 32 under oath as her own report.** Later the same day, the ATF firearms/toolmark examiner — **the same person the report's signature block names as examiner** *(§7; recorded in official capacity only)* — was shown the exhibit:

> *"Do you recognize Plaintiff's Exhibit number 32?"* — *"I do, yes."* *"**Are you the author of this report?**"* — *"**I am, yes.**"* (**06:25:38 → 06:25:44**) · *"And are your conclusions accurately documented in your report?"* — *"Yes."* (**06:26:21 → 06:26:32**)

**Confidence: High.** ⚠️ **This authenticates the exhibit as her report. It does not compare the exhibit against the motion attachment — she was never asked to.**

**(2) The exhibit's page-and-paragraph layout, as navigated in open court, matches the motion attachment exactly.** Counsel's display instructions are a layout test, and **nine of them land on the rendered pages precisely**:

| `day4.txt` | Instruction, verbatim | What sits there in the motion attachment |
|---|---|---|
| **05:28:16** | *"The lab numbers and agency numbers are listed here on the first page, right?"* | p. 1 header block: Case Number **2025-W-000401**, Reference **25-24969**; column heads **"Lab # – Agency #"** |
| **05:28:21** | *"scroll down to the bottom of Page 1 … read the **second line** under Results of Examination"* | The **second** line under **RESULTS OF EXAMINATION** is the test-fire sentence *(the first is the report's limiting sentence)* |
| **05:28:52** | *"if you'll **skip the next line** and then go to the Exhibit 2 cartridge case"* | The skipped line is *"Exhibit 2 consists of one (1) 30-06 Springfield caliber fired cartridge case bearing a Remington headstamp"*; **the line after it is the source-identification sentence** |
| **05:29:07** | *"jump back up to the **top where it lists the exhibits**. 2 through 5"* | The **EXHIBITS** list heads p. 1; items 2–5 are the cartridge case and the three cartridges |
| **05:29:42** | *"read the **last paragraph on this page**"* | p. 1's last paragraph is the toolmark paragraph — **and it breaks mid-sentence at "commonly found"** |
| **05:30:14 → 05:30:22** | *"Scroll down, please"* → *"Installed in handheld rotary tools…"* | **p. 2 line 1** is the continuation *"installed in handheld rotary tools (such as a Dremel tool)…"* |
| **05:30:54** | *"Going back to **Page 2** … the **first FULL paragraph** there beginning with 'Exhibit 6'"* | p. 2's first paragraph is that straddling continuation; **its first *full* paragraph is *"Exhibit 6 consists of…"*** |
| **05:31:45** | *"the line starting with 'The Exhibit 6B through 6E'"* | That line sits **two paragraphs below** — past the *"numerous makes and models"* paragraph, **which was never read aloud** |
| **06:26:34** | *"Could you turn to **page two** of the report? **Second, bottom of the page, those two paragraphs**"* → the DOJ Uniform Language question | p. 2's **last two paragraphs** are exactly the DOJ-policy sentence and the techniques sentence — **this file's `F-99`** |

**Confidence: High.** 🚨 **The page break, the line order, the skipped line and the straddling paragraph are not content anyone could infer from a summary. They are structure, and the structure matches.**

**(3) The appendix is where the attachment puts it — page 4 of 4.** On cross (**07:10:31**) counsel returned to *"the report, the State 32"* and to *"the second page"*, quoting the Exhibit 6A paragraph; then at **07:11:34**: *"And on the next page, if you could **go to two pages in**, you have an **appendix**, do you not, where you explain what inconclusive means? **Next page. One more. There we go.**"* — **two pages on from p. 2 is p. 4, and p. 4 of the motion attachment is the APPENDIX**, headed *Source identification / Source exclusion / Inconclusive*. Counsel then read its inconclusive definition back, and the witness answered *"my conclusion is inconclusive **just as it says in the appendix**"* (**07:12:36**). **Confidence: High.** ✅ **This is the definitional material this file's `F-97` and `F-98` rely on** — it is in the exhibit, at the page the attachment puts it.

**(4) The submission number matches.** *"For the **submission one** report, I received a firearm, cartridge case, three cartridges, one bullet jacket fragment, and four lead fragments"* (**06:25:53**) — the attachment's face reads **Submission(s): 1** and lists exactly those six exhibits (§2). **Confidence: High.** ⚠️ **This also bounds the finding: `F-139` is about the SUBMISSION-1 firearms report.** The witness's phrasing implies at least one further submission exists, and the *Touhy* request records **three** ATF firearms reports (`CR-E14`; `CR-E20` §6.5). **No later ATF firearms report is held, and none is identified with Exhibit 32.**

### `F-139(c)` · Why it remains an inference — the limbs, separately

`CR-E20 F-4` states three things as unestablished — complete, unredacted, paginated identically — and adds that no witness was asked. **This pass moved two of the three and narrowed the fourth clause, and must say so rather than repeat a caveat it has overtaken** *(a caveat is a claim — it needs a verification act like any other)*:

| Limb | Status after this pass |
|---|---|
| **Paginated identically** | ✅ **NO LONGER OPEN — supported directly, at High**, by `F-139(b)(2)` and `(3)`: nine independent navigation instructions land on the attachment's own page and paragraph structure, including a mid-sentence page break and an appendix two pages on from p. 2 |
| **Complete** | ⚠️ **Substantially supported, not closed — Medium-high.** The attachment's footers read **"Page 1 of 4" … "Page 4 of 4"**, and the exhibit as displayed was navigated on pp. 1, 2 and 4 with p. 3 passed through on screen. **Nothing on the record states the exhibit's page count** |
| **Unredacted** | 🚨 **UNTESTED. Unverified.** No question on this record addresses whether the exhibit copy carries redactions. *(Scoped null, run this pass: all **15** `/redact/i` hits in `day4.txt` fall in the morning colloquy and testimony about the **Twiggs recorded statement and its transcript** (lines 347–1535). **None concerns a laboratory-report exhibit and none falls in any of the three Exhibit-32 blocks.** ⚠️ **This establishes only that the question was never raised — not that no redaction exists.**)* |
| **No witness was asked** | ⚠️ **TRUE OF THE IDENTITY QUESTION, and only of it.** A witness **was** asked whether she authored the exhibit and whether her conclusions are accurately documented in it — and answered yes (`F-139(b)(1)`). **No witness was asked whether State's Exhibit 32 is the document attached to the 9 January 2026 defence motion.** *(Scoped null, run this pass: across all three Exhibit-32 blocks — `day4.txt` 05:26:18–05:32:02, 06:25:27–06:27:07, 07:10:29–07:12:54 — the only references to the prior disclosure are the court's question to COUNSEL at 05:26:42 and the court's own remark at 05:27:20. Neither is a witness answer.)* |

🚨 **THE GRADE IS DELIBERATELY HELD AT MEDIUM-HIGH AND IS NOT RAISED HERE**, for three reasons stated so the restraint is auditable: **(a)** the decisive artifact — **State's Exhibit 32 as admitted** — is **not held**, and every act above compares the record's *description* of the exhibit against the attachment, never the two documents; **(b)** the unredaction limb is untested and the identity question was never put to a witness; **(c)** **`CR-E20` is the canonical map and `CR-E20 F-4` is its finding — a `[PROVISIONAL]` file does not out-grade the map that governs it.** ✅ **A re-grade is now available on this evidence and is `CR-E20`'s to make, not this file's.**

**What would change it:** **State's Exhibit 32 as admitted, compared page-for-page against the motion attachment.** Failing that, a witness or a filing stating the two are the same document.

### `F-139(d)` · Divergences recorded rather than smoothed

**Verifying in both directions means logging what does *not* line up.** Four points where the transcript and the document differ:

- **05:29:53** renders *"(inscribed marks)"* and *"engravings and/or rotary cutting tips"*; the document reads **"(scribe marks)"** and **"engraving and/or"**.
- **05:31:18** renders *"The **Exhibit 6** bullet jacket fragment **cannot** be identified"* and *"The **results** of the comparison **was** inconclusive"*; the document reads **"Exhibit 6A"**, **"could not be identified"**, **"The result of the comparison was inconclusive."**
- **07:11:34** renders *"a microscopic **similarity** that is insufficient to form the conclusion of source exclusion"*; the appendix reads **"microscopic dissimilarity"** — and counsel's very next question says *"dissimilarity,"* so the divergence is the rendering's, not counsel's.
- **07:10:31** renders *"fired from the **Exhibit 1A**"*; the document reads **"the Exhibit 1 rifle."**

✅ **These cut FOR the join, not against it.** Every one is a Rev rendering of speech — a witness reading aloud or counsel paraphrasing — and **`CR-E18 F-138`'s standing limit governs: a divergence from an uncertified rendering is not evidence that two documents differ.** ⚠️ **And they establish the direction of value: at each point the document this file rendered is the better text.**

### `F-139(e)` · 🚨 THE CONSEQUENCE — available, stated, and EXPRESSLY NOT TAKEN

**IF the identity holds, then:**
1. **State's Exhibit 32 is the ONE forensic exhibit in this case whose contents this library has actually read.** `CR-E20` §1 records that **not one** of the hearing's forensic exhibits has been read by this library; **this file is its sole candidate exception.**
2. **`F-96`, `F-97` and `F-98` may be read as findings about a HEARING EXHIBIT rather than only about a motion attachment** — and `F-99` with them, since its DOJ-policy and techniques sentences are the two paragraphs put to the author at **06:26:34**.
3. **The library holds materially more of this exhibit than the hearing record conveys**: the two bracketed designators, the *"numerous makes and models"* paragraph *(never read aloud)*, the **disposition-of-evidence statement on p. 3** *(held in the document, and — flagged here — **not recorded anywhere in this file**)*, and the **full appendix**, of which only the inconclusive definition was put to the witness.

🚨 **THAT PROMOTION IS NOT PERFORMED. NOT HERE, NOT ANYWHERE, UNTIL THE DECISIVE ARTIFACT IS COMPARED.** **Every finding in §3 and §4 stands exactly as it stood at v1.0 — as findings about a document read from a court filing.** ⚠️ **No finding's grade is raised, no finding's scope is widened, and no other file is edited by this pass.** **Recorded as available-and-not-taken so that the option is visible and the restraint is auditable.**

**`F-140` — A CROSS-FOLDER JOIN FAILURE: BOTH HALVES WERE ON DISK, IN DIFFERENT FOLDERS, SINCE 2026-07-27, AND NO FILE JOINED THEM. THIS IS THE SECOND INSTANCE OF THIS EXACT SHAPE FOUND ON 2026-08-30. Confidence: High.**

- **First instance, same day: `DNA-E01 F-14`** — ATF sub-item **1.11** is the laboratory's own **test fires**, not a DNA swab, which is why it appears on neither consumption list. **The answer was the test-fire sentence of State's Exhibit 32** — banked in `files - Court record/` since the founding acquisition pass and read at Tier 1 **in this file** — while the sub-item series lived in `files - DNA evidence/`. Both halves held; nobody joined them.
- **Second instance, this finding:** the **document** was read at Tier 1 here on 2026-08-16 from `CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.pdf`; the **hearing designator for the same document** sat in `day4.txt`, in the **same acquisition folder**, banked the same day. **This file named Exhibit 32 nowhere; `day4.txt` was never read against this file.**

⚠️ **THE CLASS IS DISTINCT FROM `F-101`'s AND THAT IS WHY IT GETS ITS OWN NUMBER.** `F-101` is about **held documents nobody cited**. **`F-140` is about held documents that WERE cited, in separate files, which nobody read against each other** — and it is the harder failure, because **every individual file looks complete.** ✅ **Neither instance was a retrieval. Both were joins.**

⚠️ **AND THE SECOND-ORDER CAUSE IS NAMED IN `CR-E20 F-2`:** while the library called **State's Exhibit 30** *"the ATF firearm report,"* the natural name for **Exhibit 32**, the two reports were verbally indistinguishable — **which is precisely what made both joins invisible.** **The naming defect and the join failure are the same defect twice.** → §0.0.

⚠️ **What this does NOT establish:** how many further such joins are unmade. **This pass found one by being told where to look; it ran no systematic sweep**, and *"two instances"* is a count of what was found, **not of what exists.**

---

## §5 · Scoped nulls

- **N-1 — The report makes no statement about the shooter, the shooting, distance, trajectory or position.** It is a comparison report on six exhibits. Scope: all four pages, read as rendered images.
- **N-2 — The report does not mention DNA.** Scope: as above. *(A separate ATF DNA track exists — CR-E11, CR-E14 — and is not this report.)* 🛠 *(v1.1: **that separate track's hearing exhibit is State's Exhibit 30, the ATF DNA report** — §0.0, `CR-E20` §2. **N-2 is the reason this file could never have been about Exhibit 30.**)*
- **N-3 — No autopsy finding is stated here.** The bullet jacket fragment's provenance is not described in this report; **that it is "the bullet recovered at autopsy" is the defence's description, not the report's.** ⚠️ **Recorded because it matters: this file does not establish where Exhibit 6 came from.**
- **N-4 — The report states no conclusion about the three unfired cartridges' source**, only that toolmarks of comparison value are present on them.
- 🛠 **N-5 *(added v1.1, 2026-08-30)* — AT v1.0 THIS FILE NAMED STATE'S EXHIBIT 32 NOWHERE.** Scope: `/Exhibit 32/` over `CR-E15` v1.0, whole file, run independently on 2026-08-30 = **0 hits**. ⚠️ **This is a null about this project's own work, and it is the null that `F-139` and `F-140` exist to close.** *(`CR-E20 F-4` reports the same null from its own run.)*
- 🛠 **N-6 *(added v1.1, 2026-08-30)* — THIS FILE HAS NEVER IMPLIED THAT ITS REPORT IS STATE'S EXHIBIT 30.** Scope: `/Exhibit 30/` and `/ATF firearm report/` over `CR-E15` v1.0, whole file = **0 hits each**; the only `State's Exhibit` string in the file is **Exhibit 11**, the autopsy report, at §6 E-4. ⚠️ **Checked because §0.0 asserts it — a caveat is a claim.** 🛠 **Two bare *"ATF report"* usages (§6 'Resolved'; §6 roadmap E-3) were disambiguated in place at v1.1** under `CR-E20`'s writing rule 1; **neither was wrong, both were under-specified.**
- 🛠 **N-7 *(added v1.1, 2026-08-30)* — NO WITNESS WAS ASKED WHETHER STATE'S EXHIBIT 32 IS THE DOCUMENT ATTACHED TO THE 9 JANUARY 2026 DEFENCE MOTION.** Scope: all three Exhibit-32 blocks in `day4.txt` — **05:26:18–05:32:02**, **06:25:27–06:27:07**, **07:10:29–07:12:54**. The only references to the prior disclosure are **the court's question to counsel (05:26:42)** and **the court's own remark (05:27:20)**. ⚠️ **This is the null that keeps `F-139`'s identity limb an inference.** ⚠️ **It is not evidence of absence beyond that scope:** Days 1–3 and 5 were not searched for this question.

---

## §6 · Findings, resolutions and open items

**Resolved.** **Q-101 is EXECUTED** — the **ATF firearms/toolmark report, 2025-W-000401 of 2025-09-17** *(= **State's Exhibit 32** on the best available reading, `F-139` — ⚠️ **inference, Medium-high**; **NOT** State's Exhibit 30, which is the ATF **DNA** report — §0.0)* — is held and read directly. 🛠 *(v1.1: designator added; the earlier wording read "the ATF report," which `CR-E20`'s writing rule 1 bars.)* **Q-35's motion is also held.** The library no longer depends on any party's characterisation of this report.

**Not resolved.** Whether the fragment came from the autopsy (N-3). What the later FBI comparative and bullet-lead analyses concluded — **incomplete as of 2026-03-27** (CR-E14 §5). Whether any suspect rotary tool was located and compared (F-98). ⚠️ **The motion's own subject — that FBI testing may further alter the fragment — is a live dispute this file does not resolve.**

**Acquisition roadmap:**

| | Target | Why |
|---|---|---|
| **E-1** | The **FBI comparative bullet analysis and bullet-lead analysis** | Incomplete at 2026-03-27; would qualify F-97 directly |
| **E-2** | The **ruling on the bullet-fragment motion**, and the State's response | Already **Q-35**; the exculpatory-characterisation dispute turns on it |
| **E-3** | Any **later ATF firearms/toolmark report** on a located suspect tool 🛠 *(v1.1: discipline named — `CR-E20` rule 1. ⚠️ **A later ATF *biology* report on the Dremel already exists and is a different document — State's Exhibit 33**, `CR-E20` §2)* | F-98 is expressly contingent on one |
| **E-4** | The **autopsy report** (Q-51 / State's Exhibit 11) | The only route to N-3 |

⚠️ **Tier 3 context, recorded as context and not adopted:** reporting of March–April 2026 indicates this report became the subject of public controversy and a judicial unsealing, with fact-checks disputing characterisations of it as exonerating. **This library reached its position from the document, before consulting any of that reporting, and states it independently of it.**

---

## §7 · Living persons

The **examiner and two reviewers** are federal employees named as authors on a laboratory report filed in the public court record; they are recorded **in official capacity only**, with **no characterisation attached**. The **addressee agent** likewise. ⚠️ **A rifle serial number appears on the report's face and is reproduced here only because it is the exhibit designator the report uses**; no other identifying detail is carried. **No allegation in this file is adopted, and nothing here adjudicates anyone's conduct.**

---

## §8 · Residual scope

This file read **the report's four pages and the motion's body**. It did **not** read the motion's remaining exhibits, the State's response, or any ruling. It did **not** verify any ATF conclusion — **it records what a laboratory concluded, which is a different thing.** It did **not** establish the provenance of Exhibit 6. It did **not** assess whether the defence's motion should succeed. **Case posture untouched: Tyler James Robinson has NOT been bound over; the presumption of innocence applies.**

🛠 **RESIDUAL OF THE v1.1 PASS SPECIFICALLY — stated so it is not read as coverage it is not.**

1. 🚨 **`F-139`'s DECISIVE ARTIFACT WAS NOT OBTAINED.** **State's Exhibit 32 as admitted is not held.** Every act at `F-139(b)` compares the *record's description and navigation of* the exhibit against the motion attachment. **The two documents were never placed side by side, because only one of them is held.**
2. 🚨 **THE PROMOTION AT `F-139(e)` WAS NOT PERFORMED.** `F-96`–`F-99` are unchanged in wording, scope and grade. **No finding in this file was re-verified by this pass** — the v1.1 pass tested the **identity of the document**, not the accuracy of anything read from it.
3. **This pass read `day4.txt` only, and only its three Exhibit-32 blocks** (05:26:18–05:32:02, 06:25:27–06:27:07, 07:10:29–07:12:54) **plus the Exhibit-30 identification at 05:18:35–05:19:09 for §0.0.** It did **not** read Days 1, 2, 3 or 5, and did not read the rest of Day 4.
4. **It re-rendered pages 1–4 of the report** (PDF pp. 26–29 of `tyler-robinson-ballistics-motion.pdf`; p. 25 is the *"Exhibit 2"* slip sheet) **to test layout, not to re-read content.** ✅ *En route it confirmed §1's extraction-defect caveat — `pdftotext` over pp. 25–26 still returns mojibake — and the motion PDF's own **CreationDate: 2026-01-09**, consistent with §1's "dated 9 January 2026" and with the court's "late last year or early this year."*
5. ⚠️ **NO OTHER FILE WAS TOUCHED.** **`CR-E20` is owed two things by this pass and receives neither: the locator repair at `CR-E20 F-4`** (*"roughly 05:29:5x"* → **05:29:01**) **and the re-grade `F-139(c)` says is now available.** **Both are `CR-E20`'s to make.** `DNA-E01`, `CR-E01`, `CR-E02` and `CR-E14` are unedited.
6. ⚠️ **NO REGISTER ENTRY IS ASSIGNED, MOVED OR RESOLVED.** **No D-number is touched and no ceiling is restated — `QUEUE.md`'s header is the single source of truth.** 🛠 **`F-139` and `F-140` were assigned after reading the F-series' assignment sites rather than counting strings** (standing hazard 6): the highest F-number **assigned** anywhere in the repository on 2026-08-30 was **`F-138`** (read at its assignment site in `CR-E18`'s findings section, not inferred from a prose mention), and **`F-139`/`F-140`/`F-141` returned 0 hits repo-wide across all file types.**
7. ⚠️ **`[PROVISIONAL]` IS NOT CLEARED.** No independent verification cycle has run on this file — **including on `F-139` and `F-140`, which are as provisional as everything above them** → **Q-113**.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-101 EXECUTED — and the target was already on disk.** The ATF firearms report (2025-W-000401, 2025-09-17) is **Exhibit 2 to the bullet-fragment motion banked in the founding acquisition pass of 2026-07-27**, and was invisible to every text search because **its text layer is corrupted by a broken font encoding** — read here by rendering the pages. **F-96: the cartridge case WAS identified to the rifle at `[Source identification]`.** **F-97: the bullet jacket fragment is `[Inconclusive]` — could not be identified OR excluded, with all class characteristics in agreement but compatible with numerous makes and models.** **F-98: rotary-tool scribe marks on the case and cartridges, expressly contingent on a suspect tool being located.** **F-100 corrects the record on CR-E14's F-87: the defence's characterisation is accurate as far as it goes and materially incomplete**, and this file states the operative rule barring either half from travelling alone. **F-101: third instance in one day of holding an uncited Tier 1 document — → Q-110.** `[PROVISIONAL]`. |
| **v1.1** | **2026-08-30** | 🚨 **THE JOIN LANDED: THE REPORT THIS FILE READ AT TIER 1 IS STATE'S EXHIBIT 32 — `F-139` ADDED at the new §4A**, executing **`CR-E20 F-4`** on the `CR-E15` end. ⚠️ **SPLIT-GRADED AND THE SPLIT IS THE FINDING: ANCHOR High · IDENTITY Medium-high, AN INFERENCE.** **Anchor:** the exhibit is identified at `day4.txt` **05:26:25** *("an ATF report that I received in relation to the gun as well as cartridge case and cartridges")* and admitted **05:27:06**; the test-fire sentence read at **05:28:32** and the source-identification sentence at **05:29:01** are **this file's `F-96`**, the toolmark paragraph at **05:29:53→05:30:22** is **`F-98`**, and the *"Exhibit 6B through 6E lead fragments are not suitable for microscopic comparison"* line at **05:31:54** is **`F-97`'s second limb, verbatim**; the court noted at **05:27:20** that the exhibit *"has been previously disclosed publicly from an earlier filing, I believe from either late last year or early this year"* — and the motion this file read is **dated 9 January 2026** *(PDF CreationDate 2026-01-09, verified this pass)*. **FOUR VERIFICATION ACTS RUN THIS PASS, none imported:** **(1)** the report's **author authenticated Exhibit 32 under oath** — *"Are you the author of this report?" — "I am, yes."* (**06:25:42–44**), conclusions *"accurately documented"* (**06:26:32**); **(2)** **nine display-navigation instructions land on the motion attachment's own page and paragraph layout** — *"the second line under Results of Examination,"* *"skip the next line,"* *"the last paragraph on this page"* (**which breaks mid-sentence**), *"the first FULL paragraph"* on p. 2, and the DOJ-policy *"two paragraphs"* at the bottom of p. 2 that are **`F-99`**; **(3)** the **appendix is at p. 4 of 4**, reached on cross as *"two pages in"* from p. 2 (**07:11:34**), the witness answering *"just as it says in the appendix"* (**07:12:36**); **(4)** *"the **submission one** report"* (**06:25:53**) matches the attachment's **Submission(s): 1** — ⚠️ **which also bounds `F-139` to the submission-1 report; the *Touhy* request records three ATF firearms reports and no later one is held.** 🛠 **CORRECTION MADE, NOT CARRIED: `CR-E20 F-4` places the source-identification reading at *"roughly 05:29:5x"* — it is at 05:29:01**; 05:29:53 is `F-98`. **The repair on the `CR-E20` end is owed and NOT made here.** 🚨 **TWO OF `CR-E20 F-4`'s "not established" limbs are OVERTAKEN and are restated accurately rather than repeated:** **pagination is now supported directly at High**, and **"no witness was asked" is true of the IDENTITY question only** — a witness *was* asked about authorship. **Completeness is Medium-high** (footers read *"Page 1 of 4"…"Page 4 of 4"*; nothing on the record states the exhibit's page count); **unredaction is UNTESTED and unverified.** ✅ **THE GRADE IS HELD AT MEDIUM-HIGH AND DELIBERATELY NOT RAISED** — the decisive artifact (Exhibit 32 as admitted) is not held, and **a `[PROVISIONAL]` file does not out-grade the canonical map that governs it; a re-grade is available and is `CR-E20`'s to make.** 🚨 **`F-139(e)`: IF the identity holds, State's Exhibit 32 is the ONE forensic exhibit in this case whose contents this library has actually read, and `F-96`/`F-97`/`F-98` (and `F-99`) may be read as findings about a HEARING EXHIBIT.** ⚠️ **THAT PROMOTION IS EXPRESSLY NOT PERFORMED — recorded as available-and-not-taken so the restraint is auditable; every §3/§4 finding stands exactly as at v1.0.** 🆕 **`F-140`: A CROSS-FOLDER JOIN FAILURE — both halves on disk, in different folders, since 2026-07-27, and no file joined them. Second instance of this exact shape found on 2026-08-30**, the first being **`DNA-E01 F-14`** (ATF sub-item 1.11 = the test fires). ⚠️ **A DISTINCT CLASS FROM `F-101`, which is why it gets its own number:** `F-101` is held documents **nobody cited**; `F-140` is held documents **cited in separate files that nobody read against each other** — the harder failure, because every individual file looks complete. **`F-101` is annotated in place as EXTENDED, not superseded.** 🚨 **NEW §0.0 — NAMING DISCIPLINE, per `CR-E20`:** **State's Exhibit 30 is the ATF DNA report and is a DIFFERENT DOCUMENT** (*"the ATF report that I received regarding the DNA testing on the gun…"*, `day4.txt` **05:18:35**); **nothing in this file may be cited to Exhibit 30**, and `CR-E20`'s writing rules bind future edits. ✅ **CHECKED: this file never implied otherwise** — `/Exhibit 30/` = **0**, `/ATF firearm report/` = **0** (**`N-6`**); 🛠 **two under-specified bare *"ATF report"* usages at §6 disambiguated in place.** **Nulls added: `N-5`** (`/Exhibit 32/` over v1.0 = **0** — the null this revision closes), **`N-6`**, **`N-7`** (no witness asked the identity question; scope = the three Exhibit-32 blocks). ⚠️ **Divergences logged rather than smoothed (`F-139(d)`):** four points where Rev renders the reading differently from the document — *"(inscribed marks)"* for **"(scribe marks)"**, *"Exhibit 6"* for **"Exhibit 6A"**, *"a microscopic similarity"* for **"microscopic dissimilarity"**, *"Exhibit 1A"* for **"the Exhibit 1 rifle"** — **all Rev renderings of speech, governed by `CR-E18 F-138`'s standing limit, and all cutting FOR the join.** ⚠️ **RESIDUAL at §8: the decisive artifact was not obtained; no §3/§4 finding was re-verified; only `day4.txt`'s Exhibit-32 blocks were read; NO OTHER FILE WAS TOUCHED.** ⚠️ **NO REGISTER ENTRY ASSIGNED, MOVED OR RESOLVED; no D-number touched; no ceiling restated — `QUEUE.md` governs.** **`F-139`/`F-140` assigned after reading the F-series' assignment sites, not counting strings** (hazard 6): highest **assigned** was `F-138`; `F-139`–`F-141` returned 0 hits repo-wide. 🛠 **TWO DEFECTS INTRODUCED BY THIS PASS AND CAUGHT WITHIN IT, LOGGED RATHER THAN QUIETLY FIXED:** **(a)** §0.0's Exhibit-30 null was first written unscoped, and it is **false of v1.1** — the block names Exhibit 30 throughout; **now scoped to v1.0 expressly** *(the `caveats-are-claims` shape, committed inside the caveat that states the rule)*. **(b)** §0.1 still read **"this file depends on no other provisional file,"** which **§4A made false** — **`CR-E20` is `[PROVISIONAL]`**; the dependency is now **declared at §0.1**, with what does and does not turn on it separated, and **neither file may clear the other.** **`[PROVISIONAL]` NOT cleared → Q-113. Case posture untouched: Tyler James Robinson has NOT been bound over and the presumption of innocence applies.** |
