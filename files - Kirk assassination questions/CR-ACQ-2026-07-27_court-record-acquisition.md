# CR-ACQ-2026-07-27 — Court Record Acquisition: State v. Robinson, Case No. 251403576

**File ID:** CR-ACQ-2026-07-27
**Scope:** first acquisition pass on the **primary court record** in *State of Utah v. Tyler James Robinson*. Establishes the access-path map (what is free, what is paywalled, what is bot-gated), banks the documents obtained, and records what they establish. This is the project's first file built on **Tier 1 court filings read directly** rather than on reporting about them.
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo Department, Utah County — Honorable **Tony F. Graf, Jr.** presiding. **Tyler Robinson is presumed innocent.** As of **2026-07-27** he has **not been bound over for trial**: the preliminary hearing concluded 2026-07-10 with the probable-cause ruling reserved for briefing (State's opening brief 2026-07-28, defense response 2026-08-11, State's reply 2026-08-18, oral argument 2026-09-01). Every allegation recorded below is an allegation; every defense assertion is a defense assertion. Nothing here is adopted.
**Prepared:** July 27, 2026
**Status:** v1.0

**Headline result:** The ATF's firearms examination of the **only bullet jacket fragment recovered in this case** was **INCONCLUSIVE** — the fragment "could not be identified or excluded as having been fired from" the rifle the State seeks to connect to Robinson. That is not a defense characterization; it is the operative language of the ATF laboratory report dated 2025-09-17, quoted verbatim in a signed court filing and attached to it as an exhibit. This single fact anchors a great deal: it is the documentary basis beneath Candace Owens' Ep 319 case claim (registered and resolved at **D-48**, §6), and it is the first hard forensic datum this library holds on the shot itself.

**Second result, methodological:** the access-path map is now known. Utah XChange is **paywalled** and is excluded. But the filings in this case are **public** — a motion to seal was denied — and are reachable free through outlet mirrors and transcript services. **The court record is an open acquisition channel for this project.**

---

## 0. Sourcing framework (project standard)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements (incl. named first-person statements by principals)
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material

**"T1 via T3"** marks primary-document content known only through reporting. Confidence grades trace to a verification act by this project; **"— (checkable)"** marks the verifiable-but-not-yet-verified, never counted as findings.

**One tiering nuance is load-bearing in this file and is stated up front.** The ATF report (Exhibit 2) is **banked in this library as a PDF** but its text **cannot be machine-extracted** (§1). Its operative language is therefore known to this project through the defense motion's **verbatim quotation** of it — that is a primary court filing, signed and served, quoting a primary laboratory report. This is recorded as **T1 quoting T1**, which is stronger than "T1 via T3" but is **not** the same as having read the report directly. It is not silently promoted. Direct reading is §8 item 1.

## 1. ACCESS PATH (caveats first)

**Route map established 2026-07-27:**

| Route | Status | Note |
|---|---|---|
| **Utah XChange** (`xchange.utcourts.gov`) | **PAYWALLED — excluded** | $10 one-time-use account (+$0.35/search, $1.00/document), or $25 setup + $40/month. Free access exists only at physical courthouse terminals. **No account was created and no fee was incurred.** This is a user spending decision, not one this project takes unilaterally |
| **Outlet-mirrored filings** | **OPEN — used** | Both documents below were retrieved this way (HTTP 200, curl with browser user-agent) |
| **Rev transcripts** | **OPEN — verified, not yet ingested** | Preliminary-hearing transcripts are freely readable. Day 4 (2026-07-10) confirmed present and un-paywalled. **Deliberately not ingested this session** — see §8 item 2 |
| **DocumentCloud** project 224251 ("Charlie Kirk Murder Case and Tyler Robinson") | **BOT-GATED** | API returned HTTP 403 to curl; the project page is JS-rendered so WebFetch sees the shell but no document list. Needs an interactive browser session |
| Direct court docket | **NOT OBTAINED** | No free public docket route found. The docket's existence and partial contents are inferred from filing references (§5) |

**Machine-readability caveat — this determines what §3 can claim.** The motion PDF's body (pp. 1–19) and Exhibit 1 (pp. 20–24) extract cleanly with `pypdf`. **Exhibit 2 — the ATF report itself, pp. 25–29 — does not.** Its pages are drawn with a **Type3 font carrying no `/ToUnicode` map**, so extraction yields only null glyphs (`/0 /0 /0…`). The embedded images on those pages are logos, seals, and small figures, not full-page scans, so image extraction does not recover the text either. Reading Exhibit 2 directly requires **rendering the pages to images**, which needs `poppler` (`pdftoppm`), **not installed on this machine**. No system change was made to work around this.

