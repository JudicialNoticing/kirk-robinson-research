# CR-E20 — The forensic exhibit map: which report is which, and the "Exhibit 30" collision

**File ID:** CR-E20 · **Scope:** the **canonical identification of every forensic laboratory report entered at the preliminary hearing** (2026-07-06 → 2026-07-10) in *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo Department, Utah County — Hon. **Tony F. Graf, Jr.** Written because **this library has been calling State's Exhibit 30 "the ATF firearm report," which is the natural name for State's Exhibit 32** — and because **"Exhibit 30" has three referents on this record.**

**Prepared:** 2026-08-30 · **Status:** **v1.3 — `[PROVISIONAL]`.** 🛠 **2026-08-30: `F-4`'s bound re-expressed from "the submission-1 report" (no such thing — see `CR-E21 F-2`) to "the 2025-09-17 firearms report." F-4 itself survives unchanged.** No independent verification cycle has run on this file. ⚠ **`CR-E15` v1.1 now DEPENDS on this file for `F-4`, and this file is provisional — neither can clear the other (§8).** Every identification below is **read directly from the transcripts on disk and quoted verbatim**, but the exhibits themselves remain unread.

> 🚨 **CASE POSTURE, as of 2026-08-30. TYLER ROBINSON HAS NOT BEEN BOUND OVER.** The preliminary hearing tests probable cause only; 2026-09-01 is its last day, argument on a closed evidentiary record. **Presumption of innocence is absolute.** No court has found any fact below to be true, and the court made **no reliability ruling** on any forensic evidence.

> **Living persons.** **Lance Twiggs** holds use immunity from two offices, **did not testify live** (sworn recorded statement received under Rule 1102), and **is accused of nothing**. **Amber Robinson and Matthew Robinson** appear in this material only as **elimination-sample donors**, sought because they were associated with the premises and **not as suspects**; neither is accused of anything. This file assigns no DNA to anyone and draws no inference about any person.

---

## §0 · Sourcing framework (project standard)

**Tier 1** — sworn testimony and primary court filings/documents · **Tier 2** — named official statements · **Tier 3** — named journalistic reporting/analysis · **Tier 4** — anonymous or low-verification. **"T1 via T3"** marks primary-document content known only through reporting.

**Every identification in §2 is Tier 1** — a witness, under oath, saying what the document in front of him was, at a located timestamp. ⚠ **Tier 1 as to what the witness said the document is. NOT Tier 1 as to the document's contents, which remain unread (§1).**

## §1 · Access-path caveats — read before using any row

- 🚨 **NOT ONE OF THESE EXHIBITS HAS BEEN READ BY THIS LIBRARY.** Every one is known only through a witness describing or reading portions aloud. **`CR-E15` is the sole partial exception and it is a different access path — see §4.**
- ⚠ **Uncertified Rev machine transcripts.** Speaker attributions inferred from content, never labels (`CR-E16`).
- ⚠ **This map is of STATE'S exhibits at the preliminary hearing.** It does not govern the defence's exhibit series, the "Oliver NNN" display-software designators (`DNA-E01` §1.4), ATF's or the FBI's internal item numbering, or exhibit numbers in any filing.

---

## §2 · 🚨 THE CANONICAL MAP

