# CR-E14 — The motion to vacate or continue, the discovery record it puts on the public file, and the chronology gap it closes

**File ID:** CR-E14 · **Scope:** the defence *Motion to Vacate or Continue Preliminary Hearing Pending Discovery* (signed and served **2026-03-27**, 69 PDF pp. with two addenda and Exhibits A–G), and the victim representative's *Invocation of Speedy Trial Rights* (**2026-01-16**) — read in full. Closes the library's **May → July** preliminary-hearing chronology gap (**F-49**). ⚠️ **The motion also puts a substantial forensic and discovery record on the public file, and that is the reason this file matters beyond scheduling.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo Department — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

⚠️ **Findings `[PROVISIONAL]`.** Sourced from the 2026-08-16 reader pass; raw report banked with the others at `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q70-completion-six-reader-reports_RAW.md`. **No independent verification cycle has run** → **Q-99**.

🚨 **CASE POSTURE: Tyler James Robinson has NOT been bound over for trial. The presumption of innocence applies throughout.** As of this motion's own date the preliminary hearing had not yet occurred. **Every assertion in §4–§6 is the DEFENCE's, attributed and adopted by nobody.**

---

## §0 · Sourcing framework (project standard)

**Tier 1** — sworn testimony and primary court filings/documents · **Tier 2** — named official statements · **Tier 3** — named journalistic reporting/analysis · **Tier 4** — anonymous-source or low-verification material. **"T1 via T3"** marks primary content known only through reporting.

🚨 **A tier warning that governs this entire file.** The motion is **Tier 1 as a filing** — it reliably establishes *what the defence asserted, and when*. **It is not a source for the truth of anything it describes.** It characterises **laboratory reports this library does not hold**. Several of those characterisations are extraordinarily consequential (§5). **They are recording layer and must stay there.**

---

## §1 · Access-path caveats, first

| | |
|---|---|
| **How obtained** | DocumentCloud, **outside** project 224251 — found by a case-number search on 2026-08-16 and banked the same day (**[CR-ACQ-2026-08-16](CR-ACQ-2026-08-16_documentcloud-complete-sweep.md)** §3, as corrected at v1.1). ⚠️ **Uploaded three times under three IDs; the three are byte-identical but for the PDF trailer `/ID`. ONE document, not three.** |
| ⚠️ **Hazards 11 and 13 both live here** | Both `.txt` files are classified **`data`** by `file(1)`; the motion's extraction carries **69 NUL bytes, 4× U+FFFE and 2× U+019F**. **A bare `grep` on these files is unsafe.** Every read and search behind this file was run in Python with `errors='replace'`, on whitespace-collapsed text with dashes and quotes treated as character classes. |
| **Provenance — one of three** | ⚠️ **No court file-stamp, no clerk endorsement, no assigned document number, no XChange stamp.** Signature block ✅ and certificates of service ✅; PDF metadata records creation **2026-03-27 22:38 EDT**. **This is the as-submitted copy.** |
| ⚠️ **Date convention** | **The document is signed, served and created 2026-03-27. The banked filename says 2026-04-02** (the upload date). **Do not conflate them in chronology work** — and note this is a fourth instance of the standing metadata hazard (CR-ACQ-2026-08-16 **F-39**). |
| **Not held** | The State's opposition, if any; **any order disposing of the motion**; the 2026-04-17 minute entry; and every laboratory report the motion describes. |

---

## §2 · What the motion is, and what it actually sought

**Not what its title suggested.** *"March 27, 2026"* in the DocumentCloud title is the motion's **own signature date**, not a date being vacated.

**The target is the preliminary hearing set for the week of 2026-05-18 → 05-22.**

**F-82 — The relief sought was two-tier, and the second tier is the load-bearing one. Confidence: High.** Unless the outstanding materials were produced by **2026-04-17** — *"the date on which this motion is set for hearing"* — the hearing *"should be vacated until they have been."* **If they were produced by then, the hearing should be postponed by *"no less than six months."***

**Grounds** (recording layer): Sixth and Eighth Amendments; Utah Const. art. I §§ 12, 13; Utah R. Crim. P. 7B; Utah R. Civ. P. 40(b); Utah R. Evid. 1102 — argued factor-by-factor against the five-factor test of *Layton City v. Longcrier*, 943 P.2d 655, 659 (Utah 1997).

