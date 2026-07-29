# CR-AUDIT-2026-07-28 — Independent Adversarial Pass on the 2026-07-27/28 Output (Q-02)

**File ID:** CR-AUDIT-2026-07-28
**Scope:** the pass QUEUE.md **Q-02** exists to run. Both prior adversarial passes — CR-AUDIT-2026-07-27 and BOC-AUDIT-2026-07-27B — were **self-audits by the analyst who produced the work**, and both said so in their own residual sections. This one re-reads **CR-ACQ v1.5, CR-E01 v1.1, CR-E02 v1.3, CR-E03 v1.0, CR-E04 v1.0, BOC-ROUTE v1.1** and the two prior audits.
**Method:** **primary artifacts first.** The banked transcripts, the four rendered ATF report pages, and the RSS feed were searched and read *before* the write-ups, and the write-ups were then read only to extract testable propositions. This is the discipline LOOP.md §2 requires: *the verification cycle must go back to the source, not to the write-up.* Search was performed on whitespace-flattened text and **validated against a known positive** before any null was accepted (BOC-AUDIT-2026-07-27B §4). Tooling: `scratchpad/tsearch.py`, method recorded at §7.
**Prepared:** July 28, 2026
**Status:** v1.2 — **Q-43 authorised by the user and executed the same day** (§5.1). Q-42 and Q-44 remain open. The pass's findings are otherwise unchanged.

**Headline result: the six files are substantially sound, and the pass found six defects — three material.** Every quotation tested against the transcripts and the ATF report came back **verbatim or fairly rendered**; nothing in the forensic record was found to be misquoted. The defects are of a different kind: **two exhibits sharing a number across two files, an item graded *down* when the record grades it up, and a live deadline held at second-hand confidence while the project's own banked Tier 1 artifact settles it.**

The most consequential is the third. **D-51 taught this library that "where the project holds a primary artifact, no secondary source may set a fact the artifact can settle."** The rule was written on 2026-07-28. **It was not applied to the briefing schedule** — the one part of the record with real deadlines — which BOC-ROUTE §4 still holds at Medium-high on a single news report while **the entire scheduling colloquy sits in `day4.txt`, in the judge's own words**, banked since 2026-07-27.

**Independence, stated honestly.** This pass was run in a **separate session with no memory of producing the audited work**, from the artifacts rather than the summaries. That is materially more independent than a self-audit. **It is not a different reader**: the same model produced both, so shared systematic blind spots — a disposition to over-hedge forensic findings, a habit of building inferences where testimony already exists — would not be visible from here. Two of the six defects below are instances of exactly that shape, which is weak evidence that the blind spot is real and stronger evidence that it is not fully self-correcting. **A human read, or a differently-built reader, remains owed.**

---

## 1. WHAT WAS CHECKED, AND AGAINST WHAT

