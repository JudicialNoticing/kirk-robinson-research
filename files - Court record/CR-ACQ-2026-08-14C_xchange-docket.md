# CR-ACQ-2026-08-14C — Acquisition: the XChange docket, case filing → 2026-03-14

**File ID:** CR-ACQ-2026-08-14C *(the third acquisition file of 2026-08-14)* · **Scope:** acquisition and facial (recording-layer) read of two XChange case-history printouts; partial execution of Q-03; resolution of Q-66 · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-14 · **Status:** v1.0

⚠️ **Findings `[PROVISIONAL]` (added 2026-08-14).** This file is scoped as a facial, recording-layer read — but it makes **analyst-layer claims**: two scoped nulls (no contempt proceeding before 2026-03-14; no bullet-fragment matter in the period), a corroboration claim about CR-E07's count numbering, and a correction to the library's own prior title for the media-access notice. **No independent cycle has run on them** and they may not be cited until one does.

**Sourcing framework (project standard):** Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries a URL and a retrieval date.

---

## §1 · Access-path caveats, first

| | |
|---|---|
| **What this is** | Two **Utah XChange case-history printouts**, generated **2026-03-15 at ~03:18–03:21** and uploaded to DocumentCloud the same day. They are court-system *output about* the docket, not the filings themselves. |
| **How obtained** | DocumentCloud API (open), documents **27880531** and **27880533**, both inside project **224251**; PDFs and text pulled from `s3.documentcloud.org`, retrieved **2026-08-14** |
| **Uploader** | user **144356**, organisation **87307** — ⚠️ **identity NOT established**; the anonymous API returns no names, and this is a **different** uploader from the one that posted the defence brief (user 109543 / org 270, Epoch Times) |
| **Hash discipline** | ⚠️ **The served PDFs are DocumentCloud RE-RENDERS, not the uploaded originals** (the trap logged at CR-WATCH-log v1.3). The API `file_hash` values — the uploaded files' SHA-1 — are **`63d36b7fc21eaa099248d7dcc4f5c46fe7069631`** (27880531) and **`4e23edb3b79e42bc0f5da11c5dbfc6fdbbf10dfc`** (27880533). The banked bytes are the re-renders; their own SHA-256s are recorded at §2. **Never compare a served PDF against an original — compare against `file_hash`.** |
| **Provenance** | ⚠️ **ZERO of three in the filing sense** — these are not filings and carry no signature block, certificate of service or clerk file-stamp. What they carry instead is **court-system provenance**: the Fourth District caption, the case number, a generation timestamp and page numbering. **Their reliability rests on their being XChange output, and this project has not independently confirmed that they are** — no XChange account exists (Q-31, 👤). **Treat as Tier 1 court-record content at the recording layer, with the generation route unverified.** |
| **Coverage ceiling** | ⚠️ **The docket runs to 2026-03-14 and stops.** It **predates the entire preliminary hearing (2026-07-06→07-10), the June contempt matter, and all three briefing dates.** Nothing here speaks to any event after 2026-03-14, and no null taken from it may be stated about a later period. |
| **What it does not contain** | ⚠️ **No document/docket-number COLUMN.** 🛠 **CORRECTED 2026-08-16 (CR-REVIEW-2026-08-16B, R1): FOUR DOCKET NUMBERS DO APPEAR — `Dkt. #23`, `Doc. 165`, `Dkt 197`, `Dkt. 325`, six occurrences in EACH printout, embedded inside filing titles the parties typed. The printouts have no document-number COLUMN; the absolute form was FALSE and this library already relied on the contrary (CR-E12 grades Dkt. #23 at High from exactly this source).** Entries are dated and titled but unnumbered, so **Docs. 525, 570, 625, 631 and 678** — the pre-hearing hearsay briefing the defence brief incorporates (Q-48, CR-E07 §5) — **cannot be resolved from these files**, and in any case post-date their ceiling. |

---

## 2. What was acquired

| | |
|---|---|
| **A — full case history, 31 pp.** | "tyler robinson case list of all filings and hearings as of 3-15-2026", DocumentCloud **27880531** · `https://www.documentcloud.org/documents/27880531-list-of-all-filings-and-hearings-as-of-3-15-2026/` · banked as `2026-03-15_xchange-case-history-full_dc27880531.pdf` (58 KB, SHA-256 `f3eed9a484e55ee05b887ade4c8ab2e920e039ddf7ebfb31529a4f5f7ad64ee3`) + `.txt` (71 KB, SHA-256 `b09d12d28f4ab8dee72fe512ef3b585655ed65f64fe153df89700fe8365486c0`) |
| **B — short case history, 13 pp.** | "tyler robinson all docket entries as of 3-15-2026", DocumentCloud **27880533** · banked as `2026-03-15_xchange-short-case-history_dc27880533.pdf` (28 KB, SHA-256 `f65a8791251534db1dc010eca412c3b15433be05e63007dbeadbc2a392531555`) + `.txt` (42 KB, SHA-256 `96135546a0e8b1e49a4e12023d9f2f3177a2df153912b0a5a350730d8d77d940`) |

**A is the fuller artifact** (charges with attributes, hearing notices, signing judges, order titles); **B is the condensed "Xchange Short Case History"** (parties and counsel, charge list, a flat chronological events list). They overlap heavily and corroborate each other.

## 3. Why this matters: the library has never held a docket

**Q-03 ("Docket pull — Fourth District, Case 251403576") has been `blocked` since 2026-07-27**, on the grounds that XChange is paywalled (Q-31) and DocumentCloud was bot-gated (Q-32). **The DocumentCloud API route opened at DOCKET-WATCH Run 2, and the docket was sitting inside the already-enumerated project 224251 the whole time.** ⚠️ **The project had been enumerated three times — Runs 2 and 3 and again on 2026-08-14 — and each enumeration read the titles for the State's brief and stopped.** *(The lesson is not that the sweeps were careless but that **a search for one artifact does not inventory a corpus**; "list of all filings and hearings" is not a phrase any State's-brief query would surface.)*

