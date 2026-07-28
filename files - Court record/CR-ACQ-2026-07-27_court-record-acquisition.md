# CR-ACQ-2026-07-27 — Court Record Acquisition: State v. Robinson, Case No. 251403576

**File ID:** CR-ACQ-2026-07-27
**Scope:** first acquisition pass on the **primary court record** in *State of Utah v. Tyler James Robinson*. Establishes the access-path map (what is free, what is paywalled, what is bot-gated), banks the documents obtained, and records what they establish. This is the project's first file built on **Tier 1 court filings read directly** rather than on reporting about them.
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo Department, Utah County — Honorable **Tony F. Graf, Jr.** presiding. **Tyler Robinson is presumed innocent.** As of **2026-07-27** he has **not been bound over for trial**: the preliminary hearing concluded 2026-07-10 with the probable-cause ruling reserved for briefing (State's opening brief 2026-07-28, defense response 2026-08-11, State's reply 2026-08-18, oral argument 2026-09-01). Every allegation recorded below is an allegation; every defense assertion is a defense assertion. Nothing here is adopted.
**Prepared:** July 27, 2026
**Status:** v1.3 — contains a material correction to v1.0 (correction notice below, §3.1), and a **second correction from the adversarial pass**: the `source identification` was over-weighted because the identified cartridge case came from the rifle's own chamber. **D-48 has been resolved three times in one day** and now stands as an explicit split (§6.1). See **CR-AUDIT-2026-07-27 §2.1**.

> ### ⚠ CORRECTION NOTICE (v1.1, 2026-07-27)
> **v1.0 of this file materially understated the ATF report, and D-48 was resolved wrongly as a result.** v1.0 was written from the ATF report's language **as quoted in the defense motion**, because the report itself (Exhibit 2) could not then be machine-read. The report has since been **read directly** by rendering its pages. The direct reading shows the defense motion quoted only the portion bearing on *its own* subject — the bullet jacket fragment — and that **the same report also records a positive `source identification` linking a fired cartridge case to the Exhibit 1 rifle.** The corrected findings are at §3.1; D-48 is re-resolved at §6. v1.0's headline framing is superseded and should not be cited.

**Headline result (corrected).** The ATF firearms report of 2025-09-17 reaches **two different conclusions on two different items**, and any account giving only one of them misrepresents it:

- **Exhibit 2 — a fired .30-06 cartridge case — WAS positively identified as having been fired in the Exhibit 1 rifle. `[Source identification]`** — the strongest positive conclusion available in the DOJ's reporting framework.
- **Exhibit 6A — the bullet jacket fragment recovered at autopsy — was INCONCLUSIVE**: neither identified nor excluded. The four accompanying lead fragments were unsuitable for comparison.

The Exhibit 1 rifle is identified in the report as **a Mauser model 98, .30-06 Springfield caliber, serial number 8863, with an optical accessory**, test fired and found **operable**. This is the first hard forensic datum this library holds on the shot itself, and it is now held at **Tier 1, read directly**.

**Second result, methodological — and the more transferable one.** The correction above is a live instance of the project's cardinal error caught in the act. A **primary court filing quoted a primary lab report accurately but selectively**, and this file's v1.0 carried the resulting impression into the analyst layer. What prevented it from hardening was the project's own discipline: v1.0 refused to grade the quotation as "read directly," tiered it **T1 quoting T1**, and made reading the original **open item #1**. Closing that item within the same session reversed the finding. **Selective quotation by an adversarial party is a distinct sourcing hazard from the ones §0 already names, and it now has a name in this library.**

**Third result:** the access-path map is known. Utah XChange is **paywalled** and excluded. But the filings in this case are **public** — a motion to seal was denied — and are reachable free through outlet mirrors and transcript services. **The court record is an open acquisition channel for this project**, and four of the five preliminary-hearing days are now banked (§2C).

---

## 0. Sourcing framework (project standard)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements (incl. named first-person statements by principals)
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material

**"T1 via T3"** marks primary-document content known only through reporting. Confidence grades trace to a verification act by this project; **"— (checkable)"** marks the verifiable-but-not-yet-verified, never counted as findings.

**Tiering of the ATF report — history retained deliberately, because the change is the lesson.** In **v1.0** the report's language was known only through the defense motion's verbatim quotation, and was tiered **T1 quoting T1** — stronger than "T1 via T3," but explicitly *not* "read directly," with direct reading logged as open item #1. **In v1.1 that item is closed:** the report has been read directly by rendering its pages, and is now **Tier 1, read directly**. The upgrade did not merely raise confidence — **it reversed a finding** (§3.1, §6), because the quotation, though accurate, was partial.

**Standing rule this establishes.** A verbatim quotation by a party with an interest in the outcome is evidence of *what the quoted words say*, never of *what the source document as a whole establishes*. Grade the quotation and the document separately, exactly as the project already grades an anchor separately from the connection asserted on it. Treat this as a sibling of the V-10 lesson: there, a detail was carried at unearned confidence from a **claimant**; here, from an **adversarial filing**. Same failure mode, different source.

## 1. ACCESS PATH (caveats first)