**The core theory**, attributed: that Utah Const. art. I § 12 makes appropriate discovery a **precondition** to the State's use of reliable hearsay under URE 1102 at a preliminary hearing — because the State intended to proceed largely on **forensic reports without live expert testimony**, which the defence says it cannot test without the underlying laboratory files.

**F-83 — The State's intended preliminary-hearing case is described, and it matches what was actually held. Confidence: Medium-high** (the description is the defence's, but the library has read all five hearing days). Per a 2026-03-12 meet-and-confer the State intended discrete "buckets" through **three identified law-enforcement witnesses** — FBI/ATF DNA and ballistics, phone and social-media data, crime-scene and search testimony — plus testimony from the defendant's parents and roommate, and possibly one to three lay witnesses. ⚠️ **Family members and the roommate are referenced by role only, in the filing and here.**

---

## §3 · F-84 — The May → July chronology gap is CLOSED. Confidence: High as to the mechanism.

The library has carried, unexplained, that the preliminary hearing was set for **May 2026** as of February and held in **July 2026**. **The chain is now unbroken, and every link is a document this project holds:**

| Date | Event | Source |
|---|---|---|
| **2025-12-11** | The court sets the prelim for the week of **May 18–22, 2026**, ⚠️ **at the State's request**, over defence's stated concern that the setting was premature. The court's own words, as quoted: the date is *"not set in stone,"* *"it certainly can be moved,"* and *"this is a goal."* | quoted in the motion from **Doc. 454** |
| **2026-01-16** | **Erika Kirk, as designated victim representative, invokes speedy-trial rights** under Utah Code § 77-38-7(2), through counsel | the Invocation, **held** (§7) |
| **2026-02-02** | The State deploys that invocation as scheduling pressure: *"The victim's representative has asserted the victim's speedy trial rights… This Court must firmly grasp the reins… to ensure that **May's preliminary hearing goes forward on schedule.**"* | **CR-E11**, Dkt. 366, **held** |
| **2026-03-13** | Defence gives notice in open court of its intention to move | the motion |
| **2026-03-27** | **This motion** — vacate, or continue by no less than six months | **held** |
| **2026-07-06 → 07-10** | The preliminary hearing is held | the library's five transcripts |

**F-85 — The outcome was a PARTIAL grant far below the relief sought — and this is an inference, not a record. Confidence: Medium.** The motion asked for vacatur **or no less than six months**, which from 18 May lands near mid-November. **The hearing was held 6 July — roughly seven weeks later, a fraction of what was requested.** ⚠️ **No order is held.** A superseding stipulation, a competing State motion, or the court's own calendar cannot be excluded as the operative cause. **What would settle it: the ruling or minute order from the 2026-04-17 hearing** → **Q-100**.

**F-86 — The motion contains no outcome of any kind. Confidence: High** (scoped null, §9 N-1). All 69 pages read; no judicial signature, no order, no proposed order, no notice of hearing, no clerk endorsement, no docket number.

---

## §4 · RECORDING LAYER — the discovery record the motion puts on the public file

⚠️ **All figures below are the defence's, in a contested filing. This library has verified their internal arithmetic and nothing else.**