| State's Exhibit | Identified on the record as — **verbatim** | Laboratory & discipline | What it carries |
|---|---|---|---|
| **30** | *"This is **the ATF report that I received regarding the DNA testing on the gun** and cartridge and cartridge casings, oh, sorry, correction, cartridge case and cartridges."* — Sgt. Faumuina, `day4.txt` **05:18:35**. Prosecutor, moving admission: *"This Exhibit deals with **DNA testing on the rifle and the cartridges**."* (**05:19:09**) | **ATF — DNA** | ATF **item 1.x** (the rifle's sub-items), **2.1** (fired .30-06 cartridge case), **3.1 / 4.1 / 5.1** (cartridges from the firearm), **7.1** (Tyler Robinson's known sample), **8.1** (undescribed). **The seven statistical calculations.** **p. 8 = the consumed / retained-extract page.** |
| **31** | *"This is **the FBI report** that was provided to me by the FBI **that documents DNA testing**."* — Sgt. Faumuina, `day2.txt` ~05:05, confirming it includes *"the screwdriver… and the towel"* | **FBI — DNA** | FBI **items 1–6** (Losee north-east corner swabs), **7 the towel**, **8 the screwdriver**, **9 backpack**, **54** swiped finger areas, **55** stairwell railing |
| **32** | *"This is **an ATF report that I received in relation to the gun as well as cartridge case and cartridges**."* — Sgt. Faumuina, `day4.txt` **05:26:25**. Admitted 05:27:06. Next question: *"Exhibit 32 is in front of you. **And what was being analyzed in this test?**"* | **ATF — firearms / toolmark** | 🚨 **THE TEST FIRES: *"The Exhibit 1 rifle was test fired and found to be in operable condition. The test fires were designated as Exhibit 1.11."*** (**05:28:32**) · the `[Source identification]` of the Exhibit 2 cartridge case to the Exhibit 1 rifle · the `[Inconclusive]` bullet-jacket fragment |
| **33** | *"This is **an ATF biology report on the Dremel tool** as well as **the cartridge cases that were found on top of the safe** in Tyler's home."* — Sgt. Faumuina, `day4.txt` **05:32:33** | **ATF — DNA / biology** | ATF **items 15.x** (Dremel: buttons, cord, metal bits), **18.1** (the etched *"test shot"* .30-06 cartridge case from atop the safe) |
| **34** | *"This is **an ATF report I received that was comparing tool marks**."* — Sgt. Faumuina, `day4.txt` **05:36:19** | **ATF — toolmark comparison** | *"The **Exhibit 15A engraving cutter** was identified as having made tool marks located on the Exhibit 2 cartridge case, Exhibit 3 through five cartridges, and Exhibit 18A cartridge case."* |
| ⚠ **"Baker Exhibit 30"** *(DEFENCE series — NOT State's)* | *"Could you go to **Baker Exhibit 30**, page one… **This is a publication by the National Institute of Standards and Technology called Forensic DNA Interpretation and Human Factors**."* — Mr. Burt to Oliver, `day5.txt` **01:35:11–01:35:37** | — | **A NIST publication. NOT a laboratory report. NOT State's Exhibit 30.** |

> ### ⚠ IS THE SET COMPLETE? — a scoped null, run 2026-08-30
>
> **The five laboratory reports above are the complete forensic-report set entered at this hearing, on this record.** *(Method: `/Exhibit (29|3[0-9])/` over `day1.txt`–`day5.txt`, every hit opened.)*
> - **No "Exhibit 29", "Exhibit 36", "Exhibit 37" or "Exhibit 38" occurs anywhere in five days — zero hits each.**
> - **State's Exhibit 35 exists but is NOT a laboratory report: it is a MAP.** *(`day4.txt` 04:41:xx — "will you take a look at Exhibit 35?… **Will you take a moment to orient yourself on that map** and tell me when you've found the relevant points…")* It was on screen when Exhibit 30 was introduced and was taken down for it, which is why the two sit adjacent in the transcript.
> - So the run **30 · 31 · 32 · 33 · 34** is unbroken and closed at both ends **as to what was displayed and identified on this record.**
>
> ⚠ **SCOPE, STATED EXACTLY: this is a null over the FIVE-DAY TRANSCRIPT, not over the exhibit list as filed.** An exhibit marked but never displayed, or displayed without its number spoken, would not appear. **"No further forensic report was identified on this record" is NOT "no further forensic report exists."** **Decisive artifact: the court's exhibit list.**

---

## §3 · 🚨 THE COLLISION, STATED SO IT CANNOT RECUR

**`CR-E20 F-1` — "The ATF report" is never a sufficient designation, because there are FOUR of them and they split two-and-two across disciplines. Confidence: High.**

| | **DNA / biology** | **Firearms / toolmark** |
|---|---|---|
| **The rifle and its ammunition** | **Exhibit 30** | **Exhibit 32** |
| **The Dremel and the home cartridge cases** | **Exhibit 33** | **Exhibit 34** |

⚠ **Exhibits 30 and 32 are BOTH ATF reports, BOTH about the same rifle and the same cartridge case and cartridges, and were admitted EIGHT MINUTES APART through the SAME witness.** Their identifying sentences are nearly identical in form — *"the ATF report… regarding the DNA testing on the gun and cartridge case and cartridges"* against *"an ATF report… in relation to the gun as well as cartridge case and cartridges."* **The only discriminator in the second sentence is the ABSENCE of the words "DNA testing."**

> ### ✅ TWO FURTHER ANCHORS, AND ONE OF THEM IS THE COURT'S OWN
>
> 🛠 *(ADDED 2026-08-30, surfaced by the `DNA-E01` corrective pass, verified directly here.)*
> - **A THIRD confirmation of Exhibit 30's discipline, on its own first page:** counsel walks the witness to *"the bottom of this first page, and here in **the DNA Analysis section**, again, we see that the report or the author refers to the items by their Exhibits numbers"* (`day4.txt` **05:20:17**). **The document says "DNA Analysis" on its face.**
> - 🚨 **THE COURT NAMED BOTH EXHIBITS SEPARATELY, IN ONE SENTENCE, AND RE-CHARACTERISED NEITHER:** ruling on a relevance objection during Karner's cross — *"I find that this is relevant, as it relates to **State's Exhibit 30, which was admitted, as well as State's Exhibit 32, which is admitted**"* (`day4.txt` **06:36:35**). **Previously unrecorded anywhere in this library.** It is the strongest single line establishing that **30 and 32 are two distinct admitted exhibits**, and it comes from the bench rather than from a party.

**`CR-E20 F-2` — This library has been calling State's Exhibit 30 "the ATF firearm report," which is the natural name for State's Exhibit 32. Confidence: High.**

> ✅ **AND THE BOTH-DIRECTIONS RESULT, WHICH RUNS TOWARD THE LIBRARY AND IS RECORDED AS PROMINENTLY AS THE DEFECT.** The corrective pass audited **all 54 case-insensitive "Exhibit 30" references in `DNA-E01`** and classified every one. **Mis-citations of Exhibit 32's CONTENT to Exhibit 30 — the test fires, the `[Source identification]`, the `[Inconclusive]` fragment: ZERO.** Not one sentence. **The defect was NAMING, not mis-citation** — the library had the right number attached to the right content throughout and called that number by the wrong report's name. ⚠ **That distinction matters for how far the correction has to reach: no substantive finding in `DNA-E01` moved, and none needed to.**

**The defect was found on 2026-08-30 by an independent adversarial agent**, in this shape: `DNA-E01` §1.4 defines the map correctly — Exhibit 30 = the ATF DNA report, Exhibit 32 = *"not DNA"* — **and then five other sections of the same file call Exhibit 30 "the ATF firearm report."** ⚠ **The cost is not cosmetic.** `DNA-E01 F-14` turns on 1.11 arriving from a **different report** than the consumption lists; **under the old naming both reports were called "the ATF firearm report," which made that distinction invisible to any reader who did not already know it.**

**`CR-E20 F-3` — "Exhibit 30" has THREE referents on this record and a bare use is unsafe. Confidence: High.**
1. **State's Exhibit 30** — the ATF DNA report.
2. **"Baker Exhibit 30"** — the defence's NIST publication (`day5.txt` 01:35:11).
3. Any bare *"Exhibit 30"* in a transcript passage, which must be resolved from context before use.

> ### 🚨 THE WRITING RULES THIS FILE IMPOSES ON THE LIBRARY
>
> 1. **NEVER write "the ATF report" or "the ATF firearm report" bare.** Write **"State's Exhibit 30 (the ATF DNA report)"** or **"State's Exhibit 32 (the ATF firearms/toolmark report)"** — number **and** discipline, every time.
> 2. **NEVER write a bare "Exhibit 30."** Write **"State's Exhibit 30"** or **"the defence's Baker Exhibit 30"** (§3 `F-3`).
> 3. **The consumption page (p. 8), the seven calculations and every ATF item 1.x/2.1/3.1/4.1/5.1 belong to Exhibit 30.** **The test fires (ATF 1.11), the source identification and the inconclusive fragment belong to Exhibit 32.** **Never cite one to the other.**
> 4. **"ATF item 1.11" is not a DNA sub-item at all** — it is Exhibit 32's designator for the laboratory's own test fires (`DNA-E01 F-14`), which is why it appears on neither of Exhibit 30's consumption lists.
> 5. ⚠ **The FBI's item series and ATF's item series are different series** (`DNA-E01 F-7`). Exhibit 31's item 7 is the towel; Exhibit 30's item 7.1 is, on the best reading, Tyler Robinson's known sample. **Write the laboratory every time.**

> ### 🚨 §3a · A PARTY TOLD THE COURT OLIVER'S REPORTS WERE "EXHIBITS 30 AND, I BELIEVE, 34" — AND ON THIS MAP THAT CANNOT BE RIGHT
>
> 🛠 *(ADDED 2026-08-30; found by an independent agent auditing `CR-E06`, verified directly here.)* On Day 5, before Oliver was called, counsel told the court:
>
> > *"we have one witness, the final witness. Well, the defense has one witness. That witness is a ATF DNA forensic biologist, and I assume that the exhibits that will be admitted through her will be of that nature. We've already, in fact, admitted the report that she is going to be testifying to. **The reports, I should say that's exhibits 30 and, I believe, 34.**"* — `day5.txt` **55:28**
>
> ⚠ **ON THE §2 MAP THIS IS WRONG: State's Exhibit 34 is the ATF TOOLMARK COMPARISON report, not a DNA report.** The ATF's second **biology** report — the Dremel and the cartridge cases from atop the safe — is **State's Exhibit 33**. The natural reading is that **"34" is a misspeak or a Rev garble for "33"**, and counsel's own **"I believe"** hedges it.
>
> ⚠ **BUT IT IS NOT RESOLVED HERE, AND TWO THINGS BLOCK RESOLVING IT.** **(1)** **Nothing on this record establishes that Oliver authored State's Exhibit 33** — Exhibit 33 was identified on a **different day by a different witness** (Sgt. Faumuina, `day4.txt` 05:32:33), and Oliver was never asked about its authorship. So the correction "33 not 34" is itself an inference. **(2)** ⚠ **THE SPEAKER IS NOT ESTABLISHED.** Rev labels the turn **Mr. McBride** (the State), but the content self-corrects mid-sentence — *"we have one witness… Well, **the defense** has one witness"* — and the surrounding turn order is irregular (the court says *"To the media"* and the next turn is again labelled McBride). **Per this library's standing rule, speakers are inferred from content and never from labels; here the content is ambiguous, so the attribution is left open.** *(→ `CR-E16`.)*
>
> **What this DOES establish, and it is the point of recording it: a party stated a report-to-exhibit mapping in open court that does not match the identifications made on the record, and nobody corrected it.** **Confidence that the statement was made: High** *(verbatim, located)*. **Confidence that "34" should read "33": Medium — an inference, not a finding.** **Confidence as to who said it: unverified.**
>
> **What would settle it:** the court's exhibit list; the authorship block of State's Exhibit 33; the certified transcript for both the wording and the speaker.

---

## §4 · The join nobody had made: `CR-E15`'s document IS State's Exhibit 32

**`CR-E20 F-4` — The ATF firearms report that `CR-E15` read at Tier 1 from a court filing IS State's Exhibit 32. ANCHOR: High. IDENTITY: High.** 🛠 **RE-GRADED from Medium-high, 2026-08-30, the same day it was written** — see the box below. **The upgrade was earned by verification acts performed on `CR-E15`'s v1.1 pass, not by re-reading my own reasoning.**

`CR-E15` (v1.0, 2026-08-16) read the **ATF firearms report 2025-W-000401 of 2025-09-17** by rendering the pages of **Exhibit 2 to the defence's bullet-fragment motion**, banked 2026-07-27. **It records the `[Source identification]` on the cartridge case, the `[Inconclusive]` bullet-jacket fragment, the rotary-tool scribe marks, and that the rifle was test fired and found operable** — *which is the content of State's Exhibit 32*, and the test-fire sentence read at `day4.txt` 05:28:32 is **the same sentence**.

⚠ **`CR-E15` NAMES STATE'S EXHIBIT 32 NOWHERE.** *(Scoped null, run 2026-08-30: `/Exhibit 32/` over `CR-E15` = **0 hits**.)* **The library therefore holds the best-read version of this report and the hearing's designator for it in two files that do not know about each other** — the same cross-folder join failure that hid `DNA-E01 F-14`, and the second instance found in one session.

🛠 **WHAT THE FIRST FORM OF THIS FINDING SAID, AND WHY IT WAS TOO WEAK.** It rested the join on content correspondence plus the court's remark that Exhibit 32 *"has been previously disclosed publicly from an earlier filing"* (`day4.txt` 05:27:20), and stated that identity was *"NOT established… paginated identically"* and that *"no witness was asked."* **Three of those four hedges did not survive the verification pass.**

**THE EVIDENCE AS IT NOW STANDS — five limbs, four of them tested on 2026-08-30:**

1. 🚨 **THE COURT ASKED THE QUESTION DIRECTLY, AND THE PROSECUTOR ANSWERED IT ON THE RECORD.** *"So question for you, **was this the report that was previously disclosed in one of the early motions?**"* — **"Yes."** (`day4.txt` **05:26:42 → 05:26:50**, verified directly here.) ⚠ **It narrows to "an early motion," not uniquely to the bullet-fragment motion — that limb is still an inference.**
2. 🚨 **A PAGINATION FINGERPRINT.** `CR-E15`'s v1.1 pass rendered the motion attachment's pp. 1–4 and tested them against counsel's on-record display instructions: **nine landmarks land exactly** — including *"the last paragraph on this page,"* **which breaks mid-sentence**, and the appendix reached as *"two pages in"* from p. 2 = **p. 4 of 4**. **A four-page document whose page breaks fall where counsel's instructions say they fall is a structural match, not a content resemblance.**
3. **Submission match:** counsel's *"the **submission one** report"* (`day4.txt` 06:25:53) against the attachment's own **Submission(s): 1**.
4. **The motion PDF's CreationDate is 2026-01-09** — the date on the face of the bullet-fragment motion.
5. **The author authenticated Exhibit 32 under oath:** *"Are you the author of this report?"* — *"I am, yes."* (06:25:42–44). ⚠ **"No witness was asked" was therefore true only of the IDENTITY question — the authorship question WAS asked and answered.**

⚠ **THE RESIDUAL IS NOW NARROW, AND IT IS NOT ABOUT IDENTITY.** What remains unestablished is whether the exhibit **as admitted** is **complete and unredacted** relative to the attachment, and whether **further ATF submissions beyond submission 1** exist — counsel's own *"submission one"* implies they might, and the three known ATF bullet/toolmark reports. 🛠 **CORRECTED 2026-08-30 — an earlier form of this was WRONG TWICE. (a) The *Touhy* request names ONE report (the 2025-09-17). The THREE are listed in a DIFFERENT document — Exhibit F to the same filing, defence counsel's letter of 2026-03-25 ¶ 1.3: *"We have received **three** bullet/toolmark examination reports from the ATF: **September 17, 2025** (submission 1), **October 6, 2025** (submission 1), and **February 25, 2026** (submission 1, 4, 6)."* (b) The library **DOES hold one of them** — the 2025-09-17 report is what `CR-E15` read. (c) *"firearms reports"* was this library's paraphrase; the filing says **"bullet/toolmark examination reports."** *(Corrected from `CR-E14`'s end on its v1.3 pass.)* ⚠ **The substantive point survives and is strengthened: three ATF bullet/toolmark reports are known to exist, the hearing admitted two firearms/toolmark exhibits (32 and 34), and the library holds one.** 🛠 **`F-4` is bounded to THE 2025-09-17 FIREARMS REPORT.** *(RE-EXPRESSED 2026-08-30 — an earlier form said "bounded to the ****2025-09-17 firearms report** 🛠 *(re-expressed v1.3 — see the log)***," and **there is no such thing**: see `CR-E21 F-2`. **Both laboratories number by EVIDENCE SUBMISSION, not by report**, and **ATF submission 1 carries at least FOUR reports across three disciplines** — a DNA report, this firearms report of 2025-09-17, a further firearms/toolmark report of 2025-10-06, and a latent print report of 2025-09-15. ⚠ **`F-4` ITSELF SURVIVES UNCHANGED — it rests on the pagination fingerprint, the court's remark and the prosecutor's on-record "Yes," NOT on the submission number** — **but the submission number was never the bound it appeared to be.** ⚠ **GENERAL RULE: cite a laboratory report by DISCIPLINE + DATE + identifier; an identifier alone is ambiguous at both laboratories in this case.**)* **Decisive artifact: State's Exhibit 32 as admitted, compared page-for-page.**

