# CR-ACQ-2026-08-16 — Acquisition: DocumentCloud project 224251 completed (46/46), plus nine filings found outside it

**File ID:** CR-ACQ-2026-08-16 · **Scope:** acquisition only — the completion of Q-70 (the 32 unread filings of DocumentCloud project 224251), the discovery that the project was never the whole corpus, and the provenance/hash/metadata discipline attaching to all of it. **Substantive reads of the acquired documents are NOT in this file** — see §8 for where they go. · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, **Fourth Judicial District Court, Provo — case type FS** (see F-41), Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** **v1.3** — 🚨 *§6.1's hazard was twice too small and once prescribed a remedy that does not work; **remediated in full at Q-105** — 1,189 NULs across 50 files repaired, content verified unchanged against git.* · *(v1.1 — 🚨 *§3 corrected in place: v1.0's "seven were new" was wrong, and wrong by this file's own F-39. Two of the seven are third-party filings that merely CITE this case; one is a hash-duplicate. See the correction block in §3.*

⚠️ **Findings `[PROVISIONAL]`.** This file makes analyst-layer claims — the metadata hazard (§4), two empirically demonstrated false-null mechanisms (§6), the completeness null (§3), and five corrections to this project's own filenames (§5). **No independent cycle has run on them.** They may not be cited elsewhere until one does (LOOP §2). → **Q-83**.

> ### ⚠️ §0.1 · PROVISIONAL DEPENDENCIES — *added 2026-08-16, LOOP §2 discipline*
>
> 🚨 **THIS FILE IS THE ROOT OF A FIVE-FILE DEPENDENCY GRAPH, AND IT IS ITSELF `[PROVISIONAL]`.**
> **F-39** (a docket number from a DocumentCloud title is Tier 4), **F-40** (a docket number in a responsive caption cites the filing it ANSWERS) and **F-41** (the case number is not unique) are relied on by **CR-E11, CR-E12, CR-E13 and CR-E14** — every tier claim about a docket number in those four files rests on findings **no independent cycle has checked**.
> ⚠️ **If F-39 or F-40 falls, docket-number claims move in four files at once.** That concentration is why this block exists.
> **This file's own provisional dependencies:** `CR-ACQ-2026-08-14C` — the DocumentCloud re-render hash trap, and its XChange "no document numbers" caveat *(the latter already corrected — see §4)*.
> **Clearing item: Q-83.**

**Sourcing framework (project standard):** Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting/analysis · Tier 4 — anonymous-source or low-verification material. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries a URL and a retrieval date.

---

## §1 · Access-path caveats, first

| | |
|---|---|
| **The route died and came back on the same day** | Run 4 of the docket watch, earlier on **2026-08-16**, recorded the DocumentCloud API as **HTTP 403 behind a Cloudflare interstitial from local sessions**, on three endpoints under two user agents, re-tested twice — and escalated it as a **standing route loss** reversing the 08-13 enumeration. **Re-tested at ~14:05 the same day: the route is fully open.** Search endpoint `200`, per-document endpoint `200`, and S3 assets `200` for both `.txt` and `.pdf`. ⚠️ **Treat the route as INTERMITTENT, not restored.** Nothing was done to fix it; it changed on its own. **Re-test before relying on it, and never log its silence as a null** (a route that flaps will produce false "empty" results that look exactly like real ones). |
| **How obtained** | DocumentCloud API, anonymous, no credentials: `https://api.www.documentcloud.org/api/documents/search/?q=project:224251` (paginated, 3 pages, `per_page=25`) for enumeration; `https://s3.documentcloud.org/documents/<id>/<slug>.{pdf,txt}` for assets. Retrieved **2026-08-16**. The alternate host `https://www.documentcloud.org/api/documents/search/` returns `404` and is not a valid endpoint — do not read that 404 as a block. |
| **Uploader** | ⚠️ **All 46 documents in project 224251 were uploaded by a SINGLE account — user `144356`, organisation `87307` — between 2026-03-15T19:33Z and 2026-03-16T16:42Z.** This is **one curation act by one party**, not an accreting public archive. Identity **NOT established** (the anonymous API returns no names). That same account has **338 public documents**, the great majority on unrelated matters (Scientology, an LA mandamus proceeding, an NYPD RICO suit) — so it is a general-purpose document poster, not a Robinson-case archivist. |
| **Hash discipline** | ⚠️ **The served PDF is a DocumentCloud RE-RENDER, not the uploaded original.** The API's `file_hash` field is the SHA-1 of the **original**; the bytes you download are not it. **This trap is now DEMONSTRATED on a case artifact rather than merely asserted — see §6.3.** Both hashes are recorded below: `file_hash` (SHA-1, authoritative for document identity) in §2, and the served bytes' SHA-256 in the machine-readable receipts (§7). **Never compare a served PDF against an original; compare against `file_hash`.** |
| **Provenance of the collection** | ⚠️ **Zero of three in the filing sense for the collection as a whole.** These are third-party uploads. Individual documents carry their own provenance — signature blocks, certificates of service, e-file stamps, court seals — which must be assessed **per document**, not inherited from the project. Several are court orders bearing Judge Graf's e-signature and the court seal; several are party filings with signature blocks; several are not filings at all (press releases, a jail booking screenshot, a case-search printout). |
| **Coverage ceiling of the collection** | 🚨 **The collection stops at 2026-03-14 and this is structural, not incidental** — it was assembled on 2026-03-15/16, so **nothing in it postdates its own creation.** It therefore contains **nothing** about the preliminary hearing (2026-07-06→07-10), the June 2026 contempt matter, the 2026-04-17 evidentiary hearing, or any of the three 2026 briefing dates. **No null taken from this collection may be stated about any period after 2026-03-14.** |