- **R-1 — Volume.** ~**19,612 files** across **25 productions** between 2025-10-10 and 2026-03-18; ~**61,500 pages** of document and image files; **31 hours** of audio; **more than 5,000 video files / over 698 hours**. Separately **~12 terabytes** of digital-device discovery — **6,425 folders, 613,023 files** — with ~60 days needed for initial review alone. **28 law-enforcement agencies** are listed.
- **R-2 — Latency, asserted.** A cellphone associated with the defendant was **extracted 2025-09-13 and reviewed by 2025-09-14**, and **not produced to the defence until March 2026** — roughly six months. An index is said to show nearly all **38 digital items** fully reviewed by law enforcement by **2025-09-25**, likewise not produced until March 2026. The **autopsy report** was completed **2025-09-16** and produced **2025-11-13**; **autopsy photographs** taken **2025-09-10** and produced **2026-03-18**.
- **R-3 — Where the defence places blame, and where it does not.** Expressly **not** with the Utah County Attorney's Office — counsel describes a *"highly professional rapport"* — but *"with the law enforcement agencies that have delayed providing the requested materials."* ⚠️ **Recorded because it cuts against the reading a hostile summary would give this motion**, and because it is an attributed characterisation of named agencies which this library does not adopt.
- **R-4 — Expert timelines.** A retained forensic biologist declares she needs **~six months after all discovery is produced**. A second expert estimates 3–4 weeks for initial review plus 2 weeks for a report, and potentially another month if validation data must be reviewed.
- **R-5 — The federal-testimony track.** On **2026-03-27** defence counsel wrote to **ATF Chief Counsel and FBI General Counsel** under **28 C.F.R. § 16.21** *et seq.* (*Touhy*) seeking testimony from **three ATF examiners** (forensic biologist, firearm/toolmark examiner, fingerprint specialist — Beltsville, MD) and **two FBI examiners** (Quantico, VA), demanding a definitive response **by 2026-04-15**. 🚨 **The examiners named include the ATF and FBI analysts whose preliminary-hearing testimony this library has already read in full at CR-E06.** **The agencies' responses are not held.**

---

## §5 · 🚨 THE SINGLE MOST CONSEQUENTIAL CLAIM IN THE DOCUMENT — and it stays in the recording layer

**F-87 — The defence states that an ATF summary report indicates ATF *was unable to identify the bullet recovered at autopsy to the rifle allegedly tied to Mr. Robinson*, and that the defence *"may very well decide to offer"* that examiner's testimony **as exculpatory evidence**. Confidence in the ASSERTION being made: High. Confidence in the underlying fact: UNVERIFIED — and it must stay that way on this filing alone.**

**Why this cannot be promoted:**
1. **The report is not held.** This is a party's characterisation of a document nobody in this project has read.
2. **It is a characterisation made in a motion whose purpose is to obtain a continuance** — i.e. by a party with an interest in emphasising what is missing and unresolved.
3. **The motion itself says the FBI is separately conducting a SECOND comparative bullet analysis plus a bullet-lead analysis, both incomplete as of 2026-03-27.** ⚠️ **"Unable to identify" in one examination is not "excluded," and a later examination may say something different.** Firearms identification has inconclusive outcomes that are neither identification nor elimination, and **nothing in this filing establishes which category the ATF result falls into.**
4. ⚠️ **The motion's own phrasing is careful — *"the rifle allegedly tied to Mr. Robinson"*** — and this file preserves that hedge rather than dropping it.

**What it does establish, at High confidence:** that **as of 2026-03-27 the defence was asserting on the public record that an ATF ballistics result did not identify the autopsy bullet to the rifle, and was contemplating offering it as exculpatory.** That is a fact about the litigation, and it is the correct level at which to hold it.

🚨 **This is the highest-value acquisition target the library has surfaced today** → **Q-101**. Until the report is held, **no file may state that the bullet was not matched to the rifle.**

**F-88 — DNA characterisations, likewise recording layer.** The motion states that **both FBI and ATF recovered "minute quantities"**, with mixtures of **up to "five or more" individuals**, and that **both used STRmix**; it cites four federal decisions excluding or remanding STRmix analyses. ⚠️ **Consistent with, and not a substitute for, what DNA-E01 establishes from the sworn testimony itself.** → §6.

---

## §6 · What this does to the DNA file, stated carefully

DNA-E01's headline result — that **both headline DNA statistics assume Lance Twiggs is a contributor in both of their competing propositions**, so the statistic never tests his presence, and **the only likelihood ratio ever run on him alone was 1, "uninformative"** — is derived from **sworn testimony** and is **untouched by this motion**.

**What the motion adds is context, not evidence:** that the underlying samples were *"minute quantities"*, that mixtures ran to *"five or more"* contributors, that **STRmix** was the tool on both sides, and that a body of federal authority contests STRmix analyses. ⚠️ **All four are the defence's assertions in a contested filing.**

**F-89 — A caution against a tempting error. Confidence: High.** These characterisations are **congenial to DNA-E01's existing finding**, which is exactly why they must not be folded into it. **The project's cardinal error is asserting in the analyst layer something carried from a claimant** — the V-10 lesson. **Grade the anchor and the connection separately:** that the defence *asserted* five-or-more-contributor mixtures is an anchor; that this supports any conclusion about what the DNA can bear is a connection, and it is not established by this filing. → **Q-102**.

