# BOC-AUDIT-2026-07-27B — Adversarial Verification Pass on the BOC Side of the 2026-07-27 Session

**File ID:** BOC-AUDIT-2026-07-27B
**Scope:** the adversarial pass that **CR-AUDIT-2026-07-27 §5.4 declared still owed** — a deliberately skeptical re-read of the BOC-side output of 2026-07-27: **D-45**, **D-46**, **D-47**, **BOC-ROUTE v1.0**, **BOC-T1 v1.4**, **BOC-E07 v1.4**, **BOC-E08 v1.1**.
**Method:** default-skeptical, checking each load-bearing claim against the banked primary artifacts (`transcript_primary.txt`, `transcript_secondary.txt`, `feed_20260727.xml`) rather than against the files' own reasoning. The question asked was *"what would have to be true for this to be wrong?"* — not *"can I find support?"*
**Prepared:** July 27, 2026
**Status:** v1.0

**Headline result:** the BOC side held up **better than the court-record side did**. **No resolution was reversed.** D-45 survives a test it had not previously been given, and the T1 integration is provably complete. But the pass found **two real defects — both of them overstatements in headline positions** — plus one under-weighted item and one methodological near-miss worth recording.

---

## 1. WHAT WAS CHECKED

| Claim | Verdict |
|---|---|
| **D-45** — Owens renders Woolsey as "the CIA director"; CIA gives tenure 5 Feb 1993 – 10 Jan 1995 | **CONFIRMED on a test not previously run.** §2.1 |
| **D-46** — finale never aired in series form; material ran as Eps 314–317 | **CONFIRMED and correctly bounded.** §3 |
| **D-47** — "Show Trial Begins" vs. a concluded preliminary hearing | **CONFIRMED.** §3 |
| **"41 of 54 case-relevant"** (BOC-ROUTE headline, echoed in two audits) | **DEFECT — overstates. The honest figure is 35.** §2.2 |
| **"Third confirmed instance of the migration pattern"** | **DEFECT (precision) — conflates two distinct phenomena.** §2.3 |
| **T1 Part B E08 table** — 19 rows built from E08 §16 | **CONFIRMED COMPLETE** — 19 rows against 19 source items, nothing dropped. §3 |
| Register integrity D-1–D-50 | **PASS** — no gaps, one assignment site per number |
| Ep 320's forensic claim | **UNDER-WEIGHTED** — §2.4 |

## 2. FINDINGS

### 2.1 D-45 — CONFIRMED, on a test it had not previously been given

**The risk that was never checked.** D-45 resolves against Owens' premise that the *Black Start* documentary "features **the CIA director** James Woolsey." But BOC-E08 rests entirely on **machine ASR transcripts**, and E08 §1 declares that limitation itself. A dropped qualifier — "**former** CIA director," "**ex**-CIA director" — is exactly the kind of word ASR loses, and it would have **collapsed the discrepancy entirely**: if Owens said "former," there is no misrendering and no premise to resolve against. Today's session resolved D-45 **without re-checking the carriers.**

**The test.** Both banked carriers were flattened (line structure defeats naive grep — see §4) and searched for the passage and for any qualifier near "CIA," "Woolsey," or "director."

| Carrier | Rendering |
|---|---|
| Podscripts (primary) | "…she that appears in this documentary that's called Black Start by **Petria Patrick**. The documentary also features **the CIA director James Woolsey**." |
| pod.wave (secondary) | "…she then appears in this documentary that's called Black Start by **Patria Patrick**. The documentary also features **the CIA director James Woolsey**." |

**Result: CONFIRMED.** Two independent ASR passes render the operative phrase **identically**, and **neither contains "former," "ex-," or any temporal qualifier** anywhere near the phrase. The premise Owens' inference rests on is as E08 recorded it. **D-45's resolution stands at High.**

