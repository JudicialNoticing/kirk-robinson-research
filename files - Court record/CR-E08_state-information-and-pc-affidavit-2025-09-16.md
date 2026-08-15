# CR-E08 — The State's Information and Affidavit of Probable Cause, 2025-09-16

**File ID:** CR-E08
**Scope:** A reasoned read of two primary charging documents — the **Information** (10 pp., authorised for presentment and filing 2025-09-16, sworn by Utah County Attorney Jeffrey S. Gray) and the **Affidavit of Probable Cause** (3 pp., submitted 2025-09-12 by Brian Davis, Utah State Bureau of Investigation). Covers identity and provenance, a recording-layer inventory of what the State alleges, and an analyst-layer assessment of what these documents do and do not establish. **It does not assess the merits of any charge, and it does not touch case posture.**
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr.
**Prepared:** 2026-08-14
**Status/version:** v1.0 — ⚠️ **findings `[PROVISIONAL]`; no independent verification cycle has run on this file.**

> ⚠️ **AS OF 2026-08-14, TYLER ROBINSON HAS NOT BEEN BOUND OVER FOR TRIAL. PRESUMPTION OF INNOCENCE APPLIES THROUGHOUT.** The documents read here are **the State's own accusatory filings**. Every factual assertion in them is **an allegation by a party**, recorded faithfully below and **adopted nowhere**. A charging document is an accusation, not a finding; no court has found any of it true. Nothing in this file resolves any disputed fact.

---

## §0 · Sourcing framework (project standard)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material
- **"T1 via T3"** — primary-document content known only through reporting. Never silently promoted.

**These documents' grade: T1 (held and read directly).** ⚠️ **This is the first filing BY THE STATE that this project holds as a document.** Until now the State's theory was available only through its opponent's description — the position CR-E07 recorded as **F-15**. That position is now **partly cured**, and the cure has a hard limit: **these are the charging documents of September 2025, not the State's 2026-07-28 preliminary-hearing brief**, which remains unheld (Q-45).

## §1 · Access-path caveats — first, per project standard

| | |
|---|---|
| **How obtained** | DocumentCloud API (open), documents **27880532** (Information) and **27880530** (PC affidavit), both inside project **224251**; PDFs and text pulled from `s3.documentcloud.org`, retrieved **2026-08-14** |
| **Banked** | `2025-09-16_information-charging-document_dc27880532.pdf` / `.txt` · `2025-09-16_affidavit-of-probable-cause_dc27880530.pdf` / `.txt`, all in the CR-ACQ artifacts folder. SHA-256s recorded in the acquisition note; **the API `file_hash` values for the uploaded originals are `8218cb86…5e1c` (Information) and `926a764f…bbe1` (affidavit)** |
| **Hash discipline** | ⚠️ **The served PDFs are DocumentCloud RE-RENDERS, not the uploaded originals.** Compare only against the API `file_hash` field, never against the served bytes (the trap logged at CR-WATCH-log v1.3) |
| **Provenance** | **Information: two of three.** Signature block ✅ (*"Sworn to by: JEFFREY S. GRAY, Utah County Attorney"*), authorisation line ✅ (*"Authorized for presentment and filing on September 16, 2025"*), **clerk file-stamp ❌ not visible in the text layer.** **Affidavit: electronically submitted**, carrying `/S/ Davis, Brian`, a submission timestamp of `09/12/2025 07:18`, an OTN and booking identifiers — **court-system metadata rather than a clerk stamp.** ⚠️ **Neither is a court-stamped copy; both are recorded as document text, not silently promoted** |
| **Uploader** | user **144356** / org **87307** — ⚠️ **identity NOT established**; the anonymous API returns no names |
| ⚠️ **DELIBERATELY NOT REPRODUCED** | **Both documents print the defendant's full home address and date of birth on their face.** Neither appears anywhere in this file. They bear on no public question this library investigates, and the project standard bars reproducing residential and identifying detail for living persons **even when the source publishes it.** A researcher needing them has the banked documents |
| ⚠️ **Private individuals** | The documents recount statements by **Robinson's mother, his father, and a family friend described as a retired deputy sheriff**, and describe **his roommate**. **None is named in either document** *(the roommate's identity is established elsewhere in this library, not here)*. Their accounts are recorded below **only where they bear on the public questions under investigation**, in the minimum words, attributed and adopted nowhere |
| **Not consulted** | The exhibits, the photographs, the surveillance recordings, the note, the messages in native form, the ME report (*"pending"* as of 2025-09-16), and **the State's 2026-07-28 brief** |

