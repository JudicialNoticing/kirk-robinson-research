# CR-E16 — Who is who: the verified participant roster, and the transcript-label reconciliation it exists to enable

**File ID:** CR-E16 · **Scope:** every identified participant in the case — bench, prosecution, defence, victim's counsel, media counsel, investigators, forensic examiners, testifying witnesses, and officials who spoke publicly — verified against held primary sources, with role, office and first appearance. **Executes Q-96.** ⚠️ **Its operational purpose is §10: this library reads machine transcripts whose speaker labels are demonstrably unreliable, and a verified roster is what makes the standing "infer from content" rule usable.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

⚠️ **Findings `[PROVISIONAL]`** → **Q-139**.

> ### ⚠️ §0.1 · PROVISIONAL DEPENDENCIES
> ✅ **This file depends on no other provisional file.** Every entry was verified directly against a primary artifact, a docket printout read in Python, or a transcript. **Clearing item: Q-139.**

---

## §0 · Rules this file is written under

🚨 **ROLES AND FACTS ONLY. No characterisation, no criticism, and no adverse inference attaches to any named person anywhere in this file.** This library had to **retract a finding that named a living attorney beside an adverse judicial finding** under three disclaimers — and the inference *was* the finding. **The test: strip the guards and read the sentence alone. If what remains is an argument about a named living person, it does not belong here.**

🚨 **CASE POSTURE: Tyler James Robinson has NOT been bound over for trial. The presumption of innocence applies throughout.** ⚠️ **And the reason is now precisely stated: the preliminary hearing is not finished** — 2026-07-06→07-10 were five days **of evidence**, and **2026-09-01 is described on the record as *"the last day of the preliminary hearing."***

**Two people are deliberately unidentified and stay that way:**
- **`[Dpty Atty]`** — a Deputy Utah County Attorney **whom the State itself redacted** from a public filing. ⚠️ **No attempt was made to identify him, and the field was NOT narrowed by elimination. The six-name signature block at §2a is not a candidate list.**
- **`H.G.`** — a witness **the court identified only by initials.** ⚠️ **No attempt was made to resolve them, and no search was designed to.**

**Private individuals are out of scope by rule** — family members, the roommate, eyewitnesses, elimination-sample donors, the juvenile witness, and Rule 1102 written-statement declarants. Where the case turns on them, only the role appears, never identifying detail. **That is a scope choice, not a completeness claim.**

**Sourcing:** **Tier 1** — sworn testimony and primary filings · **Tier 2** — named official statements · **Tier 3** — named journalism · **Tier 4** — anonymous/low-verification. **Every grade below traces to a verification act performed for this file, never inherited.**

---

## §1 · The bench

| | Name · role | First appearance | Confidence |
|---|---|---|---|
| **B-1** | **Hon. Tony F. Graf, Jr.** — assigned trial judge | **2025-09-16**, and presided at the initial appearance the same day | High |
| **B-2** | **Hon. Shawn R. Howell** — signed the **Order to Hold Without Bail** | **2025-09-12, 08:40:00** — **four days before the Information was filed** | High |
| **B-3** | **Justice Jill M. Pohlman**, Supreme Court of Utah — **denied the petition for permission to appeal an interlocutory order** | **2026-01-02, 09:17:30**, No. **20251388-SC** | High |

🚨 **The hold order carries NO case number** — searched both readings, zero hits for `251403576` and for `Case No`. It is identified only by a **Probable Cause ID** and a **Submission ID**, and rests on the affirmation of the arresting officer (**I-1**). ⚠️ **This is the artifact that makes the bare case number insufficient to identify the case: it predates the number** *(and see CR-ACQ-2026-08-16 F-41 — the number is not unique in Utah either)*.

**Court staff, recorded because their names occupy transcript and minute-entry labels:** a District Court Clerk who countersigns orders; a clerk appearing once at the initial appearance under a login-style string *(name not established — **Low**)*; and two certified court reporters, one covering the 2025-10-24 sealed hearing and two 2026 hearings, the other three 2025–26 hearings.

---

## §2 · Prosecution — and the two lists that answer different questions

⚠️ **The signature block and the counsel-of-record block DIFFER, and conflating them produces a wrong answer to a real question.** The **signature block** answers *who put their name and bar number on the State's filings*. The **counsel-of-record block** answers *whom the court's own case-management system recognises as appearing for the plaintiff*.

### 2a · The signature block — six names, unchanged across every State filing

Verified identical from the 2025-09-16 Information through the 2026-02-02 filings:

