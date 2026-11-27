# CR-ACQ-2026-11-26 — Acquisition: the Rev transcript of the 2026-11-09 trial-setting hearing (Q-200)

**File ID:** CR-ACQ-2026-11-26 · **Scope:** acquisition and facial (recording-layer) reading of one Rev transcript, the court's oral reading of its trial-setting and case-management order on 2026-11-09, checked against the calendar rows the docket watch had written from search results (Runs 26–30) · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo · **Prepared:** 2026-11-26 · **Status:** v1.1 `[PROVISIONAL]`. Iteration 1 of 3. Every check below is the finder's own, and **the author may not clear the flag** (`VERIFICATION-PROTOCOL` §3.4).

**Sourcing framework (project standard):** Tier 1 is sworn testimony and primary court filings or documents. Tier 2 is named official statements. Tier 3 is named journalistic reporting. Tier 4 is anonymous or low-verification material. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries its transcript timestamp; the retrieval date is 2026-11-26.

**§1 Access-path caveats, first:**
- **This is a Rev machine-generated transcript.** It carries the same dependency as the five hearing-day transcripts and the contempt-hearing transcript (`CR-ACQ-2026-08-14`). Speaker attribution is Rev's: the bench appears as both "The Court" and "Judge", six voices are unattributed ("Speaker 1–6"), and counsel's names are spelled by ear ("Ms. Nestor" for Nester). Garbles are present; one sits inside a sentence this file uses (`01:08:36`, *"proposed microscopy, I can't speak, testing"*).
- **It renders the court READING A WRITTEN ORDER, not the order itself.** At `29:07` the court says it will read from "the order which will be uploaded later today" and names it a trial-setting and case-management order with an **Addendum A** (the schedule) and an **Addendum B** (counsel's conflicts). **The written order and both addenda are NOT held.** Every date below is a date as spoken and as Rev rendered it. Where the order is acquired it governs, and this file must be re-checked against it (P8).
- **One internal inconsistency is recorded and not resolved.** At `01:22:23`–`01:23:40` the rendering says both *"October 21st, 2028 is the last reserved day"* and *"November 21st, 2028 is 105th reserve court day"*. **2028-10-21 is a Saturday**, which points to a rendering garble or a different count, but this file does not decide which.
- **Acquisition route:** a direct HTTPS fetch from this machine. The docket-watch routine had seen the page only in a search index, at Run 26 (2026-11-11), because its egress has been blocked since 2026-08-05.

---

## 1. Outcome, stated first

**The library now holds a Tier 1 rendering (machine transcript, with the caveats above) of the hearing every trial-phase row in `DOCKET-WATCH.md` depends on.** Most of what Runs 26–30 reported from the index is **supported**. **Two calendar statements are contradicted by the rendering:** the jury-selection start time, and the breakdown of the 105 reserved days. **One is not found in it:** a 2027-01-14 appearance. Details and labels are in §4.

## 2. What was acquired

| | |
|---|---|
| **Page** | "Tyler Robinson Trial Date \| Rev", slug `tyler-robinson-trial-date` |
| **URLs** | `https://www.rev.com/transcripts/tyler-robinson-trial-date` and `https://webflow.rev.com/transcripts/tyler-robinson-trial-date`. Both were retrieved **2026-11-26** with HTTP 200 and **returned byte-identical bodies** |
| **Page date** | `datePublished` **2026-11-10**, `dateModified` 2026-11-10T15:08:31.957Z (page metadata). That is one business day after the hearing, consistent with the lag the library has observed before (D-51 discipline) |
| **Banked (raw)** | `CR-ACQ-2026-07-27_court-record-artifacts/2026-11-10-pub_rev-trial-setting-hearing-2026-11-09_raw.html`, 259,550 b, SHA-256 `ce8435f73f9e4f45fb0fd038df6f8ecb64d3de53a2a837a33ec235056d5a9dcc` |
| **Banked (extraction)** | `…/2026-11-10-pub_rev-trial-setting-hearing-2026-11-09.txt`, 63,624 b, SHA-256 `781faa78e6a0449941eb6e242f7e40cab8cedd3a040fd3587ae4ca5e42e8a216`. It holds **137 speaker-paired entries** from `19:18` (the case is called) to `01:37:06` ("All rise") |
| **Extraction method** | Rev splits each stamp across three elements (`Name (` · `MM:SS` · `):`), so the extraction re-joins them and pairs each stamp with the body text that follows it. A stamp with no name, which is Rev's continuation mark, is written `[same speaker]`. The page's trailing boilerplate (topics, subscription text, other transcripts) is cut after the closing "All rise." |

## 3. What the transcript facially shows (recording layer only)

**Appearances** (`19:18`–`19:56`, Rev attribution): for the defence, Kathy Nester, Michael Burt, Staci Visser and Richard Novak, with Mr. Robinson present at counsel table. Chad Grunander speaks for the State. A person named "Mr. Neiman" attends online; the rendering does not establish his role, and this file assigns none.

**The court's framing** (`29:07`–`30:19`): the court says it is ruling on the defence's scheduling memorandum and discovery reports, the State's memorandum and proposed scheduling order, and **Mrs. Kirk's motion for speedy disposition**. After weighing them, it **"selects a different date"** from all three proposals.

**The proposals as the court recites them** (`31:27`–`46:48`):
- **Mrs. Kirk, through counsel:** trial by **2027-10-04**.
- **The State:** ⚠ **the rendering contradicts itself on the State's proposed date.** At `32:54` it reads *"The State proposes July 31st, 2028"*. But at `41:48`–`42:53` the court turns to *"the January 2028 proposal"*: January 31st, 2028, which it ties to the State's need for a firm date and to Mr. Grunander's preference for late January. KSL (art. 51644704, retrieved 2026-11-26) quotes the State's memorandum as proposing **January 31, 2028**. **This file adopts neither date.** The likeliest reading is a Rev garble of "January" at `32:54`, but that is `[inference]`, and the State's memorandum is not held. The State's written estimate is **85 court days, including 20 for jury selection**, described at argument as a 17-week trial.
- **The defence:** a trial period of **July–September 2029**. Mr. Novak called that a tentative target at argument. The defence estimates six to seven months of trial.
- **Discovery figures recited from the defence's written report:** 49 productions, 30,983 files and about 3.3 TB of data.

The court considers October 2027 and January 2028 and rejects both on this record.

**The settings as read** (each a date as rendered; weekday arithmetic checked under P8 and consistent unless marked):

| Date | Setting as read | Timestamp |
|---|---|---|
| **2026-12-14** (Mon) | Initial conflict and progress report, **each side**. Either may file earlier. This date is fixed regardless of the trial date | `48:19`, `01:04:39` |
| from **January 2027** | Pretrial status conferences on the **last Friday of each month** (so the first falls **2027-01-29**). Because of holidays the March and December 2027 conferences move to **2027-03-25** and **2027-12-30** | `01:17:08` |
| **2027-11-10** (Wed) | Venue-motion date in Addendum A. The court states that this date does not extend the Rule 29(c)(3) 14-day rule | `01:12:44` |
| **2027-12-22** (Wed) | **Venue argument (target)** | `53:29` |
| **2027-12-23** (Thu) | Defence mitigation-investigation status report. T−180 is Fri 2027-12-24, an observed holiday, so the report moves back one day | `01:04:39`, `01:11:33` |
| **2027-12-29** · **2028-01-06** | Questionnaire argument (target) · initial decisions (target) | `53:29` |
| **2028-03-24** · **2028-03-31** | Joint report on obstacles to mailing · status conference (the clerk reports on mailing readiness) | `50:00` |
| **2028-04-11** (Tue) | **Readiness hearing**. The court decides whether counsel can complete essential work before jury selection | `31:27`, `50:00` |
| **2028-04-12** · **2028-05-03** | Questionnaires mailed · returns due (21 days, checked) | `53:29` |
| **2028-05-19** (Fri) | **Final (joint) report**, for the **2028-05-26** conference | `56:53`, `01:17:08` |
| **2028-05-30** · **2028-06-13** | Proposed instructions and final exhibits · objections | `01:15:48` |
| **2028-06-07** (Wed) | Media-coverage requests due (14 days before jury selection) | `01:15:00` |
| **2028-06-15** · **2028-06-16** | Final pretrial conference · target date for the media ruling | `01:15:48` |
| 🚨 **2028-06-21** (Wed) | **Jury selection begins at 9:30 a.m.**, courtroom 4B, Fourth District Courthouse, Provo, **"subject to further order"** | `30:19`, `46:48` |
| **105 court days** | **The court's reservation:** 105 full days, of which **5 are for legal argument and 100 are jury days**, running 2028-06-21 to **2028-11-21** (154 calendar days, checked) | `01:21:13`, `01:23:40` |

**Questionnaires** (`53:29`–`56:53`): the State proposed 3,000 and the defence accepted that figure for planning; **the court sets a planning pool of 3,600.**

**Mrs. Kirk's participation** (`31:27`, `46:48`, `51:08`): the court states that she must have an opportunity to be heard before the trial date is changed or a continuance is ruled on (the order's "part five"). **This file records what the court said; it characterises no party's position.**

