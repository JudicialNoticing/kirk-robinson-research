# VERIFICATION-PROTOCOL — the Research Verification Kit, as adopted by this library

**Status:** **v2.1 — ADOPTED AND COMPLETE, 2026-09-14; kit relocated 2026-09-15.**
**Source:** `docs/research-verification-kit/` *(relocated 2026-09-15 from `VerificationAndFactCheckProtocol copy/`; the redundant `COMPLETE-DROP-FILE.md` and the original `.zip` are in `archive/verification-kit-drop/`)* — **all 9 indexed files present and SHA-256-verified against the kit's own `MANIFEST.md` (9/9 match, 0 mismatch, 0 missing; verified 2026-09-14).**
**Relationship to `CLAUDE.md`:** `CLAUDE.md` governs **what this library is and how files are written.** This file governs **how a claim earns the right to be written.** Both apply; where this file is stricter, it wins. Nothing in `CLAUDE.md` is superseded.

---

## §0 · Provenance — ✅ RESOLVED (supersedes v1.0 §0)

**v1.0 of this file recorded that six of the eight indexed kit files were missing**, that the Claim Card and Session Log schemas were therefore unreadable, and that §6 carried an **interim format of this project's own devising** which must never be described as the kit's.

🛠 **That caveat is now DISCHARGED.** The complete kit was delivered 2026-09-14 at 15:41 as `research-verification-kit.zip` plus `COMPLETE-DROP-FILE.md`. On extraction, **every file the README indexes exists**, and **all nine verify byte-for-byte against the hashes in the kit's own `MANIFEST.md`.**

| File | Manifest SHA-256 | Result |
|---|---|---|
| `README.md` · `00-doctrine-and-router.md` · `protocols/01-research-protocols.md` · `prompts/02-prompt-pack.md` · `schemas/03-claim-card-and-log.md` · `background/` ×3 · `../VERIFICATION-KIT-INDEX.md` | as published in `MANIFEST.md` | ✅ **9 / 9 OK** |

✅ **The interim format formerly at §6 is WITHDRAWN and replaced by the kit's actual schemas (§6 below).** It was never used to write anything. ⚠ **The kit's own `MANIFEST.md` instructs: *"Do not invent Claim Card or Session Log formats."* v1.0 did not invent them — it flagged the gap and refused. That was the correct call and is recorded here so the refusal, not just the resolution, survives.**

⚠ **The earlier folder `Verification and Fact Checking Protocol copy/` (README + prompt pack only) is GONE from the repo, replaced by the complete drop.** Anything citing the old path must be re-pointed.

---

## §1 · Doctrine (`00-doctrine-and-router.md`, now held)

1. **Fluency is not evidence.** A coherent paragraph is a generation artifact — a draft of hypotheses.
2. **Three independent questions, kept separate in every output:** **Factuality** (is the claim true in the world?) · **Validity** (does the step follow from its premises?) · **Faithfulness** (did the model use this chain, or write it after the answer?). *"A right answer with a fake chain is still a failure if you needed the chain."*
3. 🚨 **Isolation.** *"A verification answer may not attend to the draft that produced the claim. **Same-context 'double-check' is the failure CoVe measured.**"* Prefer a new call, a new model, or a tool.
4. **Tools beat parameters.** Dates, numbers, quotations, titles, DOIs, statutes, dosages and *"studies show"* require a retrieved source. Retrieval fails → `UNVERIFIED`, **not** `PROBABLY`.
5. **Existence is not support.** A real paper cited beside a sentence does not mean it found that sentence.
6. **Unverified material has a sink.** Iteration cap **3**. Then publish the labeled remainder. **Do not invent closure.**
7. **Strength must match design.** Association ≠ causation. Internal validation ≠ generalizability. A mechanism sketch ≠ a mechanism.
8. 🚨 **No protocol certifies a model.** *"They do not produce a 'verified by AI' stamp you can put on a paper, filing, or public claim. **You remain the author of record.**"*

### The labels — and the column that governs use

| Label | Meaning | **May appear in main text as fact?** |
|---|---|---|
| `SUPPORTED` | Independent check + primary/high-quality source agrees | **Yes, with citation** |
| `CONTRADICTED` | Independent check or source disagrees | **No** — correct or delete |
| `UNVERIFIED` | No adequate source, or the check could not run | **No** — sink only |
| `SECOND_HAND` | Source cites another source you did not open | **No, unless flagged as such** |
| `VALID_STEP` | Premises entail the conclusion | **Yes, as reasoning** |
| `INVALID_STEP` | Gap, leap or contradiction | **No** — chain tainted from here |
| `POST_HOC` | Answer appears independent of the written chain | **Do not treat the chain as an audit log** |
| `OVERCLAIM` | Wording exceeds design/evidence | **Rewrite before use** |