**Incidental finding for V-12.** The carriers **diverge on the director's name** — "**Petria**" (primary) vs "**Patria**" (secondary). E08 recorded "Petria Patrick [as heard]," which matches the primary but silently picks one of two renderings. Minor, but it should be declared rather than chosen: **the name is unresolved between carriers**, which strengthens the case for pulling the documentary's actual credits (E08-1 / T1 roadmap).

### 2.2 DEFECT — "41 of 54 case-relevant" overstates; the honest figure is 35

**What the files say.** BOC-ROUTE §3's headline, echoed in BOC-AUDIT-2026-07-27 Part 8 and in the memory record, reports **"54 episodes, 41 case-relevant."**

**What the number actually is.** The 41 is a **keyword-regex count**, not a curated classification — a hit on Owens' title or the first 600 characters of her published description. Re-testing the flagged episodes shows the regex fires on **other events entirely**: the **Butler** rally shooting (Eps 348, 349), the **White House Correspondents' Dinner** shooting (Eps 339, 343), and general media disputes (330, 333). **Six CASE-flagged rows are routed "out of scope" in this project's own table.**

**Assessment.** The **routing column caught every one of them** — the table itself is sound, and no misrouted episode entered the priority queue. The defect is confined to the **headline figure**, which conflates "keyword hit" with "relevant to *this* case" and travels more easily than the table does. **Corrected figure: 54 episodes, of which ~35 route to case-relevant destinations and 6 concern other events.** BOC-ROUTE §3's method caveat was accurate; the headline that summarized it was not.

### 2.3 DEFECT (precision) — "three confirmed instances of the migration pattern" conflates two phenomena

Today's files assert a **"third confirmed instance"** of a single migration pattern, and BOC-E07 v1.4 promotes it to a **standing project rule**. On re-read, the three instances are **not the same phenomenon**:

| Instance | What actually happened | Phenomenon |
|---|---|---|
| **D-35** (Episode 8) | A **numbered series installment** — "Bride Of Charlie: Red Sparrow \| Episode 8" on YouTube — whose **podcast simulcast dropped the series prefix** | **Title-rendering hazard**: same content, different label per platform |
| **Eps 309–311** (Epstein pair + footage) | **Regular numbered episodes** carrying series-adjacent subject matter | **Content migration** |
| **Eps 314–317** (the alibi material) | **Regular numbered episodes** carrying the promised finale's subject matter | **Content migration** |

**Assessment.** Content migration is confirmed **twice**, not three times; the title-rendering hazard is confirmed **once**. **The operational rule survives intact** — *sweep by channel and date, never by title string* — because all three would defeat a title-string search, which is what the rule guards against. But "three instances of the migration pattern" is imprecise and, left standing, would let a future session infer a stronger regularity in Owens' publishing behaviour than the evidence supports. **Corrected in place** (§5).

### 2.4 UNDER-WEIGHTED — Ep 320's forensic claim

Ep 320 ("Friends In High Temples," 2026-04-02) was flagged CASE and routed "main case," but its content was not surfaced in any priority list. Its published chapter markers include **"22:42 – The CIA connection"** and **"31:39 – The discontinued FBI forensic technique used on the JFK assassination being used again."**

That second item is a **specific, checkable, case-directed forensic assertion** — the kind this library is built to grade, and now gradeable against the primary record the project has begun acquiring. **It belongs in the inventory priority list alongside Eps 327/328/360/362/361**, and was omitted. Added at §5.

## 3. WHAT SURVIVED

- **D-46** — the null is correctly scoped (YouTube/RSS/Rumble; candaceowens.com excluded), the placement finding rests on Owens' own titles and chapter markers, and the files repeatedly state that **the episodes were never heard**. The "High on placement / nothing on content" split is properly drawn. **No over-claim found.**
- **D-47** — the steelman is genuine (three readings offered, one conceded as a confirmation *for* Owens), and the docket fact is unambiguous: the preliminary hearing **concluded 2026-07-10**, four days before Ep 358 aired, so "begins" fails on any reading. **Confirmed.**
- **BOC-T1 v1.4** — **19 table rows against 19 source items in E08 §16.** Verified by count and by content: §16 item 4 was correctly **split** into two rows (Woolsey / *Black Start*) and items 1–2 correctly **merged** into one file-maintenance row. **Nothing dropped, nothing invented.**
- **Register integrity** — D-1–D-50, no gaps, one assignment site per number; forward-looking "next is D-N" notes were read rather than pattern-matched, the hazard having now fired four times without causing an error.
- **Scope discipline** — every BOC file states what it did not verify. BOC-ROUTE §1's declaration that no episode was heard is repeated at every point where it matters.