| Proposition | Primary artifact | Verdict |
|---|---|---|
| Karner: "I use pliers" (CR-E01 §3.2) | day4 06:39:54 | **CONFIRMED verbatim** |
| Inconclusive = data insufficiency; "missing data points"; "Missing is not the same thing as dissimilar" (CR-E01 §3.3) | day4 07:19:31–07:19:59 | **CONFIRMED verbatim** |
| "identifies the cartridge case as being fired in the firearm, but that's all it says" (CR-E01 §3.4) | day4 06:31:27 | **CONFIRMED verbatim** |
| The three comparison photos were an AFTE proficiency-test compilation of images volunteered by examiners who answered **incorrectly** (CR-E01 §3.6) | day4 07:37:01–07:37:20 | **CONFIRMED** |
| "Exhibit 19" as used in CR-E01 §3.6 vs CR-E02 §4 | day4 04:55:45 and 07:33:29–07:36:03 | **DEFECT — two different exhibits.** §2.1 |
| Perch geometry 415 slope / 410 horizontal / 68 vertical (CR-E02 §2; D-50 dissolution) | day4 04:37:27–04:38:24 | **CONFIRMED verbatim.** D-50's dissolution is correct |
| Chamber case = ATF Exhibit 2, graded "well-supported inference… Medium-high" (CR-E02 §4) | day4 05:39:52–05:40:01 | **DEFECT — it is direct sworn testimony.** §2.2 |
| Exhibit 34: "The Exhibit 15A engraving cutter was identified as having made tool marks…" (CR-E02 §5.4b) | day4 05:40:07 | **CONFIRMED verbatim** |
| Exhibit 34: "The Exhibit 16 and Exhibit 18A through 18E cartridge cases were identified as having been fired in the Exhibit 1 rifle" | day4 05:39:06 | **CONFIRMED verbatim** |
| 15A = the longest metal bit of the Dremel (CR-E02 §5.4b) | day4 05:39:33 | **CONFIRMED as testimony**, not inference |
| Fingerprint stipulation incl. "Subsequent examinations… by the FBI were inconclusive" (CR-E02 §3) | day4 04:38:54–04:39:48 | **CONFIRMED verbatim** |
| "We determined that he was not — or he did not touch it" (CR-E02 §3) | day4 05:44:47 | **CONFIRMED verbatim** |
| Twiggs: Dremel "to inscribe bullets"; "I just told him where it was" (CR-E02 §5.3) | day4 02:33:09–02:33:31 | **CONFIRMED verbatim** |
| Hull: no bullets or casings on or immediately around the Losee building (CR-E04 §5.1) | day2 01:49:40–01:50:02 | **CONFIRMED verbatim** |
| Shot 12:23:28; jump 12:24:42 (CR-E04 §4) | day2 00:55:27, 00:56:47 | **CONFIRMED verbatim** |
| "We had identified a person of interest, but we did not specifically know who the shooter was" (CR-E04 §5.5) | day2 01:52:15 | **CONFIRMED verbatim** |
| The .223 round "accounted for" as an officer's ejected cartridge (CR-E04 headline 2, §5.2) | day2 01:43:19–01:44:13 | **DEFECT (minor) — headline firmer than the body.** §2.4 |
| Oliver: samples entirely consumed 1.4, 1.6, 1.9, 1.10, 1.12, 2.1, 3.1, 4.1, 5.1 (CR-E03 §3.2) | day5 01:31:39 | **CONFIRMED verbatim**, incl. the retained-extract list |
| Oliver: support for inclusion of Matthew Robinson (bolt, 1.6) and Lance Twiggs (Dremel buttons) (CR-E03 §3.3) | day5 01:49:41–01:51:25 | **CONFIRMED verbatim**, incl. her "reasonable to assume" framing |
| Bakker's 2025-09-13 communication log (CR-E03 §5) | day2 05:19:02 | **CONFIRMED verbatim** (one trailing sentence dropped; §3) |
| ATF report §3.1 — metadata, exhibit list, all four conclusions, Appendix definitions (CR-ACQ) | `atf_page-26/27/28/29.png`, read directly | **CONFIRMED**, with one truncation defect. §2.6 |
| Which cartridges bore scribe marks | ATF report p.1 vs Exhibit 34 via day4 | **DEFECT (minor) — the two ATF documents disagree.** §2.5 |
| Briefing schedule at Medium-high / "T1 via T3" (BOC-ROUTE §4) | day4 08:16:28–08:21:05 | **DEFECT — the project holds the Tier 1 artifact.** §2.3 |
| D-51 reversal: Rev dates are publication dates lagging one business day | day4 08:12:16–08:18:05; `day*_raw.html` timestamps | **CONFIRMED on two tests not previously run.** §4 |
| BOC-ROUTE §3 corpus: 409 feed items, 54 in window, titles and dates | `feed_20260727.xml`, re-parsed | **CONFIRMED item-for-item** |
| Register integrity D-1 – D-51 | `queue-check.sh` + full grep | **PASS** — no gaps, one assignment site per number |

---

## 2. DEFECTS

### 2.1 MATERIAL — "Exhibit 19" names two different things in two files, and neither says so

**What the files say.** CR-E02 §4: "**State's Exhibit 19 is 'the cartridge case that was recovered from the gun,' from the chamber.**" CR-E01 §3.6: "Burt closed his direct by showing Karner three bullet comparisons (**Exhibit 19, pp. 26–28**)."

**What the record shows — two separate exhibits, in two separate series.**

| | CR-E02's Exhibit 19 | CR-E01's Exhibit 19 |
|---|---|---|
| Transcript | day4 **04:55:45**, State's case | day4 **07:33:29 / 07:34:39 / 07:36:03**, defence case |
| Offered by | McBride, for the State | Burt, for the defence |
| What it is | the **fired cartridge case from the rifle's chamber** — "This is the cartridge case that was recovered from the gun" | **three bullet-comparison photographs**, pp. 26–28, from the AFTE proficiency-test compilation |
| Status | **admitted and published at all three levels** | **NOT admitted.** Burt: "*It has not been admitted… I'm asking this question as a foundation for admitting it*" (07:34:17) |