| | Name | Bar no. | Title | First appearance |
|---|---|---|---|---|
| **P-1** | **Jeffrey S. Gray** | 5852 | **Utah County Attorney** (elected) | Swore the Information **2025-09-16** |
| **P-2** | **Chad E. Grunander** | 9968 | Deputy; **Chief Deputy** | **2025-09-16** — the only prosecutor present at the initial appearance |
| **P-3** | **Ryan McBride** | 13079 | Deputy; **General Crimes Division Chief** | 2025-09-29 |
| **P-4** | **Lauren Hunt** | 14682 | Deputy; **special victims** | 2025-09-29 |
| **P-5** | **David Sturgill** | 7995 | Deputy | Signature block **2025-09-16**; examined witnesses on Days 1–2 |
| **P-6** | **Christopher D. Ballard** | 8497 | Deputy; **General Counsel & PIO** → **Chief of Staff** | 2025-09-29 |

### 2b · The counsel-of-record block — **four** names

The court's own record lists **Gray · Ballard · Grunander · McBride**.

🚨 **F-102 — The delta is real and it runs both ways. Confidence: High.**
- **P-4 is NOT in the counsel-of-record block** — yet appears in three minute-entry `PRESENT` blocks and conducted a direct examination on Day 3.
- **P-5 appears NOWHERE in either docket printout** — a case-insensitive scan of the full 1,817-line history returns **zero**. He nonetheless signs **every** State filing, appears in the 2025-10-24 appearance block, and **the judge addresses him by name 38 times on Day 1.**

⚠️ **So *"is X a prosecutor of record?"* and *"is X on the State's papers?"* are different questions with different answers, and the second set is larger.**

### 2c · `[Dpty Atty]` — the deputy the State redacted

**P-7.** What the held record establishes: a deputy county attorney contacted a UCAO investigator seeking a sight-line measurement, having stated he intended to disclose a fact to defence counsel; the two travelled to the campus on **2025-09-30**. **His name and the relationship term are redacted throughout**, in the State's own public filing and in the defence's. 🚨 **He stays redacted. §2a is not a candidate list.**

---

## §3 · 🚨 The same office, a second capacity — "UCAO" does not mean "prosecution"

**F-103 — The Utah County Attorney's Office appeared in this case in a second, separate capacity, for a different client, and said so on the record. Confidence: High.**

**C-1 — an attorney of the same office, at the same address, appeared for the *Utah County Sheriff's Office* — a non-party** — at the 2025-10-24 sealed hearing. His words:

> *"The sheriff's office wants to make it clear that they are **not entering an appearance in this case and they do not intend to ever enter an appearance in this case**."*

Corroborated documentarily: a defence filing attaches prosecution correspondence stating *"our **Civil Division, who represents the Sheriff's Office**, is going to be responding for the State."* ⚠️ **The Civil Division has its own chief, distinct from the trial team.**

**C-2 — a second, distinct non-appearance, easy to conflate with the first.** At the 2025-09-16 initial appearance an attorney appeared *"on behalf of the county"* and addressed the court on the appointment of Rule 8 counsel; the minute entry records that he **"does not enter an appearance in this case."** ⚠️ **The minute entry names no office or division, and none is inferred here.**

---

## §4 · The Utah Attorney General — four capacities, and counsel in none

🚨 **F-104 — Scoped null, verified first: NO attorney from the Utah Attorney General's Office appears as counsel anywhere in the held record.** Searched `Attorney General` across all 63 banked `.txt` artifacts **under both readings**, every hit opened, plus both docket printouts read in full. **Not in the counsel-of-record block, not in any `PRESENT` block, not in any signature block.** **Confidence: High** — the search space would necessarily contain such an appearance. ⚠️ **It does not extend to filings this project does not hold.**

| | Capacity | Establishing fact |
|---|---|---|
| **A-1** | **Coordination partner named by the County Attorney** | *"I have also been coordinating with Utah Attorney General Derek Brown and officials at the United States Attorney's Office"* (Tier 2, 2025-09-10) |
| **A-2** | 🚨 **PRIOR EMPLOYER of two members of the trial team** — **the capacity most easily mistaken for an AG appearance** | Their own office biographies record long prior AG service. ⚠️ **Tier 2, and this project has verified none of the biographical claims inside those documents. Past employment is not present appearance.** |
| **A-3** | **Statutory referral destination — requested, opposed, DENIED** | Defence moved for referral under Utah Code § 17-68-304; the State opposed; **2026-02-03: *"Court denies the motion and request for referral to the Attorney Generals' Office."*** |
| **A-4** | **Named official present at a State press conference** | *"our attorney general, Derek Brown, who is standing behind me today"* (Tier 2, 2025-09-16) |

