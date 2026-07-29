# CR-WATCH-log — Docket Watch Run Log

**Purpose:** one row per run of the [DOCKET-WATCH.md](../DOCKET-WATCH.md) spec. **A run that finds nothing still writes a row** — a watch with gaps in its log is indistinguishable from a watch that was not running.
**Case:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr.
**Standing constraint:** a run may acquire and bank freely and may update DOCKET-WATCH's own calendar table with an observed status. **It may never change a case-posture statement in a topic file, resolve a register entry, characterise a filing's contents beyond its title and date, or infer an outcome from a filing's existence.** D-51 is why.
**Status:** v1.0

---

## Run index

| # | Date | Trigger | Headline | Escalated? |
|---|---|---|---|---|
| **1** | **2026-07-28** | first run; State's opening brief due this date | **State's opening probable-cause brief reported FILED 2026-07-28** (T1 via T3, single independent source). 09-01 argument still stands. **A previously unknown Rev transcript located: a contempt hearing, c. 2026-06-22.** | No — no escalation trigger met |

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

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-28 | File created; **Run 1 logged.** The first execution of the DOCKET-WATCH spec, which until now had no runner attached. **The State's opening probable-cause brief is reported filed on 2026-07-28** — T1 via T3, one independent source, no primary document obtained, and the date confirmed by day-of-week check against D-51 rather than by machine extraction (two automated passes returned wrong dates and are logged as a caveat). **The brief's contents are deliberately not recorded**, per DOCKET-WATCH's prohibition and because Q-04's decisive artifact is the document itself. **The 09-01 argument stands**; no continuance motion found, with the Nester conflict still open and the 08-11 defence reply named as the next checkpoint. **A previously unknown proceeding was located** — a contempt hearing c. 2026-06-22, absent from the library's five-day transcript inventory. **The `legacy.utcourts.gov` press-notice route was retrieved for the first time** and holds nothing after 2026-07-06; **abc4.com is newly bot-blocked**. Three items queued (**Q-45, Q-46, Q-47**). No escalation trigger met; no case-posture statement altered; no register entry assigned or moved. |