## 4. Against the calendar: what the index-grade rows said, checked against this rendering

Labels are per `VERIFICATION-PROTOCOL`, and each is the finder's own check: **`[PROVISIONAL]`**.

| # | Calendar statement (DOCKET-WATCH, Runs 26–30) | Rendering | Label |
|---|---|---|---|
| **C-1** | 2028-06-21 row: *"jury selection is reported to begin at **9:00 a.m.**"* (Run 29, from ABC4) | **9:30**, read twice (`30:19`, `46:48`) | **CONTRADICTED** at rendering grade. Correct the row when the order is held, or carry both with this pointer |
| **C-2** | 2028-06-21 row: *"the 105 days break down as **20 for jury selection + 85 for trial**"* (Run 29) | 85 days *including* 20 for jury selection is **the State's estimate** (`32:54`). The court **reserved 105**, as 100 jury days plus 5 for legal argument (`01:21:13`). **The row merges the State's estimate into the court's reservation** | **CONTRADICTED** |
| **C-3** | 2027-01-14 (Thu), 9:00 a.m.: *"next court appearance, oral argument on motions"* (Run 27) | **No "January 14" anywhere in the rendering.** It sets monthly conferences on the last Friday from January 2027, which puts the first on 2027-01-29, and it records the **State's request** for a one-day January 2027 hearing on pending discovery (`01:08:36`) | **UNVERIFIED** in this artifact: a check ran and found nothing. **Not contradicted**, because the date may come from a later notice or minute entry. Do not drop the row on this alone |
| **C-4** | "December 2027 venue-argument hearing" (Run 27) | Targeted for **2027-12-22** (`53:29`) | **SUPPORTED**, and sharpened to a day |
| **C-5** | 2026-12-14 report; 2028-04-11 readiness; 2028-05-19 final report; monthly conferences from January 2027 (Runs 26–27) | All four read on the record as stated | **SUPPORTED** |
| **C-6** | Bullet-fragment motion described as seeking to **bar** VCM and metallurgy testing (Run 28) versus to **pause** it or allow a defence expert to **observe** (Run 30) | Among the defence's anticipated motions the court lists *"safeguards for destructive ballistics testing, including observation or video recording"* (`01:08:36`) | Consistent with Run 30's reading. **Not resolved**: the motion itself is not held, and a list of anticipated subjects is not the motion |

