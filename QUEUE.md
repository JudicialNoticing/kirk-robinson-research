# QUEUE — Machine-Readable Work Graph

**Purpose:** the project's open items, already scattered across every file's §Open Items and every audit's launch pad, gathered into **one dispatchable list**. This is the artifact an autonomous loop reads to decide what to do next. It is also just a good index for a human.
**Generated:** 2026-07-28 · **Register ceiling:** **D-52** *(assigned 2026-07-28, CR-E05 §5 — Exhibit 12.1's Day 1 exclusion; **OPEN**)* · **Next number:** **D-53**
**Protocol:** see [LOOP.md](LOOP.md). **Validator:** `./queue-check.sh`

> **Loop is DISARMED.** Cron `28cde284` was created 2026-07-28 and **cancelled the same day at session close**, before it ever fired. **Zero cycles have run; every Q item below is in its authored state.**
> **To arm it:** create a recurring `CronCreate` job whose prompt is the cycle spec — validate with `./queue-check.sh`, take the top `ready` item, honour its gate per LOOP.md §3, execute to files, update this queue, log to the session audit, re-validate, commit with the Q-ID in the subject, push. Session-only; expires in 7 days; fires only while idle.
> **Audit any cycles:** `git log --oneline --grep='Q-[0-9]'`.
> This never covered the docket (DOCKET-WATCH.md) — that needs a durable cloud routine via `/schedule`, and it is the half with real deadlines.

## How to read this

| Column | Meaning |
|---|---|
| **ID** | Stable handle. `Q-nn`. Never reused. |
| **P** | Priority 1 (do next) → 5 (someday) |
| **Status** | `ready` · `blocked` · `doing` · `done` · `parked` (needs a human decision) |
| **Blocked by** | Q-IDs, or an external condition |
| **Decisive artifact** | The specific thing that closes it. If this column is empty the item is not actionable — fix that before dispatching it. |
| **Cost** | `S` <1h · `M` a session · `L` multi-session · `XL` a programme |
| **Gate** | `auto` — a loop may execute and commit · `verify` — must survive an independent pass before findings harden · `human` — stop and ask |

**Gate rules are not advisory.** See LOOP.md §3. Anything touching **case posture**, **a living person's conduct**, or **spending money** is `human` regardless of what else it says.

---

## P1 — do next

| ID | Item | Status | Blocked by | Decisive artifact | Cost | Gate |
|---|---|---|---|---|---|---|
| ~~Q-01~~ | ~~**Read hearing Day 1**~~ | **done 2026-07-28** | — | **[CR-E05](files%20-%20Court%20record/CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md)** v1.0, `[PROVISIONAL]`. Read end to end, full coverage. **Exhibit 12.1 was OFFERED AND EXCLUDED on Day 1** (→ **D-52**); **Officer Chris Bagley** enters the library — first officer on the Losee roof, **searched for a casing and found none**; **Exhibit 11 is the 9-page ME report, ADMITTED** (→ Q-15/D-49); the whole **Rule 1102 architecture** with all five video sources absent. ⚠ **Rev's Day 1 speaker labels are broken** → hazard 9. Spawned **Q-51…Q-54** | M | verify |
| **Q-54** | **Independent verification cycle on CR-E05** — the file is `[PROVISIONAL]` and **no cycle has run on it**. The Q-14 cycles found 6 defects and 14 omissions in a section one-tenth its size; **assume both until checked.** Both passes needed: proposition-testing **and** completeness | ready | — | the cycle, worked from `day1.txt` | M | verify |
| **Q-51** | **State's Exhibit 11 — the Utah ME report of examination** (9 pp., Dr. Guajardo). **Admitted 2026-07-06, publication denied.** **Decisive for Q-15 / D-49** — the fragment count. The library did not know it was in evidence | ready | — | Exhibit 11 | S | human *(Q-15 is human-gated; this inherits)* |
| **Q-52** | **The Day 2 re-offer of Exhibit 12.1** — what foundation was supplied after Day 1's exclusion, and whether Exhibit 12.3 was **amended or replaced**. **Resolves D-52.** Sits alongside Q-11 and CR-ACQ §8 item 12 | ready | — | `day2.txt`, the 12.1 re-offer passage | S | verify |
| **Q-53** | **Bagley's body-camera recording** (27 min 35 s — his only footage; **shows the unidentified armed man in civilian clothes**) and **his police report** ("Bagley 1", shown to the witness only, never offered) | ready | — | the recording + the report | M | verify |
| ~~Q-02~~ | ~~**Independent adversarial pass** on all 2026-07-27/28 output~~ | **done 2026-07-28** | — | **[CR-AUDIT-2026-07-28](files%20-%20Court%20record/CR-AUDIT-2026-07-28_independent-pass.md)** — six defects, three material; nothing in the forensic record misquoted; D-51 confirmed on two new tests. Spawned **Q-42, Q-43, Q-44**; re-ranked Q-14. **Residual: same model, different session — a human or differently-built reader is still owed** | M | verify |
| ~~Q-43~~ | ~~**Promote the briefing schedule to Tier 1, read directly**~~ | **done 2026-07-28** (user-authorised) | — | **[CR-ACQ §5.1](files%20-%20Court%20record/CR-ACQ-2026-07-27_court-record-acquisition.md)** — now the library's canonical statement of the briefing order. BOC-ROUTE v1.2, DOCKET-WATCH v1.1, CR-E04 v1.1, LOOP repointed. **D-47 not re-resolved.** Full read added: the **07-28 date is conditional** on transcript delivery; the order's procedural history; **a reserved Exhibit 12.1 ruling nobody was tracking** (→ CR-ACQ §8 item 12) | S | **human** — gate satisfied |
| Q-03 | **Docket pull** — Fourth District, Case 251403576. Settles D-51's underlying facts, the bullet-fragment motion ruling, and the briefing status | blocked | XChange paywalled (Q-31); DocumentCloud bot-gated (Q-32) | the docket itself | S | human |
| Q-04 | **Briefing set as filed** — dates now Tier 1 (CR-ACQ §5.1). ⚠ **The 07-28 date was conditional** on the reporter delivering by 07-13, so a slip may signify nothing; and **a defence continuance risk against 09-01 is on the record**. Both sides' evidence theory in their own words | ready | — | the filed briefs | S | verify |
| **Q-45** | **Acquire the State's opening probable-cause brief** — **reported filed 2026-07-28** (CR-WATCH-log Run 1), T1 via T3, one independent source. **The document is not held and its contents are deliberately unrecorded until it is.** No public PDF mirror found on any route tried; recheck outlets next cycle, and the Utah County Attorney media page, which posts case documents but had nothing after 2026-06-26 | ready | — | the brief itself | S | verify |
| **Q-46** | **The contempt-hearing transcript, c. 2026-06-22** — Rev page "Tyler Robinson Comtempt Hearing" *[sic]*, page date 2026-06-23. **A proceeding entirely absent from this library's inventory**, which holds only the five hearing days. Nature and subject unknown | ready | — | the transcript | S | verify |
| **Q-47** | **The Kirk-family motion of 2026-07-10** asking the court to make the probable-cause determination no later than Sept. 1. Reported via a search snippet only; contents not characterised | ready | — | the motion | S | verify |
| Q-05 | **Inventory Ep 319** ("Tyler Robinson Is A Patsy") — **decisive for D-48**, which has moved four times. A Tier 1 record now exists to grade it against | ready | Q-20 (carrier check) | episode transcript | M | verify |

## P2 — high value, unblocked

| ID | Item | Status | Blocked by | Decisive artifact | Cost | Gate |
|---|---|---|---|---|---|---|
| Q-06 | **Bakker past her opening** (~384 turns, Day 2) + **Exhibit 31** — the likelihood ratios behind Robinson's inclusion on the **towel and screwdriver** are unknown | ready | — | day2.txt + Exhibit 31 | M | verify |
| Q-07 | **Feed `files - Losee building`** (62 lines, no primary sourcing) from CR-E02 §2 and CR-E04 §4 — rooftop processing, 415/410/68 geometry, the movement timeline | ready | — | write the file | M | verify |
| Q-08 | **Feed `files - DNA evidence`** from CR-E03 §3 (Oliver's limits) and CR-E02 §5.1. **Must carry the mixture/activity/consumption caveats** | ready | — | write the file | M | verify |
| Q-09 | **Feed `lance-twiggs-comprehensive-profile.md`** from CR-E02 §5.3 and CR-E03 §4.3. **Must record the use immunity** from both offices | ready | — | write the file | M | human |
| Q-10 | **Feed `files - Arrest chronology`** from CR-E03 §4.2 (Mitchell, surrender) and CR-E04 §5.5 | ready | — | write the file | M | verify |
| Q-11 | **Oliver's testimony after the isoallele objections**, incl. any State cross. ⚠ **Also settles CR-ACQ §8 item 12** — whether the full **Exhibit 12.1** was played in open court, a ruling reserved at the close of Day 4 | ready | — | day5.txt | S | verify |
| Q-12 | **Novak's cross of Davis** (Day 3) | ready | — | day3.txt | S | verify |
| Q-13 | **Hull's later cross** (from the Ty Phillips video line) + any redirect | ready | — | day2.txt | S | verify |
| ~~**Q-14**~~ | ~~**Faumuina's Day 2 turns** (58)~~ | **done 2026-07-28** | — | **[CR-E03 §5A](files%20-%20Court%20record/CR-E03_prelim-hearing-Days2-3-5.md)** v1.2, `[PROVISIONAL]`. **The likelihoods CR-E03 §5 called "unknown" are on the record** — 1.7 octillion (towel) and 30 quintillion (screwdriver), **both conditioned on Twiggs as one of two contributors**. Two verification cycles run: proposition-testing found **6 defects in the draft**, completeness found **14 omissions**, incl. the **Rule 1102 constitutional standing objection** the exhibit came in under, and that **the previewed cross never happened — the figures went untested for two hearing days**. Spawned **Q-48, Q-49, Q-50**; **hazard 9** added | S | verify |
| **Q-42** | **Re-grade the chamber-case identity: it is sworn testimony, not an inference.** CR-E02 §4 holds it at "well-supported inference, Medium-high" and CR-AUDIT-2026-07-27 §2.4 graded it *down*, but Faumuina mapped ATF Exhibits 2, 3–5 and 18A to provenance outright at day4 05:39:52. Relaxes CR-ACQ §6.2's dependent caveat. **Direction of D-48 unaffected** | ready | — | the re-grade; the passage is already read and quoted in CR-E02 §4 | S | **human** (touches D-48, which has moved 4× — past LOOP §4's third-movement stop) |
| **Q-48** | **Dockets 631 and 678** — the **denial** of the defence motion to hold Art. I §12 / Rule 7B / Rule 1102 unconstitutional as to reliable hearsay at a preliminary hearing (631), and the **standing objection** filed 2026-07-03 (678). Both named on the record at day2 00:17:51. **Every hearsay exhibit in this case — including Exhibit 31 — came in over this objection**, and it covers Day 1 as well ("all of yesterday's proceedings"). The library has neither document | ready | — | the two filings | S | verify |
| **Q-49** | **Did the Day 4 cross of Faumuina ever reach her Day 2 subject matter?** Burt reserved cross "until she has completed her testimony"; Day 2 adjourned without recalling her, so **the towel and screwdriver figures went uncrossed for two hearing days**. CR-E02 covers Day 4 but was not written with this question in mind | ready | — | day4.txt, re-read against this question | S | verify |
| Q-15 | **D-49 — the fragment count.** ME photo reportedly shows seven; ATF received five | ready | — | **the medical examiner's report + photograph**; chain-of-custody records | M | human |

## P3 — exhibits and records, known to exist

| ID | Item | Status | Decisive artifact | Cost | Gate |
|---|---|---|---|---|---|
| Q-16 | **Exhibits 33 and 34** — the ATF **biology** and **toolmark comparison** reports. Q-34 carries the Dremel-bit identification; both known only from a witness reading paragraphs aloud | ready | the exhibits | M | verify |
| Q-17 | **Exhibit 30** (ATF DNA, rifle) and **Exhibit 32** (ATF firearms) — read directly rather than via testimony | ready | the exhibits | S | verify |
| Q-18 | **Surveillance exhibits 12.1 / 12.3 / 12.4** — the compilations and Olson's authenticating statement. **12.1 was admitted but withheld from publication** | ready | the exhibits | M | verify |
| Q-19 | **The bystanders' video and interview** — two young men filmed the roof ~10s before the shot and believed they were seeing **police overwatch**. Hull never read their interview | ready | video + interview | M | human |
| Q-33 | **Trooper Gonzalez's report** and the holster/handgun items | ready | the report | S | verify |
| Q-34 | **Sgt. Bricker's timeline** and **Hull's 2025-09-14 report** | ready | the reports | S | verify |
| Q-35 | **The bullet-fragment motion ruling** and the **State's response** to it — the exculpatory-characterization dispute is open only because neither is held | blocked | Q-03 | docket | S | verify |
| Q-36 | **Certified court transcript**, replacing the commercial rendering, before any register entry resolves on transcript quotation | ready | the certified transcript | M | human |
| **Q-44** | **Two ATF documents disagree on which cartridges bore scribe marks.** The 2025-09-17 report says "Exhibit 2 … **and Exhibit 3 cartridges**"; **Exhibit 34** says "Exhibit 2 … **Exhibit 3 through five** … and Exhibit 18A." Probably a typo in the earlier one; unresolvable without the exhibits. **No D-number** — only one of the two documents has been read directly | blocked | Q-16 / Q-17 (the exhibits) | Exhibits 32 and 34 | S | verify |

## P3 — the Owens corpus

| ID | Item | Status | Blocked by | Decisive artifact | Cost | Gate |
|---|---|---|---|---|---|---|
| Q-20 | **Transcript-carrier check for the 300-series** — prerequisite for any episode inventory. Podscripts presumed; HappyScribe bot-blocked; pod.wave secondary | ready | — | a successful pull | S | auto |
| Q-21 | **Ep 320** — published claim re "the discontinued FBI forensic technique used on the JFK assassination being used again." Now gradeable against the court record | ready | Q-20 | transcript | M | verify |
| Q-22 | **Ep 327** (Robinson's grandfather on the rifle) → rifle-photo dossier, DNA, arrest chronology | ready | Q-20 | transcript | M | verify |
| Q-23 | **Ep 328** (claimed Lori Frantzve gun transaction) — the one item in **both** the BOC and forensics corpora | ready | Q-20 | transcript | M | verify |
| Q-24 | **Eps 360 / 362** (claimed lone witness; state witness) → Losee building | ready | Q-20 | transcripts | M | verify |
| Q-25 | **Ep 361** (the backpack) → main-case evidence chain | ready | Q-20 | transcript | M | verify |
| Q-26 | **The corpus programme decision** — ~35 case-relevant episodes at roughly BOC-E08 cost each. **A programme, not a task** | parked | — | **user decision** | XL | human |

## P4 — BOC register backlog (known decisive artifacts, low stakes)

| ID | Item | Status | Decisive artifact | Cost | Gate |
|---|---|---|---|---|---|
| Q-27 | **D-25** — AZ Corporation Commission filing images (incorporator line) | ready | ACC images | M | human |
| Q-28 | **D-42** — Ohio SoS (VRI date); Az-Tech event history | ready | Ohio SoS record | S | human |
| Q-29 | **D-40 / D-41** — ASU Spring 2012 commencement programme. Physical route: University Archives, Hayden Library rm. 138; ≥5 business days | ready | the programme | L | human |
| Q-30 | **E07 F-1(d)** — NY DOS FOIL for the license record | ready | FOIL response | L | human |
| Q-37 | **T1 roadmap E08-1** — *Black Start* credits/metadata; also settles **V-12**, where the two ASR carriers **diverge** on the director's name (Petria/Patria) | ready | IMDb/distributor credits | S | verify |
| Q-38 | **Phase 1 orders** — M-2 (birth record, cheapest decisive), M-1, M-11. Unstarted since the roadmap was written | ready | vital records | L | human |
| Q-39 | **Re-polls** — IRS 2026 XML (FYE2025 990s), archive.today captures, SAM.gov API key | ready | the pulls | S | auto |

## Blocked / gated on a decision or a payment

| ID | Item | Why | Gate |
|---|---|---|---|
| Q-31 | **Utah XChange subscription** — $10 one-time or $25 + $40/mo. Would open the docket directly | costs money | **human** |
| Q-32 | **DocumentCloud project 224251** — bot-gated (403 / JS). Needs an interactive browser session | needs a live browser | **human** |
| Q-41 | **Integrate the claude.ai project material** — files and ~3 chats from the claude.ai project "Kirk Robinson Research," last 24h as of 2026-07-28. **Not reachable from this environment**: no claude.ai Projects connector; Artifact list, Google Drive and local disk all checked and clear. Needs the user to export to disk, paste, or supply artifact URLs (those *are* fetchable). **Integration is not a copy** — each item needs a sourcing tier, a register check against D-1–D-51 so no duplicate numbers are assigned, and a dedup pass against the eight BOC files and five court-record files. Any findings enter `[PROVISIONAL]` per LOOP.md §2 | blocked | user must supply the content | the exported files / pasted text / artifact URLs | M | **human** |
| **Q-50** | **Does Oliver's household-transfer explanation reach the towel and the screwdriver?** Her "reasonable to assume that anyone living in the household could have contributed to DNA on an object found in **that household**" (CR-E03 §3.3) covers the Dremel. **These two items were recovered away from the household** — the towel in the wooded area, the screwdriver on the roof. Whether that distinction carries weight bears on **a living person who is not accused and testified under use immunity** | conduct of a living person | **human** |
| Q-40 | **`files - George Zinn`** — CR-E04 §5.4 records an early detention expressly **not** treated as a suspect. **Whether this concerns that matter is NOT established and must not be assumed** | living person; unestablished identity | **human** |

---

## Standing hazards (read before dispatching anything)

1. **Selective quotation** — a quotation by an interested party is reliable as to the words, never as to the document. (CR-ACQ §0)
2. **Provenance** — a forensic report is silent about where its exhibits came from. Provenance is a **separate** verification act. (CR-AUDIT §4)
3. **Sampling** — keyword sampling of sworn testimony finds *topics* and misses *conclusions*. (CR-E02 §1)
4. **Metadata vs. content** — a page date is a fact about a publishing schedule, not about a courtroom. **Always ask what a datum is a fact *about*.** (D-51 reversal, CR-E03 §7)
5. **Search nulls** — a null from a text search is a claim about the search until the method is validated against a known positive. (BOC-AUDIT-2026-07-27B §4)
6. **Register numbering** — grep, then **read the hit**. Forward-looking "next is D-nn" notes have matched the pattern five times without yet causing an error.
7. **Exhibit numbers are not unique** — the State and the defence each have an "Exhibit 19" on Day 4, and the transcript renders both bare. **Always write "State's" or "the defence's."** Merging them would put the chamber cartridge case inside the AFTE proficiency-test demonstration. (CR-AUDIT-2026-07-28 §2.1)
10. **Transcript timestamps are RECORDING-STREAM time, not time of day.** The clock jumps across every recess (Day 2: ~1 hour). **"day2 05:10:57" is an identifier, not 5:10 p.m.** Citing them as locators is correct; **converting one to a clock time, or computing a duration across a recess, is not.** Related: **part-seams can fall mid-question**, with counsel's words duplicated either side — quoting across one can render a single question as two. (CR-E03 §1, added 2026-07-28.)
9. ⚠ **REV'S SPEAKER LABELS ARE NOT EVIDENCE — infer every speaker from content.** *(New 2026-07-28, Q-14 verification + Q-01 inspection. Potentially the most damaging hazard yet found, because it corrupts attribution rather than content.)* Rev's diarisation fails **systematically** across this corpus, and worst on **Day 1**:
   - **Day 1: a witness's sworn answers carry a defence attorney's label.** Officer Chris Bagley's testimony is labelled "**Richard Novak**" — Rev merged the witness and his cross-examiner into one label. A file quoting Day 1 from labels would **attribute a police officer's sworn testimony to defence counsel.**
   - **Day 1: there is no "Sturgill" label at all**, though Judge Graf hands Hull's direct to Mr. Sturgill; the next turn is labelled "Ryan McBride."
   - **The oath is misattributed on at least three days** — to defence counsel "Kathy Nestor" on Days 1 and 2, and on Day 5 to **the witness being sworn**, which is impossible.
   **Rule: identify speakers functionally (question vs. answer, argument vs. ruling) and name a person only with a stated basis — e.g. the court addressed them by name in an adjacent turn.** Where a label and the content disagree, **the content wins.** Anything already written against a Day 1 label must be re-checked before it hardens.
8. **Over-hedging is a defect too.** Two of this project's corrections have now run *toward* the State — the Dremel identification (CR-E02 v1.2) and the chamber-case identity (Q-42) — both because a summary graded down what the record states outright. **A caveat that the evidence does not support is as much an error as a claim it does not support.** (CR-AUDIT-2026-07-28 §2.2)

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.2 | 2026-07-28 | **Q-43 executed and closed** on user authorisation. The briefing schedule is now **Tier 1, read directly**, canonical at **CR-ACQ §5.1**; BOC-ROUTE, DOCKET-WATCH, CR-E04 and LOOP repointed; **D-47 not re-resolved and the register has not moved.** The full colloquy added what the audit extract had not: the **07-28 date is conditional** on the court reporter, the order's procedural history, and **a reserved Exhibit 12.1 publication ruling** now folded into **Q-11**. **Q-04 annotated** with both caveats. Still open from Q-02: **Q-42** (human) and **Q-44** (blocked). |
| 1.1 | 2026-07-28 | **Q-02 executed and closed** → `CR-AUDIT-2026-07-28`. Six defects, three material; every forensic quotation tested came back verbatim. Three items spawned, each queued rather than executed because its gate binds the pass that found it: **Q-43** (briefing schedule held at second hand while the banked Day 4 transcript settles it — `human`, case posture, **and the only new P1**), **Q-42** (chamber-case identity is testimony, not inference — `human`, touches D-48 past its third movement), **Q-44** (inter-document scribe-mark tension — blocked on the exhibits). **Q-14 re-ranked** — Faumuina's Day 2 turns carry FBI DNA results read into the record. **Two standing hazards added** (7: exhibit numbers are not unique across parties; 8: over-hedging is a defect, and two corrections have now run toward the State). **No register entry assigned or moved; ceiling stays D-51.** |
| 1.0 | 2026-07-28 | Initial queue. 40 items harvested from the §Open Items and launch pads of CR-ACQ, CR-E01–E04, CR-AUDIT, BOC-AUDIT-2026-07-27/B, BOC-ROUTE, BOC-T1 and the BOC episode files. Gates assigned per LOOP.md §3; the five standing hazards carried forward from the files that earned them. |
