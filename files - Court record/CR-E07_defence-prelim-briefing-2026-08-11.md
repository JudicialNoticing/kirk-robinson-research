# CR-E07 — Defence Preliminary Hearing Briefing, filed 2026-08-11

**File ID:** CR-E07
**Scope:** A reasoned read of one primary document — *Defendant Tyler James Robinson's Preliminary Hearing Briefing*, signed and served 2026-08-11. Covers the filing's identity and provenance, a recording-layer inventory of what it argues, and an analyst-layer assessment of what it does and does not establish. **It does not assess the merits of any legal argument, and it does not touch case posture.**
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth Judicial District Court, Provo Department — Hon. Tony F. Graf, Jr.
**Prepared:** 2026-08-13
**Status/version:** v1.1 (2026-08-13 — adds F-17 citation verification and F-18 outlet attribution; resolves D-60 in part; corrects §6)
**Upstream:** banked by [CR-WATCH-log](CR-WATCH-log.md) Run 3 (2026-08-13), which was expressly forbidden from characterising contents. This file is that separate act.

> ⚠️ **AS OF 2026-08-13, TYLER ROBINSON HAS NOT BEEN BOUND OVER FOR TRIAL. PRESUMPTION OF INNOCENCE APPLIES THROUGHOUT.** The document read here is an **advocacy filing by the defence**. Every factual assertion in it is a **claim by a party**, recorded faithfully below and adopted nowhere. Nothing in this file resolves any disputed fact.

---

## §0 · Sourcing framework (project standard)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material
- **"T1 via T3"** — primary-document content known only through reporting. Never silently promoted.

**This document's grade: T1 (document held and read directly) — with one provenance element missing, see §1.** This is the **first primary filing this project holds as a document rather than through reporting.** The State's 2026-07-28 opening brief remains **unheld** and stays T1 via T3.

## §1 · Access-path caveats — first, per project standard

| | |
|---|---|
| **How obtained** | Direct fetch of an **outlet-mirrored copy**: `static.foxnews.com/foxnews.com/content/uploads/2026/08/robinson-prelim-filing.pdf`, retrieved **2026-08-13** |
| **Banked** | `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.pdf` (+ `.txt` extraction), SHA-256 `c3f394372192a6a3c6b791839a22a9ce4be43aea6f9985b9fc3703633bfde0e4` |
| **Provenance** | ⚠️ **TWO OF THREE ELEMENTS PRESENT.** Signature block ✅ (*"RESPECTFULLY SUBMITTED this 11th day of August, 2026"*, `/s/` Nester, Burt, Novak, Visser). Certificate of service ✅ (`/s/` Visser, *"served via the Court's electronic filing system on the 11th day of August, 2026"*). **Clerk file-stamp / e-filing header ❌ — not visible anywhere in the text layer.** |
| **What that means** | This is an **outlet-hosted copy carrying the defence's own attestation of filing**, not a court-stamped document. Materially better provenance than the State's Scribd mirror (which has none of the three verified) and still short of a stamped filing. **A court-stamped copy remains an open acquisition item.** |
| **Length** | 41 PDF pages; internal printed numbering to 35 (body ends p. 33, signature p. 34, certificate p. 35). ⚠️ **35 is also the court's page limit for this brief. Length and limit COINCIDE. This is recorded as a coincidence and is not read as a finding in either direction** — the inverse of the conflation hazard logged at Run 2, where 28 pp. of the State's brief was being read against a 35-page limit |
| **Date verification** | 2026-08-11 **is a Tuesday** — confirmed by calculation, consistent with the calendar's "all three briefing dates fall on Tuesdays." Verified by **direct reading of the document**, not machine extraction; Run 2 logged three separate extractions asserting a wrong day-of-week for a different date |
| **Not consulted** | **No docket.** The XChange paywall (Q-31) is unchanged, so this file cannot say whether the filing was later amended, supplemented, or responded to |
| **Exhibits** | The brief cites State's Exhibits (StEx 5.1, 6, 12.1, 12.4, 16, 16.1, 16.2) and Docs. 525, 570, 625, 631, 678. **None of these underlying artifacts is held by this project.** Every characterisation of them below is *the defence's*, recorded as such |
| **Parallel citation unreachable** *(added v1.1, 2026-08-13)* | The *Murphy* opinion itself was obtained (see F-17). Its **parallel Pacific Reporter citation, 588 P.3d 1039, could not be confirmed on any open source.** Reporter volume-and-page assignments are made after publication and are a Westlaw/Lexis-tier field. CourtListener's citation lookup `https://www.courtlistener.com/c/P.3d/588/1039/` returns *"Unable to Find Citation '588 P.3d 1039'"* (retrieved 2026-08-13); CourtListener's own API record for the case carries `"citation":["2026 UT App 38"]` with an empty `lexisCite`; Justia's Citation field reads `2026 UT App 38`. **This is a limit of the access path, not a defect found in the brief** — see F-17 |
| **Failed retrievals logged** *(added v1.1, 2026-08-13)* | `thehill.com` article on the filing — **HTTP 403**, not read. `law.justia.com` section index — **HTTP 403**, though the direct case URL fetched successfully. Logged per the operational rule that failed retrievals are recorded, not silently dropped |
| **Outlet articles read as raw page text** *(added v1.1, 2026-08-13)* | For F-18, each outlet article was fetched and its **raw HTML converted to text locally**, then read directly. This was deliberate. A *summarising* fetch of the Deseret article returned the sentence *"The defense does not contest that Robinson committed the shooting"* framed as reporting — **that sentence appears nowhere in the Deseret article.** It was the summariser's own synthesis. The failure class F-14 identifies was reproduced live, by this project, while auditing F-14 |