**Independent Tier 2 support for the trial date.** The Utah County Attorney's *Charlie Kirk Case Updates* page (`https://atty.utahcounty.gov/media/ckpr`, fetched directly 2026-11-26, HTTP 200) carries an entry dated **2026-11-13, 12:53 PM MT**, headlined *"Jury Trial in Tyler Robinson Case to Begin June 21, 2028"*, which states that the court scheduled the jury trial at the 2026-11-09 hearing. This is a named official statement by a party, so it is Tier 2 and **its orientation is the prosecution's**. Banked as `CR-ACQ-2026-07-27_court-record-artifacts/2026-11-26_utah-county-attorney-case-updates-page_raw.html` (51,938 b, SHA-256 `5daa8bbd53913d13622473416a2399d876023cbaece411ed7ae5107cd324e5ac`). **The page links no documents in its served HTML.** The routine's index view had suggested document links; this capture does not show any.

**The written order: a scoped null, 2026-11-26.** The court said the order would be **"uploaded later today"** (`29:07`). Two extended web searches (the order's title; utcourts.gov and the case number) and the county attorney's page returned **no copy**. **Not searched:** XChange, which is paid (Q-31), and the courts' own news feed for November. **Absence here is not evidence that the order was not uploaded.**

## 5. Hazards and residue

- **The posture line has not been touched.** Whether "trial set: jury selection 2028-06-21" enters `DOCKET-WATCH.md`'s case-posture line is **Q-201, the owner's call** (`LOOP.md` §3). This file is the Tier 1 rendering Q-201 recommended waiting for. **The written order is still the better basis.**
- **C-1 and C-2 change calendar text that a published page carries, if `DOCKET-WATCH.md` is published.** The rows are pointed here, not rewritten, until the order is held or the owner rules.
- **Not done:** no check of any authority the court cited; no reading of the 2026-10-23 hearing (a separate Rev page may exist); no attempt on the order's upload route.
- **No register entry is assigned, resolved or moved** (D-76 assigned, D-77 next free). Presumption of innocence applies in full.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-11-26 | Same day, before push: the State's proposed date is recorded as **internally inconsistent in the rendering** (July 31 at `32:54` vs the January 31, 2028 proposal discussed at `41:48`), with neither adopted; the 3,600 questionnaire pool added; the county attorney's 2026-11-13 entry banked as Tier 2 support for the trial date; the written order recorded as a scoped null. |
| 1.0 | 2026-11-26 | File created (Q-200, first target). Rev page fetched from two hosts with byte-identical results; raw page and extraction banked with SHA-256s. Settings read off the rendering and weekday-checked. Six calendar statements checked: two **CONTRADICTED** (the 9:00 start time; the "20 + 85" breakdown of 105 days), one **UNVERIFIED** (2027-01-14), two **SUPPORTED**, one consistent but unresolved. `[PROVISIONAL]`, iteration 1 of 3. |