The transcript renders both as bare "Exhibit 19", the way it renders the defence's Karner exhibits as "Karner 6" and "Karner 11" only when counsel says so.

**Why this matters.** A reader working across CR-E01 and CR-E02 — which is precisely how this library is meant to be read, and which §5 of each file invites — would merge them and conclude that **the chamber cartridge case was the subject of the defence's proficiency-test demonstration**. It was not. Separately, **CR-E01 §3.6 does not record that its Exhibit 19 was unadmitted at the moment it was shown**, which bears directly on the weight of a demonstration the file describes as having its force reversed on cross.

**Fixed in place** (§5): both files now disambiguate, and CR-E01 records the admission status.

### 2.2 MATERIAL — the chamber-case identity is *under*-graded: it is sworn testimony, not an inference

**What the files say.** CR-E02 §4: "Supporting the identity of the items across the two exhibit-numbering systems: the ATF received exactly one fired case plus three cartridges, the fired case bore a Remington headstamp, and Faumuina confirmed the gun's contents went to the FBI and then to the ATF. **This is a well-supported inference, not a stated fact, and is graded as such (Medium-high).**" CR-AUDIT-2026-07-27 §2.4 found the identity "stated flatly" in v1.0 and **re-graded it down** to Medium-high as "an inference presented as a fact."

**What the record shows.** While reading Exhibit 34 aloud on direct, Faumuina was asked the mapping question outright and answered it (day4 **05:39:52–05:40:01**):

> **McBride:** "And then, also the Exhibit 2 cartridge case, what is that?"
> **Faumuina:** "**This would've been the cartridge case that was found in the gun.**"
> **McBride:** "And Exhibits 3, 4, and 5 cartridges?"
> **Faumuina:** "**They were the ones also found in the gun.**"
> **McBride:** "And Exhibit 18A?"
> **Faumuina:** "**Is the one that was found on the safe.**"

That is the ATF lab numbering mapped to physical provenance **on the record, by the witness**, for all three groups at once. `grep -rn "found in the gun"` across the repository returns **nothing** — no file records it.

**How it was missed, and it is a familiar shape.** The passage sits **three questions before** the Exhibit 34 line CR-E02 §5.4b quotes, inside the same block of testimony. CR-E02 §1 records the lesson from the previous miss in almost these words: *"the answer to 'was the tool compared?' sat three questions past every keyword that located the tool."* The full read reached the quotation it was looking for and stopped **one question short in the other direction**.

**Consequence, stated narrowly.** CR-ACQ §6.2's caveat — "the chamber-case inference is **Medium-high**, not certain… **this resolution is therefore itself provisional**" — is **more cautious than the record requires**. The correction runs **toward the State**, as CR-E02 v1.2's Dremel correction did.

**NOT APPLIED — human gate.** Two independent reasons under LOOP.md: this would touch **D-48**, a register entry resolved against a named person (§3), and **D-48 has already moved four times in one day** — §4's hard stop fires at the third. **The direction of D-48 does not change**; what changes is the strength of a caveat attached to it. → **Q-42**, human-gated.

### 2.3 MATERIAL — the briefing schedule is held at second hand while the project holds the primary artifact

**What the files say.** BOC-ROUTE §4 records the briefing schedule from Deseret News at **"Confidence: Medium-high… the docket itself has not been read by this project — the briefing dates in particular are exactly the kind of detail that should be confirmed against the court record before being relied on. Promotion to High requires a direct Utah court-record pull."** CR-ACQ §5/§8 and DOCKET-WATCH.md carry the same dates on the same footing.

**What the record shows.** The whole schedule was set in open court at the close of Day 4 and is in `day4.txt` at **08:16:28–08:21:05**, banked 2026-07-27:

> **Grunander (08:17:54):** "if we're able to collect the transcript Monday, if we had two weeks from Tuesday, we could have our motion in. I believe that's **the 28th of July**."
> **Graf:** "So state's brief by the 28th of July…"
> **Visser (08:18:16):** "We need two weeks after that. So **August 11th**…"
> **Grunander (08:18:28):** "It would be seven days after that, Judge. So **the 18th**?" — **Graf:** "**August 18th.**"
> **Graf (08:18:35):** "And for oral argument, what I can set is **September 1st**… we can start at **10:00 a.m.**"
> **Graf (08:20:50):** "So **35 pages** for the initial filings, **18** response, and September 1st at 10:00 a.m."

