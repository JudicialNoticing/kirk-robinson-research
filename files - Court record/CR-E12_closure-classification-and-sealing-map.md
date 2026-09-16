# CR-E12 — What is sealed, closed or classified in this case: the map, and what it bounds

**File ID:** CR-E12 · **Scope:** execution of **Q-75** — a map of every closure, sealing and record-classification event in the case, at the granularity the record actually uses; the inventory of the four confusably-named "protective/protection orders"; and a plain statement of **which records this library can and cannot ever obtain, and why.** · **Case context:** *State of Utah v. Tyler James Robinson*, No. **251403576**, **Fourth Judicial District Court, Provo — case type FS**, Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-16 · **Status:** v1.0

⚠️ **Findings `[PROVISIONAL]`.** Sourced from the 2026-08-16 reader pass; raw report banked at `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q70-completion-six-reader-reports_RAW.md`. **No independent verification cycle has run** → **Q-91**.

> ### ⚠️ §0.1 · PROVISIONAL DEPENDENCIES — *added 2026-08-16, LOOP §2 discipline*
>
> **LOOP §2 bars a `[PROVISIONAL]` finding from being cited elsewhere or used to resolve a register entry.** This file both **is** provisional and **rests on** provisional findings — and, most seriously, **it was used to CORRECT another file.**
>
> | this file's claim | rests on | status |
> |---|---|---|
> | every `dkt<N>` tier statement; the "2-13-2026" resolution | **CR-ACQ-2026-08-16 F-39 / F-40** | `[PROVISIONAL]` → Q-83 |
> | §3/§4's corrections to the granularity finding | **CR-E10 F-35 / F-36** | `[PROVISIONAL]` |
> | §8.1's docket-#14 resolution | **CR-E09 F-30** | `[PROVISIONAL]` |
> | §7's F-68 comparison against the preservation order | **CR-E13 §4** | `[PROVISIONAL]` → Q-94 |
> | §6.1's "public/redacted counterparts exist and are held" | **CR-E11 §1** | `[PROVISIONAL]` → Q-87 |
>
> 🚨 **NOTE THE DIRECTION OF TRAVEL: CR-E10 was revised to v1.3 on the strength of THIS file's F-62 / F-63 / F-69.** That is provisional→provisional, so ✅ **no verified file was contaminated** *(CR-E05 and CR-E06, the two verified files, were not touched on 2026-08-16)* — **but it is exactly the propagation LOOP §2 forbids, and CR-E10's v1.3 rows must be re-checked when Q-91 clears this file.**
> **Clearing item: Q-91.**

🚨 **CASE POSTURE: Tyler James Robinson has NOT been bound over for trial as of 2026-08-16. Presumption of innocence applies throughout.** Nothing in this file adjudicates anyone's conduct.