---

## §2 · What was acquired — project 224251, all 46

**28 newly banked today; 18 already held.** Files land in `CR-ACQ-2026-07-27_court-record-artifacts/` as `<date>_<descriptor>_dkt<N>_dc<id>.{pdf,txt}`.

🚨 **Read §4 before using the "Dkt*" or "Title" columns for anything.** Both are **uploader-supplied metadata**, not document content.

| # | Date (title) | Dkt* | pp | DC id | API `file_hash` (SHA-1) | New today | Title as uploaded (verbatim) |
|---|---|---|---|---|---|---|---|
| 1 | 2025-09-10 | — | 1 | `27880543` | `e93de8a85d8c94325df731ad5174ebd96c9f1780` | ✅ | 9-10-2025 utah county district attorney press release after shooting |
| 2 | 2025-09-12 | 3 | 3 | `27880877` | `8c9e4332774037d23e2bf4c1a940f674b777f9c5` | ✅ | 9-12-2025 public safety assessment report - docket 3 |
| 3 | 2025-09-16 | 4 | 1 | `27880869` | `deccfcdd5807a2cebc9d7b1e06f709150fc5e292` | ✅ | 9-16-2025 bail order – docket 4 |
| 4 | 2025-09-16 | 7 | 6 | `27880860` | `266fccb19b108d5b9cba24f1ecaa1d5f1773d8c8` | ✅ | 9-16-2025 proposed pretrial protective order - docket 7 |
| 5 | 2025-09-16 | 12 | 2 | `27880865` | `9c9e86cbe2cd37df962038958585ce936665b76d` | ✅ | 9-16-2025 Request for Designation of Victim Representative - docket 12 |
| 6 | 2025-09-16 | 14 | 6 | `27880872` | `2d70980d6d529c647f5299eb6094cdee88984039` | — | 9-16-2025 Order Pretrial Protective Order - docket 14 |
| 7 | 2025-09-22 | — | 2 | `27880535` | `071f04dbe51be940338d4764f2e3b4f2bfa2e8e6` | ✅ | 9-22-2025 Utah County District Attorney press release - tyler robinson prosecutor trial team |
| 8 | 2025-09-22 | — | 2 | `27880539` | `0d0cb3cc8773854943e090c24707e7c8bd7f8eea` | ✅ | 9-22-2025 prosecutor Chad Grunander biography |
| 9 | 2025-09-22 | — | 2 | `27880541` | `eea80ea3f226f80bcba95e2152e4af00864d6629` | ✅ | 9-22-2025 prosecutor Christopher Ballard biography |
| 10 | 2025-09-22 | — | 1 | `27880538` | `5256c9c4e3588786bca85ee4008060ebbe35ab33` | ✅ | 9-22-2025 prosecutor David Sturgill biography |
| 11 | 2025-09-22 | — | 1 | `27880540` | `7aab429f9d835adb0376f5d58c83a6138fe97941` | ✅ | 9-22-2025 prosecutor Lauren Hunt biography |
| 12 | 2025-09-22 | — | 2 | `27880537` | `517c756cc1d2be1a1c99b38a41156cc268d54c1a` | ✅ | 9-22-2025 prosecutor Ryan McBride biography |
| 13 | 2025-09-22 | — | 2 | `27880536` | `48ecbf310c7603bb90703ece85d11b4253ff08e9` | ✅ | 9-22-2025 prosecutor jeffrey gray biography |
| 14 | 2025-09-24 | 24 | 1 | `27880870` | `bf7482cde58f4b0daa2f0e18e3f90e9fe7c7b22f` | ✅ | 9-24-2025 Order To Transport for virtual hearing - docket 24 |
| 15 | 2025-10-08 | 74 | 2 | `27880859` | `b017422a7062c77767cc7bc37ac1211deea38f04` | ✅ | 10-08-2025 Copy of Video-Audio Record completed - docket 74 |
| 16 | 2025-10-08 | 75 | 3 | `27880857` | `534dcba92f9c9be679c2bf80cab0ddac45087c91` | — | 10-08-2025 Defendant Motion to Preserve Evidence - docket 75 |
| 17 | 2025-10-08 | 76 | 3 | `27880875` | `3f0b41a9d2e5bc3676be337e8e325bcffc0c05b3` | ✅ | 10-08-2025 Proposed Order Granting Motion to Preserve Evidence - docket 76 |
| 18 | 2025-10-13 | 91 | 5 | `27880863` | `358a89356450dc48a45a4e1aee461cb9bad3e471` | ✅ | 10-13-2025 Both Parties Motion for Discovery Protective Order Stipulated - docket 91 |
| 19 | 2025-10-21 | 111 | 10 | `27880867` | `594cbf7df66c43bbf133f18a6ade81ae524da97a` | ✅ | 10-21-2025 Defendant Motion to Strike Response to Defendant s Motion to Appear at All In-Person Proceedings in Civilian Clothing and Without Restraints - docket 111 |
| 20 | 2025-10-22 | 116 | 3 | `27880864` | `b13575951b15c840fce84793fcd7232cd3fb686d` | — | 10-22-2025 Prosecutor Motion to Set Aside 10-20-2025 Order Granting Motion to Preserve Evidence - docket 116 |
| 21 | 2025-10-22 | 117 | 7 | `27880878` | `5290593ac427448fa05c66cd1119a14dcd751cf9` | — | 10-22-2025 Prosecutor Response to Defendant Motion to Preserve Evidence - docket 117 |
| 22 | 2025-10-27 | 135 | 3 | `27880871` | `22860bb9efc9cceedf17b0092e6d0b97087ca770` | — | 10-27-2025 Prosecutor Notice of Open File Poilcy and Invitation to Inspect Physical Evidence - docket 135 |
| 23 | 2025-10-27 | 137 | 9 | `27880868` | `8c7f53bfd2ed0668fb9cf0eb42bd9ec3f423f38d` | ✅ | 10-27-2025 ruling and order on defendant motion to strike and appear in civilian clothing without restraints - docket 137 |
| 24 | 2025-11-03 | 152 | 3 | `27880861` | `b30d2c0b4ff7614c337aeb5cad9cbc12a9d4f19a` | — | 11-3-2025 defendant stipulated Motion to Order Transcript and Classify Transcript and Audio as Private from 10-24-2025 - docket 152 |
| 25 | 2025-11-04 | 161 | 4 | `27880862` | `273e430c346faba340a8ecb8cf9e1b6f53235d10` | — | 11-4-2025 Order Stipulated Order (1) Setting Aside 10-20-2025 Order Granting Motion to Preserve Evidence and (2) Granting In Part Motion to Preserve Evidence - docket 161 |
| 26 | 2025-11-10 | 169 | 7 | `27880858` | `73adeb9c24f175f3676ebc4b70ad4c97d4f44452` | — | 11-10-2025 Defendant Tyler James Robinson Response to Request for Notice of Motion to Close Judicial Proceedings and Records - docket 169 |
| 27 | 2025-12-04 | 211 | 1 | `27880874` | `358e9b4570ba9448f26ebbbcf69e71d6babc3f1f` | ✅ | 12-4-2025 Utah Office for Victims of Crime Restitution Notice Claim#1113665 - docket 211 |
| 28 | 2025-12-08 | 213 | 9 | `27880876` | `e4ea9888a2843f1bed38d7c0832bf14bad134087` | — | 12-8-2025 defendant response to the motion for limited intervention of deseret news et al (Dkt 197) - docket 213 |
| 29 | 2025-12-15 | 242 | 3 | `27880866` | `7e38df28274ec1502a6e22c29eebd6e80ad05a4b` | — | 12-15-2025 ruling and order granting prosecutor motion to clarify courts pretrial and trial publicity order - docket 242 |
| 30 | 2025-12-17 | 250 | 48 | `27880873` | `3ab5a9abe2e6703fab7220a1c76eb6cafb151304` | ✅ | 12-17-2025 defendant Motion to Disqualify prosecutor and or judge for conflict of interest - docket 250 |
| 31 | 2026-01-02 | 406 | 1 | `27880887` | `136329d0e5eeabe0c36e39697e61cbaceb7da3bf` | — | 1-2-2026 Appellate Order on defendant appeal on 11-17-2025 interlocutory order - docket 406 |
| 32 | 2026-01-05 | 289 | 33 | `27880888` | `3b36f2509dc103dde1b9e72c5f1bd65cc9eb6f77` | ✅ | 1-5-2026 prosecutor Opposition to Defendant Motion to Disqualify the Utah County Attorney Office - docket 289 |
| 33 | 2026-01-08 | 293 | 7 | `27881513` | `34b2684342b75b3037aac8a2d05c04ba995d4107` | ✅ | 1-8-2026 Defendant Reply to Prosecutor Opposition to Motion to Disqualify Public - docket 293 |
| 34 | 2026-01-09 | 291 | 4 | `27881510` | `fbfb9ad67c95e8bb3f911ed0725268f188bb17d8` | — | 1-9-2026 Subpoena for Sgt David Hull - docket 291 |
| 35 | 2026-01-30 | 346 | 3 | `27881511` | `e76e31891263cf213d10e39ece9b9b5134645b87` | ✅ | 1-30-2026 prosecutor Opposition to Defendant Motion to Classify Motion to Exclude Still media from the Courtroom and classify as private hearing - docket 346 |
| 36 | 2026-01-30 | 348 | 12 | `27881509` | `6b1b4208a5ef4a1eef745b5630e0b758630aca22` | ✅ | 1-30-2026 DEFENDANT TYLER ROBINSON RENEWED MOTION TO DISQUALIFY UTAH ATTORNEY GENERAL MEMORANDUM OF POINTS AND AUTHORITIES - docket 348 |
| 37 | 2026-01-30 | 355 | 5 | `27881506` | `7ba8780c0629c9cde06c751088337294a22707b2` | — | 1-30-2026 attachment A internal communications at prosecutors office to cease public statements - docket 355 |
| 38 | 2026-02-02 | 366 | 14 | `27881512` | `b729357353b75f0d6c381b886579ae784cf3e6c9` | ✅ | 2-2-2026 prosecutor Memorandum and Opposition to Defendant Renewed Request to Motion to Disqualify to the Utah Attorney General - docket 366 |
| 39 | 2026-02-02 | 368 | 5 | `27881508` | `6f038b15b973555edd9fe054df324b88e4f34f0b` | ✅ | 2-2-2026 Proffer of Facts re Closure of Poritons of Evidentiary Hearing on Motion to Disqualify UCAO - docket 368 |
| 40 | 2026-02-13 | 413 | 3 | `27881507` | `aeb51f9560299f2d1a6d0ed375feeff026257bf1` | — | 2-13-2026 minute order on ORAL ARUGMENT of EVIDENTIARY HEARING - docket 413 |
| 41 | — | — | 13 | `27880533` | `4e23edb3b79e42bc0f5da11c5dbfc6fdbbf10dfc` | — | tyler robinson all docket entries as of 3-15-2026 |
| 42 | — | — | 31 | `27880531` | `63d36b7fc21eaa099248d7dcc4f5c46fe7069631` | — | tyler robinson case list of all filings and hearings as of 3-15-2026 |
| 43 | — | — | 2 | `27880529` | `36d7bb97e5a0b90a3e1117b52d783d876a78306a` | ✅ | tyler robinson case search on utah state court online xchange service |
| 44 | — | — | 10 | `27880532` | `8218cb8683028c680bab5f11ac00a095e47c5e1c` | — | tyler robinson information of charges filing by district attorney 9-16-2025 |
| 45 | — | — | 1 | `27880534` | `d3c50ac9fdc3340e2700e1c5e0b8e54876cc9ebd` | ✅ | tyler robinson utah county sheriff office inmate custody booking |
| 46 | — | — | 3 | `27880530` | `926a764f4b2f1d7818995d2d9525da9f25dbbbe1` | — | utah county district attorney affidavit of probable cause against tyler robinson 9-16-2025 |