**Q-03 is therefore PARTIALLY EXECUTED, not closed** — the library now holds the docket **through 2026-03-14 only**, and every question Q-03 was opened to answer (the bullet-fragment ruling, the briefing status, D-51's underlying facts) concerns later periods.

## 4. What the docket facially shows (recording layer)

- **Caption and forum.** Fourth Judicial District, Provo, Utah County; **Case No. 251403576, State Felony**; **current assigned judge Tony F. Graf, Jr.**
- **Counsel of record, as listed.** For the State: **Jeffrey Gray, Christopher Ballard, Chad Grunander, Ryan McBride.** For the defendant: **Public Defender, Kathryn Nester, Staci Visser.** *(⚠️ The list is as of 2026-03-15 and does not include Michael Burt or Richard Novak, both admitted pro hac vice and both signing the 2026-08-11 brief — a reminder that a party's representation is a moving fact.)*
- **THE SEVEN CHARGES, WITH STATUTES AND OFFENSE DATES — a Tier 1 confirmation the library did not previously hold:**

| # | Statute | Charge | Degree | Offense date |
|---|---|---|---|---|
| 1 | 76-5-202 | Aggravated murder | 1st degree felony | 2025-09-10 |
| 2 | 76-11-210(2)+(3C) | Felony discharge of firearm causing serious bodily injury | 1st degree felony | 2025-09-10 |
| 3 | 76-8-306(2)+(3A) | Obstruction of justice — capital/first-degree-felony conduct | 2nd degree felony | 2025-09-10 |
| 4 | 76-8-306(2)+(3A) | Obstruction of justice — capital/first-degree-felony conduct | 2nd degree felony | 2025-09-10 |
| 5 | 76-8-508 | Tampering with a witness | 3rd degree felony | 2025-09-10 |
| 6 | 76-8-508 | Tampering with a witness | 3rd degree felony | **2025-09-11** |
| 7 | 76-3-203.10(2) | Violent offense committed in presence of a child | Class A misdemeanour | 2025-09-10 |

  ✅ **This independently corroborates CR-E07's account of the defence brief's count numbering** — the brief's "Count Six" (witness tampering) and "Count Seven" (violent offense in presence of a child) match the docket's charges 6 and 7 exactly. **The brief's numbering was a party's characterisation of an Information this project does not hold; it now has court-record corroboration.** ⚠️ **Charges 5 and 6 share a statute and differ only by offense date (09-10 vs 09-11) — any file citing "the tampering count" must say which.**
- **Case opened** 2025-09-16 (Information filed; case filed by efiler; WebEx initial appearance the same day), with a **bail order** and a **pretrial protective order** the same day.
- **The docket runs continuously to 2026-03-14**, ending with *"Rulings And Orders On Classification And Closure Motions,"* signed by Judge Graf **2026-03-13**.

## 5. Q-66 — ANSWERED, and the library's borrowed title was wrong

**Q-66 sought "the 2026-02-02 'Notice re Media Access'", known only from one line of the 2026-07-08 supplemental notice** (CR-ACQ-2026-08-14B), which described itself as supplementing it.

✅ **The filing exists and is on the docket: "Filed: Notice Concerning Media Access", 02-02-2026** — confirmed in **both** printouts independently.

⚠️ **Its actual title is "Notice Concerning Media Access", not "Notice re Media Access."** The library had taken the title from **the supplemental notice's own description of it** — i.e. from a party's paraphrase of a document. **Standing hazard 1 in a new place: a filing's description of another filing is reliable as to the fact of it, not as to its title.** Q-66 should be pursued under the docket's title, not the brief's.

**What Q-66 still needs:** the document itself. The docket gives its existence and date only; **its filer and contents remain unknown**, and it sits in a dense 2026-01-30 → 2026-02-04 cluster of media-access, classification and closure litigation involving the news media, the defence and the State.

## 6. Scoped nulls — with their scope stated

- **NO CONTEMPT PROCEEDING APPEARS ANYWHERE BEFORE 2026-03-14.** `/contempt/` returns **9 hits in the 31-page history and every one was opened**: all nine are the **standard UCJA Rule 4-401.02 boilerplate** printed on hearing notices (*"may NOT be recorded, photographed, or transmitted. Failure to comply … may be treated as contempt of court"*). **None refers to any contempt proceeding in this case.** ⚠️ **Had these been counted without opening them, the library would have manufactured a pre-March contempt matter that does not exist** — standing hazard 6's "grep, then read the hit," earned outside the register for the first time. **Scope: this is a claim about the period to 2026-03-14 only; the OSC/contempt matter the library does hold is June 2026 (Q-65) and lies beyond this docket's ceiling.**
- **`/bullet/` and `/fragment/` return ZERO** across the 31-page history — so **the bullet-fragment motion and its ruling (Q-35, blocked on Q-03) are not in this period.** `/preserve/` returns 12, all concerning the **motion to preserve evidence** and its orders (2025-10-08 → 2025-11-04), a different matter.
- **No document numbers anywhere**, so Q-48's Docs. 631 and 678 remain unresolved from here.

## 7. Residue and next steps

| → | Item |
|---|---|
| **Q-03** | **PARTIALLY EXECUTED** — docket held through **2026-03-14**. ⚠️ **The period that matters most — the preliminary hearing, the June contempt matter, the three briefs, and any motion to continue — is entirely outside it.** A current docket still requires **👤 Q-31 (XChange, ~$10)** or another route |
| **Q-66** | **Existence and date CONFIRMED; the DOCUMENT is still not held**, and its correct title is **"Notice Concerning Media Access"** |
| **Q-65** | Unaffected — the 2026-06-26 contempt/OSC ruling post-dates this docket |
| **Q-48** | Unaffected — no document numbers here |
| **NEW** | ⚠️ **The 2026-01-09 → 2026-02-04 media-access, classification and closure litigation is a substantial body of proceedings this library has never inventoried**, and the docket names its filings. It bears directly on why the exhibit-publication questions arose at the hearing. Worth a scoped read |
| ✅ **DONE, same session** | ~~**Project 224251 holds ~44 further docket filings this library has not read**, including the **Information (10 pp.)** and the **probable-cause affidavit (3 pp.)**… **Neither is held.**~~ **BOTH WERE ACQUIRED AND READ ON 2026-08-14 → [CR-E08](CR-E08_state-information-and-pc-affidavit-2025-09-16.md)** — the first filings **by the State** this project holds as documents. **CR-E07's F-15 is partly cured**, and **A-4 upgraded Medium → High**: the Information pleads exactly one aggravating circumstance. **~42 filings in the project remain unread → Q-70.** |

**No case-posture statement in any topic file is altered by this acquisition. No D-register entry is assigned, resolved or moved.** As of 2026-08-14, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-14 | File created. **The library holds a docket for the first time** — two XChange case-history printouts (31 pp. and 13 pp.) banked with SHA-256s and with DocumentCloud's `file_hash` recorded per the re-render trap. **Q-03 partially executed**, coverage **case filing → 2026-03-14**, with the ceiling stated plainly because everything Q-03 was opened to answer lies beyond it. ⚠️ **The artifacts were inside project 224251 all along, enumerated three times by sweeps hunting the State's brief** — a search for one artifact does not inventory a corpus. **The seven charges with statutes and offense dates are now held at Tier 1**, independently corroborating CR-E07's account of the defence brief's Count Six / Count Seven numbering, and flagging that **charges 5 and 6 share a statute and differ only by offense date.** **Q-66 answered as to existence and date — and the library's title for it was wrong**: the docket says *"Notice Concerning Media Access"*, where the library had taken *"Notice re Media Access"* from another filing's description of it (hazard 1: a filing's description of another filing is reliable as to the fact, not the title). **Two scoped nulls with their scope stated: no contempt proceeding before 2026-03-14** — all nine `/contempt/` hits opened and every one is Rule 4-401.02 boilerplate, so counting without reading would have manufactured a proceeding that does not exist — **and no bullet-fragment matter in the period.** ⚠️ **Provenance is zero-of-three in the filing sense and the XChange generation route is unconfirmed** (no account exists, Q-31 👤). No register entry assigned, resolved or moved; no case-posture statement altered. |