**Retrievals and failures logged (all 2026-07-27):**
- Ballistics motion PDF — **success**, HTTP 200, 1,369,739 bytes, 29 pages.
- Redacted Oct 24 hearing transcript PDF — **success**, HTTP 200, 1,060,521 bytes, 97 pages.
- DocumentCloud API + project page — **403 / JS-gated**, no document list obtained.
- Utah XChange — **not attempted** (paywalled by design, see above).

**Artifacts banked**, byte-verified, in `CR-ACQ-2026-07-27_court-record-artifacts/` alongside this file, with SHA-256 for provenance:
- `tyler-robinson-ballistics-motion.pdf` — `b2395846d144924f683218a69e1b17e01ac5e3cd48ba7a6dd1ef6deb99f17f36`
- `tyler-robinson-redacted-hearing-transcript.pdf` — `7a891b006d5c7128a5e120a469461855d9121239189ca3011625036949e16dc6`
- plus extracted text (`…-ballistics-motion.txt`, `oct24_clean.txt`) for searchability. **The PDFs are authoritative; the .txt files are convenience derivatives** and, for Exhibit 2, are known-incomplete.

**Quotation note:** the filings are quoted as written, including their own typographical errors (e.g. the caption's "THISE VIDENCE"; a body reference to "January 12, 2025" where 2026 is meant; "two three separate types"). Errors are the source's, preserved rather than silently corrected.

## 2. DOCUMENTS ACQUIRED

**(A) Defendant's Motion re: bullet jacket fragment** — *Defendant's Motion For An Order Prohibiting Any Further Alteration Or Testing Of A Bullet Jacket Fragment Pending The Outcome Of This Motion, And Permitting A Defense Expert To Examine And Photograph This Evidence Before It Is Further Altered Or Destroyed, Or, In The Alternative, Permitting Either Defense Expert Observation Of Any Further Alteration Or Testing Of This Evidence, Or Video Recording Of Such Alteration And Testing, and Memorandum In Support.* 19 pages + 2 exhibits (29 PDF pages). Certificate of service: **served 2026-01-09** via the court's electronic filing system. **Tier 1.**

- **Counsel for Robinson:** Kathryn N. Nester (Nester Lewis PLLC); Richard G. Novak (*pro hac vice*); Michael N. Burt (*pro hac vice*); Staci Visser (Brown, Bradshaw & Moffat).
- **Exhibit 1** — *State's Notice Of Intent To Conduct Non-Destructive Testing*, served **2025-12-22**, 4 pages. Signed by Utah County Attorney **Jeffrey S. Gray** with Deputy County Attorneys Grunander, McBride, Hunt, Sturgill, and Ballard. **Readable — Tier 1, read directly.**
- **Exhibit 2** — **ATF laboratory report dated 2025-09-17**, disclosed to the defense 2025-12-18. **Banked but not machine-readable** (§1).

**(B) Redacted Transcript of Sealed Motion Hearing, 2025-10-24** — 97 pages, before Judge Graf, Fourth District Court, 137 North Freedom Boulevard, Provo. Reported by Phoebe S. Moorhead, RDR, CRR, UT CSR (Noteworthy Reporting, LLC). **Tier 1** (verbatim transcript of proceedings). Content summarized at §4.

## 3. WHAT THE BALLISTICS MOTION ESTABLISHES

### 3.1 The ATF firearms examination — the operative finding

Quoted in the motion from Exhibit 2, the ATF report of **2025-09-17**:

> Exhibit 6 consists of one (1) .30-caliber class deformed/damaged bullet jacket fragment (designed 6A) and four (4) lead fragments (designed 6B through 6E).
>
> The Exhibit 6A bullet jacket fragment could not be identified or excluded as having been fired from the Exhibit 1 rifle based on an agreement of all discernible class characteristics and neither sufficient agreement nor sufficient disagreement of individual characteristics. The result of the comparison was inconclusive. [Inconclusive].
>
> Firearms that produce general rifling characteristics similar to those observed on the Exhibit 6A bullet jacket fragment include numerous makes and models.
>
> The Exhibit 6B through 6E lead fragments are not suitable for microscopic comparison.

**Analyst layer — what this does and does not establish.**

| Established | Confidence |
|---|---|
| The recovered projectile evidence consists of **one** .30-caliber-class bullet jacket fragment (6A) plus four lead fragments (6B–6E), all recovered **at autopsy** | **High** |
| The ATF comparison of 6A against the Exhibit 1 rifle returned **inconclusive** — neither identification nor exclusion | **High** |
| The four lead fragments are **not suitable** for microscopic comparison | **High** |
| Rifling characteristics observed on 6A are consistent with **numerous makes and models** of firearm | **High** |
| Per the motion, this is the **only** bullet fragment recovered in the case ("there is only one bullet fragment recovered in this case") | **Medium-high** — a defense assertion in a signed filing, uncontradicted in the documents held, but not independently confirmed |

**What "inconclusive" does not mean.** It is not an exclusion, and it is not affirmative exculpatory proof. It means the examiner could neither match nor rule out. The **defense** characterizes it as "material exculpatory evidence" under *California v. Trombetta*; the State's contrary position is not in the documents this project holds. **That characterization dispute is unresolved and is recorded as a dispute, not decided here.** Nor does this speak to the strength of the State's case overall: reporting describes forensic evidence, surveillance video, and alleged admissions presented across the five-day preliminary hearing, **none of which this project has reviewed**.

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
- **The ATF examiner may have already folded back pieces** of the fragment during the earlier LCM analysis.
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
| **D-48** | Owens' Ep 319 ATF claim | *Candace* Ep 319, "PROVE ME WRONG: Tyler Robinson Is A Patsy." (published **2026-04-01**). Owens' own published episode description: "The internet exploded because **the ATF in the Tyler Robinson case cannot connect the gun to him.** We wanted to make sure we took our time and read through the court filings…" | The ATF report of 2025-09-17 finds the sole recovered bullet jacket fragment "could not be identified or excluded as having been fired from the Exhibit 1 rifle… The result of the comparison was inconclusive." | Owens' published RSS description (BOC-ROUTE §3, retrieved 2026-07-27) vs. §3.1 above | **RESOLVED — the narrow claim VERIFIES. Logged as a confirmation FOR Owens** under the both-directions rule. The "patsy" characterization does **not** follow and is not resolved here |

**Analysis.** On the specific proposition that the ATF could not connect the recovered projectile evidence to the rifle, Owens is **accurate**, and the primary record confirms it. Her stated method — "we took our time and read through the court filings" — also appears, on this point, to be what actually happened: this is a claim traceable to a real document saying what she says it says.

**What does not follow.** "Inconclusive" is not "excluded," and a single inconclusive ballistics comparison is not a basis for the episode title's "Patsy." Those are separate propositions requiring separate evidence, and the episode itself remains **uninventoried** — this entry rests on Owens' published description, exactly the basis permitted at BOC-ROUTE §1 and used for D-47, and on nothing else.

**Pattern significance — and a genuine qualification to the project's standing finding.** The standing pattern has been that Owens' *checkable anchors* verify while her *asserted connections* do not. D-48 fits that shape, but with a sharper edge than usual: here the verified anchor is not a peripheral calendar detail but a **materially load-bearing forensic fact**. The project should be careful not to let a pattern derived from actor-context claims harden into an expectation about case claims, which draw on a different and far better-documented evidentiary base. **On this record, a case claim of hers checked out.** That is worth stating plainly, and it is exactly what the both-directions rule exists to force.

## 7. FINDINGS

1. **The ATF ballistics comparison on the sole recovered bullet jacket fragment was inconclusive** — neither identification nor exclusion, with rifling characteristics common to numerous makes and models. **High.** §3.1.
2. **The four recovered lead fragments are unsuitable for microscopic comparison.** **High.** §3.1.
3. **The fragment had already been physically altered before the State proposed further testing** — a portion was detached on arrival at the FBI, and the ATF examiner may have folded back pieces during the earlier LCM analysis. **High** (the State's own notice says so). §3.2.
4. **The FBI declined both defense-expert observation and videotaping** of the proposed VCM examination. **High** (quoted in a signed filing). §3.2.
5. **D-48 RESOLVED, verifying FOR Owens** on the narrow ATF proposition; the "patsy" characterization neither established nor addressed. §6.
6. **The court record is an open, free acquisition channel** despite XChange's paywall — filings are public, a seal motion was denied, and mirrors plus transcript services are reachable. **This is the methodological finding with the longest reach.** §1.
7. **The Oct 24, 2025 hearing is procedural** (restraints, attire, booking-photo provenance), not forensic — with a named on-record account of how the booking photo reached the media. **High** as to what was said; the account itself is attributed, not adopted. §4.

## 8. OPEN ITEMS / ACQUISITION PATHS

1. **Read Exhibit 2 (the ATF report) directly** — the one gap between "T1 quoting T1" and "T1 read directly" on the file's headline finding. Requires rendering pp. 25–29 to images: `brew install poppler`, then `pdftoppm -png -r 200 -f 25 -l 29`. **A user decision (system change); trivial once approved.**
2. **Rev preliminary-hearing transcripts, Days 1–5** — free and confirmed open; Day 4 (**2026-07-10**) verified to contain FBI **Agent Davis** testimony, a **Lance Twiggs** recorded statement, text messages (Ex. 16.1), Discord chats (Ex. 16.2), and a handwritten note found under Robinson's keyboard (Ex. 16.3). **Deliberately not ingested this session**: partial ingestion of a five-day hearing would create a false impression of coverage. Take all five or none. **This is the single highest-value remaining acquisition in the project**, and it feeds `lance-twiggs-comprehensive-profile.md` directly.
3. **DocumentCloud project 224251** — needs an interactive browser session (403/JS-gated to automation). Likely the fastest route to a full filings inventory.
4. **The ruling on this motion** — was the VCM testing permitted, barred, or conditioned? Not established. Decisive for whether the fragment survives in comparable condition.
5. **The briefing set** — State's opening (2026-07-28), defense response (2026-08-11), State's reply (2026-08-18), oral argument (2026-09-01). These will state both sides' evidence theory in their own words. **Time-sensitive; acquire as filed.**
6. **The State's response to this motion**, if any — the State's position on whether the fragment is exculpatory is currently absent from the record held, which is why §3.1's characterization dispute is left open.
7. **Utah XChange** — remains excluded pending a user decision on the fee.

**File-placement note.** This file sits in `files - Kirk assassination questions` because that is the main-case hub, but the court record spans ballistics, DNA, arrest chronology, and the Losee-building questions alike. **If the court-record program proceeds past this first pass, it should get its own topic folder** (`files - Court record`) rather than being distributed across four existing ones. Flagged, not decided.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-27 | Initial file. First acquisition pass on the primary court record in Case No. 251403576. Access-path map established: **XChange paywalled and excluded** (no account created, no fee incurred); outlet mirrors open; Rev transcripts open but deliberately not ingested; DocumentCloud bot-gated. Two Tier 1 documents acquired, banked, and byte-verified with SHA-256: the defense bullet-jacket motion (served 2026-01-09, 19pp + 2 exhibits) and the redacted 2025-10-24 sealed-motion-hearing transcript (97pp). **Headline finding:** the ATF report of 2025-09-17 records the comparison of the sole recovered .30-caliber bullet jacket fragment against the Exhibit 1 rifle as **INCONCLUSIVE** — neither identified nor excluded — with the four lead fragments unsuitable for comparison. Tiering stated precisely as **T1 quoting T1**: Exhibit 2 is banked but its text is not machine-extractable (Type3 font, no `/ToUnicode`), so the report is known through the motion's verbatim quotation, not direct reading (§8 item 1). Testing-and-alteration chronology reconstructed from the State's own notice (§3.2), incl. the already-detached portion, the possible prior ATF fold-back, and the FBI's refusal of defense observation or videotaping. **D-48 assigned and RESOLVED verifying FOR Owens** on the narrow proposition that the ATF could not connect the gun to Robinson — a case claim of hers that checks out against the primary record — while the "patsy" characterization is neither established nor addressed, and the episode remains uninventoried. Qualification logged: the project's anchors-verify/connections-fail pattern was derived from actor-context claims and should not harden into an expectation about case claims. Oct 24 hearing characterized as procedural (restraints, attire, booking-photo provenance via GRAMA sharing — attributed to the State, not adopted). Docket scale marker recorded (Dkt. 261 by 2025-11-04). Case posture date-stamped 2026-07-27: **no bindover**. |
