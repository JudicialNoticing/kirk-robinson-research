# CR-ACQ-2026-08-14 — Acquisition: the Rev "Contempt Hearing" transcript (Q-46)

**File ID:** CR-ACQ-2026-08-14 · **Scope:** acquisition and facial (recording-layer) verification of one Rev transcript; resolution of Q-46's two-dates question · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-14 · **Status:** v1.0

**Sourcing framework (project standard):** Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries a URL and a retrieval date.

**§1 Access-path caveat, first:** this is a **Rev machine-generated transcript** retrieved from the public page — the same dependency class as the five hearing-day transcripts, with the same hazards: garbles are possible (`[inaudible 00:14:45]` appears in the opening line), speaker attribution is Rev's, and one speaker is unattributed ("Speaker 1"). The page was retrieved by direct local fetch (HTTP 200, 206,156 bytes) on **2026-08-14** — the route is open locally; note the *cloud* watch runner has been egress-blocked from rev.com since 08-05 (CR-WATCH-log v1.4).

---

## 1. Outcome, stated first

**Q-46 is ANSWERED on the face of a now-held T1 record: the c. 2026-06-22 proceeding and the 2026-06-26 contempt ruling are DIFFERENT EVENTS in the same matter.** The transcript is of a **status hearing** at which the court **postponed its anticipated ruling** on the defence's motion for order to show cause and **set Friday 2026-06-26, 8:30 a.m., for delivery of the decision.** The 06-26 event reported by outlets (e.g. CNN's contempt-ruling article dated 2026-06-26, already in the library's search trail) is the delivery the transcript schedules. Run 2's "two dates in play" hazard is resolved: both dates are real, and they are hearing-then-ruling, not duplicates.

## 2. What was acquired

| | |
|---|---|
| **Page** | "Tyler Robinson Charlie Kirk Contempt Bullet" — slug `tyler-robinson-comtempt-hearing` *[sic — Rev's own misspelling; the second slug trap, logged since Run 1]* |
| **URL** | `https://www.rev.com/transcripts/tyler-robinson-comtempt-hearing` · retrieved **2026-08-14**, HTTP 200 |
| **Page date** | `datePublished` **2026-06-23** (from the page's own metadata) |
| **Banked** | `CR-ACQ-2026-07-27_court-record-artifacts/2026-06-23-pub_rev-contempt-hearing-transcript.html` (raw, 206,156 b, SHA-256 `b1ba235f3f85de6dab32e78a0a026c14d8ff92f016b05ee62041abd3699418b9`) + `….txt` (extraction, 36 speaker-paired entries, 36,842 b, SHA-256 `4e4bcd4f905a23dd6b50bb442fe668a2859253b9115076a77dfb4b15a3a63b45`) |
| **Extraction method** | Speaker-stamp paragraphs (`Name (MM:SS):`) paired with their following body paragraphs; Rev splits them across elements, so naive timestamp searches on the raw HTML return zero — logged so the next extraction does not re-derive this |

## 3. What the transcript facially shows (recording layer only)

- **The court calls case 251403576** and takes appearances: for the State, **Chad Grunander, Ryan McBride, Jeff Gray, Chris Ballard**; for the defence, **Kathryn Nester** and **Michael Burt** (Rev attribution). Mr. Robinson participates by listening without video, at the defence's request. The hearing runs ~14:44–55:28 in transcript time and ends in recess.
- **The contempt matter appears as "Defense's motion for order to show cause."** The court states the parties submitted additional briefing on **June 17th and June 18th**, the most recent received "at approximately 9:21 on June 18th," and that because submissions arrived "shortly before the anticipated ruling," it "requires additional time to complete its thorough review."
- **The ruling is set for June 26th at 8:30 a.m.** ("we'll plan on June 26th at 8:30 in the morning"), with the judge apologising "for today" — i.e., a ruling had been anticipated at this hearing and was continued.
- The court also delivers prepared remarks on **preliminary-hearing legal standards** (magistrate's limited role; *State v. Lopez* on quashing subpoenas compelling an alleged victim's testimony) and gives notice that the then-upcoming public preliminary hearing would allow **no electronic devices** in the courtroom.

## 4. Dating the proceeding — basis stated exactly

The transcript **nowhere states its own hearing date on its face.** The bounds it does state: after 2026-06-18 (briefing received that morning) and before 2026-06-26 (the setting). The page's `datePublished` is 2026-06-23; applying the library's established one-business-day publication lag (D-51 discipline) puts the proceeding at **c. Monday 2026-06-22** — consistent with Run 1's estimate. **"c. 06-22" therefore remains an inference from publication lag inside a documented 06-18→06-26 window, not a read date; graded accordingly.**

## 5. Hazards and residue

- ⚠ **Title vs. content:** Rev titles the page "Contempt Hearing"/"Contempt Bullet," but the in-transcript vehicle is the defence's **order-to-show-cause motion**, and **no contempt finding, sanction ruling, or "under advisement" language appears in the transcript text** — this is the scheduling/continuance hearing, not the ruling. Anyone citing "the contempt hearing transcript" for the *ruling's* content is citing the wrong artifact.
- **Residue (open):** when the OSC/contempt matter was *argued* is not established by this artifact — the judge's "does the defense need the benefit of the record as it relates to that issue" implies prior proceedings this library does not hold. The **06-26 ruling itself** is likewise not held (it is known T1-via-T3 through the 06-26 reporting); if a transcript or order of the 06-26 delivery exists, it is a natural next acquisition.
- The five hearing-day transcripts remain the library's only other Rev holdings; this file adds the sixth.

**No case-posture statement in any topic file is altered by this acquisition. No D-register entry is assigned, resolved or moved; Q-46 (a queue item) is marked done with a pointer here.** As of 2026-08-14, Tyler Robinson has NOT been bound over for trial. Presumption of innocence applies throughout.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-14 | File created. Rev "Comtempt Hearing" page acquired and banked (raw + extraction, SHA-256s recorded); Q-46's two-dates question answered on the record's face: the c. 06-22 proceeding is a status hearing that continued the anticipated OSC ruling and set 2026-06-26 08:30 for its delivery — hearing and ruling are distinct events. Dating basis stated as an inference (06-18→06-26 window + publication lag). Residues: the 06-26 ruling itself is not held; when the matter was argued is unestablished. |
