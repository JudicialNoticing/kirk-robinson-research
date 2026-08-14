# CR-WATCH-log — Docket Watch Run Log

**Purpose:** one row per run of the [DOCKET-WATCH.md](../DOCKET-WATCH.md) spec. **A run that finds nothing still writes a row** — a watch with gaps in its log is indistinguishable from a watch that was not running.
**Case:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr.
**Standing constraint:** a run may acquire and bank freely and may update DOCKET-WATCH's own calendar table with an observed status. **It may never change a case-posture statement in a topic file, resolve a register entry, characterise a filing's contents beyond its title and date, or infer an outcome from a filing's existence.** D-51 is why.
**Status:** **v1.4 — THE GAP'S CENTRAL QUESTION IS RESOLVED: THE ROUTINE FIRED ALL THREE TIMES; ITS REPORTS WERE DELIVERED AND NEVER PASTED.** Established 2026-08-14 by direct API retrieval of the routine's own run sessions — see [Routine-liveness resolution — 2026-08-14](#routine-liveness-resolution--2026-08-14--not-a-run-of-the-spec). ⚠ **With it came a route finding this file did not have: every cloud firing since 2026-08-05 has run BLIND** — the cloud session's egress proxy 403-blocks all direct HTTPS document fetches (a control fetch of `example.com` included), so those runs were **search-index-only**. **The routine is enabled; next firing Sat 2026-08-15 09:00 ET — and it will run blind again unless its environment changes.**
**Prior status text (v1.3), retained:** **Run 3 logged 2026-08-13; a separate Q-45 ACQUISITION ATTEMPT the same date FAILED and is logged below the runs.** ⚠ **The State's 2026-07-28 opening brief is still NOT HELD.** Its only located mirror (Scribd) is behind a JavaScript anti-bot interstitial that every automated route hits; **"Q-45 is actionable" proved to mean "the mirror is located," not "the document is retrievable."** See **[Q-45 acquisition attempt — 2026-08-13](#q-45-acquisition-attempt--2026-08-13--outcome-not-obtained)**.
**Prior status text, retained:** **v1.2 — Run 3 logged 2026-08-13, a CATCH-UP RUN AFTER A 12-DAY GAP.** 🚨 **THE WATCH WENT DARK BETWEEN 2026-08-01 AND 2026-08-13.** The durable cloud routine (`trig_016faLfbQWCz72M463Dy8HsL`, Wednesdays and Saturdays 09:00 ET, first firing 2026-08-05) had **three scheduled firings — Wed 08-05, Sat 08-08, Wed 08-12 — and none produced a row here.** It is **REPORT-ONLY**: the cloud environment was refused access to the private repository, so **its output must be pasted into this file by hand**, and no hand-paste occurred. **Whether the routine fired and was never pasted, or is dead, is NOT ESTABLISHED from inside this repository — 👤 check `/schedule`.** Runs 1, 2 and 3 were all executed by hand. **Next scheduled firing: Sat 2026-08-15. Next hard case date: Tue 2026-08-18 (State's reply). Oral argument: Tue 2026-09-01.**

---

## Run index

| # | Date | Trigger | Headline | Escalated? |
|---|---|---|---|---|
| **1** | **2026-07-28** | first run; State's opening brief due this date | **State's opening probable-cause brief reported FILED 2026-07-28** (T1 via T3, single independent source). 09-01 argument still stands. **A previously unknown Rev transcript located: a contempt hearing, c. 2026-06-22.** | No — no escalation trigger met |
| **2** | **2026-08-01** | scheduled follow-up; the durable routine created this date | **A PUBLIC MIRROR OF THE STATE'S BRIEF EXISTS AND IS RETRIEVABLE** — 28 pp., Scribd, closing Run 1's "no public mirror" null and giving **Q-45** a route. The 07-28 filing date is now **multi-sourced** (Run 1 had one). **The DocumentCloud API is no longer bot-gated** and project 224251 was enumerated for the first time (46 documents). ⚠ **28 pp. is the LENGTH; 35 was the page LIMIT.** | No — no escalation trigger met |
| — | *2026-08-05* | scheduled firing | 🚨 **NO ROW** — ~~the watch did not run, or ran and was never pasted; not established which~~ ⚠ **RESOLVED 2026-08-14: IT RAN** (session `cse_015Hy9bdS2JDtiPsi4U2RNpR`, 33 turns; report written, pushed and delivered — never pasted; **egress-blinded, search-index only**). → [liveness resolution](#routine-liveness-resolution--2026-08-14--not-a-run-of-the-spec) | *The run itself declared escalation MET — route trigger, environmental* |
| — | *2026-08-08* | scheduled firing | 🚨 **NO ROW** — ⚠ **RESOLVED 2026-08-14: IT RAN** (session `cse_011tF4hurEd5KesDxvPQkdSk`, 28 turns; report delivered, never pasted; **egress-blinded**) | *Escalation MET — route trigger, environmental* |
| — | *2026-08-12* | scheduled firing | 🚨 **NO ROW** — ⚠ **RESOLVED 2026-08-14: IT RAN** (session `cse_01QXdVjFPwhLrbJpnybTJFSp`, 29 turns; report delivered, never pasted; **egress-blinded**). ⚠ **The 2026-08-11 defence deadline, named by Run 1 as "the next checkpoint," passed inside this gap unchecked by any document-capable pass** — the run itself recorded the 08-11 filing as "no observation either way," which Run 3 later settled by banking the brief | *Escalation MET — route trigger, environmental* |
| — | *2026-08-13* | **Q-45 acquisition attempt — NOT a run of the spec** | **THE STATE'S OPENING BRIEF COULD NOT BE OBTAINED.** Six routes tried, one identified-but-gated (Scribd doc **1067587104**, ID recorded here for the first time), four scoped nulls, two owner-only. **Nothing banked; contents not recorded; no CR-E08 written.** Collateral: **project 224251 now enumerates 46/46**, and the defence brief's DocumentCloud copy is **byte-for-byte the file already banked** | *n/a — not a run* |
| **3** | **2026-08-13** | **catch-up after the gap was found from outside this repo** | **THE DEFENCE BRIEF IS FILED AND BANKED — the first primary filing this project holds as a document rather than through reporting.** *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* signed and served **Tue 2026-08-11**, 41 pp. / 35 printed. ⚠ **No clerk file-stamp visible — two of three provenance elements present.** **09-01 stands**, confirmed by a **T2** official item dated 08-11. **No continuance motion found** (scope stated; no docket consulted). Contents deliberately unread. | No — no escalation trigger met. ⚠ **But the trigger list contains no trigger for "the watch stopped," which is why the gap went unnoticed** |

---

## Run 1 — 2026-07-28

**Method:** three parallel search routes (filings / Rev transcripts / scheduling), web search and direct fetch only. **No docket access.** Every filing fact below is **T1 via T3** — known through reporting, never through reading the filing. Retrieval date for everything in this run: **2026-07-28**.

### 1. Findings

**(a) The State's opening probable-cause brief is reported filed — on time, on the conditional date.**

| | |
|---|---|
| **What is reported** | The prosecution "on Tuesday filed the first of three written briefs" ordered by Judge Graf |
| **Source** | Fox News, byline Stepheny Price. Published **2026-07-28, 20:38:15 EDT** (`datePublished`, read from the article HTML) |
| **URL** | `https://www.foxnews.com/us/charlie-kirk-murder-case-straight-forward-gets-prosecutors-argue-case-nears-trial-decision` |
| **Tier** | **T1 via T3.** The filing itself is **not held.** No primary document was located (see §2) |
| **Independence** | **One source.** Two further copies located (`jammin999fm.com`, `jingletree.com`) are **syndications of the same Fox text** and are not corroboration — syndicated recaps are one source, not many |

**Date cross-check, run against this project's own Tier 1 finding rather than the article.** The article dates the filing only as "on Tuesday." **2026-07-28 is a Tuesday** — derived from D-51 as reversed and confirmed: the preliminary hearing's Day 1 sat **Monday 2026-07-06**, so 07-13, 07-20 and 07-27 are Mondays and **07-28 is a Tuesday**. The article's "Tuesday" and its publication date agree. *(One machine-extraction caveat, logged because this project has been burned by exactly this: a first automated pass over the article returned a garbled filing date of "July 30", and another returned "July 23" — a Thursday. Both were wrong; the second pass against the article text gave only "on Tuesday." **Machine date-extraction from this article is unreliable and the date above rests on the publication timestamp plus the day-of-week check, not on an extracted date.**)*

⚠ **What is NOT recorded here, deliberately.** The Fox article also **characterises the brief's contents and quotes from it**. DOCKET-WATCH.md forbids a watch run from characterising a filing's contents beyond its title and date, and **Q-04's decisive artifact is the filed brief itself**, not reporting about it. Those characterisations are therefore **left unrecorded pending acquisition of the document**. This is the standing-hazard-1 discipline (a quotation by another party is reliable as to the words, never as to the document) applied before the fact rather than after it.

**Consequence for the conditional.** CR-ACQ §5.1 records that the 07-28 date was **expressly conditional** on the court reporter delivering the transcript by 2026-07-13, and START-HERE warned that a slip might mean the reporter rather than the case. **On this report the date did not slip.** No inference is drawn about the transcript's delivery; it is simply no longer a live worry for this deadline.

**(b) The 2026-09-01 oral argument still stands; no continuance motion found.** The named risk — lead defence counsel **Nester's stated trial conflict** with that week, declined on the record (CR-ACQ §5.1) — remains open and unrealised. The most recent located coverage (the Fox article above, published the evening of 2026-07-28) **affirmatively restates** that oral arguments are scheduled for Sept. 1. **Six targeted searches found no defence motion to continue and no report of the date moving.** ⚠ **This is "no coverage found via the listed routes," not "nothing happened"** — an unreported filing would be invisible to every route available this session. **Next natural checkpoint: the defence reply due 2026-08-11**, the likeliest vehicle for such a motion.

**(c) NEW — a proceeding this library did not know about.** Rev carries a page titled "**Tyler Robinson Comtempt Hearing**" *[sic — Rev's own title and slug misspell "Contempt"]*, **page date 2026-06-23**. Applying the established one-business-day publication lag (D-51), the proceeding sits at approximately **Monday 2026-06-22**. It **predates the preliminary hearing** and is therefore not a "new filing," but it is **entirely absent from the library's transcript inventory**, which holds only the five hearing days. **Nature and subject unknown; not retrieved this run.** → queued.

**(d) A filing at the hearing/argument boundary, previously unlogged.** Fox News live coverage of 2026-07-10 reports that shortly after court adjourned, **an attorney for the Kirk family filed a motion asking Judge Graf to make the probable-cause determination no later than Sept. 1**. Reported via search-result snippet; the live page was not separately fetched. **T1 via T3, single source, contents not characterised.** Consistent with CR-ACQ §5.1's record that the victim's representative asked for speed while taking no position on the briefing. → queued.

**(e) Corroboration of an existing Tier 1 detail.** KSL's 2026-07-10 report gives "**four hours allocated**" for oral argument, consistent with Graf's "*it sounds like* up to two hours per side" (CR-ACQ §5.1). Recorded as corroboration only; **CR-ACQ §5.1 remains canonical** and is not amended — the transcript is the better source and already says this.

### 2. Nulls — each is a claim about the search, and scoped as one

| Sought | Result | Where it was looked for |
|---|---|---|
| **A public mirror of the State's brief (PDF)** | **NOT FOUND** | Fox article HTML (474,605 bytes, **zero** `.pdf` / DocumentCloud / Scribd links); `static.foxnews.com`, which **does** host prior case PDFs in this matter (the ballistics motion, the redacted PC affidavit) but surfaced no brief; **Utah County Attorney media page** (`atty.utahcounty.gov/media`) — loads, most recent Robinson item is **2026-06-26**, brief not posted; **DocumentCloud project 224251** — still bot-gated |
| **A ruling on the bullet-fragment / VCM motion** | **NOT FOUND** | Three query variants. Surfaced the defence motion itself and prior coverage, but **no granted/denied/moot disposition**. Open since the first acquisition pass (CR-ACQ §8) |
| **Any Rev transcript newer than Day 5** | **NONE EXISTS, on positive enumeration** | **Seven** Rev pages of this case positively identified and fetched — the five hearing days (Day 1 confirmed live at its divergent slug `ut-v-tyler-robinson---day-1`), the contempt-hearing page at (c), and a 2025-09-17 press briefing. **The slug trap was respected:** this null rests on enumerating what exists, not on 404s of guessed slugs |
| **Deseret / SLTrib / KSL / ABC4 / Fox13 coverage of the 07-28 filing** | **NOT FOUND at retrieval time** | The filing was reported at 20:38 EDT on the retrieval date. **Local coverage may simply not have run yet**; recheck next run |

### 3. Access routes — two changes

| Route | Status this run |
|---|---|
| **`legacy.utcourts.gov` press notices** | ✅ **NOW RETRIEVED — route works.** Previously carried in DOCKET-WATCH as Tier 2, unretrieved. The archive index loads; it holds **exactly one** Robinson entry, "PUBLIC INFORMATION REGARDING THE TYLER ROBINSON PRELIMINARY HEARING" (2026-07-06), covering hearing-week logistics only — **no post-07-10 dates, no September 1, no continuance language.** Nothing newer posted |
| **`abc4.com`** | ⚠ **NEW BOT-BLOCK — HTTP 403.** A continuance-adjacent ABC4 article could not be retrieved. From search context it concerns the **pre-hearing May 2026** stay request, **not** the 09-01 argument — flagged so it is not later mistaken for a post-07-10 continuance motion. **Characterisation is from snippet context only and is unverified against the article text.** ABC4's case timeline was also 403-blocked |
| **DocumentCloud project 224251** | **Still blocked.** Page shell loads but the document list is JS-rendered; the API returned a Cloudflare 403 (Ray ID `a2289fe618a2c8e3`). Unchanged (Q-32) |
| **Utah XChange** | **Not attempted** — paywalled, `human` gate, no account (Q-31) |

**Note on §4's escalation rule.** DOCKET-WATCH escalates immediately if "a route that previously worked starts failing." **ABC4 is a new block on a route this project had not previously used successfully**, so this is a newly-discovered closed door rather than a degradation — **not an escalation trigger**, but logged so a future run can tell the difference.

### 4. Escalation check

| Trigger | Met? |
|---|---|
| A bindover ruling issues | **No** — Robinson has **not** been bound over as of 2026-07-28 |
| The 09-01 date moves | **No** — affirmatively restated as standing |
| A filing sealed or unsealed | **No** — none observed |
| A previously working route starts failing | **No** — see the note above |

**No escalation.**

### 5. Queued out of this run

| → | Item |
|---|---|
| **Q-45** | **Acquire the State's opening probable-cause brief.** Reported filed 2026-07-28; not held. Until it is, **its contents are unrecorded by this project**. Feeds Q-04 |
| **Q-46** | **The contempt-hearing transcript, c. 2026-06-22** — a proceeding absent from the library's inventory. Rev page dated 2026-06-23 |
| **Q-47** | **The Kirk-family motion of 2026-07-10** re a probable-cause determination by Sept. 1 |

---

## Run 2 — 2026-08-01

**Method:** three parallel routes (filings / calendar / Rev transcripts), web search and direct fetch only. **No docket access.** Retrieval date for everything in this run: **2026-08-01**. **Every filing fact below is T1 via T3 unless expressly marked otherwise.**

### 1. Escalation check — NO TRIGGER MET

| Trigger | Met? |
|---|---|
| A bindover ruling issues | **No.** Three web searches run; nothing found. **Tyler Robinson has NOT been bound over as of 2026-08-01** and is presumed innocent |
| The 09-01 date moves | **No.** Affirmatively restated as standing by Reavy, ABC News and KUTV. **No continuance motion found** |
| A filing sealed or unsealed | **No.** All sealing/unsealing events returned are dated 2026-07-10 or earlier |
| A previously working route starts failing | **No.** The only route change is a route **re-opening** — see §4 |

### 2. Filings

- ⚠ **THE STATE'S OPENING BRIEF NOW HAS AN ACQUISITION ROUTE.** A **28-page "Memorandum in Support of Preliminary Hearing Bindover," Case No. 251403576**, is hosted on **Scribd by The Post Millennial** (HTTP 200, download offered). **This closes Run 1's "no public mirror found" null.** → **Q-45.** ⚠ **The document has NOT been banked and its contents are NOT recorded** — that is the next act, and **provenance verification is a SEPARATE act from reading it**: locate the electronic file-stamp line, the signature block and date, and the certificate of service, **none of which was visible in the retrieved extract.** Until then the copy is an upload of unverified provenance, not a filed document.
- ⚠ **28 PAGES IS THE ACTUAL LENGTH. 35 WAS THE COURT-ORDERED PAGE LIMIT.** Two independent outlets (KUTV, Fox News) state 28. **`DOCKET-WATCH.md` already says "35-page limit" correctly, so no library file requires correction** — but **no file may write "35 pp." as a page count.** *(This run's own task framing made that conflation; recorded so the next run does not.)*
- **The 2026-07-28 filing date is now MULTI-SOURCED.** Run 1 rested on one independent source (Fox News). As of this run: **Fox News, Pat Reavy, KUTV, ABC News, Washington Examiner, and Deseret/KSL.** ⚠ **Source independence for the FILING EVENT is upgraded; the DOCUMENT remains unheld. It stays T1 via T3 and must not be silently promoted.**
- **A NEW ARTIFACT THE LIBRARY DOES NOT HOLD:** "**Supplemental Notice Concerning Access to Evidence Presented in Open Court**" *(title carries a typo, "Evidennce", in the source metadata)*, DocumentCloud doc 28443912, **4 pages, created 2026-07-09 — i.e. filed DURING hearing week, between Day 4 and Day 5.** ⚠ **Its adjacency to the Exhibit 12.1 publication question rests on the TITLE ONLY.** Not retrieved; contents uncharacterised.
- **Second source for Q-47** (KUTV): the Kirk family, through their attorneys, asked the court to rule by September 1, citing Utah's Crime Victims' Rights Act. Run 1 had a single search snippet. **Still T1 via T3; the motion itself remains unheld.**
- **The bullet-fragment motion ruling remains unobtained after two runs.**

### 3. Calendar — observed status

| Date | Event | Observed status, 2026-08-01 |
|---|---|---|
| 2026-07-28 | State's opening brief, 35-page limit | **Reported filed**, 28 pp., multi-sourced |
| **2026-08-11** | Defence response, 35-page limit | **Pending. Every post-07-28 source restates it as standing.** The next hard checkpoint |
| 2026-08-18 | State's reply, 18-page limit | **Pending**, on a thinner base — only Deseret/KSL restates it |
| **2026-09-01, 10:00** | Oral argument, in person | **Pending and standing.** No continuance motion found. ⚠ Nester's trial-week conflict remains an open, named risk |
| after 09-01 | Bindover ruling | **Pending. Robinson has NOT been bound over** |

### 4. Route status — one route RE-OPENED

- ⚠ **THE DOCUMENTCLOUD API IS NO LONGER BOT-GATED.** Run 1 recorded a Cloudflare 403; on 2026-08-01 `api.www.documentcloud.org/api/documents/search/` returned **HTTP 200 with valid JSON**, honouring `+project:224251` filtering and cursor pagination. **Project 224251 was POSITIVELY ENUMERATED for the first time: count field = 46; 45 distinct documents listed across two cursor pages.** ⚠ **One of the 46 is unaccounted for in the enumeration and no claim is made otherwise.** **The DocumentCloud WEB UI remains JS-gated** — so **Q-32 should be SPLIT, not closed.**
- **Q-03 partially unblocked:** two docket-listing documents are now retrievable without the XChange paywall, **but both are current only to 2026-03-15** and so do not cover this watch window. **The blocker on a CURRENT docket is unchanged.**
- **Collateral benefit relevant to standing hazard 9:** project 224251 holds a **"prosecutor David Sturgill biography"** document. **Sturgill is the examining prosecutor who has NO speaker label anywhere in Rev's Day 1 transcript** (CR-E05 §1.2).
- **abc4.com** and the DocumentCloud **web UI** have now failed on two consecutive runs.

### 5. ⚠ Two hazards this run hit

- **MACHINE EXTRACTION WAS UNRELIABLE AGAIN, ON FOUR COUNTS — and Run 1 logged this hazard for the same article set.** Three separate page-extractions asserted the filing date as "**Tuesday, July 29, 2026**"; **2026-07-29 is a Wednesday.** One extraction reported the **defence** deadline as Aug. 18. **Do not take a date from an extraction without a day-of-week check.**
- **A CONFLATION TRAP, flagged for the next run.** Searches for a ruling on the **bullet-fragment motion** repeatedly surface the **2026-06-26 CONTEMPT ruling** instead — Judge Graf finding a Deputy Utah County Attorney in civil contempt over public comments *about* the bullet fragment. **These are different matters.** ⚠ **It also means TWO DATES are now in play for Q-46**: the Rev contempt-hearing page (proceeding c. 2026-06-22) and this 06-26 ruling. **Whether they are the same event is not established.**

### 6. Deliberate non-recording

**Every outlet retrieved this run characterises the brief's argument and several quote from it directly; the search layer surfaced such quotations unprompted and repeatedly. NONE of it is recorded here.** DOCKET-WATCH forbids a watch run from characterising a filing's contents beyond title and date, and **Q-04's decisive artifact is the document itself.**

### 7. Blind spot, stated

**No located source is dated after 2026-07-29. This run has a three-day gap at its own leading edge.** An unreported filing or a stipulated extension would be invisible to it, because **no docket was consulted.**

### 8. Queued out of this run

| → | Item |
|---|---|
| **Q-45** | ~~**Now actionable** — bank the Scribd mirror, then verify provenance as a separate act before reading~~ ⚠ **QUALIFIED 2026-08-13, not struck as wrong:** the mirror is real and was re-located (Scribd doc 1067587104), but **it is not retrievable by any automated route** — every Scribd endpoint returns a JavaScript "Client Challenge" interstitial. **"Actionable" meant *located*, not *retrievable*.** See the Q-45 acquisition attempt below |
| **Q-32** | **Split**: API route open, web UI still gated |
| **Q-46** | Two dates now in play — establish whether the 06-22 proceeding and the 06-26 ruling are the same event |
| **NEW** | The 2026-07-09 "Supplemental Notice Concerning Access to Evidence Presented in Open Court," 4 pp. |
| **NEW** | Consider escalating **Q-32** (interactive browser) from nice-to-have to a blocking dependency before 09-01 |

**No register entry was assigned or moved. No case-posture statement in any topic file was altered.**

---

## Run 3 — 2026-08-13 · CATCH-UP RUN AFTER A 12-DAY GAP

> 🚨 **SCOPE CAVEAT, STATED FIRST — THIS RUN COVERS A WINDOW THE WATCH DID NOT WATCH.**
> Run 2 was logged **2026-08-01**. The durable routine's scheduled firings on **Wed 2026-08-05, Sat 2026-08-08 and Wed 2026-08-12** produced **no rows in this file**. This run is a single catch-up pass covering **2026-08-01 → 2026-08-13**, not a reconstruction of three runs, and **no rows are backfilled for them** — a fabricated row is worse than a missing one.
> ⚠ **Which failure occurred is NOT ESTABLISHED.** Two possibilities are consistent with the evidence and they need different fixes: (a) the routine fired and its reports were never hand-pasted, or (b) the routine is dead. The routine is **report-only** — the cloud environment was refused the private repo (HTTP 403) — so it cannot write here itself, and from inside this repository the two cases are indistinguishable. **Determining which is a 👤 owner action** (check `/schedule` for `trig_016faLfbQWCz72M463Dy8HsL`). This is exactly the condition the spec names: *"A watch with gaps in its log is indistinguishable from a watch that was not running."*
> **Detection path:** the gap was found on 2026-08-13 from outside this repository, during an unrelated session-state reconstruction, because this file's mtime was 12 days old. **It was not caught by the watch.**

**Method:** three search routes (filings / scheduling / continuance-specific), plus **one direct primary-document retrieval and one Tier 2 official-page read**. No docket access. Retrieval date for everything in this run: **2026-08-13**.

### 1. Findings

**(a) THE DEFENCE RESPONSE WAS FILED ON TIME — and unlike the State's brief, THIS ONE IS HELD.**

| | |
|---|---|
| **Document** | **"DEFENDANT TYLER JAMES ROBINSON'S PRELIMINARY HEARING BRIEFING"** *(title as printed on the first page)* |
| **Caption** | STATE OF UTAH, Plaintiff, vs. TYLER JAMES ROBINSON, Defendant — **Case No. 251403576**, **Honorable Tony F. Graf, Jr.**, In the Fourth Judicial District Court, Provo Department, in and for the County of Utah, State of Utah |
| **Date** | **Tuesday, 2026-08-11** — *"RESPECTFULLY SUBMITTED this 11th day of August, 2026"* ✅ **Day-of-week checked: 2026-08-11 is a Tuesday**, consistent with the calendar's "all three briefing dates fall on Tuesdays." *(Run 2 logged machine extraction returning wrong days-of-week on four counts; this date is verified by direct reading of the document, not extraction.)* |
| **Signature block** | `/s/` Kathryn N. Nester (13967) · `/s/` Michael N. Burt (pro hac vice) · `/s/` Richard G. Novak (pro hac vice) · `/s/` Staci Visser (14358) — "Attorneys for Defendant, Tyler James Robinson" |
| **Certificate of service** | **PRESENT**, `/s/` Staci Visser: *"served via the Court's electronic filing system on the 11th day of August, 2026"* |
| **Length** | **41 PDF pages; internal printed page numbering runs to 35** (body ends p. 33, signature p. 34, certificate p. 35). ⚠ **35 is also the court's page LIMIT for this brief. LENGTH AND LIMIT COINCIDE HERE — do not read the coincidence as a finding either way, and do not repeat Run 2's conflation hazard in reverse.** |
| **Route** | Direct fetch, `static.foxnews.com/foxnews.com/content/uploads/2026/08/robinson-prelim-filing.pdf` — an **outlet-mirrored filing**, the same route class that produced both previously banked motions |
| **Banked** | ✅ `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.pdf` + `.txt` extraction · SHA-256 `c3f394372192a6a3c6b791839a22a9ce4be43aea6f9985b9fc3703633bfde0e4` |

⚠ **PROVENANCE — ONE ELEMENT IS MISSING, AND IT IS THE SAME ONE Q-45 TURNS ON.** The signature date and the certificate of service both attest e-filing on 2026-08-11, but **no clerk file-stamp / e-filing header line is visible anywhere in the text layer**. Per Run 2's own standard — *"provenance verification is a SEPARATE act from reading it: locate the electronic file-stamp line, the signature block and date, and the certificate of service"* — **two of those three are present and one is absent.** This copy is therefore **an outlet-hosted upload carrying the defence's own attestation of filing, not a court-stamped document.** It is materially better provenance than the State's Scribd mirror (which has none of the three verified) and still **short of a stamped filing.** Treat as **T1 document text with an unverified stamp**, and do not silently promote.

**(b) THE 2026-09-01 ORAL ARGUMENT STILL STANDS — now confirmed by a Tier 2 official source dated the same day as the defence filing.**

The **Utah County Attorney's Office media page** (`atty.utahcounty.gov/media/ckpr`, retrieved 2026-08-13) carries an item dated **2026-08-11: "Preliminary Hearing Argument set for September 1, 2026, in the Tyler Robinson Case."** This is a **named-official (Tier 2)** statement of the date, current to the day the defence brief was filed. **Escalation trigger "anything moving the 09-01 date": NOT MET.**

**(c) NO MOTION TO CONTINUE FOUND — with its search scope stated.**

The spec directs a *specific* check for a defence motion to continue, because lead counsel stated a trial conflict with the 09-01 week on the record and was declined. **None was found.** ⚠ **Scope of that null, per the "absence of evidence is a finding with a scope" rule:** the search covered web search on the continuance question, the Utah County Attorney media page, and the four corners of the banked 08-11 brief. It did **not** cover the court docket (still paywalled, Q-31/Q-03), and **a motion filed 08-12 or 08-13 would very likely not yet be reported.** This is **not** evidence that no such motion exists — only that none surfaced on the open routes as of 2026-08-13.

**(d) The State's reply deadline is corroborated as Tue 2026-08-18** — reporting of the briefing schedule (State 07-28 → defence 08-11 → State's reply 08-18) matches the calendar in DOCKET-WATCH, which took it from CR-ACQ §5.1. ✅ Day-of-week checked: 2026-08-18 is a Tuesday. **This is the next hard date, and it falls five days from this run.**

### 2. Escalation check — NO TRIGGER MET

| Trigger | Status |
|---|---|
| A bindover ruling issues | **No.** None found; the ruling follows the 09-01 argument |
| The 09-01 date moves | **No** — affirmatively confirmed standing by a T2 source dated 2026-08-11 |
| A filing is sealed or unsealed | **No** — none found |
| A previously working route starts failing | **No.** The Utah County Attorney page **still works and has moved** (its latest Robinson item was 2026-06-26 at Run 1; it is now 2026-08-11). Outlet-mirrored filings still work — that route produced this run's primary document |

**The 12-day gap is itself the finding of this run.** It met no escalation trigger as defined, and the spec's trigger list does not contain "the watch stopped running" — which is why nothing raised it.

### 3. ⚠ Deliberate non-recording

**The banked brief's arguments, and every outlet characterisation of them retrieved this run, are NOT recorded here.** DOCKET-WATCH forbids a watch run from characterising a filing's contents beyond its title and date, and the document is now held, so reading it is a **separate act** belonging to an evidence file under the two-layer discipline — not to a watch row. The search layer again surfaced outlet summaries unprompted; none is reproduced.

⚠ **A second, independent reason for restraint here.** The text extraction incidentally surfaced material concerning the **sexuality and gender identity of Mr. Robinson and of Mr. Twiggs**, a private individual. **None of it is recorded in this file.** Under CLAUDE.md's living-persons rule, such material is admissible only insofar as it bears on a public question under investigation, and that determination belongs to a reasoned evidence-file pass with the analyst/recording layers kept separate — **not to a docket-watch row, and not to an incidental extraction.**

### 4. Blind spot, stated

**This run consulted no docket.** The paywalled-XChange blocker (Q-31) is unchanged, so any filing not mirrored by an outlet or announced by the prosecutor's office is invisible to it — including, specifically, a continuance motion filed in the last 48 hours. **The 08-01 → 08-13 window was covered by one pass at its trailing edge, not by the three scheduled passes**, so a filing that appeared and was superseded inside that window would leave no trace here.

### 5. Queued out of this run

| → | Item |
|---|---|
| **👤 URGENT** | **Determine whether `trig_016faLfbQWCz72M463Dy8HsL` is alive** (check `/schedule`). Next firing **Sat 2026-08-15**; if dead, it must be recreated **before Tue 2026-08-18** |
| **👤** | **Grant the Claude Code GitHub App access to `JudicialNoticing/kirk-robinson-research`** — DOCKET-WATCH calls this "the one outstanding step," and its absence is the mechanism by which this watch went dark: a report-only routine's output must be hand-pasted, and no hand-paste occurred |
| **NEW** | **Add "the watch itself has not run" to the escalation-trigger list** in DOCKET-WATCH. Every existing trigger describes an event *in the case*; none describes a failure *of the watch*, which is why 12 days passed unnoticed |
| **Q-45 analogue** | The defence brief is banked and **its contents are unread by design.** A reasoned read belongs in a CR-E evidence file, not here |
| **Q-45** | Unchanged — the **State's** 07-28 brief remains unbanked and its Scribd mirror unverified. ⚠ **ATTEMPTED AND FAILED the same day; see the Q-45 acquisition attempt below.** The mirror is still unverified as to provenance for the same reason it is unbanked: **nothing can read it faithfully from here** |
| **NEW** | **Locate a court-stamped copy** of the 08-11 brief to close the missing file-stamp element. ⚠ **STILL OPEN as of 2026-08-13 — one candidate route was checked and is NOT independent:** the brief is now on DocumentCloud (doc **28551955**, uploaded 2026-08-12 by Epoch Times), but DocumentCloud's own `file_hash` for it equals the SHA-1 of the copy already banked, so **it is the same file, not a second source.** See the acquisition attempt below |
| **Q-31 / Q-03** | Unchanged — no current docket. ⚠ **This run is the second consecutive one whose blind spot is docket access**; consider promoting it to a blocking dependency before 09-01, as Run 2 already suggested for Q-32 |

**No register entry was assigned or moved. No case-posture statement in any topic file was altered.** ⚠ **As of 2026-08-13, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.**

---

## Q-45 acquisition attempt — 2026-08-13 · OUTCOME: NOT OBTAINED

> **This is not a run of the DOCKET-WATCH spec.** It is a single-purpose execution attempt on **Q-45 / Q-56** — *acquire the State's opening probable-cause brief, reported filed 2026-07-28* — logged here because the watch log is where this project's access routes live and because **a failed retrieval is an access-path caveat, not something to drop silently** (CLAUDE.md, operational rules).
> **Why it was attempted now:** the library holds the **defence** brief as a primary document and has never held the **State's**. The State's reply is due **Tue 2026-08-18** and oral argument is **Tue 2026-09-01**.
> **Outcome, stated first: the document was NOT obtained. Nothing was banked. No SHA-256 exists because no bytes were retrieved. Its contents remain unrecorded, and no evidence file was written** — an evidence file about a document this project cannot read would be the exact error the library exists to avoid.
> ⚠ **28 pp. is the reported LENGTH of that brief. 35 was the court's page LIMIT. Do not conflate** (Run 2's standing warning, restated because this is now the third file to touch the figure).
> ⚠ **Tyler Robinson has NOT been bound over. Presumption of innocence applies. Nothing here characterises what either party argues.**

**Method:** direct HTTP fetch and public-API queries only. **Retrieval date for everything below: 2026-08-13.** Byte counts and status codes are as observed on that date.

### 1. Routes tried, and what each returned

| # | Route | Result |
|---|---|---|
| **R1** | **The Scribd mirror — LOCATED AND IDENTIFIED, NOT RETRIEVABLE** | ⚠ **The blocking failure.** See §2 |
| **R2** | **Web archives of that mirror** | **No capture exists at the Wayback Machine** — CDX prefix query on `scribd.com/document/1067587104` returns **zero rows** (positive enumeration, not a 404 guess). **archive.today: NOT ESTABLISHED** — `archive.ph/newest/…` returned **HTTP 429** (rate-limited), as did `archive.org/wayback/available`. A retry on another day is cheap and is queued |
| **R3** | **Outlet-mirrored PDF — the route class that produced the defence brief** | **NOT FOUND.** The Fox News article of 2026-07-28 (`foxnews.com/us/charlie-kirk-murder-case-straight-forward-gets-prosecutors-argue-case-nears-trial-decision`, HTTP 200, **476,625 bytes**) contains **zero `.pdf`, Scribd or DocumentCloud links**; every `static.foxnews.com/…/uploads/` path in it is an image. **This reproduces Run 1's result on the same URL 16 days later.** Wayback CDX prefix enumeration of `static.foxnews.com/foxnews.com/content/uploads/2026/07/` and `…/2026/08/` surfaces **no Robinson/Kirk/bindover PDF**. KUTV (383,970 b), KSL (181,486 b) and Deseret (173,794 b) articles all fetched HTTP 200 and carry **no document link and no document iframe** |
| **R4** | **DocumentCloud project 224251 + full-text search (API open)** | **THE BRIEF IS NOT THERE.** `api.www.documentcloud.org/api/documents/search/` HTTP 200 throughout. **✅ The project is now FULLY enumerated: `count` = 46 and 46 distinct documents listed across three cursor pages (25 + 21 + 0)** — this closes Run 2's "one of the 46 unaccounted for." Every document in the project is dated **2026-03-15/16**; none is the State's brief. Full-text: `251403576` → 40 hits, only four after 2026-06 (the 07-09 supplemental notice; a 06-25 reply; a 663-pp federal item; the **defence** brief) — **no State's brief**. `"Memorandum in Support of Preliminary Hearing Bindover"` → **0**. `"straight-forward a bindover"` → **0**. `title:bindover` → 4, none after June. The account that posted the defence brief (`+user:109543`, 57 docs; `+organization:270`) posted **no State's brief**. ⚠ **Scope: this is a claim about DocumentCloud, not about the world** |
| **R5** | **Utah County Attorney media page** | **HOSTS ANNOUNCEMENTS, NOT FILINGS.** `atty.utahcounty.gov/media/ckpr` HTTP 200, 52,823 bytes; its **complete `href` inventory contains no `.pdf` or `.doc` link of any kind**, and the item pages `/media/ckpr/{123,126,128,131,135}` (HTTP 200) carry none either. Newest item remains the **2026-08-11** notice that argument is set for 09-01 — the same Tier 2 item Run 3 logged. **This route has now failed for this purpose on three consecutive occasions (Runs 1, 3, and here) and should be treated as structurally unable to supply filings** |
| **R6** | **Utah XChange** | **NOT ATTEMPTED.** Paywalled, account creation required — **👤 owner-only** (Q-31/Q-03), unchanged since 2026-07-27 |
| **R7** | **A live browser** | **NOT ATTEMPTED — a scope statement, not a null.** A browser is connected to this environment, but pointing it at the mirror requires an owner-facing confirmation this session cannot present, and any Scribd download is an owner-gated action. ⚠ **Consequence: the Scribd gate now sits behind the SAME dependency as the DocumentCloud web UI (Q-32(b)). That dependency now has two dependents, one of them Q-45 itself** — Run 2 and Run 3 both suggested promoting it to a blocking dependency before 09-01; this attempt is the argument for doing so |

### 2. The blocking failure, in detail — the mirror is real, identified, and unreadable from here

**What was established about the mirror (new to this library):**

| | |
|---|---|
| **Where it is embedded** | The Post Millennial article `https://thepostmillennial.com/utah-county-prosecutors-urge-judge-graf-to-send-tyler-robinson-to-trial-for-murder-of-charlie-kirk` — HTTP 200, **91,085 bytes**, carrying `<iframe class="scribd_iframe_embed" … title="Memorandum in Support of Preliminary Hearing Bindover in Tyler Robinson case">` |
| **Document identity** | **Scribd document ID `1067587104`.** Canonical: `https://www.scribd.com/document/1067587104/Memorandum-in-Support-of-Preliminary-Hearing-Bindover-in-Tyler-Robinson-case`. Embed: `https://www.scribd.com/embeds/1067587104/content?start_page=1&view_mode=scroll&access_key=key-phgNr7tNlwIJ4Dg9z3o1`. Uploader account: `https://www.scribd.com/user/654373344/The-Post-Millennial`. ⚠ **Run 2 recorded that the mirror exists; it did not record its identifier. Recording the ID is the one durable gain of this attempt** |
| **What every fetch returned** | **HTTP 200 with a 3,038-byte page whose `<title>` is "Client Challenge"** — a JavaScript anti-bot interstitial, not the document. Identical result on **seven** endpoints: `/document/<id>/<slug>`, `/doc/<id>`, `ru.scribd.com`, `www.everand.com`, `/document/<id>/download?commit=Download+Now`, `/document_downloads/<id>?extension=pdf`, and `/services/oembed`. `m.scribd.com` failed to connect outright |
| **Bytes obtained** | **None. No file, no hash, nothing banked.** ⚠ **HTTP 200 here means "the gate answered," not "the document was served" — a status code is not a retrieval** |

⚠ **One route did get past the gate, and it is deliberately not being used.** A *summarising* fetch (the same channel class CR-E07 §1 logs as having **fabricated a sentence** that appears nowhere in the article it claimed to be reading) reached the Scribd page and returned its listing metadata — title as above, **28 pages**, uploader *The Post Millennial*, a download button present. **It also returned document text. None of that text is recorded here**, per the standing constraint that a watch entry may not characterise a filing's contents — and it would be unusable even if the constraint allowed it, because a paraphrasing intermediary is not a primary document. **A summary of a filing is what this project already had; the point of Q-45 is to stop relying on one.**

**Provenance: still ZERO of three, and for a reason worth stating precisely.** Run 2 set the standard — locate (a) the electronic file-stamp line, (b) the signature block and date, (c) the certificate of service, **as an act separate from reading the document.** None of the three could be checked, **not because they are absent but because no available channel renders the document's own pages faithfully.** That distinction matters: for the defence brief, the same separate-act discipline produced a real finding (stamp absent, other two present). Here it produces **no finding at all**, which is a different and weaker state. **The Scribd copy therefore remains what Run 2 called it: an upload of unverified provenance, not a filed document.**

### 3. Collateral findings — checkable, and none of them about the State's brief

- **✅ Project 224251 is fully accounted for: 46 of 46.** Run 2 enumerated 45 and expressly declined to claim the 46th. Three cursor pages returned 25 + 21 + 0 against a `count` field of 46. **Run 2's open remainder is closed.**
- **The 2026-08-11 defence brief is now also on DocumentCloud — and it is the file this project already holds, not a second source.** Doc **28551955**, "Defendant Tyler James Robinson's Preliminary Hearing Briefing, 8-11-26", 41 pp., uploaded **2026-08-12T19:27Z** by **Savannah Pointer, Epoch Times** (org 270, verified-journalist flag set). DocumentCloud's metadata field `file_hash` = `a93801eef1bcbe30e0af4f569d91e841b266ce2b`, which is **exactly the SHA-1 of the copy banked from the Fox mirror**. **Same bytes, therefore no independent provenance, no file-stamp gain, and no second attestation.** The hunt for a **court-stamped** copy is unaffected and stays open. *(Recorded here as an access-route fact. No register entry is resolved, and no evidence file is amended by this note.)*
- ⚠ **A HASH TRAP, logged so the next run does not fall into it. The PDF DocumentCloud SERVES is not the file that was uploaded to it.** Downloaded 2026-08-13 from `s3.documentcloud.org/documents/28551955/defendant-tyler-james-robinsons-preliminary-hearing-briefing-8-11-26.pdf`: **383,293 bytes, SHA-256 `5c2c426b79febf1260b1b3458b379c184d609c1a36f18e6cc52bb8369d94e490`, SHA-1 `a408efc77654339c1eff1c13cde96339e5a25c34`** — different length and different hashes from the banked copy (**389,135 bytes**, SHA-256 `c3f394372192a6a3c6b791839a22a9ce4be43aea6f9985b9fc3703633bfde0e4`) **and** from DocumentCloud's own `file_hash`. It is nonetheless the **same document re-rendered by DocumentCloud's pipeline**: 41 pages, and its extracted text is **identical to the banked extraction after whitespace normalisation, 91,729 characters on both sides.** **Rule for future comparisons: never hash a DocumentCloud-served PDF against an original — compare against the API's `file_hash` field, which is the uploaded file's hash.** ⚠ **Scope of the "same file" claim above, stated exactly: it rests on the `file_hash` FIELD matching the banked copy's SHA-1, not on a byte-for-byte download — the download cannot test it, because what is served is a re-render.** What the download independently confirms is narrower and still worth having: the DocumentCloud copy is **the same document, same page count, same text**, so the two claims are consistent rather than circular.

### 4. What would be needed — stated as requirements, not wishes

| | Requirement |
|---|---|
| **👤 A live browser session driven by the owner** | Open `https://www.scribd.com/document/1067587104/…`, let the JavaScript challenge clear, and save the PDF. **This is the shortest path and it is the only one that reaches the located artifact.** ⚠ If Scribd demands an account to download, **stop** — account creation is an owner decision, and the fallback below does not require one |
| **👤 Utah XChange (Q-31/Q-03)** | A paid account would supply a **court-stamped** copy, which is strictly better than any mirror and would also close the stamp question for the defence brief. Cost previously recorded as ~$10 |
| **Retry, cheap and automatable** | **archive.today** (429 today, not a null); a **later DocumentCloud sweep** — the defence brief reached DocumentCloud only on 08-12, so a State filing may yet be uploaded; and **the State's reply due Tue 2026-08-18**, which may be mirrored by the same outlets that mirrored the defence brief |
| **Not acceptable as a substitute** | Reconstructing the brief through a summarising fetch, or recording its contents from reporting. **The library already has the second; Q-45 exists because the second is not enough** |

### 5. Queue out of this attempt

| → | Item |
|---|---|
| **Q-45** | **OPEN. Not obtained. Route located and identified (Scribd doc 1067587104) but gated.** Its contents remain unrecorded by this project, and **CR-E07's F-15 stands unchanged: the State's theory is visible only through its opponent's description** |
| **Q-56** | The execution item for Q-45 — **attempted 2026-08-13 and failed at the retrieval step**, before provenance verification and before any reading. **Not closed** |
| **Q-32(b)** | ⚠ **Now carries a second dependent, and the more important one.** A live browser is no longer only about the DocumentCloud web UI; **Q-45 is behind it too.** Run 2 and Run 3 each suggested promoting it to a blocking dependency before 09-01 — **this attempt is the concrete case for doing so** |
| **Q-31 / Q-03** | Unchanged. **Third consecutive entry whose blind spot is docket access** |
| **NEW** | **Re-check archive.today for a capture of Scribd doc 1067587104** — today's 429 is a rate-limit, not an absence. ⚠ **Retried 2026-08-14: still HTTP 429** (second consecutive rate-limit — the archive.today question remains NOT ESTABLISHED); Wayback CDX prefix again returned **zero rows**, and `archive.org/wayback/available` itself returned 429 this time. No change; the retry stays queued |
| **NEW** | **Re-sweep DocumentCloud after 2026-08-18** for the State's reply and for any late upload of the 07-28 brief. The API route is open and the sweep is cheap |
| **Watch** | **State's reply due Tue 2026-08-18** (18-page limit). **Oral argument Tue 2026-09-01, 10:00.** If the reply is mirrored the way the defence brief was, that mirror is also the best chance of finally seeing the State's own words |

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No evidence file was created. The contents of the State's brief remain unrecorded by this project.** ⚠ **As of 2026-08-13, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.**

---

## Routine-liveness resolution — 2026-08-14 · NOT a run of the spec

> **This section resolves the one question the v1.2 status text said could not be resolved from inside this repository:** *"Whether the routine fired and was never pasted, or is dead, is NOT ESTABLISHED."* **It is now established: the routine fired, all three times, and its reports were never pasted.** Method: direct retrieval of the routine's configuration and run-session logs through the claude.ai remote-trigger API, from a local session with the owner's credentials. **Retrieval date for everything below: 2026-08-14.** Nothing here is reconstructed or inferred from absence — every claim traces to the API's own records.
> ⚠ **No run rows are backfilled.** The v1.2 rule stands: a fabricated row is worse than a missing one. The three firings' full report texts were written to their cloud sessions' ephemeral scratchpads and delivered as file attachments into the routine's claude.ai sessions; **this repository still does not hold them.** What follows is the watch-relevant substance of the condensed API run logs, with each session's ID as its citation.

### 1. The routine, as the API reports it

| | |
|---|---|
| **Routine** | `trig_016faLfbQWCz72M463Dy8HsL` — "DOCKET-WATCH — State v. Robinson, Case 251403576 (report-only)" |
| **State** | **`enabled: true`** · cron `0 13 * * 3,6` UTC (Wed + Sat 09:00 ET) · model `claude-opus-5` |
| **Last fired** | 2026-08-12T13:04:20Z |
| **Next firing** | **2026-08-15T13:00:41Z (Sat 09:00 ET)** |
| **Sources** | **None configured** — each run's environment log records `No sources configured`. The routine does not merely lack *permission* to the repository; **its job config carries no repository at all.** Granting the GitHub App access is necessary but not sufficient: the routine's config must also gain the source before a run can write here |
| **Prompt** | The inlined spec as of 2026-08-01 — ⚠ confirming v1.4's warning that it is **out of sync** with DOCKET-WATCH.md as amended 2026-08-13 |

### 2. The three firings — each ran, reported, delivered, and was never pasted

| Firing | Session | Outcome |
|---|---|---|
| **Wed 2026-08-05** | `cse_015Hy9bdS2JDtiPsi4U2RNpR` (33 turns, ~5 min) | Completed. Report `CR-WATCH-2026-08-05.md` written and **delivered as a file attachment** (uuid `8dfdb3b6-4a9e-4c8a-a0af-cf2b900f3b2d`) **plus a mobile push**. Its own headline: **ESCALATION MET — route trigger**: every direct-retrieval route failed at the session egress proxy (11/11 hosts incl. control), search-index the only channel. Case observations (search-only): no bindover; 09-01 unmoved; no continuance motion surfaced; State's 07-28 brief corroboration broadened, document still unheld |
| **Sat 2026-08-08** | `cse_011tF4hurEd5KesDxvPQkdSk` (28 turns, ~4 min) | Completed, delivered (file uuid `b3715c88-1d06-4a11-b1ca-141932e69a29` + push). **ESCALATION MET — route trigger**, same blackout. Case observations (search-only): all four standing checks negative-unverified; noted the 08-11 defence deadline as the item to re-run before |
| **Wed 2026-08-12** | `cse_01QXdVjFPwhLrbJpnybTJFSp` (29 turns, ~5 min) | Completed, delivered (file uuid `8282eb7f-f646-4bc0-b584-2951fcf9348f` + push). **ESCALATION MET — route trigger**, same blackout. Case observations (search-only): no bindover; 09-01 still reported standing; no continuance motion found; **the 08-11 defence response: "no observation either way"** — recorded there as an open question, later settled by Run 3's banking of the brief |

**None of the three case-observation sets adds anything the library does not already hold at better tier through Run 3 (2026-08-13).** They are recorded here as evidence about the watch, not as findings about the case.

### 3. The route finding — the watch has been running blind since 2026-08-05

Every firing hit the same wall: **the cloud session's egress proxy returned `403 CONNECT tunnel failed — policy denial` for every direct HTTPS fetch**, including a control fetch of `example.com` — which is what identifies the failure as **environmental (the session's egress policy), not site-side**. Blocked in-session: `legacy.utcourts.gov` (which Run 1 retrieved successfully on 07-28 from a local session), `rev.com`, `atty.utahcounty.gov`, `utcourts.gov`, `documentcloud.org`, `static.foxnews.com`, and every news outlet tried. **Web search was the only functioning channel in all three runs.** Each run identified this correctly, declared the *"a route that previously worked has started failing"* escalation, and said so at the top of its report — **the escalation fired three times into a channel nobody was reading.**

**Consequences, stated as such:**
1. **Fired-and-never-pasted is confirmed** — so the paste-back failure is fixed by the 👤 GitHub App grant **plus adding the repository to the routine's config** (§1: it has no source at all).
2. **The grant does not fix the blindness.** Unless the environment's egress policy changes, every future firing — **including tomorrow's, Sat 2026-08-15, and the one covering the Tue 2026-08-18 State's-reply window** — is a search-index tripwire only. **Document acquisition currently works only from a local, by-hand run**, which is how Runs 1–3 and the Q-45 attempt all worked.
3. **The delivery channel was the real gap.** Three mobile pushes and three file attachments landed and were not seen. A report-only routine whose output arrives somewhere nobody looks is the same as a dead one — which is what the staleness trigger added in v1.4 (no log row within 4 days of a firing) now guards against, from the log's own mtime.

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No filing's contents are characterised here.** ⚠ As of 2026-08-14, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.4** | **2026-08-14** | **The "fired or dead" question is RESOLVED — the routine FIRED ALL THREE TIMES (08-05, 08-08, 08-12) and its reports were delivered and never pasted.** Established by direct API retrieval of the routine's run sessions (IDs cited in the new liveness-resolution section); the routine is **enabled**, next firing Sat 2026-08-15 09:00 ET. **No run rows backfilled** — the v1.2 rule stands; the three firings' watch-relevant substance is recorded in the resolution section with each session ID as its citation, and none of it adds anything the library does not already hold at better tier through Run 3. 🚨 **New route finding: every cloud firing since 2026-08-05 ran BLIND** — the session egress proxy 403-blocked all direct HTTPS fetches including a control fetch of `example.com` (environmental, not site-side); web search was the only working channel, and **each run correctly declared the route-failure escalation into a delivery channel nobody was reading** (three mobile pushes, three file attachments, zero pastes). **Consequences recorded:** the 👤 GitHub App grant fixes paste-back only if **the repository is also added to the routine's config, which currently carries NO source at all** (`No sources configured` in every run's environment log); the grant does **not** fix the blindness, so the Sat 08-15 and Tue 08-18 windows have no document-capable scheduled cover — local by-hand runs remain the only acquisition-capable pass. Run-index rows for the three firings annotated in place; status text superseded to v1.4 with v1.3 retained. No register entry assigned or moved; no case-posture statement altered; no filing contents characterised. |
| **1.3** | **2026-08-13** | **A Q-45 ACQUISITION ATTEMPT WAS RUN AND FAILED — logged as a section, not as a run row, because it is not an execution of the DOCKET-WATCH spec.** 🚨 **The State's 2026-07-28 opening brief was NOT obtained. Nothing was banked, no SHA-256 exists because no bytes were retrieved, its contents remain unrecorded, and no CR-E08 evidence file was written** — writing one about a document this project cannot read would be the error the library exists to prevent. **Six routes are logged with their exact results, per the rule that failed retrievals are access-path caveats rather than things to drop silently.** ⚠ **The blocking failure: the Scribd mirror is real and was positively identified — document ID `1067587104`, embedded in The Post Millennial's article, uploader account `The Post Millennial`; Run 2 recorded that the mirror existed but never recorded its identifier, so the ID is this attempt's one durable gain.** Every one of **seven** Scribd endpoints (canonical, `/doc/`, `ru.`, everand, two download paths, oEmbed) returned **HTTP 200 with an identical 3,038-byte "Client Challenge" JavaScript interstitial** — ⚠ **a status code is not a retrieval.** **Q-45's "now actionable" (Run 2 §8) is QUALIFIED IN PLACE, not struck as wrong: "actionable" meant *located*, not *retrievable*.** ⚠ **A summarising fetch did get past the gate and returned page metadata (28 pp., uploader, download button) AND document text; the text is deliberately not recorded** — it arrived through the same channel class CR-E07 §1 logs as having fabricated a sentence, and **a paraphrasing intermediary is not a primary document; the library already had summaries, which is why Q-45 exists.** **Provenance therefore remains ZERO of three — not because the file-stamp, signature block and certificate of service are absent, but because nothing renders the document faithfully; the separate-act discipline that produced a real finding on the defence brief produces NO finding here, a weaker state that is stated rather than glossed.** **Scoped nulls: no Wayback capture of the Scribd document exists (CDX prefix enumeration, zero rows) while archive.today is NOT ESTABLISHED (HTTP 429, a rate-limit, not an absence); no outlet-mirrored PDF exists — the Fox 07-28 article re-fetched at 476,625 bytes still carries zero PDF/Scribd/DocumentCloud links 16 days after Run 1 found the same, and Wayback CDX over `static.foxnews.com/…/uploads/2026/07/` and `/08/` surfaces no Robinson PDF, while KUTV, KSL and Deseret carry no document links or iframes; the Utah County Attorney media page has no `.pdf` href anywhere and is now recorded as structurally unable to supply filings after failing this purpose three times; XChange (👤, Q-31) and a live browser (👤, Q-32(b)) were not attempted and are stated as scope, not as nulls.** ⚠ **Consequence: the Scribd gate now sits behind the SAME dependency as the DocumentCloud web UI, so Q-32(b) has a second and more important dependent — Q-45 itself.** **Collateral, all checkable: (1) project 224251 is now FULLY enumerated, 46 of 46 across three cursor pages (25 + 21 + 0), closing Run 2's unaccounted 46th; (2) the defence brief reached DocumentCloud on 2026-08-12 (doc 28551955, Epoch Times / Savannah Pointer) but DocumentCloud's `file_hash` for it equals the SHA-1 of the copy this project already banked — the SAME FILE, so no independent provenance and no progress on a court-stamped copy; (3) ⚠ a HASH TRAP is logged — the PDF DocumentCloud SERVES (383,293 bytes, SHA-256 `5c2c426b…`) is a re-render and matches neither the banked original (389,135 bytes, SHA-256 `c3f39437…`) nor DocumentCloud's own `file_hash`, though its extracted text is identical to the banked extraction at 91,729 characters; future comparisons must use the API's `file_hash` field, never the served file.** **Requirements to close Q-45 are stated as requirements: an owner-driven browser session, or XChange for a stamped copy — with the instruction to STOP if Scribd demands an account.** **Cheap retries queued: archive.today, a post-08-18 DocumentCloud sweep, and the State's reply due Tue 2026-08-18, whose outlet mirror may be the next real chance at the State's own words. CR-E07's F-15 stands unchanged — the State's theory is still visible only through its opponent's description. No register entry was assigned, resolved or moved; no case-posture statement was altered; Robinson has not been bound over.** |
| **1.2** | **2026-08-13** | **Run 3 logged — a CATCH-UP RUN, and the run's headline finding is about the watch, not the case.** 🚨 **The watch went dark for 12 days:** three scheduled firings (Wed 08-05, Sat 08-08, Wed 08-12) produced no rows, and **the 2026-08-11 defence deadline — which Run 1 itself named as "the next checkpoint" and the likeliest vehicle for a continuance motion against a named on-the-record risk — passed inside that gap, unchecked.** The gap was found **from outside this repository** during an unrelated session reconstruction, by this file's 12-day-old mtime; the watch did not catch itself. ⚠ **No rows were backfilled** for the three missed firings — a fabricated row is worse than a missing one — and **whether the routine fired-and-was-never-pasted or is dead is expressly NOT ESTABLISHED**, since a report-only routine refused the private repo cannot be distinguished from a dead one from inside it. **On the case: the defence brief is FILED AND BANKED** — *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* Case No. 251403576, Hon. Tony F. Graf, Jr., **signed and served Tue 2026-08-11** (day-of-week verified by direct reading, not extraction, per Run 2's logged hazard), 41 PDF pp. / 35 printed, SHA-256 recorded, `.txt` extraction alongside. **This is the first primary filing the project holds as a document rather than through reporting.** ⚠ **Provenance is two-of-three: signature block and certificate of service present, NO clerk file-stamp line visible** — better than the State's unverified Scribd mirror, still short of a stamped filing, and **not silently promoted.** ⚠ **35 is both the printed length and the court's page limit here; the coincidence is recorded and explicitly not read as a finding.** **The 09-01 argument STANDS**, upgraded from reporting to a **Tier 2 named-official** item dated 2026-08-11 (Utah County Attorney media page, a route whose latest Robinson item was 2026-06-26 at Run 1). **No continuance motion found — with scope stated**: open routes only, no docket consulted, and a motion filed in the last 48 hours would likely not yet be reported, so this is not evidence of absence. **The brief's contents are deliberately unrecorded** per the spec, and **a second restraint is logged**: the extraction incidentally surfaced material on the sexuality and gender identity of the defendant and of a private individual, none of which is recorded, that determination belonging to a reasoned evidence-file pass under the two-layer discipline rather than to a watch row. **No escalation trigger met — and the run flags that the trigger list contains no trigger for "the watch itself has stopped," which is precisely why 12 days passed unnoticed.** Queued: 👤 confirm the routine is alive before Sat 08-15, 👤 grant the GitHub App access, add a watch-failure escalation trigger, locate a stamped copy. **No register entry assigned or moved; no case-posture statement altered.** |
| **1.1** | **2026-08-01** | **Run 2 logged.** **No escalation trigger met** — no bindover, 09-01 standing, nothing sealed or unsealed, and the only route change is a route **re-opening**. ⚠ **A public mirror of the State's opening brief now exists and is retrievable** — a 28-page "Memorandum in Support of Preliminary Hearing Bindover" on Scribd — **closing Run 1's "no public mirror found" null and giving Q-45 an acquisition route.** The document was **not banked and its contents are not recorded**; provenance verification is named as a separate act from reading it. ⚠ **28 pp. is the actual length; 35 was the court's page LIMIT — the two were being conflated, though DOCKET-WATCH already stated it correctly, so no library file required correction.** The **2026-07-28 filing date is now multi-sourced** across six outlets where Run 1 had one; **source independence for the filing event is upgraded, the document remains unheld, and it stays T1 via T3.** ⚠ **The DocumentCloud API is no longer bot-gated: project 224251 was positively enumerated for the first time (46 documents; 45 listed, one unaccounted for and not claimed otherwise), while the web UI remains JS-gated — so Q-32 should be SPLIT, not closed.** A **new unheld artifact** was located: a 4-page "Supplemental Notice Concerning Access to Evidence Presented in Open Court," **filed 2026-07-09, during hearing week** — adjacency to the Exhibit 12.1 question resting on **title only**. Second source obtained for **Q-47**. ⚠ **Two hazards recurred and are logged: machine extraction gave wrong dates on four counts (three extractions called 2026-07-29 a Tuesday; it is a Wednesday), and searches for the bullet-fragment ruling repeatedly surface the 2026-06-26 contempt ruling instead — which also puts TWO dates in play for Q-46.** **A three-day blind spot at the run's leading edge is stated.** Outlets' characterisations and direct quotations of the brief were surfaced repeatedly by the search layer and **deliberately not recorded**, per the spec. **No register entry assigned or moved; no case-posture statement altered.** |
| 1.0 | 2026-07-28 | File created; **Run 1 logged.** The first execution of the DOCKET-WATCH spec, which until now had no runner attached. **The State's opening probable-cause brief is reported filed on 2026-07-28** — T1 via T3, one independent source, no primary document obtained, and the date confirmed by day-of-week check against D-51 rather than by machine extraction (two automated passes returned wrong dates and are logged as a caveat). **The brief's contents are deliberately not recorded**, per DOCKET-WATCH's prohibition and because Q-04's decisive artifact is the document itself. **The 09-01 argument stands**; no continuance motion found, with the Nester conflict still open and the 08-11 defence reply named as the next checkpoint. **A previously unknown proceeding was located** — a contempt hearing c. 2026-06-22, absent from the library's five-day transcript inventory. **The `legacy.utcourts.gov` press-notice route was retrieved for the first time** and holds nothing after 2026-07-06; **abc4.com is newly bot-blocked**. Three items queued (**Q-45, Q-46, Q-47**). No escalation trigger met; no case-posture statement altered; no register entry assigned or moved. |
