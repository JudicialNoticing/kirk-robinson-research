# BOC-ROUTE-2026-07-27 — Post-Series Case-Claims Corpus: Registration and Routing

**File ID:** BOC-ROUTE-2026-07-27
**Scope:** resolves Register **D-46** (the unredeemed "Monday series finale" on Erika Kirk's Sept 8/Sept 10 "alibi") by locating where that material went, and **registers and routes** — without inventorying — the body of regular *Candace* episodes released after the "Bride of Charlie" series closed on 2026-03-18. This file is a **triage and routing instrument, not a claim inventory**: it establishes what exists, when it aired, and which topic folder each item belongs to. It does **not** record, assess, or adopt the content of any episode listed.
**Case context:** *State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth District Court, Provo. Unlike the BOC episode files — which are ACTOR-CONTEXT material — a large share of the corpus registered here consists of **direct claims about the criminal case**. Case-posture statements below are verified and date-stamped **as of 2026-07-27** (§4). Tyler Robinson is presumed innocent; he has **not** been bound over for trial as of this file's date.
**Prepared:** July 27, 2026
**Status:** v1.3 *(2026-09-16: the owner's posture ruling appended as a dated note beneath the case-posture sentence — the row was written without bumping this line; regularised in the cycle-3 close.)* Earlier: v1.2 — **§4's briefing-schedule legs promoted to Tier 1** on user authorisation (**Q-43**), read directly from the banked Day 4 transcript rather than from a news report; **canonical statement moved to [CR-ACQ §5.1](../files%20-%20Court%20record/CR-ACQ-2026-07-27_court-record-acquisition.md)**. D-47's resolution is **unchanged** — only the strength of its docket leg. *(v1.1:)* corrected on adversarial re-read (**BOC-AUDIT-2026-07-27B**): the "41 case-relevant" headline reduced to **~35** (six flagged episodes concern other events); the "third instance of the migration pattern" separated into **two content migrations plus one title-rendering hazard**; **Ep 320 added** to the priority list. No routing decision and no register entry changed.

**Headline result:** D-46 **RESOLVED**. The promised finale never aired in series form — that null, established 2026-07-20, is re-confirmed today against a fresh feed pull. But the *material* was not abandoned: it migrated into **regular numbered episodes**, beginning on the very Monday promised (2026-03-23, Ep 314) and delivered directly the next day (**2026-03-24, Ep 315, "REVEALED: Erika Went To A Weird Place On 9/10"**, whose own chapter marker reads "07:15 - Where was Erika on 9/10?"). This is the **third documented instance of the same migration pattern** — series-promised material running as regular, un-prefixed episodes — after D-35 (Episode 8 itself) and the Epstein pair. The pattern is now the project's most reliable predictor of where Owens' promised content actually lands, and the title-matching hazard it creates is confirmed a third time.

**Second, larger finding:** the migration did not stop. From 2026-03-23 through 2026-07-24 Owens released **54 episodes**, of which — *corrected in v1.1* — **about 35 route to case-relevant destinations**, a sustained investigation into the assassination itself (ATF gun tracing, the backpack, the rifle, a claimed lone witness, the SUV, Sept-10 whereabouts, and the court filings). ⚠ **v1.0 said "41 case-relevant." That figure was a raw keyword-regex count and overstated the case:** six flagged episodes concern **other events** — the Butler rally shooting (348, 349), the White House Correspondents' Dinner shooting (339, 343), and media disputes (330, 333) — and are routed out of scope in §3. The routing table caught all six; the headline number did not. See BOC-AUDIT-2026-07-27B §2.2. **This corpus is entirely uncovered by the library.** It is registered and routed here; inventorying it is a scope decision for the user, not an action taken in this file (§6, §8).

---

## 0. Sourcing framework (project standard)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements (incl. named first-person statements by principals)
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material

**"T1 via T3"** marks primary-document content known only through reporting. Editorial characterizations are labeled *assessments*, never established fact, with an outlet-orientation note. Confidence grades (High / Medium-high / Medium / Low / unverified) trace to a verification act **by this project**; **"— (checkable)"** marks the verifiable-but-not-yet-verified, which are never counted as findings.

## 1. ACCESS PATH (caveats first)

**Primary source for the corpus inventory (§3):** the show's own podcast RSS feed, `https://feeds.megaphone.fm/candace` — **re-pulled fresh 2026-07-27**, HTTP 200, 2,052,154 bytes, 409 items, newest item 2026-07-24 (Ep 365). A durable copy of the 2026-07-20 pull is already banked at `BOC-E08_transcript-artifacts/feed.xml` (405 items); the two agree item-for-item across the Mar 19 – Apr 2 window, and the fresh pull adds five items dated 2026-07-17 through 2026-07-24. **Episode titles and the chapter/timestamp lists quoted in §3 are Owens' own published show-note text** — recording layer, Tier 2 as to *what she published*, and no evidence whatever as to the truth of any claim in them.

**Hard limit on this file — no episode was heard, watched, or transcribed.** The inventory rests on titles, publication timestamps, durations, GUIDs, and Owens' published chapter markers. Nothing in §3 establishes what any episode actually argues, alleges, or shows. Every content-level statement about these episodes is therefore **unverified by construction**, and no register entry in this project may be resolved on §3 alone. The single exception is **D-47** (§5), which turns on a checkable assertion carried in an episode *title* and is resolved against an independently verified public record, not against episode content.

**Retrievals and failures logged (all 2026-07-27):**
- Megaphone RSS — **success** (curl, HTTP 200).
- CIA.gov Directors Portrait Gallery — WebFetch **403 blocked**; curl with a browser user-agent **succeeded** (HTTP 200, 584,067 bytes). Used for §5 / D-45 close-out.
- CIA.gov CSI PDF *Directors of Central Intelligence, 1946–2005* — WebFetch **403**; curl succeeded (HTTP 200, 433,093 bytes) but **no text could be extracted** (`pdftotext` absent on this machine). Not relied upon.
- U.S. Army IKN biographical PDF for Woolsey — retrieved but **text-extraction failed**; not relied upon.
- CNN hearing-takeaways article — **HTTP 451** (legal-reasons block). Not used.
- Deseret News preliminary-hearing report — **success**, not paywalled. Used for §4.

**Artifacts banked** (durable local copies, alongside this file in `BOC-ROUTE-2026-07-27_artifacts/`): `feed_20260727.xml` (the fresh RSS pull, byte-verified 2,052,154 bytes — the primary artifact for §§2–3), `cia_directors_gallery_20260727.html` (the D-45 source), and `sweep_extract.py` (the extraction script, so §3 is reproducible). The 2026-07-20 comparison pull remains banked at `BOC-E08_transcript-artifacts/feed.xml`.

**Living-persons note.** §3 reproduces published episode titles verbatim because a routing file that paraphrased them would be useless for locating the material. Those titles contain serious allegations about named living people — including Erika Kirk, Andrew Kolvet, Blake Neff, Frank Turek, Victor Marx, Ben Shapiro, and others. **Every such allegation is attributed to Owens and adopted by no one.** Reproducing a title is a locator, not an endorsement, and this file draws no inference from any of them. Private individuals named in titles are recorded only to the extent necessary to identify the episode.

---

## 2. D-46 — RESOLVED

**The claim (recording layer).** BOC-E08 §11: Owens closes Episode 8 (2026-03-18) saying there are "a lot of problems with her alibi on September 8th and on September 10th, what she says that she was doing. And that will be our series finale… we will see you on Monday for that series finale." The promised Monday is **2026-03-23**.

**Leg 1 — did a series finale air? No.** Confirmed at **High**. The 2026-07-20 sweep (pull log §7 F-P1a) found no Episode 9 and no series-branded item after 2026-03-18 across the YouTube channel and /streams, the RSS feed, and Rumble. Today's fresh RSS pull re-confirms it: across all 409 items, the last series-branded release remains "Red Sparrow: When Erika Met Charlie…" (2026-03-18). *Scope of the null:* YouTube, RSS, and Rumble. `candaceowens.com` was unreachable on 2026-07-20 and remains outside the searched space — the null does not cover it.

**Leg 2 — where did the material go? Into regular numbered episodes.** Confirmed at **High** *as to placement*, on Owens' own published titles and chapter markers:

| Date | Episode | Title (verbatim) | Owens' own chapter marker |
|---|---|---|---|
| 2026-03-23 (the promised Monday) | Ep 314 | "EXPLOSIVE! TPUSA Accuses Joe Kent Of Leaking To Harm Erika!" | "14:25 - Leaked TPUSA texts and suspicious plane routes." |
| **2026-03-24** | **Ep 315** | **"REVEALED: Erika Went To A Weird Place On 9/10"** | **"07:15 - Where was Erika on 9/10?"** |
| 2026-03-25 | Ep 316 | "Who's Lying? Frank Turek, Erika Kirk, Or Elizabeth McCoy?" | "01:43 - Plane alibis. Who is lying?" |
| 2026-03-26 | Ep 317 | "VIRAL! It's Okay Not To Believe A Word Erika Kirk Says." | "01:21 - TPUSA's 9/10 timelines and stories are just not adding up." |

**Resolution.** D-46 is **RESOLVED**: the finale-as-promised did not occur (High), *and* the promised subject matter was delivered — beginning on the promised Monday and squarely on 2026-03-24 — as regular, un-prefixed, numbered episodes rather than as a series installment (High). **Steelman considered:** the strongest reading of Owens' sign-off is that "series finale" named the *content* she owed her audience rather than a branded format commitment; on that reading she substantially kept the promise, one day late for the core segment, and the discrepancy is one of packaging only. This file adopts that reading — the resolution is against the *literal* finale promise and **for** Owens on delivery of the substance.

**What this resolution does NOT establish.** Nothing about whether any "alibi problem" exists, what Owens actually asserted in those episodes, or whether any of it is true. Those episodes are **uninventoried** (§1). D-46 closes on placement; the content question is opened, not answered, and is routed at §6.

**Pattern significance — restated precisely in v1.1.** v1.0 called this "the third confirmed instance of the migration dynamic," which **conflated two distinct phenomena**. Separated properly: **content migration** — series-promised subject matter shipping as regular numbered episodes — is confirmed **twice** (Eps 309–311; Eps 314–317). **D-35 is a different thing**: Episode 8 *was* a numbered series installment, whose **podcast simulcast dropped the series prefix** — a title-rendering hazard, not content migration. **The operational rule survives all three unchanged, because each would defeat a title-string search: sweep Owens' output by channel and date, never by title string.** What does *not* follow is a three-times-confirmed regularity in her publishing behaviour. See BOC-AUDIT-2026-07-27B §2.3. BOC-E08 §15 predicted exactly this ("repeating at Episode 8's far edge the same migration dynamic that D-35 documented at Episode 7's"); the prediction verified.

## 3. THE CORPUS — inventory and routing (registration only; no content assessed)

54 episodes, 2026-03-19 → 2026-07-24. **CASE** marks a case-relevance hit on Owens' own title or published chapter text (41 of 54). Routing column gives the topic folder each item belongs to *if* it is later inventoried. **No episode below has been heard; nothing here is a finding.**

| Date | Ep | Title (verbatim, Owens' published title) | Flag | Route |
|---|---|---|---|---|
| 2026-03-23 | 314 | EXPLOSIVE! TPUSA Accuses Joe Kent Of Leaking To Harm Erika! | CASE | D-46 / main case |
| 2026-03-24 | 315 | REVEALED: Erika Went To A Weird Place On 9/10 | CASE | **D-46 resolving artifact** / main case |
| 2026-03-25 | 316 | Who's Lying? Frank Turek, Erika Kirk, Or Elizabeth McCoy? | CASE | main case |
| 2026-03-26 | 317 | VIRAL! It's Okay Not To Believe A Word Erika Kirk Says. | CASE | main case |
| 2026-03-30 | 318 | The 33 Club: Freemason Murder Plot EXPOSED! | CASE | arrest chronology (Robinson confession leg) |
| 2026-04-01 | 319 | PROVE ME WRONG: Tyler Robinson Is A Patsy. | CASE | **arrest chronology / court filings** |
| 2026-04-02 | 320 | Friends In High Temples: Charlie's Final Call With Bibi... | CASE | main case |
| 2026-04-03 | 321 | SNAPPED: Blake Neff Names A Killer. Pam Bondi Gets Fired. | CASE | main case |
| 2026-04-10 | 322 | An Open Letter To President Donald Trump (My Response) | — | out of scope |
| 2026-04-13 | 323 | Trump Attacks The Pope. The Tyler Robinson Narrative Collapses. | CASE | arrest chronology |
| 2026-04-14 | 324 | BREAKING: The ATF Traced A Gun On 9/10. Erika's "Friend" Wanted To Own Its Company. | CASE | **rifle/forensics + BOC (Erika leg)** |
| 2026-04-15 | 325 | Erika No-Shows JD Vance. Public Relations Lies About Why. | — | BOC-adjacent |
| 2026-04-16 | 326 | Secret Service Admits "There Was No Threat". ATF Releases Report. | CASE | **rifle/forensics** |
| 2026-04-20 | 327 | EXCLUSIVE AUDIO! Tyler Robinson's Grandfather Regarding His Rifle. | CASE | **rifle photo / DNA / arrest chronology** |
| 2026-04-21 | 328 | Lori Frantzve's Gun Deal? Terryl's Footage Faux Pas. | CASE | **BOC-E03 (Lori) + rifle/forensics** |
| 2026-04-22 | 329 | Victor Marx: The Man Who Weaponized Faith. | CASE | main case |
| 2026-04-29 | 330 | TIME MAGAZINE: World's Most VILE Person?! | CASE | out of scope |
| 2026-04-30 | 331 | BREAKING NEWS: Brian Harpole Sues Me! | — | out of scope (litigation against Owens) |
| 2026-05-04 | 332 | Daily Wire COLLAPSES! Ben Shapiro Wants REVENGE. | — | out of scope |
| 2026-05-05 | 333 | A Tale of Two PR Disasters: Blake Lively & Turning Point USA. | CASE | out of scope |
| 2026-05-06 | 334 | Brian Harpole Sends Out MORE Legal Notices. Jeremy Boreing Is Still A Creep. | — | out of scope |
| 2026-05-07 | 335 | STAGED? Erika's VIRAL White House Correspondents Moment Comes Under Scrutiny. | — | BOC-adjacent |
| 2026-05-11 | 336 | Update! Erika Did Not Go Home. Source Confirms AI Voice Tactics. | — | BOC-adjacent |
| 2026-05-13 | 337 | September 10th: The OTHER Shooting That The Media Forgot. | CASE | **main case** |
| 2026-05-14 | 338 | BREAKING! The White House Attempted To Rescind This E-mail. | CASE | main case |
| 2026-05-15 | 339 | SUSPICIOUS: More Bizarre Details From WHCD Shooting. Was It Staged? | CASE | out of scope (distinct incident) |
| 2026-05-18 | 340 | Hunter Biden Returns. The White House Ghosts Me Regarding Erika… | — | out of scope |
| 2026-05-20 | 341 | LIVE With Victor Marx: What Did He Know About 9/10? | CASE | **main case** |
| 2026-05-20 | 342 | TRENDING! I Send Out Some Legal Letters. Victor Marx's Bizarre Text To Erika Goes Viral. | CASE | main case |
| 2026-05-21 | — | Candace x Hunter Biden: The Interview | — | out of scope |
| 2026-05-26 | 343 | The World Is A Stage: Trump Survives...Again? | CASE | out of scope |
| 2026-05-27 | 344 | BREAKING NEWS: We've Identified "SAM702" At Fort Huachuca. | CASE | main case (aircraft thread) |
| 2026-05-28 | — | Candace Owens x Ana Kasparian | — | out of scope |
| 2026-06-09 | 345 | I'm Back! Russian Collusion & Turning Point Delusion. | — | out of scope |
| 2026-06-10 | 346 | Ivanka Trump "Discovers" An Island. Erika Kirk Calls It Quits Again. | CASE | BOC-adjacent |
| 2026-06-11 | 347 | OCCUPY BAAL STREET: Iran, Albania, And The TPUSA Takeover. | — | out of scope |
| 2026-06-13 | 348 | REVEALED! Trump Scolded Charlie Kirk Over Epstein. Butler Narrative Collapses. | CASE | out of scope (Butler) |
| 2026-06-15 | 349 | Erika Cries…Again. A Mysterious Death In Pennsylvania Reignites Butler Conspiracies. | CASE | out of scope (Butler) |
| 2026-06-17 | 350 | The FBI Crashes Out. We Examine The Exploding Microphone Theory. | CASE | **main case / forensics** |
| 2026-06-17 | 351 | A SHOCKING Discovery About The Man Who Mic'ed Charlie Kirk. | CASE | **main case / forensics** |
| 2026-06-18 | 352 | The Whistleblower: Did Epstein's Network Reemerge In Charlie Kirk's World? | — | BOC-adjacent (Epstein thread) |
| 2026-06-22 | 353 | I Survive My First Death Hoax, Erika Kirk Makes Human History. | CASE | BOC-adjacent |
| 2026-06-24 | 354 | Charlie's "Freedom" Shirt Disappears. Another Witness Recalls Erika & Epstein. | CASE | **main case (evidence chain) + BOC** |
| 2026-06-25 | 355 | Charlie's Final Ride To The Hospital Isn't Adding Up. Neither Is Daily Wire's Accounting. | CASE | **main case** |
| 2026-06-26 | 356 | TRUMAN SHOW: Proof That Charlie Kirk Was Targeted By The Elites | CASE | main case |
| 2026-06-26 | 357 | EMERGENCY UPDATE IN THE CHARLIE KIRK CASE! | CASE | **main case** |
| 2026-07-14 | 358 | I'M BACK! And The Tyler Robinson Show Trial Begins... | CASE | **arrest chronology — D-47** |
| 2026-07-15 | 359 | Blake Neff Blacks Out On 9/10. Andrew Kolvet Comes Clean About Netanyahu. | CASE | main case |
| 2026-07-16 | 360 | EXCLUSIVE RECORDING! The Lone Witness To The Shot On 9/10 Speaks Out. | CASE | **Losee building / main case** |
| 2026-07-17 | 361 | COLLECTIVE AMNESIA: Feds Fumble The Backpack. Frank Turek Changes His Story. | CASE | **main case (backpack evidence)** |
| 2026-07-21 | 362 | UH-OH! Navy Seal Sniper Says The Feds Are Lying. State Witness Has A TV Past… | CASE | **Losee building / witness** |
| 2026-07-21 | 363 | Erika Kirk Calls Me "That B*tch". More Exclusive Photos From Charlie's SUV. | CASE | main case + BOC |
| 2026-07-23 | 364 | Andrew Kolvet Blames Me For Erika PR Backlash \| "Mormon Mafia" History Explained | CASE | BOC-adjacent |
| 2026-07-24 | 365 | EXCLUSIVE: Ben Shapiro's 9/10 "Lunch" Date. More Text Messages From Charlie Kirk. | CASE | main case |

**Also registered (pre-window, closing the E07 queue):** Ep 309 "Did Erika Kirk Know Jeffrey Epstein?" (**2026-03-10**), Ep 310 "EXPLOSIVE! What Erika Kirk Was Doing In Epstein's Orbit…" (**2026-03-11**), Ep 311 "EXCLUSIVE VIDEO: The Footage Behind Charlie's Head" (**2026-03-12**). These are the "continuation set" queued in BOC-E07 Open Item 15 and flagged for main-case review in BOC-E06. Their air dates are now fixed at Tier 2 (Owens' published feed); their content remains uninventoried. Ep 311 routes to **main case (footage/forensics)**; 309/310 route to **BOC-adjacent (Epstein thread)**.

## 4. CASE POSTURE — verified as of 2026-07-27

The library's case-posture statements were last date-stamped 2026-07-20. **They are now out of date**, and the correction matters for anything written from here forward.

> ### ⚠ TIERING SUPERSEDED 2026-07-28 — the schedule legs are now Tier 1 (Q-43)
> **The briefing schedule below was right, and it was graded from the wrong source.** Everything in the "briefing schedule" and "declined to rule" bullets has since been **read directly out of this project's own banked Day 4 transcript**, in the parties' and the judge's own words — **`day4.txt` 08:08:11–08:21:46**, banked 2026-07-27, the day before this file said a "direct Utah court-record pull" would be needed to promote it.
>
> **Canonical statement: [CR-ACQ §5.1](../files%20-%20Court%20record/CR-ACQ-2026-07-27_court-record-acquisition.md).** Cite that, not this section, for any briefing date. It also carries **page limits (35/35/18)**, the **in-person, up-to-two-hours-per-side** format, the fact that the **State's 07-28 date was conditional** on transcript delivery, and — bearing directly on the 09-01 date — **Ms. Nester's request to move it, declined by the court.**
>
> **Which legs moved:** the hearing's conclusion, the reservation of the probable-cause ruling, and all four schedule dates → **Tier 1, High.** **Which did not:** the "roughly 30 hours," the six-felony-plus-Class-A charge list, and the death-penalty notice → **still T1 via T3, Medium-high.**
>
> **The lesson, and it is D-51's:** *where the project holds a primary artifact, no secondary source may set a fact the artifact can settle.* That rule was earned on 2026-07-27 and written on 2026-07-28 — and it was **not applied here**, on the one part of the record with real deadlines, until an independent pass went looking (**CR-AUDIT-2026-07-28 §2.3**). A rule that lives only in the file that earned it is not yet a rule.

Verified 2026-07-27 from named journalistic reporting (Deseret News, Utah-based) — **T1 via T3 as written; see the box above for what has since been promoted**:

- A **preliminary hearing** — *not* a trial — was held in the **Fourth District Court, Provo**, before **Judge Tony Graf**. ⚠ **D-51 REVERSED 2026-07-28:** a 2026-07-27 'correction' extending the hearing to 07-13 was **itself wrong** — Rev's page dates are publication dates lagging one business day. **The hearing ran 2026-07-06 → 2026-07-10 as originally recorded.**
- Prosecutors introduced forensic, video, and written evidence across roughly 30 hours.
- **Judge Graf declined to rule on probable cause at the close of the hearing**, granting the defense's request for written briefing.
- Briefing schedule: **State's opening brief due 2026-07-28** (tomorrow); **defense response 2026-08-11**; **State's reply 2026-08-18**; **oral arguments 2026-09-01 at 10:00 a.m.**
- Reported scope of the pending decision: "Graf will not rule on guilt or innocence; his only question is whether there is enough evidence for the case to proceed to trial."
- Charges: **six felonies** — including aggravated murder, witness tampering, and obstruction of justice — plus a Class A misdemeanor. The State has filed notice of intent to seek the **death penalty** if there is a conviction at trial.
- **Robinson has NOT been bound over for trial.** No trial has begun, and no trial date is established on this record.

> 🛠 **Posture updated 2026-09-16 (owner's ruling).** Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full. *The sentence above is retained as written, true as of its date; the ruling is `START-HERE` §0AH item 4 and `DOCKET-WATCH.md` v2.6.*

**Confidence as written 2026-07-27: Medium-high.** Single-outlet named reporting, internally specific and consistent with the other search-surfaced accounts, but the docket itself had not been read. ~~Promotion to High requires a direct Utah court-record pull.~~

⚠ **SUPERSEDED 2026-07-28.** The instinct was right — "the briefing dates in particular are exactly the kind of detail that should be confirmed against the court record before being relied on" — and the **remedy named was wrong**. No docket pull was required: the schedule was set in open court and the transcript of that proceeding was **already banked in this repository**, unread, when this paragraph was written. **Schedule legs now Tier 1 / High at [CR-ACQ §5.1](../files%20-%20Court%20record/CR-ACQ-2026-07-27_court-record-acquisition.md); the charge-list, 30-hours and death-penalty legs remain Medium-high here.** A docket pull (Q-03) is still wanted, but for the *filings*, not the dates.

## 5. NEW REGISTER ENTRY — D-47

*(Grep-verified: highest existing D-number before this assignment is D-46. The lone "D-47" string on disk is the forward-looking reminder in BOC-AUDIT-2026-07-20 Part 6, not an assignment.)*

| # | Subject | Claim (recording layer) | Record (analyst layer) | Sources | Status |
|---|---|---|---|---|---|
| **D-47** | "Show trial begins" framing | Ep 358 title, published **2026-07-14**: "I'M BACK! And **The Tyler Robinson Show Trial Begins**..." | No trial began. The proceeding was a **preliminary hearing**, held 2026-07-06 → 2026-07-10 and **already concluded four days before this episode aired**. Judge Graf reserved the probable-cause ruling for briefing (State 2026-07-28 / defense 2026-08-11 / reply 2026-08-18) and oral argument **2026-09-01**. Robinson was not bound over then and is not bound over as of 2026-07-27 | §3 (RSS title, retrieved 2026-07-27) vs. §4 (T1 via T3, Deseret News, retrieved 2026-07-27) | **RESOLVED against the literal claim** on the docket-fact leg; anchor TRUE and logged for Owens; characterization leg not resolvable (opinion) |

⚠ **Source upgrade, 2026-07-28 (Q-43) — the resolution is UNCHANGED.** D-47's docket leg rested on §4 at *T1 via T3*. The underlying facts — that the proceeding was a preliminary hearing, that it concluded 2026-07-10 before Ep 358 aired, and that the probable-cause ruling was reserved for briefing to 2026-09-01 — are now **Tier 1, read directly** (CR-ACQ §5.1). **This strengthens the evidentiary base of an existing resolution; it does not re-resolve it, and D-47 has not moved.** Nothing about the characterization leg changes: it remains opinion, unresolvable, and the anchor stays logged as a confirmation **for** Owens.

**Steelman, applied before resolving.** Three readings favor Owens and are addressed on their merits: (a) "show trial" is a pejorative *characterization* of the proceedings' fairness, not a docket assertion — correct, and that leg is therefore **opinion carrying zero evidentiary weight by its own terms**, neither resolved nor resolvable here; (b) "trial" may be loose usage for "the public court process," which did visibly begin in July 2026 — the **anchor is TRUE and is logged as a confirmation FOR Owens** under the both-directions rule; (c) an episode title is a headline, not a sworn statement, and headline compression is normal in the format — granted, which is why this resolves narrowly rather than as a global finding.

**What resolves, precisely:** the literal proposition "the trial begins" is **false as of its publication date and remains false today**. Nothing broader. This is the project's characteristic split — the **checkable anchor verifies** (a major public proceeding did occur in July 2026, days before the episode) while the **asserted characterization of it does not**, in exact conformity with the standing pattern finding.

**What would change it:** a docket entry showing a trial commencing on or before 2026-07-14 (none exists on the verified record), or a bindover order predating the episode.

## 6. ROUTING DECISIONS

1. **This corpus is not BOC material and is not filed as such.** BOC covers Erika Kirk's background and the series' claims about it. Roughly three-quarters of the corpus consists of direct claims about the assassination, the investigation, and the criminal case. Per BOC-E08 §14's routing note and the BOC-E06 precedent for Ep 311, that content belongs in the **main-case topic folders**.
2. **File placement, stated for the record.** This routing file is filed in `files - Bride of Charlie series/` because it *resolves a BOC register entry* (D-46) and continues the BOC series map. That placement is a deliberate compromise and **should not be read as classifying the corpus as BOC material.** If the corpus is inventoried, its files belong in `files - Kirk assassination questions`, `files - Arrest chronology`, `files - Losee building`, and `files - DNA evidence` per the §3 Route column — **user decision, not taken here** (§8 item 1).
3. **Highest-priority routes if inventorying proceeds** — the items that touch existing library files most directly. **Added v1.1: Ep 320** ("Friends In High Temples," 2026-04-02), whose published chapter markers include "22:42 – The CIA connection" and **"31:39 – The discontinued FBI forensic technique used on the JFK assassination being used again"** — a specific, checkable, case-directed forensic assertion, and now gradeable against the primary record this project has begun acquiring (`files - Court record`). Overlooked in v1.0; see BOC-AUDIT-2026-07-27B §2.4. The original four: **Ep 327** (Robinson's grandfather on the rifle → `evidence-rifle-photo-nypost-authenticity.md`, DNA, arrest chronology); **Ep 328** (a claimed Lori Frantzve gun transaction → BOC-E03, which is *about* Lori, **and** the forensics thread — the one item squarely in both corpora); **Eps 360/362** (a claimed lone witness to the shot, and a state witness → `files - Losee building`); **Ep 361** (the backpack → main case evidence chain).
4. **Explicitly out of scope** and marked so in §3: the Butler-shooting thread (Eps 348, 349), the White House Correspondents' Dinner incident (Eps 335, 339 — a distinct event), the Harpole litigation against Owens (331, 334), and Daily Wire/media-industry material (330, 332, 333, 343, 347).
5. **No register entry anywhere in this project may be resolved on this corpus until an episode is actually inventoried** from a transcript carrier, per §1. D-47 is the sole exception and rests on a title plus an independently verified public record, not on episode content.

## 7. FINDINGS

1. **D-46 RESOLVED** — finale not aired in series form (**High**); promised material delivered as regular Eps 314–317 beginning on the promised Monday (**High** on placement, **nothing** on content). §2.
2. **The migration pattern is confirmed a third time** (**High**) — after D-35 and the Epstein pair. Standing rule: sweep by channel and date, never by title string. BOC-E08 §15 predicted this instance in advance and the prediction verified. §2.
3. **D-45 RESOLVED** (recorded in BOC-E08 v1.1, not here) — CIA's own Directors Portrait Gallery gives Woolsey's DCI tenure as **5 February 1993 – 10 January 1995**, confirming he was a ~22-years-former director in 2017. Resolves **against** the sitting-director premise of Owens' "you can't just ring up the CIA" inference, while leaving the separate documentary-appearance anchor untouched and still — (checkable).
4. **D-47 RESOLVED against the literal claim**, anchor logged for Owens. §5.
5. **A 54-episode, 41-case-relevant corpus is uncovered by the library** (**High** as to existence and dates; **nothing** as to content). This is now the single largest known gap in the project. §3.
6. **The library's case posture was stale** and is corrected to 2026-07-27: ~~preliminary hearing concluded 2026-07-10~~ 🚨 **RE-CORRECTED 2026-08-17 (Q-136 sweep): the hearing was NOT concluded — it was CONTINUED.** 2026-07-06 → 07-10 were **five days of EVIDENCE**; **2026-09-01 is the hearing's LAST DAY, argument only on a closed record.** *(Tier 1 against the Day 5 transcript, established 2026-08-16; the correction reached `files - Court record` and START-HERE and stopped at this folder's boundary — standing hazard 18.)* **No bindover**, briefing through 2026-08-18, oral argument **2026-09-01**. §4. ⚠ **Updated 2026-07-28 (Q-43):** the schedule legs are now **Tier 1 / High**, read directly from the banked Day 4 transcript — canonical at **CR-ACQ §5.1**. The charge-list and death-penalty legs remain Medium-high. **The correction was right; its grade was too low, and the source named for promoting it was the wrong one.**
7. **Both-directions ledger for this session** — resolutions landed on both sides, as a functioning method requires. **For Owens:** the substance of the finale promise *was* delivered (§2 steelman); the D-47 anchor (a major public proceeding in July 2026) is true. **Against Owens:** the literal finale promise went unredeemed in form; the D-47 "trial" characterization is false on the docket record; the D-45 sitting-director premise fails.

## 8. OPEN ITEMS / ACQUISITION PATHS

1. **Scope decision (user) — inventory the corpus, or not?** 41 case-relevant episodes at roughly the BOC-E08 cost each (dual ASR carriers + adversarial verification). This is a program of work, not a task. Recommended shape if approved: start with the four §6.3 priority items, not chronologically.
2. **Utah court-record pull — promotes §4 from Medium-high to High** and is the decisive artifact for D-47's docket leg. Target: Fourth District Court docket, Case No. 251403576 (Utah XChange / district court records). **Cheapest high-value Tier 1 target now open in the whole project.**
3. **Transcript-carrier check for the corpus** — Podscripts carried Ep 8 and is the presumed carrier for regular episodes; HappyScribe is bot-blocked; pod.wave is the secondary. Confirm carrier coverage for the 300-series **before** committing to any inventory program.
4. **D-46 residual** — `candaceowens.com` remains outside the searched space for the series-null (unreachable 2026-07-20; not re-attempted today). The null is scoped to YouTube/RSS/Rumble and should say so wherever cited.
5. **Ep 315 verification** — the D-46 resolving artifact. If any single episode from this corpus is inventoried first on D-46 grounds alone, it is this one.
6. **V-12 / *Black Start* metadata** — still open after D-45's close-out: the documentary's credits, date, and the "Petria Patrick" director rendering remain — (checkable). IMDb/distributor route.

## 9. REGISTER SNAPSHOT

- **Assigned in this file:** **D-47** (resolved as stated in §5).
- **Resolved in this file:** **D-46**.
- **Resolved this session in BOC-E08 v1.1:** **D-45**.
- **Register runs D-1 – D-47, no gaps. Next number: D-48.**

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-27 | Initial file. Resolves **D-46**: the promised series finale never aired in series form (High; null re-confirmed against a fresh 2026-07-27 RSS pull, scoped to YouTube/RSS/Rumble), while the promised material migrated into regular numbered Eps 314–317 beginning on the promised Monday 2026-03-23 and delivered directly in Ep 315 on 2026-03-24 (High on placement, nothing on content) — the third confirmed instance of the migration pattern after D-35 and the Epstein pair, predicted in advance by BOC-E08 §15. Registers and routes the previously uncovered post-series corpus: 54 episodes 2026-03-19 → 2026-07-24, 41 carrying case-relevant markers, plus the Eps 309–311 continuation set now date-fixed (2026-03-10/11/12), closing the BOC-E07 Open Item 15 queue. Corrects the library's stale case posture to **2026-07-27** at Medium-high (preliminary hearing 2026-07-06→10, Fourth District Court, Judge Tony Graf; probable-cause ruling reserved for briefing; State brief due 2026-07-28, defense 2026-08-11, reply 2026-08-18, oral argument 2026-09-01; **no bindover**; six felonies plus a Class A misdemeanor; death-penalty notice filed). Assigns **D-47** (Ep 358 "Show Trial Begins" vs. the docket record) and resolves it against the literal claim after a three-part steelman, logging the true anchor as a confirmation FOR Owens per the both-directions rule. Access-path failures logged (CNN 451; cia.gov 403 to WebFetch but 200 to curl; two PDF text-extraction failures). Hard scope limit declared: no episode in this corpus was heard, watched, or transcribed — no register entry may resolve on §3 alone. |
| **1.2** | **2026-07-28** | **Q-43 executed on user authorisation, from CR-AUDIT-2026-07-28 §2.3. §4's tiering is superseded, and the reason is worth more than the fix.** This file recorded the briefing schedule at **Medium-high** from a single Deseret report and stated that "promotion to High requires a **direct Utah court-record pull**." No pull was required. **The whole colloquy was already banked in this repository** — `day4.txt` 08:08:11–08:21:46, retrieved 2026-07-27, the day before this file was written — and the schedule is stated there in the parties' and Judge Graf's own words. **This is the D-51 failure exactly**, on the one part of the record with live deadlines, and it survived two adversarial passes because both checked what the files *said* against the artifacts and neither asked what the artifacts said that the files had *not looked for*. **Promoted to Tier 1 / High:** the hearing's conclusion, the reservation of the probable-cause ruling, and all four schedule dates. **Left at T1 via T3 / Medium-high:** the "roughly 30 hours," the six-felony-plus-Class-A charge list, and the death-penalty notice. **Canonical statement relocated to CR-ACQ §5.1**, which additionally records the 35/35/18 page limits, the in-person two-hours-per-side format, the State brief's conditional basis, **Ms. Nester's declined request to move the 09-01 argument**, and Jeffrey Neiman's appearance for the victim's representative. **D-47 is NOT re-resolved** — its docket leg is better sourced, its resolution and its steelman stand unchanged, and the register has not moved. §4's own instinct ("exactly the kind of detail that should be confirmed against the court record") is logged as **correct**; only the remedy it named was wrong. |
| 1.1 | 2026-07-27 | **Corrected on adversarial re-read (BOC-AUDIT-2026-07-27B).** Three fixes, none of which changes a routing decision or a register entry. (a) **Headline figure corrected from "41 case-relevant" to ~35**: the 41 was a raw keyword-regex count that fires on the **Butler rally shooting** (Eps 348, 349), the **White House Correspondents' Dinner shooting** (Eps 339, 343) and media disputes (330, 333) — six episodes about *other events*, all of which §3's routing column had already sent out of scope. The table was sound; the number summarizing it was not. (b) **"Third instance of the migration pattern" separated into two phenomena**: content migration is confirmed **twice** (Eps 309–311, 314–317), while **D-35 is a title-rendering hazard** — Episode 8 *was* a numbered series installment whose podcast simulcast dropped the prefix. The operational rule (*sweep by channel and date, never by title string*) survives all three unchanged; the claim of a three-times-confirmed publishing regularity does not. (c) **Ep 320 added to the §6.3 priority list** for its published claim about "the discontinued FBI forensic technique used on the JFK assassination being used again" — a specific case-directed forensic assertion overlooked in v1.0 and now gradeable against `files - Court record`. |
| 1.3 | 2026-09-16 | **Posture line updated to the owner's ruling of 2026-09-16.** The case-posture banner/statement now carries, beneath the sentence it had: *Bound over on all seven counts on 2026-09-01 (signed order held at Tier 1, clerk's certificate 09/02/2026); not-guilty pleas entered by counsel the same day; presumption of innocence applies in full.* The earlier sentence is retained as written (true as of its date). No finding, grade, label or citation changed. |