⚠️ **A fifth apparent appearance, flagged and NOT counted.** The probable-cause submission block carries an agency-identifier-style code followed by the words *"Attorney General."* **Which office it denotes, and which form field it belongs to, could not be established** — the two-column form flattens on extraction. **Confidence: unverified.** Recorded so a later reader does not encounter it and treat it as an appearance.

---

## §5 · Defence

| | Name · bar no. | First appearance |
|---|---|---|
| **D-1** | **The Public Defender** *(the docket renders the entity "DEFENDER PUBLIC")* — appointed on an indigency finding | **2025-09-16** |
| **D-2** | **Kathryn N. Nester**, UT 13967 — **lead counsel** | Rule 8 declaration 2025-09-25; first minute entry 2025-09-26 |
| **D-3** | **Staci Visser**, UT 14358 | Signature block by 2025-10-21; first minute entry 2025-10-28 |
| **D-4** | **Richard G. Novak** — ***pro hac vice*** | Order admitting **signed 2025-09-27**; first in court 2025-09-29 |
| **D-5** | **Michael N. Burt** — ***pro hac vice*** | Order admitting **signed 2025-09-26** — **one day before D-4's** |

⚠️ **The supplemental exhibits for both admissions were filed 2025-09-28 — *after* both orders.** The court made its Rule 8 finding on the record on 2025-09-29. **Composition is unchanged through the last held filing.**

---

## §6 · Victim's side · Media counsel

**V-1 / V-2 — victim's counsel filed on 2025-09-16**, the same day as the Information. ⚠️ **Ten months earlier than this library previously understood.** **Erika Kirk** was **requested** as designated victim representative that day and **granted on the record 2025-12-11**. ⚠️ *That is a status, not a professional role.* ⚠️ **The signature block's layout does not state which attorney holds which firm affiliation, and none is inferred.**

**M-1 … M-4 — media counsel for the intervenor group.** ⚠️ **None is a party.** The court **denied** intervention on 2025-12-29 and entered a standing notice order instead; on 2026-02-23 it granted the media's motions to amend that order and for **attorneys'-eyes-only access to closure motions**. One of the four appears **only in a service list** — no appearance found (**Medium-high**).

**Pool camera operators and still photographers sworn to the decorum order** are recorded in §10's source material because they occupy speaker labels.

---

## §7 · Investigators and forensic examiners

| | Name · office · role |
|---|---|
| **I-1** | **Brian Davis** — State Bureau of Investigation; **arresting officer**; **swore the probable-cause affidavit**; co-lead case agent |
| **I-2** | **David Hull** — DPS/SBI Major Crimes; **lead case agent**; testified at the disqualification hearing and on Days 1–2 |
| **I-3** | **Jennifer Faumuina** — DPS/SBI **Sergeant**, oversaw the crime scenes; routed items to the FBI and ATF laboratories |
| **I-4** | **Cole Christensen** — **UCAO Bureau of Investigations** Special Agent; **swore the sight-line affidavit** ⚠️ *headed "Special Agent", signed "Sgt." — both preserved* |
| **I-5** | **Christopher Bagley** — Spanish Fork Police Department; **first State witness** |
| **I-6** | **Amanda Bakker** — **FBI Laboratory, DNA Casework Unit**, Quantico; **author of the FBI DNA report** |
| **I-7** | **Samantha Karner** — **ATF Forensic Science Laboratory**; Firearm and Toolmark Examiner; **author of the report at CR-E15** |
| **I-8** | **Caitlin Oliver** — **ATF DNA Section Chief**; **author of three ATF DNA reports** |
| **I-9** | **Dr. Guajardo** — Utah Medical Examiner's Office; conducted the autopsy *(**Medium-high** — surname spelled aloud by a witness who prefaced it "I believe is how it's pronounced"; the report is not held)* |
| **I-10** | An **FBI Special Agent** named only by surname in a communication log read aloud *(**Medium**)* |

🚨 **F-105 — All three laboratory examiners who authored the State's forensic exhibits were called to the stand BY THE DEFENCE. Confidence: High.** Recorded as a structural fact about the hearing, without comment.

**Chain of custody as testified:** rifle → FBI custody → **ATF laboratory**; towel and screwdriver → **FBI laboratory**.

---

## §8 · Testifying witnesses, by day