---

## §2 · Recording layer — what the State alleges

**Faithfulness to the claim is the standard here, not correctness.** These are the State's allegations.

### 2.1 The charge structure, at source

**Seven counts.** Count 1 **Aggravated Murder**, a capital felony (§ 76-5-202); Count 2 **Felony Discharge of a Firearm Causing Serious Bodily Injury** (§ 76-11-210(2),(3)(c)); Counts 3 and 4 **Obstruction of Justice**, 2nd degree (§ 76-8-306(2)) — **3 for concealing or removing the firearm (09-10), 4 for destroying, concealing or removing the clothing (09-11)**; Counts 5 and 6 **Tampering with a Witness**, 3rd degree (§ 76-8-508) — **5 for directing the roommate to delete incriminating text messages (09-10), 6 for directing the roommate to stay silent if questioned by police (09-11)**; Count 7 **Violent Offense Committed in the Presence of a Child**, class A misdemeanour (§§ 76-3-203.10(2), 76-3-203.14(3)(a)(ii)).

**⚠️ THE AGGRAVATING CIRCUMSTANCE, VERBATIM AND SINGULAR.** Count 1 charges that the defendant *"intentionally or knowingly caused the death of Charlie Kirk **under the following circumstance: (iii) the defendant knowingly created a great risk of death to another individual other than Charlie Kirk and the defendant**."* **One circumstance is pleaded, and only one.**

**The enhancements, and which counts carry them.** The **victim-targeting enhancement** (§ 76-3-203.14(2) — *"intentionally selected Charlie Kirk because of … belief or perception regarding Charlie Kirk's political expression"*) is pleaded on **Counts 1, 2 and 7**. The **violent-offense-in-presence-of-a-child aggravating factor** is pleaded on **Counts 1 and 2**.

### 2.2 The State's probable-cause narrative (Information §PC)