---

## §2 · Recording layer — what the filing argues

**Faithfulness to the claim is the standard here, not correctness.** These are the defence's positions.

### 2.0 Threshold argument — hearsay under Rule 1102

The brief opens its Argument section with a challenge that is **not** confined to the aggravators: it asserts the State's use of hearsay deemed reliable by Utah R. Crim. P. 1102 violates constitutional rights and separation-of-powers principles (citing U.S. Const. amends. VI, VIII, XIV; Utah Const. art. I, § 1; and Docs. 525, 570, 631, 678, described as briefed pre-hearing and preserved as a continuing objection).

It applies this **specifically to identity for all charged counts**, characterising the State's identity evidence as consisting largely of alleged communications between Mr. Robinson and Mr. Twiggs, alleged Discord communications, and an identification from UVU surveillance footage — all said to derive from or become presumptively admissible through a recorded interview with witness **Lance Twiggs** whom, the brief states, the Court would not allow the defence to subpoena from another state to testify (Doc. 625).

It concludes this section: *"This Court must decline bind over on all charges."*

### 2.1 Argument I — the KGRD aggravator (the sole alleged aggravator)

Directed at Utah Code § 76-5-202(2)(a)(iii): that the actor "knowingly created a great risk of death to another individual other than the deceased individual and the actor." The brief abbreviates it **KGRD**.

Sub-arguments, as structured in the filing:
- **(a)** The U.S. and Utah Constitutions require aggravators to be **narrowly construed**, citing *Gregg v. Georgia*, *Proffitt v. Florida*, *Lewis v. Jeffers*, *State v. Wood*.
- **(b)** Utah Supreme Court decisions narrowly construing KGRD require striking it here.
- **(c)** The State's evidence fails to establish probable cause as to KGRD.
- **(d)** The State's theories fail — addressed under **line of sight** and an **"anyone near"** theory, the latter split into **knowledge** and **presence alone is insufficient as a matter of law**.
- **(e)** A survey of other jurisdictions supporting narrow construction.

Its stated legal standard: the State must show more than a "possibility" that another person may be killed — rather a **"high probability"**, *and* that the defendant **knew** of that high probability. It argues the Court may draw reasonable inferences but **may not speculate**, citing *State v. Murphy*, 2026 UT App 38 and *State v. Prisbrey*.

The brief also asserts the State's failure cannot be attributed to any limiting order: it states the Court excluded no evidence on this subject, excluded no proffered expert testimony, and did not limit the State's time.

### 2.2 Argument II — Count Six, witness tampering

Count Six charges tampering with a witness (Utah Code § 76-8-508), the Information alleging Mr. Robinson directed his roommate to stay silent if questioned by police.

The defence position: the advice was **"purely altruistic"** and therefore not obstruction, invoking *United States v. Peterson*, 385 F.3d 127 (2d Cir. 2004) for the proposition that the inducer's **motive** distinguishes obstruction from altruistic advice. It frames the underlying advice as an invocation of the Fifth Amendment right to counsel and silence, and argues surrounding context shows a focus on protecting Mr. Twiggs rather than impeding investigation. The brief quotes the message at issue and several surrounding messages (StEx 16.1).

### 2.3 Argument III — Count Seven, offence in the presence of a child

Count Seven charges knowingly exposing a child under 14 to the homicide (Utah Code § 76-3-203-10(2)), which the brief says requires the offence occur in the physical presence of a child under 14 **with the defendant having knowledge** the child is present and may see or hear it.

The defence position: the State presented video showing two children present at the event (StEx 6) but **no evidence the shooter was aware of any child's presence**. It characterises the State's inference — drawn from an alleged earlier walking tour of campus — as speculation, noting a distance of approximately 400 feet and a 35–44 second period, and asserting the path shown in StEx 12.1 and 12.4 suggests no one identifiable as under 14 was passed.