| Day | Witness | Called by | Direct by |
|---|---|---|---|
| 1 | **Bagley** (I-5) | State | Grunander |
| 1 | **Hull** (I-2) | State | McBride, then **Sturgill** |
| 2 | **Hull**, continued | — | Sturgill; **cross Nester** |
| 2 | **Faumuina** (I-3) | State, **limited purpose, testimony paused** | McBride |
| 2 | **Bakker** (I-6) | 🚨 **Defence, out of order** | Burt |
| 3 | **Davis** (I-1) | State | **Hunt** |
| 4 | **Davis**, continued · **Faumuina** recalled · **Karner** (I-7) | State · State · 🚨 **Defence** | Hunt · McBride · Burt |
| 5 | **Oliver** (I-8) | 🚨 **Defence** | Burt |

**At the 2026-02-03 disqualification evidentiary hearing** *(from the court's minute entry — the transcript is NOT held)*: **P-1 testified**, called by defence counsel and **cross-examined by his own deputy**; **H.G.** testified, called by defence; **P-2 testified**, called by defence; and **I-2** testified, called by the State. 🚨 **H.G. stays H.G.**

⚠️ **A recorded interview of a private individual was played on Day 4. It is a played recording, not live testimony, and he is outside this roster by rule.**

⚠️ **Hearing DATES are not established.** Rev's article dates are **publication** dates; the held docket stops at 2026-03-15 with the hearing then set for May. **Day numbering is reliable; calendar dates are not.**

---

## §9 · Officials speaking publicly — the four newly banked transcripts

⚠️ **Tier 2 as to the officials. Reporters' questions in them are Tier 3, and a premise inside a question is not evidence of anything.** ⚠️ **Rev's page titles assert conclusions this project does not adopt.** ⚠️ **Speaker labels in these four are mostly generic — every name was read from CONTENT.**

- **2025-09-10, the day of the shooting** — the **Commissioner of Utah DPS**; the **FBI Special Agent in Charge, Salt Lake**; a **Vice President of the university**; the **Governor**; the **university Police Chief**.
- **2025-09-11** — the **DPS Communications Director**, the Commissioner, and the FBI SAC.
- **2025-09-12, the arrest announcement** — the **Governor** and the **Director of the FBI**. ⚠️ **A speaker self-identifies "as the sheriff" but is NOT named in that transcript** and carries the same generic label as the master of ceremonies; the name is **not** resolved here *(**Medium** as to role, unestablished as to name)*.
- **2025-09-16, the charging press conference** — a **county communications manager** and **P-1**, who announces the seven counts and the death-penalty notice.

🚨 **F-106 — The charging press conference independently corroborates §2a: the elected County Attorney introduces his trial team on the record**, naming his two chief deputies, the General Crimes chief, a special-victims prosecutor and the deputy "handling motions." ⚠️ **And he refers to P-4 as "she"** — directly relevant to §10's "Mr. Hunt" entries.

---

## §10 · 🚨 THE TRANSCRIPT-LABEL RECONCILIATION — the reason this file exists

**Standing rule: infer every speaker from content; where label and content disagree, content wins.** Here is the roster applied to it.

**F-107 — Four label failures are demonstrated, not theorised. Confidence: High.**

1. 🚨 **A police officer's sworn testimony is credited to defence counsel.** On Day 1 the witness's own answer — *"[name]. B-A-G-L-E-Y … employed with the Spanish Fork Police Department"* — **carries the label of defence counsel (D-4)**, while the questioner carries a prosecutor's label.
2. 🚨 **One prosecutor's label covers another prosecutor for hundreds of turns.** On Day 1 the label for **P-3** covers the prosecutor **the judge repeatedly addresses as "Mr. Sturgill" (P-5)** — verified at five separate timestamps. **Mislabelled is not unlabelled.**
3. 🚨 **The same label covers OPPOSING counsel in adjacent turns.** On Day 5 the judge says *"Thank you, Mr. McBride. **To the media**"* — and the next turn, still labelled with the prosecutor's name, says *"Appreciate the opportunity to be here to speak **on behalf of the media**."*
4. 🚨 **The oath is attributed to defence counsel.** On Day 1 both witness oaths carry **lead defence counsel's** label; the identical function is labelled `Bailiff` on Day 4.

**F-108 — Two failures are in the COURT'S OWN RECORD, not the transcription vendor's. Confidence: High.**
- 🚨 **A media attorney is listed as `Prosecutor:` in a 2026-02-24 minute entry**, in the same block as four actual prosecutors — while an earlier entry lists him correctly under *"Other Attorneys."*
- 🚨 **A minute entry renders defence counsel's surname as "Bury."**

**F-109 — "Hunt" is undecidable from a label alone, and the record contains an unresolved conflict. Confidence: High as to the conflict.** **Two people, opposite sides**: a Deputy Utah County Attorney (**P-4**, whom the elected County Attorney calls *"she"*) and **media counsel (M-1)**. Two minute-entry narratives read **"Mr. Hunt"** — one where the `PRESENT` block lists **the prosecutor and no media attorney at all**, another where **no Hunt of any kind is listed.** ⚠️ **The conflict is recorded as a fact about the record and deliberately NOT resolved.**

**F-110 — A prosecutor's surname occupies the WITNESS-ANSWER position. Confidence: High.** At two 2026 hearings the minute entries record defence counsel **calling P-1 and P-2 as witnesses**. ⚠️ **A search that assumes those surnames mark questioners will invert those passages.**

### Garble-normalisation list

**Carried forward:** *"Bury"* → **Burt** · *"Erica"* → **Erika**.

**✚ New:** *"Nestor"* → **Nester** *(all five days — ⚠️ and **a State signature block in the held corpus itself reads "Nestor"**, so the misspelling is not only the vendor's)* · *"Baker"* → **Bakker** · *"Holt"/"Hall"* → **Hull** · *"Burke"* → **Burt** · *"Ryman"* → **Reymann** · *"Falmina"* → **Faumuina** · *"Carner"* → **Karner** · *"Nyman"/"Dyer"* → **Neiman** *(role-based inference from self-identified function, **Medium-high**)* · *"Bayliff"* → **Bailiff**.

**In the press-conference transcripts:** *"Rob/Robert Bowles"* → **Bohls** · *"Charlie Cook"* and *"Kurt"* → **Kirk** · *"130 tests"* → **tips**.

**In the court record and docket, not the vendor's:** the surname-first `GRUNANDER, CHAD`; *"DEFENDER PUBLIC"*; a transcript caption reading **"IN AND FOR PROVO COUNTY"** *(the county is Utah; Provo is the city)*; and a victim's-side filing **dated January 2026 whose certificate of delivery certifies September 2025** — an internal conflict recorded, not resolved.

---

## §11 · Scoped nulls

**No Utah AG attorney as counsel** (§4, High) · **P-5 appears nowhere in either docket printout** — zero occurrences, verified by direct read rather than `grep` · the referent of the *"Attorney General"* agency code — **unverified** · given names of the FBI examiner at I-10 and of I-9 — **not stated** · the master of ceremonies at the first press conference — **unnamed** · the sheriff's name at the arrest announcement — **not stated in that transcript** · **no media-counsel signature block is banked** · one media attorney has **no appearance found** · the names of a supervising lieutenant and of a digital-forensics analyst — **not stated** · **no certified transcript of the 2026-02-03 hearing is held.**

---

## §12 · Residual scope

**Bar numbers were taken from the parties' own signature blocks and were NOT verified against the Utah State Bar roll** — nobody has performed that act, and no grade above rests on it. **The prosecutors' biographies are Tier 2 and were used only for titles and office**; none of their biographical claims is verified. **The transcripts are commercial renderings, not certified.** **First-appearance dates are the earliest occurrence in the HELD record**, and six appearance-of-counsel filings are unattributed in the docket, so an earlier one may exist inside them. **The 2025-10-24 transcript is the court-filed REDACTED version.**

⚠️ **Two artifacts in the folder belong to OTHER CASES and contain other people's names** — a South Carolina criminal filing and an unrelated civil complaint. **None of those names is in this roster, and a name-search across the artifact folder will surface them.** Flagged so no later reader mistakes them for participants.

**This file establishes WHO, not what they said.** No testimony content, exhibit numbering, statistic or conclusion in CR-E01–E15 was re-verified here.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-96 executed.** F-102 → F-110 opened. **The operational payload is §10: four transcript-label failures demonstrated rather than theorised** — a police officer's sworn testimony credited to defence counsel; one prosecutor's label covering another for hundreds of turns; a single label covering **opposing** counsel in adjacent turns; and the oath attributed to defence counsel. 🚨 **Two further failures are in the COURT'S OWN RECORD** — a media attorney listed as `Prosecutor:`, and a defence surname garbled — **so the docket is not a safe check on the transcript.** **F-109 records an unresolved "Mr. Hunt" conflict and deliberately leaves it unresolved.** **F-102: the signature block (six) and the counsel-of-record block (four) differ both ways.** **F-103: the same office appeared for a non-party client and said so on the record — "UCAO" does not mean "prosecution."** **F-104: no Utah AG attorney is counsel anywhere in the held record, though the office appears in four other capacities.** **F-105: all three laboratory examiners who authored the State's forensic exhibits were called by the DEFENCE.** ⚠️ **`[Dpty Atty]` and `H.G.` stay unidentified; private individuals are out of scope by rule.** `[PROVISIONAL]`. |
