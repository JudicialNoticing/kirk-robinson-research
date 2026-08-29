# CR-WATCH-log — Docket Watch Run Log

**Purpose:** one row per run of the [DOCKET-WATCH.md](../DOCKET-WATCH.md) spec. **A run that finds nothing still writes a row** — a watch with gaps in its log is indistinguishable from a watch that was not running.
**Case:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr.
**Standing constraint:** a run may acquire and bank freely and may update DOCKET-WATCH's own calendar table with an observed status. **It may never change a case-posture statement in a topic file, resolve a register entry, characterise a filing's contents beyond its title and date, or infer an outcome from a filing's existence.** D-51 is why.
**Status:** **v1.9 — A NEW DEFENCE FILING IS ON THE RECORD, AND THE PASTE-BACK GAP WAS CLOSED IN HOURS FOR THE FIRST TIME.** The Wed 2026-08-26 firing reported a **defence opposition to the electronic media coverage orders for the 09-01 hearing, filed 2026-08-22**, with an EMC-applicability ruling **pending** — `T1 via T3`, document not held. ⚠ **Not a motion to continue; 09-01 unmoved.** Transcribed **the same day**, ~3 hours after firing, during a session close — the previous four reports went unread for days. 🚨 **Root cause still unfixed: `No sources configured`, five reports deep.** ⚠ **Egress blocked for the 21st straight cloud run, WebFetch included.** 🚨 **Q-45 is 29 days open.** **Next firing Sat 08-29 09:00 EDT — the last before the 09-01 hearing.**
**Prior status text (v1.8), retained:** **v1.8 — THE 2026-08-22 FIRING IS TRANSCRIBED, AND THE PASTE-BACK FAILURE HAS NOW HAPPENED FOUR TIMES.** The Sat 2026-08-22 scheduled firing **ran** (`cse_0195NQbHgY7PS24U8JCmB71S`, 29 turns, 264 s) and returned a **scoped null with no escalation**: egress still blocked, **09-01 10:00 observed standing, no defence motion to continue**, Q-45 still held nowhere. Its report was delivered to a push notification and a file attachment and **reached this repository only when an unrelated vault session compared this file's mtime against the routine's `last_fired_at` on 2026-08-24.** 🚨 **The root cause is unchanged and is not the paste step: the routine still has `No sources configured`, so it has no checkout to write to.** 🚨 **A second gap is recorded from this transcription: the vault staleness check cannot see this failure** — it measures this file's mtime, which only moves on a human/local write, so an unread cloud report reads as `ok` until the max age elapses. **Liveness is answerable only from the routine's run sessions via the API.** ⚠ The delivered 15.9 KB report file itself is still **not held**; what is transcribed is the run's own reported findings. **Next firing Wed 2026-08-26 09:00 EDT, against a repository it still cannot write to.**
**Prior status text (v1.7), retained:** **v1.7 — THE STATE'S REPLY IS BANKED, AND THE 08-18 BY-HAND COVER DID NOT RUN.** 🚨 **The planned Tue 2026-08-18 local run — named since Run 4 as the only document-capable cover for the State's reply — did not happen.** No row, no commit; the miss was found **2026-08-20 at session reconstruction, from outside this repository** (the vault's scheduled-check registry watching this file's mtime) — the same detection path as the 12-day gap. ✅ **The case did not suffer for it: Run 7 (local, 2026-08-20) ran the diff two days late and the route built for exactly this caught exactly this** — 16 new PDFs on the Fox mirror, two of them one byte-identical document: *"Reply Memorandum in Support of Preliminary Hearing Bindover,"* filed **2026-08-18** per its own certificate of service, **ACQUIRED AND BANKED** ([CR-ACQ-2026-08-20](CR-ACQ-2026-08-20_states-reply.md); provenance two-of-three, contents unread). ⚠️ **But cover-by-luck is Run 3's lesson repeated, and it is recorded as such, not absorbed silently.** ✅ **The Wed 2026-08-19 scheduled firing RAN** (egress-blind, day 15; no checkout) and its report — which correctly reported the reply filed, T1 via T3 — is **transcribed below, hand-pasted 2026-08-20 from the run log**. ⚠️ **Q-45 (opening brief): a July-folder CDX enumeration returned an attempted null — still unheld.** 🚨 **Escalation this run: route RECOVERY (Q-147's trigger, second application) — Fox/CDX is back, though measured intermittent (blocked and open twice within ten minutes on 08-20).** ~~👤 **The routine's prompt is now stale twice over** (it still carries "08-18: not filed" as background fact and lacks the recovery trigger) **and must be re-applied before the Sat 2026-08-22 09:00 firing.**~~ ✅ **DONE 2026-08-21 ~08:57 EDT, ~28 hours ahead of that firing** (`updated_at` 2026-08-21T12:57:10Z, independently re-fetched; six invariants intact). 🚨 **AND IT WAS STALE IN FOUR PLACES, NOT TWO.** Beyond the two named here, the SOURCING DISCIPLINE paragraph still carried **the Fox-mirror baseline at `55` PDFs** — Run 7 refreshed it to **71** on 08-20 — **and a route-status block stamped `as of 2026-08-16`**, predating both Run 6's 504 and Run 7's recovery. ⚠️ **The baseline is the serious one: a diff against 55 would have re-flagged this run's own sixteen triaged PDFs as new.** **Both were found only by reading the whole live prompt before diffing; neither appeared in any queue row here.** Standing lesson, now sharpened: **diff both ways AND diff the whole prompt — a queue row records what someone saw, never a census of what is wrong.**
**Prior status text (v1.6), retained:** **RUNS 5 AND 6 LOGGED. 🚨 T-1 TO THE STATE'S REPLY AND THE CHEAP-DIFF ROUTE IS DOWN.** **Run 6 (2026-08-17) escalates on a degradation trigger: the Fox outlet-mirror route is BLOCKED — Wayback CDX returns HTTP 504** — and that is the route Run 4 baselined to make Tuesday cheap. ⚠️ **The failure sits at the third-party index, not at the mirror; but blocked is not empty, it was not baselined, and the 08-18 cover is one route weaker than Run 4 left it.** ✅ **DocumentCloud is OPEN — a fourth observation and the first on a second consecutive day, so "intermittent" is now measured across four observations spanning two days.** ✅ **Rev 7/7 and Utah Courts 2/2 are ATTEMPTED nulls.** **No early filing on any attemptable route; nothing was expected.** ✅ **Q-147's route-RECOVERY trigger landed in `DOCKET-WATCH.md` today and Run 6 is its first application**; 👤 **the matching routine-prompt change is drafted and unapplied, and should land before the Wed 08-19 firing.** ⚠️ **The Tue 2026-08-18 by-hand run remains the only document-capable cover for the State's reply.**
**Prior status text (v1.5), retained:** **THE PASTE-BACK GAP IS CLOSED FOR THE FIRST TIME, AND A ROUTE THIS FILE RELIED ON HAS FAILED.** The **Sat 2026-08-15** firing ran, and its report is now **in this file** (hand-pasted 2026-08-16 from the run log) — the first time in this routine's history that a scheduled report reached the repository rather than an unread channel. It was a **null result with no escalation**, and **egress is still blocked, day 10**. 🚨 **Run 4 (local, 2026-08-16) escalates on a route trigger: the DocumentCloud API is now Cloudflare-gated from LOCAL sessions too**, reversing Run 2's "no longer bot-gated" — so the cheap post-08-18 sweep queued by the Q-45 attempt is unavailable. ✅ **Two routes confirmed open and now baselined for Tuesday:** Rev (enumerated from its own sitemap — **no new transcripts; all six held**) and the Fox outlet mirror (**55 PDFs in `2026/08`; the one Robinson item is the banked defence brief, byte-identical on re-fetch — integrity confirmed, provenance unchanged**). **Q-45 stays open; the State's 07-28 brief is still not held.** ⚠ **The Tue 2026-08-18 State's reply still has NO document-capable scheduled cover — the routine's next firing is Wed 08-19, after the deadline, and it is blind. A local run on 08-18/08-19 is the cover, and Run 4 left a diffable baseline to make it cheap.**
**Prior status text (v1.4), retained:** **THE GAP'S CENTRAL QUESTION IS RESOLVED: THE ROUTINE FIRED ALL THREE TIMES; ITS REPORTS WERE DELIVERED AND NEVER PASTED.** Established 2026-08-14 by direct API retrieval of the routine's own run sessions — see [Routine-liveness resolution — 2026-08-14](#routine-liveness-resolution--2026-08-14--not-a-run-of-the-spec). ⚠ **With it came a route finding this file did not have: every cloud firing since 2026-08-05 has run BLIND** — the cloud session's egress proxy 403-blocks all direct HTTPS document fetches (a control fetch of `example.com` included), so those runs were **search-index-only**. **The routine is enabled; next firing Sat 2026-08-15 09:00 ET — and it will run blind again unless its environment changes.**
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
| — | **2026-08-15** | scheduled firing | ✅ **IT RAN, AND FOR THE FIRST TIME ITS REPORT REACHED THIS FILE** (session `cse_01SmvswMBC5ozv2PFA8fTWtX`, 16 turns, 165 s) — hand-pasted 2026-08-16 from the run log. **Null result, no escalation. Egress still BLOCKED (day 10), both routes, control-confirmed.** Still no checkout and `No sources configured`. ⚠ **Its DocumentCloud / Scribd / mirror nulls are *unattemptable*, not empty — no evidential weight.** It escalated to a human that **the 08-18 window needs a LOCAL run** | No — egress *unchanged*, so the change-trigger correctly did not fire |
| **4** | **2026-08-16** | **local pre-cover: the 08-18 reply has no document-capable scheduled cover** | 🚨 **ESCALATION MET — the DocumentCloud API is newly Cloudflare-gated from LOCAL sessions** (403, three endpoints, two UAs), a regression against Run 2's "no longer bot-gated" and the 08-13 46/46 enumeration. **The queued post-08-18 DocumentCloud sweep is unavailable.** ✅ **Rev enumerated from its own sitemap: no new transcripts, all six held** — the first transcript null with real evidential weight. ✅ **Fox mirror route OPEN and baselined** (55 PDFs; one Robinson item = **the banked defence brief, byte-identical, SHA-256 re-verified** → integrity ✅, provenance unchanged). **Q-45 still open.** 09-01 stands; no continuance motion. **The 08-15 run's unresolved ambiguity RESOLVED** | 🚨 **YES — route trigger** |
| **5** | **2026-08-16**, late evening | **runner-verification pass, not a full spec execution** | ✅ **THE DOCUMENTCLOUD 403 WAS NOT A STANDING LOSS — the route is OPEN again**, third observed state in one day (403 at 09:00 · open 14:05 · open 22:47) with nothing changed at this end. **All four routes attemptable, zero drift against baseline**, so Tuesday is a diff. 🚨 **Found a gap in the spec itself: the escalation trigger list is ASYMMETRIC and has no trigger for a route that RECOVERS** → Q-147 | No — and Run 4's escalation is **resolved**, not re-raised |
| **6** | **2026-08-17** | **local, T-1 to the State's reply** | 🚨 **ESCALATION MET — the Fox outlet-mirror route is BLOCKED (Wayback CDX, HTTP 504), and it is the route Run 4 built the cheap 08-18 diff on.** ⚠️ **The failure is at the third-party INDEX, not the mirror — but blocked is not empty, it is not baselined, and tomorrow's cover is one route weaker than Run 4 left it.** ✅ **DocumentCloud OPEN — fourth observation, first on a second consecutive day; "intermittent" now measured across four observations over two days.** ✅ **Rev 7/7 and Utah Courts 2/2 — attempted nulls with real weight.** **No early filing. Q-147's recovery trigger landed in the spec today and this run is its first application** | 🚨 **YES — route trigger (degradation)** |
| — | *2026-08-18* | **planned local by-hand run — THE COVER FOR THE STATE'S REPLY** | 🚨 **DID NOT RUN.** No row, no commit; the repo is untouched after the 08-17 session close. **This was the one dated thing a session must not miss, and it was missed** — found 2026-08-20 from outside the repo (this file's mtime, via the vault's scheduled-check registry, max age 4 days). ⚠️ **The miss class is new: a planned ONE-OFF has no scheduled-firing anchor, so the "watch itself has stopped" trigger (keyed to scheduled firings) could not see it.** No row is backfilled; this row records the absence | *n/a — nothing ran* |
| — | **2026-08-19** | scheduled firing | ✅ **IT RAN** (session `cse_016wQT7cqdPdKWEwzVbWMZMi`, 21 turns, 259 s) — **transcribed below, hand-pasted 2026-08-20 from the run log via the remote-trigger API**; ⚠ the delivered report file itself (attachment uuid `14d7ce13-…`) is still NOT held. **Egress BLOCKED, day 15; no checkout; search-index only.** **One new item: the State's reply REPORTED FILED 2026-08-18** (T1 via T3, Fox + ABC legs; **reported 19 pp. against the 18-page limit — flagged by the run and left unreconciled**). Every document route unattemptable; it stated it could not verify whether the 08-18 local run had happened — **it had not** | No — egress unchanged; no case trigger met |
| **7** | **2026-08-20** | **local CATCH-UP: the planned 08-18 by-hand run did not happen** | 🚨 **THE STATE'S REPLY IS ACQUIRED AND BANKED** — *"Reply Memorandum in Support of Preliminary Hearing Bindover,"* filed **2026-08-18** per its own certificate of service; found by the Run-4 diff (16 new mirror PDFs; two URLs, one byte-identical document); **19 pp. vs the 18-page limit recorded, not reconciled**; provenance **two-of-three, same grade as the defence brief**; contents unread → [CR-ACQ-2026-08-20](CR-ACQ-2026-08-20_states-reply.md). **DocumentCloud 40/40 · Rev 7/7 · Utah Courts 2/2 — attempted nulls.** **Q-45 July-folder re-attempt: attempted null** (56 PDFs, none case-related). Baseline refreshed (Fox now 71 PDFs) | 🚨 **YES — route RECOVERY (Fox/CDX), Q-147's trigger, second application** |
| — | **2026-08-22** | scheduled firing | ✅ **IT RAN — and its report went unread for two days, the FOURTH instance of this failure class** (session `cse_0195NQbHgY7PS24U8JCmB71S`, 29 turns, 264 s, success) — **transcribed below 2026-08-24 from the run log via the remote-trigger API**; ⚠ the delivered report file itself (attachment uuid `a9f62b90-…`, 15,854 chars) is **NOT held here**, and the run **self-titled "Run 8"** — recorded, not renumbered. **NULL RESULT, scoped. Egress still BLOCKED; `No sources configured` again; no checkout.** **09-01 10:00 observed STANDING; NO defence motion to continue** (three targeted queries). **Q-45 still held nowhere.** Rev 7/7 already held. ✅ Two disciplines met unprompted: the outlet *"hearing concluded"* headlines were logged as a **source-side conflict and NOT adopted**, and the bullet-fragment/contempt trap reproduced and was **not conflated** — by-product, a ballistics-motion PDF URL, **queued unfetched**. ⚠ A 2026-07-10 Kirk-family motion was **date-pinned and excluded as not-new** | *Not met — all five triggers negative* |
| — | **2026-08-26** | scheduled firing | 🚨 **IT RAN — and produced the first MATERIAL finding since Run 7: a NEW DEFENCE FILING reported filed 2026-08-22**, opposition to the electronic media coverage orders for the 09-01 hearing, ruling on EMC applicability **pending**; `T1 via T3`, document not held. ⚠ **Not a motion to continue** (that risk searched two ways: null) and **does not move 09-01.** (session `cse_017Fd6cNGgWdHveUY2xCaZ3W`, 24 turns, 257 s) — **transcribed same-day, ~3h after firing**; ⚠ report file (uuid `bde1f037-…`) **NOT held**. **EGRESS BLOCKED — 21st straight; WebFetch blocked too.** **Q-45 still nowhere, 29 days open.** ✅ Rev sitemap logged **unattemptable not empty**; Fox baseline **not refreshed** (stands 71); DocumentCloud **not attempted so not a null**; ~10 Sinclair stations counted as **ONE** source | *Not met — all five triggers negative* |
| — | **2026-08-29** | scheduled firing — **THE LAST BEFORE 09-01** | 🚨 **IT RAN, and it is the SIXTH report that could not reach this repo** (session `cse_01WkDERotRAkUdZFg1mBvhkB`, 23 turns, 260 s) — **transcribed same-day, ~5h45m after firing**; ⚠ report file (uuid `cad3fabd-…`) **NOT held**. ⚠ **`next_run_at` is 2026-09-02 — the day AFTER the hearing, so this was the last scheduled cover and any further pre-hearing pass must be LOCAL.** **09-01 STANDS, firm at three days out, on TWO official-issuer sources**; **no motion to continue** (named risk, searched specifically). 🚨 **The 08-22 defence filing resolves to TWO filings — EMC oppositions (Salt Lake Tribune, KUTV) PLUS motions to seal the unredacted EMC material; the sealing motion is PENDING, no ruling located.** ⚖️ **Correctly logged as a watch item, not an escalation — a pending motion to seal is not a sealing.** **EGRESS BLOCKED, both routes control-tested.** Q-45 now **32 days** open. ✅ Fox baseline **not refreshed** (stands 71); blocked routes kept **unattemptable, not null**. ⚠️ **The run flagged a summariser hazard against its own evidence** — the utcourts notice was twice rendered as an 08-28 *hearing* date; that is the **publication path-date**, and the page body was unreachable. 🚩 **One loose end recorded unresolved: headlines referencing a ruling on closed hearings sit oddly against a sealing motion found pending — NOT adopted, queued first for the next pass** | *Not met — all five triggers negative* |

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
- **A NEW ARTIFACT THE LIBRARY DOES NOT HOLD:** "**Supplemental Notice Concerning Access to Evidence Presented in Open Court**" *(title carries a typo, "Evidennce", in the source metadata)*, DocumentCloud doc 28443912, **4 pages, created 2026-07-09 — i.e. filed DURING hearing week, between Day 4 and Day 5. 🛠 **CORRECTED 2026-08-16 (Q-111): the document's own Certificate of Delivery reads *"e-filed … on **July 8, 2026**"* — the evening of hearing **Day 3**, not between Days 4 and 5. **2026-07-09 is DocumentCloud's `created_at`** — a fact about a mirror, not about the court. ⚠️ **CR-ACQ-2026-08-14B corrected this on 2026-08-14 and said so in terms; it was never propagated back here. The project rule is that supersessions get matching log rows on BOTH ends — only one end had one.**** ⚠ **Its adjacency to the Exhibit 12.1 publication question rests on the TITLE ONLY.** Not retrieved; contents uncharacterised.
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
- **Q-03 partially unblocked:** two docket-listing documents are now retrievable without the XChange paywall, **but both are current only to **2026-03-14** 🛠 *(corrected 2026-08-16, R7: the last docket entry is 2026-03-14; 2026-03-15 03:18/03:21 is the printout's GENERATION stamp, not its coverage — every other file in the library says 03-14)*** and so do not cover this watch window. **The blocker on a CURRENT docket is unchanged.**
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
- ⚠ **A HASH TRAP, logged so the next run does not fall into it. The PDF DocumentCloud SERVES is not the file that was uploaded to it.** Downloaded 2026-08-13 from `s3.documentcloud.org/documents/28551955/defendant-tyler-james-robinsons-preliminary-hearing-briefing-8-11-26.pdf`: **383,293 bytes, SHA-256 `5c2c426b79febf1260b1b3458b379c184d609c1a36f18e6cc52bb8369d94e490`, SHA-1 `a408efc77654339c1eff1c13cde96339e5a25c34`** — different length and different hashes from the banked copy (**389,135 bytes**, SHA-256 `c3f394372192a6a3c6b791839a22a9ce4be43aea6f9985b9fc3703633bfde0e4`) **and** from DocumentCloud's own `file_hash`. It is nonetheless the **same document re-rendered by DocumentCloud's pipeline**: 41 pages, and its extracted text is **identical to the banked extraction after whitespace normalisation, 91,729 characters on both sides 🛠 **CORRECTED 2026-08-16 (Q-111, re-measured by the orchestrator): NOT IDENTICAL.** Under plain whitespace normalisation the banked Fox-mirror extraction is **91,729** characters and the DocumentCloud re-render is **91,715**. **They first diverge at character 671**, where the two-column caption is read in a different order — banked *"STATE OF UTAH, vs. Plaintiff, TYLER JAMES ROBINSON"* against *"STATE OF UTAH, Plaintiff, vs. TYLER JAMES ROBINSON"*. ⚠️ **The re-render also carries three `U+FFFE` line-break splits the banked extraction does not** (standing hazard 16). **Same document, same page count — NOT the same text**, exactly as CR-ACQ-2026-08-16 §6.2 later found for two extractions of one PDF. ⚠️ **Scope: this measures the artifact now on disk; the figure taken live on 2026-08-13 cannot be re-tested. And note the re-render's length CHANGED on 2026-08-16 when its 41 NULs became form feeds — a NUL is not whitespace and a form feed is, so pre- and post-repair figures are both correct at their own dates.**.** **Rule for future comparisons: never hash a DocumentCloud-served PDF against an original — compare against the API's `file_hash` field, which is the uploaded file's hash.** ⚠ **Scope of the "same file" claim above, stated exactly: it rests on the `file_hash` FIELD matching the banked copy's SHA-1, not on a byte-for-byte download — the download cannot test it, because what is served is a re-render.** What the download independently confirms is narrower and still worth having: the DocumentCloud copy is **the same document, same page count, same text**, so the two claims are consistent rather than circular.

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
| **NEW** | **Re-sweep DocumentCloud after 2026-08-18** for the State's reply and for any late upload of the 07-28 brief. The API route is open and the sweep is cheap. ⚠ **Early sweep run 2026-08-14: still absent** — title full-text `"Memorandum in Support of Preliminary Hearing Bindover"` → 0; case-number search newest items remain 2026-03-15/16; org-270's newest Robinson upload is still the 08-12 defence brief. Scoped null; the post-08-18 sweep stays queued |
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

## Cloud firing — 2026-08-15 · REPORT HAND-PASTED FROM RUN RECORDS

> **This is the first scheduled firing whose report reached this file.** The four before it (08-05, 08-08, 08-12 and this routine's whole history) were delivered into a claude.ai session and a mobile push and never pasted — the failure mode this file exists to catch. **Pasted 2026-08-16 from the routine's own run-session log via the remote-trigger API** (session `cse_01SmvswMBC5ozv2PFA8fTWtX`, fired 2026-08-15T13:01:17Z = **Sat 09:01 ET**, 16 turns, 165 s, `result: success`).
> ⚠ **Provenance of this section, stated plainly: it is transcribed from the condensed API run log, NOT from the report file the run produced.** That file (`CR-WATCH-2026-08-15.md`, delivered as attachment uuid `5c052481-52b0-46ae-ac0d-500e89e7adb2`) **is still not held by this repository** — it lives only in the routine's claude.ai session. The run log carries the run's own final summary in full, which is what is recorded below; where the log truncates, this section says so rather than filling the gap.

### 1. Egress status and escalation

**EGRESS: BLOCKED — unchanged, day 10.** The run performed the mandated control test first: `curl https://example.com/` returned **`curl: (56) CONNECT tunnel failed, response 403`**, and the proxy status endpoint logged it as a policy denial. It then tested the *second* route independently — `WebFetch` against the same control host — which returned **`EGRESS_BLOCKED`**. **Both routes are blocked, and the control host confirms the failure is environmental, not site-side.** No attempt was made to route around the proxy. The container was bare: `/home/user` empty, `No sources configured` in the environment log, so **no repository checkout existed** and nothing was committed.

**ESCALATION: NOT MET** — correctly. The escalation trigger is *"your egress has CHANGED in either direction"*; it did not change, it persisted. No bindover ruling; 09-01 not moved; nothing sealed or unsealed; no previously-working route newly failing **from that environment**.

### 2. Findings — all search-index-only, and scoped as such

| Check | Result |
|---|---|
| **New filings** | **Scoped null.** The State's 08-18 reply was **not yet due** (three days out); no early filing indexed. **Q-45 unchanged** — no mirror of the 07-28 brief located; status stays **T1 via T3**, not promoted |
| **Bullet-fragment ruling** | **Not found.** The search reproduced the known trap exactly, returning the **2026-06-26 contempt ruling** instead. Not conflated; still unobtained |
| **New transcripts** | **Scoped null.** Only the known July preliminary-hearing days surfaced. **No URL was guessed and no 404 was read as absence** — the slug-trap discipline held |
| **Scheduling** | **09-01, 10:00 standing.** No defence motion to continue found, checked specifically |

🚨 **The run's own most important caveat, and it is a strong one:** the DocumentCloud API, Scribd and outlet-mirror routes were **unattemptable rather than empty**. **Those nulls carry no evidential weight** — they are facts about the environment, not about the world. The run said so itself rather than reporting four clean negatives.

### 3. What the run escalated to a human

1. **The report requires hand-pasting** — no checkout, so `DOCKET-WATCH.md`'s calendar table was not updated either. *(Closed by this section and by Run 4.)*
2. **"The 08-18 window needs a LOCAL run."** The run stated directly that a cloud run on that date **cannot acquire the reply at all**, because the outlet-mirror route that landed the defence brief is unreachable from its environment. *(Acted on — see Run 4, which establishes the mirror baseline three days early.)*
3. **One ambiguity it deliberately left unresolved rather than guessing** — an 08-13 aggregator headline. The API log truncates the sentence, so **this file does not record what the run meant**; Run 4 resolved the question independently rather than reconstructing it. → Run 4 §4.

**No register entry assigned, resolved or moved; no case-posture statement altered; no filing's contents characterised.** ⚠ As of 2026-08-15 Tyler Robinson has NOT been bound over for trial.

---

## Run 4 — 2026-08-16 · LOCAL, EGRESS-CAPABLE · pre-cover for the 08-18 window

**Trigger:** not a scheduled firing. Run from a local session **because the 2026-08-18 State's reply has no document-capable scheduled cover** — the cloud routine is egress-blind (10 days) and its next firing is **Wed 2026-08-19, after the deadline**. Retrieval date for everything below: **2026-08-16**.

### 1. ESCALATION — MET · route trigger

🚨 **THE DOCUMENTCLOUD API HAS STARTED FAILING FROM LOCAL SESSIONS.** This is the spec's *"a route that previously worked has started failing"* trigger, and it is a **regression against this file's own record**: Run 2 (v1.1) logged the API as **"no longer bot-gated"**, and the 2026-08-13 Q-45 attempt used it to enumerate project 224251 **46 of 46 across three cursor pages**. Today it is gated again.

| Endpoint | Result |
|---|---|
| `https://api.www.documentcloud.org/api/documents/search/?q=%2Bproject%3A224251` | **HTTP 403**, `server: cloudflare`, 5,802-byte "Attention Required! \| Cloudflare" interstitial |
| `https://www.documentcloud.org/api/documents/search/?q=%2Bproject%3A224251` | **HTTP 403**, identical interstitial |
| `https://api.www.documentcloud.org/api/documents/?per_page=1` | **HTTP 403**, identical interstitial |

**Tested with a default agent UA and with a current desktop-Chrome UA; both 403.** So it is not UA-shaped, and it is not this project's usual JS-gating of the *web UI* — **the API itself is now behind the challenge.** ⚠ **Consequence, and it is the one that matters on Tuesday: the "post-08-18 DocumentCloud sweep" queued as a cheap retry by the v1.3 Q-45 attempt is NOT AVAILABLE unless this lifts.** Local egress itself is fine — the control fetch `https://example.com/` returned **HTTP 200** — so this is site-side, the mirror image of the cloud runner's problem.

### 2. New filings — scoped null, with one positive identification

**The State's reply is not yet due (Tue 2026-08-18); nothing was expected and nothing was found.** Reporting independently confirms the briefing schedule this project already holds at Tier 1: State 07-28 → defence 08-11 → **State's rebuttal 08-18** → argument 09-01 *(`https://www.deseret.com/utah/2026/07/29/this-is-a-close-case-state-tells-judge-in-tyler-robinson-case/`, `https://www.ksl.com/article/51596294/tyler-robinson-preliminary-hearing`; retrieved 2026-08-16)*. ⚠ **Outlets call the 08-18 filing the State's "rebuttal"; this library calls it the State's "reply." Same filing, same 18-page limit** — recorded so a future search does not treat the two words as two documents.

🔍 **POSITIVE IDENTIFICATION — the Fox mirror route carries a Robinson case PDF, and it is one this project already holds.** Enumerating `static.foxnews.com/foxnews.com/content/uploads/2026/08/*` through the Wayback CDX API (55 PDFs, `collapse=urlkey`, mimetype-filtered) surfaced exactly one case-relevant item:

| | |
|---|---|
| **URL** | `https://static.foxnews.com/foxnews.com/content/uploads/2026/08/robinson-prelim-filing.pdf` |
| **First capture** | 2026-08-13 06:22:14 UTC (Wayback CDX) |
| **Fetched live** | 2026-08-16, **HTTP 200, 389,135 bytes**, `application/pdf`, PDF v1.6 |
| **SHA-256** | `c3f394372192a6a3c6b791839a22a9ce4be43aea6f9985b9fc3703633bfde0e4` |
| **Identification** | **Byte-identical to the banked defence brief** — `2026-08-11_defendant-prelim-hearing-briefing.pdf`, same 389,135 bytes, same SHA-256, **compared by hashing both files rather than by trusting this log's record of the first** |

**What this is and is not.** ✅ It is a genuine **integrity check**: an independent re-fetch from the origin mirror, five days after banking, reproduces the banked bytes exactly — the banked copy is faithful to its source and has not drifted. ❌ It is **not** a provenance gain: identical bytes are the *same rendering*, so **provenance stays two-of-three and the clerk file-stamp gap (Q-63) is untouched.** ⚠ **And it is not Q-45** — this is the defence brief, not the State's. **Q-45 remains open and the State's 07-28 brief remains unheld.**

⚠ **A name trap worth logging**, because it will recur on Tuesday: filename-matching `robinson` across that Fox directory also returns **`bijan-robinson-falcons-saints-victory.jpg`** — an unrelated football item. **Match on the case, not on the surname.**

### 3. New transcripts — a null with real evidential weight, for the first time

**NONE beyond the six this library already holds.** This null is **not** search-index-only and **not** built from guessed-slug 404s: it comes from **Rev's own sitemap** (`https://www.rev.com/sitemap.xml`, gzipped, retrieved 2026-08-16, HTTP 200), which enumerates every transcript page the site publishes.

| Rev slug | Held? |
|---|---|
| `ut-v-tyler-robinson---day-1` *(known slug trap)* | ✅ `day1.txt` |
| `ut-v-tyler-robinson-preliminary-hearing-day-2` | ✅ `day2.txt` |
| `ut-v-tyler-robinson-preliminary-hearing-day-3` | ✅ `day3.txt` |
| `ut-v-tyler-robinson-preliminary-hearing-day-4` | ✅ `day4.txt` |
| `ut-v-tyler-robinson-preliminary-hearing-day-5` | ✅ `day5.txt` |
| `tyler-robinson-comtempt-hearing` *(Rev's own misspelling)* | ✅ acquired 2026-08-14 |

**Seven `robinson` entries appear in the sitemap; the seventh is `general-lori-robinson-unh-commencement-speech-transcript`, unrelated.** All three known case slugs additionally returned HTTP 200 on direct check. **Route status: `rev.com` OPEN from local.** ⚠ Rev's `/transcripts/search?q=` path returns **404** — it is not a search endpoint; **the sitemap is the enumeration route that works**, and it should replace slug-guessing in future runs.

### 4. Scheduling — 09-01 stands · no continuance motion · and the 08-15 ambiguity resolved

**No defence motion to continue found**, checked specifically, across two targeted searches. **The 2026-09-01 10:00 argument is restated as standing** by current reporting *(`https://thepostmillennial.com/judge-graf-to-rule-on-probable-cause-to-try-tyler-robinson-for-charlie-kirks-killing-sept-1`, `https://www.ksl.com/article/51596294/tyler-robinson-preliminary-hearing`; retrieved 2026-08-16)*, with four hours total allocated — consistent with CR-ACQ §5.1, which remains canonical and is not amended.

✅ **The ambiguity the 08-15 cloud run flagged and would not guess at is RESOLVED, independently.** The mid-August aggregator wave — e.g. `https://thehill.com/regulation/court-battles/6026466-kirk-tyler-robinson-death-penalty-defense/`, `https://www.sltrib.com/news/2026/08/12/charlie-kirk-shooting-tyler/`, `https://www.deseret.com/utah/2026/08/12/tyler-robinson-contends-state-has-not-proven-elements-needed-for-aggravated-murder/` (all retrieved 2026-08-16) — **is downstream coverage of the 2026-08-11 defence brief this library already holds as a document.** It is **not a new filing, ruling or scheduling event.** ⚠ **Those articles characterise and quote the brief's contents; per DOCKET-WATCH's prohibition none of that is recorded here** — this project holds the document itself, and CR-E07 is where a reasoned read belongs.

⚠ **One candidate escalation was checked and CLEARED rather than left ambiguous.** A search result headlined *"Judge unseals documents in Charlie Kirk murder case"* (`https://www.courthousenews.com/judge-unseals-documents-in-charlie-kirk-murder-case/`) would meet the *"a filing has been sealed or unsealed"* trigger if current. **It is dated 2026-03-13** — read from the article body, HTTP 200, 105,473 bytes, retrieved 2026-08-16. **Five months old; trigger NOT met.** Recorded because a checked-and-negative is worth more than an unchecked headline.

### 5. Q-45 — cheap retries run, all still closed

| Route | Result 2026-08-16 |
|---|---|
| **archive.today** (Scribd doc `1067587104`) | **HTTP 429** on `archive.ph` and `archive.is` (55,543 bytes, rate-limit interstitial); `archive.today` returned **404** on the `/newest/` path form. ⚠ **NOT ESTABLISHED — a rate-limit is not an absence.** Third consecutive 429 across three sessions |
| **Wayback CDX** (Scribd doc) | **HTTP 200, empty result set `[]`** — a true scoped null. **Zero captures exist.** Confirms the 08-13 finding |
| **Fox outlet mirror** | Enumerated (§2). **No State's brief.** The only Robinson item is the defence brief already held |
| **DocumentCloud sweep** | ⛔ **UNAVAILABLE — newly Cloudflare-gated (§1).** Not a null |
| **Scribd direct** | Not re-attempted; the v1.3 attempt logged seven endpoints behind an identical challenge and nothing suggests it changed. Stated as scope, not as a null |

**Q-45 remains OPEN. The State's 2026-07-28 brief is still NOT HELD, its contents remain unrecorded, and it stays T1 via T3.** The remaining real routes are unchanged and both 👤: an owner-driven browser session (Q-32(b)) or Utah XChange (~$10, which would also address **Q-63**).

### 6. Queued for the next run

1. 🚨 **Re-run this sweep on Tue 2026-08-18 / Wed 2026-08-19, locally.** The Fox-mirror baseline is now recorded (55 PDFs in `2026/08`, one Robinson case item) — **a diff against it is the cheapest possible detector for the State's reply appearing.**
2. **Re-test DocumentCloud.** If the Cloudflare gate lifts, the queued post-08-18 sweep becomes available again; if it persists past the next run, it should be recorded as a standing route loss rather than a transient.
3. **Watch specifically for a defence motion to continue** — still the named, expected risk, and still unrealised.

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No filing's contents are characterised here. No evidence file was created.** ⚠ As of 2026-08-16, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.

---

## Run 5 — 2026-08-16, late evening · LOCAL · RUNNER-VERIFICATION PASS, not a full spec execution

**Trigger:** not a scheduled firing and not a full run. Executed to **de-risk the 2026-08-18 window by proving the diff runner works and the stored baseline still holds** — so that Tuesday is a diff and not a debugging session. Retrieval time: **2026-08-16, 22:47 EDT**.

⚠️ **SCOPE, STATED FIRST BECAUSE IT BOUNDS EVERYTHING BELOW. This is a PARTIAL execution of the DOCKET-WATCH spec.** `./docket-watch-run.py` covers the four mechanical routes only. **The spec's search-dependent legs were NOT run:** no web search for scheduling changes, and **no specific check for a defence motion to continue** — the named, expected risk. **Nothing here is evidence about those questions in either direction.**

### 1. Escalation — NOT MET · and Run 4's escalation is RESOLVED rather than re-raised

✅ **THE DOCUMENTCLOUD API IS OPEN AGAIN.** The case-number search returned **40 documents**, matching baseline. ⚠️ **That is the third observed state in a single day** — **403 behind a Cloudflare interstitial at 09:00, open at 14:05, open again at 22:47** — with nothing changed at this end between them. 🚨 **Run 4 escalated the 403 as a possible standing route loss. It was not one.** ✅ **The "INTERMITTENT" characterisation is now measured across three observations rather than inferred from two, and the operative rule is unchanged and reinforced: never log this route's silence as a null. A blocked route is unattemptable, not empty.**

🚨 **A GAP IN THE SPEC ITSELF, FOUND BY THIS RUN AND QUEUED BELOW: the escalation trigger list is ASYMMETRIC.** It fires on *"a route that previously worked has started failing"* — **there is no trigger for a route that had failed and has RECOVERED.** ⚠️ **Recovery changes what is possible on the next run** (here, it puts the cheap post-08-18 DocumentCloud sweep back on the table), **so a watch that only escalates degradation will silently under-report its own capability.** This run had to notice it by reading a diff.

### 2. Route status — all four attemptable, zero drift

| Route | This run | Baseline | Result |
|---|---|---|---|
| DocumentCloud case-number search | 40 documents | 40 | **no new documents** |
| Fox outlet mirror (Wayback CDX) | 55 PDFs, 2 flagged case-related | 55 | **no new PDFs** — the second flag is the known *"Preliminary Injunction"* false positive already carried in the baseline, deliberately not re-raised |
| Rev transcripts (sitemap) | 7 `robinson` URLs | 7 | **no new transcripts** |
| Utah Courts press notices | 2 matching notices | 2 | no change |

✅ **Every route returned OK — none returned BLOCKED — so all four nulls above are ATTEMPTED nulls and carry evidential weight**, which is the distinction the runner exists to preserve.
⚠️ **The baseline was deliberately NOT refreshed** (`--baseline` not passed): nothing new was found, so there was nothing to bank, and refreshing a baseline that has not moved only risks writing a transient state into it.

### 3. The case — nothing observed, and nothing was expected

**The State's reply is due Tue 2026-08-18 and was not due tonight.** No early filing indexed on any attemptable route; no mirror. **09-01 was not re-checked** (see the scope caveat) and this run makes no statement about it.

### 4. Queued out of this run

1. 🚨 **The 2026-08-18 by-hand run still stands and is still the only document-capable cover.** This pass verified the instrument, not the window.
2. **Add a route-RECOVERY escalation trigger to the DOCKET-WATCH spec and to the routine's prompt** (§1 above) — the trigger list currently cannot see a capability returning.
3. **Re-attempt the post-08-18 DocumentCloud sweep**, which Run 4 recorded as unavailable and which this run shows is available again — subject to the route being intermittent, so attempt it rather than assume it.

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No filing's contents are characterised here. No evidence file was created.** ⚠ As of 2026-08-16, Tyler Robinson has NOT been bound over for trial, and the preliminary hearing is not concluded — 2026-09-01 is its last day. Presumption of innocence applies throughout.

---

## Run 6 — 2026-08-17 · LOCAL · T-1 to the State's reply

**Trigger:** not a scheduled firing. Executed on the day **before** the 2026-08-18 State's-reply deadline, to (a) confirm the diff runner and baseline still hold so Tuesday is a one-day diff rather than a debugging session, and (b) catch an early filing if one existed. Retrieval time: **2026-08-17, ~07:5x EDT**.

⚠️ **SCOPE, STATED FIRST BECAUSE IT BOUNDS EVERYTHING BELOW. This is a PARTIAL execution of the DOCKET-WATCH spec**, identical in scope to Run 5. `./docket-watch-run.py` covers the four mechanical routes only. **The spec's search-dependent legs were NOT run:** no web search for scheduling changes, and **no specific check for a defence motion to continue.** **Nothing here is evidence about those questions in either direction.**

### 1. Escalation — 🚨 **MET.** A route that previously worked has started failing

**The Fox outlet-mirror route is BLOCKED.** The Wayback CDX index returned **HTTP 504 Gateway Time-out**. ⚠️ **This is the route Run 4 built the cheap 08-18 diff on** — 55 PDFs in `2026/08`, exactly one case item — and today it cannot be attempted at all.

⚠️ **Locate the failure precisely, because the two possibilities have different consequences:** the 504 comes from the **Wayback CDX API**, a third-party index, **not from the Fox mirror itself**. The mirror has no index page of its own, which is *why* the route depends on CDX. **So this is most likely a transient outage of the index rather than a change at the source — but "most likely" is not a finding, and the operative rule does not depend on which it is:**

> 🚨 **BLOCKED IS NOT EMPTY. Today's Fox result carries no evidential weight in either direction and must not be baselined.** If a mirror item appeared today, this run would not have seen it.

✅ **Consequence for tomorrow, and it is the reason this run was worth doing:** the 08-18 cover is **one route weaker than Run 4 left it.** The Fox route must be **re-attempted** on Tuesday, and if CDX is still down, the mirror needs a different enumeration path or the cover rests on DocumentCloud and Rev alone.

### 2. ✅ Route recovery — and the trigger for reporting it exists as of today

**The DocumentCloud API is OPEN.** The case-number search returned **40 documents**, matching baseline.

⚠️ **This is the FOURTH observation of that route's state, and the FIRST on a second consecutive day:** 403 at 09:00 on 08-16 · open at 14:05 · open at 22:47 · **open at ~07:5x on 08-17.** **"Intermittent" is now measured across four observations spanning two days**, and the operative rule is unchanged: **never log this route's silence as a null.**

✅ **The route-RECOVERY escalation trigger that Run 5 identified as missing was added to `DOCKET-WATCH.md` earlier today (Q-147), and this run is its first application:** DocumentCloud's continued availability is reported here **as a capability**, not left to be inferred from a diff — **it means the post-08-18 DocumentCloud sweep is cheap and should be attempted rather than assumed unavailable.** 👤 **The matching change to the routine's own prompt is drafted and awaiting authorisation** ([DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md](../DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md)) and should land before the **Wed 08-19** firing.

### 3. Route status

| Route | This run | Baseline | Result |
|---|---|---|---|
| DocumentCloud case-number search | 40 documents | 40 | **no new documents** — an ATTEMPTED null |
| **Fox outlet mirror (Wayback CDX)** | 🚨 **BLOCKED — HTTP 504** | 55 PDFs | **UNATTEMPTABLE. Not a null. Not baselined.** |
| Rev transcripts (sitemap) | 7 `robinson` URLs | 7 | **no new transcripts** — an ATTEMPTED null |
| Utah Courts press notices | 2 matching notices | 2 | no change — an ATTEMPTED null |

⚠️ **The baseline was deliberately NOT refreshed** (`--baseline` not passed). Nothing new was found, and **refreshing while one route is blocked would bank a hole as though it were a state.**

### 4. The case — nothing observed, and nothing was expected

**The State's reply is due Tue 2026-08-18 and was not due today.** No early filing was indexed on any attemptable route. **09-01 was not re-checked** (see the scope caveat) and this run makes no statement about it. **No filing's contents are characterised here.**

### 5. Queued out of this run

1. 🚨 **The 2026-08-18 by-hand run still stands and is still the only document-capable cover.** This pass verified the instrument and found one of its four routes down.
2. **Re-attempt the Fox/Wayback CDX route on 08-18.** If it is still 504, record a standing route-degradation and find a second enumeration path for the mirror — **the cheap diff Run 4 built depends on it.**
3. 👤 **Apply the Q-147 prompt change before the Wed 08-19 firing.**

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No evidence file was created.** ⚠ **As of 2026-08-17, Tyler Robinson has NOT been bound over for trial, and the preliminary hearing is not concluded — 2026-09-01 is its last day, argument only on a closed evidentiary record.** Presumption of innocence applies throughout.

---

## Scheduled firing 2026-08-19 — report transcribed 2026-08-20 · NOT executed by this repository

**Provenance of this section:** transcribed **2026-08-20** from the run-session log via the remote-trigger API (session `cse_016wQT7cqdPdKWEwzVbWMZMi`, created 2026-08-19T13:01:32Z = **09:01 EDT**, 21 turns, 259 s, result `success`). ⚠ **The report file the run delivered (attachment uuid `14d7ce13-568f-437f-a198-fc80c891d976`) is still NOT held here** — this section records the run's logged findings, not the artifact. The run itself correctly flagged, at the top of its report, that it required hand-pasting.

### 1. Egress and environment

- **Egress BLOCKED — 15th consecutive day.** Control fetch of `https://example.com/` returned `CONNECT tunnel failed, response 403` at the session proxy; the harness `WebFetch` was blocked by the same policy (`EGRESS_BLOCKED`). Web search was the only functioning route; the run stated it made no attempt to route around the proxy.
- **No repository checkout** (`/home/user` empty; `No sources configured`) — nothing was committed by the run.

### 2. The run's findings, as logged

- **Escalation: NOT met**, per the run — no bindover, 09-01 unmoved, no new sealing/unsealing, no route newly failing, egress unchanged. ("Sealed transcript released" search hits were checked by the run and identified as coverage of an older matter — cleared, not conflated.)
- 🚨 **One new item: the State's reply brief REPORTED FILED 2026-08-18** — **T1 via T3** (Fox + ABC as the independent legs). The deadline this watch exists to cover was reported met. **The document was not held by that run.** ⚠ **Reported length 19 pp. against the recorded 18-page limit — flagged by the run and deliberately left unreconciled** (its stated discipline, mirroring 28-vs-35 on the opening brief). The run recorded existence, date and reported length only; search snippets carried quotations from the filing and the run withheld them.
- **Unattemptable, not empty** (the run's own scoping): DocumentCloud API, Rev sitemap, the Fox-mirror baseline diff, Scribd — all `HTTP 000` / `CONNECT 403`. **The Fox-mirror diff — the designed detector for exactly this filing — never ran in that session.**
- **Genuine nulls, scoped:** no ruling on the bullet-fragment motion indexed (searches again surfaced the 2026-06-26 contempt ruling — a different matter, not conflated); **no defence motion to continue 09-01 indexed.**
- The run stated it **could not verify whether the 2026-08-18 local by-hand run had happened** (no checkout, no log to read) — and flagged that if it had not, its own search-only report was the only coverage of the reply's filing window. **It had not** (see Run 7).

---

## Run 7 — 2026-08-20 · LOCAL · CATCH-UP: the 08-18 cover did not run

**Trigger:** not a scheduled firing. 🚨 **The planned Tue 2026-08-18 by-hand run — named since Run 4 as "the only document-capable cover" for the State's reply — DID NOT HAPPEN.** No row, no commit; this file's mtime sat at 2026-08-17 07:56. The miss was found **2026-08-20 ~10:54 EDT during session reconstruction, from outside this repository** — the vault's scheduled-check registry watches this file's mtime with a 4-day max age, which is the same class of external detection that found the 12-day gap. This run is the catch-up, two days late. Retrieval window for everything below: **2026-08-20, ~10:55–11:10 EDT.**

⚠️ **The miss class is worth naming: a planned ONE-OFF has no anchor.** The "watch itself has stopped" trigger (added 2026-08-13) is keyed to *scheduled firings*; a one-off local run that simply never starts trips nothing. The external mtime watch caught it at T+2 — inside its design window, but after the filing date it existed to cover. **The case did not suffer for it (see below) — but that was luck, not the system working. Run 3's epitaph, verbatim, applies again.**

**Scope:** the four mechanical routes via `./docket-watch-run.py` (diff against Run 4's baseline), caption-level triage of flagged newcomers, a Q-45 re-attempt, and the transcription above. **The spec's search-dependent legs were NOT re-run locally** — the most recent search coverage of scheduling changes and a defence motion to continue is the 2026-08-19 firing (transcribed above, both nulls, search-index only). This run makes no independent statement on those questions.

### 1. Escalation — 🚨 MET: route RECOVERY (Q-147's trigger, second application)

**The Fox outlet-mirror route is BACK.** Run 6 (08-17) found the Wayback CDX index HTTP 504 — unattemptable — and queued a re-attempt. Today the index answered and the mirror enumerated: **71 PDFs under `2026/08` against the 55-PDF baseline.** Per Q-147, the recovery is reported as a capability, not left to be inferred from a diff — and the capability was used the same hour (see §3).

⚠️ **The intermittency is now measured on this route too:** open ~10:57 → **blocked ~11:05** (baseline pass, correctly refused to bank a hole) → open ~11:07 (retry; baseline then refreshed). Same shape as DocumentCloud's 08-16 day. **Operative rule: retry a CDX failure before recording a block, and never baseline through one.**

### 2. Route status

| Route | This run | Baseline | Result |
|---|---|---|---|
| DocumentCloud case-number search | 40 documents | 40 | **no new documents — an ATTEMPTED null.** The route is OPEN again locally (the 08-16 gating did not persist); "intermittent" remains the standing description |
| **Fox outlet mirror (Wayback CDX)** | ✅ **RECOVERED — 71 PDFs** | 55 | 🚨 **16 NEW PDFs → §3.** Baseline refreshed to 71 after triage |
| Rev transcripts (sitemap) | 7 `robinson` URLs | 7 | **no new transcripts — an ATTEMPTED null** (all six case transcripts held) |
| Utah Courts press notices | 2 matching notices | 2 | no change — an ATTEMPTED null |

### 3. 🚨 THE STATE'S REPLY IS ACQUIRED AND BANKED

Of the 16 newcomers, the over-inclusive matcher flagged three; caption checks resolved all of them, and one unflagged item was checked besides:

- **`Prosecutor_Reply.pdf` and `744b16b3-Prosecutor_Reply.pdf` are ONE DOCUMENT — byte-identical (`cmp` clean, same SHA-256), and it is the filing this watch existed to catch:** *"Reply Memorandum in Support of Preliminary Hearing Bindover,"* Fourth Judicial District Court, **Case No. 251403576**, Judge Tony F. Graf, Jr.; **filed 2026-08-18 per its own certificate of service** (e-filed; `/s/ Christopher D. Ballard` for Jeffrey S. Gray, Utah County Attorney). **Banked** at `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.pdf` (277,548 B, SHA-256 `0e287a048829b100f9b7e003d2b1475c75b43d0e755fff4f7f6f9fa67dfd14f2`) + unread `.txt` extraction. **Full acquisition record: [CR-ACQ-2026-08-20](CR-ACQ-2026-08-20_states-reply.md).**
- ⚠ **Provenance two-of-three** — signature block ✅, certificate of service ✅, clerk file-stamp ❌ — the identical grade to the banked defence brief. Outlet-hosted; not silently promoted.
- ⚠ **19 PDF pp., printed numbering to 19 (p. 19 is the certificate of service), against an 18-page limit — recorded, deliberately NOT reconciled.** This corroborates the 08-19 firing's reported "19 pp." independently, from the document itself.
- **Pages viewed: 1, 18, 19 — caption and attestation only. Pages 2–17 unread; no content recorded anywhere.**
- **Cleared lookalikes:** `abdulloi-toshpulodzoda-court-filing.pdf` → Circuit Court of Fairfax County, Virginia — unrelated, cleared by caption. `order-081726.pdf` → Supreme Court of New York, an unrelated matter — **checked though the matcher did not flag it**, because the bullet-fragment ruling is unheld and a case order could hide behind a generic filename; cleared by caption. ⚠ **Matcher gap, observed not fixed: filenames like `order-*.pdf` never flag.** The remaining 12 newcomers are facially unrelated by self-describing filename and were not fetched.

### 4. Q-45 re-attempt — an ATTEMPTED null

With CDX recovered, the mirror's **`2026/07/` folder was enumerated for the State's opening brief: 56 PDFs, none case-related** (two pattern matches on "preliminary," both self-describing as unrelated; cleared at filename level, stated as such). **Q-45 stays open — the opening brief is still held nowhere.**

### 5. Queued out of this run

1. 👤 **Re-apply the routine's prompt before the Sat 2026-08-22 09:00 firing.** It is now stale twice over: it still carries *"2026-08-18: not yet due and not filed"* as background **fact** (the false-premise hazard the 08-16/08-17 re-sync cycle documented), and it lacks Q-147's recovery trigger. DOCKET-WATCH.md's calendar changed again today; **by the two-copies rule, that edit is unfinished until the prompt is re-applied and re-fetched.**
2. **A reasoned read of the banked reply** — a separate act, a CR-E evidence file under the two-layer discipline; not a watch row and not started here.
3. **Court-stamped copies of all three cycle briefs** remain sought (the defence brief's stamp gap is Q-63; the reply now shares the same grade).
4. **Q-45 unchanged** — the opening brief is the only cycle document still unheld in any form.

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. The reply's contents are not characterised beyond its title and date; no evidence file about its contents exists.** ⚠ **As of 2026-08-20, Tyler Robinson has NOT been bound over for trial, and the preliminary hearing is not concluded — 2026-09-01 is its last day, argument only on a closed evidentiary record.** Presumption of innocence applies throughout.

---

## 2026-08-22 scheduled firing — TRANSCRIBED (cloud run; the run self-titled "Run 8")

> ⚠ **TRANSCRIBED 2026-08-24 from the run-session log via the remote-trigger API** (`cse_0195NQbHgY7PS24U8JCmB71S`, **29 turns, 264 s, result success**; fired `2026-08-22T13:00:58Z` = **09:00:58 EDT**, last event `13:05:31Z`). **This is the SECOND time this routine's output has reached the repository, and the second time it had to be recovered rather than delivered.**
>
> ⚠ **THE DELIVERED REPORT FILE ITSELF IS STILL NOT HELD HERE.** The run wrote a **15,854-character** report to `/home/user/CR-WATCH-log-RUN8-2026-08-22.md` and delivered it via `SendUserFile` (attachment uuid `a9f62b90-10de-466e-ae6a-1b6df628ac16`) plus a `PushNotification`. **The session did not persist** (`persist_session: false`), so what follows is transcribed from the condensed run log and the run's own closing summary — **it is a faithful record of what the run reported, not the 15.9 KB report verbatim.** Stated rather than implied, per the Run-4/v1.5 precedent.
>
> 🚨 **NUMBERING, recorded rather than silently reconciled: the run titled its own report "Run 8."** This index reserves numbered rows for runs whose report reached this file at the time, and gives scheduled firings a `—` row (08-05, 08-08, 08-12, 08-15, 08-19). **This firing takes a `—` row on that convention, so a later reader does not conclude a "Run 8" is missing — it is this section.** The next *local* run should take the number 8.

### 0. How this was found — the fourth instance of the same failure

**Found 2026-08-24 ~20:45 EDT from outside this repository**, during an unrelated vault session's reconstruction: this file's mtime read **2026-08-21 09:00** while the routine's `last_fired_at` read **2026-08-22T13:00:58Z**. The firing happened; the report went to a push notification and a file attachment; **nothing brought it here.** That is the same shape as 08-05, 08-08 and 08-12 — *reports delivered and never pasted* — and it is now the fourth instance.

🚨 **A GAP IN THE STALENESS CHECK ITSELF, found by this transcription and recorded because nothing else would catch it.** The vault's `scripts/check-scheduled.sh` registers this watch at a **4-day max age against this file's mtime**. But this file's mtime only moves when **a human or a local session writes to it** — a cloud firing that reports into an unread channel does not touch it. So across 08-22 and 08-23 the check reported **`ok` (3d)** while the report sat unread, and it would not have flagged until **08-25**, three days after the firing. ⚠ **The check measures paste-back latency, not firing liveness, and those are different failures.** The liveness question is answerable only from the routine's own `last_fired_at` / run-session list via the API — which is not part of the check. **Recorded as an observed design gap; not fixed here.**

### 1. EGRESS STATUS + ESCALATION

**EGRESS: BLOCKED — unchanged since 2026-08-05.** The mandated control fetch of `https://example.com/` returned `curl: (56) CONNECT tunnel failed, response 403`; the session proxy's own status endpoint logged the denial (`connect_rejected`, policy denial, `13:01:13Z`). **`WebFetch` was also unavailable** (*"Unable to verify if domain example.com is safe to fetch"*). The run states explicitly that it **did not attempt to route around the proxy**, and that **every observation in the run is search-index-only.**

**NO CHECKOUT.** `/home/user` was empty; `find` for `*kirk*`, `*robinson*`, `DOCKET-WATCH.md`, `CR-WATCH-log.md` returned nothing. **Nothing was appended, committed or pushed by the run**, and its report carried the mandated hand-pasting banner. ⚠ The environment log again reads **`No sources configured`** — the repository is *still* not attached to the routine, which is the standing cause of this whole failure class.

**ESCALATION: NOT MET** — all five triggers checked and negative: no bindover ruling; **2026-09-01 observed standing**; nothing sealed or unsealed; **no route observed to change state in either direction**; egress unchanged in either direction since the last run.

### 2. Calendar status — observed

| Date | Observed status | Basis |
|---|---|---|
| 2026-07-06 → 07-10 | Five days of evidence; **hearing NOT concluded** | Tier 1 Day 5 transcript (held); the run did **not** adopt outlet headlines to the contrary — see §5 |
| 2026-07-28 | State's opening brief — **reported filed; document still unheld (Q-45)** | search index only; no mirror surfaced this run |
| 2026-08-11 | Defence response — **filed and banked** (held) | unchanged |
| 2026-08-18 | State's reply — **filed and banked** (held) | unchanged |
| **2026-09-01, 10:00** | **OBSERVED STANDING** — argument only, in person | multiple index sources; **no motion to continue found** |

### 3. New filings — a SCOPED NULL

**No new filing found.** Routes attempted, all via web search (the only channel available under the egress block): targeted queries on the September 1 setting; motion-to-continue (**three separate targeted queries**); August 2026 docket/rulings before Judge Graf; the bullet-fragment ruling; the 08-18 reply memorandum; the 07-28 opening brief and any PDF mirror; `site:documentcloud.org` for project 224251; a Scribd-mirror query; postponed / rescheduled / sealed / unsealed; and general case activity dated 08-20 → 08-22. ⚠ **Direct fetch and DocumentCloud's API were UNATTEMPTABLE, not empty** — the egress block, not the sites. **Q-45 remains the only bindover-cycle document held nowhere.**

**A candidate chased down rather than assumed — and correctly EXCLUDED.** A Kirk-family / victim-representative motion urging the court to avoid further delay surfaced and read as new. The run pinned its date rather than reporting it: **published 2026-07-10**, predating the last logged run. **Excluded as not-new.** ⚠ It is queued only as a **possible holdings gap** — the project may not hold that filing — and **its contents are not characterised here.**

### 4. New transcripts — a SCOPED NULL

**None new.** Rev's index surfaced **Days 1–5 plus the contempt-related hearing — all seven already held.** The run searched rather than guessing slugs, per the two logged slug traps.

### 5. Route status + two discipline points the run raised itself

**No route changed state in either direction.** Every blocked route is logged as **unattemptable**, never as a null.

⚠ **A SOURCE-SIDE CONFLICT, recorded and NOT adopted.** Outlet **headlines** widely say the preliminary hearing *"concludes"* / *"ends"*; **the same outlets' body text** says it resumes in September. The run recorded the conflict and **declined to resolve it in the outlets' favour — the Tier 1 Day 5 transcript governs, and the hearing is NOT concluded.** This is the precise error the DOCKET-WATCH prompt's first calendar bullet exists to prevent, and it was met correctly.

⚠ **The bullet-fragment trap reproduced exactly.** Searches for the bullet-fragment ruling again returned the **2026-06-26 contempt ruling** — a different matter. **Not conflated.** ✅ One durable by-product: a **direct PDF URL for the underlying ballistics motion** was surfaced — `https://static.foxnews.com/foxnews.com/content/uploads/2026/04/tyler-robinson-ballistics-motion.pdf` (2026/04 folder). **Queued UNFETCHED** — the run had no egress to retrieve it, and it is recorded here as a lead, not as a holding.

### 6. Queued out of this firing

1. 👤 **Attach the repository to the routine.** `No sources configured` has now produced four unread reports. This is the root cause, not the paste-back step.
2. **Fetch the ballistics-motion PDF** (2026/04 Fox mirror) from a local session with egress — a lead, currently unheld.
3. **Confirm whether the 2026-07-10 Kirk-family / victim-representative motion is held**; if not, it is a holdings gap, not a new filing.
4. **Q-45 unchanged** — the State's 07-28 opening brief remains held nowhere.
5. ⚠ **Next scheduled firing: Wed 2026-08-26 09:00 EDT** (`next_run_at 2026-08-26T13:00:41Z`, routine **enabled**). It will run against a repository it still cannot write to.

**No register entry was assigned, resolved or moved. No case-posture statement in any topic file was altered. No filing's contents are characterised beyond title and date.** ⚠ **As of 2026-08-24, Tyler Robinson has NOT been bound over for trial, and the preliminary hearing is not concluded** — 2026-09-01 is its last day, argument only on a closed evidentiary record. Presumption of innocence applies throughout.

---

## 2026-08-26 scheduled firing — TRANSCRIBED (cloud run)

> ⚠ **TRANSCRIBED 2026-08-26 from the run-session log via the remote-trigger API** (`cse_017Fd6cNGgWdHveUY2xCaZ3W`, **24 turns, 257 s, result success**; fired `2026-08-26T13:04:21Z` = **09:04 EDT**). 🚨 **The FIFTH report delivered and never pasted** — caught the same day this time, ~3 hours after firing, during a session close.
>
> ⚠ **The delivered report file is NOT held here.** The run wrote a **~15,017-character** report to its sandbox scratchpad and delivered it via `SendUserFile` (uuid `bde1f037-3c2f-4f9a-ba3c-8bec2517bca2`) plus a push notification. Session did not persist. What follows is transcribed from the condensed run log and the run's closing summary — **a faithful record of what the run reported, not the report verbatim.**

### 1. EGRESS + ESCALATION

**EGRESS: BLOCKED — the 21st straight blocked cloud run.** Control fetch `curl: (56) CONNECT tunnel failed, response 403`; proxy status recorded `connect_rejected` / *"gateway answered 403 to CONNECT (policy denial)"*. ⚠ **`WebFetch` — a separate path — also returned `EGRESS_BLOCKED`**, so both direct-fetch routes are down. No routing around attempted. **Everything is search-index-only; no document retrieved or banked.**

**NO CHECKOUT** — `/home/user` empty; `No sources configured` again. **ESCALATION: NOT MET** on all five triggers.

### 2. 🚨 The material finding — a NEW DEFENCE FILING

**Reported filed 2026-08-22: a defence opposition to the electronic media coverage (EMC) orders for the 2026-09-01 hearing**, with a ruling on whether the EMC order applies that day reported **PENDING**. `T1 via T3 — document NOT held.`

⚠ **Read precisely, because two things it is not:** it does **not** move the 09-01 date, and it is **not** a motion to continue. **That named, expected risk was searched under two phrasings and returned NULL.** The filing's contents are not characterised here beyond title and date.

### 3. Calendar

**2026-09-01, 10:00 a.m. — argument-only final day, OBSERVED STANDING** (Utah County Attorney case page; most recent dated reporting 2026-08-25). July 6–10 remains **continued, not concluded** — ⚠ the run again logged that several headlines say *"concludes"* while their own body text says it resumes 09-01, and **did not adopt the headlines.**

🚨 **Q-45 — the State's 2026-07-28 opening brief — is still located nowhere, and is now 29 days open.** It remains the last outstanding bindover-cycle document.

### 4. Scoped nulls, and three route disciplines met

- **No new transcripts.** ⚠ **Rev's sitemap was UNATTEMPTABLE, not empty** — the run states nothing should be logged as "Rev published nothing."
- **No new mirror of the 07-28 brief.** ⚠ **The Fox 2026/08 baseline was NOT refreshed and stands at 71** — correct: never refresh through a degraded route.
- ⚠ **DocumentCloud was not attempted, so its silence is explicitly NOT a null.**
- **Bullet-fragment ruling still unobtained** — the search again surfaced the 2026-06-26 contempt ruling; **not conflated.**
- ✅ **Syndication counted correctly:** one result set was ~10 Sinclair stations running a single story, **counted as ONE source.**

### 5. Queued

1. 👤 **Attach the repository to the routine.** `No sources configured` has now produced **five** unread reports. Root cause, unchanged.
2. **Obtain the 2026-08-22 defence EMC opposition**, and watch for the pending ruling on whether the EMC order applies on 09-01.
3. **Q-45 unchanged** — 29 days open.
4. ⚠ **Next firing Sat 2026-08-29 09:00 EDT** (`next_run_at 2026-08-29T13:00:41Z`) — **the last scheduled firing before the 09-01 hearing.**

**No register entry assigned, resolved or moved. No case-posture statement altered. No filing's contents characterised beyond title and date.** ⚠ **Robinson has NOT been bound over, and the preliminary hearing is not concluded** — 09-01 is its last day, argument only on a closed evidentiary record. Presumption of innocence applies throughout.

---

## 2026-08-29 scheduled firing — TRANSCRIBED (cloud run) · THE LAST SCHEDULED COVER BEFORE 09-01

> Session `cse_01WkDERotRAkUdZFg1mBvhkB`, 23 turns, 260 s, status SUCCEEDED, fired **2026-08-29 09:01:47 EDT** (`13:01:47Z`), finished `13:06:15Z`. **Transcribed the same day, ~5h45m after firing**, from the condensed run log and the run's closing summary via the remote-trigger API.
>
> ⚠ **The delivered report file itself is NOT held here** — attachment uuid `cad3fabd-22ad-4fbc-85fe-3dc15cb8e155`, `CR-WATCH-run-2026-08-29.md`, ~13,571 chars, written to the run's own scratchpad and delivered by `SendUserFile` + push. This section is a transcription of the log, stated as such per the v1.5 precedent, **not a copy of the report.**
>
> 🚨 **`No sources configured` again — the SIXTH consecutive report that could not reach this repository.** Root cause unchanged since 2026-08-14: the routine has no checkout, so it cannot write here and never could.

### 0. Why this firing mattered more than the others

**`next_run_at` is `2026-09-02T13:00:41Z` — the Wednesday *after* the hearing.** This was therefore **the last scheduled cover before the 2026-09-01 preliminary-hearing final day**, exactly as the 08-26 entry warned. Had it not been transcribed, the pre-hearing window would have closed with six unread reports and no observation on the record.

⚠ **Found the same way as the previous five** — not by anything in this repository, but by a vault session reading the routine's `last_fired_at` against this file's mtime. The supervising check (`check-scheduled.sh`) reported this row **`ok` (3d of 4d)** throughout, because mtime moves on a *human* write. **It measures paste-back latency, not firing liveness.**

### 1. EGRESS STATUS + ESCALATION

**Egress: BLOCKED. Unchanged since 2026-08-05.** Both routes control-tested at the top of the run, as the spec requires:

| Route | Result |
|---|---|
| `curl https://example.com/` | `curl: (56) CONNECT tunnel failed, response 403` → `HTTP 000` |
| `WebFetch https://example.com/` | `EGRESS_BLOCKED` — *"Access to example.com is blocked by the network egress proxy."* |

**Every observation this run is search-index-only.** No document was acquired and **none was acquirable**. No attempt was made to route around the proxy.

**ESCALATION: NOT MET.** All five triggers negative — no bindover ruling; 09-01 has not moved; **nothing observed sealed or unsealed**; no route changed state in either direction; egress unchanged.

### 2. 🚨 The material finding — the 08-22 defence filing is now TWO filings, and one of them is a motion to SEAL

The 08-26 firing recorded *one* new defence filing dated **2026-08-22**. This run resolves it further:

- **Two defence filings dated 2026-08-22** — oppositions to electronic-media-coverage (EMC) requests **by the Salt Lake Tribune and by KUTV** for the 09-01 hearing.
- **Plus motions to classify the unredacted EMC-request material private/sealed.**
- **The sealing motion appears PENDING, with no ruling located.**

`T1 via T3`. **Documents not held. Contents not characterised beyond title and date.**

⚖️ **Why this was logged as a watch item and NOT an escalation, and the run made the call itself:** the trigger is *"a filing has been sealed or unsealed."* **A pending motion to seal is not a sealing.** If it is granted, the trigger fires. Flagged by the run as the top item for the next pass.

### 3. Calendar — observed status

| Date | Observed status | Source + retrieval |
|---|---|---|
| **2026-09-01, 10:00** | **STANDS. Firm, three days out.** Two official-issuer sources | [Utah Courts press notice](https://legacy.utcourts.gov/utc/news/2026/08/28/public-attendance-for-tyler-robinson-preliminary-hearing/) (published 2026-08-28) · [Utah County Attorney media page](https://atty.utahcounty.gov/media/ckpr) — both retrieved 2026-08-29 via search index only |
| Defence motion to continue | **NOT FOUND** — searched specifically, the named risk, under targeted phrasings | scoped null, search-index only |

⚠️ **A CAUTION THE RUN RAISED AGAINST ITS OWN EVIDENCE, and it is the [[summarising-fetch-fabricates]] failure mode in a new place.** The search summariser **twice** rendered the Utah Courts notice as though the hearing were on **2026-08-28**. It is not — **08-28 is the notice's publication path-date.** Because egress was blocked the run **could not open the page**, so its reading that the notice concerns the 09-01 hearing rests on the URL date-path plus "final day" framing, **not on the page body.** ▶️ **Re-verify directly when egress returns.** Recorded because a date read out of a URL is not a date read out of a document.

### 4. Scoped nulls and route discipline

| Route | State | Weight |
|---|---|---|
| Fox outlet mirror (Wayback CDX) | **unattemptable** — egress blocked | none; **baseline NOT refreshed, stands at 71 PDFs from 2026-08-20** |
| DocumentCloud | **unattemptable** | none — silence explicitly not logged as a null |
| Scribd (Q-45) | **unattemptable** | none |
| Direct fetch, any host | **unattemptable** | none |
| Rev transcripts | searched; no new case transcripts surfaced | search-index only |

✅ **Three disciplines met without prompting:** the four blocked acquisition routes were kept as **unattemptable, not null**; the **Fox baseline was not refreshed through a degraded route**; and no route was recorded as changed state.

🚨 **Q-45 — the State's 2026-07-28 opening brief — remains held nowhere. It is now 32 days open** and is still the only bindover-cycle document the library does not hold.

### 5. ⚠ One loose end this transcription records rather than resolves

The run's searches surfaced outlet headlines referring to a **judge's decision on the defence's push for closed/secret hearings** and to the defence **"losing"** a camera fight — while the run's own finding is that the **sealing motion is pending with no ruling located.** These are not obviously consistent.

**Not reconciled here, and deliberately not adopted.** Media headline characterisations are not observed status, the run did not establish a ruling, and inferring one from a headline is precisely what this spec prohibits. ▶️ **Queued as the first thing to check on the next pass** — if an EMC or sealing ruling has in fact issued, that is a live escalation trigger and it would be sitting unrecorded three days before the hearing.

### 5b. ⚠ LOCAL ADDENDUM, same day — the §5 loose end is RESOLVED, and it resolves to a date trap

**Run by a local (egress-capable) session on 2026-08-29 ~15:05 EDT, immediately after transcribing.** The cloud run could not do this: it was egress-blocked and could only see headline text.

🚩 **The headlines are OLD, and the conflation was the whole of the apparent conflict.**

| Article | Date, read from the page itself | Bearing |
|---|---|---|
| Fox, *"Tyler Robinson asks for more secret hearings after losing fight over cameras in court"* | **`datePublished` 2026-05-18T06:00:37-04:00** — read from the page's own JSON-LD and `<time datetime=...>`, HTTP 200, 464,181 bytes | **Three months old. NOT a ruling on the 2026-08-22 motions.** |
| Prior sealing / camera denials (Fox, stgeorgeutah, LA Mag, Deseret, Post Millennial) | surfaced as **March and June 2026** items | earlier matters in the same dispute; **not new** |

✅ **Therefore: NO ruling on the 2026-08-22 EMC-opposition or sealing motions has been located, and the cloud run's "pending, no ruling located" stands.** The apparent inconsistency was an artifact of undated headlines, not a contradiction in the record. ⚖️ **The run's decision not to escalate was correct** — and it would still have been correct had the headlines been recent, because a pending motion to seal is not a sealing.

⚠️ **Route note: `abc4.com` returned HTTP 403 to a direct fetch** (6,520-byte block page), consistent with the bot-block first logged at Run 1. **Not a null — unattemptable.** The Fox host was open.

⚠️ **Scope, stated:** search-index plus two direct fetches. **No docket was consulted.** A ruling issued in the last day or two might not yet be reported, so this is **not evidence of absence** — it is evidence that no *reported* ruling exists on the routes tried.

### 6. Queued out of this firing

1. ✅ **CLOSED SAME DAY by the local addendum (§5b) — no ruling located; the conflicting headlines date-pinned to 2026-05-18 and earlier.** ⚠ Re-check on the next pass anyway: the window between this check and 09-01 is exactly where a ruling would land.
2. 👤 **Attach the repository to the routine.** `No sources configured` has now produced **six** unread reports. Root cause, unchanged since 2026-08-14.
3. ⚠ **Re-verify the Utah Courts 08-28 notice against its page body** when egress returns — §3 caution.
4. **Q-45 unchanged — 32 days open.**
5. ⚠ **There is NO further scheduled firing before the hearing.** `next_run_at` = **2026-09-02**, the day after. **Any pre-hearing cover must be a local by-hand run** — the same gap-class that lost the 08-18 window (Run 7).

**No register entry assigned, resolved or moved. No case-posture statement altered. No filing's contents characterised beyond title and date.** ⚠ **Robinson has NOT been bound over, and the preliminary hearing is not concluded** — 09-01 is its last day, argument only on a closed evidentiary record. Presumption of innocence applies throughout.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **2.0** | **2026-08-29** | **The last scheduled firing before the 09-01 hearing is transcribed the same day it fired — and the transcription is the only reason it exists on the record.** (`cse_01WkDERotRAkUdZFg1mBvhkB`, 23 turns, 260 s.) 🚨 **`next_run_at` is 2026-09-02 — AFTER the hearing.** There is **no further scheduled cover**; any pre-hearing pass must be local, the same gap-class that lost the 08-18 window. 🚨 **Sixth consecutive undelivered report; `No sources configured` unchanged.** ✅ **09-01 10:00 observed STANDING at T-3 on two official-issuer sources**, and the named continuance risk searched specifically and **null**. 🚨 **The 08-22 defence filing is now resolved as TWO filings — EMC oppositions (Salt Lake Tribune, KUTV) plus motions to seal the unredacted EMC-request material, sealing motion PENDING with no ruling located.** ⚖️ **Escalation correctly NOT raised: a pending motion to seal is not a sealing** — but it is flagged as the next pass's first item, because if it has been granted the trigger is live and unrecorded three days out. ⚠️ **EGRESS BLOCKED on both routes, control-tested, unchanged since 2026-08-05**; all four document routes **unattemptable, not null**; **Fox baseline not refreshed** (71). 🚨 **Q-45 is 32 days open.** ⚠️ **A summariser hazard logged against the run's own evidence:** the Utah Courts notice was twice rendered as though the hearing were 2026-08-28 — that is the **publication path-date**, and with egress blocked the page body could not be read, so the calendar reading rests on a URL path plus framing. **Re-verify when egress returns.** 🚩 **One loose end recorded rather than resolved:** outlet headlines referencing a decision on the defence's push for closed hearings sit oddly against a sealing motion found **pending**; **not reconciled, not adopted, queued first.** No register entry assigned or moved; no case-posture statement altered; no filing's contents characterised. ⚠ Robinson has NOT been bound over and the preliminary hearing is not concluded. |
| **1.9** | **2026-08-26** | **The 2026-08-26 firing is transcribed the same day it fired — the first time the paste-back gap has been closed in hours rather than days.** (`cse_017Fd6cNGgWdHveUY2xCaZ3W`, 24 turns, 257 s.) 🚨 **First material finding since Run 7: a NEW DEFENCE FILING reported filed 2026-08-22 — opposition to the electronic media coverage orders for the 2026-09-01 hearing, with a ruling on EMC applicability reported PENDING.** `T1 via T3`; document not held; contents not characterised. ⚠ **It does NOT move 09-01 and is NOT a motion to continue** — that named risk was searched under two phrasings and returned null. ⚠ **EGRESS BLOCKED for the 21st consecutive cloud run**, and `WebFetch` — a separate path — is blocked too, so both direct-fetch routes are down. **09-01 10:00 argument-only observed standing.** 🚨 **Q-45 is 29 days open and remains the last outstanding cycle document.** ✅ **Three route disciplines met without prompting:** Rev's sitemap logged **unattemptable, not empty**; the Fox 2026/08 baseline **not refreshed** through a degraded route (stands at 71); DocumentCloud **not attempted, so its silence is explicitly not a null**. ✅ **Syndication counted correctly** — ~10 Sinclair stations running one story counted as ONE source. ✅ The *"hearing concludes"* headline/body conflict logged again and **not adopted**. 🚨 **Root cause unchanged and now five reports deep: `No sources configured` — the routine still has no checkout.** ⚠ **Next firing Sat 2026-08-29 09:00 EDT is the LAST scheduled firing before the 09-01 hearing.** No register entry assigned or moved; no case-posture statement altered; Robinson has NOT been bound over. |
| **1.8** | **2026-08-24** | **The 2026-08-22 scheduled firing is transcribed — recovered, not delivered, and that is now a four-time pattern.** The firing RAN (`cse_0195NQbHgY7PS24U8JCmB71S`, 29 turns, 264 s, success, fired 09:00:58 EDT) and reported a **SCOPED NULL with NO escalation met on any of the five triggers**: **2026-09-01 10:00 observed STANDING**, **no defence motion to continue** (three targeted queries), no new filings, no new transcripts (Rev 7/7 already held), **Q-45 — the State's 07-28 opening brief — still held nowhere.** ⚠ **Egress BLOCKED, unchanged since 2026-08-05** (control fetch `CONNECT 403`, proxy logged `connect_rejected`; WebFetch also unavailable), so every observation is **search-index-only** and DocumentCloud/direct fetch are **unattemptable, not empty**. 🚨 **Found from outside this repository on 2026-08-24** by comparing this file's mtime (08-21 09:00) against the routine's `last_fired_at` (08-22 13:00:58Z) — **the fourth report delivered and never pasted.** 🚨 **Root cause named and unchanged: `No sources configured` — the routine has no checkout**, so it cannot write here and never could; the paste-back step is the symptom. 🚨 **A NEW GAP RECORDED, in the watch's own supervisor: the vault's `check-scheduled.sh` cannot detect this.** It measures this file's mtime against a 4-day max age, but the mtime moves only on a human/local write — so an unread cloud report reports **`ok`** and would not have flagged until 08-25. **The check measures paste-back latency, not firing liveness.** Not fixed here. ⚠ **The delivered report file (uuid `a9f62b90-…`, 15,854 chars) is NOT held**; the transcription is from the condensed run log and the run's closing summary, stated as such per the v1.5 precedent. ⚠ **The run self-titled "Run 8"; the index gives it a `—` row on this file's convention and records the discrepancy rather than renumbering** — the next LOCAL run takes 8. ✅ **Two disciplines the run met unprompted and which are logged as met:** outlet headlines saying the preliminary hearing *"concluded"* were recorded as a **source-side conflict and expressly NOT adopted** (the Tier 1 Day 5 transcript governs), and the bullet-fragment search trap reproduced exactly and was **not conflated** with the 2026-06-26 contempt ruling. ✅ **One candidate chased rather than assumed:** a Kirk-family/victim-representative motion was **date-pinned to 2026-07-10 and excluded as not-new**, queued only as a possible holdings gap, contents uncharacterised. ✅ **One durable lead banked as a lead:** a direct ballistics-motion PDF URL on the Fox 2026/04 mirror, **queued UNFETCHED** (the run had no egress). **No register entry assigned, resolved or moved; no case-posture statement altered; no filing's contents characterised.** ⚠ Robinson has NOT been bound over, and the preliminary hearing is not concluded. |
| **1.7** | **2026-08-20** | **Run 7 logged (local catch-up), the 2026-08-19 scheduled firing transcribed, and the run index gains a row type it never wanted: a planned run that did not happen.** 🚨 **The Tue 08-18 by-hand run — the only document-capable cover for the State's reply — DID NOT RUN**; the miss was found 2026-08-20 from outside the repo by this file's mtime, and is recorded as its own index row rather than papered over (no row backfilled — the absence is the record). ⚠️ **The miss class is named: a planned one-off has no scheduled-firing anchor, so the "watch stopped" trigger could not see it; the external mtime watch caught it at T+2 — after the filing date it existed to cover. Cover-by-luck, Run 3's lesson repeated.** ✅ **AND THE LUCK HELD: Run 7's diff caught the filing — the State's *"Reply Memorandum in Support of Preliminary Hearing Bindover"* (filed 2026-08-18 per its own certificate of service) is ACQUIRED AND BANKED** ([CR-ACQ-2026-08-20](CR-ACQ-2026-08-20_states-reply.md)): two mirror URLs, one byte-identical document; 19 pp. vs the 18-page limit recorded and not reconciled; provenance two-of-three, the defence brief's grade exactly; **contents unread — pages 1/18/19 only, caption and attestation.** 🚨 **Escalation: route RECOVERY (Fox/CDX), Q-147's trigger, second application — and the route's intermittency is now measured (blocked and open twice within ten minutes), rule: retry before recording a block, never baseline through one.** ✅ DocumentCloud 40/40, Rev 7/7, Utah Courts 2/2 — attempted nulls. ✅ **Q-45 July-folder enumeration: attempted null (56 PDFs); the opening brief remains the only cycle document unheld.** ✅ The 08-19 firing (egress-blind day 15, no checkout) reported the reply filed T1-via-T3 with the same 19-vs-18 flag — independently corroborated by the banked document. Baseline refreshed to 71 PDFs after triage. 👤 **Queued: prompt re-sync before Sat 08-22 09:00 — stale twice over (false-premise "not filed" + missing recovery trigger).** No register entry assigned or moved; no case-posture statement altered; no filing's contents characterised. |
| **1.6** | **2026-08-17** | **Runs 5 and 6 logged.** 🚨 **Run 6 escalates on a DEGRADATION trigger the day before the State's reply: the Fox outlet-mirror route is BLOCKED (Wayback CDX, HTTP 504) — the very route Run 4 baselined so that Tuesday would be a diff.** ⚠️ **The failure is located at the third-party INDEX rather than at the mirror, which is worth stating precisely because the two have different consequences — but the operative rule does not depend on which it is: blocked is not empty, it carries no evidential weight in either direction, and it was deliberately NOT baselined** (refreshing while a route is down banks a hole as a state). ✅ **DocumentCloud OPEN — the fourth observation of that route and the first on a second consecutive day, so 'intermittent' is now measured across four observations spanning two days rather than three within one.** ✅ **Rev 7/7 and Utah Courts 2/2 are ATTEMPTED nulls and carry weight.** **No early filing; none was expected.** ✅ **Q-147 closed on the spec side earlier the same day and Run 6 is the first application of its route-RECOVERY trigger** — DocumentCloud's availability is now reported as a capability rather than left to be inferred from a diff. 👤 **The matching routine-prompt change is drafted and NOT applied; it should land before the Wed 08-19 firing.** **Run 5 (2026-08-16, late evening) is logged here for the first time as a numbered run and added to the run index** — it had a section in this file but no index row, so the index under-counted the runs it records. ⚠️ **The Tue 08-18 by-hand run remains the only document-capable cover.** No register entry assigned or moved; no case-posture statement altered. |
| **1.6** | **2026-08-16** | **Run 5 logged — a LOCAL RUNNER-VERIFICATION PASS, and it is recorded as a PARTIAL execution of the spec rather than a run.** `./docket-watch-run.py` covers the four mechanical routes only; **the spec's search-dependent legs were NOT run**, so this file makes no statement about scheduling changes or a defence motion to continue, and says so rather than leaving the scope to inference. **Purpose: de-risk the 2026-08-18 window by proving the instrument works before the day that matters.** ✅ **All four routes attemptable, zero drift against baseline** (DocumentCloud 40/40 · Fox 55/55 PDFs · Rev 7/7 · Utah Courts 2/2), so all four nulls are **attempted** nulls and carry evidential weight. ✅ **RUN 4'S ESCALATION IS RESOLVED, NOT RE-RAISED: the DocumentCloud API is open again** — **403 at 09:00, open at 14:05, open at 22:47 the same day**, nothing changed at this end. **"INTERMITTENT" is now measured across three observations rather than inferred from two**, and the operative rule is reinforced: never log this route's silence as a null. ⚠ **Baseline deliberately NOT refreshed** — nothing new was found, and refreshing an unmoved baseline only risks writing a transient into it. 🚨 **A GAP IN THE SPEC ITSELF, found by this run: the escalation trigger list is ASYMMETRIC — it fires on a route that *starts failing* and has NO trigger for a route that has RECOVERED.** Recovery changes what the next run can do (here it restores the cheap post-08-18 DocumentCloud sweep), so a watch that only escalates degradation silently under-reports its own capability; this run had to notice by reading a diff → **Q-147**. **The 08-18 by-hand run still stands as the only document-capable cover.** No register entry assigned, resolved or moved; no case-posture statement altered; no filing's contents characterised. |
| **1.5** | **2026-08-16** | **THE 2026-08-15 SCHEDULED FIRING'S REPORT IS PASTED INTO THIS FILE — the first time this routine's output has ever reached the repository instead of an unread channel.** Transcribed from the run-session log via the remote-trigger API (`cse_01SmvswMBC5ozv2PFA8fTWtX`, 16 turns, 165 s, success); ⚠ **the delivered report file itself (attachment uuid `5c052481-…`) is still NOT held here**, and the section says so rather than implying a document was banked. **That run: null result, escalation correctly NOT met** (egress *unchanged*, and the trigger is *change*), **egress blocked on both routes at day 10, control-confirmed**, no checkout, `No sources configured`. ⚠ **Its DocumentCloud / Scribd / outlet-mirror nulls are recorded as UNATTEMPTABLE, carrying no evidential weight** — the run made that distinction itself. It escalated to a human that **the 08-18 window needs a local run**. **Run 4 logged (local, 2026-08-16), run precisely because of that.** 🚨 **ESCALATION MET — route trigger: the DocumentCloud API is now Cloudflare-gated from LOCAL sessions** (HTTP 403 + "Attention Required!" interstitial on three endpoints, tested under two user agents), **a regression against Run 2's "no longer bot-gated" and against the 08-13 attempt's 46/46 enumeration; the cheap post-08-18 DocumentCloud sweep is therefore UNAVAILABLE, not empty.** Local egress itself verified fine (`example.com` HTTP 200), so this is site-side — the mirror image of the cloud runner's environmental block. ✅ **First transcript null with real evidential weight: Rev enumerated from its OWN SITEMAP** (not slug guesses, not search snippets) — six case transcripts exist, **all six already held**; the seventh `robinson` hit is an unrelated commencement speech. ⚠ **Rev's `/transcripts/search?q=` path is a 404 and is not a search endpoint — the sitemap is the enumeration route that works.** ✅ **The Fox outlet-mirror route — the one that landed the defence brief — is OPEN and now BASELINED for Tuesday's diff**: 55 PDFs under `uploads/2026/08/`, exactly one case item, `robinson-prelim-filing.pdf`, **fetched live at 389,135 bytes / SHA-256 `c3f39437…` — byte-identical to the banked defence brief, verified by hashing both files rather than by trusting this log.** **Recorded as an INTEGRITY confirmation (the banked copy is faithful to source five days on) and expressly NOT as a provenance gain — identical bytes are the same rendering, so the clerk file-stamp gap (Q-63) is untouched.** ⚠ **Name trap logged: `bijan-robinson-…jpg` also matches a surname search of that directory — match on the case, not the surname.** **Q-45 remains OPEN and the State's 07-28 brief remains unheld**: archive.today **429 again** on two hosts (third consecutive; ⚠ a rate-limit is NOT an absence), Wayback CDX a **true empty null** (zero captures), Fox mirror carries no State's brief, DocumentCloud unavailable, Scribd not re-attempted and stated as scope. **09-01 10:00 stands; no defence motion to continue found.** ✅ **The ambiguity the 08-15 run flagged and refused to guess at is RESOLVED independently: the mid-August aggregator wave is downstream coverage of the already-banked 08-11 defence brief, not a new filing** — and its characterisations of that brief are deliberately not recorded. ⚠ **One candidate escalation checked and CLEARED rather than left hanging:** a *"Judge unseals documents"* headline is dated **2026-03-13**, read from the article body — five months old, trigger not met. **Also corrected here: the routine's inlined prompt is NO LONGER the 2026-08-01 text** — the API shows it re-synced 2026-08-14T20:23 EDT and it now carries the egress control test, the `comtempt` slug trap and 08-14 route status. **No register entry assigned, resolved or moved; no case-posture statement altered; no filing's contents characterised; no evidence file created.** ⚠ Robinson has NOT been bound over. |
| **1.4** | **2026-08-14** | **The "fired or dead" question is RESOLVED — the routine FIRED ALL THREE TIMES (08-05, 08-08, 08-12) and its reports were delivered and never pasted.** Established by direct API retrieval of the routine's run sessions (IDs cited in the new liveness-resolution section); the routine is **enabled**, next firing Sat 2026-08-15 09:00 ET. **No run rows backfilled** — the v1.2 rule stands; the three firings' watch-relevant substance is recorded in the resolution section with each session ID as its citation, and none of it adds anything the library does not already hold at better tier through Run 3. 🚨 **New route finding: every cloud firing since 2026-08-05 ran BLIND** — the session egress proxy 403-blocked all direct HTTPS fetches including a control fetch of `example.com` (environmental, not site-side); web search was the only working channel, and **each run correctly declared the route-failure escalation into a delivery channel nobody was reading** (three mobile pushes, three file attachments, zero pastes). **Consequences recorded:** the 👤 GitHub App grant fixes paste-back only if **the repository is also added to the routine's config, which currently carries NO source at all** (`No sources configured` in every run's environment log); the grant does **not** fix the blindness, so the Sat 08-15 and Tue 08-18 windows have no document-capable scheduled cover — local by-hand runs remain the only acquisition-capable pass. Run-index rows for the three firings annotated in place; status text superseded to v1.4 with v1.3 retained. No register entry assigned or moved; no case-posture statement altered; no filing contents characterised. |
| **1.3** | **2026-08-13** | **A Q-45 ACQUISITION ATTEMPT WAS RUN AND FAILED — logged as a section, not as a run row, because it is not an execution of the DOCKET-WATCH spec.** 🚨 **The State's 2026-07-28 opening brief was NOT obtained. Nothing was banked, no SHA-256 exists because no bytes were retrieved, its contents remain unrecorded, and no CR-E08 evidence file was written** — writing one about a document this project cannot read would be the error the library exists to prevent. **Six routes are logged with their exact results, per the rule that failed retrievals are access-path caveats rather than things to drop silently.** ⚠ **The blocking failure: the Scribd mirror is real and was positively identified — document ID `1067587104`, embedded in The Post Millennial's article, uploader account `The Post Millennial`; Run 2 recorded that the mirror existed but never recorded its identifier, so the ID is this attempt's one durable gain.** Every one of **seven** Scribd endpoints (canonical, `/doc/`, `ru.`, everand, two download paths, oEmbed) returned **HTTP 200 with an identical 3,038-byte "Client Challenge" JavaScript interstitial** — ⚠ **a status code is not a retrieval.** **Q-45's "now actionable" (Run 2 §8) is QUALIFIED IN PLACE, not struck as wrong: "actionable" meant *located*, not *retrievable*.** ⚠ **A summarising fetch did get past the gate and returned page metadata (28 pp., uploader, download button) AND document text; the text is deliberately not recorded** — it arrived through the same channel class CR-E07 §1 logs as having fabricated a sentence, and **a paraphrasing intermediary is not a primary document; the library already had summaries, which is why Q-45 exists.** **Provenance therefore remains ZERO of three — not because the file-stamp, signature block and certificate of service are absent, but because nothing renders the document faithfully; the separate-act discipline that produced a real finding on the defence brief produces NO finding here, a weaker state that is stated rather than glossed.** **Scoped nulls: no Wayback capture of the Scribd document exists (CDX prefix enumeration, zero rows) while archive.today is NOT ESTABLISHED (HTTP 429, a rate-limit, not an absence); no outlet-mirrored PDF exists — the Fox 07-28 article re-fetched at 476,625 bytes still carries zero PDF/Scribd/DocumentCloud links 16 days after Run 1 found the same, and Wayback CDX over `static.foxnews.com/…/uploads/2026/07/` and `/08/` surfaces no Robinson PDF, while KUTV, KSL and Deseret carry no document links or iframes; the Utah County Attorney media page has no `.pdf` href anywhere and is now recorded as structurally unable to supply filings after failing this purpose three times; XChange (👤, Q-31) and a live browser (👤, Q-32(b)) were not attempted and are stated as scope, not as nulls.** ⚠ **Consequence: the Scribd gate now sits behind the SAME dependency as the DocumentCloud web UI, so Q-32(b) has a second and more important dependent — Q-45 itself.** **Collateral, all checkable: (1) project 224251 is now FULLY enumerated, 46 of 46 across three cursor pages (25 + 21 + 0), closing Run 2's unaccounted 46th; (2) the defence brief reached DocumentCloud on 2026-08-12 (doc 28551955, Epoch Times / Savannah Pointer) but DocumentCloud's `file_hash` for it equals the SHA-1 of the copy this project already banked — the SAME FILE, so no independent provenance and no progress on a court-stamped copy; (3) ⚠ a HASH TRAP is logged — the PDF DocumentCloud SERVES (383,293 bytes, SHA-256 `5c2c426b…`) is a re-render and matches neither the banked original (389,135 bytes, SHA-256 `c3f39437…`) nor DocumentCloud's own `file_hash`, though its extracted text is identical to the banked extraction at 91,729 characters; future comparisons must use the API's `file_hash` field, never the served file.** **Requirements to close Q-45 are stated as requirements: an owner-driven browser session, or XChange for a stamped copy — with the instruction to STOP if Scribd demands an account.** **Cheap retries queued: archive.today, a post-08-18 DocumentCloud sweep, and the State's reply due Tue 2026-08-18, whose outlet mirror may be the next real chance at the State's own words. CR-E07's F-15 stands unchanged — the State's theory is still visible only through its opponent's description. No register entry was assigned, resolved or moved; no case-posture statement was altered; Robinson has not been bound over.** |
| **1.2** | **2026-08-13** | **Run 3 logged — a CATCH-UP RUN, and the run's headline finding is about the watch, not the case.** 🚨 **The watch went dark for 12 days:** three scheduled firings (Wed 08-05, Sat 08-08, Wed 08-12) produced no rows, and **the 2026-08-11 defence deadline — which Run 1 itself named as "the next checkpoint" and the likeliest vehicle for a continuance motion against a named on-the-record risk — passed inside that gap, unchecked.** The gap was found **from outside this repository** during an unrelated session reconstruction, by this file's 12-day-old mtime; the watch did not catch itself. ⚠ **No rows were backfilled** for the three missed firings — a fabricated row is worse than a missing one — and **whether the routine fired-and-was-never-pasted or is dead is expressly NOT ESTABLISHED**, since a report-only routine refused the private repo cannot be distinguished from a dead one from inside it. **On the case: the defence brief is FILED AND BANKED** — *"Defendant Tyler James Robinson's Preliminary Hearing Briefing,"* Case No. 251403576, Hon. Tony F. Graf, Jr., **signed and served Tue 2026-08-11** (day-of-week verified by direct reading, not extraction, per Run 2's logged hazard), 41 PDF pp. / 35 printed, SHA-256 recorded, `.txt` extraction alongside. **This is the first primary filing the project holds as a document rather than through reporting.** ⚠ **Provenance is two-of-three: signature block and certificate of service present, NO clerk file-stamp line visible** — better than the State's unverified Scribd mirror, still short of a stamped filing, and **not silently promoted.** ⚠ **35 is both the printed length and the court's page limit here; the coincidence is recorded and explicitly not read as a finding.** **The 09-01 argument STANDS**, upgraded from reporting to a **Tier 2 named-official** item dated 2026-08-11 (Utah County Attorney media page, a route whose latest Robinson item was 2026-06-26 at Run 1). **No continuance motion found — with scope stated**: open routes only, no docket consulted, and a motion filed in the last 48 hours would likely not yet be reported, so this is not evidence of absence. **The brief's contents are deliberately unrecorded** per the spec, and **a second restraint is logged**: the extraction incidentally surfaced material on the sexuality and gender identity of the defendant and of a private individual, none of which is recorded, that determination belonging to a reasoned evidence-file pass under the two-layer discipline rather than to a watch row. **No escalation trigger met — and the run flags that the trigger list contains no trigger for "the watch itself has stopped," which is precisely why 12 days passed unnoticed.** Queued: 👤 confirm the routine is alive before Sat 08-15, 👤 grant the GitHub App access, add a watch-failure escalation trigger, locate a stamped copy. **No register entry assigned or moved; no case-posture statement altered.** |
| **1.1** | **2026-08-01** | **Run 2 logged.** **No escalation trigger met** — no bindover, 09-01 standing, nothing sealed or unsealed, and the only route change is a route **re-opening**. ⚠ **A public mirror of the State's opening brief now exists and is retrievable** — a 28-page "Memorandum in Support of Preliminary Hearing Bindover" on Scribd — **closing Run 1's "no public mirror found" null and giving Q-45 an acquisition route.** The document was **not banked and its contents are not recorded**; provenance verification is named as a separate act from reading it. ⚠ **28 pp. is the actual length; 35 was the court's page LIMIT — the two were being conflated, though DOCKET-WATCH already stated it correctly, so no library file required correction.** The **2026-07-28 filing date is now multi-sourced** across six outlets where Run 1 had one; **source independence for the filing event is upgraded, the document remains unheld, and it stays T1 via T3.** ⚠ **The DocumentCloud API is no longer bot-gated: project 224251 was positively enumerated for the first time (46 documents; 45 listed, one unaccounted for and not claimed otherwise), while the web UI remains JS-gated — so Q-32 should be SPLIT, not closed.** A **new unheld artifact** was located: a 4-page "Supplemental Notice Concerning Access to Evidence Presented in Open Court," **filed 2026-07-09, during hearing week** — adjacency to the Exhibit 12.1 question resting on **title only**. Second source obtained for **Q-47**. ⚠ **Two hazards recurred and are logged: machine extraction gave wrong dates on four counts (three extractions called 2026-07-29 a Tuesday; it is a Wednesday), and searches for the bullet-fragment ruling repeatedly surface the 2026-06-26 contempt ruling instead — which also puts TWO dates in play for Q-46.** **A three-day blind spot at the run's leading edge is stated.** Outlets' characterisations and direct quotations of the brief were surfaced repeatedly by the search layer and **deliberately not recorded**, per the spec. **No register entry assigned or moved; no case-posture statement altered.** |
| 1.0 | 2026-07-28 | File created; **Run 1 logged.** The first execution of the DOCKET-WATCH spec, which until now had no runner attached. **The State's opening probable-cause brief is reported filed on 2026-07-28** — T1 via T3, one independent source, no primary document obtained, and the date confirmed by day-of-week check against D-51 rather than by machine extraction (two automated passes returned wrong dates and are logged as a caveat). **The brief's contents are deliberately not recorded**, per DOCKET-WATCH's prohibition and because Q-04's decisive artifact is the document itself. **The 09-01 argument stands**; no continuance motion found, with the Nester conflict still open and the 08-11 defence reply named as the next checkpoint. **A previously unknown proceeding was located** — a contempt hearing c. 2026-06-22, absent from the library's five-day transcript inventory. **The `legacy.utcourts.gov` press-notice route was retrieved for the first time** and holds nothing after 2026-07-06; **abc4.com is newly bot-blocked**. Three items queued (**Q-45, Q-46, Q-47**). No escalation trigger met; no case-posture statement altered; no register entry assigned or moved. |