It offers a contrast case: the inference "might" be reasonable at an obviously occupied elementary school or day care, but not on a college campus.
- **(a)** The parallel **aggravating factor** under § 76-3-203.9, alleged with Counts One and Two, must be stricken for the same want of knowledge.
- **(b)** The State's backup position — that sentencing enhancements are not subject to proof at a preliminary hearing — is inconsistent with established constitutional law (the brief's Table of Authorities cites *Apprendi v. New Jersey*).

### 2.4 Argument IV — the victim-targeting enhancement

Utah Code § 76-3-203(14), which the brief describes as focused on the defendant's perception of a **"personal attribute"** of the victim. The single attribute alleged in the Information is Mr. Kirk's **"political expression"** (§ 76-3-203(14)(1)(k)), which the brief says carries no further specificity in the charging document.

The defence addresses the two evidentiary sets it says the State proffers:
1. **Exhibit 5.1**, a Rule 1102 witness statement of **David Englehardt**, a pastor — argued to contain nothing about Mr. Robinson's state of mind, and to identify no specific pre-2025-09-10 statement by Mr. Kirk, only general categories of belief and topics of debate.
2. **A single statement** by Mr. Robinson to Mr. Twiggs — *"I had enough of his hatred"* (StEx 16.1) — argued to be unaccompanied, per Mr. Twiggs, by any prior communication between them about Mr. Kirk, and to refer to "hatred and nothing more."

> ⚠️ **HANDLED MINIMALLY AND DELIBERATELY.** This section of the brief also **characterises the State's theory** as resting in part on the relationship between Mr. Robinson and Mr. Twiggs and on Mr. Twiggs' gender identity. **Mr. Twiggs is a private individual.** That material is recorded here only to the extent required to state what the contested enhancement turns on — because the brief's argument is that the State substituted these circumstances for proof of motive — and is **attributed to the filing's characterisation of the State's position, not adopted, and not elaborated.** Under this project's living-persons rule, nothing further about a private individual's identity belongs in this library. **Note also that the brief is characterising its opponent's argument; the State's actual position is not held by this project.**

### 2.5 Conclusion as filed

The brief asks the Court to **decline bindover**, resting first on the hearsay/reliability argument ("for this reason alone"), then on the asserted legal insufficiency of the KGRD aggravator, and finally on Counts Six and Seven and the enhancements.

---

## §3 · Analyst layer — what this document does and does not establish

**Grades trace to a verification act by this project, not to the filing's own confidence.**

| # | Statement | Grade | Basis |
|---|---|---|---|
| A-1 | A document titled *"Defendant Tyler James Robinson's Preliminary Hearing Briefing"* exists, is captioned to Case No. 251403576 before Hon. Tony F. Graf, Jr., and bears a signature date and certificate of service of **2026-08-11** | **High** | Read directly from the banked PDF; caption, signature block and certificate all present |
| A-2 | That document was **filed with the court** on 2026-08-11 | **Medium-high** | The certificate of service attests e-filing that date and multiple outlets report the filing — **but no clerk file-stamp is visible**, so filing is attested by the filer, not evidenced by the court |
| A-3 | Defence counsel of record are Nester, Burt (pro hac vice), Novak (pro hac vice), and Visser | **High** | Signature block, read directly |
| A-4 | The **sole aggravator alleged** in support of aggravated murder is the KGRD aggravator | **Medium** | The brief states this repeatedly and unambiguously. It is a party's characterisation of the Information; **the Information itself is not held by this project** |
| A-5 | The State's opening brief argued the case is "as straightforward a bind-over decision as this Court will ever see" | **T1 via T3 — unchanged** | Reported; the State's brief remains unheld. Recorded here only because the defence filing responds to it |
| A-6 | The defence contests **identity**, not merely the aggravators | **High** | Read directly — see D-60 below |

**What this file expressly does NOT establish, and no reading of it should imply:**
- Whether any argument in it is legally correct. That is for the court on 2026-09-01.
- Any fact about what occurred on 2025-09-10. Every factual assertion in the brief is a party's characterisation of exhibits this project does not hold.
- Anything about the State's actual position. Its brief is unheld; the defence's account of it is one side's.
- Any change to case posture. **Robinson has not been bound over.**

---

## §4 · Findings