---

## §7 · The victim representative's Invocation of Speedy Trial Rights

**F-90 — Identified exactly. Confidence: High.** The 2026-01-19 filing is an ***Invocation of Speedy Trial Rights***, **dated 2026-01-16**, filed by victim's counsel with Utah local counsel, in which **Erika Kirk, as the court-designated victim representative, asserts her right to a speedy trial under Utah Code § 77-38-7(2).** It is a **notice**: it requests no scheduling order and seeks no specific relief. ⚠️ **This is precisely the assertion the State invoked seventeen days later as scheduling pressure** (§3).

**Recording layer:** the filing argues that the Constitution guarantees a defendant a fair trial but *"does not guarantee them the right to cause undue delay,"* and quotes the statutory victims' right to a speedy disposition free from unwarranted delay caused by or at the behest of the defendant. ⚠️ **The quoted passage carries no pin cite to its subsection**, and this project has not verified the quotation against the statute → **Q-103**.

**D-72 — OPEN: the Invocation's certificate of delivery is dated four months before the document. Confidence in the discrepancy: High; the cause is Medium-high.** The certificate certifies e-filing *"on September 16, 2025,"* while the document is dated — and its PDF created — **2026-01-16**. **Probable cause, and it is checkable:** the January filing reuses the header block and certificate paragraph of the same counsel's **2025-09-16** victim-representative request **verbatim**, carrying the stale date through. 🚨 **Do not read "September 16, 2025" as this document's filing date.**

**F-91 — 🚨 The defence motion never engages the invocation at all, and the silence is itself a finding. Confidence: High** (scoped null, §9 N-2). The stem `speedy` returns **zero** across all 69 pages — **six weeks after the State deployed the victim's invocation as the reason the May date must hold.** ⚠️ **Recorded as a fact about the filings, not as a criticism of counsel; a party is not obliged to answer every argument.**

---

## §8 · Candidate discrepancies and defects on the face of the filing

**D-70 — OPEN: the ATF DNA report count conflicts inside one filing.** Counsel's *Touhy* letter describes the ATF examiner's output as *"her single report dated September 15, 2025, and two reports dated December 11, 2025"* — **three**. An exhibit letter lists **four** ATF DNA laboratory reports (two dated 2025-09-15, two dated 2025-12-11, across submissions 1, 1&2, 3&5, 4). **Not reconcilable from the face of the document.** ⚠️ **This matters: it is a count of the very reports DNA-E01 is built around.**

**D-71 — OPEN: the 12 TB production date.** The memorandum body says the digital discovery arrived *"during the March 12, 2026 meeting"* and again *"received on March 12, 2026"* — while **citing a declaration paragraph that says March 13, 2026**. A one-day conflict inside a single filing.

**Defects recorded but below register threshold:**
- **A promised attachment is absent.** The expert's declaration states her full resume *"is attached hereto."* **It is not in the 69 pages.** Verified at page level, not by keyword.
- **The *Touhy* request covers only one of three ATF firearms reports** listed in the same filing's own exhibit (2025-09-17 sought; 2025-10-06 and 2026-02-25 not).
- **Two internal quotations are inaccurate to their own sources** — one compresses a declaration's sentence inside quotation marks, dropping its tail; another block quote **ends mid-sentence**, omitting the closing words.
- **A typographic-defect cluster consistent with a rushed filing**, including a misspelling **in the motion's own title**, two instances of "2015" for 2025, one of "2025" for 2026 inside a sworn declaration, and a mis-numbered sub-item series.
- **The defence expert appears under an informal first name in the body and her formal name in the declaration.** Same person.