**Route map established 2026-07-27:**

| Route | Status | Note |
|---|---|---|
| **Utah XChange** (`xchange.utcourts.gov`) | **PAYWALLED — excluded** | $10 one-time-use account (+$0.35/search, $1.00/document), or $25 setup + $40/month. Free access exists only at physical courthouse terminals. **No account was created and no fee was incurred.** This is a user spending decision, not one this project takes unilaterally |
| **Outlet-mirrored filings** | **OPEN — used** | Both documents below were retrieved this way (HTTP 200, curl with browser user-agent) |
| **Rev transcripts** | **OPEN — verified, not yet ingested** | Preliminary-hearing transcripts are freely readable. Day 4 (2026-07-10) confirmed present and un-paywalled. **Deliberately not ingested this session** — see §8 item 2 |
| **DocumentCloud** project 224251 ("Charlie Kirk Murder Case and Tyler Robinson") | **BOT-GATED** | API returned HTTP 403 to curl; the project page is JS-rendered so WebFetch sees the shell but no document list. Needs an interactive browser session |
| Direct court docket | **NOT OBTAINED** | No free public docket route found. The docket's existence and partial contents are inferred from filing references (§5) |

**Machine-readability — problem and resolution (v1.1).** The motion PDF's body (pp. 1–19) and Exhibit 1 (pp. 20–24) extract cleanly with `pypdf`. **Exhibit 2 — the ATF report, pp. 25–29 — does not:** its pages are drawn with a **Type3 font carrying no `/ToUnicode` map**, so `pypdf` yields null glyphs (`/0 /0 /0…`) and `pdftotext` yields a document-specific substitution scramble (the glyph codes are assigned in order of first use, not by character). The embedded images on those pages are logos and seals, not full-page scans, so image extraction recovers nothing either.