**F-14 — The characterisation circulating in coverage summaries, that the defence is no longer contesting that Mr. Robinson committed the offence, is contradicted by the filing itself.**
A search-result synthesis retrieved 2026-08-13 asserted the defence "is now arguing not that Robinson didn't commit the crime, but that it shouldn't be a death penalty case." **The brief's threshold section argues the State's identity evidence for *all* charged counts is inadmissible hearsay under Rule 1102 and concludes "This Court must decline bind over on all charges."** The conclusion repeats that the hearsay failure warrants declining bindover "for this reason alone."
⚠️ **Scope of this finding, as stated at v1.0:** the quoted characterisation comes from a **search-engine synthesis of multiple outlets**, not from a verified sentence in a named article. ~~**This project has not established which outlet, if any, published those words.**~~ ~~The finding is therefore: *a characterisation in circulation is contradicted by the primary document* — **not** that any specific outlet erred.~~ ~~Confirming attribution requires reading the individual articles, which is queued below.~~
✅ **SCOPE CAVEAT CLOSED 2026-08-13 (v1.1).** The individual articles have now been read as raw page text. **A named outlet did publish those words in its own voice: Townhall.com (Amy Curtis, 2026-08-12).** F-14's substance is unchanged and stands; only its "attribution not established" limit is lifted. **See F-18 for the attribution, the steelman, and the both-directions sweep** — which found more outlets stating the point correctly than incorrectly.
**Why it matters:** it is a textbook instance of this project's core pattern — **the primary document was available and said something materially different from the summary of it.** It is also the exact reason the watch spec forbids characterising a filing's contents from reporting.

**F-15 — The State's theory is now partially visible, but only through its opponent's description.**
The brief discloses more about the State's asserted theories (line of sight, "anyone near", the campus walking tour, the Englehardt statement, the "I had enough of his hatred" text) than any source previously held. **This is second-hand by construction.** It should be treated as a **map of what to look for in the State's own filings**, never as the State's position. Q-45 (bank the State's opening brief) gains value accordingly.

**F-16 — Provenance verification and content reading are, again, demonstrably separate acts.**
Run 2 stated this as a principle for the State's Scribd mirror. Applying it here produced a concrete result: the document is readable and its signature and service blocks verify, **while its file-stamp does not exist in the copy held.** Had the two acts been merged, this copy would likely have been recorded as a stamped filing.

---

### Added at v1.1 — 2026-08-13

**F-17 — *State v. Murphy*, 2026 UT App 38 EXISTS, and both propositions the brief draws from it are accurate. The parallel P.3d cite alone is unconfirmed — an access limit, not an error.**
Grade: **High** for existence, identifying fields, and both propositions. **Unverified** for the parallel citation. This closes the v1.0 open item and V-32.

*Existence and identifying fields — read off the opinion, not off a search result.* The opinion was retrieved 2026-08-13 from **the Utah appellate courts' own domain**, `https://legacy.utcourts.gov/opinions/appopin/State%20v.%20Murphy20260319_20240145_38.pdf`, and independently from the CourtListener mirror `https://storage.courtlistener.com/pdf/2026/03/19/state_v._murphy.pdf`. **The two files are byte-identical**, SHA-256 `dac0a92258ede9fbed34df1eab8ccff3ed7f86129064d653d86f7ce777fd3b38` — so the mirror is not an independent transcription risk. The opinion reads: *State of Utah, Appellant, v. Shawn Phillip Murphy, Appellee*; **Opinion No. 20240145-CA**; **Filed March 19, 2026**; on appeal from the Third District Court, Salt Lake Department (Hon. Patrick Corum), No. 221907614; authored by **Judge David N. Mortensen**, with Judges Gregory K. Orme and Ryan M. Harris concurring. The running footer of every page reads `20240145-CA … 2026 UT App 38`. Justia's record for docket 20240145-CA agrees (`Citation: 2026 UT App 38`).

⚠️ **Identification was made on docket number and filing date, not on case name.** A different *State v. Murphy*, No. 20170193-CA (Utah Ct. App. 2019), surfaces in the same searches and is not this case. Naming a case is not identifying it.

*Parallel citation — **588 P.3d 1039** is **unverified**.* No open source consulted carries it: the citation lookup returns "Unable to Find Citation", the CourtListener API record lists only the neutral cite with an empty `lexisCite`, Justia lists only the neutral cite, and the slip opinion carries none (normal — reporter pagination is assigned after publication). A search for the literal string `"588 P.3d 1039"` returned **the defence brief itself as the only carrier found.** **This is recorded as "not reachable from here," not as "wrong."** It is a Westlaw/Lexis-tier field; see §1 and Q-64.

*Proposition 1 — the bindover standard. **Accurate.*** The brief (printed p. 2) cites *Murphy* ¶ 8 for bindover only "if the prosecution produces evidence sufficient to demonstrate probable cause that the charged crimes were committed." **Murphy ¶ 8 contains that sentence**, quoting *State v. Ramirez*, 2012 UT 59, ¶ 8, 289 P.3d 444 — exactly the attribution chain the brief prints. The brief's added clause "and the defendant committed them" tracks **Utah R. Crim. P. 7B(b)**, which *Murphy* ¶ 8 quotes in the same paragraph, and which the brief separately cites. No overstatement found.