**Every date the library carries is correct.** The defect is not the dates — it is that **the one time-critical fact set in the library is graded from a news report while a Tier 1 artifact stating it sits unread in the repository.** That is the D-51 failure verbatim, and the rule D-51 earned was written the same day this file set was finished.

**Four things established here that no file records:**

1. **Page limits** — 35 pages for both initial briefs, **18** for the State's reply.
2. **Oral argument format** — **in person**, up to **two hours per side**.
3. **Ms. Nester asked to move the September 1 argument** ("I'm going to be in trial that week and I'd really like to be here for this argument") and **the court declined** — "This is a fortunate opening" — with the defence accepting. **DOCKET-WATCH.md §"What each run checks" item 3 watches for "anything moving the 09-01 date"; a known, on-the-record scheduling conflict for lead defence counsel is exactly the precursor that watch exists to catch, and the watch does not know about it.**
4. **A party role the library does not have.** **Jeffrey Neiman** appeared as counsel for Ms. Kirk / the Kirk family as victim's representative (day4 08:14:52, 08:15:12, 08:21:30, and at 06:14:36 on the exhibit-publication request). CR-ACQ §5's participant list has prosecution, defence and the Sheriff's separate counsel — **no victim's counsel**. He is an active participant whose requests the court ruled on.

**NOT APPLIED — human gate.** Case posture is `human` in every mode (LOOP.md §3), and DOCKET-WATCH.md's own rules say a run "**Must NOT, ever: change a case-posture statement in any topic file.**" That prohibition binds this pass too. → **Q-43**, human-gated. **This is the single highest-value item this pass produced**, because it is the half of the project with deadlines.

### 2.4 MINOR — the .223 round is resolved more firmly in the headline than in the body

**What the file says.** CR-E04's headline finding 2: "**The .223 round on the Computer Science roof was accounted for as a police officer's ejected cartridge** — resolving, innocuously, the item CR-E03 §4.1 recorded neutrally." CR-E03 §4.1 now carries a banner reading "⚠ **EXPLAINED 2026-07-28**."

**What the record shows** (day2 01:43:19–01:44:13). Nester asked about "a bullet found on **another building**." Hull: "I believe an unfired bullet had been found on another building at some point." — "**Which building was that, sir?**" — "**I don't recall.**" No calibre was given. His account is expressly recollective: "**My recollection is** that was accounted for…", and to "when was that accounted for?" — "**I don't know specifically.**"

Davis's item (day3, CR-E03 §4.1) is a **live .223 round on the Computer Science building roof**, documented by Agent Snyder. Identifying Hull's unrecalled item with Davis's specific one is an **inference** — a good one, and the innocuous reading is the one the record offers.

**Assessment.** CR-E04 §5.2's **body is correct and properly hedged**, grading it **Medium** and stating the non-recollection plainly. **The headline and the cross-file banner are not** — both read as settled. This is the shape CR-AUDIT-2026-07-27 §2.4 found one day earlier ("an inference presented as a fact"), reappearing in a **headline position**, which travels further than a body paragraph. It matters because CR-E03 itself says this is "exactly the sort of item that acquires meaning in retellings" — and an over-firm dismissal circulates as readily as an over-firm anomaly.

**Fixed in place** (§5): headline and banner now carry the body's grade.

### 2.5 MINOR — two ATF documents disagree about which cartridges bore scribe marks, and no file notes it

| Document | Text |
|---|---|
| ATF report, 2025-09-17, p.1 (**read directly**) | "Toolmarks were located on the exterior of the Exhibit 2 cartridge case **and Exhibit 3 cartridges** (scribe marks)…" |
| Exhibit 34, read aloud by Faumuina (day4 05:40:07) | "…identified as having made tool marks located on the Exhibit 2 cartridge case, **Exhibit 3 through five cartridges**, and Exhibit 18A cartridge case." |