**Resolved 2026-07-27** by installing `poppler` (with the user's authorization) and rendering the pages: `pdftoppm -png -r 170 -f 26 -l 29`. The four resulting page images are banked and are **the authority for §3.1**. A plain-text transcription is *not* banked, because any transcription would be this project's own rendering of a scanned-glyph document; the images are cited instead.

**Retrievals and failures logged (all 2026-07-27):**
- Ballistics motion PDF — **success**, HTTP 200, 1,369,739 bytes, 29 pages.
- Redacted Oct 24 hearing transcript PDF — **success**, HTTP 200, 1,060,521 bytes, 97 pages.
- DocumentCloud API + project page — **403 / JS-gated**, no document list obtained.
- Utah XChange — **not attempted** (paywalled by design, see above).

**Artifacts banked**, byte-verified, in `CR-ACQ-2026-07-27_court-record-artifacts/` alongside this file, with SHA-256 for provenance:
- `tyler-robinson-ballistics-motion.pdf` — `b2395846d144924f683218a69e1b17e01ac5e3cd48ba7a6dd1ef6deb99f17f36`
- `tyler-robinson-redacted-hearing-transcript.pdf` — `7a891b006d5c7128a5e120a469461855d9121239189ca3011625036949e16dc6`
- `atf_page-26.png` … `atf_page-29.png` — **the rendered pages of Exhibit 2 (the ATF report), added v1.1. These images are the authority for §3.1**, since the page text is not extractable.
- `prelim-hearing-transcripts/day2–day5.txt` + `_raw.html` — the four banked hearing days (§2C), **unread**.
- plus extracted text (`…-ballistics-motion.txt`, `oct24_clean.txt`) for searchability. **The PDFs and page images are authoritative; the .txt files are convenience derivatives** and, for Exhibit 2, are known-corrupt (glyph scramble) and must not be quoted.

**Quotation note:** the filings are quoted as written, including their own typographical errors (e.g. the caption's "THISE VIDENCE"; a body reference to "January 12, 2025" where 2026 is meant; "two three separate types"). Errors are the source's, preserved rather than silently corrected.

## 2. DOCUMENTS ACQUIRED

**(A) Defendant's Motion re: bullet jacket fragment** — *Defendant's Motion For An Order Prohibiting Any Further Alteration Or Testing Of A Bullet Jacket Fragment Pending The Outcome Of This Motion, And Permitting A Defense Expert To Examine And Photograph This Evidence Before It Is Further Altered Or Destroyed, Or, In The Alternative, Permitting Either Defense Expert Observation Of Any Further Alteration Or Testing Of This Evidence, Or Video Recording Of Such Alteration And Testing, and Memorandum In Support.* 19 pages + 2 exhibits (29 PDF pages). Certificate of service: **served 2026-01-09** via the court's electronic filing system. **Tier 1.**

- **Counsel for Robinson:** Kathryn N. Nester (Nester Lewis PLLC); Richard G. Novak (*pro hac vice*); Michael N. Burt (*pro hac vice*); Staci Visser (Brown, Bradshaw & Moffat).
- **Exhibit 1** — *State's Notice Of Intent To Conduct Non-Destructive Testing*, served **2025-12-22**, 4 pages. Signed by Utah County Attorney **Jeffrey S. Gray** with Deputy County Attorneys Grunander, McBride, Hunt, Sturgill, and Ballard. **Readable — Tier 1, read directly.**
- **Exhibit 2** — **ATF laboratory report dated 2025-09-17**, disclosed to the defense 2025-12-18. **Banked but not machine-readable** (§1).

**(B) Redacted Transcript of Sealed Motion Hearing, 2025-10-24** — 97 pages, before Judge Graf, Fourth District Court, 137 North Freedom Boulevard, Provo. Reported by Phoebe S. Moorhead, RDR, CRR, UT CSR (Noteworthy Reporting, LLC). **Tier 1** (verbatim transcript of proceedings). Content summarized at §4.

**(C) Preliminary-hearing transcripts, Days 2–5 — BANKED, NOT YET READ.** Retrieved 2026-07-27 from Rev (free, un-paywalled), verbatim with named speakers and timestamps:

| Day | Chars | Timestamped turns | Status |
|---|---|---|---|
| Day 2 | 323,256 | 2,344 | banked, unread |
| Day 3 | 133,574 | 690 | banked, unread |
| Day 4 | 312,833 | 2,288 | banked, unread |
| Day 5 | 108,205 | 614 | banked, unread |

**Day 1 was not obtained** — it does not exist at the URL pattern the other four follow, and four variant slugs all returned HTTP 404. Whether Rev published a Day 1 at all is unresolved (§8 item 8). Speakers visible in the banked text include **Judge Tony F. Graf Jr.**, **Kathy Nester**, **Michael Burt**, **Richard Novak**, **Staci Visser**, **Chad Grunander**, County Attorney **Jeff Gray**, and witnesses including one **Caitlin Oliver** (Day 5). Day 4 is reported to contain FBI **Agent Davis**, a **Lance Twiggs** recorded statement, text messages, Discord chats, and a handwritten note.

**These four days are banked as primary artifacts and have NOT been read.** Nothing anywhere in this library may cite them for content until they are. They are Tier 1 when read; right now they are only *acquired*.

## 3. WHAT THE BALLISTICS MOTION ESTABLISHES

### 3.1 The ATF firearms examination — CORRECTED IN v1.1 FROM DIRECT READING

**Report identification (read directly from the rendered pages):** U.S. Department of Justice, Bureau of Alcohol, Tobacco, Firearms and Explosives, **Forensic Science Laboratory – Washington**, 6000 Ammendale Road, Beltsville, MD 20705. ANAB ISO/IEC 17025:2017 accredited. **Date of Report: September 17, 2025.** Case Number **2025-W-000401**; Reference **25-24969**; Title: **"Homicide of Charlie Kirk"**; Type of Exam: **Firearms**. Addressed to **Special Agent Derek Thorstenson**, ATF Salt Lake City. Examiner **Samantha E.A. Karner**; Technical Reviewer **Sean T. Tokay**; Administrative Reviewer **Jennifer J. Owens**, Chief, Firearms & Identification Section — all digitally signed 2025-09-17. Marked *For Official Use Only*. 4 pages.

**Exhibits submitted, as listed in the report:**

| Lab # | Item |
|---|---|
| 1 | One **Mauser, model 98, .30-06 Springfield caliber rifle, serial number 8863**, with an optical accessory |
| 2 | One .30-06 Springfield caliber **cartridge case** (fired) |
| 3–5 | Three .30-06 Springfield caliber **cartridges** (unfired) |
| 6 | One **bullet jacket fragment** and four **lead fragments** (6A–6E) |

**Results of examination — all four conclusions, verbatim:**

> The Exhibit 1 rifle was test fired and found to be in operable condition. The test fires were designated as Exhibit 1.11.
>
> Exhibit 2 consists of one (1) 30-06 Springfield caliber fired cartridge case bearing a Remington headstamp.
>
> **The Exhibit 2 cartridge case was identified as having been fired in the Exhibit 1 rifle. [Source identification]**
>
> The Exhibit 2 cartridge case and Exhibit 3 through 5 cartridges were examined for the presence of comparable toolmarks. Toolmarks were located on the exterior of the Exhibit 2 cartridge case and Exhibit 3 cartridges (scribe marks) that are consistent with being produced by engraving and/or rotary cutting tips commonly found installed in handheld rotary tools (such as a Dremel tool). These toolmarks contain marks of value for comparison if a suspect tool is located.

**The portion the defense motion quoted — accurate, but only part of the report:**

> Exhibit 6 consists of one (1) .30-caliber class deformed/damaged bullet jacket fragment (designed 6A) and four (4) lead fragments (designed 6B through 6E).
>
> The Exhibit 6A bullet jacket fragment could not be identified or excluded as having been fired from the Exhibit 1 rifle based on an agreement of all discernible class characteristics and neither sufficient agreement nor sufficient disagreement of individual characteristics. The result of the comparison was inconclusive. [Inconclusive].
>
> Firearms that produce general rifling characteristics similar to those observed on the Exhibit 6A bullet jacket fragment include numerous makes and models.
>
> The Exhibit 6B through 6E lead fragments are not suitable for microscopic comparison.

**Analyst layer — corrected.**

| Established | Confidence |
|---|---|
| **The Exhibit 2 fired cartridge case was identified as having been fired in the Exhibit 1 rifle — `source identification`** | **High** |
| The Exhibit 1 rifle is a **Mauser model 98, .30-06, s/n 8863, with an optical accessory**, test fired and **operable** | **High** |
| The Exhibit 6A bullet jacket fragment comparison to the Exhibit 1 rifle was **inconclusive** — neither identified nor excluded | **High** |
| The four lead fragments (6B–6E) are **not suitable** for microscopic comparison | **High** |
| Rifling characteristics on 6A are consistent with **numerous makes and models** of firearm | **High** |
| **Scribe/engraving toolmarks** on the Exhibit 2 case and Exhibit 3 cartridges are consistent with rotary-tool cutting tips (e.g. a Dremel) and **retain comparison value if a suspect tool is found** | **High** |
| Exhibit 6 was recovered **at autopsy**, and 6A is the **only** bullet fragment recovered | **Medium-high** — from the defense motion, not the ATF report; uncontradicted but not independently confirmed |

**What the report's own terms mean** (its Appendix, read directly):
- **`Source identification`** — "an examiner's conclusion that two toolmarks originated from the same source… all observed class characteristics are in agreement and the quality and quantity of corresponding individual characteristics is such that the examiner would not expect to find that same combination… repeated in another source." **This is the strongest positive conclusion in the framework**, and it is the conclusion reached on the cartridge case.
- **`Inconclusive`** — "all observed class characteristics are in agreement but there is insufficient quality and/or quantity of corresponding individual characteristics such that the examiner is unable to identify or exclude." **Not an exclusion.**
- The report states its conclusions "conform with the relevant Department of Justice policy on Uniform Language for Testimony and Reports."

**What this establishes, stated carefully.** The ATF **did** link the recovered fired cartridge case to the specific rifle in evidence, at the strongest available confidence level. It **did not** achieve that link from the bullet jacket fragment taken at autopsy. Both are true, and they concern **different items**. An account that reports only the inconclusive result describes the report's treatment of Exhibit 6A accurately while misrepresenting the report as a whole.

**Three limits on what any of this proves.**
1. **Firearms identification links items to a firearm, not a firearm to a person.** Nothing in this report speaks to who possessed or fired the Exhibit 1 rifle. That link, if it exists, rests on other evidence this project has not reviewed.
2. The **defense** characterizes the 6A result as "material exculpatory evidence" under *California v. Trombetta*. The State's contrary position is not in the documents held. **Recorded as a live dispute, not decided.**
3. This is one report. Reporting describes forensic evidence, surveillance video, and alleged admissions across the five-day preliminary hearing — four days of which are now banked (§2C) but **none of which has yet been read**.

### 3.2 The testing-and-alteration chronology

| Date | Event | Source |
|---|---|---|
| 2025-09-17 | ATF laboratory report issued; LCM (Light Comparison Microscopy) comparison of 6A → **inconclusive** | Ex. 2 via motion |
| 2025-11-04 | Court order (**Dkt. 261**): the Utah County Attorney's Office and any involved law enforcement agency must **notify defense counsel prior to any potentially destructive testing**; 14-day objection window; "potentially destructive" defined as likely to consume evidence or **change its character** | Motion, quoting the order |
| 2025-12-18 | ATF report disclosed to the defense | Motion |
| 2025-12-22 | **State's Notice of Intent** to conduct **VCM** (Virtual Comparison Microscopy) via an **FBI** examiner. States testing "will not destroy or consume the fragments," but **"may alter their character"** | Ex. 1 |
| 2025-12-23 | Defense asks whether a defense expert may attend or the process be videotaped. State responds the FBI's "policies, which will not change for this case, do not allow a defense examiner to be present or video taping of the examination" | Motion |
| 2026-01-09 | Motion served | Certificate of service |

**Points of substance carried by Exhibit 1 (the State's own notice), read directly:**
- To obtain a usable VCM scan, the FBI examiner **may need to fold back portions of the jacket fragment using pliers or similar gripping tools**, which "could leave marks on the surfaces."
- The FBI examiner reported that **when the fragment arrived from the ATF, a small portion was already detached**.
- **The ATF examiner may have already folded back pieces** of the fragment during the earlier LCM analysis. → **RESOLVED TO FACT 2026-07-27 (CR-E01 §3.2):** examiner Samantha Karner testified under oath that she cleaned the fragment and "peeled the petals back," using **pliers**, as documented preparation with before/after photographs in her case file. The hedge is retired.
- The FBI acknowledges the item is **"fragile"** and that "it is possible that additional pieces of the fragment may inadvertently become detached during the VCM analysis."
- The State also intends **metallurgical testing** on at least one of the four lead fragments.

**Analyst note.** The evidentiary significance is narrow but real: the sole comparable projectile fragment in a capital case has already been physically manipulated once, and further manipulation was proposed. Whether that manipulation was proper, and whether the court permitted it, **is not established by the documents held** — the ruling on this motion was not obtained (§8 item 4). The defense's constitutional argument (Trombetta/Youngblood federally; *State v. Tiedemann* and *State v. DeJesus* under Utah due process; URCP 16) is recorded as **the defense's argument**, not as law applied to this case.

## 4. THE OCTOBER 24, 2025 SEALED MOTION HEARING

97-page redacted transcript, read. **Subject matter is procedural, not forensic** — a scan for `bullet`, `rifle`, `DNA`, `ballistic`, `autopsy`, `jacket` returns **zero** hits; `sheriff` returns 109.

- The hearing concerned **shackling/restraints and courtroom attire** — including a defense request that Robinson's hand be freed so he could take notes — with the **Utah County Sheriff's Office separately represented** by Benjamin C. Van Noy of the Utah County Attorney's Office, distinct from the prosecution team.
- Judge Graf stated he would take the weekend and issue an **oral ruling Monday at 1:00**.
- On the **booking photo**: the State represented that although the photo originated with the sheriff, "it was not the sheriff's office that released that to the media. That was a different law enforcement agency that did that… It was shared with that law enforcement agency under the government sharing provisions under **GRAMA**," and that the sheriff's office "was very concerned that it had been made public." **Recorded as the State's representation on the record — attributed, not adopted.** The releasing agency is not named in the transcript.

**Value to this library:** modest but real. It documents the separate posture of the Sheriff's Office in this case and puts a named, on-the-record account of the booking-photo release into the file — a discrete provenance question that had no primary source before.

## 5. DOCKET AND PARTY FACTS ESTABLISHED

- **Court:** Fourth Judicial District Court, Provo Department, Utah County. **Judge Tony F. Graf, Jr.**
- **Prosecution:** Utah County Attorney **Jeffrey S. Gray** (#5852); Deputy County Attorneys **Chad E. Grunander** (#9968), **Ryan McBride** (#13079), **Lauren Hunt** (#14682), **David Sturgill** (#7995), **Christopher D. Ballard** (#8497). 100 East Center, Suite 2100, Provo.
- **Defense:** **Kathryn N. Nester** (UT #13967); **Staci Visser** (UT #14358); **Richard G. Novak** and **Michael N. Burt**, both *pro hac vice* — Burt and Novak are capital-defense specialists, consistent with the death-penalty posture.
- **Utah County Sheriff's Office:** separately represented by **Benjamin C. Van Noy**.
- **Docket landmarks:** **Dkt. 61** = Defendant's Formal Request for Discovery under URCP 16 + Rule 404(b) notice, filed "early on." **Dkt. 261** = the 2025-11-04 destructive-testing notice order. **The docket therefore exceeded 261 entries by 2025-11-04** — a useful scale marker for what a full docket pull would involve.

## 6. NEW REGISTER ENTRY — D-48

*(Grep-verified: highest existing D-number before this assignment is D-47. The lone "D-48" strings on disk are the forward-looking notes in BOC-ROUTE §9 and BOC-AUDIT-2026-07-27 — not assignments. The hazard fired as predicted; the notes were read, not just matched.)*

| # | Subject | Claim (recording layer) | Record (analyst layer) | Sources | Status |
|---|---|---|---|---|---|
| **D-48** | Owens' Ep 319 ATF claim, **as published in the episode description** | *Candace* Ep 319, "PROVE ME WRONG: Tyler Robinson Is A Patsy." (published **2026-04-01**). Owens' own published episode description: "The internet exploded because **the ATF in the Tyler Robinson case cannot connect the gun to him.** We wanted to make sure we took our time and read through the court filings…" | The ATF report of 2025-09-17 records **`source identification`** — the framework's strongest positive conclusion — linking the Exhibit 2 fired cartridge case to the **Exhibit 1 rifle**. The **`inconclusive`** result applies to a *different item*, the Exhibit 6A bullet jacket fragment | Owens' published RSS description (BOC-ROUTE §3, retrieved 2026-07-27) vs. §3.1, read directly | **RE-RESOLVED A SECOND TIME (v1.3) — SPLIT.** v1.0 resolved FOR Owens; v1.1 resolved AGAINST. **Both were too simple.** The claim is **substantially TRUE of ATF *ballistics*** and **FALSE of the ATF's work as a whole**, because the ATF also did the **DNA** testing. See §6.1 |

### 6.1 D-48, third resolution — the split (v1.3, from adversarial re-read)

Day 4's testimony (CR-E02) supplied two facts that neither earlier resolution had:

1. **The source-identified cartridge case was recovered from inside the rifle's chamber** (CR-E02 §4). A fired case found *in* a rifle is expected to identify to that rifle. **On the record read, no cartridge case was recovered at the perch or elsewhere at the scene**, and the only projectile evidence from the body — fragment 6A — was **inconclusive**. **So the ATF firearms examination did not link this rifle to the shooting.** On *ballistics*, Owens' claim is substantially **correct**, and v1.1's flat resolution against her was **wrong**.
2. **But the ATF also performed the DNA testing.** Faumuina identified Exhibit 30 as "the **ATF report**… regarding the **DNA testing on the gun** and cartridge… case and cartridges," and read likelihood ratios of "**at least one trillion** times more likely" (trigger and trigger guard) and "**6.28 billion** times more likely" (the scope's optical accessory) for Robinson as a contributor. That is ATF work, and it is precisely what connects **the gun to him**.

**Resolution, stated narrowly.** Read as a statement about **ATF ballistics**, the claim is **substantially accurate** — logged as a confirmation **FOR** Owens, and a more substantial one than v1.0 supposed, since it survives contact with the full firearms report. Read as a statement about **what the ATF established in this case**, it is **false**, because the ATF's DNA results are strongly inculpatory on the very question of connecting the gun to Robinson. **Which reading her episode advances is unknown** — Ep 319 remains uninventoried, and this entry still grades only the published description.

**Caveats carried forward.** The DNA likelihood ratios were **captured incomplete** and are unusable until Exhibit 30 is read (CR-E02 §5.1); a likelihood ratio without its alternative hypothesis states nothing. The chamber-case inference is **Medium-high**, not certain. **This resolution is therefore itself provisional**, and the honest summary is that the firearms and DNA evidence point in different directions and must never be collapsed into one claim about "the ATF."

**Why v1.0 got this wrong.** v1.0 compared Owens' description against the *only* part of the ATF report then legible — the part the defense motion quoted, which concerned the bullet fragment because that was the motion's subject. On that partial record her description looked accurate. Against the full report it does not. **The error was this file's, not a claimant's**, and it is corrected here rather than quietly dropped.

**Steelman — applied before resolving, and it materially limits the resolution.** Three readings favor Owens:

- **(a) If she meant the autopsy bullet fragment specifically**, she is **correct** — that comparison was inconclusive, and the ATF genuinely could not tie that fragment to the rifle. **Logged as a confirmation FOR Owens on that leg.**
- **(b) "Connect the gun to *him*"** — read strictly, a firearms examination never links a weapon to a *person*; it links toolmarks to a firearm. On that reading the statement is trivially true of *any* firearms report and carries no information, though the framing implies a failed attempt where none was made.
- **(c) Most importantly: this entry grades a one-sentence promotional description, not the episode.** The description also says she "took our time and read through the court filings," and the episode runs roughly 68 minutes. **It is entirely possible Owens discussed the cartridge-case identification on air.** Nothing here establishes that she did or did not.

**What resolves, precisely.** The **published description**, standing alone, states that the ATF "cannot connect the gun" while omitting that the ATF positively identified the fired cartridge case to that gun. As a characterization of the report, that is **materially incomplete and misleading** — resolved **against**. **What does not resolve:** whether the episode itself is misleading; the "patsy" thesis; and anything about gun-to-person linkage, on which this report is silent.

**Consequence — Ep 319 is promoted to the top of the inventory queue.** It is now the single most decision-relevant episode in the corpus, because a Tier 1 document exists against which its central factual claim can be graded line by line. Whether D-48 ultimately resolves for or against Owens *as a broadcaster* depends on what she actually said, and that is cheap to determine.

**Pattern note — v1.0's version of this paragraph is withdrawn.** v1.0 read D-48 as a case claim that "checked out" and warned against assuming otherwise. On the corrected record the standing pattern is **undisturbed**: the checkable anchor (an inconclusive ATF result on one item) is real, while the framing built on it — that the ATF could not connect the gun — does not survive contact with the source. **Anchor true, connection overstated.** The caution in v1.0 was nonetheless worth stating and is retained in weaker form: case claims rest on a better-documented evidentiary base than actor-context claims, so each still needs grading on its own record rather than by pattern.

## 7. FINDINGS

1. **The ATF positively identified the recovered fired cartridge case as having been fired in the Exhibit 1 rifle — `source identification`, the strongest positive conclusion in the DOJ framework.** **High.** §3.1. *(New in v1.1; absent from v1.0 and the reason for the correction.)*
2. **The bullet jacket fragment recovered at autopsy (6A) was inconclusive** — neither identified nor excluded — with rifling characteristics common to numerous makes and models; the four lead fragments (6B–6E) are unsuitable for comparison. **High.** §3.1.
3. **The weapon in evidence is a Mauser model 98, .30-06 Springfield, serial 8863, with an optical accessory, test fired and operable.** **High.** §3.1.
4. **Scribe/engraving toolmarks consistent with a rotary tool (e.g. a Dremel) are present on the fired cartridge case and on the unfired Exhibit 3 cartridges**, and retain comparison value if a suspect tool is located. **High.** §3.1. *(This is the ATF's documentary correlate of the "bullet engraving" thread; it bears directly on the Day 4 hearing testimony now banked but unread.)*
5. **The bullet fragment had already been physically altered before further testing was proposed** — a portion was detached on arrival at the FBI, and **the ATF examiner peeled the petals back with pliers**, confirmed under oath (CR-E01 §3.2). **High.** §3.2.
5a. **The `inconclusive` result rests on data insufficiency, not dissimilarity** — marks of value were present and areas of agreement observed; damage destroyed the comparable surface ("almost like missing data points"). **High** as sworn testimony; the expert dispute is not adjudicated. **CR-E01 §3.3 — this materially qualifies finding 2 and should be read with it.**
6. **The FBI declined both defense-expert observation and videotaping** of the proposed VCM examination. **High** (quoted in a signed filing). §3.2.
7. **D-48 re-resolved AGAINST Owens' published episode description** — which omits the positive identification — with the **episode itself expressly not resolved against**, and one leg (the bullet-fragment result) confirmed **for** her. **v1.0's contrary resolution is withdrawn.** §6.
8. **Selective quotation by an adversarial party is a distinct sourcing hazard** — accurate as to the words quoted, unreliable as to the source document as a whole. Established the hard way, in this file, within one session. **This is the finding with the longest reach.** §0.
9. **The court record is an open, free acquisition channel** despite XChange's paywall — filings are public, a seal motion was denied, and mirrors plus transcript services are reachable. §1.
10. **The Oct 24, 2025 hearing is procedural** (restraints, attire, booking-photo provenance), not forensic — with a named on-record account of how the booking photo reached the media. **High** as to what was said; the account itself is attributed, not adopted. §4.

## 8. OPEN ITEMS / ACQUISITION PATHS

1. ~~**Read Exhibit 2 (the ATF report) directly**~~ — **CLOSED 2026-07-27.** poppler installed with authorization; pages rendered and read; §3.1 rewritten and **D-48 reversed** as a result. The single highest-yield hour of the session.
2. **READ the four banked preliminary-hearing days** (§2C) — **STARTED 2026-07-27.** The **Karner testimony from Day 4 is now read and inventoried at CR-E01** (and yielded **D-49**). Still unread: the rest of Karner (incl. **any State examination of her** — the largest gap), **Sergeant Faumuina** (330 turns), **FBI Agent Davis** (105 turns), the Twiggs statement, texts, Discord and handwritten note, and **Days 2, 3, 5 entirely**. ~800k characters remain.
3. **Inventory Ep 319** — promoted to top of the corpus queue by §6. A Tier 1 document now exists against which its central factual claim can be graded, and the D-48 resolution against the *episode* turns entirely on what she actually said on air.
3. **DocumentCloud project 224251** — needs an interactive browser session (403/JS-gated to automation). Likely the fastest route to a full filings inventory.
4. **The ruling on this motion** — was the VCM testing permitted, barred, or conditioned? Not established. Decisive for whether the fragment survives in comparable condition.
5. **The briefing set** — State's opening (2026-07-28), defense response (2026-08-11), State's reply (2026-08-18), oral argument (2026-09-01). These will state both sides' evidence theory in their own words. **Time-sensitive; acquire as filed.**
6. **The State's response to this motion**, if any — the State's position on whether the fragment is exculpatory is currently absent from the record held, which is why §3.1's characterization dispute is left open.
7. **Utah XChange** — remains excluded pending a user decision on the fee.

8. **Day 1 of the preliminary hearing** — not found. Four URL-slug variants returned 404; whether Rev published a Day 1 is unresolved. Alternatives: Rev's news index, the Utah Courts press notice for the hearing (`legacy.utcourts.gov`, 2026-07-06), or the YouTube livestream recording of the proceedings.
9. **Utah Courts official press notice** on the preliminary hearing (2026-07-06) — a Tier 2 institutional source surfaced but not retrieved.

**File-placement note — RESOLVED 2026-07-27.** v1.0 sat in `files - Kirk assassination questions` and flagged the question. **This file and its artifacts now live in the topic folder `files - Court record`**, created for the purpose, because the court record cuts across ballistics, DNA, arrest chronology, and the Losee-building questions and would otherwise be scattered across four folders. Those four folders should point here for anything primary-record-derived rather than duplicating it.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-27 | Initial file. First acquisition pass on the primary court record in Case No. 251403576. Access-path map established: **XChange paywalled and excluded** (no account created, no fee incurred); outlet mirrors open; Rev transcripts open but deliberately not ingested; DocumentCloud bot-gated. Two Tier 1 documents acquired, banked, and byte-verified with SHA-256: the defense bullet-jacket motion (served 2026-01-09, 19pp + 2 exhibits) and the redacted 2025-10-24 sealed-motion-hearing transcript (97pp). **Headline finding:** the ATF report of 2025-09-17 records the comparison of the sole recovered .30-caliber bullet jacket fragment against the Exhibit 1 rifle as **INCONCLUSIVE** — neither identified nor excluded — with the four lead fragments unsuitable for comparison. Tiering stated precisely as **T1 quoting T1**: Exhibit 2 is banked but its text is not machine-extractable (Type3 font, no `/ToUnicode`), so the report is known through the motion's verbatim quotation, not direct reading (§8 item 1). Testing-and-alteration chronology reconstructed from the State's own notice (§3.2), incl. the already-detached portion, the possible prior ATF fold-back, and the FBI's refusal of defense observation or videotaping. **D-48 assigned and RESOLVED verifying FOR Owens** on the narrow proposition that the ATF could not connect the gun to Robinson — a case claim of hers that checks out against the primary record — while the "patsy" characterization is neither established nor addressed, and the episode remains uninventoried. Qualification logged: the project's anchors-verify/connections-fail pattern was derived from actor-context claims and should not harden into an expectation about case claims. Oct 24 hearing characterized as procedural (restraints, attire, booking-photo provenance via GRAMA sharing — attributed to the State, not adopted). Docket scale marker recorded (Dkt. 261 by 2025-11-04). Case posture date-stamped 2026-07-27: **no bindover**. |
| **1.1** | **2026-07-27** | **MATERIAL CORRECTION — v1.0's headline finding was incomplete and D-48 was resolved wrongly on it.** With the user's authorization, `poppler` was installed and Exhibit 2 (the ATF report) was **rendered and read directly**, closing v1.0's open item #1 within the same session. The direct reading shows the defense motion quoted the report **accurately but selectively** — only the portion about its own subject, the bullet jacket fragment. The full report also records **`source identification`** (the DOJ framework's strongest positive conclusion) linking the **Exhibit 2 fired cartridge case to the Exhibit 1 rifle** — a Mauser model 98, .30-06, s/n 8863, test fired and operable — plus **scribe/engraving toolmarks** consistent with a rotary tool on the fired case and the unfired Exhibit 3 cartridges, retaining comparison value if a suspect tool is found. Report metadata now recorded (ATF FSL-Washington, Beltsville MD; case 2025-W-000401; ref 25-24969; examiner Samantha E.A. Karner, technical reviewer Sean T. Tokay, administrative reviewer Jennifer J. Owens; all signed 2025-09-17), along with the Appendix's own definitions of `source identification`, `source exclusion`, and `inconclusive`. **D-48: v1.0's resolution FOR Owens is WITHDRAWN and re-resolved AGAINST her published episode description**, which omits the identification and so misrepresents the report as a whole — while the **episode itself is expressly NOT resolved against** (a 68-minute broadcast may well have covered it; unknown), and the bullet-fragment leg remains **confirmed for her**. Ep 319 promoted to top of the inventory queue as the decisive artifact. Tiering upgraded T1-quoting-T1 → **T1 read directly**; §0 gains a standing rule on **selective quotation by an adversarial party** as a sourcing hazard, sibling to the V-10 lesson. Sections rewritten: header/headline, §0, §1 (machine-readability resolved; artifacts extended), §3.1 (rewritten), §6 (re-resolved), §7 (renumbered, ten findings), §8 (items 1 closed, 2–3 and 8–9 added). **Also this revision:** preliminary-hearing **Days 2–5 acquired and banked** (§2C — ~878k chars, ~5,900 turns, **unread**; Day 1 not found at four URL variants), and the file **moved to the new topic folder `files - Court record`** with its artifacts, resolving v1.0's open placement question. |
| 1.2 | 2026-07-27 | Cross-referenced to **CR-E01** (Karner's sworn Day 4 testimony), which **corroborates §3.1 at source**. Two updates in place: §3.2's hedge that the ATF examiner "may have already folded back pieces" is **resolved to fact** — Karner testified she peeled the petals back with **pliers**, with before/after photographs in her case file; and a new finding **5a** records that the `inconclusive` result rests on **data insufficiency, not dissimilarity** (marks of value present, areas of agreement observed, damage described as "missing data points"), which materially qualifies finding 2 and must be read with it. §8 item 2 updated: Day 4's Karner testimony read; the rest of Day 4 and Days 2/3/5 (~800k chars) still unread, with **any State examination of Karner** flagged as the largest remaining gap. **D-49 was assigned in CR-E01**, not here; register now D-1–D-49. No finding in this file was reversed by CR-E01. |
| **1.3** | **2026-07-27** | **SECOND CORRECTION — from the adversarial pass (CR-AUDIT-2026-07-27 §2.1).** This file's headline **over-weighted the `source identification`**. Day 4 testimony establishes the identified cartridge case was **recovered from inside the rifle's chamber**, and that on the record read **no cartridge case was recovered at the perch or elsewhere at the scene**; the only projectile evidence from the body remained **inconclusive**. A fired case found inside a rifle is expected to identify to that rifle, so **the ATF firearms examination did not link this rifle to the shooting.** **D-48 accordingly re-resolved a second time — its third resolution today — as an explicit SPLIT** (new §6.1): the claim is **substantially TRUE of ATF ballistics** (a confirmation FOR Owens, and a stronger one than v1.0 supposed) and **FALSE of the ATF's work as a whole**, because the ATF also performed the **DNA** testing that produced likelihood ratios of "at least one trillion" (trigger/trigger guard) and "6.28 billion" (scope) for Robinson as a contributor. Which reading Ep 319 advances is still unknown; the episode remains uninventoried. Both caveats carried: the DNA figures were **captured incomplete** and are unusable until Exhibit 30 is read, and the chamber-case identity is a **Medium-high inference**, so this resolution is itself provisional. **Standing rule extended** (CR-AUDIT §4): a forensic report is reliable as to the items it examined and **silent about their provenance** — provenance is a separate verification act. Both of the day's material errors were instances of that one failure, and neither was catchable from the document in hand. |
