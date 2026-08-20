# ZINN-ACQ-2026-08-20 — Acquisition: the two George Zinn probable-cause affidavits (Q-153)

**File ID:** ZINN-ACQ-2026-08-20 · **Scope:** execution of Q-153 (the DocumentCloud platform sweep for Zinn material) and acquisition of its yield: two probable-cause affidavits. Facial reading of the obstruction PCA only; **the sexual-exploitation PCA's narrative is deliberately unread** (§4). · **Case context:** George Hodgson Zinn was prosecuted **separately** from *State of Utah v. Robinson*, No. 251403576; his record is not in the Robinson docket (ZINN-REVIEW-2026-08-17). · **Prepared:** 2026-08-20 · **Status:** **v1.0 · `[PROVISIONAL]`** — no independent verification cycle has run on this file.

**Sourcing framework (project standard):** Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries a URL and a retrieval date.

## §1 · Access-path caveats — first

- **Provenance is zero-of-three court provenance (third-party upload).** Both documents were uploaded to DocumentCloud by **USA Today** (org 61), user **Nick Penzenstadler** (a named reporter acting in a professional capacity — recorded per the T3 convention), on **2025-09-16** — the day the Robinson charging documents also became public. They carry the PCA form's own attestation (`/S/` officer signature under criminal penalty), no clerk file-stamp, no docket caption.
- 🚨 **The hash trap fired on BOTH documents, exactly as CR-ACQ-2026-08-13 documented for the defence brief:** the PDF DocumentCloud *serves* is a re-render whose SHA-1 does **not** match the API's `file_hash` field. Both hash sets are recorded in §2; **future integrity comparisons must use the API's `file_hash`, never the served bytes.**
- Retrieved by direct local fetch, **2026-08-20**. The DocumentCloud **API** is open (Q-32(a)); this acquisition used no browser.
- Extractions are `pdftotext -layout`; **0 NULs, hazard-13/16 census clean** on both.

## §2 · What was acquired

| | `zinn_obstruction_pca` | `zinn_sex_charges_pca` |
|---|---|---|
| **DocumentCloud id** | 26098558 | 26098557 |
| **URL** | `https://www.documentcloud.org/documents/26098558-zinn_obstruction_pca/` | `https://www.documentcloud.org/documents/26098557-zinn_sex_charges_pca/` |
| **Pages** | 2 | 3 |
| **API `file_hash` (SHA-1)** | `18e52004a33b2a8b4bf1a5ea0e084197b99b997a` | `7bddfe01478fdc55fc91721e093aef1da677cf87` |
| **Served bytes** | 63,062 B · SHA-1 `214fdc0d…` · SHA-256 `78e8d571207127f2efeb39cb5ad9e45d888dfef8d550ce5556e0ccd34bb152dc` | 66,997 B · SHA-1 `5f28dc68…` · SHA-256 `30cef9b8d4ff67a2f8766ca3b836173f07f2a1928d9acc4a2d2bc10147695883` |
| **Banked** | `ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_obstruction_pca_dc26098558.pdf` + `.txt` | `ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_sex_charges_pca_dc26098557.pdf` + `.txt` *(extraction banked, narrative unread — §4)* |
| **Charges as captioned** | 1 count, *"OBSTRUCTION OF JUSTICE - CAPITAL/FIRST DEGREE FELONY CONDUCT"*, statute **76-8-306(2)+(3A)**, severity **F2**, court DST; arrest 09/15/2025 12:07 | 4 counts, *"SEXUAL EXPLOITATION OF A MINOR"*, statute **76-5B-201**, severity **F2**, court DST; arrest 09/15/2025 16:25 |
| **Mechanics carried** | PC ID **189957** · agency case **25UV01023** (UVU PD, ORI UT0251900) · booking agency Utah County Sheriff (ORI UT0250000) · affiant **Detective Michael Dutson, UVU PD** | separate PC statement; same arrestee caption |

⚠️ **PII handling:** both captions carry the arrestee's date of birth and a residential address, and the submission blocks carry personal identifier numbers (SID/OTN/FBI/inmate). **None of these is reproduced in this file**; they exist in the banked artifacts. Booking-process identifiers reproduced above (PC ID, agency case, ORIs) are docket mechanics needed by the roadmap.

🚨 **NEITHER DOCUMENT CARRIES A COURT CASE NUMBER.** The PCAs predate court filing; `25UV01023` is a **police agency** case number, not a docket number. **The court case number Q-153 hoped to surface — the input the Zinn roadmap's every other route needs — is NOT obtained.** The short-case-history route (XChange, or a third-party upload of one) remains the only path to it.

## §3 · The Q-153 sweep — scope and result, stated exactly

- **Query set, all against the open DocumentCloud API on 2026-08-20:** bare `Zinn` (2,811 hits, dominated by unrelated Zinns — Howard Zinn among them); phrase `"George Zinn"` (**17 hits, 2 relevant** — the two PCAs); `user:11107 zinn` (**exactly 2 — the uploader holds nothing else on him**); `zinn utah` (98,771 hits, OR-semantics junk, no relevant additions on the first page).
- ✅ **Yield: the two PCAs above — the first primary documents in this library's Zinn holdings.**
- ⚠️ **Attempted null with a stated scope: no short case history, docket printout, charging Information, or plea/sentencing document for Zinn exists on DocumentCloud findable by these queries.** The Robinson pattern (a third party uploading XChange printouts) has **no Zinn counterpart** on this platform as of today. This null is about DocumentCloud only; it says nothing about XChange or any other repository.

## §4 · What was read, and what was deliberately not