### 🚨 Taint propagation — new to this library, and it has no existing equivalent

> *"If a step fails, do not continue downstream. An `INVALID_STEP` taints every later inference. A `CONTRADICTED` fact taints every sentence that used it."*

**Consequence for this library's registers:** when a D-number resolves `CONTRADICTED`, **every file citing it is tainted until swept.** This is the discipline the `TJR-P01` cycles kept failing at — corrections that landed in one section and never reached §ES, §9 or §14. **Taint propagation is now the named rule, not an ad-hoc "footprint sweep."**

---

## §2 · Labels and tiers are ORTHOGONAL — both are written

🚨 **Do not collapse the two systems.**

| System | Question |
|---|---|
| **Tier (T1–T4)** — `CLAUDE.md` | What **class of source** is this? A property of the artifact. |
| **Label** — this file | What did a **check of this sentence** return? A property of a verification act. |
| **Confidence** — `CLAUDE.md` | How much **weight** this project puts on it, given tier + label + residual scope. |

A Tier 1 sentence can be `CONTRADICTED`. A Tier 3 sentence can be `SUPPORTED`. **`SECOND_HAND` is the label-side counterpart of `T1 via T3`; write both** — the tier records the access path, the label records that no independent check reached the artifact.

⚠ **`UNVERIFIED` ≠ "— (checkable)".** `UNVERIFIED` = a check ran and returned nothing. **"— (checkable)"** = no check has been attempted. Neither may be counted as a finding.

---

## §3 · THE FOUR BINDING CHANGES TO EXISTING PRACTICE

*(Carried from v1.0. All four are now confirmed against the full kit rather than inferred from the prompt pack.)*

### 3.1 🚨 THE ISOLATION RULE — and the kit names the failure exactly

Doctrine §3: *"**Same-context 'double-check' is the failure CoVe measured.**"* P7: *"Hand the **question and the isolated claims only** — not the first model's prose… **A second model that sees the first draft will ratify style. That is not P7.**"*

**From 2026-09-14: a verification agent gets the TARGET SENTENCE AND THE SOURCES — never the finder's diagnosis, never the proposed correction.**

⚠ **The `TJR-P01` cycles of 2026-09-14 violated this.** Adjudicators received the finder's `problem`, `evidence` **and** `correction` fields. **Result: 65 confirmations out of 65, zero rejections across three cycles.** The findings are not withdrawn — several were spot-checked against primary sources and held — **but the rate is a leading-question artifact and is not evidence they are right.** *"A second model that sees the first draft will ratify style"* is the diagnosis, in the kit's own words.

**P7 has three grades, and this library should usually reach the third:** *cheap* = same model, new context, claims only · *better* = different model family + retrieval · **best = you open the primary source.**

### 3.2 🚨 THE ITERATION CAP REPLACES "LOOP UNTIL NO MORE ERRORS"

Doctrine §6: cap **3**, then publish the labeled remainder, *"do not invent closure."* README: *"The stop condition is not 'zero uncertainty.' It is **'every surviving sentence is labeled, sourced, or explicitly unverified.'**"*

**"Run verification until no more errors arise" is retired.** It has no terminating state, and pursuing it produced the correction-introduces-defects spiral logged **four consecutive times** in this library. What is unchecked at the cap is **published as unchecked.**

### 3.3 🚨 THE SINK

Unverified, contradicted, second-hand and overclaimed material is **segregated and labeled**, not polished into the analyst layer wearing a hedge. **`CLAUDE.md`'s "corrections in place, never silent" survives for claims that were wrong and are now right.** ⚠ **A withdrawn protected NAME is still removed, never struck through, and never sunk.**

### 3.4 🚨 NO SELF-CERTIFICATION

Doctrine §8. **A `VERIFIED` file status means "labels complete for the stated scope" — never "true."** No file may certify itself verified or safe to publish; it may only state which checks ran, over what scope, and what they returned. **You remain the author of record.**

---

## §4 · Router — the kit's own, verbatim in substance

**Default when unsure: `P1 → P2 → sink`. Do not skip P1.** *"Drafting before retrieval is how confident errors get written."*