- **The event and the shot.** A TPUSA event at UVU, *"the first in a series of similar events to be held at college campuses nationwide"*; several hundred attended; Kirk seated under a portable canopy taking questions. *"Approximately fifteen minutes into the event, Mr. Kirk was answering a question about mass shootings by transgender individuals when a gunshot rang out."*
- **⚠️ THE STATE'S KGRD FACTUAL THEORY, IN ITS OWN WORDS.** *"Mr. Kirk's team members were very close to him on his right and left, as well as some behind his canopy… The large crowd surrounded Mr. Kirk on three sides. Temporary metal fencing separated attendees from Mr. Kirk by only a matter of feet. Directly above and behind Mr. Kirk was the UVU Hall of Flags… People were in the walkway at the time of the shooting."* And decisively: ***"The bullet's trajectory passed closely to several other individuals beside Mr. Kirk, including the questioner who was standing directly in front of Mr. Kirk."*** *"Children were visible near Mr. Kirk's stage when he was shot."*
- **The officer and the roof.** A UVU police officer watching from an elevated vantage point, believing from the sound that the shot came from a rifle, *"looked for potential sniper positions,"* noted *"a roof area **approximately 160 yards** away,"* climbed the railing, confirmed *"a clear shooting corridor,"* and noticed *"markings in the gravel rooftop consistent with a sniper having lain on the roof."*
- **The surveillance reconstruction.** Entry to campus ~11:51 a.m.; *"walking with very little bending in his right leg – **consistent with a rifle being hidden in his pants**"*; over the railing onto the roof ~12:15 p.m.; running and low-crawling to the prone position; after the shot, running across the roof *"carrying an item whose shape is consistent with a rifle,"* dropping it in *"a controlled fall,"* picking it up, and running northeast.
- **The rifle.** Found in a wooded area, wrapped in a towel, *"contained one spent round and three unspent rounds. This is consistent with the facts officers observed… — **no shell casings were found on the roof, suggesting a bolt-action rather than an auto-loading weapon**, and only a single round was fired."*
- **The inscriptions.** Four, given in a table: fired cartridge *"NoTices Bulge / OWO What's / This?"*; then *"Hey Facist! / Catch! / [arrow symbols]"*; *"O Bella ciao, / Bella ciao / Bella ciao / Ciao, ciao!"*; and *"If you Read / This, You Are / GAY / Lmao"*.
- **⚠️ THE DNA ALLEGATION, VERBATIM.** *"DNA consistent with Robinson's was found on the trigger, other parts of the rifle, the fired cartridge casing, two of the three unfired cartridges, and the towel."*
- **The surrender.** Robinson *"went to the Washington County Sheriff's Office with his parents and a family friend to turn himself in"* on the evening of 2025-09-11.
- **The family accounts.** His mother saw the published photograph and thought it resembled her son; his father agreed, and believed the rifle *"matched a rifle that was given to his son as a gift."* The parents arranged to meet him; on the State's account *"Robinson implied that he was the shooter"* and, asked why, *"explained there is too much evil and the guy [Charlie Kirk] spreads too much hate."* A family friend, a retired deputy sheriff, was brought in and *"convinced Robinson to turn himself in."*
- **The messages.** A note under a keyboard, photographed by police, and a subsequent text exchange with the roommate, quoted at length — including *"I had enough of his hatred. Some hate can't be negotiated out."*, *"delete this exchange"*, *"Im gonna turn myself in willingly"*, *"you are all I worry about love"*, and *"if any police ask you questions ask for a lawyer and stay silent"*.
- **The residence search.** *"a shell casing with etchings like the etchings found on the shells in the rifle near UVU"*, and *"several targets with bullet holes."*

⚠️ **A characterisation of a private individual, recorded minimally because a party's argument turns on it and not elaborated:** the State's own filings — not merely the defence's account of them — describe the roommate's gender identity and the nature of the relationship, and place that description inside the motive narrative. **CR-E07 recorded the defence's attribution of this framing to the State; these documents confirm the attribution is accurate.** Nothing further about it is reproduced here.

---

## §3 · Analyst layer — what these documents do and do not establish

| # | Statement | Grade | Basis |
|---|---|---|---|
| **B-1** | A charging Information was authorised for presentment and filing on **2025-09-16**, charging seven counts as set out at §2.1 | **High** | Read directly; corroborated independently by the XChange docket (CR-ACQ-2026-08-14C), which lists the same seven charges with the same statutes and offense dates |
| **B-2** | **The Information pleads exactly ONE aggravating circumstance for Count 1 — the KGRD circumstance, § 76-5-202(2)(a)(iii)** | **High** | Read directly from the charging language. ⚠️ **This RESOLVES the open question behind CR-E07's A-4**, which was graded **Medium** solely because "the Information itself is not held by this project." **The defence's characterisation was accurate.** → see F-23 |
| **B-3** | The victim-targeting enhancement is pleaded on Counts 1, 2 and 7; the child-presence aggravating factor on Counts 1 and 2 | **High** | Read directly. Corroborates CR-E07's record of the defence brief's account of the child-presence factor "in connection with Counts One and Two" |
| **B-4** | The State's KGRD factual theory rests on **the bullet's trajectory passing close to identified people**, the crowd on three sides, fencing "a matter of feet" away, and occupants of the Hall of Flags walkway | **High** *as to what the State alleges* | Read directly. ⚠️ **This is an allegation, not a finding. Whether the trajectory did so is contested** — the defence brief asserts the opposite (CR-E07 §2.1) |
| **B-5** | The affidavit charged **three** offences at arrest (2025-09-12); the Information filed four days later charges **seven** | **High** | Both documents read directly. The four added counts are the second obstruction, both tampering counts and the child-presence count |
| **B-6** | The medical examiner's report was **"pending"** as of 2025-09-16 | **High** | Stated in terms. Bears on the Q-51 / D-49 chronology |
| **B-7** | The State's own account attributes the no-casing fact to a bolt-action weapon and a single shot | **High** *as to the State's inference* | Read directly. ⚠️ **The inference is the State's; this file adopts none of it** |