- **The obstruction PCA was read in full** (2 pp.) — §5.
- 🚫 **The sexual-exploitation PCA's PC-statement narrative was NOT read and is not characterised here.** ZINN-REVIEW-2026-08-17 §5 flags the Zinn evidence file for reproducing charging detail concerning **child victims**, and *"recording a conviction does not require reproducing its contents."* The same restraint is applied at acquisition: this file records that document's **caption fields only** (charge count, statute, severity, arrest date/time). The extraction exists on disk unread. Any future pass that needs its contents must clear the living-persons gate first.

## §5 · What the obstruction PCA facially shows (recording layer — the affiant's sworn account, attributed, adopted nowhere)

All of the following is **Detective Dutson's account as sworn in the PCA**, `[PROVISIONAL]` and uncorroborated except where noted:

1. **Event-day sequence (2025-09-10):** the affiant, stationed at the back of the venue, heard *"what sounded like a single gunshot"* at **"about 12:20PM"**; was approached by a man later identified as George Zinn who repeatedly stated *"I shot him now shoot me"*; handcuffed him and **advised him he was under arrest**; searched him and **found no weapon**; escorted him to a patrol car; and (with an Officer Wallace) transported him to the **UVU Police Department**.
2. **At UVU PD, same day:** before Miranda advisement Zinn requested an attorney; the affiant told him *"I did not think he was the one who did the shooting"*; Zinn then stated **on his own** that he did not shoot the individual and *"did it to draw attention from the real shooter."*
3. **Hospital interval:** Zinn was transported to hospital for a medical condition the same day, with an officer accompanying; the affiant records statements at the hospital that Zinn *"was glad he said he shot the individual so the real suspect could get away"* and *"wanted to be a martyr for the person who was shot."*
4. **Booking:** released from hospital **2025-09-15**; transported by Utah County Sheriff to the Utah County Jail; the affiant **booked him there**; the form's arrest date/time is **09/15/2025 12:07**, PC entered 09/15/2025 12:00.

### Document-internal irregularities, recorded verbatim-level and NOT resolved

- **The charge-table "Offense Date" reads 09/15/2025** while the PC statement places the conduct on **2025-09-10** (and closes *"committed during the act of the murder at Utah Valley University on September 10,2025"*). The column likely mirrors the arrest date; **that is an inference and is not adopted** — both dates are recorded as the document prints them.
- **Three severity signals in one document:** the offense description says *"CAPITAL/FIRST DEGREE FELONY CONDUCT"*; the severity column says **F2**; the narrative says *"2nd degree felony."* Under Utah's obstruction statute the grade tracks the underlying offence's grade — **stated here only to explain why the three can coexist; the document is not harmonised.**
- The extraction carries a **duplicated line** at the narrative's close (*"of the murder at Utah Valley University on September 10,2025."* twice) — an extraction or source artifact, present in the banked text.

## §6 · What this acquisition bears on — flagged, not resolved

- 🚨 **The §1.7 booking-date conflict (ZINN-REVIEW §5) now has T1 anchors for BOTH of its senses:** the same-day official statement (2025-09-10: Zinn *"has been booked … by Utah Valley University Police Department"*) sits beside this PCA's event-day custody **at UVU PD** and its **2025-09-15 jail booking** after hospital release. The PCA is *consistent with* the two-senses reading the review deliberately left open — **and this file does not resolve it**; that is Q-136-remainder work under its own gates.
- **Q-40's boundary holds and is restated:** CR-E04 §5.4's early detainee is *expressly not treated as a suspect*; nothing here may be merged with that record. This PCA concerns Zinn's own detention on his own statements. **At least two people were detained on 2025-09-10; they are not merged here.**
- **A second sworn anchor for the shot time** (~12:20 p.m., the affiant's estimate) enters the library — adjacent to SEC-E01 D-73's *"approximately 12:15 p.m."* / *"1217 hours"* crossing times. Recorded as adjacency; D-73 is about the barrier descriptions and does not move.
- **Roadmap effect (for the Q-136 remainder to apply):** these documents bear on the Zinn file's charge-mechanics items (the review's D1/D3-series and §2.2), but **without a court case number they do not execute Route A** — the roadmap's short-case-history acquisition (XChange; Q-31/Q-149) remains the decisive step.
- **Zinn is a living person.** The charges recorded here are charges as of their 2025-09-16 publication; **no statement about their disposition is made in this file**, and nothing here is evidence of guilt on any count. The presumption of innocence applies to Mr. Zinn as to anyone.

## §7 · Residual scope

- It did not read the sexual-exploitation PCA beyond its caption (§4). It did not view the PDFs' page images beyond text extraction. It did not search any platform other than DocumentCloud. It did not touch `zinn-george-evidence.md` (header-flagged, Q-136 paused) or resolve anything in ZINN-REVIEW-2026-08-17. It assigned no D-, V-, F- or M-number. **Q-153 is closed by this file; its application to the Zinn evidence file is Q-136-remainder work.**

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-08-20** | File created. Q-153 executed: DocumentCloud platform sweep (query set and scope stated), yield = the two 2025-09-16 USA Today-uploaded PCAs, both banked with dual hashes (🚨 the served-file/`file_hash` re-render trap fired on both, per the CR-ACQ-2026-08-13 rule). Obstruction PCA read in full at the recording layer: the sworn false-confession account, event-day UVU PD custody, hospital interval, 2025-09-15 jail booking, no weapon found on search. **The sexual-exploitation PCA's narrative deliberately unread** (child-victim restraint, ZINN-REVIEW §5); caption fields only. 🚨 **No court case number in either document — Route A's decisive input is still missing.** Booking-date conflict now has T1 anchors for both senses; left unresolved for Q-136. PII withheld (DOB, address, personal identifier numbers). No register entry assigned, resolved or moved; no case-posture statement altered. |