⚠ **CONSEQUENCE, AND IT RUNS TOWARD THE LIBRARY'S CAPABILITY, NOT AGAINST IT:** if the identity holds, **State's Exhibit 32 is the ONE forensic exhibit in this case whose contents this library has actually read**, and `CR-E15`'s findings `F-96`/`F-97`/`F-98` may be read as findings about a hearing exhibit rather than only about a motion attachment. **That promotion is NOT performed here** — it needs `CR-E15`'s own pass.

---

## §5 · FINDINGS

**`CR-E20 F-1`** — "The ATF report" is never sufficient: four ATF reports, splitting two-and-two across DNA/biology and firearms/toolmark, across two evidence groups. **High.**
*What would change it:* nothing on the transcript side; the identifications are verbatim and unambiguous.

**`CR-E20 F-2`** — The library has systematically called State's Exhibit 30 "the ATF firearm report," the natural name for Exhibit 32, and the collision materially obscured `DNA-E01 F-14`. **High.**
*What would change it:* nothing; this is a naming defect established by reading the record against the files.

**`CR-E20 F-3`** — "Exhibit 30" has three referents; a bare use is unsafe. **High.**
*What would change it:* nothing.

> ⚠ 🚨 **AND THE TWO FILES DISAGREE ON THIS GRADE — DECLARED, NOT SMOOTHED.** `CR-E20` (here) holds **IDENTITY: High**; **`CR-E15 F-139` — written by the pass that actually READ the document — deliberately holds it at Medium-high** and says in terms that it is *"NOT RAISED HERE."* ⚠ **The disagreement is an artefact of parallel passes, not of the evidence: `CR-E15`'s own pass SURFACED the pagination fingerprint and the court exchange that justify High, then held its file at the grade it had been briefed with, while this file was re-graded on that same evidence an hour later.** ⚠ **`CR-E20` is the finding's home and is canonical for the grade; `CR-E15` should POINT here rather than restate it** *(the same discipline as the register ceiling)*. **Until that pointer is written, any file citing `F-4` must carry BOTH grades and say which file it is following. Neither file may be cited as having settled it alone.**