**What these documents expressly do NOT establish, and no reading of them should imply:**
- **That any allegation in them is true.** They are accusatory pleadings. **No court has found any of it.**
- **Anything about the evidence's admissibility, reliability or weight** — all of which was litigated afterwards and none of which these documents address.
- **The State's current position.** These are September 2025 filings; the State's 2026-07-28 preliminary-hearing brief is **still unheld** and may frame the case differently after five hearing days.
- **Any change to case posture.** **Robinson has not been bound over.**

---

## §4 · Findings

**F-23 — The Information pleads exactly one aggravating circumstance, which upgrades CR-E07's A-4 from a party's characterisation to a document-verified fact.**
Grade: **High.** CR-E07 graded A-4 (*"the sole aggravator alleged is KGRD"*) at **Medium**, with the express caveat *"It is a party's characterisation of the Information; the Information itself is not held by this project."* **The Information is now held, and the characterisation verifies against it.** Count 1 pleads circumstance **(iii)** and no other. *What would change it:* an amended Information; the docket (CR-ACQ-2026-08-14C) shows none through 2026-03-14, and the period after is not held.

**F-24 — THE SAME SENTENCE IS QUOTED BY BOTH PARTIES AT DIFFERENT LENGTHS, AND THE TRUNCATION IS DOING THE ARGUMENTATIVE WORK.**
Grade: **High** — both sides read directly from banked primary documents.
The State's Count 6 predicate, quoted in the Information: ***"if any police ask you questions ask for a lawyer and stay silent."*** Full stop.
The defence brief's rendering of the same message (CR-E07 §2.3): ***"If any police ask you questions, ask for a lawyer and stay silent. My lawyer should be Doug Terry, I'll see if he can reach out to you. And make sure the police follow the right procedures, proper warrants and stuff, but be polite and respectful of course."***
**The State charges on the first clause; the defence's "purely altruistic advice" argument runs entirely on the continuation.** Neither is misquoting the words it prints — **but neither document, standing alone, lets a reader see the sentence whole.** ⚠️ **This is standing hazard 1 demonstrated at Tier 1 in both directions on a single sentence**, and it is the cleanest instance this library has recorded. *(Recorded separately: the defence brief itself prints the passage twice with small internal variations, and the two parties render the adjacent media-instruction differently — "don't talk to **the** media" in the Information, "Don't talk to **any** media" in the brief. **Neither party is working from a certified transcript of the messages, and this project holds none.**)*

**F-25 — The State's charging document asserts a DNA proposition in the exact formulation its own laboratory witnesses later disclaimed on the stand.**
Grade: **High** as to what each document says; **this file draws no conclusion about the underlying science.**
The Information alleges: *"DNA consistent with Robinson's **was found on** the trigger, other parts of the rifle, the fired cartridge casing, two of the three unfired cartridges, and the towel."*
On Day 5, the ATF analyst who authored the State's DNA reports **agreed that a headline of the form "Mr. Robinson's DNA is found on this item" is a source attribution and "would not be scientifically defensible"** (CR-E06, VERIFIED).
⚠️ **Two guards, because this finding is easy to over-read.** **(1)** The Information's *"DNA consistent with Robinson's"* is itself hedged — it is **not** the bare source attribution the analyst rejected, and the affidavit uses the same hedge. The tension is in *"was found on"*, not in the whole sentence. **(2)** A charging document written in September 2025 is not bound by testimony given in July 2026, and **nothing here suggests the State knew or should have known otherwise when it filed.** What the finding establishes is narrower and still worth having: **the plain-language formulation the public case was built on is one the State's own expert would not adopt under oath** — which is precisely why this library forbids the formulation in its own voice.
⚠️ **A related precision point, recorded and NOT resolved:** the Information places DNA *"on the trigger."* Day-5 testimony establishes that ATF item 1.3 was **the trigger and trigger guard swabbed together**, with the witness stating she could not say where on that area the DNA came from. **The charging document is therefore more precise than the underlying laboratory evidence supports.** *(Sourced to CR-E06-adjacent Day-5 testimony; the Day-5 completeness harvest carrying it is banked but `[PROVISIONAL]` and not yet verified, so this point is flagged rather than graded.)*