**F-92 — The defence team is FOUR counsel, not three. Confidence: High.** The signature block carries **Nester, Novak, Burt and Visser** (Brown, Bradshaw & Moffat, UT #14358), with Visser signing both certificates. ⚠️ **Any library file carrying "Nester / Novak / Burt" is incomplete.**

**F-93 — Internal arithmetic verified, and it holds. Confidence: Medium-high.** The 25-row production exhibit sums to **19,612**, matching its own stated total; a second exhibit's six categories sum to the same figure; a third reconciles exactly via its own footnote; and the declaration's month-by-month counts match the exhibit's row dates. ✅ **Logged as a confirmation, per the verify-in-both-directions rule.** ⚠️ **This grades the arithmetic only. Internal consistency is not external truth.**

---

## §9 · Scoped nulls

Each was run in Python on normalised, control-stripped text across all 69 pages, **with every hit opened and read** and substring false positives (e.g. *"gag"* inside *engaged*, *"closure"* inside *disclosure*) excluded by reading.

- **N-1 — No outcome, order or disposition anywhere in the motion.** §3, F-86.
- **N-2 — `speedy` returns zero.** §7, F-91.
- **N-3 — Dkt. 332 is NOT cited in this motion.** Searched `332`, `331`, `333`, `Dkt`, `Doc.`, `docket`, and every bare three-digit number. **Zero.** ⚠️ **But the motion independently confirms the same underlying proceeding** — it records that at *"the hearing held January 16, 2026"* the parties discussed the status of the laboratory files and the State said it too was awaiting them. **The library's identification of Dkt. 332 stands on the State's own citation; this motion is simply not a second source for the number.**
- **N-4 — The disqualification litigation is not discussed.** `disqualif`, `recus`, `conflict of interest`, `Attorney General` → **zero**.
- **N-5 — Mitigation timelines are not discussed.** The stem `mitigat` returns **zero across 69 pages**. Penalty-phase investigation appears only inside quoted ABA Guideline text, never as a case-specific schedule. ⚠️ **Expert timelines are discussed at length; mitigation timelines are not** — a distinction worth preserving.
- **N-6 — Death-penalty posture is assumed, not litigated.** The case is repeatedly described as capital; there is no notice-of-intent discussion, no aggravator analysis, no posture change.
- **N-7 — Case-substantive topics absent entirely:** `Zinn`, `Twiggs`, `Losee`, `Discord`, `transgender`, `manifesto`, `shackl`, `contempt`, `seal`, `bail`, `protective order`, `bind over` / `bound over`, `trial date` → **zero**. All `competen` hits are *"competent counsel"*.
- **N-8 — Scope limit, stated honestly:** a search of the two XChange case-history extracts for the document numbers surfaced here returned nothing, **but that is a null about those two files' format** (they carry no document numbers at all — and see standing hazard 13), **not evidence that the numbers are absent from the docket.**

---

## §10 · 🚨 A closure-map consequence CR-E12 did not have

**F-94 — Content from a classified transcript reaches the public record through party filings. Confidence: High.** This motion **quotes the court's own words from Doc. 454, the transcript of the 2025-12-11 hearing.** ⚠️ **CR-E12 records that hearing as PARTIALLY CLOSED, its transcripts filed `**** PRIVATE ****`, its redacted version `**** SEALED ****`, and its minute order `**** SEALED ****`** — the strictest lock in the case.

**Yet a party with access quoted it in a filing that is publicly available.** So the closure map needs a route it does not currently have: **classification restricts the record; it does not restrain a party's quotation of it in a later public filing.** ⚠️ **Two cautions attach.** (a) The quoted passages here are from **the open portion** so far as can be told, and **nothing may be inferred about the closed segment from them.** (b) **A party's quotation of a transcript this project cannot read is unverifiable** — it is Tier 1 as to the fact of the quotation, and **T1-via-a-party as to the words.** → **Q-104**, and CR-E12 should carry this at its next revision.

**F-95 — Doc. 454 and Doc. 61 arrive at Tier 1.** **Doc. 454** = the 2025-12-11 hearing transcript. **Doc. 61** = the defence's formal Rule 16 discovery request with 404(b) notice, filed **2025-09-30**, its ¶¶ 24–31 covering forensic testing. **Both cited by number inside a primary filing**, which is the Tier 1 route under CR-ACQ-2026-08-16 F-39. **Neither is held.**

---

## §11 · Living persons and PII

- **A defence counsel's personal cellular telephone number** appears in the *Touhy* letters at two identified pages. **Not reproduced.**
- **The defendant's parents and roommate** are referenced **by role only**, both in the filing and here. They are private individuals; they appear solely because their anticipated testimony defines the scope of the hearing. **No further detail.**
- **Federal forensic examiners and technical reviewers are named** in the *Touhy* letters and an exhibit. They are **government employees named as report authors in a public court filing** — public-role actors — and are recorded here **by role and report date only**, because their reports are acquisition targets. **No personal details, no duty-station detail beyond what identifies the office.**
- **Counsel anonymised his own team members by role** (*"Paralegal 1," "EDCA 1"*). **Preserved as-is.**
- **Erika Kirk** appears **only** in her role as court-designated victim representative and as the party invoking speedy-trial rights. **No other family detail.**
- **Case and laboratory identifiers** useful for future requests are recorded in the acquisition roadmap; they identify **files**, not persons.

---

## §12 · Findings, resolutions and open items

**Resolved:** the May → July mechanism (**F-84**, High). The Invocation's identity (**F-90**, High). The defence team's composition (**F-92**). The motion's internal arithmetic (**F-93**, a logged confirmation).

**Explicitly NOT resolved:** what actually moved the date (**F-85**, Medium, inference only — no order held). **Anything at all about the ATF ballistics result** (**F-87** — recording layer, and it stays there).

**Acquisition roadmap:**

| | Target | Why |
|---|---|---|
| **D-1** 🚨 | **The ATF summary report on the autopsy bullet** | **The highest-value target surfaced today.** Until it is held, no file may say the bullet was not matched to the rifle (**F-87**). |
| **D-2** | **The ruling / minute order from the 2026-04-17 hearing** | The only document that converts **F-85** from inference to record. |
| **D-3** | **Doc. 454** — the 2025-12-11 hearing transcript | Carries the court's *"not set in stone"* remarks and the original May setting. ⚠️ **Classified — but §10 shows its content can surface through party filings.** |
| **D-4** | **Doc. 61** — the defence Rule 16 discovery request, 2025-09-30 | The baseline against which every latency assertion in §4 is measured. |
| **D-5** | The **ATF and FBI responses** to the 2026-03-27 *Touhy* letters, due 2026-04-15 | Determines whether federal examiners could be compelled — bears on every forensic acquisition route the library has. |
| **D-6** | The **FBI second comparative bullet analysis** and **bullet-lead analysis** (incomplete at 2026-03-27) | Directly qualifies **F-87**. |
| **D-7** | The **autopsy report** (completed 2025-09-16) and photographs | Already tracked as Q-51 / State's Exhibit 11; now with production dates. |
| **D-8** | An **FBI summary report of 2025-09-14** said to reference a headquarters unit regarding **the writing on the bullet casings** | A distinct lead the library has never had. |

---

## §13 · Residual scope — what this file did NOT do

**It verified no factual assertion in the motion against any external source.** §4, §5 and §6 are recording layer throughout; **F-87 in particular is the defence's characterisation of a report nobody here has read, and it is the single most consequential claim in the document.** No order disposing of the motion was located or read; no State opposition; no 2026-04-17 minute entry — **F-85's Medium grade rests entirely on that gap.** The 2025-12-11 hearing quotations were not checked against Doc. 454, which is not held. The four cited STRmix decisions were not audited for accurate characterisation, nor was any other citation. The exhibits' **internal arithmetic** was verified; **their external truth was not**. The statutory quotation in the Invocation was not checked against the statute. **No PDF was examined for redactions, annotations or embedded attachments.**

**Nothing in this file alters case posture. Tyler James Robinson has NOT been bound over for trial; the presumption of innocence applies throughout.**

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Closes the May → July preliminary-hearing chronology gap (F-84, High)** with an unbroken six-link chain, and identifies the victim representative's **Invocation of Speedy Trial Rights** exactly (F-90). F-82 → F-95 opened; **D-70, D-71, D-72** opened; **Q-99 → Q-104** raised. 🚨 **F-87 records the defence's assertion that an ATF report did not identify the autopsy bullet to the rifle — held strictly in the recording layer, with four stated reasons it cannot be promoted, and raised as the library's highest-value acquisition target.** **F-94 gives CR-E12 a route it lacked: classification restricts a record but does not restrain a party from quoting it in a later public filing.** `[PROVISIONAL]`. |
