# CR-E15 — The ATF firearms laboratory report of 2025-09-17, read directly

**File ID:** CR-E15 · **Scope:** the **ATF Forensic Science Laboratory report, case 2025-W-000401, dated 2025-09-17**, read **directly from the document** — not through a party's characterisation of it — together with the defence motion it is attached to. Executes **Q-101** and bears on **Q-35**. · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

⚠️ **Findings `[PROVISIONAL]`.** No independent verification cycle has run → **Q-113**.

🚨 **CASE POSTURE: Tyler James Robinson has NOT been bound over for trial. The presumption of innocence applies throughout.** ⚠️ **This file records forensic findings that cut in more than one direction. It adopts none of them as proof of anything, and it is not an argument for or against any party.**

> ### ⚠️ §0.1 · PROVISIONAL DEPENDENCIES — LOOP §2 discipline
> ✅ **This file depends on no other provisional file.** The report was **read directly from the primary document** (rendered pages, not a text layer). Its only outbound correction is to **CR-E14 F-87**, which was itself explicitly recording-layer. **Clearing item: Q-113.**

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

**F-101 — This is the third instance in one day of the same failure, and the pattern is now the finding. Confidence: High.** The library held (a) `oct24_clean.txt`, a 97-page Tier 1 transcript of a hearing CR-E12 called *"structurally unobtainable"*; (b) this ATF report, named the same day as the **highest-value acquisition target** while sitting on disk; and (c) the **bullet-fragment motion** (Q-35). **All three were acquired in the founding pass of 2026-07-27 and never cited by an evidence file.** ⚠️ **In this case a fourth factor hid it: an extraction defect made the document unreachable by every search the library runs.** → **Q-110** is not housekeeping; it is the highest-yield item open.

---

## §5 · Scoped nulls

- **N-1 — The report makes no statement about the shooter, the shooting, distance, trajectory or position.** It is a comparison report on six exhibits. Scope: all four pages, read as rendered images.
- **N-2 — The report does not mention DNA.** Scope: as above. *(A separate ATF DNA track exists — CR-E11, CR-E14 — and is not this report.)*
- **N-3 — No autopsy finding is stated here.** The bullet jacket fragment's provenance is not described in this report; **that it is "the bullet recovered at autopsy" is the defence's description, not the report's.** ⚠️ **Recorded because it matters: this file does not establish where Exhibit 6 came from.**
- **N-4 — The report states no conclusion about the three unfired cartridges' source**, only that toolmarks of comparison value are present on them.

---

## §6 · Findings, resolutions and open items

**Resolved.** **Q-101 is EXECUTED** — the ATF report is held and read directly. **Q-35's motion is also held.** The library no longer depends on any party's characterisation of this report.

**Not resolved.** Whether the fragment came from the autopsy (N-3). What the later FBI comparative and bullet-lead analyses concluded — **incomplete as of 2026-03-27** (CR-E14 §5). Whether any suspect rotary tool was located and compared (F-98). ⚠️ **The motion's own subject — that FBI testing may further alter the fragment — is a live dispute this file does not resolve.**

**Acquisition roadmap:**

| | Target | Why |
|---|---|---|
| **E-1** | The **FBI comparative bullet analysis and bullet-lead analysis** | Incomplete at 2026-03-27; would qualify F-97 directly |
| **E-2** | The **ruling on the bullet-fragment motion**, and the State's response | Already **Q-35**; the exculpatory-characterisation dispute turns on it |
| **E-3** | Any **later ATF report** on a located suspect tool | F-98 is expressly contingent on one |
| **E-4** | The **autopsy report** (Q-51 / State's Exhibit 11) | The only route to N-3 |

⚠️ **Tier 3 context, recorded as context and not adopted:** reporting of March–April 2026 indicates this report became the subject of public controversy and a judicial unsealing, with fact-checks disputing characterisations of it as exonerating. **This library reached its position from the document, before consulting any of that reporting, and states it independently of it.**

---

## §7 · Living persons

The **examiner and two reviewers** are federal employees named as authors on a laboratory report filed in the public court record; they are recorded **in official capacity only**, with **no characterisation attached**. The **addressee agent** likewise. ⚠️ **A rifle serial number appears on the report's face and is reproduced here only because it is the exhibit designator the report uses**; no other identifying detail is carried. **No allegation in this file is adopted, and nothing here adjudicates anyone's conduct.**

---

## §8 · Residual scope

This file read **the report's four pages and the motion's body**. It did **not** read the motion's remaining exhibits, the State's response, or any ruling. It did **not** verify any ATF conclusion — **it records what a laboratory concluded, which is a different thing.** It did **not** establish the provenance of Exhibit 6. It did **not** assess whether the defence's motion should succeed. **Case posture untouched: Tyler James Robinson has NOT been bound over; the presumption of innocence applies.**

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-101 EXECUTED — and the target was already on disk.** The ATF firearms report (2025-W-000401, 2025-09-17) is **Exhibit 2 to the bullet-fragment motion banked in the founding acquisition pass of 2026-07-27**, and was invisible to every text search because **its text layer is corrupted by a broken font encoding** — read here by rendering the pages. **F-96: the cartridge case WAS identified to the rifle at `[Source identification]`.** **F-97: the bullet jacket fragment is `[Inconclusive]` — could not be identified OR excluded, with all class characteristics in agreement but compatible with numerous makes and models.** **F-98: rotary-tool scribe marks on the case and cartridges, expressly contingent on a suspect tool being located.** **F-100 corrects the record on CR-E14's F-87: the defence's characterisation is accurate as far as it goes and materially incomplete**, and this file states the operative rule barring either half from travelling alone. **F-101: third instance in one day of holding an uncited Tier 1 document — → Q-110.** `[PROVISIONAL]`. |