**F-26 — The State's early distance estimate and the later surveyed measurement differ by roughly 65–70 feet, and both are on the record.**
Grade: **Medium-high.** The Information records the officer's contemporaneous estimate of *"approximately 160 yards"* (≈ 480 ft) from the suspected shooting position to Kirk. Sgt. Faumuina's Day 4 testimony gives **approximately 415 ft slope distance, 410 ft horizontal, 68 ft elevation** (CR-E02 §2, where the geometry checks by Pythagoras). ⚠️ **This is not presented as a contradiction:** the first is an officer's on-the-spot estimate expressly qualified as approximate, the second a survey. **Recorded so that no file cites "160 yards" and "415 feet" as though they were independent corroboration of each other — they are one distance, estimated once and measured once.**

---

## §5 · Open items and register

| → | Item |
|---|---|
| **D-60 (new)** | ⚠️ **Discrepancy — the text of the keyboard note versus the text of State's Exhibit 16.3.** The **Information** states police found a note under the roommate's keyboard reading ***"I had the opportunity to take out Charlie Kirk and I'm going to take it,"*** and that *"Police found a photograph of this note."* The **defence brief** quotes **StEx 16.3** as ***"I had the opportunity to take out Charlie Kirk and I took it."*** ⚠️ **The difference is not cosmetic: "I'm going to take it" is a statement of intent written before the act; "I took it" is an admission after it.** **NOT RESOLVED, and it must not be resolved from these two documents alone** — the two may be **separate artifacts** (a handwritten note and a later message), since the defence describes StEx 16.3 as *"communications … between Mr. Robinson and Mr. Twiggs"* while the Information describes a physical note. **Steelman recorded: the defence's own use of the quote — as showing "intention to kill Charlie Kirk" — fits the Information's wording better than its own, which is weak evidence that one artifact is being loosely quoted rather than that two exist.** **Decisive artifact: State's Exhibit 16.3 itself, and the photograph of the note.** Neither is held |
| **Q-69 (new)** | **Obtain State's Exhibit 16.3 and the photograph of the keyboard note** — decisive for D-60 |
| **Q-70 (new)** | **Read the remaining ~42 filings in DocumentCloud project 224251.** Two of the highest-value documents in that project were acquired only after three sweeps read past them (CR-ACQ-2026-08-14C). The rest have never been inventoried |
| **Q-45** | **Unchanged and still the priority for the State's position.** These are the September 2025 charging documents; **the State's 2026-07-28 preliminary-hearing brief remains unheld.** F-15 is **partly** cured, not cured |
| **NEW** | ⚠️ **The four engraved inscriptions now exist in THREE renderings across two State documents and one quoted message** — *"Notices Buldge"* (affidavit), *"NoTices Bulge"* (Information), *"notices bulge uwu"* (the quoted message); *"hey fascist!"* (affidavit) versus *"Hey Facist!"* (Information). **No file may present any one rendering as the inscription's text.** The decisive artifact is the physical cartridge or its photograph |
| **NEW** | The **09-12 affidavit** and the **09-16 Information** give slightly different clock times for the same movements (e.g. first capture ~1150 vs ~11:51 a.m.; roof entry ~1217 vs ~12:15 p.m.). **Recorded; neither is treated as authoritative over the other** |