*Proposition 2 — reasonable inference versus speculation. **Accurate, and verbatim.*** The brief's indented block quote attributed to "2026 UT App 38, ¶ 10" is **word-for-word identical to Murphy ¶ 10**, including its internal citations to *State v. Prisbrey*, 2020 UT App 172, ¶¶ 22–23, 479 P.3d 1126 and *Salt Lake City v. Carrera*, 2015 UT 73, ¶ 12, 358 P.3d 1067. It is a quotation, not a paraphrase presented as one. The brief's later short cite — *Murphy*, ¶ 10, for the inference/speculation definitions — also checks out against ¶ 10.

*Collateral verification.* ***State v. Prisbrey*, 2020 UT App 172, 479 P.3d 1126** — the brief's companion authority for this standard — is **independently confirmed as cited**, because *Murphy* itself cites it in exactly that form. That is a Tier 1 confirmation obtained as a by-product.

*One descriptive fact about the authority, with the merits question expressly left alone.* *Murphy* **affirmed** a magistrate's refusal to bind over, and the element that failed there was **identity** (¶¶ 11–12, 19). This is recorded because it is a fact about what the cited case is. **It is not an assessment of whether the citation is apt, strong, or dispositive here, and nothing in it forecasts any ruling** — §6's bar on assessing legal merit is unchanged.

**F-18 — D-60's characterisation traces to one named outlet, Townhall; the both-directions sweep found more outlets stating the point correctly than incorrectly, and outlet orientation did not predict accuracy.**

*The carrier, identified.* **Townhall.com — Amy Curtis, "Tyler Robinson's Defense Team Just Filed a Very Interesting Brief With the Court," published 2026-08-12 2:15 PM** (`https://townhall.com/news/amy-curtis/2026/08/12/tyler-robinson-defense-filing-n2681123`, raw page text retrieved 2026-08-13). In the article's own lede — unquoted, unattributed, stated as fact — it reads: *"The defense is now arguing not that Robinson didn't commit the crime, but that it shouldn't be a death penalty case…"* That is the F-14 wording, near-verbatim. **The v1.0 caveat is therefore closed: a named outlet did publish it in its own voice.**
⚠️ Orientation note (**assessment**, calibration only, **not** disqualifying): Townhall is conservative opinion-news; the page's own chrome carries "Watch Salem News Channel" (Salem Media Group).
⚠️ It is **highly likely but not proven** that the v1.0 search synthesis was reproducing this article — the wording matches closely, but this project cannot inspect which pages a search engine drew from.

*Upstream of the outlet, recorded separately.* The same Townhall article embeds an X post by **Andrew Kolvet** (TPUSA spokesman) quoting **Claudia Cowan** (Fox News): *"The apparent defense strategy here isn't to prove that Tyler Robinson didn't kill Charlie Kirk, but that he didn't intend to kill anyone else…"* This is a **third party quoted by the outlet, not the outlet's own words**, and it is materially **softer** ("the apparent defense strategy"). Recording layer keeps the two apart.

*Steelman first, per the objectivity rule.* The strongest reading of Townhall's sentence is **substantially supported by the filing**: on the brief's own printed pagination the threshold identity/hearsay challenge occupies roughly **one page** of a 33-page body (it opens the Argument on p. 1, runs into p. 2, and ends "This Court must decline bind over on all charges"), while the remaining ~31 pages address the aggravator, Counts Six and Seven, and the enhancements. The brief refers to **"the shooter" 41 times** without proposing an alternative perpetrator; it quotes Mr. Robinson's own message *"Im gonna turn myself in willingly"* without disputing it; and it contains **no reference to DNA at all**. "This filing is overwhelmingly about death-penalty eligibility" is a **fair** characterisation and is not disturbed here.

*What still fails, narrowly.* The specific clause — that the defence is **no longer contesting commission** — is contradicted by the filing's text. The threshold section applies the Rule 1102 challenge expressly to the evidence establishing identity **"for all of the charged counts"** and concludes **"This Court must decline bind over on all charges."** Contesting the admissibility and sufficiency of the State's identity proof is **not** an assertion of innocence — but it is equally **not** the concession of commission that the sentence asserts. **D-60 resolves against Townhall on that clause only, not on its emphasis characterisation.** Confidence **High**: both sides were read directly — the article as raw page text, the filing as the banked PDF text.

*Verified in both directions — outlets that got it right, logged explicitly (BOC-AUDIT Part 5.2).* All retrieved 2026-08-13. Orientation labels are **assessments**.