---

## §3 · The completeness question — and the null that closes one seam while opening another

**Sibling projects: enumerated, and they are empty of new material.** Every one of the 46 documents also belongs to project **225170**, and six also to project **225296**. Both were enumerated in full: `225170` = 46 documents, `225296` = 6 documents, and **every one is already inside 224251**. **Zero new documents.** This is a genuine scoped null and it closes the seam — nobody needs to chase those projects again.

🚨 **But the corpus was never the project. A case-number search returns documents project 224251 does not contain.**

`q="251403576"` returns **40 documents**, of which **9 sit outside project 224251**. Two of the nine were already held by this library from other routes (the defence brief; the victim-family supplemental notice) — which is itself the confirmation that the query works, since it found what the library already knew about.

> # 🚨 CORRECTED AT v1.1, 2026-08-16 — AND THE ERROR IS THIS FILE'S OWN F-39, COMMITTED WITHIN THE HOUR
>
> **v1.0 said "Seven were new" and described the 663-page federal filing as *"a parallel FEDERAL track this library has never looked at."* THAT WAS WRONG, and it was wrong the exact way §4 warns about.** I took a search result's **membership in a result set** — metadata — as evidence of **relevance**, and wrote it into a published file **without opening the documents**. The readers who caught my filename errors caught them by opening documents; I did not open these.
>
> **What the seven actually are, each verified by reading its first page:**
>
> | DC id | Verdict | What it actually is |
> |---|---|---|
> | `26099252` | ⚠️ **DUPLICATE, not new** | The **proposed pretrial protective order** — `file_hash` **identical** to `27880860` already in the project. ✅ **Not worthless: a second, independent uploader holding the byte-identical original is genuine provenance corroboration.** |
> | `26493871` | ✅ **GENUINELY NEW, this case** | A **victim's-counsel filing of 2026-01-19**, Fourth Judicial District, signed by the same victim's counsel the library tracks. Unread. |
> | `27998184` · `27998188` · `27998189` | ✅ **GENUINELY NEW, this case — but ONE document, not three** | The **motion to vacate or continue** (28 printed pp.), signed by this case's defence team. Identical `file_hash` on all three. Unread. |
> | `28324423` | ❌ **NOT THIS CASE** | ***State of South Carolina v. Richard Alexander Murdaugh***, Colleton County. It matched because it **CITES** *Utah v. Robinson* as persuasive authority on shackling and courtroom cameras. |
> | `28417731` | ❌ **NOT THIS CASE, and not a "parallel federal track"** | A **civil** matter in the District of Utah. It matched because it **CITES** *Utah v. Robinson* by analogy on a limited-intervention procedure. **It is not a parallel proceeding, and nothing about this case turns on it.** |
>
> **So the honest count is: two genuinely new documents of this case (both unread), one hash-duplicate with provenance value, and two third-party documents that merely cite the case.** Not seven.
>
> ✅ **The two false positives nonetheless PAID OUT, and that is recorded rather than buried:**
> - **F-80 — Two docket numbers arrive at Tier 1 from the federal filing's own citation:** the media's intervention request is **Docket No. 267**, and the ***Order Denying Media's Request to Intervene* is Doc. 266, 4th Dist. Ct., 2025-12-29**, described as requiring notice to media representatives of future Rule 4-202.04 closure or classification motions. **These are exactly CR-E12's B-7 and Q-77 targets, and they are now numbered.** *(Tier 1 by this file's own §4 rule: a docket number cited inside a primary filing.)* **Confidence: High.**
> - **F-81 — 🚨 A VIDEO OF THE 2025-12-11 HEARING MAY EXIST PUBLICLY.** The South Carolina filing cites a **YouTube recording of the 2025-12-11 hearing**. ⚠️ **CR-E12 records that hearing as PARTIALLY CLOSED** (12:12–2:19 closed, remainder open, its minute order **`SEALED`**) — so any public video can only be of the **open** portion, and **nothing may be inferred about the closed segment from it**. ⚠️ **The URL is OCR-mangled and the video ID is NOT recoverable**: the PDF's text layer *is* the OCR (`pdftotext` reproduces it identically), rendering *"hitps://wwiv.youtube.com/walch?v=…&1=324s"*. **Do not guess the ID.** → **Q-97.** **Confidence that a recording was cited: High. Confidence in the identifier: nil.**
> - The same filing asserts, as a Tier 3-equivalent characterisation by an out-of-state litigant, that the court ordered cameras repositioned and warned they would be excluded if the defendant were again shown in restraints. ⚠️ **Attributed, not adopted; this library holds no order to that effect.**
>
> **The lesson, stated against myself:** §4 of this file establishes that *a document's title is not the document*. **A search result's presence in a result set is the same kind of claim, and I believed it for the same reason — it was cheap.** The rule generalises: **relevance is established by reading, not by retrieval.**

**The material found outside the project, as banked:**

| Date | pp | DC id | Uploader org | API `file_hash` (SHA-1) | Title as uploaded (verbatim) | Disposition |
|---|---|---|---|---|---|---|
| 2025-09-16 | 6 | `26099252` | 729 | `266fccb19b108d5b9cba24f1ecaa1d5f1773d8c8` | document (5) | banked |
| 2026-01-19 | 3 | `26493871` | 102365 | `bf5b4453fd686a31f27bd5d5d9c8f003f79fde45` | document (4) | banked |
| 2026-04-02 | 69 | `27998184` | 27875 | `a8383ffe1dfe667bef96cb05f0e742e41f8ae0a0` | tyler robinson motion to vacate or continue march 27 2026 | banked |
| 2026-04-02 | 69 | `27998188` | 27875 | `a8383ffe1dfe667bef96cb05f0e742e41f8ae0a0` | tyler robinson motion to vacate or continue march 27 2026 | banked |
| 2026-04-02 | 69 | `27998189` | 27875 | `a8383ffe1dfe667bef96cb05f0e742e41f8ae0a0` | tyler robinson motion to vacate or continue march 27 2026 | banked |
| 2026-06-25 | 4 | `28324423` | 60250 | `d4a997ac81aae5ace133c48bce0cd1527238a632` | Reply to the States Response for Motion for Defendant to be Unshackled | banked |
| 2026-07-06 | 663 | `28417731` | 758 | `4660cb21d41269e89c1d76a81d9e47be0884559f` | gov.uscourts.utd.165286.1.4 1 | banked |
| 2026-07-09 | 4 | `28443912` | 19290 | `e31404f912f4a36578ed774b1e3fa02f746875fb` | Supplemental Notice Concerning Access to Evidennce Presented in Open Court re Tyler Robinson | banked |
| 2026-08-12 | 41 | `28551955` | 270 | `a93801eef1bcbe30e0af4f569d91e841b266ce2b` | Defendant Tyler James Robinson's Preliminary Hearing Briefing, 8-11-26 | banked |

⚠️ **The three copies of the 69-page "motion to vacate or continue March 27 2026" are ONE document, not three** — identical `file_hash` `a8383ffe1dfe667b...` on all three. **Do not count them as three filings.**

🚨 **The lesson, and it is the same one this library has now learned FOUR times at successively larger scale — the fourth time inside this very file (see the correction block above):** *a search for one artifact does not inventory a corpus* (2026-08-14, three sweeps read past the Information while hunting the State's brief) — and now — **enumerating a project is not inventorying a platform.** The library spent two days believing "46/46" meant complete. It meant complete *as to one uploader's folder*. **Q-79** opens to sweep the platform properly rather than one project.

**Scope of this null, stated exactly:** searched DocumentCloud's public API on 2026-08-16 for the exact string `"251403576"` and for `user:144356`. **Not searched:** other case-number formats, party-name queries, or any other document platform. `+robinson +tyler` returns ~17,000 results and is useless without further constraint. **This does not establish that 55 documents is the whole of the case on DocumentCloud.**

---

## §4 · 🚨 THE METADATA HAZARD — uploader titles are not document content, and this library has been treating them as if they were

**Established at High confidence, by two independent readers working on disjoint document sets who reached it separately, plus direct verification.**

**Every docket number and every title in §2 comes from a field a third-party uploader typed.** They are not printed on the documents. Specifically:

- **Of the documents examined in depth, only three docket numbers are stated on a document face** — **#75**, **#107** and **#116**. All the rest (#3, #4, #7, #12, #14, #24, #74, #76, #91, #117, #135, #161, #197/213, #250, #289, #348, #366, #368, #413…) rest on the uploader's title, on a filename derived from it, or on a citation inside some *other* filing.
- **The XChange docket printouts cannot corroborate any of them.** Both banked printouts are date-ordered and **have no document-number column.** 🚨 **CORRECTED 2026-08-16 — v1.0 of this line said they "carry no document numbers at all… now confirmed against the full 31-page file." THAT ASSERTED A VERIFICATION ACT THAT DID NOT HAPPEN, and the claim is false.** 🛠 **CORRECTED 2026-08-16 (CR-REVIEW-2026-08-16B, R1): FOUR DOCKET NUMBERS DO APPEAR — `Dkt. #23`, `Doc. 165`, `Dkt 197`, `Dkt. 325`, six occurrences in EACH printout, embedded inside filing titles the parties typed. The printouts have no document-number COLUMN; the absolute form was FALSE and this library already relied on the contrary (CR-E12 grades Dkt. #23 at High from exactly this source).**
- **The uploader's titles contain demonstrable errors.** The minute order for the 2026-02-03 hearing is titled *"2-13-2026 minute order…"*. **There is no 2026-02-13 docket entry of any kind in this case** — the February entries run 02-12 → 02-19 🛠 **CORRECTED 2026-08-16 (R2): February 2026 actually runs 02-02 → 02-26, fourteen distinct dates. The true fact is a GAP between 02-12 and 02-19. The conclusion (no 02-13 entry) survives; the stated basis did not — and 12 of the 14 February dates fall outside the range as written, including 02-23/02-24 which carry the disqualification denial.**. The document's own face reads hearing date **February 3, 2026** and entry stamp **February 23, 2026, 01:43:54 PM**. **"2-13-2026" is a typo for 2-23-2026.**

**F-39 — the tier of a docket number in this library is now explicit.** A docket number is **Tier 1 only when read off a document face or cited inside a primary filing**. When it comes from a DocumentCloud title it is **uploader metadata — treat as Tier 4** and mark it. The `dkt<N>` component of every filename in the artifacts folder is a **convenience label, not an assertion**, unless §2's "Dkt*" column is confirmed by one of the two Tier 1 routes.

**F-40 — a second, sharper trap: a docket number in a responsive filing's caption is a citation to the filing it ANSWERS, not its own number.** The file banked as `…_dkt197_…` is captioned *"…RESPONSE TO THE MOTION FOR LIMITED INTERVENTION OF DESERET NEWS, ET AL. **(Dkt 197)**"* — and then **pin-cites into "Dkt 197" six times** (`at 1-2`, `at 3-4`, `at 4 & n.1`, `at 5`, `at 6-7`, `at 7`). **A document cannot pin-cite its own pages as another party's argument.** Dkt 197 is the *media's motion*, filed 2025-11-24; **the response is docket 213**. Utah practice puts the answered document's number in the responsive title, so **every filename in this library derived from a caption-embedded docket number needs re-checking** → **Q-80**.

**D-62 — OPEN: the docket number of the State's opposition to the motion to disqualify.** The defence's reply cites it as *"docket entry **279**"*; the DocumentCloud title says **289**. **Steelman for both being right:** the docket shows a `**** PRIVATE ****` opposition filed 2026-01-05 and a separate unmarked one filed 2026-01-10, so **279 may be the sealed original and 289 the public version.** That reconciliation is *inference*, not record. **Do not cite either number as established.**

**F-41 — 🚨 CASE NUMBER 251403576 IS NOT UNIQUE IN UTAH'S COURT SYSTEM, AND THIS LIBRARY HAS BEEN CITING IT BARE.** The banked XChange case-search printout (`dc27880529`) returns **four rows for the string `251403576`**: two are this case — **UTAH county · Provo District · case type `FS` (State Felony) · filed 2025-09-16** — and **two are an unrelated case in a different court**: **SALT LAKE county · Salt Lake City Justice Court · case type `MO` · filed 2025-04-07**, with an unrelated private defendant. **Every citation in this library must carry court and case type alongside the number** — *Fourth District Court, Provo, case type FS* — or it does not identify a case. The unrelated individual is a private person and is not named anywhere in this library. **Confidence: High** (read directly off the printout). → **Q-85**.

**D-63 — OPEN: whether one pretrial protective order exists or two.** The banked instrument is signed **2025-09-16, 08:22:46 PM**. The docket separately records *"09-23-2025 Filed protective order: Pre-Trial Protective Order — Signed September 23, 2025"* with a return of personal service the same day. **Nothing in the banked document indicates amendment or supersession.** Any file citing "the pretrial protective order" must now state **which signature date**.

---

## §5 · 🛠 Corrections to this project's own work, made in place today

**Five filenames created earlier today were wrong, and all five were wrong the same way: they were generated from the uploader's titles.** The errors were found by readers who opened the documents. **This is the §4 hazard biting the very acquisition that discovered it, within the same session.**

| Was | Is now | Why the old name was wrong |
|---|---|---|
| `…defendant-motion-disqualify-**prosecutor-judge**-conflict-interest_dkt250…` | `…defendant-motion-disqualify-utah-county-attorneys-office_dkt250…` | 🚨 **No judge is a target.** The motion seeks disqualification of a deputy prosecutor and, by imputation, the Utah County Attorney's Office. Judge Graf appears only in the caption. A full read of all 48 pages plus a normalised search finds no request to disqualify or recuse any judicial officer. |
| `…defendant-**renewed-motion-disqualify**-utah-attorney-general-memorandum_dkt348…` | `…defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348…` | 🚨 **It does not seek to disqualify the Attorney General.** It asks the court to **refer** the pending disqualification motion **to** the AG under Utah Code §17-68-304. **The AG is the proposed remedy, not the respondent.** This is the error most likely to have propagated a wrong inference. |
| `…order-transport-**virtual**-hearing_dkt24…` | `…order-transport-in-person-waiver-hearing_dkt24…` | The order transports the defendant to an **in-person** waiver hearing, Courtroom 4B, 2025-09-29 10:00. The virtual appearance was agreed **2025-09-26 — two days after this order**. |
| `…utah-county-**district-attorney**-press-release-after-shooting_dc27880543…` | `…utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543…` | **There is no Utah County District Attorney.** Utah County has a **County Attorney**. |
| `…utah-county-**district-attorney**-press-release-prosecutor-trial_dc27880535…` | `…utah-county-attorney-press-release-trial-team-roster_dc27880535…` | Same; and the release is a **personnel roster**, not a statement about prosecuting. |

**Two duplicate downloads were moved to `~/.Trash`** (not `rm`, per project rule): a second copy of the 07-08 supplemental notice (byte-identical SHA-1 `d8076450…` to the copy banked 2026-08-14), and the DocumentCloud re-render of the defence brief. **One file was kept and renamed** — see §6.3.

---

## §6 · Three hazards, tested rather than asserted

The library's standing complaint about itself is that *a caveat is a claim, and claims need verification acts* — and that hazards 1–8 have never been tested. **These three were tested today.**

### 6.1 🚨 STANDING HAZARD 13 — `grep` FAILS SILENTLY AND TOTALLY ON THE XCHANGE DOCKET FILES

Both banked XChange case-history extractions are classified by `file(1)` as **`data`**, not text. Consequence, measured:

| File | `file -b` | `grep -ci judd` | Python count |
|---|---|---|---|
| `2026-03-15_xchange-case-history-full_dc27880531.txt` | `data` | *(empty — no output at all)* | **4** |
| `2026-03-15_xchange-short-case-history_dc27880533.txt` | `data` | *(empty)* | 0 *(a true null)* |

**`grep` returns nothing — not "0", not "Binary file matches", nothing — on a file containing four occurrences.**

> ## 🚨 THIS SECTION WAS TWICE TOO SMALL AND ONCE PRESCRIBED A REMEDY THAT DOES NOT WORK — corrected at v1.3, same day
>
> **(1) Scope: 50 files, not two.** Every `.txt` in this artifacts folder except nine. No `.md`, `.json`, `.py` or transcript file anywhere is affected.
> **(2) Detector: `file(1)` is NOT a valid test** — two files it calls *"Unicode text, UTF-8"* are still silently skipped, because `file` tolerates a single trailing NUL. ✅ **The correct predicate is `NUL count > 0`.**
> **(3) 🚨 THE REMEDY THIS FILE PRESCRIBED WAS INSUFFICIENT. `\x00` IS NOT WHITESPACE TO PYTHON'S `\s`.** §6.1 told readers to work in Python with whitespace normalisation. **That leaves the NULs in place.** Measured: **953 NULs sat directly adjacent to a non-space character**, and **all 50 files carried NULs that survived normalisation** — so a phrase spanning a page break returned **a false null in Python too**. ⚠️ **Every reader dispatched on 2026-08-16 was given exactly that insufficient instruction**; their nulls were re-run under **Q-105**.
>
> ✅ **REMEDIATED, 2026-08-16 (Q-105): 1,189 NULs across 50 files replaced with `0x0C`** — the form feed the extractor should have emitted, and which **is** whitespace to both `grep` and `\s`.
>
> | verification | result |
> |---|---|
> | `grep -ci judd` on the full history | **4** — matches Python for the first time |
> | files still classified `data` | **0** |
> | NULs remaining in any `.txt` | **0** |
> | content identical modulo the separator, vs `git HEAD` | **50 of 50 — zero content changed** |
>
> ⚠️ **Why substitution rather than re-extraction, stated because it was a judgement and not a necessity.** `pdftotext` was tested on five affected documents and returns **~equivalent** text, so re-extraction was available. It was rejected because **re-extraction produces DIFFERENT text**, and **§6.2 of this very file measures that two extractions of one PDF differ in ways that produce false nulls.** Re-extracting would have **invalidated every verification act already performed against the current text**, including all of 2026-08-16's reader passes. The substitution is minimal, reversible, auditable, and content-preserving by construction — and it was safe to apply unambiguously because **zero affected files contained any pre-existing `0x0C`**.
>
> **Artifacts:** `docket-artifacts_2026-08-16_NUL-repair.py` (the script, with its invariants) and `docket-artifacts_2026-08-16_NUL-repair_SUPERSESSION.json` (old and new SHA-256 for all 50, per CLAUDE.md's supersession rule). ⚠️ **This is worse than every previous false-null hazard, because the others produced a *wrong answer* and this produces *no answer that looks like a wrong answer*.** **The library has run greps against these files.** Any null previously taken from the XChange printouts is **void and must be re-run** in Python with `errors='replace'` → **Q-81**.

### 6.2 Hazard 11 is stronger than stated — extraction substitutes characters, not just line breaks

Hazard 11 says a PDF text extraction is line-wrapped, so `grep` misses phrases spanning a break, and that **normalising whitespace** cures it. **Whitespace normalisation is not sufficient.** Two independent extractions of the **byte-identical same PDF** were compared after flattening all whitespace: they still differ. The differences are **not** line-wrap:

- **41 NUL bytes (`\x00`)** inserted in one extraction, attached to running page numbers.
- **A hyphen replaced by U+FFFE** in *"High-Powered"*.

Measured consequence, on the same underlying document:

```
grep 'High-Powered'  extraction A → 1 hit
grep 'High-Powered'  extraction B → 0 hits    ← FALSE NULL
```

**So: normalise whitespace AND strip control characters AND treat every hyphen, dash and quote as a character class before believing a null.** The two extractions are otherwise substantively identical, which independently **validates** the extraction banked on 2026-08-13.

### 6.3 The re-render hash trap — demonstrated, not assumed

The library holds the defence brief from an outlet mirror (banked 2026-08-13). Measured today:

| Artifact | SHA-1 |
|---|---|
| Outlet-mirrored PDF banked 08-13 | `a93801eef1bcbe30e0af4f569d91e841b266ce2b` |
| **DocumentCloud API `file_hash` for the same document** | `a93801eef1bcbe30e0af4f569d91e841b266ce2b` ✅ **identical** |
| The PDF DocumentCloud actually served today | `a408efc77654339c1eff1c13cde96339e5a25c34` ❌ **different** |

✅ **Two findings at once.** (a) **The outlet-mirrored copy this library banked IS the original uploaded to DocumentCloud, byte for byte** — independent re-verification of CR-WATCH-log v1.3. (b) **The served file is a re-render and its hash is meaningless for identity** — the trap is real and now demonstrated on a case artifact.

**The re-rendered PDF was trashed. Its text extraction was KEPT** as `2026-08-11_defendant-prelim-hearing-briefing_ALT-EXTRACTION-dc28551955.txt`, deliberately: a **second independent extraction of the same PDF** lets any grep-based null be cross-checked against a different character stream, which is precisely what §6.2 shows is necessary. **It is not a second document and must never be cited as one.**

---

## §7 · Machine-readable receipts

Retrieval receipts — per-document served byte counts, served SHA-256, API `file_hash`, source URL and retrieval date — are held at `dc224251_bank_receipts.json` and `dc_casenumber_bank_receipts.json` alongside the enumeration `dc224251_manifest.json`. ⚠️ **These currently sit in the session scratchpad and are NOT yet banked into the repository → Q-82.** Everything in §2 and §3 is reproducible from the API without them.

---

## §8 · What this file does NOT do

**This is an acquisition record. It characterises no document's contents beyond its title, date and facial type.**

Six independent readers read the newly banked material on 2026-08-16 and returned substantial findings — a previously unexamined **prosecutor-disqualification track**, a **closure/classification map** answering Q-75, a completed **evidence-preservation chronology** bearing on F-27, a **counsel-of-record roster** bearing on the transcript speaker-inference rule, and **Tier 1 eyewitness and sworn-geometry material** filed for unrelated purposes. **None of it is recorded here**, and none of it may be cited from this file.

⚠️ **Those findings are CANDIDATES, not findings, until they are written into evidence files with their own verification cycles** (LOOP §2). Destinations: **CR-E11** (disqualification track), **CR-E12** (closure and classification map), **CR-E13** (preservation chain), and corrections into **CR-E10** and **DNA-E01**. → **Q-84**.

**Residual scope — what this acquisition did NOT do:** it did not read the acquired documents (§8); did not verify any docket number against a court source; did not establish the uploader's identity; did not search DocumentCloud by party name or alternate case-number formats; did not attempt the XChange, Scribd or PACER routes; and did not re-test whether the DocumentCloud block that was live this morning will return. **Case posture untouched: as of 2026-08-16 Tyler Robinson has NOT been bound over, and the presumption of innocence applies throughout.**

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. Project 224251 completed 46/46 (28 newly banked, 0 failures); sibling projects 225170/225296 enumerated and returned no new documents; a case-number search found **9 documents outside the project, 7 of them new**, including material postdating the collection's 2026-03-14 ceiling. **F-39/F-40 open on the uploader-metadata hazard; D-62 and D-63 opened; standing hazard 13 added; hazard 11 strengthened; the re-render hash trap demonstrated.** Five of this project's own filenames corrected in place (§5). Q-79 through Q-84 raised. |
| **v1.1** | **2026-08-16** | 🚨 **§3 CORRECTED IN PLACE, and the error was this file's own F-39 committed within the hour.** v1.0 stated that the case-number search found **seven new documents**, and characterised a 663-page filing as *"a parallel FEDERAL track this library has never looked at."* **Both were wrong.** Verified by reading each document's first page: **two are third-party filings that merely CITE this case** — *State of South Carolina v. Murdaugh* (shackling/cameras) and an unrelated **civil** matter in the District of Utah (limited-intervention procedure) — **one is a hash-duplicate** of a document already in the project, and **three are one document uploaded three times.** **Honest count: two genuinely new documents of this case, both unread.** ✅ **The two false positives paid out anyway and it is recorded, not buried: F-80** puts the media-intervention request at **Docket 267** and the **Order Denying Intervention at Doc. 266 (2025-12-29)** — Tier 1 by this file's own rule, and exactly CR-E12's B-7 / Q-77 targets; **F-81** finds that a **YouTube recording of the partially-closed 2025-12-11 hearing was cited**, though the URL is OCR-mangled and the video ID is **not recoverable** (→ Q-97). **Root cause, stated against myself: §4 says a title is not the document; a search result's membership in a result set is the same kind of claim, and I believed it for the same reason — it was cheap. Relevance is established by reading, not by retrieval.** |
| **v1.2** | **2026-08-16** | 🛠 **REGISTER COLLISION CORRECTED, caught before it propagated.** v1.1 assigned the two findings recovered from the false positives as **F-42a / F-42b** — but **F-42 was already assigned in CR-E11** the same day (*the disqualification target never changed*). Suffixed sub-numbers are not a register convention here and would have hidden the clash from `queue-check.sh`, which counts strings. **Renumbered to F-80 and F-81**, the true next-free values (CR-E13 runs to F-79); all references updated in QUEUE.md. ⚠️ **This is standing hazard 6 in a new form — the earlier instance read a forward-looking "next is D-59" as a prior high; this one invented a sub-number to avoid checking the ceiling at all. Check the ceiling; do not decorate a number.** No finding's content changed. |
| **v1.3** | **2026-08-16** | 🚨 **§6.1 CORRECTED A THIRD TIME, AND REMEDIATED.** The hazard was **50 files, not two**; **`file(1)` is not a valid detector** (it tolerates a single trailing NUL, so two affected files read as clean text); and 🚨 **the remedy this file prescribed — Python plus whitespace normalisation — DOES NOT WORK, because `\x00` is not whitespace to `\s`.** Measured: **953 NULs adjacent to non-space characters, and all 50 files carried NULs surviving normalisation**, so phrases spanning a page break returned false nulls **in Python too**. ⚠️ **Every reader dispatched on 2026-08-16 was given that insufficient instruction** → nulls re-run under **Q-105**. ✅ **REMEDIATED: 1,189 NULs → `0x0C` across 50 files.** `grep` and Python now agree (`judd` = 4); **zero** files classified `data`; **zero** NULs remain; **content identical modulo the separator on 50 of 50, proven against `git HEAD`.** ⚠️ **Substitution was chosen over re-extraction deliberately** — `pdftotext` returns ~equivalent text and was available, but re-extraction would have produced different text and **invalidated every verification act already performed**, per this file's own §6.2. Script and supersession record (old/new SHA-256 for all 50) banked alongside the artifacts. |
| **v1.4** | **2026-08-16** | ⚠️ **§0.1 PROVISIONAL DEPENDENCIES added (LOOP §2 discipline).** This file is the **root of a five-file dependency graph and is itself `[PROVISIONAL]`** — F-39/F-40/F-41 are relied on by CR-E11, E12, E13 and E14, so **if F-39 or F-40 falls, docket-number claims move in four files at once.** Its own dependency on CR-ACQ-2026-08-14C is stated. |
