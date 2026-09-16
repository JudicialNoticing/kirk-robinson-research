# SEC-E01 — The security posture at the UVU event of 2025-09-10: what the record establishes, and what it does not

**File ID:** SEC-E01
**Scope:** the law-enforcement and private-protective arrangement in place at Charlie Kirk's outdoor event at Utah Valley University on **2025-09-10**, and the professional conduct of personnel **acting in a public capacity** that day. Built from the sworn preliminary-hearing record, the State's charging documents, a State proffer, and named officials' contemporaneous public statements. **This file is about an arrangement and a public question. It is not about any individual private person.**
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo.
**Prepared:** 2026-08-17 · **Status:** **v1.1 · `[PROVISIONAL]`** — no independent verification cycle has run on this file.

> 🚨 **CASE POSTURE, VERIFIED 2026-08-17. TYLER ROBINSON HAS NOT BEEN BOUND OVER.** The preliminary hearing is **UNFINISHED**: 2026-07-06 → 07-10 were five days **of evidence**; **2026-09-01 is its last day — ARGUMENT ONLY, on a closed evidentiary record.** The hearing did **not** "conclude" on 07-10. **The presumption of innocence is absolute.**
> 🛠 **Posture updated 2026-09-16 (owner's ruling).** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full. *The sentence above is retained as written, true as of its date; the ruling is `START-HERE` §0AH item 4 and `DOCKET-WATCH.md` v2.6.*
>
> 🚨 **NO MEMBER OF MR. KIRK'S SECURITY TEAM IS ACCUSED OF ANYTHING BY ANYONE.** No charge, no filing, no investigative finding and no official statement in this library's holdings alleges any failure, omission, negligence or fault by any member of that team, by Utah Valley University Police, by its chief, or by any officer. **Nothing in this file may be read to imply otherwise, and any framing that reads as insinuation about a security team member's conduct is refused on sight.** The State's charged grave-risk-of-death aggravator is an allegation about **the shooter's conduct** — it is not a charge about the adequacy of anyone's security arrangement.

---

## §0 · Sourcing framework — the project standard, reproduced

| Tier | What it is |
|---|---|
| **Tier 1** | Sworn testimony and primary court filings / primary documents |
| **Tier 2** | Named official statements (incl. named first-person statements by principals) |
| **Tier 3** | Named journalistic reporting / analysis |
| **Tier 4** | Anonymous-source or low-verification material |

- **"T1 via T3"** marks primary-document content known only through reporting. It is never silently promoted.
- **Confidence grades** — High / Medium-high / Medium / Low / unverified — **must trace to an actual verification act by this project.** A grade is never inherited from a claimant, and never from repetition across outlets.
- **"— (checkable)"** marks items verifiable but not yet verified. They feed §10 and **are never counted as findings.**
- Every claim carries a locator; every retrieval carries a date. Editorial characterisations are labelled *assessments*, not fact.

---

## §1 · ACCESS PATH — read this before anything else

Everything below is bounded by the following. These are not formalities; each one has produced a measurable error in this library before.

### 1.1 🚨 The hearing transcripts are UNCERTIFIED COMMERCIAL MACHINE TRANSCRIPTS

`day1.txt` … `day5.txt` are **Rev renderings**, not the certified record. This project has **never heard the audio**. The parties themselves cite a paginated certified transcript (`PH1:46-47`, `PH2:69`, `PH4:91-92`) that this library **does not hold**, so the stream offsets used here **cannot be cross-walked** to the citations the court will use on 2026-09-01.

**The transcription defect is demonstrated, not hypothetical.** In the banked 2025-09-10 press-conference transcript Rev renders the victim's name as *"Charlie **Cook**"* — present identically in Rev's own raw HTML, so it is Rev's error and not the extraction's. **Every quotation below is a quotation of what the banked rendering records, not of what was necessarily spoken.**

### 1.2 🚨 REV SPEAKER LABELS ARE NOT EVIDENCE — and this file's central witness is the worst instance

**In `day1.txt`, every one of Officer Bagley's answers carries the speaker label "Richard Novak" — the name of a defence attorney of record.** He holds the stand from line 628 to line 6291.

**Speaker attribution here is inferred from CONTENT, and the basis is stated:**
- The State calls *"Officer Chris Bagley"* (line 628); the judge addresses *"Officer Bagley"* (632, 636, 648).
- Asked to state and spell his name **under oath**, the witness answers: *"Christopher Bagley. Last name spelling B-A-G-L-E-Y"* (line 672).
- Defence counsel opens cross: *"Officer Bagley, my name is Kathy Nester"* (line 4718).
- **The labeller is demonstrably worthless**: the same rendering labels the **administration of the oath** *"Kathy Nestor"* (line 640) — a defence attorney cannot administer the oath.

⚠️ **Counsel's own surname is a label hazard too, and this file does not resolve it.** Measured across all 72 banked artifacts under both readings: **"Nestor" = 694 hits in 4 files** (essentially nothing but Rev speaker labels in `day1`/`day2`/`day2_condensed`), while **"Nester" = 255 hits in 28 files**, including every court filing, her own self-introduction (*"my name is Kathy Nester"*, `day1` 02:43:01) and the judge's own address to her. **One filing's signature block nonetheless reads "Kathryn N. Nestor."** This file writes **Ms. Nester** for the transcript prose and flags the divergence rather than picking a winner.

### 1.3 Rev timestamps are STREAM OFFSETS

They are approximate as clock times (±5 min) and are **never converted to a time of day** anywhere in this file. Where a clock time appears (12:15 p.m., 12:23, 12:30 a.m.), **it is a clock time a witness or a document gave**, not a converted offset. Intervals measured *within one stream* (e.g. "78 seconds later") are relative and are what the offsets can bear.

### 1.4 Search-method disclosure — both U+FFFE readings, measured

All corpus searches ran through `artifact_search.find()`, which tests **both** the joined and hyphenated readings of the U+FFFE line-break defect. **Defect census run 2026-08-17 over all 72 banked `.txt` artifacts: NUL bytes = 0; U+FFFE = 131; ligature defects = 6.** ⚠️ **`day1.txt` through `day5.txt` carry ZERO U+FFFE and zero NUL**, so for the transcripts the two readings are **byte-identical** — the dual-reading test is real but vacuous there, and this file says so rather than claiming rigour it did not need. The defect *is* live in the Information (1), the defence briefing ALT extraction (3) and the disqualification filings (50).

### 1.5 🚨 Corpus contamination — excluded per term, and which

`2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt` is a **mis-banked, unrelated federal case**. It was **retained in every sweep and excluded per term**: it produced exactly **one** false hit on the private-security battery (`security guards`, a jail anecdote), which is excluded. It returned **zero** on `Goforth`, `plainclothes`, `magnetometer`, `Hall of Flags`, `operations order`, `threat assessment` and `after-action`, so no blanket exclusion was applied and no true hit was destroyed.

### 1.6 What this project does NOT hold, and what each gap bounds

| Not held | What it bounds |
|---|---|
| 🚨 **The State's 2026-07-28 Memorandum in Support of Preliminary Hearing Bindover** (~28 pp.). Retrieval attempted and **FAILED 2026-08-13** | **§6 in its entirety.** Every statement in this file about the State's *2026* grave-risk argument is **the defence's characterisation of it**, recorded as such. The State's operative brief has never been read by this project |
| **Every exhibit.** State's Exhibits 1, 2, 7, 8, 9, 11, 12.1–12.4 and the surveillance video | §4, §5 and §6 carry only witnesses' and parties' **accounts of** exhibits, never their content |
| **Officer Bagley's body-worn camera** | The one artifact covering the pre-shot co-location on the Hall of Flags (§4.2) |
| **Any UVU Police record whatever** — operations order, event plan, post assignment sheet, briefing record, after-action review | **§8 in its entirety.** This is the decisive gap |
| **The certified transcript** | §1.1 |

### 1.7 ⚠️ The sibling file is PROVISIONAL and is NOT relied on here

`files - Event security/SEC-E02_security-team-allegations-assessment.md` (v1.0, 2026-08-17) is marked **`[PROVISIONAL]`**. Under LOOP §2, **a provisional finding may not be cited by another file, propagated into a topic folder, or used to resolve a register entry.** **Nothing in SEC-E02 is cited, relied on, or assumed anywhere in SEC-E01.** Where the two files touch, SEC-E01 rests on the primary sources it read directly.

🚨 **A live conflict between the two files is recorded rather than smoothed.** SEC-E02 §2 makes a reasoned carve-out and **names two members of Mr. Kirk's private detail**. SEC-E01 does not, and cannot: see §2. **This is an unresolved editorial question for the owner, not something this file resolves by acting.** → **Q-180** *(v1.0 wrote "Q-171" here; renumbered 2026-08-20 — see the revision log)*.

---

## §2 · 🚨 SCOPE, AND THE NAMING RULE — with the record-based reason

### 2.1 What this file is about

**The security posture and the professional conduct of personnel acting in a PUBLIC CAPACITY on 2025-09-10.** That is a legitimate public question, and it is a live one in this case: it bears on how the shooter reached the roof, on the State's charged grave-risk-of-death aggravator, and on the defence's answer to it (§6).

### 2.2 🚨 What this file deliberately does NOT contain

**The personal backgrounds of individual private security personnel.** No employment histories, no residences, no family, no social media, no photographs, no physical descriptions, no vehicle or licensing details, no prior careers — **for any individual member of Mr. Kirk's private security team.**

🚨 **AND NO INDIVIDUAL MEMBER OF THAT TEAM IS NAMED IN THIS FILE, even where a source names them.** They are referred to **by role only** — *"a member of Mr. Kirk's security team"*, *"the individual on the Hall of Flags"*.

### 2.3 The reason, and it comes from the court record, not from editorial preference

A **sworn proffer filed 2026-02-02 by a Deputy Utah County Attorney (docket 368)** — held on disk, read directly on its face, signed */s/ Ryan McBride, Deputy Utah County Attorney*, dated *"this 2nd day of February, 2026"* — states:

> **¶6:** *"Members of Charlie Kirk's security team have reported threats, doxing – the publication of personal information online for harassment purposes, and risks to them since Charlie Kirk's murder."*
>
> **¶5:** witnesses *"have received threats because of their involvement. Some have relocated to avoid these threats. Many have deleted online accounts and changed usernames and social media handles."*

**[T1 — for what the State represented to the court. ⚠️ A party's proffer, not an adjudicated finding.]**

The project rule already forbids identifying information about uninvolved private individuals **even when sources publish it**. Here the court record independently establishes that **publication of exactly this material is a reported, ongoing harm to exactly this population.** The rule and the record point the same way.

### 2.4 The two categories, stated explicitly

| Category | Named here? | Why |
|---|---|---|
| **Sworn police witnesses testifying in open court in their public roles** — Officer Christopher Bagley (UVU PD on 2025-09-10; Spanish Fork PD at the time of testimony), Agent David Hull (Utah DPS / State Bureau of Investigation), Officer Goforth (Spanish Fork PD) | ✅ **Named** | Public officials acting in public capacities, named on the face of the public record |
| **Agency heads speaking at announced press conferences** — UVU Police Chief Jeff Long; DPS Commissioner Beau Mason; FBI SAC Robert Bohls; Utah County Attorney Jeff Gray; Gov. Spencer Cox | ✅ **Named** | Named officials speaking in their public roles |
| **Counsel of record and the court** — Mr. Grunander, Mr. McBride, Mr. Sturgill for the State; Ms. Nester, Mr. Burt, Mr. Novak for the defence; Judge Tony F. Graf, Jr. | ✅ **Named** | Officers of the court in their public roles |
| 🚫 **Any individual member of Mr. Kirk's private security team** | ❌ **NEVER** | Private individuals; §2.3 |
| 🚫 **Private civilians incidental to the security question** — the questioner at the microphone, video declarants (one of whom the record establishes is **a minor**), the residents whose doorbell footage was collected | ❌ **Not named** | Bear on no public question this file investigates. ⚠️ One banked artifact states a **private residential street address**; it is cited by line number only and is not reproduced |

### 2.5 ✅ N-1 — A MEASURED NULL: the court record itself names no member of the private team

**Every reference to Mr. Kirk's private security team across all 72 banked artifacts is ROLE-ONLY. No individual member is named anywhere.**

- **Pattern (capable by construction — it is the vocabulary in which a name would appear):** `(Kirk's|his|own|private|personal|lead)\s+(security|detail)` OR `security\s+(team|guard|personnel|detail|guy)` OR `bodyguard`, both U+FFFE readings, all 72 artifacts.
- **Result — every hit opened and read, none counted:** the State's proffer (¶6, ¶7); the Information — **zero**; the PC affidavit — **zero**; the 2026-08-11 defence briefing (*"two security personnel"*, *"one of Mr. Kirk's security guards"*, *"observed security personnel standing an unknown distance"*); `day1.txt` (*"his own security team"*, *"Mr. Kirk's private security team"*, *"Mr. Kirk's detail, his own security team"*, *"one of the team's vehicles"*); `day2.txt` (*"his parts of his security team"*, and Officer Goforth *"doing security detail"* — **a sworn officer, a different category**); the 2025-09-10 press conference (*"his lead security guy"*). **Not one carries a personal name.**
- **Positive controls in the same run, proving the method finds surnames in this corpus:** `Bagley` 37 / 3 files · `Faumuina` 804 / 9 files · `Goforth` 8 / 2 files · `Losee` 211 / 11 files · `Hall of Flags` 53 / 5 files.
- **Contamination:** one false `security guards` hit in the mis-banked federal artifact, excluded per term.
- ⚠️ **SCOPE.** This is a fact about **this library's banked holdings**, not about the world. It is **not** evidence that no such name exists anywhere. It is stated because it establishes that **this file's role-only rule costs the record nothing** — the record itself is role-only.

**Confidence: High** (direct measurement by this project, 2026-08-17).

---

## §3 · The law-enforcement posture — what the arrangement DID include

🚨 **This section exists because verifying in both directions is a procedure, not a posture.** A file about security at an assassination is the natural home of insinuation. The affirmative record is therefore logged **first**, and as squarely as anything in §8.

All of §3 is **Tier 1** unless marked. Source: `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day1.txt`, Officer Christopher Bagley, direct by Mr. Grunander and cross by Ms. Nester. ⚠️ **His answers carry the Rev label "Richard Novak"; speaker inferred from content per §1.2.**

### 3.1 The officer and his qualification

| Fact | Locator | Tier · Confidence |
|---|---|---|
| **26 years a police officer**; Utah POST Academy, *"about 600 hours"*, certified | `day1` 45:14, 45:23 | T1 · High |
| **UVU Police Department on 2025-09-10**, where he had served **five years as a senior officer**; patrol, investigations, campus response | `day1` 46:12–46:38 | T1 · High |
| Prior service: Utah County Sheriff's Office 13 yrs, Springville City PD 6 yrs, Salt Lake County Sheriff's Office 1 yr; assignments *"Varies. I did K-9, I did SWAT, I did motors. Senior officer, FTO officer, detectives"* | `day1` 47:03, 47:21 | T1 · High |
| ⚠️ **He was NOT a sniper** — asked directly on cross: *"I wasn't. I worked well with them, but I was not a sniper."* Recorded because his rifle-vs-pistol discrimination and his identification of a sniper position (§5) rest on **familiarity, not on that qualification** | `day1` 04:05:35 | T1 · High |
| Deep familiarity with campus CCTV: station desktops, a dispatch camera wall, navigation maps he built for dispatch, used *"Every day"* | `day1` 47:44–48:30 | T1 · High |

*(Note: his own service arithmetic — 5 + 13 + 6 + 1 = 25 years, plus five months at his current agency — does not close against a stated "26 years." Recorded as a minor recollection caveat, not as a defect.)*

### 3.2 ✅ The deployment, in the officer's own words

- **The event was known in advance and specially staffed.** *"I did. I signed up for an overtime shift, so yes. For the special event, I signed up for the overtime shift."* (02:43:21) — so staffing was **augmented above normal duty**, at least as to him. Shift began *"approximately about 11 o'clock in the morning"* (01:02:29).
- **Fifteen officers employed; six assigned.** *"Employ, there was 15"* (02:44:31). Asked how many were assigned to cover the event: *"There was six of us that were, there was patrol one and then five others that were there with the chief"* (02:44:36); when counsel said five, **he corrected her** — *"Six, yes"* (02:44:51). ⚠️ **The composition is ambiguous on its face**: whether the chief is inside or outside the six is not resolved. *(This project's arithmetic — six of fifteen — is analyst-layer, not testimony.)*
- **All six armed**, with *"Glock pistols"* (02:45:03, 02:45:06).
- **The crowd size was anticipated, not a surprise.** Asked whether they had an idea thousands would attend: *"Had an idea"* (02:44:49). From the overlook he estimated *"several thousand people"* (01:37:58).
- ✅ **A pre-shot assignment existed and was given.** *"Did you receive a specific assignment shortly after coming onto duty?"* — *"Yes, I did."* — *"It was to secure the top of the Hall of Flags on the south end. So we had people that were gathering on top of that that were looking down on top of the tent, so we wanted to secure that area. So I was put up on top of the Hall of Flags on the south end."* (01:02:32–01:02:41)
- ✅ **Command was on scene and functioning before the shot.** *"The Chief Long got a text or an email or phone call stating that there was people on top of the Hall of Flags throwing stuff down to the tent. Therefore, he sent the two officers that were on duty down to secure the area. I got dressed and then came back and then went to the Hall of Flags to secure that area."* (02:43:36). Chief Long was **personally beside him in the courtyard** moments after the shot (01:40:24).
- ✅ **A physical barrier was in place on the walkway.** *"there's some … Actually, it looks like yellow crime scene tape. That was some of our barrier that we put up so people wouldn't go above that and walk."* (01:03:13) ⚠️ **He first reads the object as what "looks like yellow crime scene tape," and nothing in the record dates the placement.** "Pre-placed" is not established; **that it existed and was UVU PD's is.**
- ✅ **A body camera was worn and running**, chest-mounted (04:08:28–04:08:31).

### 3.3 ⚠️ The elevated post was CROWD CONTROL, not overwatch — and the distinction matters in both directions

**The record's word is "secure the top of the Hall of Flags."** The post was created **in response to a disturbance already under way** — civilians on the walkway throwing objects down onto the tent (02:43:36, 02:48:12).

🚨 **This file does not call it an "overwatch post."** "Overwatch" is a term of art connoting a covering or counter-sniper position. Applying it here would **import a protective function that was never assigned** and would recast an ordinary crowd-control posting as a failed protective pairing. **That is exactly the insinuation §2 forbids, and it is unearned.**

⚠️ **The same correction cuts the other way, and both halves are recorded.** Because the post was crowd control, the record **does not establish that UVU PD had identified the Hall of Flags as an elevated threat vector** — but neither does it establish that anyone thought it was one and failed to act. **The record is silent on the question, not negative.** Separately: two civilian witnesses who filmed a figure on the Losee roof shortly before the shot *"believed it was overwatch or some kind of a police overwatch for the event"* (Agent Hull, `day2` 01:55:12) — bystanders read a rooftop figure as normal event security. **That is Hull's recollection of others' understanding, and is recorded as such, not adopted.**

### 3.4 What was measurably NOT in place — witness-scoped, and stated that way

| Item | The record | Scope |
|---|---|---|
| **Magnetometers** | Asked whether any such machines were *"set up or being used on campus that day"* — **"No"** (02:45:30). Corpus-wide, `magnetometer` = **1 occurrence**, this one; `metal detector` = **0** | **A fact about the campus.** He answered a campus-wide question directly |
| **Drones flying** | *"as far as you know, were there any drones that were flying above campus that day?"* — **"Not that I know of"** (02:45:39) | ⚠️ **A HEDGE, not a null.** It must never be flattened to "no drones" |
| **UVU drone capability** | *"Did you guys even have drone capability? Did you have a drone on campus that you used?"* — **"No"** (02:54:15), reinforced at 02:54:24 | **A statement of departmental capability**, not an absence inference |
| **Briefing / debrief / meeting** | *"did you attend any type of debrief or briefing or meeting to prepare for the security of this event?"* — *"I did not because that morning when I got there, we had individuals on top of the Hall of Flags…"* (02:43:36); *"So you never attended any kind of… debrief or meeting…?"* — **"No, not that morning"** (02:44:16) | 🚨 **SCOPED TO HIM, and to that morning.** See the next row |
| 🚨 **Whether ANY briefing occurred** | *"Do you know if there was such a meeting?"* — **"I don't know** because when I got there, it was starting to… People were throwing stuff down on the tent"* (02:44:18) | **DISPOSITIVE. This is non-knowledge, not a null.** |
| **Written briefing materials** | *"Did you receive any type of briefing materials, written materials prior to the event…?"* — **"No, not that morning."** (02:48:12) | Scoped to what **he received**, and to that morning |
| **Operational / tactical plan** | After lunch, counsel restated **her own premise** — *"we talked about that you had had no briefing or no materials"* — then asked: *"Did you ever have any operational or tactical plan **that you were given** for that event?"* — **"For this event, no."** (04:05:02–04:05:26) | Scoped to what **he was given**. ⚠️ The premise is **counsel's**, not the witness's |
| **The Losee building** | ⚠️ **A COMPOUND question**: *"And did anyone ever talk to you about covering anything near or on top of or in the Losee building? Were you ever assigned that area before the shooting?"* — a single **"No"** (02:45:53). Then: *"Do you know who was?"* — **"I don't"** (02:45:55) | 🚨 **Both halves are about HIM.** And *"Do you know who was?"* **presupposes** someone was assigned; *"I don't"* is **non-knowledge**. A questioner's premise is not an answer — it establishes neither that someone was assigned nor that nobody was |
| **Other agencies** | *"Was there any other law enforcement agency besides Mr. Kirk's private security team and your six officers… did you have any Provo police or Orem police or anyone that you knew of or federal agencies?"* — **"I don't know"** (02:47:28) | 🚨 **He expressly could not close the set.** Any claim that the arrangement comprised only these bodies is not carried by this witness |

### 3.5 The Losee building's physical access — established, and it cuts both ways

On **direct** (`day1` 01:12:28–01:13:38):
- The Losee Center has **four stories**. Access to the roof is by *"an outside stairway"* to the south, which is **"open to the public"** (*"Is that open to the public?"* — *"It is"*).
- From the stairway, a red pathway runs between the Losee Center and the computer science building. Separating that pathway from the roof is *"a little handrail, like a little guardrail, probably about a couple feet high that somebody could jump over."*
- 🚨 **But the roof itself was restricted.** *"Is that area restricted? Is it off limits?"* — **"Yes, it is. There's a natural barrier with the guardrail. And from there on, there's no path. It's gravel roof, so it's not paved like everything else."** Asked whether someone could hop over it — **"Yes."**

**The State's own charging document says the same thing about the approach**, at page 5 of the 10-page Information filed 2025-09-16 *(sworn to by Utah County Attorney Jeffrey S. Gray; factual narrative submitted by Brian Davis, Utah SBI)*:

> *"The suspected shooting position is adjacent to an open, publicly-accessible walkway. To access the suspected location, a person must climb over a railing and then drop to the roof only slightly below."*

🚨 **THIS CUTS BOTH WAYS AND IS RECORDED AS CUTTING BOTH WAYS.** No locked door was defeated and no staffed perimeter was breached at that location — **because the record describes none there.** Equally, **no forced entry was required.** And the roof was **not** an undesignated space: the State's own witness called it *restricted and off limits* behind a barrier. **Whether a six-officer detail should have posted that roof is a judgment nobody in this record makes.** ⚠️ **Note also that the officer who described the approach is, on content, almost certainly the "UVU Officer" whose account the Information's narrative summarises** (matching on six particulars: elevated vantage point, rifle inferred by sound, reasoning to the Losee line of sight, transit there, climbing the railing, the gravel impressions). **These are therefore ONE observer in two documents, not independent corroboration.** *(Medium-high; content-based, no contrary candidate found in `day1`.)*

### 3.6 🚨 D-73 — THE BARRIER IS DESCRIBED THREE DIFFERENT WAYS BY THREE SOURCES, TWO OF THEM THE STATE'S OWN

| Source | Description | Locator |
|---|---|---|
| **Information, 2025-09-16** (State) | *"a railing"* | p. 5 |
| **Affidavit of Probable Cause, face-dated 09/12/2025** (State; */S/ Davis, Brian*; three counts, not seven) | *"a **short concrete wall** that separates the common area from the rooftop of the Losee Center building"* | dc27880530 |
| **Officer Bagley, sworn** | *"a little handrail, like a little **guardrail**, probably about a couple feet high"* | `day1` 01:13:08 |

**And the space itself:** *"an open, publicly-accessible walkway"* (Information) vs *"the common area adjacent to the Losee Center building"* (affidavit).
**And the time:** the Information puts the crossing/drop at *"approximately 12:15 p.m."*; the affidavit puts the suspect on the stairs at ~1215 and over the short wall at ~**1217**, having entered *"through a set of doors on the southeast corner"* — an interior route the Information's *"from the public walkway"* does not convey.

⚠️ **Neither filing is authoritative over the other, and this file picks neither.** The divergence matters because *"a railing"* and *"a short concrete wall"* imply different degrees of physical separation, and any statement about how easily the position was reached inherits whichever word is chosen. **(CR-E08 already registers the 1217-vs-12:15 divergence; the barrier-description divergence is new here.)** **Confidence: High** (all three read directly).

---

## §4 · Mr. Kirk's private security team — ROLE ONLY

🚨 **No individual is named, described, or made identifiable in this section. Nothing in it implies any failure, omission or fault by any member of that team, and no such implication may be drawn.**

### 4.1 ✅ What is established at Tier 1

| # | Fact | Locator | Tier · Confidence |
|---|---|---|---|
| **a** | **Mr. Kirk had his own security team present with him.** *"Were you aware of whether Mr. Kirk had his own security team present there with him?"* — **"Yes"** | `day1` 02:46:51 | T1 · High |
| **b** | **A member of that team was on top of the Hall of Flags, next to the officer's own position, BEFORE the shot** — *"one of the individuals that was on top of the Hall of Flags right next to me"*, confirmed *"before the shooting"* | `day1` 02:46:55–02:47:00 | T1 · High |
| **c** | **The officer understood that individual to be armed** — *"I was aware he was armed"* | `day1` 02:47:07 | T1 · High |
| **d** | **Further members were in the crowd and near Mr. Kirk** — *"And then I saw several down in the crowds and down by him, yes."* ⚠️ Prefaced *"And then"*: **its timing relative to the shot is NOT fixed by the record.** Only (b) is expressly confirmed as before the shot | `day1` 02:47:00 | T1 · High as to the words; timing unfixed |
| **e** | **The team removed Mr. Kirk from the scene** — *"Mr. Kirk's detail, his own security team removed him from the scene whilst administering first aid and they conducted what would be called a hasty transport to Timpanogos Hospital"* — elaborated: *"he was thrown into one of the team's vehicles and then transported to the hospital as opposed to waiting for an ambulance"* | Agent Hull, `day1` 05:58:03, 05:58:49 | T1 · High |
| **f** | ⚠️ *"[T]wo security personnel in front and diagonal to Mr. Kirk, standing in the grass area by the barrier"* appear in State's Exhibit 8; *"[o]ne of Mr. Kirk's security guards comes into frame from the right of Mr. Kirk three seconds after the shot"* | 2026-08-11 defence briefing | **T1 for what was filed** — ⚠️ **a party's characterisation of an exhibit this project has not seen** |
| **g** | ⚠️ **The arrangement was described as JOINT and ROUTINE by the police chief.** *"So we work together. He has his team and they do this all over the country, we all know. That this is not uncommon for them. They're very comfortable on campuses. And I was coordinating with his lead security guy. So yeah, we were working together."* | Chief Jeff Long, 2025-09-10 press conference, ( 15:06 ) | **T2** · High as to what he said |

### 4.2 ⚠️ Asked whether he COMMUNICATED with them, the officer answered with a SIGHTING — and the record is SILENT on coordination, not NEGATIVE

The exchange, in full — a single 23-second stretch on cross (`day1` 02:46:45–02:47:08):

> **Q:** *"Were you aware of whether Mr. Kirk had his own security team present there with him?"* — **A:** *"Yes."*
> **Q:** *"Did you **communicate** with any of those people?"* — **A:** *"I **saw** one of the individuals that was on top of the Hall of Flags right next to me, **yes**."*
> **Q:** *"And that was before the shooting?"* — **A:** *"Yes. And then I **saw** several down in the crowds and down by him, yes."*
> **Q:** *"And were you aware of whether that person was armed either?"* — **A:** *"I was aware he was armed."*

**The verb in the question is "communicate" — which appears exactly ONCE in this witness's entire testimony, in that question. The verb in the answer is "saw," twice.** *(Measured inside the exchange: `saw` = 2. There is no third use; the nearby "I did not see" at 02:46:35 is outside it and answers a different question.)* **No content, time, subject or direction of any communication appears anywhere in his testimony.**

**⚖️ TWO READINGS LIVE, AND THIS FILE RESOLVES NEITHER.**
- **(i) The affirmative reading, which may well be right and is at least as strong.** The answer **ends in "yes"** — to a yes/no question that is an affirmative, with *"I saw"* supplying detail rather than correcting the verb. **Two armed professionals standing beside each other on a walkway for over an hour almost certainly spoke.** And his awareness that the man was armed (02:47:07) uses a **knowledge verb whose basis he never states** — one ordinary way to know another person is armed is **to be told**. This reading is the steelman, it is credited, and nothing in the record defeats it.
- **(ii) The substitution reading.** The answer supplies a sighting where a communication was asked for.

**What is durable across both: no content of any exchange is in the record. Nothing supports reading the answer as evasive, and it must not be so characterised.**

### 4.3 ✅ N-2 — the coordination null, measured, with the scope stated

**Capable patterns over `day1.txt`, both readings:** `channel` = **0** · `deconflict` = **0** · `liais` = **0** · `frequenc` = **0** · `earpiece` = **0** · `coordinat` = **4** — all four opened and read, **all four Agent Hull describing POST-shooting inter-agency investigative coordination** (directing the investigation, coordinating with the state crime lab and responding scene techs) · `radio` = **2**, both post-shot internal police traffic.

🚨 **THIS ESTABLISHES SILENCE, NOT ABSENCE, AND THE DIFFERENCE IS THE WHOLE POINT.** The record does **not** establish that UVU PD and the private team coordinated, deconflicted sectors or shared a channel — **and it does not establish that they failed to.** The same witness answered *"I don't know"* about whether any other agency covered the event (02:47:28) and *"I don't know"* about whether any security meeting occurred (02:44:18). ⚠️ **And the one named official who was asked directly said the opposite of an absence: *"I was coordinating with his lead security guy"* (§4.1 g).**

### 4.4 🚨 CATEGORY DISCIPLINE — three people who are NOT private security and must never be merged with them

1. **Officer Goforth, Spanish Fork Police** — Agent Hull: *"When that vehicle was stopped, it actually made contact with an officer who was doing **security detail**"* (`day2` 00:57:54). 🚨 **A SWORN MUNICIPAL POLICE OFFICER.** ⚠️ **And the contact was at *"approximately 12:30 AM"* on *"September 11th, 2025"*** (00:58:16, 00:58:21) — **roughly twelve hours after the shot.** It cannot bear on the event-day arrangement at all. ⚠️ **What his detail was securing is nowhere stated**: `Goforth` returns 8 hits in 2 files (`day2` and its condensed twin — one source, four lines, all inside Hull's testimony), and **zero across `day1`, `day3`, `day4`, `day5`** and every filing. He did not testify.
2. **An off-duty Utah state trooper on scene.** Hull agreed, on a document-refreshed question, that a named individual was *"an off-duty trooper who happened to be there that day"* (`day2` 01:48:41) and that the trooper's report recorded a gun (01:48:58). ⚠️ **Hull did NOT adopt the name in connection with recovering a holster** — asked directly he said *"I know that a trooper was interviewed, having been on scene. I don't recall if it was Gonzalez. I don't recall the name."* **A questioner's premise is not an answer.**
3. **A badged, armed, civilian-clothed individual who accompanied the officer to the Losee building AFTER the shot** (`day1` 04:08:32–04:09:06). The officer: *"I don't know who he was exactly. He had a **badge** on… I had somebody with me to back me up"* — agency unknown. 🚨 **Post-shooting, badged, and NOT established to be private security. He must not be recorded as such.**

---

## §5 · The response to the shot — Tier 1, and logged in both directions

| # | Event | Locator | Note |
|---|---|---|---|
| 1 | The officer heard **one gunshot** from an elevated position overlooking a crowd he estimated at *"several thousand"* | `day1` 01:37:58–01:38:25 | T1 · High |
| 2 | 🚨 **Communications were FAST** — *"Within 30 seconds maybe"* between the shot and a radio report that a shooter was in custody; *"I was informed on the radio that we had a shooter in custody"* | `day1` 01:39:26, 02:54:56 | T1 · High |
| 3 | ⚠️ **AND THE REPORT WAS WRONG, AND THIS FILE SAYS SO.** The person detained was in the courtyard, not at the firing position; *"Then I realized that we probably didn't have our shooter in custody from that moment"*; *"I figured those guys saw something I didn't see… I thought that was him"* | `day1` 02:33:44, 02:55:08, 02:56:07 | 🚨 **Fast traffic carrying a mistaken belief is FAST, not "functioning." Recording only the speed would be a one-directional log** |
| 4 | ✅ **Command was co-located.** *"my chief, Chief Long, that was right next to me"* in the courtyard as they pushed people out | `day1` 01:40:24 | T1 · High |
| 5 | ✅ **A contemporaneous acoustic discrimination, with its basis stated.** He saw an empty pistol holster on the grass, turned to his chief and said *"That was a rifle shot"* — *"And he said, 'I agree.'"* Basis: *"a handgun is more of a short bang pop sound. With a rifle, you have more of a longer violent bang or crackle sound… It's longer"* | `day1` 01:41:11–01:42:00 | T1 · High **as to what was said**; ⚠️ Medium as to the discrimination's reliability — a trained ear, not an instrument, and he was **not** a sniper (§3.1) |
| 6 | ✅ He looked up, identified the Losee building as having a **direct line of sight**, and went there **before any camera evidence existed** | `day1` 01:42:00 | T1 · High |
| 7 | He reached the roof by the public stairway and *"hopped over the guardrail"*; found impressions in the gravel; **no law enforcement was on the roof, the stairway or the walkway** when he arrived | `day1` 01:43:12, 02:45:58–02:46:11 | T1 · High. ⚠️ **This is the state of the roof AFTER the shot. It cannot carry any claim about pre-event assignment** |
| 8 | ✅ He **preserved both scenes without walking through them**, taped the roof at the guardrail, and posted Payson officers to exclude all but law enforcement; turned the roof over to a deputy sheriff | `day1` 02:41:17–02:41:38, 02:47:41–02:47:49 | T1 · High |
| 9 | ⚠️ **His body camera died on the roof, before the crime tape went up, and was never restarted.** *"I think the battery went dead. It was just right at that moment"*; *"Usually dock it, but no, I didn't go back. It was too chaotic running around"* | `day1` 04:12:23, 04:12:35 | T1 · High. 🚨 **Any description of the camera as running "throughout" is wrong** |
| 10 | ⚠️ **The "27 minute and 35 second" duration is DEFENCE COUNSEL'S characterisation inside a compound question**, answered *"Yes"* to the operative clause *"that's the only body cam you have that day?"* **Nobody testified to measuring it.** ⚠️ And it **cannot** span the co-location: the officer checked in ~11:00 a.m. and timed the shot at 12:23 — **over 80 minutes on the Hall of Flags** — so a 27:35 clip ending on the Losee roof covers at most its final stretch, and **whether it reaches back before the shot is unestablished** | `day1` 04:12:40–04:12:54; 01:02:29, 02:51:13 | T1 for what was put and assented to. **Medium** as a duration |
| 11 | **The private team removed Mr. Kirk, administered first aid, and effected a hasty transport in one of the team's own vehicles rather than waiting for an ambulance** | Hull, `day1` 05:58:03, 05:58:49 | T1 · High |
| 12 | **Agent Hull arrived on campus *"shortly after 1:30"* — *"approximately an hour after Mr. Kirk had already been removed"*** (*"Approximately, yes"*), and had **no pre-event role**: *"you were not engaged in any way with this event prior to getting a call after the shooting? Is that correct?"* — **"Correct"** | `day2` 01:40:24–01:41:13 | T1 · High |
| 13 | 🚨 **Hull's *"we did have a plan"* and the SBI task assignments are the POST-SHOOTING INVESTIGATIVE RESPONSE and must NEVER be read across to pre-event security planning** | `day1` 04:34:48, 04:32:33–04:33:48 | T1 · High |
| 14 | *"Eventually my understanding is the campus was locked down and secured, and we were able to start getting people in to start processing crime scenes"* | Hull, `day1` 04:34:23 | ⚠️ **Hedged** (*"my understanding"*) and anchored to the **afternoon of the 10th** |

---

## §6 · The litigated grave-risk issue — recording layer, both sides

🚨 **This is the RECORDING layer. Fidelity to what each party said is the standard. Nothing here is adopted, and no filing's characterisation of an exhibit is treated as a description of that exhibit.**

⚠️ **AND THE DECISIVE LIMIT, RESTATED: the State's 2026-07-28 bindover memorandum is NOT HELD.** Everything below about the State's **2026** position is the **defence's characterisation of it**.

### 6.1 What the State pleaded — verbatim, 2025-09-16 Information

**Count 1 charges aggravated murder under exactly one circumstance:**
> *"(iii) the defendant **knowingly created a great risk of death to another individual** other than Charlie Kirk and the defendant."*

**The probable-cause narrative supplies the proximity facts (page 4):**
> *"**Mr. Kirk's team members** were very close to him on his right and left, as well as some behind his canopy and others at various close locations near him. The large crowd surrounded Mr. Kirk on three sides. Temporary metal fencing separated attendees from Mr. Kirk by only a matter of feet. Directly above and behind Mr. Kirk was the UVU Hall of Flags, an indoor walkway spanning several hundred feet with floor-to-ceiling glass windows which overlook the plaza where Mr. Kirk was seated. **People were in the walkway at the time of the shooting.**"*

And the sentence the State's own summary marks as load-bearing:
> *"The bullet's trajectory passed closely to several other individuals beside Mr. Kirk, **including the questioner who was standing directly in front of Mr. Kirk.** Children were visible near Mr. Kirk's stage when he was shot."*

### 6.2 🚨 F-119 — THE STATE'S CHARGING DOCUMENTS NEVER USE THE WORD "SECURITY"

**Measured 2026-08-17, both U+FFFE readings, on both filings read end to end:**

| Filing | `securit*` | `guard` | `bodyguard` |
|---|---|---|---|
| **Information, 2025-09-16** (10 pp.) | **0** | **0** | **0** |
| **Affidavit of Probable Cause, face-dated 2025-09-12** (3 pp.) | **0** | — | **0** |

*(Positive controls in the same run on the Information: `officer` 6, `police` 20, `Kirk` 44, `roof` 14, `railing` 4, `walkway` 5.)*

🚨 **The State's phrase is "Mr. Kirk's TEAM MEMBERS," and its subject must not be silently dropped.** "Security personnel" enters this case's vocabulary through **the defence's brief** and through **witnesses' and officials' answers** — not through the State's pleading. **A file that answers an allegation about "team members" with evidence about a videographer, or that converts "team members" into "private security team," has blended the layers.** *(Note: on redirect Agent Hull described the people behind the banner as *"representatives… of TP USA"* and *"law enforcement representatives"* — §6.4. The State's "team members" is not established to mean private security.)*

**Confidence: High** (direct measurement).

### 6.3 What the defence argued — 2026-08-11 preliminary-hearing briefing

The brief attacks the aggravator as resting on speculation. In its own words, the State *"speculates, and asks this Court to speculate"*:
> *"a) That the shooter actually **observed security personnel standing an unknown distance from Mr. Kirk**; b) That the shooter may have known that there were people behind the pop-up tent when the single shot was fired, although the State's evidence actually shows otherwise…"*

And on the geometry:
> *"There was no one 'directly' next to Mr. Kirk when he was shot, and there was **no one under the tent on the side that Mr. Kirk was struck or behind him in the breezeway.** Multiple shots were not fired. There were no ricocheting bullets."*
> *"…the single bullet came from above… The bullet traveled at a downward angle and hit Mr. Kirk in the left side of his neck."*

Its own description of State's Exhibit 8 nonetheless places **two security personnel in frame in front of and diagonal to Mr. Kirk**, and **one coming into frame from the right three seconds after the shot** (§4.1 f).

### 6.4 ⚠️ Two corrections to how this exchange is usually reported

**(1) Agent Hull never adopted the "dead-on view of … his security team" characterisation.** On cross, Ms. Nester established only that a video was *"taken by [a civilian attendee] from behind the individual that was speaking to Mr. Kirk"* — which Hull adopted (*"Correct."*, `day2` 01:58:05). ⚠️ **That attendee is named in the transcript and is NOT named here: the record establishes he is a MINOR** (*"because he is a minor, his mother witnessed it, and also signed the statement"*, `day1` 05:14:41), and defence counsel argued his Rule 1102 statement is protected on that basis (`day1` ~05:17:33). His identity bears on nothing in this file. Her **next** turn (01:58:06) put a **two-clause** question whose **first** clause asserted the video *"showed a dead-on view of Mr. Kirk and his parts of his security team."* **Hull's reply went only to the second clause:** *"You're referring to the UVU video in the breezeway?"* — *"Yes."* — *"We have that video, yes."* (01:58:25–01:58:27). 🚨 **The "Correct" PRECEDES the security-team sentence by one second on the stream offsets and is chronologically incapable of assenting to it. The first clause was never answered and never revisited.** ⚠️ **This does not establish that the exhibit fails to show security personnel — only that this witness never said it does.** *(Hull did describe a different exhibit — State's Exhibit 9 — as showing Mr. Kirk *"being carried down the left side of the video under that breezeway"* by his own security: `day1` 05:58:29. The two must not be conflated.)*

**(2) 🚨 THE STATE'S ANSWER ON REDIRECT, WHICH RUNS AGAINST THE DEFENCE'S "NO ONE BEHIND HIM" LINE — logged because the both-directions rule requires it.** Mr. Sturgill, on the same tunnel view (`day2` 02:19:39):
> **Q:** *"Leading up to the shot, what's going on behind that banner?"*
> **A:** *"There are representatives, I believe, of TP USA… There are **law enforcement representatives**. I don't know if there's any student body. But essentially, people are **moving to and fro** behind that area. A couple of individuals are retrieving items from a vehicle, but there's **consistent movement** behind and in that area."*
> **Q:** *"Directly behind the banner?"* — **A:** *"Correct."* (02:20:15)

⚠️ **The two are reconcilable and must not be blended: the defence's proposition is scoped to the INSTANT of the shot; Hull's redirect is scoped "leading up to" it.** Both are recorded; neither is resolved here.

### 6.5 ✅ N-3 — the defence brief never mentions the Hall of Flags

**Measured on BOTH banked extractions, both U+FFFE readings:** `Hall of Flags` = **0** · `hall` = **0** · `flag` = **0**. **Positive controls in the same run on the same files:** `Losee` 17 · `securit*` 4 · `walkway` 4 · `breezeway` 1 · `zone of danger` 4 · `StBr` (its citations to the State's brief) 7.

⚠️ **STATE THIS NARROWLY, AND NOT AS A GAP.** The Hall of Flags walkway is one recital in the **2025** Information's narrative — **not a pleaded element**. The brief is a **reply to the State's 2026 brief**, which it quotes seven times, and **not one quoted State position invokes the Hall of Flags**; the brief enumerates the two theories it is answering (*"line of sight"* as to the questioner, and *"a zone of danger encompasses everyone near a shooting victim"*). **A reply that tracks its opponent's opening is not ignoring a pillar.** ⚠️ **And the State's brief is not held, so the leading explanation cannot be tested.** **Confidence: High** as to the null; **Medium** as to the explanation.

---

## §7 · What officials said — Tier 2, recording layer

⚠️ **All three are Rev machine transcripts (§1.1). HIGH confidence that the banked transcripts record these words in this capacity; MEDIUM-HIGH that they are the exact words spoken, because no audio has been heard.**

### 7.1 🚨 UVU Police Chief Jeff Long, 2025-09-10 — the "we didn't" line

**Speaker identified from CONTENT, three ways:** Gov. Cox thanks *"Chief Long, and his response here with the UVU Police Department"* ( 04:40 ); Cox hands off — *"Chief Long?"* ( 12:50 ); the speaker self-identifies — *"So my name is Jeff Long. I'm the police chief here at UVU"* ( 12:52 ). **A named public official in his public role.**

Asked *"Can you talk a little bit about the security of the event itself, who was there security-wise **and what happens on these kind of events**?"*, he answered, contiguously:

> *"But I can tell you about our venue today. **This was an open venue. This was outside. We did have six officers working that event. We had probably over 3,000 people that were in attendance**, [sat down in kind of a bowl area here on the central campus. We have a waterfall area, and so] he was in a lower area surrounded by buildings.*
> *We had some **plainclothes police officers that were in the crowd** as well. We trained for these things and you think you had things covered and these things, unfortunately, they happen. **You try to get your bases covered and unfortunately today we didn't. And because of that, we had this tragic incident.** So, we did have officers there. We had Charlie Kirk's team. He has a security team that travels with him and they were here with him when he was shot."* ( 13:48 )

🚨 **WHAT HE CONCEDED, PRECISELY — TWO THINGS, NOT ONE, AND THE FILE STATES BOTH.**
1. That the generic aspiration (*"you try to get your bases covered"*) was not met *"today."*
2. That the shortfall and the killing were causally connected — *"**And because of that**, we had this tragic incident."*

**He named NO omitted measure, NO breached protocol, NO responsible party and NO failing by any person.** ✅ **Verified by measurement, not assumed:** across this entire transcript, `fail`, `mistake`, `responsib`, `apolog`, `fault`, `blame`, `lapse`, `breach`, `shortcom`, `should have`, `hindsight`, `review`, `after-action` all return **ZERO**; the same stems return hits in the sibling banked transcripts, so the battery is capable. `protocol` appears once and it is **a reporter's** word, never his.

🚨 **TWO REFERENTS ARE LEFT OPEN, AND NEITHER MAY BE RESOLVED.**
- **The "we" of "we didn't"** — UVU PD alone, or the whole joint effort? The sentence's subject shifts from generic second person (*"you try"*) to *"we,"* and he never fixes it. 🚨 **IT MUST NEVER BE RESOLVED ONTO MR. KIRK'S PRIVATE SECURITY TEAM.**
- **The "that" of "because of that"** — the shortfall, or the preceding *"these things happen"*?

**⚖️ TWO READINGS, AND THIS FILE RESOLVES NEITHER.** **(i) An OUTCOME reading** — the effort did not succeed in preventing this — which sits naturally beside *"these things, unfortunately, they happen"* and makes the causal clause nearly tautological. **(ii) A MEASURE reading** — some specific base was left uncovered. **The record does not choose.**

**⚠️ CONTEXT, MEASURED RATHER THAN ASSERTED:**
- The sentence sits **78 seconds of stream time** — not five minutes — before his answer describing the arrangement as **joint and routine** (§4.1 g). Two questions intervene. **The proximity strengthens rather than weakens the point that this is not a considered admission of fault.**
- Gov. Cox had **praised his leadership on the record before it**.
- He was speaking **the same afternoon**, having opened *"we are devastated… This is a police chief's nightmare"* — **and before the shooter was identified**, before the shot's origin was fixed (Commissioner Mason at the same podium: *"Potentially from a roof, yes. A longer distance shot from a roof"*), and with no review in existence.
- ⚠️ **This file does NOT state how many hours after the killing the conference began.** The transcript carries no clock time — only stream offsets and *"Good afternoon."* — *(checkable)*.

🚨 **THIS IS AN EXPRESSION OF DISMAY BY A GRIEVING CHIEF, NOT AN ADMISSION OF LEGAL FAULT BY ANYONE — least of all by anyone outside his own agency. It does not establish that a security failure occurred, that any measure was omitted, or that any person underperformed.**

### 7.2 DPS Commissioner Beau Mason, 2025-09-11 — declines and disclaims

Asked by a named journalist *"what were the security arrangements in place? **Was that roof being monitored?**"*, he answered:
> *"As far as the security, I cannot speak to that. **Neither the Department of Public Safety nor the Federal Bureau of Investigation was involved in the planning or security of this event**, and that'll have to be a question later for other agencies."* ( 09:03 )

**He self-identified at ( 00:37 ): *"I'm Beau Mason, commissioner for the Utah Department of Public Safety."*** ⚠️ **He is a STATE official characterising a FEDERAL agency's role.** FBI SAC Robert Bohls was at the same podium and neither repeated nor confirmed it — **the FBI half is an uncontradicted third-party assertion, not the FBI's own disclaimer.** ⚠️ And the disclaimer is **role-specific**: DPS was **co-leading the criminal investigation**. It excludes two agencies from *planning*; **it does not close the set of bodies responsible** — the one sworn witness asked could not close it either (§3.4).

### 7.3 Utah County Attorney Jeff Gray, 2025-09-16 — the roof WAS camera-covered, and an officer WAS scanning

At the charging press conference, reading the Information near-verbatim:
> *"UVU surveillance. At the moment of the shot, **a UVU police officer was watching the crowd from an elevated vantage point.** As soon as he heard the shot, he began to scan the area for threats. Believing the shot came from a rifle because of its sound, he looked for potential sniper positions…"* ( 10:35 )
> *"Police reviewed surveillance from **the camera covering the roof**, and discovered that it recorded an individual dressed in dark clothing cross the railing from the public walkway and drop onto the roof at approximately 12:15 PM."* ( 12:02 )

🚨 **This is the affirmative answer to "was that roof being monitored?" that any file quoting Chief Long's "we didn't" must carry with it: the rooftop WAS under camera surveillance, and a police officer WAS posted at an elevated position scanning at the moment of the shot.**

### 7.4 ⚠️ NO OFFICIAL HAS ALLEGED A FAILURE BY ANYONE

Across all four banked press-conference transcripts, no official alleges any failure, negligence or fault by UVU Police, by Chief Long, by any officer, or by any member of Mr. Kirk's private security team. **Chief Long's sentence is the only one approaching self-criticism, no other official echoes, endorses or elaborates on it, and the one official asked directly declined the question.** ⚠️ **SCOPE: this is a claim about the FOUR Rev press-conference transcripts this library holds** (measured total runtime ≈ 99 minutes *including reporters' questions*) — **not about official remarks generally.** The library separately records further press briefings it does **not** hold.

---

## §8 · 🚨 WHAT THE RECORD DOES NOT ESTABLISH

### 8.1 🚨 THE MASTER CALIBRATION — read this before any null below

**A preliminary hearing tests PROBABLE CAUSE for the CHARGED OFFENCES. The adequacy of the security arrangement is an element of NONE of them.** The defence put its security questions to attack the State's grave-risk aggravator; the State had no reason to adduce affirmative evidence that a briefing *did* occur, and neither side was required to put on an operations order, a site survey or an event plan.

🚨 **THEREFORE: the hearing record's silence is evidence about WHAT THE PROCEEDING WAS FOR. It is not evidence about the world, and it is not evidence that anything is missing.** Every null in §8 is a null **about this library's holdings and these renderings**, and each carries its own scope.

### 8.2 🚨 The negatives are SCOPED TO ONE WITNESS — the single most consequential point in this file

**NOT ESTABLISHED:**
- ❌ **That no briefing occurred.** The witness attended none *"that morning"* and expressly answered **"I don't know"** whether one occurred.
- ❌ **That no plan existed.** He was given none; the question was scoped to what *"you were given."*
- ❌ **That nobody was assigned to the Losee building**, or that there was **"no Losee coverage."** The compound question was about **him**; the follow-up returned **non-knowledge**, on a question that **presupposed** someone was assigned.
- ❌ **That no drones were over campus.** That answer is a **hedge** — *"Not that I know of."*
- ❌ **That the responsible bodies were only UVU PD and the private team.** He could not close the set.

⚠️ **A FAIR INFERENCE EXISTS, AND IT BELONGS IN THE ANALYST LAYER, GRADED, AND NOWHERE ELSE.** An officer of 26 years, on an overtime shift signed up for in advance, who received no materials and attended nothing, **is meaningful circumstantial evidence about the arrangement as a whole**, and no contrary evidence appears anywhere in `day1` under a capable pattern (§8.3). ✅ **That is a defensible inference. Graded MEDIUM. It is not a Tier 1 finding, and it must never be merged into the recording layer.** ⚠️ **It is also weakened from inside the same file: on direct, hours earlier, this witness testified that he DID receive a specific pre-event assignment** (§3.2).

### 8.3 ✅ The measured nulls — each with its patterns, controls and scope

**Method for all: `artifact_search.find()`, both U+FFFE readings, all 72 banked artifacts unless a narrower space is stated; contamination excluded per term (§1.5); every hit opened and read, never counted.**

| # | Null | Patterns (all capable — each is the vocabulary in which the thing would appear) | Scope |
|---|---|---|---|
| **N-4** | 🚨 **NO institutional pre-event security record of any kind is held by this project.** No operations order, no event security plan, no site survey, no post assignment sheet, no advance-team record, no threat assessment | `operations order` 0 · `operational order` 0 · `post order`/`post-order` 0 · `event security plan` 0 · `site survey` 0 · `advance team` 0 · `threat assessment` 0 · `access control` 0 · `checkpoint` 0 · `bag check` 0. ⚠️ `security plan` returns **3 hits in 2 files — and BOTH are COURTROOM security** (the 2025-10-27 ruling and the 2025-10-24 sealed-hearing transcript), a different subject entirely | **This library's 72 banked artifacts.** 🚨 **NOT a claim that no such record exists.** §8.1 governs: a prosecution docket would not necessarily contain a university's event-security file |
| **N-5** | **No after-action review or post-incident security assessment is held** | `after-action` 0 · `lessons learned` 1 (a charging-decision reference in an unrelated context) · `review`/`assess` return hits only on investigative and legal review | As N-4 |
| **N-6** | **No member of Mr. Kirk's private security team testified at the preliminary hearing** | Oath/witness census across all five days: **7 sworn live witnesses** — Officer Bagley (police), Agent Hull (SBI), Sgt. Faumuina (SBI), Ms. Bakker, Agent Davis (SBI), Ms. Karner (ATF), Ms. Oliver (ATF DNA Section Chief). **All law enforcement or laboratory examiners.** ⚠️ The `day4` oath at ~02:11 is **audio inside a played recorded Rule 1102 statement**, not a live swearing | All five evidentiary days. ⚠️ **Consistent with §8.1: no civilian of any kind testified live. Before any witness was sworn the State previewed its case — *"we anticipate presenting four witnesses. **They're all law enforcement witnesses**"*** (`day1` 23:50) |
| **N-7** | **Agent Hull is not a source on the pre-shot posture in either direction** | Every `securit*`/`detail` reference in his testimony concerns the **post-shot** period or sworn police. He testified he had **no pre-event role** (`day2` 01:40:24–01:40:42) and arrived ~1 hr after Mr. Kirk was removed | Hull's testimony (`day1`, `day2`; he does not testify on days 3–5). 🚨 **This establishes only that a file built on Hull cannot answer the question** |
| **N-8** | **No content of any communication between UVU PD and the private team appears anywhere** | §4.3. `channel` 0 · `deconflict` 0 · `liais` 0 · `frequenc` 0 · `earpiece` 0; `communicate` = 1 occurrence in the witness's whole testimony, **in the question** | `day1`. 🚨 **SILENCE, not absence — and one named official said the opposite (§4.1 g)** |
| **N-9** | ⚠️ **Chief Long's "plainclothes police officers in the crowd" is UNCORROBORATED in the sworn record** | `plainclothes` = **0** across `day1` (the two `plain clothes` hits concern the defendant's courtroom attire) and **1** corpus-wide — Chief Long's own sentence | 🚨 **NOT a contradiction. Nobody was asked.** The sworn record neither confirms nor denies it; it is a **T2 statement never tested under oath** |
| **N-10** | **No wound-characteristics or range-of-fire evidence is held** | State's Exhibit 11, the medical examiner's report, was **admitted with publication DENIED** | Bounds any claim about the shot's origin resting on wound morphology. **This file makes none** |

### 8.4 What else this file expressly does not establish

- ❌ **That the arrangement was adequate.** Nothing here is a finding of adequacy.
- ❌ **That the arrangement was inadequate.** Nothing here is a finding of inadequacy, and **no official, filing or witness in this library's holdings makes one.**
- ❌ **That leaving the Losee roof uncovered was unreasonable**, or that anyone was assigned or expected to cover it. **No standard of care for an outdoor event on an open public campus in an open-carry state is in this record**, and no expert testified to one.
- ❌ **Any failure, omission, negligence, fault or complicity by any person.**
- ❌ **Anything whatever about Mr. Robinson's guilt or innocence.** He is presumed innocent, and **has not been bound over.**

> 🛠 **Posture updated 2026-09-16 (owner's ruling).** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full. *The sentence above is retained as written, true as of its date; the ruling is `START-HERE` §0AH item 4 and `DOCKET-WATCH.md` v2.6.*

---

## §9 · Findings, and open questions

**All new register numbers checked against the highest in use across all 81 repository `.md` files as of 2026-08-17 (F-116, V-32, Q-170) 🛠 **D-NUMBER CORRECTED 2026-08-17 AFTER THIS FILE WAS DRAFTED: it assigned D<hyphen>76 on a highest-STRING count. The true ceiling is D-72 and the next free number is D-73, established the same day by reading every hit (Q-161). Renumbered to D-73.**. ⚠️ N-numbers in this file are FILE-LOCAL, following CR-E11's convention.**

### 9.1 Findings

- **F-117 — 🚨 THE "NO BRIEFING / NO PLAN / NO LOSEE COVERAGE" NEGATIVES ARE SCOPED TO ONE WITNESS, NOT TO THE ARRANGEMENT — AND ONE LIBRARY FILE FLATTENS THEM IN FIVE PLACES.** Every defence negative is addressed to what **he** attended, was given or was assigned, and he twice qualifies with *"that morning"* and once with *"for this event."* Asked whether a meeting occurred at all, he answered **"I don't know."** ⚠️ **`CR-E05` strips that scope at §3.5 line 192 (*"No drones over campus"* — a hedge rendered as a null), §3.5 line 193 (*"**Nobody was ever assigned to cover the Losee building**, and he does not know if anyone was"* — a bolded universal negative contradicted by its own trailing clause, **in the RECORDING layer**), §6 line 355 and §7 line 384 (*"there having been no briefing at all"*), and §7 line 382 (*"no Losee coverage"*). The v1.0 revision-log row at line 422 carries *"nobody assigned to the Losee building."* **Confidence: High** (transcript and file both read directly). ✅ **THE CORRECTION WAS APPLIED 2026-08-20 — Q-172 executed: CR-E05 v1.4 rescopes all five sites and adds the 01:02:32–41 assignment as the internal counterweight; the timeline's drones line was rescoped the same day.** *(v1.0 wrote "NOT YET APPLIED"; updated at v1.1 the day the application landed.)* *(The timeline file already scoped the meeting correctly — *"Bagley testified he **attended** no pre-event security planning meeting"* — its drones clause was the flattened one.)*
- **F-118 — ✅ THE COURT RECORD ITSELF IS ROLE-ONLY: no member of Mr. Kirk's private security team is named in any of the 72 banked artifacts.** §2.5. **Confidence: High.** ⚠️ Scope: this library's holdings, not the world.
- **F-119 — 🚨 THE STATE'S CHARGING DOCUMENTS NEVER USE THE WORD "SECURITY."** `securit*` = 0 in both the Information and the PC affidavit, both readings, with capable positive controls. The State's pleaded proximity theory is about **"Mr. Kirk's team members."** **"Security personnel" enters through the defence's brief and through witness answers, not through the State's pleading.** **Confidence: High.** → bears on CR-E08 B-4.
- **F-120 — ⚠️ CO-LOCATION IS ESTABLISHED; COORDINATION IS SILENT IN BOTH DIRECTIONS.** A member of Mr. Kirk's team was on the Hall of Flags beside the police post before the shot and was understood to be armed; further members were in the crowd and near Mr. Kirk. **Asked whether he communicated with them, the officer answered "yes" and described a sighting.** No content, time, subject or direction of any exchange is anywhere in the record — **and no witness said there was none.** ⚠️ **The one named official asked directly said the arrangement was joint and that he was coordinating with the team's head.** **Confidence: High** as to what was said; the coordination question is **graded SILENT, not resolved.**
- **F-121 — ⚠️ CHIEF LONG'S "WE DIDN'T" IS AN UNSPECIFIED CONCESSION WITH TWO OPEN REFERENTS, AND IT IS NOT AN ADMISSION OF FAULT BY ANY PERSON.** He named no omitted measure, no breached protocol and no responsible party — **measured, with a capable battery returning zero on every fault stem.** Two readings live (outcome vs measure) and the record does not choose. He spoke the same afternoon, before the shooter was identified and before the shot's origin was fixed, 78 seconds before describing the arrangement as joint and routine. 🚨 **The "we" must never be resolved onto Mr. Kirk's private team. Confidence: High** as to what the transcript records; **the concession's content is UNRESOLVED.**
- **F-122 — 🚨 NO INSTITUTIONAL PRE-EVENT SECURITY RECORD OF ANY KIND IS HELD, AND THAT — NOT ANY TESTIMONY — IS WHY THIS QUESTION CANNOT BE ANSWERED.** N-4/N-5. ⚠️ **And the silence is STRUCTURALLY UNINFORMATIVE**: §8.1. **Confidence: High** as to the holdings; **the absence is NOT evidence that no such record exists.**
- **F-123 — ✅ THE AFFIRMATIVE POSTURE IS SUBSTANTIAL AND IS LOGGED AS SQUARELY AS THE GAPS.** Advance knowledge and an overtime-augmented shift; six of fifteen officers, all armed; an anticipated crowd; a specific pre-event assignment to an elevated position overlooking the tent; a physical barrier maintained on that walkway; the chief personally on scene and diverting officers on a report minutes before; camera coverage of the Losee roof and an officer scanning from an elevated vantage point at the moment of the shot; radio traffic within ~30 seconds; a body camera worn and running; a member of the private team armed and beside the police post; further members in the crowd and near the principal; an outdoor venue on a public campus **in an open-carry state**; responsibility split across at least three bodies. **Confidence: High** for each cited item. ⚠️ **This is NOT a finding that the arrangement was adequate** — see §8.4.
- **F-124 — ⚠️ THE FAST RADIO REPORT WAS WRONG, AND SPEED MUST NOT BE LOGGED AS CAPABILITY.** A shooter-in-custody report reached the officer within ~30 seconds; the person detained was not the shooter, and the witness says so. **Recording the speed without the error would be a one-directional log in the pro-adequacy direction — the mirror image of the bias this file exists to avoid. Confidence: High.**
- **D-73 — 🚨 THE BARRIER AT THE SHOOTING POSITION IS DESCRIBED THREE DIFFERENT WAYS BY THREE SOURCES, TWO OF THEM THE STATE'S OWN** — *"a railing"* / *"a short concrete wall"* / *"a little handrail, like a little guardrail, probably about a couple feet high"*; the space as *"an open, publicly-accessible walkway"* vs *"the common area"*; the crossing at *"approximately 12:15 p.m."* vs *"approximately 1217 hours."* **Unresolved. Neither filing is authoritative over the other. Confidence: High** (all three read directly). §3.6.

### 9.2 Open questions

| | Question | What would answer it |
|---|---|---|
| **Q-180** *(assigned as Q-171 at v1.0; renumbered 2026-08-20 — QUEUE.md had assigned Q-171 to a different item the same day, and a cross-file collision is invisible to `queue-check.sh`, which validates only QUEUE.md)* | 🚨 **SEC-E01 and SEC-E02 apply DIFFERENT naming rules to the same population, inside one topic folder.** SEC-E02 §2 names two members of the private detail on a reasoned carve-out; SEC-E01 names none. **This file does not resolve it by acting** | An owner decision. ⚠️ Note LOOP §3 makes anything asserting or implying conduct by a living person a **human gate** |
| **Q-172** | 🚨 **The five scope-flattening lines in `CR-E05` (F-117) are STILL UNCORRECTED**, plus the drones line in `kirk-shooting-official-timeline.md` | Rewrite to the witness-scoped form, add the 01:02:41 direct-examination assignment as the internal counterweight, add a correcting note to the v1.0 revision-log row **rather than editing it silently**, bump the version |
| **Q-173** | **Was there a briefing, a plan, or a Losee assignment?** Wholly unanswered; only one officer's non-knowledge is on the record | A UVU PD operations order, event plan, post assignment sheet or briefing record for 2025-09-10; or testimony from Chief Long or any of the other five officers |
| **Q-174** | **Did UVU PD and the private team coordinate, and how?** | Officer Bagley's body-worn camera; a UVU PD supervisor's account; any inter-agency communications record. ⚠️ **NOT to be pursued through any private individual** |
| **Q-175** | **What was Officer Goforth's 00:30 detail on 2025-09-11 securing?** Nowhere stated; he did not testify | His report, or his testimony |
| **Q-176** | ⚠️ **Does Officer Bagley's body camera reach back before the shot at all?** The 27:35 figure is counsel's, unmeasured, and cannot span the 80+ minute co-location | The recording itself — **the first thing to check if obtained** |
| **Q-177** | **Is Chief Long's "plainclothes officers in the crowd" corroborated anywhere?** N-9 | Testimony from any of the other five officers; a UVU PD assignment record |
| **Q-178** | ⚠️ **What does the State's 2026-07-28 bindover memorandum actually argue on grave risk?** Retrieval FAILED 2026-08-13; §6 is bounded by this | Re-attempt acquisition |
| **Q-179** | ⚠️ **A sworn witness identified by the court only as "H.G." appears in the disqualification track (`CR-E16`), category unresolved, transcript not held.** No claim in this file is stated as "anywhere in the record" for that reason | The 2026-02-03 evidentiary-hearing transcript |

---

## §10 · Acquisition targets — INSTITUTIONAL RECORDS ONLY

| | Target | Why it bears on the public question | Proper? |
|---|---|---|---|
| **SEC-A1** | 🚨 **UVU Police records for 2025-09-10**: operations order, event security plan, post assignment sheet, briefing record, radio logs, CAD | **The decisive gap (F-122).** The only artifact class that could answer Q-173 | ✅ **Institutional. Public-records route** |
| **SEC-A2** | Any **agreement or memorandum between UVU, the event organiser and any private provider** governing responsibility for the event | Would establish the division of responsibility the record leaves open | ✅ Institutional |
| **SEC-A3** | Any **after-action review or post-incident security assessment** by UVU or UVU PD | N-5 | ✅ Institutional |
| **SEC-A4** | **Officer Bagley's body-worn camera recording** (single clip; battery death on the Losee roof) | Q-174, Q-176 — the one artifact covering the pre-shot co-location | ✅ Court/discovery route; ⚠️ likely gated |
| **SEC-A5** | 🚨 **The State's 2026-07-28 Memorandum in Support of Preliminary Hearing Bindover** | **Unbounds §6.** Retrieval FAILED 2026-08-13 | ✅ Public filing |
| **SEC-A6** | **The certified preliminary-hearing transcript** (paginated as `PH1:`–`PH5:`) | Replaces the Rev renderings; makes party citations cross-walkable before 2026-09-01 | ✅ Court record |
| **SEC-A7** | **Testimony or a public statement by Chief Jeff Long, or by any of the other five officers**, on the pre-event arrangement | Q-173, Q-177 — **public officials speaking about public duties** | ✅ Public-capacity |
| **SEC-A8** | State's Exhibits **8** and **9**, and the UVU breezeway surveillance | §6.3/§6.4 rest entirely on parties' characterisations | ✅ but gated; see CR-E12 |
| — | 🚫 **Personal background of ANY individual member of Mr. Kirk's private security team** — name, employment history, prior career, residence, family, social media, photographs, physical description, vehicle or licensing details | **NAMED AND EXCLUDED.** Bears on **no** public question this file investigates. §2.3 is the record basis: docket 368 ¶6 establishes that publication of exactly this material is a **reported, ongoing harm** to exactly this population | 🚫 **IMPROPER — DO NOT SEEK, AND DO NOT RE-OPEN** |
| — | 🚫 **Any named-press or open-web sweep run against an individual private security member** | Same. **The role-only rule costs this file nothing: the court record is itself role-only (F-118)** | 🚫 **IMPROPER** |

---

## §11 · Residual scope — what this file did NOT do

**Unstated scope reads as coverage that does not exist. Stated plainly:**

- **It read `day1.txt` and `day2.txt` in the passages cited and by capable pattern across their whole texts. It did NOT read `day3`, `day4` or `day5` beyond the oath/witness census and targeted pattern sweeps.** Nothing here rests on those days.
- **It did not view or read a single exhibit.** Every exhibit reference is a witness's or a party's account of one.
- **It did not read the medical examiner's report** (admitted, publication denied) and **makes no claim resting on wound characteristics.**
- **It did not read the State's 2026-07-28 bindover memorandum**, which is not held. **§6's account of the State's 2026 position is the defence's characterisation throughout.**
- **It did not hear any audio.** All transcript quotations are of uncertified Rev renderings (§1.1).
- **It did not re-verify `CR-E05` outside §3.5, §6, §7 and the v1.0 revision-log row; nor `CR-E01`–`CR-E04`, `CR-E06`, `CR-E09`–`CR-E16` at all.** It did not apply the F-117 corrections to `CR-E05` (Q-172).
- **It did not rely on `SEC-E02` for anything** (§1.7) and **did not resolve the naming conflict between the two files** (Q-180).
- **It did not seek, and will not seek, any information about any individual private security member** (§10).
- **It assigned no V-number and resolved no existing register entry.** New: **F-117 → F-124**, **D-73**, **Q-172 → Q-179**, plus the naming-conflict question — assigned as Q-171 at v1.0, renumbered **Q-180** at v1.1. **N-1 → N-10 are FILE-LOCAL.**
- ⚠️ **`[PROVISIONAL]` — no independent verification cycle has run on this file.** Under LOOP §2 nothing here may be cited by another file, propagated into a topic folder, or used to resolve a register entry until one has. **Aim the verification pass at F-117** (a claim about another file's text), at **F-121** (an unresolved two-reading item), and at **the §8.3 null battery**, whose scope statements are the load-bearing part.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.2** | **2026-09-16** | **Posture line updated to the owner's ruling of 2026-09-16.** The case-posture banner/statement now carries, beneath the sentence it had: *Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full.* The earlier sentence is retained as written (true as of its date). No finding, grade, label or citation changed. |
| **1.1** | **2026-08-20** | 🛠 **Register correction — the naming-conflict question this file assigned as Q-171 is renumbered Q-180. Nothing else changes; no finding, grade or scope statement moves.** The collision: **QUEUE.md assigned Q-171 to a different item (the Q-138 plan §§B–C application) the same day this file assigned it to the naming conflict** — two passes, one date, two meanings, and `queue-check.sh` could not see it because it validates only QUEUE.md; the duplicate it *can* catch (Q-142R) is the within-queue kind. ⚠️ **The wider defect found with it: this file's Q-172 → Q-179 existed ONLY here and never reached QUEUE.md, the "single dispatchable list" — eight rows invisible to dispatch for three days, the same two-copies shape as hazard 18 and the D-73 ceiling error.** ✅ **All eight rows synced into QUEUE.md 2026-08-20** (Q-176 cross-referenced to Q-53, whose decisive artifact it shares; Q-178 marked as the SEC-E01 §6 consumer of Q-45's acquisition, not a second route). Renumbered in live text only (§1.7, §9.2, §11); the v1.0 row below retains "Q-171 → Q-179" as a true account of what v1.0 did. QUEUE.md's Q-171 was assigned first in the queue itself and keeps the number. Q-180 verified free repo-wide before assignment, by grep and by reading the hits. **Later the same session, Q-172 was executed** (CR-E05 v1.4 + the timeline's drones line) **and F-117's "NOT YET APPLIED" flag updated to record the application** — the finding itself is unchanged. No case-posture statement altered; no register entry resolved or moved. |
| **1.0** | **2026-08-17** | **File created.** First reasoned assembly of the security posture at the 2025-09-10 UVU event, built by direct reading of the primary sources rather than from existing library files: `day1.txt` and `day2.txt` (the cited passages plus whole-text pattern sweeps), the 2025-09-16 Information and the 2025-09-12 probable-cause affidavit, the 2026-02-02 State proffer (dkt 368), the 2026-08-11 defence preliminary-hearing briefing, and all four banked press-conference transcripts. 🚨 **THE FILE'S SCOPE AND ITS NAMING RULE ARE PUT ON A COURT-RECORD BASIS, NOT AN EDITORIAL ONE (§2.3): docket 368 ¶6 establishes that members of Mr. Kirk's security team have reported threats and doxing, so no individual member is named or described here, and personal-background compilation is written into §10 as an IMPROPER target so no later pass re-opens it.** ✅ **And the rule is shown to cost the record nothing — F-118 measures that every reference to the private team across all 72 banked artifacts is already ROLE-ONLY, with capable patterns and positive controls.** 🚨 **The file's central analytic result is F-117: the "no briefing / no plan / no Losee coverage" negatives are scoped to ONE WITNESS and to what HE attended, was given or was assigned — he twice qualifies "that morning," and when asked whether a meeting occurred at all he answered "I don't know" — and CR-E05 strips that scope in FIVE places, one of them a bolded universal negative sitting in the RECORDING layer and self-contradicted by its own trailing clause. The correction to CR-E05 is NOT yet applied (Q-172) and this file does not treat it as made.** ✅ **F-119 records a measured null nobody had run: the State's charging documents never use the word "security" at all — its pleaded proximity theory is about "Mr. Kirk's TEAM MEMBERS," and "security personnel" enters the case through the defence's brief and witness answers.** ⚠️ **F-120 grades the coordination question SILENT rather than resolved, and expressly credits the ordinary reading of the officer's "yes"; F-121 refuses to resolve Chief Long's "we didn't" in either direction, records the causal clause the usual reading drops, and states that its "we" may NEVER be resolved onto the private team.** ✅ **Both directions logged as squarely: F-123 sets out the substantial affirmative posture — advance staffing, a specific pre-event assignment, a maintained barrier, command on scene and acting, camera coverage of the roof, an officer scanning from an elevated vantage point at the moment of the shot, and an armed team member beside him — while F-124 refuses to log a fast-but-WRONG radio report as a functioning capability.** 🚨 **§8.1 states the master calibration that governs every null: a preliminary hearing tests probable cause, security adequacy is an element of no charged offence, and the record's silence is therefore evidence about what the proceeding was FOR, not about the world.** ⚠️ **D-73 opened: the barrier at the shooting position is described three different ways by three sources, two of them the State's own.** ⚠️ **§1.6 states the decisive holdings gap first — the State's operative 2026-07-28 bindover memorandum is NOT held (retrieval failed 2026-08-13), so all of §6's account of the State's 2026 position is the DEFENCE's characterisation.** ⚠️ **SEC-E02 is `[PROVISIONAL]` and is cited for nothing (§1.7); the two files' conflicting naming rules are recorded as an unresolved owner question (Q-171) rather than resolved by action.** |