| Outlet | Orientation (assessment) | What it actually published |
|---|---|---|
| **Deseret News** / **KSL** — Pat Reavy; **one syndicated piece, counted as one source, not two** | neutral, local | Lede: Robinson "should not be bound over to stand trial for aggravated murder **and the six other charges** he's accused of because the state relied on **hearsay** evidence and speculation." **Correct on the exact point Townhall missed.** Contains no concession language |
| **HotAir** — John Sexton | hostile to the defence | Under-describes the filing as death-penalty-focused, but states in its own words: *"Of course the defense isn't admitting to anything really."* — **the opposite of the D-60 characterisation** |
| **RedState** — Teri Christoph | hostile; its editor's note discloses Kirk "was our cherished Salem Media colleague" | Opens by warning readers off the very inference: *"this is not an admission of guilt from Robinson, but rather a legal argument made by the defense"* — **explicitly refuses the concession framing**, while embedding the same Kolvet/Cowan quote Townhall used |
| **Associated Press** — Matthew Brown, read via KUER | neutral wire | No concession claim; frames it as "the defense tries to block the case from proceeding to trial." Its checkable side-claim that the filing "made no mention of DNA" **verifies against the banked text** |
| **UPI** — Lisa Hornung | neutral wire | No concession claim. *(Minor, non-D-60: renders the brief's "the bullet travelled above, not through, the crowd" as "bullets" plural; AP quotes it in the singular, matching the filing)* |
| **Eastern Herald** — Shivam Chopra | neutral aggregator | Made **no** characterisation of the filing's contents, so is **not** a D-60 carrier. It instead states the defence "has not disclosed the contents of Tuesday's written filing" — **a different defect**, since the filing was publicly available and being quoted by other outlets the same day. Recorded, not folded into D-60 |

*Pattern finding — the reason this sweep was run in both directions.* **Orientation did not predict accuracy.** Townhall and RedState sit in the same ownership family with the same orientation, published within hours of each other on 2026-08-12, worked from the same embedded Kolvet/Cowan material — and reached **opposite** results, RedState correct and Townhall not. Meanwhile the outlet most hostile to the defence in tone (HotAir) stated the non-concession point correctly. **An audit that had stopped at the first outlet found in error would have produced a false pattern.** This is a concrete instance of the standing rule that orientation is calibration context, never disqualification.

---

## §5 · Open items and register entries proposed

| → | Item |
|---|---|
| **Q-63 (new)** | **Obtain a court-stamped copy of the 2026-08-11 defence brief** to close the missing provenance element. Routes: XChange (paywalled, Q-31), DocumentCloud project 224251 (API open per Run 2), or another outlet mirror |
| **D-60** ~~(new)~~ **— RESOLVED IN PART 2026-08-13 (v1.1)** | **Discrepancy — "defence concedes commission" characterisation vs the filing's own text.** See F-14, and **F-18** for the resolution. ~~⚠️ **Do not resolve this against any named outlet until individual articles are read**; presently it resolves only against the search-synthesis wording~~ — **the articles have now been read as raw page text, so this condition is satisfied.** **Resolves against Townhall.com (Amy Curtis, 2026-08-12)**, which published the characterisation in its own voice, **and only as to the clause that the defence is no longer contesting commission** — its "the filing is overwhelmingly about the death penalty" emphasis is fair and is **not** resolved against. Confidence **High**. **Deseret/KSL, AP, UPI, HotAir, RedState and Eastern Herald are expressly cleared** as carriers; three of them stated the point correctly. **Remaining open:** whether Townhall later amended or corrected the piece (not checked), and whether any outlet outside the six read carries the same wording |
| **V-32 — CLOSED 2026-08-13 (v1.1)** | **Verify *State v. Murphy*, 2026 UT App 38.** ✅ **Case exists; identifying fields and both propositions verify** against the opinion obtained from the Utah courts' own domain and a byte-identical CourtListener mirror. See **F-17**. The one element that did **not** verify is the parallel P.3d cite — carried forward as Q-64, not as a defect |
| **Q-64 (new)** | **Confirm the parallel citation 588 P.3d 1039** for *Murphy*. Not reachable on open sources (see §1). Routes: Westlaw/Lexis (paid), a law-library terminal, or a later free-tier record once reporter pagination propagates. **Until then, cite *Murphy* by its neutral citation, 2026 UT App 38, which is fully verified** |
| **Q-45** | Unchanged and now higher-value — the **State's** 2026-07-28 opening brief is still unbanked and its Scribd mirror unverified. This file's F-15 depends on it |
| **NEW** | **The exhibits cited throughout (StEx 5.1, 6, 12.1, 12.4, 16, 16.1, 16.2) are all unheld.** Every characterisation of them in §2 is the defence's. StEx 16 / 16.1 (the Twiggs interview and messages) is load-bearing for at least three of the four arguments |
| **NEW** | **Doc. 625** — the order the brief says prevented an out-of-state subpoena of Mr. Twiggs — is unheld and is directly relevant to the Rule 1102 argument |
| **NEW** | **Docs. 525, 570, 631, 678** — the pre-hearing hearsay briefing the filing incorporates — are unheld |
| ~~**NEW**~~ **DONE 2026-08-13 (v1.1)** | ~~*State v. Murphy*, **2026 UT App 38** is cited as the controlling probable-cause standard and is recent enough that this project has not verified it exists as cited. **Verify the citation** before relying on it in any analysis~~ — **done; the case exists and the citation is accurate apart from the unconfirmed P.3d parallel. See F-17, V-32, Q-64** |
| **NEW** | **Every other authority cited in the brief remains unverified** — *Gregg*, *Proffitt*, *Lewis v. Jeffers*, *State v. Wood*, *United States v. Peterson* (385 F.3d 127), *Apprendi*, *Cristobal*, *Ramirez*, *Carrera*, *Johnson*, *Pierre* and the out-of-jurisdiction survey. Only *Murphy* was checked directly; *Prisbrey* was confirmed collaterally because *Murphy* cites it. **Do not read F-17 as a clean bill for the brief's Table of Authorities** |
| **Watch** | **State's reply due Tue 2026-08-18**, 18-page limit. Oral argument **Tue 2026-09-01, 10:00 a.m.**, in person, up to two hours per side. **Check specifically for a defence motion to continue** — lead counsel stated a trial conflict with that week on the record and was declined |

---

## §6 · Residual scope — what this file did NOT do

- **Did not assess legal merit** of any argument, or predict the bindover outcome. **Unchanged at v1.1** — F-17 verifies that a cited case exists and is quoted accurately, which says nothing about whether the argument built on it succeeds.
- ~~**Did not verify a single cited case** against a reporter, including the recent *Murphy* citation.~~ **CORRECTED 2026-08-13 (v1.1):** ***State v. Murphy*, 2026 UT App 38, has now been verified** against the opinion itself, and *Prisbrey* was confirmed collaterally (F-17). **All other cited authorities remain unverified**, and the *Murphy* **parallel P.3d citation remains unconfirmed** (Q-64).
- **Did not obtain any paid-database record** (Westlaw, Lexis) — so no reporter pagination could be confirmed for any case.
- **Did not check whether Townhall, or any other outlet, later amended or corrected** its 2026-08-12 article; each was read once, on 2026-08-13.
- **Did not survey outlets beyond the seven read** for F-18 (Townhall, Deseret/KSL as one syndicated piece, HotAir, RedState, AP via KUER, UPI, Eastern Herald). **"No other carrier found" is scoped to those.**
- **Did not read the State's opening brief**, which is unheld — so every account of the State's position here is the defence's.
- **Did not consult a docket**, so cannot say whether this filing was amended, supplemented, or answered after 2026-08-11.
- **Did not examine any cited exhibit.**
- **Did not alter any case-posture statement in any topic file**, and moved no existing register entry.
- **Did not elaborate on private-individual material** beyond the minimum needed to state what the contested enhancement turns on.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-08-13** | File created. First reasoned read of the 2026-08-11 defence preliminary-hearing briefing, banked the same day by [CR-WATCH-log](CR-WATCH-log.md) Run 3 and deliberately left unread by it, since a watch run may not characterise a filing's contents beyond title and date. **This is the first primary filing the project holds as a document rather than through reporting**, and the read is graded accordingly — **T1, with the clerk file-stamp expressly absent** (signature block and certificate of service present), so it is recorded as outlet-hosted document text carrying the filer's own attestation and is **not silently promoted** to a stamped filing. Recording layer inventories the threshold Rule 1102 hearsay argument and Arguments I–IV (KGRD aggravator; Count Six witness tampering; Count Seven and the child-presence aggravating factor plus the *Apprendi* backup position; victim-targeting enhancement). Analyst layer grades six statements and states plainly what the document cannot establish — including that **every factual assertion in it is a party's characterisation of exhibits this project does not hold.** **Three findings: F-14**, that a characterisation in circulation — the defence no longer contesting commission — is contradicted by the filing, which argues the identity evidence for all counts is inadmissible hearsay and asks the court to decline bindover on all charges *(⚠️ scoped: the wording came from a search synthesis, not a verified named article, so D-60 must not resolve against any outlet until individual articles are read)*; **F-15**, that the State's theory is now partially visible but only through its opponent's description and must be treated as a map for acquisition rather than as the State's position; **F-16**, that provenance verification and content reading are again demonstrably separate acts, since this copy reads cleanly while its file-stamp does not exist. **Q-63 and D-60 proposed** (next free numbers checked against the whole repository: D-59, V-31, F-13, M-12, Q-62 were the prior highs). Seven unheld artifacts queued, including StEx 16/16.1 which is load-bearing for three of four arguments, and Doc. 625. ⚠️ **Material touching a private individual's gender identity was handled minimally, attributed to the filing's characterisation of the State's position, adopted nowhere, and not elaborated.** **No case-posture statement in any topic file was altered; no register entry was moved. Robinson has not been bound over; presumption of innocence applies.** |
| **1.1** | **2026-08-13** | **Two verification acts the v1.0 file had queued and expressly disclaimed. (1) Citation check — *State v. Murphy*, 2026 UT App 38 (F-17, V-32 closed).** The case **exists**; the opinion was obtained from **the Utah appellate courts' own domain** and, independently, from CourtListener, the two files **byte-identical** at SHA-256 `dac0a922…3bde` — so the mirror adds no transcription risk. Identifying fields were read off the opinion and matched **on docket number and filing date, not on case name** (Opinion No. 20240145-CA, filed March 19, 2026, Mortensen, J., Orme and Harris concurring); a different *State v. Murphy*, No. 20170193-CA (2019), surfaces in the same searches and is **not** this case. **Both propositions the brief draws from it verify:** ¶ 8 carries the bindover/probable-cause standard the brief attributes to it (quoting *Ramirez*, with the brief's "and the defendant committed them" tracking Utah R. Crim. P. 7B(b), quoted in that same paragraph), and the brief's block quote on **reasonable inference versus speculation is word-for-word identical to ¶ 10**, internal citations included. ***Prisbrey*, 2020 UT App 172, 479 P.3d 1126 confirmed collaterally**, since *Murphy* cites it in that exact form. **The one element that did NOT verify is the parallel citation 588 P.3d 1039** — absent from CourtListener's citation lookup and API record, absent from Justia, absent from the slip opinion, and found on the open web **only in the defence brief itself**. That is recorded as an **access-path caveat (§1) and Q-64, expressly "not reachable from here" rather than "wrong"** — reporter pagination is a Westlaw/Lexis-tier field. Noted descriptively and **without any merits inference**: *Murphy* affirmed a refusal to bind over on a failure of **identity**. **(2) D-60 resolved in part (F-18).** The individual articles were read **as raw page text**, and a named outlet **did** publish the flagged characterisation in its own voice: **Townhall.com (Amy Curtis, 2026-08-12)**. D-60 therefore **resolves against Townhall — and only as to the clause that the defence is no longer contesting commission**, which the filing contradicts by challenging identity "for all of the charged counts" and asking the court to "decline bind over on all charges"; **its "overwhelmingly about the death penalty" emphasis is fair and is not resolved against**, the steelman having been run first (the identity/hearsay challenge is ~1 page of a 33-page body; "the shooter" appears 41 times with no alternative perpetrator proposed; no DNA reference at all). The upstream **Kolvet/Cowan** wording is recorded **separately as a third party quoted by the outlet, not the outlet's own words**. **Verified in both directions, as the standing rule requires: Deseret/KSL (one syndicated piece, counted once), AP, UPI, HotAir, RedState and Eastern Herald are expressly cleared**, and **three stated the point correctly** — HotAir ("the defense isn't admitting to anything really") and RedState ("not an admission of guilt") **while hostile in orientation**, Deseret/KSL accurately reporting bindover contested on all seven charges on hearsay grounds. **Pattern finding: orientation did not predict accuracy** — Townhall and RedState, same ownership family and orientation, same source material, same day, reached opposite results; an audit stopping at the first error would have manufactured a false pattern. Eastern Herald's "contents not disclosed" claim is logged as a **different** defect, not folded into D-60. **§1 gained three caveats** — the unreachable parallel cite, two HTTP 403 retrieval failures, and a note that a *summarising* fetch invented the sentence "The defense does not contest that Robinson committed the shooting," **which appears nowhere in the Deseret article**: the F-14 failure class reproduced live while auditing F-14, which is why every outlet was then read as raw text. **§6 corrected in place, not silently** — the v1.0 line "did not verify a single cited case" is struck and restated, and four new scope limits added (no paid database; no check for later outlet corrections; survey bounded to seven outlets; all other authorities in the brief still unverified). **Recording and analyst layers kept separate; outlet characterisations labelled assessments with orientation notes as calibration only. No case-posture statement was altered anywhere. Robinson has not been bound over; presumption of innocence applies.** |

---

## Related

- [[CR-WATCH-log]] — Run 3 banked this filing; the docket calendar and escalation triggers live in [[DOCKET-WATCH]]
- [[CR-ACQ-2026-07-27_court-record-acquisition]] — §5.1 is the canonical source for the briefing calendar
- [[CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche]] · [[CR-E06_Bakker-Day2_Oliver-Day5_full-read]] — hearing testimony the brief's factual assertions run against