**`CR-E20 F-4`** — `CR-E15`'s ATF firearms report **is** State's Exhibit 32; the two were never joined until 2026-08-30. **ANCHOR: High · IDENTITY: High** *(⚠ `CR-E15` holds Medium-high — see the box above)* 🛠 *(re-graded from Medium-high the same day, on a pagination fingerprint, the prosecutor's on-record "Yes" to the court's direct question, a submission-number match and the motion PDF's creation date — §4)*. ⚠ **Bounded to the **2025-09-17 firearms report** 🛠 *(re-expressed v1.3 — see the log)*; the residual is completeness and redaction, NOT identity.**
*What would change it:* State's Exhibit 32 as admitted, compared page-for-page against the motion attachment; and the other two ATF bullet/toolmark reports named in the defence's Exhibit F letter, neither of which is held.

---

## §6 · OPEN ITEMS AND ACQUISITION TARGETS

1. **State's Exhibit 30, pp. 2–4 (item table) and p. 8 (consumption page)** — would settle ATF items 1.7, 1.8, 1.10, 1.12, 4.1, 7.1 and 8.1, and whether the item series closes at 1.13. *(`DNA-E01 F-14`, `F-16`, `F-17`.)* **P1.**
2. **State's Exhibit 32 as admitted** — would settle `F-4` and, if identical to the motion attachment, promote `CR-E15`'s findings to hearing exhibits. **P1.**
3. **State's Exhibit 31** — would settle the *"Mauser or rifle"* rendering, the FBI item descriptions, and whether items 7-1 and 8-1 were consumed *(`DNA-E01 F-20`)*. **P1.**
4. **State's Exhibits 33 and 34** — the consumption status of ATF items 15.1 and 18.1 is **not on this record at all**. — *(checkable)*
5. **The three ATF bullet/toolmark reports named in the defence's Exhibit F letter (2026-03-25 ¶ 1.3)** recorded at `CR-E14` §8.1 🛠 *(v1.2: NOT the Touhy request, which names one — see §4)* — whether they map onto Exhibits 32 and 34 plus one unheld third is **unverified**. ⚠ **Note the tension this raises and do not resolve it here: this hearing produced FOUR ATF reports, of which only TWO (32 and 34) are firearms/toolmark. A filing naming THREE firearms reports either counts differently, or reaches a report not entered at this hearing.** — *(checkable)*
6. **The court's exhibit list as filed** — would test §2's completeness null against something other than what was spoken aloud. — *(checkable)*

---

## §7 · WHERE THE UNDERLYING EVIDENCE LIVES — pointers, not findings

| Material | Lives in |
|---|---|
| All DNA items, likelihood ratios, consumption, the conditioning finding | **`DNA-E01`** |
| The ATF firearms report read at Tier 1 (= Exhibit 32, per `F-4`) | **`CR-E15`** |
| Karner's Day-4 firearms/toolmark testimony | **`CR-E01`** |
| Day-4 Faumuina/Davis, the exhibit admissions | **`CR-E02`** |
| Both DNA analysts read end to end | **`CR-E06`** |
| The complete friction-ridge record and the print null | **`CR-E19`** |
| Speaker labels and name reconciliation | **`CR-E16`** |

---

## §8 · RESIDUAL — what this file did NOT do

1. ⚠ **NO EXHIBIT WAS READ.** This file maps designators to descriptions; it verifies **no content**.
2. **It did not re-verify any DNA statistic, item description, consumption entry, toolmark conclusion or print result.** Those live in the files at §7 and govern.
3. **It did not renumber, rename or edit any other file.** The corrective pass across the library is a separate act, and until it lands **the collision is live in every file listed at §3**.
4. ⚠ **It did not PROMOTE `CR-E15`'s findings.** `F-4` is now graded High on identity, so `CR-E15`'s `F-96`/`F-97`/`F-98` **may** be read as findings about a hearing exhibit rather than only about a motion attachment — **that promotion is available and is deliberately NOT taken here.** It belongs to `CR-E15`'s own pass, and the completeness/redaction residual at §4 must be carried with it.
5. ⚠ **MUTUAL PROVISIONAL DEPENDENCY, DECLARED:** `CR-E15` v1.1 now depends on this file for `F-4`, and this file is `[PROVISIONAL]`. **Neither file can clear the other.** An independent cycle must clear both.
6. **No register entry is assigned, moved or resolved.** `QUEUE.md`'s ceiling line is the single source of truth and is not restated here.
7. ⚠ **`[PROVISIONAL]`** — no verification cycle has run; nothing here may resolve a register entry.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-08-30** | **Initial file.** 🚨 **Created because the library has been calling State's Exhibit 30 "the ATF firearm report" — which is the natural name for State's Exhibit 32 — and because "Exhibit 30" turns out to have THREE referents.** **The canonical map at §2 is built from five verbatim on-record identifications**, each located: **30** = ATF **DNA** report on the rifle and ammunition (`day4.txt` 05:18:35); **31** = the **FBI** DNA report carrying the towel and the screwdriver (`day2.txt` ~05:05); **32** = ATF **firearms/toolmark** report, **which is where the test fires and ATF designator 1.11 live** (05:26:25); **33** = ATF **biology** report on the Dremel and the cartridge cases from atop the safe (05:32:33); **34** = ATF **toolmark comparison** report, the 15A engraving cutter (05:36:19). **Plus the defence's "Baker Exhibit 30," a NIST publication** (`day5.txt` 01:35:11) — **a third referent for "Exhibit 30."** 🚨 **`F-1`: there are FOUR ATF reports and they split two-and-two across DNA/biology and firearms/toolmark, so "the ATF report" is NEVER a sufficient designation** — and **Exhibits 30 and 32 were admitted eight minutes apart, through the same witness, about the same rifle, in nearly identical words, the only discriminator being the absence of "DNA testing."** **`F-2`: the collision materially obscured `DNA-E01 F-14`**, whose whole force is that 1.11 arrives from a *different report* than the consumption lists — invisible while both were called "the ATF firearm report." **Five writing rules imposed at §3.** 🚨 **`F-4` — A SECOND CROSS-FOLDER JOIN FAILURE FOUND IN THE SAME SESSION: `CR-E15` read the ATF firearms report at Tier 1 from a court filing and NAMES STATE'S EXHIBIT 32 NOWHERE** *(scoped null: `/Exhibit 32/` over `CR-E15` = 0)*. **If the identity holds, Exhibit 32 is the ONE forensic exhibit in this case whose contents this library has actually read** — ⚠ **graded SPLIT (anchor High, identity Medium-high) and expressly NOT promoted here**, because the exhibit as admitted has not been compared against the motion attachment and no witness was asked. **`[PROVISIONAL]`; no exhibit read; no register entry assigned, moved or resolved; the ceiling is pointed at, never restated.** |

| **1.1** | **2026-08-30** | **Same-day extension after the corrective sweep reported back — logged as a version rather than folded silently into v1.0, because `CR-E15` v1.1 began depending on this file in the interval.** 🚨 **`F-4` RE-GRADED: IDENTITY Medium-high → High.** The upgrade was earned by verification acts on `CR-E15`'s pass, not by re-reading my own reasoning: **(a)** the court asked the question directly and the prosecutor answered on the record — *"was this the report that was previously disclosed in one of the early motions?"* — **"Yes."** (`day4.txt` 05:26:42→05:26:50); **(b) a PAGINATION FINGERPRINT** — nine of counsel's display instructions land exactly on the motion attachment's pp. 1–4, including one that breaks **mid-sentence** and an appendix reached as *"two pages in"* = p. 4 of 4; **(c)** counsel's *"the submission one report"* against the attachment's **Submission(s): 1**; **(d)** the motion PDF's CreationDate **2026-01-09**. ⚠ **Three of v1.0's four hedges did not survive** — in particular *"no witness was asked"* was true only of the IDENTITY question; **the author authenticated Exhibit 32 under oath.** **The residual is now narrow and is about COMPLETENESS AND REDACTION, not identity**, and `F-4` is **bounded to the submission-1 report** — counsel's own *"submission one"* implies others, and three ATF bullet/toolmark reports are known to exist and the library holds one — 🚨 ⚠ **AND IT CANNOT BE RESOLVED FROM THE TRANSCRIPTS: no ATF report DATE and no ATF case number appears anywhere in `day1`–`day5`** *(scoped null run 2026-08-30 across `2025-W`, `000401`, `W-0004`, `date of report`, `report dated` and every candidate date; every hit opened, including a date trap — a search warrant "initially filed on September 17th")*. **Neither Exhibit 32 nor Exhibit 34 was ever dated on the record, and no witness was asked.** ⚠ **At least one of the three reports has no counterpart among the hearing exhibits — a NON-CORRESPONDENCE, not a discrepancy, with innocent readings available and none excluded. No inference of withholding is drawn or licensed.**. ✅ **BOTH-DIRECTIONS RESULT ADDED AND GIVEN EQUAL PROMINENCE: the `DNA-E01` audit classified all 54 case-insensitive "Exhibit 30" references and found ZERO mis-citations of Exhibit 32's content to Exhibit 30.** **The defect was NAMING, not mis-citation** — right number, right content, wrong report name — **so no substantive finding moved anywhere.** 🆕 **TWO ANCHORS ADDED, one decisive:** Exhibit 30's own first page carries a **"DNA Analysis section"** (`day4.txt` 05:20:17); and 🚨 **THE COURT NAMED BOTH EXHIBITS IN ONE SENTENCE FROM THE BENCH** — *"as it relates to State's Exhibit 30, which was admitted, as well as State's Exhibit 32, which is admitted"* (`day4.txt` **06:36:35**) — **previously unrecorded anywhere in this library, and the strongest single line establishing that 30 and 32 are two distinct admitted exhibits.** 🆕 **§2 COMPLETENESS NULL ADDED:** `/Exhibit (29|3[0-9])/` over all five days shows the run **30·31·32·33·34 unbroken and closed at both ends** — no Exhibit 29/36/37/38 exists, and **Exhibit 35 is a MAP, not a laboratory report**, which is why it sits adjacent to 30 in the transcript. ⚠ **Scoped to what was spoken aloud, NOT to the exhibit list as filed.** 🆕 **§3a ADDED — a party told the court Oliver's reports were "exhibits 30 and, I believe, 34,"** which cannot be right on this map (34 is the toolmark comparison; the ATF biology report is 33). ⚠ **NOT resolved: nothing establishes Oliver authored Exhibit 33, and THE SPEAKER IS NOT ESTABLISHED** — Rev labels it McBride but the content self-corrects mid-sentence and the turn order is irregular, so per this library's standing rule the attribution is left open. **§8 residual renumbered; mutual provisional dependency with `CR-E15` declared.** **No register entry assigned, moved or resolved; the ceiling is pointed at, never restated.** |

| **1.2** | **2026-08-30** | 🛠 **THIS FILE'S OWN *TOUHY* CLAIM WAS WRONG TWICE AND IS CORRECTED AT ALL FOUR SITES.** It read that *"the **Touhy** request… names three ATF firearms reports, none of which this library holds."* **(a) The *Touhy* request names ONE** — the 2025-09-17 report. **The THREE are in a different document:** Exhibit F to the same filing, defence counsel's letter of **2026-03-25 ¶ 1.3** — *"three **bullet/toolmark examination reports** from the ATF: September 17 2025 (submission 1), October 6 2025 (submission 1), and February 25 2026 (submission 1, 4, 6)."* **(b) The library DOES hold one of them** — the 2025-09-17 report is precisely what `CR-E15` read, which is this file's own `F-4`. **(c)** *"firearms reports"* was the library's paraphrase, not the filing's phrase. ⚠ **Found and corrected from `CR-E14`'s end by the pass that read the filing; the substantive point SURVIVES AND IS STRENGTHENED.** 🚨 **AND THE MAPPING CANNOT BE RESOLVED FROM THE TRANSCRIPTS AT ALL: no ATF report date and no ATF case number occurs anywhere in `day1`–`day5`** *(scoped null; every hit opened, including a date trap — a search warrant "initially filed on September 17th")*. **Neither Exhibit 32 nor Exhibit 34 was ever dated on the record and no witness was asked.** ⚠ **At least one of the three reports has no counterpart among the hearing exhibits — recorded as a NON-CORRESPONDENCE, not a discrepancy; innocent readings available, none excluded, NO inference of withholding.** 🚨 **GRADE DISAGREEMENT WITH `CR-E15` DECLARED RATHER THAN SMOOTHED.** This file holds `F-4` IDENTITY at **High**; **`CR-E15 F-139` — written by the pass that actually READ the document — deliberately holds Medium-high.** ⚠ **The split is an artefact of parallel passes, not of the evidence:** `CR-E15`'s pass surfaced the pagination fingerprint and the court exchange that justify High, then held its own file at the briefed grade while this file was re-graded on that same evidence an hour later. **`CR-E20` is the finding's home and canonical for the grade; `CR-E15` should POINT here rather than restate — the same discipline as the register ceiling. Until that pointer is written, any file citing `F-4` must carry BOTH grades and say which it follows.** |

| **1.3** | **2026-08-30** | 🛠 **`F-4`'s BOUND RE-EXPRESSED, on a finding from the new `CR-E21`.** It read *"bounded to the **submission-1 report**"* — **and there is no such thing.** **Both the FBI and the ATF number by EVIDENCE SUBMISSION, not by report:** ATF **submission 1 carries at least four reports across three disciplines** (DNA; the 2025-09-17 firearms report; a further firearms/toolmark report of 2025-10-06; a latent print report of 2025-09-15), and **FBI Lab No. `2025-01779-5` carries BOTH a latent print report and a questioned-documents report on two different dates.** ✅ **`F-4` SURVIVES UNCHANGED** — its identity grade rests on the pagination fingerprint, the court's remark and the prosecutor's on-record "Yes", **never on the submission number** — **but the phrase was not the bound it appeared to be**, and is now written as **"the 2025-09-17 firearms report."** ⚠ **GENERAL RULE ADDED: cite a laboratory report by DISCIPLINE + DATE + identifier. An identifier alone is ambiguous at both laboratories in this case.** ⚠ **Scope: one phrase re-expressed and one rule added. Nothing else re-verified; `[PROVISIONAL]` not cleared; no register entry assigned, moved or resolved.** |

*End of file.*