CR-E02 §5.2b independently records engravings read into the record on **all four** items recovered from the rifle (State's Exhibits 19, 20, 21, 22), which favours the "3 through 5" reading.

**Assessment.** Most likely a typographical omission in the earlier report, and CR-ACQ quotes it faithfully under its stated policy of preserving source errors (§1). **But the tension between two ATF documents on the same items is unflagged anywhere**, and a reader holding both will hit it. Recorded as an open item, **not** a register entry — a discrepancy between two documents this project has read only one of directly does not yet earn a D-number.

### 2.6 MINOR — CR-ACQ's `source identification` definition drops a limiting clause inside an ellipsis

CR-ACQ §3.1 renders the report's Appendix definition as:

> "an examiner's conclusion that two toolmarks originated from the same source… all observed class characteristics are in agreement and the quality and quantity of corresponding individual characteristics is such that the examiner would not expect to find that same combination… repeated in another source."

The Appendix (`atf_page-29.png`, read directly) continues, in the same sentence:

> "…repeated in another source **and has found insufficient disagreement of individual characteristics to conclude they originated from different sources.**"

The quotation ends without a closing ellipsis, so it reads as complete. The dropped clause is **qualifying**, and it is dropped from the definition of the exact term CR-ACQ calls "the strongest positive conclusion in the framework" and on which D-48 turns. **This is the file's own §0 hazard — selective quotation, reliable as to the words and not as to the document — committed by the file against its own primary source.** Small in effect, worth fixing precisely because of what it is an instance of.

**Fixed in place** (§5).

## 3. WHAT SURVIVED — recorded because an audit that only finds fault is as unreliable as one that never does

- **Every forensic quotation tested came back verbatim.** The pliers, the "missing data points" exchange and Burt's "missing is not the same thing as dissimilar" concession, the DOJ limiting-language answer, the fingerprint stipulation *including* the FBI-inconclusive remainder, "he did not touch it", both Exhibit 34 identifications, the Twiggs Dremel exchange, Hull's "not to my knowledge" and "person of interest", Oliver's consumed-sample list, Bakker's communication log, the 12:23:28 and 12:24:42 timestamps. **Not one misquotation was found in the forensic record.**
- **D-50's dissolution is right.** Faumuina's complete answer gives 415 slope / 410 horizontal / 68 vertical exactly as CR-E02 §2 records; √(410²+68²) ≈ 415.6.
- **The ATF report is accurately inventoried.** Metadata, all six exhibit lines, all four conclusions, the signatories (Karner / Tokay / Owens, all 2025-09-17) and the Appendix definitions match the rendered pages, subject to §2.6.
- **BOC-ROUTE §3 is exact.** Re-parsing `feed_20260727.xml` independently gives 409 items, 54 in the declared window, newest Ep 365 at 2026-07-24 — and every date, episode number and title in the §3 table matches the feed, including the two un-numbered interview items.
- **Register integrity holds.** D-1 – D-51, no gaps, one assignment site per number; `queue-check.sh` clean; no provisional findings outstanding.
- **Scope discipline holds throughout.** Every file states what it did not read. CR-E03 §1 tabulates its own partiality day by day. No file was found claiming coverage it lacked.
- **Two apparent internal contradictions turned out to be the witness.** CR-E01 §2 says Karner had "a little over six years" at ATF and §3.6 says "six and a half"; she gave **both** figures, to different counsel (06:24:43 and 07:38:30). The file is faithful, not inconsistent.
- **The both-directions rule is being followed in practice, not just declared.** CR-E02 §3 down-weights a defence-favourable finding; CR-E02 §5.4b withdraws a bound that ran against the State; CR-E04 leads with three findings against the prosecution narrative. The ledger is genuinely two-sided.

## 4. D-51 — CONFIRMED, on two tests neither prior pass ran

The reversal rests on Rev's page dates being **publication** dates lagging one business day. The prior pass established that from the Day 1 slug plus a Daily Herald headline. Two independent mechanical tests now confirm it:

**Test 1 — the transcript's own scheduling colloquy.** On the day recorded as **Day 4**, Grunander said the State "would prefer to argue **tomorrow**" (08:12:16) and that the reporter "could have a transcript available as early as **Monday of next week**" (08:12:16), then "if we had two weeks from **Tuesday**… I believe that's **the 28th of July**" (08:17:54). Two weeks before Tuesday 28 July is Tuesday **14 July**; the Monday before that is **13 July**. A "tomorrow" must therefore follow, and the day cannot be a Friday. **Day 4's proceeding is Thursday 9 July**, and Day 5 — where Oliver testifies and no scheduling occurs — is **Friday 10 July**. If Rev's page date were the proceeding date, Day 4 would be Friday 10 July and "tomorrow" would be a Saturday.

**Test 2 — the page timestamps precede the proceedings they would have to record.** From the banked raw HTML:

| File | `datePublished` | `dateModified` (UTC) | Proceeding it records |
|---|---|---|---|
| day1 | 2026-07-07 | 07-07 15:53 | Mon 07-06 |
| day2 | 2026-07-08 | 07-08 **16:36** | Tue 07-07 |
| day3 | 2026-07-09 | 07-09 14:52 | Wed 07-08 |
| day4 | 2026-07-10 | 07-10 **11:16** | Thu 07-09 |
| day5 | 2026-07-13 | 07-14 00:01 | Fri 07-10 |

**day4's page was last modified at 11:16 UTC — about 5:16 a.m. Mountain — on 10 July.** A transcript of a proceeding held that day could not exist before it started. The same holds for day2 (10:36 a.m. Mountain, mid-proceeding). **The dates are publication dates. The hearing ran 2026-07-06 → 2026-07-10. D-51's reversal is correct and now rests on primary internal evidence rather than on metadata plus one news report.**

This also means the **State rested its case in chief on Thursday 9 July** (day4 06:14:32, "Your Honor, the State rests its case in chief"), and that Karner and Oliver were **defence** witnesses in the defence case — consistent with CR-E01 §1 and CR-E03 §1, and now anchored.

## 5. CORRECTIONS APPLIED, AND CORRECTIONS WITHHELD

**Applied** — none touches case posture, a register entry, or a living person's conduct, so all fall inside Q-02's `verify` gate:

| File | → | Change |
|---|---|---|
| **CR-E01** | v1.2 | §3.6 disambiguates the defence's "Exhibit 19" (bullet-comparison photographs, pp. 26–28) from **State's** Exhibit 19 (the chamber cartridge case), and records that the defence exhibit **had not been admitted** when shown |
| **CR-E02** | v1.4 | §4 and §5.2b mark theirs as **State's** Exhibit 19 and cross-reference the collision |
| **CR-E04** | v1.1 | Headline 2 and the CR-E03 §4.1 banner carry §5.2's **Medium** grade and Hull's non-recollection of building and calibre |
| **CR-E03** | v1.1 | §4.1 banner softened to match |
| **CR-ACQ** | v1.6 | §3.1's `source identification` definition completed with the dropped limiting clause; §2.5's inter-document scribe-mark tension added as an open item |

**Withheld, and queued instead** — each is `human`-gated under LOOP.md §3, and this pass will not execute a gate it is subject to:

| → | Item | Why withheld |
|---|---|---|
| **Q-42** | Re-grade the chamber-case identity from "Medium-high inference" to **Tier 1 sworn testimony** (§2.2), and relax CR-ACQ §6.2's dependent caveat | Touches **D-48**, resolved against a named person; **D-48 has moved four times**, past LOOP.md §4's third-movement hard stop |
| ~~**Q-43**~~ | ~~Promote the briefing schedule to **Tier 1, read directly**~~ — **AUTHORISED AND EXECUTED the same day; see §5.1 below** | ~~Case posture — `human` in every mode~~ **Gate satisfied: the user authorised it** |
| **Q-44** | Flag the ATF inter-document scribe-mark discrepancy for resolution when Exhibits 32/34 are obtained (§2.5) | Needs the exhibits, not a decision |

### 5.1 Q-43 — authorised and executed, 2026-07-28

The user authorised §2.3's fix the same day, satisfying the `human` gate. **The colloquy was then read in full**, which turned up more than §2.3 had:

| File | → | Change |
|---|---|---|
| **CR-ACQ** | v1.7 | **New §5.1** — the probable-cause briefing order at **Tier 1, read directly**, now the library's **canonical statement**. §5 gains **Jeffrey Neiman** and a count-seven corroboration. §8 item 11 closed, item 12 opened |
| **BOC-ROUTE** | v1.2 | §4 tiering superseded; schedule legs → Tier 1, charge-list/30-hours/death-penalty legs left at Medium-high; **D-47 not re-resolved** |
| **DOCKET-WATCH** | v1.1 | Calendar re-sourced; page limits, format and the conditional 07-28 date added; **run-check 3 now looks specifically for a defence motion to continue** |
| **CR-E04, LOOP** | v1.1 / — | Restatements now point at CR-ACQ §5.1 |

**Four things the full read added that the audit's first pass at §2.3 had not:**

1. **The State's 07-28 date is conditional** — Grunander offered it "if we're able to collect the transcript Monday," and Graf set it "assuming that they can get the transcript by Monday." **A slipped State brief may be the court reporter, not the case.** No file could have known this from the news report.
2. **The procedural history of the order.** The **defence** requested briefing over the **State's objection** — the State having offered to argue bind-over orally the next day with no rebuttal evidence — and the **victim's representative expressly took no position** while asking for speed. BOC-ROUTE §4's "granting the defense's request for written briefing" is confirmed at source.
3. **"Up to two hours per side" is the court's characterisation, not a formal order** — Graf: "*it sounds like* up to two hours per side." Recorded as said.
4. **A reserved ruling nobody was tracking** — the Kirk family's request to display the full Exhibit 12.1 in open court, deferred to the end of the defence case and unresolved on the portion of Day 5 read. → CR-ACQ §8 item 12.

**And one thing worth stating about the gate itself.** §2.3 was found by an independent pass, withheld under a `human` gate, authorised, and executed within hours. **The gate cost nothing and caught the right thing** — a case-posture edit went to the person entitled to decide it, and the delay was one message. That is the protocol working as designed rather than as friction.

## 6. NEW MATERIAL LOCATED, NOT INVENTORIED

**Faumuina's Day 2 turns are more substantive than the queue assumes.** Q-14 lists them as 58 turns of unread testimony. They include her **reading FBI DNA results into the record** — at day2 05:10:57 she read Item 7.1 aloud over a defence 403 objection that was overruled, and Burt's objection ("we have the analyst here who will be testifying") places it immediately before Bakker. **This is the towel-and-screwdriver material CR-E03 §5 flags as having unknown likelihood ratios.** Q-14 should be re-ranked accordingly; the content itself involves a named living person and is not summarised here.

## 7. METHOD, SO THE PASS IS REPRODUCIBLE

**Incidental tooling finding.** `queue-check.sh`'s provisional-findings check **pattern-matches the token rather than reading the hit**, and fired on the first draft of this file — on the sentence in §3 stating that *no* provisional findings are outstanding. Harmless here because the report is read by a human, but it is **standing hazard 6 in another guise** ("grep, then read the hit"), now living inside the validator that enforces the other hazards. Worked around by rewording; **the check itself is unfixed** and will fire again on any file that discusses the marker without carrying one.

Search ran on **whitespace-flattened** transcript text, because the banked files are broken into timestamp blocks and a fixed-width context window spanning line breaks silently returns nothing — the false-negative trap recorded at BOC-AUDIT-2026-07-27B §4. The tool was **validated against a known positive** ("use pliers", day4) before any null was accepted. Every null reported above is scoped to the five banked day files and to that method. The ATF report was read from the **rendered page images**, which CR-ACQ §1 correctly identifies as the authority; the `.txt` derivative is glyph-scrambled and was not used.

## 8. RESIDUAL — WHAT THIS PASS DID NOT DO

1. **Same model, different session.** More independent than a self-audit; **not** an independent reader. See the header.
2. **It checked propositions the files make.** Defects arising from **absence** — a finding never written because the material was never read — are largely invisible to it, exactly as CR-AUDIT-2026-07-27 §5.3 said of itself. §6 is the one exception, and it was found by accident.
3. **Days 1, 2, 3 and 5 were searched, not read.** Only targeted passages were opened. **Day 1 remains entirely unread (Q-01)**, and it contains Hull's first tranche.
4. **No exhibit was obtained.** Exhibits 30, 31, 32, 33, 34, the surveillance compilations and the case file remain known only through description; §2.5's discrepancy cannot be resolved without them.
5. **Still the commercial rendering.** Every quotation confirmed above is confirmed against Rev, not against the certified transcript (Q-36).
6. **The BOC side was checked only where it touches the court record** — the corpus table and D-47's docket leg. **D-45, D-46, the T1 integration and the episode files were not re-tested**; BOC-AUDIT-2026-07-27B remains the only pass over them, and it was a self-audit.
7. **It did not test the 2026-07-20 Phase 0 inheritance**, which BOC-AUDIT-2026-07-27B §6.2 also left untouched. That set is now two passes deep in inherited trust.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.2** | **2026-07-28** | **Off-by-one corrected in the register-integrity statement.** §1's check table and §3 both read "D-1 – D-52"; the register ceiling is **D-51** and D-52 is the next *unassigned* number (QUEUE.md header). Cause: `queue-check.sh` reports "highest string D-52" by counting the forward-looking "next is D-52" notes — the audit carried the validator's string count without reading the hits, which is **standing hazard 6's exact shape occurring inside the audit that enforces it**. Verified by full grep: all four D-52 sites in the library are forward-looking notes or this file's own two (now corrected) lines. No finding changes; the "no gaps, one assignment site per number" verdict stands, restated against the correct ceiling. |
| **1.1** | **2026-07-28** | **Q-43 authorised by the user and executed the same day — new §5.1.** The full colloquy (day4 08:08:11–08:21:46) was read rather than the extract §2.3 worked from, and added four things: the **State's 07-28 date is expressly conditional** on the court reporter delivering by 2026-07-13; the **procedural history** of the briefing order (defence requested, State opposed, victim's representative took no position, court granted); "up to two hours per side" is **Graf's characterisation** rather than a formal order; and a **reserved ruling nobody was tracking** — the Kirk family's request to publish the full Exhibit 12.1, deferred to the end of the defence case and unresolved on the portion of Day 5 read. Files updated: **CR-ACQ v1.7** (new §5.1, now canonical; Neiman and count-seven added to §5), **BOC-ROUTE v1.2** (§4 tiering superseded; **D-47 not re-resolved**), **DOCKET-WATCH v1.1** (calendar re-sourced; run-check 3 now looks specifically for a defence motion to continue), **CR-E04 v1.1** and **LOOP.md** (restatements repointed). §5's withheld-corrections table updated. **Q-42 and Q-44 remain open.** |
| 1.0 | 2026-07-28 | Initial file. **Q-02 executed** — the independent pass both prior audits declared owed, run in a separate session from the primary artifacts rather than the write-ups, with search validated against a known positive before any null was accepted. **Six defects, three material.** (a) **"Exhibit 19" names two different exhibits** across CR-E01 and CR-E02 — the State's admitted chamber cartridge case and the defence's **unadmitted** bullet-comparison photographs — and neither file says so; corrected in place, with the admission status now recorded. (b) **The chamber-case identity is under-graded**: CR-E02 §4 calls it "a well-supported inference… Medium-high" and CR-AUDIT-2026-07-27 §2.4 re-graded it *down*, but Faumuina mapped ATF Exhibits 2, 3–5 and 18A to their physical provenance **on the record** at day4 05:39:52, three questions before the Exhibit 34 line CR-E02 quotes — the same overshoot CR-E02 §1 had already named, running the other way. Withheld from application: touches **D-48**, past LOOP.md §4's third-movement stop. (c) **The briefing schedule is held at Medium-high from a news report while the entire scheduling colloquy sits in the banked day4 transcript in the judge's own words** — the D-51 rule unapplied to the one part of the record with live deadlines; four facts recorded that no file has, including the **35/35/18 page limits**, the two-hours-per-side in-person format, **Ms. Nester's declined request to move the 09-01 argument** (a continuance precursor DOCKET-WATCH.md is watching for and does not know about), and **Jeffrey Neiman** as counsel for the victim's representative, absent from CR-ACQ §5's participant list. Withheld: case posture is `human` in every mode. (d) **The .223 round** is stated as settled in CR-E04's headline and CR-E03's banner while the body correctly grades it **Medium** — Hull recalled neither the building nor the calibre; corrected in place. (e) **Two ATF documents disagree** on whether scribe marks were located on Exhibit 3 or Exhibits 3–5; unflagged anywhere, logged as an open item rather than a register entry. (f) **CR-ACQ's `source identification` definition** drops a limiting clause inside an ellipsis — the file's own selective-quotation hazard, committed against its own primary source; corrected. **D-51's reversal CONFIRMED on two tests neither prior pass ran:** the transcript's internal scheduling colloquy ("argue tomorrow", "transcript Monday", "two weeks from Tuesday… the 28th of July") is only consistent with Day 4 = Thursday 9 July; and **day4's page was last modified at 11:16 UTC on 10 July**, hours before a 10 July proceeding could have concluded. **Nothing in the forensic record was found misquoted** — every one of ~20 quotations tested against the transcripts and the four rendered ATF pages came back verbatim or fairly rendered, and BOC-ROUTE §3's corpus table matches the banked feed item-for-item. **New material located:** Faumuina's Day 2 turns include her reading FBI DNA Item 7.1 into the record over an overruled objection — the towel-and-screwdriver material CR-E03 §5 flags as unknown; **Q-14 re-ranked**. Three items queued rather than executed (**Q-42, Q-43, Q-44**), each because the gate that covers it binds this pass too. |