> 🛠 **Posture updated 2026-09-16 (owner's ruling).** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full. *The sentence above is retained as written, true as of its date; the ruling is `START-HERE` §0AH item 4 and `DOCKET-WATCH.md` v2.6.*

🚨 **THE WHOLE MAP IS BOUNDED AT 2026-03-14 AND MUST ALWAYS BE DATE-STAMPED AS SUCH.** Its docket source stops there (§1). **It covers nothing about the preliminary hearing, the June 2026 contempt matter, or the 2026-04-17 evidentiary hearing.**

---

## §0 · Sourcing framework (project standard)

**Tier 1** — sworn testimony and primary court filings/documents · **Tier 2** — named official statements · **Tier 3** — named journalistic reporting/analysis · **Tier 4** — anonymous-source or low-verification material. **"T1 via T3"** marks primary content known only through reporting.

**Source marks used in §2:** **[D]** = read directly from a banked primary document · **[X]** = **XChange docket printout only** — title and date established, **document unread**.

⚠️ **[X] is weaker than it looks.** The XChange printouts are court-system *output about* the docket, whose generation route this project has never independently confirmed (CR-ACQ-2026-08-14C §1), and which are subject to **standing hazard 13** — `grep` fails silently and totally on them (CR-ACQ-2026-08-16 §6.1). Every [X] row here was read in Python, not grepped.

---

## §1 · Access-path caveats, first

| | |
|---|---|
| **What the map is built from** | Ten banked primary documents read in full, plus the 31-page XChange full case history. Acquisition record: **[CR-ACQ-2026-08-16](CR-ACQ-2026-08-16_documentcloud-complete-sweep.md)**. |
| 🚨 **Ceiling** | **The docket printout ends 2026-03-14.** Every null and every "outcome unknown" below is bounded there. |
| ⚠️ **The docket has no document-number COLUMN** *(corrected 2026-08-16 — the earlier header said "No docket numbers exist in the docket", which is false)* | Both XChange printouts are **date-ordered and have no document-number COLUMN.** 🛠 **CORRECTED 2026-08-16 (CR-REVIEW-2026-08-16B, R1): FOUR DOCKET NUMBERS DO APPEAR — `Dkt. #23`, `Doc. 165`, `Dkt 197`, `Dkt. 325`, six occurrences in EACH printout, embedded inside filing titles the parties typed. The printouts have no document-number COLUMN; the absolute form was FALSE and this library already relied on the contrary (CR-E12 grades Dkt. #23 at High from exactly this source).** Every docket number in this file therefore comes from a **primary filing's own citation** (Tier 1) or from a **DocumentCloud uploader title** (Tier 4 — CR-ACQ-2026-08-16 F-39). The distinction is marked wherever it matters. |
| **Not held** | ⚠️ **NOT ONE ruling on ANY closure or classification motion is held by this project** (§8 N-4). The rulings exist and are named on the docket. This map records what was *sought* and, where the docket says so, what was *ordered* — but it reads no order's terms. |

---

## §2 · THE CLOSURE MAP

| Date | Proceeding / record | What was sought | By whom | Outcome | Granularity | Src | Conf. |
|---|---|---|---|---|---|---|---|
| 2025-09-22 | *Protection Order RE: Pre-Trial and Trial Publicity* | — (entered) | Court | **Entered** | Case-wide; **binds attorneys only** | [X]+[D] | High |
| 2025-09-24 | *Standing Decorum Order* | — | Court | Entered | Courtroom conduct / media | [X] | Med-high |
| **2025-10-15** | **Discovery Protective Order** (stipulated, U.R.Crim.P. 16(d)) | Bar dissemination of all discovery outside the defence team; bar witness PII **even to the defendant** | **Both parties, stipulated** | **Entered** | **The whole discovery corpus** | [D]+[X] | High |
| 2025-10-20 | State's response re civilian clothing | Classify **private** | State | **Granted same day** | Single document | [X] | Med-high |
| **2025-10-24** | **Hearing, 3:00 pm, Ctrm 4B** | Closure | *(not established)* | **CLOSED. Minutes filed `**** SEALED ****`** | **Whole hearing** | [X]+[D] | High |
| 2025-11-03 | Transcript + audio of the 10-24 hearing | Order transcript; classify **private** | **Defence, State stipulating** | Contested by media 12-08; **ruled 2025-12-29** | Two records | [D] | High |
| 2025-11-13 | — | *Order Requiring Parties To Serve All Closure Or Reclassification Motions On The Media* | Media | **Entered** | Procedural, case-wide | [X]+[D] | High |
| 2025-11-17 | TRANSADMIN transcript | — | — | Filed **`**** PROTECTED ****`** | Single record | [X] | Med-high |
| 2025-11-17 | Petition for permission to appeal (interlocutory) | — | Defendant | Filed **`**** PRIVATE ****`**; **denied by Utah S. Ct. 2026-01-02** | Single document | [X] | Med-high |
| 2025-12-04 | Joint status report on **redacting portions** of the 10-24 sealed transcript | Redaction rather than total suppression | Both parties | — | Portions of one transcript | [X] | Med-high |
| 2025-12-10 | Motion to Disqualify **+ exhibits** | Classify **private**; **closed hearing** | Defence | Filed private; order entered **2025-12-19** *"Pending Closure Hearing"* | Document set | [X] | Med-high |
| **2025-12-11** | **Review / oral-argument hearing** | Partial closure | Court's own agenda | **PARTIALLY CLOSED — first segment closed (12:12–2:19), remainder open. Gallery excused. A request that the family be allowed to remain was DENIED** | **Time-segment of a hearing** | [X] | High |
| 2025-12-19 / 12-31 | 12-11 hearing transcripts | Order + **temporarily** classify private | Defence | **Granted**; filed `**** PRIVATE ****` | Two records | [X] | Med-high |
| 2025-12-24 | **Minute order for the 12-11 hearing itself** | — | Court | Filed **`**** SEALED ****`** | Single court record | [X] | Med-high |
| 2025-12-29 | *Ruling And Order Re Stipulated Motion To Classify Transcript And Audio As Private* | — | Court | **Entered** — court gives findings on what shall be public and what shall remain sealed | Mixed | [X] | High |
| 2025-12-29 | **Redacted** transcript of the 10-24 sealed hearing | — | — | **Filed `**** PRIVATE ****`** | Single record | [X] | Med-high |
| 2025-12-29 | Media's request to intervene | Limited-intervenor party status | Two media groups | **DENIED**; standing R. 4-202.04 notice order entered instead | Party status | [X]+[D] | High |
| 2026-01-05 → 01-09 | Opposition to disqualification; partial reply; a defence motion + exhibits | Filed non-public / classify private | Both | 01-09 classification ordered 2026-01-12; the wider contest **still pending at the ceiling** | Document sets | [X] | Med-high |
| **2026-01-16** | **Oral argument, disqualification** | **Close the hearing** | **State moved; defence "not opposed"; media counsel heard** | 🚨 **COURT DENIED** blanket closure; will proceed **"on a witness by witness basis as to closure."** State sought reconsideration; **court refused** | 🚨 **Origin of witness-level granularity** | [X] | High |
| 2026-01-16 | Motion to Exclude Still Photographers / TV Cameras / Mics | Filed non-public + **classify private** | Defence | Opposed by **State and media**; unresolved at the ceiling | Single document | [D]+[X] | High |
| 2026-01-29 → 02-23 | **Attorneys'-eyes-only access to closure motions** | Media access | News media | **GRANTED 2026-02-23** | **An access tier between public and sealed** | [X] | Med-high |
| 2026-02-02 | Proffer of facts re **closure of portions** of the evidentiary hearing | Close the testimony of **"Prosecutor A"** and **"Adult Child"** under UCJA 4-202(2)(A),(B),(E) | **State**, defence not objecting | *(see 02-03)* | **Named-witness level** | [D] | High |
| **2026-02-03** | **Continued evidentiary hearing** | Close for *"the next witness"* | **Defence**, State stipulating | **"denies in part and grants in part"**; a witness identified in the record only by initials then testified | **Single witness** | [D] | High |
| **2026-02-03** | same hearing | Close for *"the next witness"* | **State**, defence stipulating | 🚨 **DENIED outright.** **Chad Grunander then testified in open court** | **Single witness** | [D] | High |
| 2026-02-10 | Redacted 12-11-2025 transcript | — | — | Filed **`**** SEALED ****`** | Single record | [X] | Med-high |
| 2026-02-23 | *Order On February 3, 2026, Hearing Transcript* | — | Court | **Entered** — terms unknown | One transcript | [X] | Med-high |
| 2026-02-23 | *Standing Order On Redacting And Filing Transcripts* | — | Court | **Entered** | 🚨 **Case-wide transcript regime** | [X] | Med-high |
| 2026-02-26 | **Portions of the 2026-04-17 evidentiary hearing** | Prospective closure | Defence | State responded 03-11; media opposed 03-12. **Outcome beyond the ceiling** | Portions of a hearing | [X] | Med-high |
| **2026-03-13** | 🚨 ***Rulings And Orders On Classification And Closure Motions*** | — | Court | **ENTERED, signed. NOT HELD.** Last substantive entry before the printout ends | **Omnibus** | [X] | Med-high |
| 2026-07-08 | Exhibits admitted at the **open** preliminary hearing but **not published to the courtroom** | Order them displayed | **Victim's family, via counsel** | Outcome not held | **Exhibit level, inside an open hearing** | [D] | High |

---

## §3 · F-62 — Closure here operates at FIVE granularities, not one. Confidence: High.

**Whole hearing** (2025-10-24) · **time-segment** (2025-12-11, 12:12–2:19) · **single witness** (2026-02-03, twice, with opposite outcomes) · **single document** (throughout) · **single exhibit inside an open hearing** (2026-07-08).

⚠️ **This corrects this library's own scoping.** CR-E10's F-36 recorded that closure is granular "at the witness level, not the hearing level." **That is right but under-scoped by three levels**, and a map built only at witness level would miss both the strictest lock in the case (§6.2) and the subtlest one (§5).

## §4 · F-63 — 🚨 The witness-by-witness rule originates 2026-01-16, not 2026-02-03 — and the COURT imposed it over the agreement of every party. Confidence: High.

At the 2026-01-16 hearing the **State moved to close**; the **defence stated it was not opposed**; media counsel was heard; and the **court denied the request**, stating it would take the matter *"on a witness by witness basis as to closure."* The State sought reconsideration and the court's position was unchanged.

⚠️ **Two corrections follow.** (a) **CR-E10's F-36 dates the granularity to 2026-02-03** — that is the first *instance*, not the *origin*. (b) More importantly, **the mechanism is not what it looked like.** Closure here is **constrained by the court against unanimous party stipulation**, not negotiated between adverse parties. **On 2026-02-03 the court denied a closure request that BOTH parties supported, and Chad Grunander testified in open court as a result.** Any account describing the parties as jointly narrowing public access has the direction of pressure backwards.

## §5 · F-64 — 🚨 OPEN ≠ OBSERVABLE, and no closure order is responsible for it. Confidence: High.

The victim family's 2026-07-08 supplemental notice records that at the **open** preliminary hearing *"the Kirk family sat in the room while evidence was admitted but not presented for their viewing,"* and asks the court to order that exhibits **not published to the courtroom** be displayed.

**Exhibits can be admitted into an open record without ever being shown.** ⚠️ **Consequence for this library, and it is large:** the five hearing-day transcripts it holds may reference exhibits whose content **was never rendered anywhere retrievable** — not because anything was sealed, but because nothing was displayed. **This is a sixth bound, and the library had no concept of it.** It bears directly on **Q-51 / State's Exhibit 11 (the ME report)**, on **Q-67**'s fifteen exhibit designators, and on **Exhibit 12.1**, which CR-ACQ §8 already records as admitted but withheld from publication.

## §6 · What this BOUNDS — obtainable versus permanently out of reach

### 6.1 Structurally unobtainable — the reason is not access-path, it is the record

1. 🛠 **THE 2025-10-24 HEARING — CLOSED, BUT *NOT* UNOBTAINABLE, AND v1.0 OF THIS FILE WAS WRONG TO LIST IT HERE.** *(Corrected 2026-08-16, Q-105 re-run.)* The hearing was closed, its minutes filed `**** SEALED ****`, and its transcript and audio classified; **the redacted transcript was filed `**** PRIVATE ****` on the docket on 2025-12-29 — so the redaction exercise produced no public *docket* record.** 🚨 **BUT THIS LIBRARY HOLDS A 97-PAGE TIER 1 REDACTED TRANSCRIPT OF IT, AND HAS SINCE 2026-07-27** — `CR-ACQ-2026-07-27_court-record-artifacts/oct24_clean.txt`, 176,171 characters, captioned *"REDACTED TRANSCRIPT OF: SEALED MOTION HEARING BEFORE THE HONORABLE TONY GRAF … OCTOBER 24, 2025"*, reported by a certified court reporter, **banked and SHA-256-verified**, and summarised at **CR-ACQ-2026-07-27 §4**. ⚠️ **The hearing's content is available to this project and must never again be described as structurally unobtainable.** What remains unobtainable is the **unredacted** record and the sealed minutes. 🚨 **How the error happened, because the mechanism generalises: a docket-derived observation was promoted into a claim about this library's holdings.** The docket shows what the court filed and classified. **It is not evidence of what this project possesses** — and a completeness pass against the artifacts folder would have caught it, while a pass against the docket never could. **Two other nulls in this file failed the same way** (§9 N-6, §9 N-4). ⚠️ **And the transcript bears on §4/F-63:** on 2025-10-24 the court stated that *"these hearings, unless there is mention of it needing to be a closed hearing, **the assumption is they will be open hearings** unless the parties bring compelling reasons to close them,"* and defence counsel proposed *"just have everybody leave and seal like a portion of the hearing."* **F-63's origin dating for the witness-by-witness RULE survives** — this is a precursor, not an instance — **but the open-by-default presumption and sub-hearing granularity were articulated on the record twelve weeks earlier than this file recorded.** ⚠️ **`oct24_clean.txt` is cited by no evidence file in this library. It should be read in full → Q-110.**
2. **The closed segment of 2025-12-11 — the strictest lock in the case.** Transcripts `PRIVATE`; the redacted version `SEALED`; and **the minute order for the hearing is itself `SEALED`.** Minutes, transcript and redacted transcript are all restricted.
3. 🚨 **The entire discovery corpus.** The stipulated Discovery Protective Order bars sharing discovery *"with any person or entity outside of the defense team"* and bars witness PII **even from the defendant himself**, reaching recorded interviews, photographs, and psychological/medical reports. **No route through the parties exists for any discovery material, ever, absent modification of the order.** **This is the single largest bound and the library should treat it as terminal.**
4. **The private originals of the merits filings** — the Motion to Disqualify and exhibits, the State's opposition, the partial reply, the 2026-01-09 motion, the camera motion. ⚠️ **Important nuance: "filed private" ≠ "no public version."** Public or redacted counterparts exist and this library **already holds several** (CR-E11 §1). **It is the unredacted originals that are unobtainable.**
5. **Whichever portion of one witness's 2026-02-03 testimony the court's "grants in part" covered** — and ⚠️ **what that portion was is NOT established** (§8 N-2).

### 6.2 F-65 — Three classification states operate here, not two. Confidence: Medium-high.

`**** PRIVATE ****`, `**** SEALED ****` and `**** PROTECTED ****` all appear as distinct docket markers. **This library has been treating classification as a binary.** "PROTECTED" is a **third state it has never recorded** 🛠 *(EXTENDED 2026-08-16: it appears **TWICE, and the two printouts DISAGREE** — the SHORT printout marks the **2025-12-11 REVIEW HEARING AND ORAL ARGUMENT** as `**** PROTECTED ****`, while the FULL printout carries **no marker at all** on that entry and renders it as an unmarked minute entry with full narrative. 🚨 **Two XChange printouts of the same docket assign different classification markers to the same record — a calibration fact about `[X]` sourcing generally.** And PROTECTED attaches to a **hearing**, not only to a transcript.)*, and plausibly maps to GRAMA § 63G-2-305, invoked in the discovery motion as to victim address, telephone and impact statements. ⚠️ **The mapping is inference; the three-state fact is not.** → **Q-92.**

### 6.3 F-66 — The media hold a real access tier short of intervention. Confidence: Medium-high.

Intervention was **denied** 2025-12-29 and replaced with a standing notice order. Then on **2026-02-23** the court **granted** the news media's motion to amend that order **and** its motion for **attorneys'-eyes-only access to closure motions**. **Closure motions are therefore visible to media counsel and to no one else** — a tier between public and sealed. ⚠️ **This bounds what any journalist-sourced account of this litigation can contain**, and is a calibration fact for every Tier 3 source the library reads on the closure fight.

---

## §7 · The instrument inventory — four confusably-named orders, entered within 29 days

| Dkt | Instrument | Authority | Entered | Binds | Restricts | Held? |
|---|---|---|---|---|---|---|
| **#7** | *(Proposed)* Pretrial Protective Order | Utah Code **78B-7-803** | filed 2025-09-16, **unsigned** | — | *(proposed)* | ✅ |
| **#14** | **Pretrial Protective Order** *(entered)* | **78B-7-803** | **signed 2025-09-16, 08:22:46 PM** | **The defendant** | No-contact, stay-away, residence exclusion, firearm restriction, as to a named protected person | ✅ |
| **#23** | **Protection Order RE: Pre-Trial and Trial Publicity** | R.P.C. 3.6 / inherent power | **signed 2025-09-22** | **Attorneys only** | Extrajudicial statements | ❌ **(Q-71)** |
| *(unnumbered)* | **Discovery Protective Order** | **U.R.Crim.P. 16(d)** | **signed 2025-10-15**, stipulated | **The defence team** | The whole discovery corpus + witness PII | ❌ *(only the motion is held)* |

**Docket-number confidence, stated separately from instrument identity:**
- **#23 — High.** Two independent primary citations: the State's own 2025-11-06 motion title referring to *"(Dkt. #23)"*, and Judge Graf's 2025-12-15 ruling citing it twice 🛠 *(corrected 2026-08-16: the two citations read **`(Dk. 23)`** and **`(Dkt. 23)`**. ⚠️ Unresolved between OCR artifact and original — `dkt242` is a noisy image-scan extraction (`attormeys`, `goverment`, `itis`) with **no form feeds**, so its page-level completeness is unverified. **The #23 High grade is unaffected: two independent primary citations exist.**)*.
- **#7 and #14 — Medium-high.** Their numbers rest on DocumentCloud titles **plus an ordinal reconstruction** run against the docket: numbering `Filed:` entries sequentially from the Information, **four anchors land exactly** (PSA = 3, Bail Order = 4, Proposed order = 7, Victim-representative request = 12, entered order = 14). ⚠️ **The reconstruction does NOT generalise: continued forward it predicts 19–20 for the publicity order, which the record establishes as 23.** It corroborates the 2025-09-16 cluster and **must not be used as a docket-numbering method.**

**F-67 — 🚨 A second pretrial protective order may exist, and this library cannot tell. Confidence: unverified — this is an open question, not a finding.** The docket records *"09-23-2025 Filed protective order: Pre-Trial Protective Order — Signed September 23, 2025,"* with a return of personal service on the defendant the same day. **The banked instrument is signed September 16.** **Nothing in the banked document indicates amendment or supersession.** Whether these are one order re-issued for service or two successive orders is **not established**. ⚠️ **Any file citing "the pretrial protective order" must now state which signature date.** *(Opened as D-63 at CR-ACQ-2026-08-16 §4.)*

---

## §8 · Three contradictions the library was carrying — all three resolved

### 8.1 Docket #14 — **RESOLVED: there was never a conflict.** Confidence: High.

CR-E09's F-30 described #14 as a *victim no-contact order*; the DocumentCloud title calls it *"Order Pretrial Protective Order."* **Both are correct and describe the same instrument.** The title is a verbatim copy of the docket's own entry text; the document is Utah form **1501POF**, signed 2025-09-16 at 08:22:46 PM, imposing no-contact, stay-away, residence-exclusion and firearm terms on the defendant as to a named protected person. **The library's characterisation is an accurate *substantive* description; DocumentCloud's is the *docket title*. The apparent contradiction was nominal.**

⚠️ **But the hazard it pointed at is real and wider than the pair.** *"Pretrial **Protective** Order"* (#14, victim), *"**Protection** Order RE: Pre-Trial and Trial Publicity"* (#23, attorneys) and *"Discovery **Protective** Order"* (10-15, discovery) are three different instruments entered within 29 days. **CR-E09's F-30 caught the first pair; the discovery order is a third member of the set the library never flagged as such.**

**F-68 — The court entered the parties' proposed pretrial protective order verbatim. Confidence: High.** A normalised diff of #7 against #14 returns **character-identical text** 🛠 *(corrected 2026-08-16: **7,786** characters, not 7,798 — the figure is recipe-dependent, and the recipe that yields exact identity strips page furniture, the six `PROPOSED` watermarks, the form footer, page numbers and the signature stamp. **Similarity 1.00000 — the identity finding is unaffected.**)* once page furniture, the PROPOSED watermark and the signature stamp are stripped. Every checkbox and every blank field matches. ⚠️ **This is a fact about this instrument, not a habit of this court** — on the preservation order the court did **not** adopt the proposal verbatim (CR-E13 §4).

### 8.2 The "2-13-2026" minute order — **RESOLVED: the DocumentCloud title is a typo, and the library has a phantom acquisition target.** Confidence: High.

Read off the document face: **the hearing was February 3, 2026**; **the minute order was entered February 23, 2026 at 01:43:54 PM**. A minute order legitimately postdating its hearing by 20 days.

🚨 **But "2-13-2026" is neither date, and no such entry exists.** Every February 2026 docket entry was listed: the sequence runs **02-12 → 02-19 🛠 **CORRECTED 2026-08-16 (R2): February 2026 actually runs 02-02 → 02-26, fourteen distinct dates. The true fact is a GAP between 02-12 and 02-19. The conclusion (no 02-13 entry) survives; the stated basis did not — and 12 of the 14 February dates fall outside the range as written, including 02-23/02-24 which carry the disqualification denial.****. There is **no 2026-02-13 entry of any kind in this case.** The docket instead carries a 02-23-2026 order matching this document. **"2-13-2026" is an uploader transcription error for 2-23-2026** — a third confirmed instance of CR-ACQ-2026-08-16's F-39.

**F-69 — 🚨 A DEFECT IN THIS LIBRARY'S OWN FILE, and it inflates a coverage count. Confidence: High.** **CR-E10 lists "the 2026-02-13 minute order" among Q-70's UNREAD documents while simultaneously treating Dkt. 413 as READ. They are the same document.** Consequences: **CR-E10's Q-70 coverage count (14 of 46) is inflated by one**, and **Q-70 has been carrying a phantom acquisition target since 2026-08-14.** **Corrected in place at CR-E10 v1.3, 2026-08-16** — both the Q-70 row and the F-36 scope, with matching revision-log rows.

### 8.3 `dkt197` vs docket 213 — **RESOLVED: the local filename is wrong.** Confidence: High.

The document is captioned *"…RESPONSE TO THE MOTION FOR LIMITED INTERVENTION OF DESERET NEWS, ET AL. **(Dkt 197)**"* — **and then pin-cites into "Dkt 197" across six distinct pin locations** (`at 1-2`, `at 3-4`, `at 4 & n.1`, `at 5`, `at 6-7`, `at 7`) 🛠 *(corrected 2026-08-16: **eight pin-cites**, since `at 1-2` and `at 6-7` each occur twice, plus the caption and one bare cite — **ten references in total**. The list of six distinct pins is right; "six times" was not. **The conclusion is unaffected and slightly strengthened.**)*. **A document cannot pin-cite its own pages as another party's argument.** Dkt 197 is the media's motion of 2025-11-24; **the response is docket 213.** Corroborated by a *later* docket entry that also carries "(Dkt 197)" in its title for the same citational reason. *(Generalised as F-40 at CR-ACQ-2026-08-16 §4 → Q-80.)*

---

## §9 · Scoped nulls

- **N-1 — No docket entry dated 2026-02-13 exists.** Scope: every February 2026 entry in the 31-page XChange full case history, read in Python (hazard 13), whitespace-normalised. **Does not exclude anything after 2026-03-14.**
- **N-2 — What the 2026-02-03 "grants in part" actually covered is NOT established.** The minute order records the disposition, not its terms. ⚠️ **No file may state that the witness's testimony was closed.** Resolvable only by the 2026-02-03 transcript or the closure rulings.
- **N-3 — The proffer's pseudonyms are NOT mapped to the witnesses who testified. Grade: unverified.** ⚠️ **Steelman recorded and expressly not adopted:** the strongest reading is that "Prosecutor A" is the prosecutor who testified in open court on 02-03 and "Adult Child" the witness recorded by initials. **That reading is coherent but rests on inference across two documents that never join.** Settled only by the 02-03 transcript or the closure rulings.
- 🛠 **N-4 — NARROWED 2026-08-16. No ruling on any WRITTEN closure or classification motion is held, and NO closure ruling's TERMS are held anywhere.** ⚠️ **The absolute form was wrong:** the **2026-02-03 minute order (`dkt413`) IS held, IS signed by the judge** (*"The Order of the Court is stated below … /s/ TONY F GRAF JR District Court Judge"*) **and DOES record two closure dispositions** — *"denies in part and grants in part the request for the hearing to be closed"* and *"denies the request to close the hearing for the next witness."* **§2 of this file already sources both outcomes to `[D]` at High.** ✅ **Steelman adopted:** both requests were **oral**, so no ruling on a *written filed* closure motion is held — and `dkt413` records the dispositions **only, not their terms or reasoning** (N-2). ⚠️ **§1's gloss — "where the docket says so, what was ordered" — is also inaccurate for the 02-03 rows, where the outcome comes from a held document, not the docket.** *(Original:)* **NOT ONE ruling on ANY closure or classification motion is held.** Scope: the full 46-document bank plus everything else in the artifacts folder. **At least ten such rulings are named on the docket** (2025-12-19 ×2, 2025-12-29 ×2, 2026-01-12, 2026-02-23 ×4, **2026-03-13**). **This map therefore records what was sought and what the docket says was ordered — and reads no order's terms.**
- **N-5 — Dkt. 366 contains no closure or classification argument at all.** Scope: all 14 pages read in full. Its only media-adjacent content is a footnote. *(A prior working assumption that it carried a closure limb is not borne out.)*
- 🛠 **N-6 — CORRECTED 2026-08-16: the DOCKET establishes closure status for no proceeding after 2026-03-14.** Scope: the docket's own ceiling — ⚠️ **this null is about the DOCKET, not about this library's holdings**, and v1.0 stated it the wrong way round. 🚨 **Held records outside the docket DO establish some post-ceiling status:** the 2026-07-08 supplemental notice is captioned *"…ACCESS TO EVIDENCE PRESENTED IN **OPEN COURT**"*, carries **zero** hits for `clos*`/`seal*`/`privat*`, and seeks relief predicated on openness — **and §2 and §5 of this very file already rely on it, describing "the OPEN preliminary hearing."** The publicly-published 2026-06-23 contempt-matter transcript (CR-ACQ-2026-08-14) likewise establishes that proceeding was not closed. ✅ **One limb survives intact: the outcome of the 2026-02-26 motion to close portions of the 2026-04-17 evidentiary hearing remains unestablished** — fully briefed (State 03-11, media `**** PRIVATE ****` 03-12) and undisposed at the ceiling.

---

## §10 · Living-persons and PII

- **A witness identified in the court's own minute order only by initials** — that is the court's privacy measure. ⚠️ **This library does not attempt to resolve it.**
- **The closure proffer contains a detailed account of threats, doxing and dark-web targeting directed at a prosecutor and his family**, and describes **defence counsel's private security arrangements** and two agencies' security-protocol changes. ⚠️ **The security *rationale* is summarised above; the threat mechanics and operational-security specifics are NOT reproduced.**
- **Private third parties described but unnamed** — a prosecutor's family member; children of two congregation members. **They bear on the disqualification question only and no further detail is sought.**
- **The minute order prints the defendant's full date of birth**; the protective orders carry residence/school/workplace fields for a protected person (**blank** in the banked copies). **None is reproduced.**
- **Media counsel's email addresses** appear in a certificate of service and are not reproduced.
- ⚠️ **A garble for the normalisation list:** a minute entry renders defence counsel's surname as **"Bury"** for **Burt**. Add alongside *"Erica"→Erika* and the *"Dyer/Nyman"→Neiman* family.

---

## §11 · Findings, resolutions and open items

**Q-75 is EXECUTED, not closed.** The map exists, at the granularity the record actually uses, with its ceiling stated. **What it cannot do is state outcomes**, because no closure ruling is held (N-4).

🚨 **The single most consequential unheld document in the entire case-record track is the 2026-03-13 *"Rulings And Orders On Classification And Closure Motions."*** It is the **omnibus disposition** of the whole January–March classification contest and the **last substantive entry before the docket printout ends.** **Until it is read, no statement about the final classification status of any 2026 filing is safe** — including whether the camera motion and the 2026-01-09 defence motion ended public or private. → **Q-93.**

**Acquisition roadmap, priority order:**

| | Target | Date | Why |
|---|---|---|---|
| **B-1** 🚨 | ***Rulings And Orders On Classification And Closure Motions*** | 2026-03-13 | The omnibus disposition. Everything else in this map is provisional without it. |
| **B-2** | *Standing Order On Redacting And Filing Transcripts* | 2026-02-23 | **The case-wide transcript regime** — governs every transcript this library will ever seek. |
| **B-3** | *Ruling And Order Re Stipulated Motion To Classify Transcript And Audio As Private* | 2025-12-29 | Resolves the 10-24 transcript; closes **CR-E10 F-35**. |
| **B-4** | **Docket #23** — the publicity order | 2025-09-22 | Already **Q-71**; the attorney-statements limb remains unread. |
| **B-5** | The **entered** Discovery Protective Order | 2025-10-15 | Only the parties' proposed terms are held; the largest bound in the case rests on an unread order. |
| **B-6** | *Order On February 3, 2026, Hearing Transcript* | 2026-02-23 | Would settle **N-2** and **N-3**. |
| **B-7** | Rulings on the media's amend / attorneys'-eyes-only motions | 2026-02-23 | Defines the media's actual access tier (**F-66**); disposes of **Q-77**. |
| **B-8** | 🚨 **A CURRENT DOCKET** | — | **The biggest gap is not a document but a date range.** Everything after 2026-03-14 is unmapped. **Q-31 (👤, $10 XChange) would close this in one act.** |

---

## §12 · Residual scope

This file did not read: any closure or classification ruling (none is held); docket #23; the entered discovery protective order; the 2026-01-16 or 2026-02-03 transcripts; any sealed or private filing. It did not establish the docket number of any instrument other than #23 at High. It did not resolve the initials-identified witness and **did not attempt to.** It did not map the proffer's pseudonyms. It assessed no motion's merits. **It did not verify the DocumentCloud titles against DocumentCloud** — the two title errors were tested **against the documents and the docket**, which is what settled them.

**Case posture untouched: as of 2026-08-16 Tyler James Robinson has NOT been bound over; the presumption of innocence applies throughout.**

> 🛠 **Posture updated 2026-09-16 (owner's ruling).** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full. *The sentence above is retained as written, true as of its date; the ruling is `START-HERE` §0AH item 4 and `DOCKET-WATCH.md` v2.6.*

---

## Revision log

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-08-16 | Created. **Q-75 executed.** F-62 → F-69 opened; Q-91 → Q-93 raised. **Corrects two of this library's own findings:** CR-E10 F-36 is under-scoped (closure runs at five granularities, not one) and mis-dates the witness-by-witness rule's origin (2026-01-16, not 02-03 — and the court imposed it *against* unanimous party stipulation). **F-69 finds a phantom acquisition target in CR-E10 that inflated Q-70's coverage count.** Resolves three carried contradictions (docket #14; the "2-13-2026" title; `dkt197` vs 213). **F-64 states a bound the library had no concept of: open ≠ observable — exhibits can be admitted in open court and never displayed.** `[PROVISIONAL]`. |
| v1.1 | 2026-08-16 | 🚨 **Q-105 RE-RUN — 3 REFUTED, 8 NARROWED, and the worst defect was not a null battery at all.** **§6.1 listed the 2025-10-24 hearing as *structurally unobtainable* while this library has held a 97-page Tier 1 redacted transcript of it since 2026-07-27** (`oct24_clean.txt`, 176 KB, SHA-256-verified, summarised at CR-ACQ-2026-07-27 §4) — **cited by no evidence file** → **Q-110**. 🚨 **Root cause, and it generalises: a docket-derived observation was promoted into a claim about this library's HOLDINGS. The docket is evidence of what the court filed and classified, not of what this project possesses — and TWO other nulls here failed the same way (§9 N-6, §9 N-4).** **N-6 corrected** (the preliminary hearing and the June contempt matter are both established OPEN by held records the file already relies on; only the 2026-04-17 limb survives). **N-4 narrowed** (`dkt413` **is** a held signed order recording two closure dispositions — the steelman that saves the null is that both requests were **oral**). **§6.2 extended: `PROTECTED` appears TWICE and the two printouts DISAGREE about the same record** — a calibration fact about `[X]` sourcing. F-68's char count, the `(Dk. 23)` form and the pin-cite count corrected. ✅ **21 nulls CONFIRMED, logged deliberately** — including F-63/F-64's basis, F-67, and the 2026-03-14 ceiling. ⚠️ **F-63's origin dating for the witness-by-witness RULE survives, but the open-by-default presumption was articulated on the record twelve weeks earlier.** |
| v1.2 | 2026-08-16 | ⚠️ **§0.1 PROVISIONAL DEPENDENCIES added (LOOP §2 discipline).** 🚨 **Records the direction of travel: CR-E10 was revised to v1.3 on THIS file's provisional F-62/F-63/F-69** — provisional→provisional, so **no verified file was contaminated** (CR-E05/CR-E06 untouched), **but it is the propagation LOOP §2 forbids and CR-E10's rows must be re-checked when Q-91 clears.** |
| 1.3 | 2026-09-16 | **Posture line updated to the owner's ruling of 2026-09-16.** The case-posture banner/statement now carries, beneath the sentence it had: *Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full.* The earlier sentence is retained as written (true as of its date). No finding, grade, label or citation changed. |