---

## §6 · Residual scope — what this file did NOT do

- **Did not assess the truth of any allegation**, the sufficiency of the evidence, or the merits of any charge. **These are accusatory pleadings.**
- **Did not read any exhibit, photograph, recording, or the messages in native form** — every characterisation of them is the State's.
- **Did not consult the docket beyond 2026-03-14** (the coverage ceiling of the only docket this library holds), so it cannot say whether the Information was later amended.
- **Did not read the State's 2026-07-28 brief**, which is unheld and is the document that would show the State's *current* framing.
- **Did not verify** any factual assertion in either document against the hearing transcripts, except where expressly noted (the charge structure against the docket; the distance against CR-E02; the DNA formulation against CR-E06).
- **Did not reproduce** the defendant's address or date of birth, or elaborate the private-individual material at §2.2.
- ⚠️ **No independent verification cycle has run on this file. Its findings are `[PROVISIONAL]` and may not be cited elsewhere until one does.**
- **Did not alter any case-posture statement** anywhere in this library, and **moved no existing register entry**.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-08-14** | File created. ⚠️ **THE FIRST FILING BY THE STATE THAT THIS PROJECT HOLDS AS A DOCUMENT** — the 2025-09-16 Information (10 pp.) and the 2025-09-12 Affidavit of Probable Cause (3 pp.), both banked with SHA-256s and with DocumentCloud's `file_hash` recorded per the re-render trap. **CR-E07's F-15 — "the State's theory is visible only through its opponent's description" — is PARTLY CURED, and the limit is stated: these are the September 2025 charging documents, not the still-unheld 2026-07-28 brief.** **F-23: the Information pleads EXACTLY ONE aggravating circumstance (KGRD, § 76-5-202(2)(a)(iii)), which upgrades CR-E07's A-4 from Medium — where it sat solely because the Information was not held — to a document-verified fact; the defence's characterisation was accurate.** ⚠️ **F-24: the same message sentence is quoted by both parties at different lengths, and the truncation does the argumentative work** — the State charges Count 6 on *"ask for a lawyer and stay silent"* full stop, while the defence's "purely altruistic" argument runs on a continuation the Information omits. **Neither party misquotes the words it prints; neither document alone shows the sentence whole, and this project holds no certified transcript of the messages.** **F-25: the Information asserts DNA "was found on" named items — the formulation the State's own ATF analyst later declined under oath as not scientifically defensible — recorded with two express guards** (the *"consistent with"* hedge is not the bare source attribution, and a 2025 pleading is not bound by 2026 testimony), **plus an unresolved precision point that the charging document locates DNA "on the trigger" where the underlying item was the trigger AND trigger guard swabbed together.** **F-26: the officer's contemporaneous "approximately 160 yards" and Faumuina's surveyed 415/410/68 ft are ONE distance estimated once and measured once — recorded so no file cites them as independent corroboration.** ⚠️ **D-60 OPENED and expressly NOT resolved: the keyboard note reads "and I'm going to take it" in the Information while the defence brief quotes StEx 16.3 as "and I took it" — intent before the act versus admission after it — with the steelman recorded that these may be two separate artifacts.** **Register ceiling verified by grep AND by reading every hit before assigning; D-60 was genuinely free and the next free number is D-61.** **Q-69 and Q-70 opened.** ⚠️ **Living-persons handling: the defendant's home address and date of birth appear on the face of BOTH documents and are reproduced NOWHERE here; the accounts of his mother, father, a family friend and his roommate are recorded only where they bear on the public questions, in the minimum words, none of them named beyond the documents' own descriptions; the State's characterisation of a private individual's gender identity and relationship is noted as the SOURCE of a framing CR-E07 could previously attribute only through the defence, and is not elaborated.** **Findings `[PROVISIONAL]` — no verification cycle has run. No case-posture statement altered. Robinson has NOT been bound over; presumption of innocence applies.** |