## 4. METHODOLOGICAL NEAR-MISS WORTH RECORDING

The first attempt to test D-45 used `grep -o ".\{300\}woolsey.\{200\}"` against the banked transcripts. It returned **nothing for the primary carrier** — which, taken at face value, would have supported a false and serious conclusion: that the project's *primary* source never contained the passage at all.

The cause was mundane: the primary transcript is broken into timestamp blocks, so a fixed-width context window spanning line breaks cannot match. Flattening whitespace first returned the passage immediately.

**Rule recorded:** **a null from a text search is a claim about the search, not about the corpus, until the search method has been validated against a known positive.** This project already treats "no evidence found" as requiring a stated search scope; that discipline must extend to the mechanics of the search itself. A false negative here would have been *more* damaging than the false positives the discipline usually guards against.

## 5. CORRECTIONS APPLIED

| File | Change |
|---|---|
| **BOC-ROUTE-2026-07-27** → v1.1 | Headline figure corrected from "41 case-relevant" to **35 case-relevant, 6 concerning other events**; "third instance" language corrected to **two content migrations + one title-rendering hazard**; **Ep 320 added** to the §6.3 priority list |
| **BOC-E07** → v1.5 | Standing-rule paragraph corrected to distinguish the two phenomena; the operational rule retained unchanged |
| **BOC-E08** → v1.2 | V-12 note: the director's name is **unresolved between carriers** (Petria/Patria), not settled as "Petria" |

## 6. RESIDUAL — WHAT THIS PASS DID NOT DO

1. **Self-audit.** Same analyst produced and checked the work.
2. **It did not re-verify the 2026-07-20 Phase 0 findings** that today's files build on — the 83/83 adversarial set is inherited, not re-tested.
3. **It did not test the corpus routing episode-by-episode** beyond the sample in §2.2; other misroutings may exist among the 54.
4. **No episode was heard.** Every BOC claim about Eps 309–365 still rests on titles and published descriptions.
5. **D-42, D-25, D-40/D-41 and the rest of the open register** were untouched — this pass covers only what 2026-07-27 produced.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-27 | Initial file. The adversarial pass on the BOC side, declared owed at CR-AUDIT-2026-07-27 §5.4. **No resolution reversed.** **D-45 CONFIRMED on a test not previously run:** both independent ASR carriers render "the CIA director James Woolsey" identically, with **no "former" or other qualifier anywhere near the phrase** — closing the one path by which the discrepancy could have dissolved. **Two defects, both overstatements in headline positions:** (a) "41 of 54 case-relevant" is a keyword-regex count that fires on the Butler rally and WHCD shootings — **corrected to ~35 case-relevant, 6 other-event**, the routing table itself having caught all six; (b) "third confirmed instance of the migration pattern" conflates **content migration (twice: Eps 309–311, 314–317)** with a **title-rendering hazard (once: D-35)** — the operational rule *sweep by channel and date, never by title string* survives intact, the count characterization does not. **Ep 320 promoted** to the inventory priority list for its published claim about "the discontinued FBI forensic technique used on the JFK assassination being used again." **T1's E08 integration verified complete** (19 rows / 19 source items). Incidental: the carriers **diverge on the documentary director's name** (Petria/Patria), which E08 had silently resolved to one. **Methodological rule recorded:** a null from a text search is a claim about the search until the method is validated against a known positive — the first D-45 test produced a false negative from line-structure, and taking it at face value would have supported a false and serious conclusion. |
