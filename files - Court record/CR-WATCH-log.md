# CR-WATCH-log — Docket Watch Run Log

**Purpose:** one row per run of the [DOCKET-WATCH.md](../DOCKET-WATCH.md) spec. **A run that finds nothing still writes a row** — a watch with gaps in its log is indistinguishable from a watch that was not running.
**Case:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr.
**Standing constraint:** a run may acquire and bank freely and may update DOCKET-WATCH's own calendar table with an observed status. **It may never change a case-posture statement in a topic file, resolve a register entry, characterise a filing's contents beyond its title and date, or infer an outcome from a filing's existence.** D-51 is why.
**Status:** **v1.2 — Run 3 logged 2026-08-13, a CATCH-UP RUN AFTER A 12-DAY GAP.** 🚨 **THE WATCH WENT DARK BETWEEN 2026-08-01 AND 2026-08-13.** The durable cloud routine (`trig_016faLfbQWCz72M463Dy8HsL`, Wednesdays and Saturdays 09:00 ET, first firing 2026-08-05) had **three scheduled firings — Wed 08-05, Sat 08-08, Wed 08-12 — and none produced a row here.** It is **REPORT-ONLY**: the cloud environment was refused access to the private repository, so **its output must be pasted into this file by hand**, and no hand-paste occurred. **Whether the routine fired and was never pasted, or is dead, is NOT ESTABLISHED from inside this repository — 👤 check `/schedule`.** Runs 1, 2 and 3 were all executed by hand. **Next scheduled firing: Sat 2026-08-15. Next hard case date: Tue 2026-08-18 (State's reply). Oral argument: Tue 2026-09-01.**

---

## Run index

| # | Date | Trigger | Headline | Escalated? |
|---|---|---|---|---|
| **1** | **2026-07-28** | first run; State's opening brief due this date | **State's opening probable-cause brief reported FILED 2026-07-28** (T1 via T3, single independent source). 09-01 argument still stands. **A previously unknown Rev transcript located: a contempt hearing, c. 2026-06-22.** | No — no escalation trigger met |
| **2** | **2026-08-01** | scheduled follow-up; the durable routine created this date | **A PUBLIC MIRROR OF THE STATE'S BRIEF EXISTS AND IS RETRIEVABLE** — 28 pp., Scribd, closing Run 1's "no public mirror" null and giving **Q-45** a route. The 07-28 filing date is now **multi-sourced** (Run 1 had one). **The DocumentCloud API is no longer bot-gated** and project 224251 was enumerated for the first time (46 documents). ⚠ **28 pp. is the LENGTH; 35 was the page LIMIT.** | No — no escalation trigger met |
| — | *2026-08-05* | scheduled firing | 🚨 **NO ROW — the watch did not run, or ran and was never pasted.** Not established which | *n/a* |
| — | *2026-08-08* | scheduled firing | 🚨 **NO ROW** — as above | *n/a* |
| — | *2026-08-12* | scheduled firing | 🚨 **NO ROW** — as above. ⚠ **The 2026-08-11 defence deadline, named by Run 1 as "the next checkpoint," passed inside this gap and unchecked** | *n/a* |
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
| **Q-45** | **Now actionable** — bank the Scribd mirror, then verify provenance as a separate act before reading |
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
| **Q-45** | Unchanged — the **State's** 07-28 brief remains unbanked and its Scribd mirror unverified |
| **NEW** | **Locate a court-stamped copy** of the 08-11 brief to close the missing file-stamp element |
| **Q-31 / Q-03** | Unchanged — no current docket. ⚠ **This run is the second consecutive one whose blind spot is docket access**; consider promoting it to a blocking dependency before 09-01, as Run 2 already suggested for Q-32 |

**No register entry was assigned or moved. No case-posture statement in any topic file was altered.** ⚠ **As of 2026-08-13, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.**

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.2** | **2026-08-13** | **Run 3 logged — a CATCH-UP RUN, and the run's headline finding is about the watch, not the case.** 🚨 **The watch went dark for 12 days:** three scheduled firings (Wed 08-05, Sat 08-08, Wed 08-12) produced no rows, and **the 2026-08-11 defence deadline — which Run 1 itself named as "the next checkpoint" and the likeliest vehicle for a continuance motion against a named on-the-record risk — passed inside that gap, unchecked.** The gap was found **from outside this repository** during an unrelated session reconstruction, by this file's 12-day-old mtime; the watch did not catch itself. ⚠ **No rows were backfilled** for the three missed firings — a fabricated row is worse than a missing one — and **whether the routine fired-and-was-never-pasted or is dead is expressly NOT ESTABLISHED**, since a report-only routine refused the private repo cannot be distinguished from a dead one from inside it. **On the case: the defence brief is FILED AND BANKED** — *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* Case No. 251403576, Hon. Tony F. Graf, Jr., **signed and served Tue 2026-08-11** (day-of-week verified by direct reading, not extraction, per Run 2's logged hazard), 41 PDF pp. / 35 printed, SHA-256 recorded, `.txt` extraction alongside. **This is the first primary filing the project holds as a document rather than through reporting.** ⚠ **Provenance is two-of-three: signature block and certificate of service present, NO clerk file-stamp line visible** — better than the State's unverified Scribd mirror, still short of a stamped filing, and **not silently promoted.** ⚠ **35 is both the printed length and the court's page limit here; the coincidence is recorded and explicitly not read as a finding.** **The 09-01 argument STANDS**, upgraded from reporting to a **Tier 2 named-official** item dated 2026-08-11 (Utah County Attorney media page, a route whose latest Robinson item was 2026-06-26 at Run 1). **No continuance motion found — with scope stated**: open routes only, no docket consulted, and a motion filed in the last 48 hours would likely not yet be reported, so this is not evidence of absence. **The brief's contents are deliberately unrecorded** per the spec, and **a second restraint is logged**: the extraction incidentally surfaced material on the sexuality and gender identity of the defendant and of a private individual, none of which is recorded, that determination belonging to a reasoned evidence-file pass under the two-layer discipline rather than to a watch row. **No escalation trigger met — and the run flags that the trigger list contains no trigger for "the watch itself has stopped," which is precisely why 12 days passed unnoticed.** Queued: 👤 confirm the routine is alive before Sat 08-15, 👤 grant the GitHub App access, add a watch-failure escalation trigger, locate a stamped copy. **No register entry assigned or moved; no case-posture statement altered.** |
| **1.1** | **2026-08-01** | **Run 2 logged.** **No escalation trigger met** — no bindover, 09-01 standing, nothing sealed or unsealed, and the only route change is a route **re-opening**. ⚠ **A public mirror of the State's opening brief now exists and is retrievable** — a 28-page "Memorandum in Support of Preliminary Hearing Bindover" on Scribd — **closing Run 1's "no public mirror found" null and giving Q-45 an acquisition route.** The document was **not banked and its contents are not recorded**; provenance verification is named as a separate act from reading it. ⚠ **28 pp. is the actual length; 35 was the court's page LIMIT — the two were being conflated, though DOCKET-WATCH already stated it correctly, so no library file required correction.** The **2026-07-28 filing date is now multi-sourced** across six outlets where Run 1 had one; **source independence for the filing event is upgraded, the document remains unheld, and it stays T1 via T3.** ⚠ **The DocumentCloud API is no longer bot-gated: project 224251 was positively enumerated for the first time (46 documents; 45 listed, one unaccounted for and not claimed otherwise), while the web UI remains JS-gated — so Q-32 should be SPLIT, not closed.** A **new unheld artifact** was located: a 4-page "Supplemental Notice Concerning Access to Evidence Presented in Open Court," **filed 2026-07-09, during hearing week** — adjacency to the Exhibit 12.1 question resting on **title only**. Second source obtained for **Q-47**. ⚠ **Two hazards recurred and are logged: machine extraction gave wrong dates on four counts (three extractions called 2026-07-29 a Tuesday; it is a Wednesday), and searches for the bullet-fragment ruling repeatedly surface the 2026-06-26 contempt ruling instead — which also puts TWO dates in play for Q-46.** **A three-day blind spot at the run's leading edge is stated.** Outlets' characterisations and direct quotations of the brief were surfaced repeatedly by the search layer and **deliberately not recorded**, per the spec. **No register entry assigned or moved; no case-posture statement altered.** |
| 1.0 | 2026-07-28 | File created; **Run 1 logged.** The first execution of the DOCKET-WATCH spec, which until now had no runner attached. **The State's opening probable-cause brief is reported filed on 2026-07-28** — T1 via T3, one independent source, no primary document obtained, and the date confirmed by day-of-week check against D-51 rather than by machine extraction (two automated passes returned wrong dates and are logged as a caveat). **The brief's contents are deliberately not recorded**, per DOCKET-WATCH's prohibition and because Q-04's decisive artifact is the document itself. **The 09-01 argument stands**; no continuance motion found, with the Nester conflict still open and the 08-11 defence reply named as the next checkpoint. **A previously unknown proceeding was located** — a contempt hearing c. 2026-06-22, absent from the library's five-day transcript inventory. **The `legacy.utcourts.gov` press-notice route was retrieved for the first time** and holds nothing after 2026-07-06; **abc4.com is newly bot-blocked**. Three items queued (**Q-45, Q-46, Q-47**). No escalation trigger met; no case-posture statement altered; no register entry assigned or moved. |