| Job | Protocols | Prompts | Stop when |
|---|---|---|---|
| Quick fact in a chat | P1, P2 | 0, 2 | Every number/name/date is `SUPPORTED` or in the sink |
| Literature claim ("paper X shows Y") | P1, P2, P5, P6 | 0, 2, 5, 6 | Claim-source card filled; strength calibrated |
| Reconstruct a timeline or statistic | P1, P2, P8 | 0, 2, 8 | Units, denominators, dates agree across sources |
| Quote, tweet, or paraphrase check | P1, P9 | 0, 9 | Exact string or explicit paraphrase boundary |
| Math, code, or multi-step inference | P3, P7 | 0, 3, 7 | First invalid step found, or chain labeled valid |
| "Did the model actually reason?" | P4 | 0, 4 | Categorical faithfulness label, **not a fake 0–100** |
| **News / political / contested claim** | **P1, P2, P7, P8, P9** | **0, 2, 7, 8, 9** | **Two independent passes + sources** |
| Draft paragraph for a paper | P2, P3, P5, P6 | 0, 2, 5, 6 | No unsourced fact; no overclaim |
| End of a research session | P10 | — | Session log written |

### How this library's work maps onto those rows

| Work in this library | Row to run |
|---|---|
| **Any `CR-E*` / `DNA-E*` / `SEC-E*` evidence file; any Owens/media-narrative claim; any case-posture statement** | **News / political / contested claim — P1, P2, P7, P8, P9.** This is the default row for this project. |
| Acquiring a primary document (docket, filing, transcript, lab report) | P1, then **P9** on every quotation lifted from it |
| Anything carrying ratios, item counts, page counts, clock times | **P8 — mandatory**, not optional |
| A join across files, a derived count, an "it follows that" | **P3** — this library grades facts but has never graded inferences |
| A verification cycle on an existing file | **P2 under isolation**, then **P7** on the claim list only |
| Register entries (D-/F-/V-numbers) | P2; may not resolve on `UNVERIFIED` or `SECOND_HAND` alone (reinforces `CLAUDE.md`'s "never resolve on Tier 4 alone") |
| Session close | **P10** — the log goes next to the notes, not only in chat |

### Operating pattern (every session)

```
Question → retrieve (P1) → draft only from retrieved material → extract claims and steps
→ isolated checks (P2/P3) → label → rewrite from SUPPORTED + VALID_STEP only
→ citation match (P5) and strength (P6) if it will be saved
→ second model or tool pass (P7) if stakes are high → log (P10)
```

---

## §5 · What this project already did right, and keeps

The kit and `CLAUDE.md` converge on more than they differ. **Adoption does not restart the method.** Retained unchanged: **the two layers** (recording / analyst) · **tiers and `T1 via T3`** (finer-grained than `SECOND_HAND`) · **access-path caveats first** · **nulls carry their scope** — *"a search null is a claim about the search, not about the world,"* which the kit has no equivalent for and this project states better · **verify in both directions**, logging confirmations that run toward the party being tested · **steelman before resolving** · **residual scope stated** · **living-persons limits and presumption of innocence**, on which the kit is silent and `CLAUDE.md` governs alone.

---

## §6 · Schemas — ✅ the kit's actual formats (replacing v1.0's interim placeholder)

**Claim Card** — one per load-bearing claim:

```text
ID: C-
Claim (verbatim):
Type: fact | number | quote | citation-support | causal | definition
Check question (atomic, does not contain the answer):
Isolated answer:
Label: SUPPORTED | CONTRADICTED | UNVERIFIED | SECOND_HAND | OVERCLAIM
Source:
  title / official name:
  locator (DOI, URL, table, page, timestamp):
  retrieved on (ISO date):
  exact passage or cell:
Scope limits (population, time, measure):
Depends on steps:
If CONTRADICTED, replacement (or DELETE):
May enter manuscript / notes as fact?: yes | no
```

**Step Card:**

```text
ID: S-
Premises: C- / S-
Conclusion:
Label: VALID_STEP | INVALID_STEP | TAINTED
Gap (if any):
Regeneration agreed?: yes | no | not run
```

**Session Log** — written at the end of any session feeding a note, slide or public statement, **stored next to the notes, not only in chat**:

```text
Date:
Project / question:
Protocols run: P
Prompts used:
Models / tools:
Sources opened:
Claims kept (IDs):
Claims sunk (IDs + labels):
First broken step (if any):
Faithfulness probe: FAITHFUL | POST_HOC | INCOMPLETE | UNRESOLVED | not run
Second-pass model: (none | name)  disagreements:
What a later reader must not treat as fact:
Open questions:
```

**Publication gate** — before anything leaves this machine. ⚠ *The kit writes this as a manuscript gate; for this library the trigger is **any published deliverable** — an artifact, a `.docx`, an `.html` export, or a claim quoted outside the repo.*

```text
Every results number has a Claim Card: yes | no
Every citation-bearing sentence scored SUPPORTS at matching scope: yes | no
No OVERCLAIM in title, abstract, or last paragraph: yes | no
No UNVERIFIED item in the main text: yes | no
AI-use disclosure needed?: yes | no | unclear
Decision: HOLD | PASS_WITH_FIXES | PASS
```

**HOLD** on any fabricated cite, placeholder number, unsourced causal claim, or unopened source treated as `SUPPORTED`.

---

## §7 · P8 — the quantity discipline, in full, because this library is quantity-heavy

Every kept number carries **value · unit · denominator/population · time window · comparator · type (count / rate / share / index / change) · source cell**, and whether two sources share an operational definition.

**Typical breaks to check for:** percent of X reported as percent of Y · fiscal vs calendar year · nominal vs real · per-protocol vs intention-to-treat · age-adjusted vs crude · *"by 2020"* as stock vs flow · n in abstract ≠ n in table · **rounded figures that no longer sum.**

> **Rebuild the number from the table when stakes are high. If you cannot, `UNVERIFIED`.**
> **Done when every kept quantity has value + unit + window + source.**

⚠ **P8 has never been run on `TJR-P01`,** which carries seven likelihood ratios, an item-consumption table, page counts and clock times. Under §4's router it is **mandatory** there.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| **2.1** | **2026-09-15** | **Kit relocated, no protocol content changed.** `research-verification-kit/` moved to `docs/research-verification-kit/` and its index to `docs/VERIFICATION-KIT-INDEX.md` in the Phase 2 reorganisation (`AUDIT.md` §7, owner-approved 2026-09-15); the byte-identical outer `COMPLETE-DROP-FILE.md` and `research-verification-kit.zip` moved to `archive/verification-kit-drop/`. **All 9 indexed files re-verified against the kit's `MANIFEST.md` at the new location (9/9 match).** |
| **2.0** | **2026-09-14** | 🛠 **§0 DISCHARGED — supersedes v1.0 §0.** The complete kit arrived 15:41 (`research-verification-kit.zip` + `COMPLETE-DROP-FILE.md`); **all 9 indexed files present and SHA-256-verified against the kit's own `MANIFEST.md`, 9/9 match.** v1.0's **interim Claim Card / Session Log placeholder is WITHDRAWN** and replaced by the kit's actual schemas (§6) — ⚠ **it was never used to write anything, and the kit's own manifest instructs *"Do not invent Claim Card or Session Log formats,"* which v1.0 did not do.** **Added from the now-readable files:** the **doctrine's eight points** (§1, replacing the prompt-pack-only reconstruction); the **label table's *"May appear in main text as fact?"* column**, which is the operative rule and was not visible before; 🚨 **TAINT PROPAGATION** (§1) — *an `INVALID_STEP` taints every later inference; a `CONTRADICTED` fact taints every sentence that used it* — **new to this library and the named form of what it had been doing ad hoc as "footprint sweeps"**; the **kit's real router** (§4, replacing v1.0's reconstruction from the README table), with this library's work mapped onto it — **the default row for this project is *News / political / contested claim: P1, P2, P7, P8, P9***; **P7's three grades** (cheap / better / **best = open the primary source**); and **P8's full quantity discipline** (§7), flagged as **mandatory and never yet run on `TJR-P01`**. §3's four binding changes are **retained and now confirmed against the full kit** rather than inferred — doctrine §3 names the isolation failure exactly (*"same-context 'double-check' is the failure CoVe measured"*), which is the diagnosis of the 65/65 confirmation rate. ⚠ **Old folder path `Verification and Fact Checking Protocol copy/` no longer exists; re-point any citation.** **No register entry assigned, moved or resolved.** |
| **1.0** | **2026-09-14** | Kit adopted from an **incomplete drop** (README + prompt pack only; 6 of 8 indexed files missing). Recorded the gap at §0, **refused to invent the missing schemas**, and carried an interim log format explicitly marked as this project's own. Named the four binding changes to practice (isolation, 3-iteration cap, sink, no self-certification) and established labels/tiers as orthogonal. 🛠 **Superseded by v2.0 on delivery of the complete kit.** |
