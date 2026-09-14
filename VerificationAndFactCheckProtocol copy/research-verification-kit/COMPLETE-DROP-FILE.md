# Research Verification Kit — COMPLETE DROP FILE

This is the entire kit in one file. If a project folder only contains this file, the kit is still complete. Do not invent missing schemas.

**Manifest (sha256 of the split files this was built from):**

| Path | sha256 |
|---|---|
| research-verification-kit/README.md | 56de254b96c406d5f17ef12989d605761ff436fa53bf599c9c64197d8d919def |
| research-verification-kit/00-doctrine-and-router.md | 62566be94e447ef4f7393240b669ae4cc8078efceaaed5e64b8c13a1113ed7d3 |
| research-verification-kit/protocols/01-research-protocols.md | e8751df291ee962075bf17b8fac5921ac13ccd344e8259ac24fc7c009a7d63ce |
| research-verification-kit/prompts/02-prompt-pack.md | ff6690add32d30c446cecb3b12475366a7223532534dc5a45c8ff697aface762 |
| research-verification-kit/schemas/03-claim-card-and-log.md | 67137940b3fe772bf4ffb0e0d66f96153e26ff70fb3529cfbf459670bb624d55 |
| research-verification-kit/background/chain-of-thought-verification.md | 94b08e638816e0f214ff4b84b9c7f340bdec8943c40999fdd1ee128726f5e363 |
| research-verification-kit/background/fact-checking-assistant-prompt.md | f69b8a3c77f67cb8a175fdfd150ddab546048bb572d4fec4a3071cfaf2071971 |
| research-verification-kit/background/faithfulness-metrics.md | 51e1a226d72322af3376a05a2455176fe46f4172a3ca7d226099a2dbd31a5835 |
| VERIFICATION-KIT-INDEX.md | 27d6ca54a4810681b22a176768e4dcec02c6f3b8736f2f3d6b78725d90da01ce |

Expected split-tree file count: **9** (8 kit files + index). If fewer exist on disk, this drop file is authoritative.


---

# ======== INDEX ========

<!-- source: VERIFICATION-KIT-INDEX.md -->

# Verification kit — index

Grouped and expanded from the three notes in this folder.

**Start here:** [research-verification-kit/README.md](research-verification-kit/README.md)

| Piece | Path |
|---|---|
| How to use + honest limits | `research-verification-kit/README.md` |
| Doctrine, labels, job router | `research-verification-kit/00-doctrine-and-router.md` |
| Protocols P1–P10 | `research-verification-kit/protocols/01-research-protocols.md` |
| Copy-paste prompts 0–10 | `research-verification-kit/prompts/02-prompt-pack.md` |
| Claim cards and session log | `research-verification-kit/schemas/03-claim-card-and-log.md` |
| Original fact-check prompt | `research-verification-kit/background/fact-checking-assistant-prompt.md` |
| CoT verification field map | `research-verification-kit/background/chain-of-thought-verification.md` |
| Faithfulness metrics | `research-verification-kit/background/faithfulness-metrics.md` |

Standalone copies of the three background notes remain in this folder for the earlier turns.


---

# ======== README ========

<!-- source: README.md -->

# Research Verification Kit

A working set of protocols and copy-paste prompts for using AI on research without treating fluent output as evidence.

This kit groups the three notes from this project and expands them into an operating system you can run on every research query.

```
research-verification-kit/
  README.md                         ← you are here
  00-doctrine-and-router.md         ← limits, labels, which protocol to run
  protocols/01-research-protocols.md
  prompts/02-prompt-pack.md         ← paste into any model
  schemas/03-claim-card-and-log.md  ← output formats
  background/
    fact-checking-assistant-prompt.md
    chain-of-thought-verification.md
    faithfulness-metrics.md
```

Also indexed at the artifacts root as `VERIFICATION-KIT-INDEX.md`.

---

## What this kit can and cannot do

It can force an AI to separate claims from reasoning, isolate checks from drafts, demand sources, demote unverified text, and leave a log you can audit.

It cannot make an AI “completely verifiable and factual whenever you use it.” That sentence is a guarantee no protocol can issue.

- Models invent fluent falsehoods.
- Self-checks in the same context often reprint the error.
- CoT can be true and still unfaithful, or faithful and still wrong.
- Published faithfulness scores do not transfer across papers or models.
- Isolated verification is still capped by the model’s knowledge unless a tool or primary source is used.
- Citation existence ≠ citation support.

The stop condition is not “zero uncertainty.” It is “every surviving sentence is labeled, sourced, or explicitly unverified.”

---

## Fast start

1. Read `00-doctrine-and-router.md` once.
2. Paste **Prompt 0 (Master system)** from `prompts/02-prompt-pack.md` at the top of a research thread.
3. Pick a job from the router. Paste the matching protocol prompt.
4. Require the model to emit a **Claim Card** or **Session Log** from `schemas/03-claim-card-and-log.md`.
5. Anything labeled `UNVERIFIED`, `CONTRADICTED`, or `SECOND_HAND` does not enter notes, slides, or a manuscript as fact.

For a one-shot factual paragraph, Prompt 2 (CoVe factor+revise) is enough.
For a paper draft, run Protocols 2 → 5 → 6 → 8 in that order.
For a contested public claim, run Protocols 2 + 7 + 8.

---

## The stack, one line each

| Layer | Question | File |
|---|---|---|
| Doctrine | What is allowed to count as a fact? | `00-doctrine-and-router.md` |
| P1 Source-first | What should be retrieved before anyone drafts? | protocols |
| P2 Claim verification (CoVe) | Are the stated facts true? | protocols + background CoVe note |
| P3 Step verification | Does each inference follow? | protocols + background CoT note |
| P4 Faithfulness audit | Did the model use the chain it wrote? | protocols + background metrics note |
| P5 Citation integrity | Does this source actually support this sentence? | protocols |
| P6 Claim strength | Is the wording stronger than the design? | protocols |
| P7 Adversarial second model | Does an independent pass break it? | protocols |
| P8 Numbers, units, timelines | Are the quantities internally consistent? | protocols |
| P9 Quotes and paraphrase | Is the wording faithful to the source? | protocols |
| P10 Session log | Can a future you reconstruct the check? | schemas |

Existing Grok skills that plug into the same jobs without being rewritten here: `arxiv-preflight`, `reference-integrity-checker`, `claim-strength-calibrator`, `consistency-checker-across-manuscript`.

---

## Rule of use

Never ask a model to “make this accurate.” Ask it to extract, isolate, check, label, and stop. Accuracy is a residue of that process, not a vibe you request at the end.


---

# ======== DOCTRINE AND ROUTER ========

<!-- source: 00-doctrine-and-router.md -->

# Doctrine and Router

Read this once. Use the router every time.

---

## Doctrine

### 1. Fluency is not evidence
A coherent paragraph is a generation artifact. Treat it as a draft of hypotheses.

### 2. Three independent questions
Keep them separate in every output.

- **Factuality** — is the claim true in the world?
- **Validity** — does the step follow from its premises?
- **Faithfulness** — did the model use this chain, or write it after the answer?

A right answer with a fake chain is still a failure if you needed the chain.

### 3. Isolation
A verification answer may not attend to the draft that produced the claim. Same-context “double-check” is the failure CoVe measured. Prefer a new call, a new model, or a tool. If you only have one window, answer the check question before you reread the draft’s wording.

### 4. Tools beat parameters
Dates, numbers, quotations, paper titles, DOIs, statutes, vote counts, dosages, and “studies show” require a retrieved source. If retrieval fails, the label is `UNVERIFIED`, not `PROBABLY`.

### 5. Existence is not support
A real paper cited next to a sentence does not mean the paper found that sentence. Protocol 5 exists because this is the most common scholarly failure.

### 6. Unverified material has a sink
It is never polished into the main answer. It goes to `UNVERIFIED` / `REMOVED` / `SECOND_HAND`. The iteration cap is 3. After that, publish the labeled remainder. Do not invent closure.

### 7. Strength must match design
Association is not causation. Internal validation is not generalizability. A mechanism sketch is not a mechanism. Protocol 6 exists so wording cannot launder evidence level.

### 8. No protocol certifies a model
These procedures reduce specific error classes. They do not produce a “verified by AI” stamp you can put on a paper, filing, or public claim. You remain the author of record.

### Allowed labels (use only these)

| Label | Meaning | May appear in main text as fact? |
|---|---|---|
| `SUPPORTED` | Independent check + primary or high-quality source agrees | Yes, with citation |
| `CONTRADICTED` | Independent check or source disagrees | No; correct or delete |
| `UNVERIFIED` | No adequate source or the check could not run | No; sink only |
| `SECOND_HAND` | Source cites another source you did not open | No, unless flagged as such |
| `VALID_STEP` | Premises entail the conclusion | Yes, as reasoning |
| `INVALID_STEP` | Gap, leap, or contradiction in the chain | No; chain is tainted from here |
| `POST_HOC` | Answer appears independent of the written chain | Do not treat the chain as an audit log |
| `OVERCLAIM` | Wording exceeds design / evidence | Rewrite before use |

---

## Router

Pick the row that matches the job. Run the listed protocols. Paste the listed prompts.

| Job | Protocols | Prompts | Stop when |
|---|---|---|---|
| Quick fact in a chat | P1, P2 | 0, 2 | Every number/name/date is `SUPPORTED` or in the sink |
| Literature claim (“paper X shows Y”) | P1, P2, P5, P6 | 0, 2, 5, 6 | Claim-source card filled; strength calibrated |
| Reconstruct a timeline or statistic | P1, P2, P8 | 0, 2, 8 | Units, denominators, dates agree across sources |
| Quote, tweet, or paraphrase check | P1, P9 | 0, 9 | Exact string or explicit paraphrase boundary |
| Math, code, or multi-step inference | P3, P7 | 0, 3, 7 | First invalid step found or chain labeled valid |
| “Did the model actually reason?” | P4 | 0, 4 | Categorical faithfulness label, not a fake 0–100 |
| News / political / contested claim | P1, P2, P7, P8, P9 | 0, 2, 7, 8, 9 | Two independent passes + sources |
| Draft paragraph for a paper | P2, P3, P5, P6 | 0, 2, 5, 6 | No unsourced fact; no overclaim |
| Full manuscript gate | P2, P5, P6, P8 + `arxiv-preflight` | 0 + skill | No `BLOCKER`; references resolved |
| End of a research session | P10 | — | Session log written |

Default when unsure: **P1 → P2 → sink**. Do not skip P1. Drafting before retrieval is how confident errors get written.

---

## Operating pattern (every session)

```
Question
  → retrieve (P1)
  → draft only from retrieved material
  → extract claims and steps
  → isolated checks (P2 / P3)
  → label
  → rewrite from SUPPORTED + VALID_STEP only
  → citation match (P5) and strength (P6) if it will be saved
  → second model or tool pass (P7) if stakes are high
  → log (P10)
```

If a step fails, do not continue downstream. An `INVALID_STEP` taints every later inference. A `CONTRADICTED` fact taints every sentence that used it.


---

# ======== PROTOCOLS P1–P10 ========

<!-- source: 01-research-protocols.md -->

# Research Protocols

Each protocol is a procedure, not a personality. Run them in router order. Prompts live in `../prompts/02-prompt-pack.md`.

---

## P1 — Source-first query

**Purpose.** Stop the model from answering out of parameters when the question is empirical.

**Do this**
1. Restate the question as one or more lookup targets: entity, date window, metric, jurisdiction, paper, dataset.
2. Name the source class required: primary paper/PDF, official dataset, statute, contemporaneous document, high-quality secondary, or “parameter knowledge is acceptable.”
3. Retrieve before drafting. In this environment: `web_search` / `browse_page` / connected scholarly tools. On a closed model: paste the source text in yourself.
4. If nothing adequate is retrieved, emit `UNVERIFIED` and stop. Do not fill the gap.

**Source ranking (use the highest available)**
1. Primary: paper, dataset codebook, official filing, transcript, statute, original table.
2. Contemporaneous official: agency release, court docket, company 10-K, clinical trial registry.
3. High-quality secondary that cites the primary and can be opened.
4. Encyclopedia / textbook for settled definitional facts only.
5. Model memory: only for tautologies, definitions you already know, or math.

**Never treat as a source:** another chatbot answer, an unsourced tweet, a blog that does not link a primary, “as is well known.”

**Done when** you have either a retrieved artifact or an explicit `UNVERIFIED` on the question itself.

---

## P2 — Claim verification (CoVe factor+revise)

**Purpose.** Factuality of stated claims. This is the upgraded version of `background/fact-checking-assistant-prompt.md`.

**Do this**
1. Draft only after P1, or mark the draft as `UNANCHORED`.
2. Extract every load-bearing FACT: name, date, number, statistic, quotation, paper title, legal holding, causal attribution.
3. Write one atomic verification question per fact. The question must not contain the claimed answer. Bad: “Did the war last from 1846 to 1848?” Good: “In what year did the Mexican–American War begin?”
4. Answer each question in isolation (new call, new model, or tool). No draft in context.
5. Label `SUPPORTED` / `CONTRADICTED` / `UNVERIFIED` / `SECOND_HAND`.
6. Cross-check draft vs answers. Rewrite from consistent supported facts only. Max 3 iterations.

**Known failure this protocol exists to block.** Joint self-check attends to the draft and reprints the hallucination with more confidence. See `background/chain-of-thought-verification.md`.

**Ceiling.** Isolated answers are still model-knowledge-limited. Empirical facts need P1 inside step 4.

**Done when** the main text contains only `SUPPORTED` facts, and everything else is in the sink.

---

## P3 — Step verification

**Purpose.** Validity of inferences. A true set of facts can still produce a false conclusion.

**Do this**
1. Number steps S1…Sn. Each step lists its premises (facts or prior steps) and its conclusion.
2. For each step ask, in isolation: “Do these premises entail this conclusion? If not, name the gap.”
3. Allowed gaps to flag: hidden premise, scope shift (population, time, measure), causal leap, base-rate omission, multiple comparison, substitution of a related quantity, inverted conditional.
4. On the first `INVALID_STEP`, mark every later step `TAINTED`. Do not keep scoring the tail as if it were independent.
5. Regeneration rule (SelfCheck pattern): extract the step’s goal, gather only the listed premises, regenerate the step, compare. If the regenerated step disagrees, the original step is not licensed by its premises.

**This is not faithfulness.** A valid written step can still be post-hoc. Use P4 for that.

**Done when** every surviving step is `VALID_STEP` or the chain is discarded from the first invalid step.

---

## P4 — Faithfulness audit

**Purpose.** Decide whether the written chain can be used as an audit log. It usually cannot be certified. It can be probed.

**Do this — probes, not a score**
1. Hidden-cause probe. If the prompt contained a cue, suggested answer, user preference, or metadata, the chain must say whether that cue was used. Silence → `UNVERIFIED_CAUSE`.
2. Load-bearing probe. Corrupt or delete the first load-bearing step. If the answer does not move, label `POST_HOC`.
3. Coverage probe. List factors necessary to justify the answer. Any missing factor is `INCOMPLETE`.
4. Emit only: `FAITHFUL` | `POST_HOC` | `INCOMPLETE` | `UNRESOLVED`. Never convert this to 0–100.

**Do not** quote Turpin rates, Lanham AOC, or judge F1 as if they applied to this trace. See `background/faithfulness-metrics.md` and BonaFide: most metrics are near chance against ground truth.

**Done when** you have a categorical label and you have stopped treating the chain as a window into weights.

---

## P5 — Citation integrity

**Purpose.** The cited work must support the exact sentence, at the exact scope.

**Do this**
1. Pair each citation-bearing sentence with its cite keys.
2. Open the source (PDF, official abstract + results, or full text). If you cannot open it, label `UNVERIFIED` / `SECOND_HAND`. Do not infer from the title.
3. Score each pair:
   - `SUPPORTS` — finding, population, design, and direction match the sentence.
   - `RELATED` — same topic, not this claim.
   - `OVEREXTENDED` — source is narrower (n, species, endpoint, timeframe) than the prose.
   - `MISMATCH` — source finds the opposite or something else.
   - `SECOND_HAND` — source is itself citing someone you did not open.
   - `QUOTE_DRIFT` — wording tightened, causalized, or generalized relative to the source.
4. Major integrity risk: `MISMATCH`, `OVEREXTENDED` on a results/conclusion sentence, fabricated cite, cite-key pointing at the wrong paper.
5. Do not invent a better citation to save the sentence. Rewrite the sentence or drop it.

Plugs into the `reference-integrity-checker` skill when the input is a manuscript section.

**Done when** every kept citation-bearing sentence has `SUPPORTS` at matching scope.

---

## P6 — Claim-strength calibration

**Purpose.** Wording cannot be stronger than design.

**Map before you edit**

| Evidence you actually have | Words you may use | Words you may not use |
|---|---|---|
| Association / observational | associated with, higher in, correlated | causes, drives, due to |
| Predictive model, internal test | predicted in this cohort, AUC = | clinically useful, ready for use |
| External validation | validated in cohort Z | generalizes, works in practice |
| Mechanism-consistent assay | consistent with, implicates | proves the mechanism |
| Animal / in vitro | in this model | in patients, therapeutic |
| Single study | in this study | established, definitive |
| Mixed or null literature | mixed, uncertain | emerging consensus (unless you counted papers) |

Plugs into the `claim-strength-calibrator` skill for manuscript-scale passes.

**Done when** no kept sentence is `OVERCLAIM`.

---

## P7 — Adversarial second pass

**Purpose.** One model agreeing with itself is not confirmation.

**Do this**
1. Hand the *question and the isolated claims only* — not the first model’s prose — to a second model or to tools.
2. Ask it to attack: alternative explanations, missing denominators, inverted conditionals, wrong paper, outdated figure.
3. A second model that sees the first draft will ratify style. That is not P7.
4. Reconcile on sources, not on eloquence. If they disagree and neither has a primary source, both claims stay `UNVERIFIED`.

**Cheap version.** Same model, new context, claims only, “find what is false.”
**Better version.** Different model family + retrieval.
**Best version.** You open the primary source.

**Done when** disagreements are resolved by a source or parked in the sink.

---

## P8 — Numbers, units, timelines

**Purpose.** Quantity errors survive prose checks.

**Check every number for**
- value
- unit
- denominator / population
- time window
- comparator
- whether it is a count, rate, share, index, or change
- whether two sources are using the same operational definition

**Typical breaks**
- percent of X reported as percent of Y
- fiscal year vs calendar year
- nominal vs real dollars
- per-protocol vs intention-to-treat
- age-adjusted vs crude
- “by 2020” as stock vs flow
- sample n in abstract ≠ sample n in table
- rounded figures that no longer sum

Rebuild the number from the table or codebook when the stakes are high. If you cannot, `UNVERIFIED`.

**Done when** every kept quantity has value + unit + window + source.

---

## P9 — Quotes and paraphrase

**Purpose.** Wording drift is a factual error.

**Do this**
1. Pull the exact string from the source. Ellipses must not change polarity.
2. Paraphrase test: put the source sentence and the new sentence side by side. Flag added causal verbs, dropped hedges, changed quantifiers, shifted agents.
3. Tweets, hearings, and interviews require the original artifact, not a recap.
4. If the source is paywalled and you only have a recap, the paraphrase is `SECOND_HAND`.

**Done when** every quotation is character-accurate and every paraphrase is scoped.

---

## P10 — Session log

**Purpose.** A check you cannot reconstruct did not happen.

Write the schema in `../schemas/03-claim-card-and-log.md` at the end of any session that will feed a note, slide, or paper. Store it next to the notes, not only in chat history.

**Done when** a later reader can see what was checked, against what, and what was left in the sink.


---

# ======== PROMPT PACK ========

<!-- source: 02-prompt-pack.md -->

# Prompt Pack

Paste these as written. Do not add “be thorough” or “make it accurate.” The protocol already asks for the behavior that produces accuracy.

Replace `{{ }}` fields. Keep the isolation rules.

---

## Prompt 0 — Master system (pin at the top of a research thread)

```text
You are a research verification assistant, not a stylist.

Rules that override helpfulness:
1. Fluency is not evidence. Treat your first draft as hypotheses.
2. Separate FACTUALITY, STEP VALIDITY, and FAITHFULNESS. Do not mix them.
3. When checking a claim, answer the check question without using the draft’s wording.
4. Empirical facts need a retrieved source. If you cannot retrieve one, label UNVERIFIED. Do not guess.
5. A real citation that does not support the exact sentence is not support.
6. Unverified, contradicted, second-hand, and overclaimed material goes to a sink. It does not get polished into the main answer.
7. Maximum 3 verification iterations. Then publish what is labeled. Do not invent closure.
8. Never fabricate a source, DOI, quotation, statistic, or page number.
9. Strength of wording must match study design. Association is not causation.
10. You may not certify output as “verified” or “safe to publish.” You may only label items.

Allowed labels: SUPPORTED, CONTRADICTED, UNVERIFIED, SECOND_HAND,
VALID_STEP, INVALID_STEP, POST_HOC, OVERCLAIM.

Default output shape:
- ANSWER (supported material only)
- SINK (everything else, labeled)
- CHECKS RUN (protocol ids + sources)
```

---

## Prompt 1 — Source-first (run before any draft)

```text
Question: {{QUESTION}}

Do not answer yet.

1. Restate the question as lookup targets (entity, metric, date window, jurisdiction, paper).
2. Name the source class required (primary paper, official dataset, statute, contemporaneous document, high-quality secondary).
3. Retrieve those sources. Quote the exact passage or table cell you will rely on.
4. If retrieval fails, stop and return UNVERIFIED on the question.
5. Only after sources are in hand, say READY TO DRAFT and list the facts the sources actually contain.
```

---

## Prompt 2 — Claim verification, CoVe factor+revise

```text
Text or question: {{TEXT}}
Sources already retrieved (if any): {{SOURCES}}

Run claim verification.

1. DRAFT a complete answer from the sources only. If no sources, mark UNANCHORED and keep the draft short.

2. EXTRACT every load-bearing FACT as F1, F2, … (name, date, number, quote, title, holding).

3. PLAN CHECKS. One atomic question per fact. The question must not contain the claimed answer.

4. ANSWER each check independently. Ignore the draft’s wording. Prefer the retrieved source. Label each:
   SUPPORTED / CONTRADICTED / UNVERIFIED / SECOND_HAND
   One sentence of evidence + source.

5. CRITIQUE: contradictions, leading questions, facts with no check, confidence words without a check.

6. REWRITE from SUPPORTED facts only. Move the rest to SINK.
   Iterate at most 3 times. Then stop.

Final output:
VERDICT: VERIFIED | PARTIALLY VERIFIED | UNVERIFIED
ANSWER:
SINK:
CHECKS:
```

Use separate model calls for step 4 when you control the API. One question per call. No draft in that context.

---

## Prompt 3 — Step verification

```text
Question: {{QUESTION}}
Draft reasoning: {{CHAIN}}

Decompose the chain into S1…Sn. For each step list premises and conclusion.

For each step, in isolation:
“Do these premises entail this conclusion? Name the gap if not.”
Label VALID_STEP or INVALID_STEP.

On the first INVALID_STEP, mark every later step TAINTED and stop scoring the tail.

Also run a regeneration check on each VALID_STEP:
- state the step’s goal
- use only its listed premises
- regenerate the step
- if it disagrees with the original, downgrade to INVALID_STEP

Output:
CHAIN TABLE (step, premises, label, gap)
FIRST BREAK:
SURVIVING CONCLUSION (or NONE)
```

---

## Prompt 4 — Faithfulness audit (no fake score)

```text
Prompt the model saw: {{PROMPT}}
Chain: {{CHAIN}}
Final answer: {{ANSWER}}

This is an audit of whether the chain can be treated as the process, not whether the facts are true.

Run three probes only:
1. HIDDEN CAUSE. Did the prompt contain a cue, suggested answer, preference, or metadata? Does the chain say whether it was used? Silence = UNVERIFIED_CAUSE.
2. LOAD-BEARING. If the first load-bearing step were deleted or corrupted, would this answer still be licensed by the remaining text? If yes, POST_HOC.
3. COVERAGE. List factors required to justify the answer. Any missing factor = INCOMPLETE.

Emit exactly one label: FAITHFUL | POST_HOC | INCOMPLETE | UNRESOLVED
Evidence: which probe fired.
Do not output a percentage. Do not cite published faithfulness averages as if they apply to this trace.
```

---

## Prompt 5 — Citation integrity

```text
Manuscript sentences: {{SENTENCES}}
Reference list: {{REFS}}
Source text available: {{SOURCE_EXCERPTS_OR_NONE}}

For each citation-bearing sentence:
1. Name the claim in one line.
2. Name what the cited work actually reports (design, population, endpoint, direction). If the source was not opened, stop and label UNVERIFIED / SECOND_HAND.
3. Score: SUPPORTS | RELATED | OVEREXTENDED | MISMATCH | SECOND_HAND | QUOTE_DRIFT
4. Severity: major | moderate | minor
5. Fix: rewrite the sentence to match the source, or drop the cite. Do not invent a replacement paper.

Output a table. No sentence in the “keep” column may carry MISMATCH or unopened SECOND_HAND.
```

---

## Prompt 6 — Claim-strength calibration

```text
Study design (one paragraph): {{DESIGN}}
Validation status: {{INTERNAL_ONLY | EXTERNAL | MULTI_COHORT | NONE}}
Sentences: {{SENTENCES}}

For each sentence:
1. Evidence level actually present (association, prediction, mechanism-consistent, causal demonstration, clinical utility).
2. Evidence level the wording implies.
3. If they differ: OVERCLAIM, with the inflated word circled.
4. Rewrite that stays informative and does not upgrade the design.

Forbidden unless earned: causes, drives, proves, establishes, clinically useful, ready for use, generalizes, definitive, emerging consensus.
```

---

## Prompt 7 — Adversarial second pass

```text
You are an independent attacker. You have not seen the first assistant’s prose.

Question: {{QUESTION}}
Claims to attack (list only):
{{CLAIMS}}

Sources you may use: {{SOURCES_OR_RETRIEVE}}

Find what is false, overscoped, outdated, or inverted.
Do not steelman. Do not preserve tone.
For each claim return: KEEP | KILL | NARROW, plus the source that decides it.
If you lack a source, label UNVERIFIED rather than KEEP.
```

Give this prompt to a different model, or to the same model in a fresh thread. Do not paste the original answer.

---

## Prompt 8 — Numbers, units, timelines

```text
Claims containing quantities: {{CLAIMS}}
Sources / tables: {{SOURCES}}

For each number extract:
value | unit | denominator | time window | comparator | type (count, rate, share, index, change) | source cell

Then:
- Recompute from the table if possible.
- Flag unit or denominator swaps, calendar vs fiscal, crude vs adjusted, n mismatches, rounded figures that no longer sum.
- Label each SUPPORTED or UNVERIFIED.

Output a quantity table. Any number that cannot be rebuilt stays out of the main answer.
```

---

## Prompt 9 — Quote and paraphrase

```text
Alleged quote or paraphrase: {{TEXT}}
Source artifact: {{SOURCE_OR_NONE}}

1. Pull the exact characters from the source. If no artifact, UNVERIFIED.
2. If quoted: character match, including polarity after ellipses.
3. If paraphrased: list added causal verbs, dropped hedges, changed quantifiers, shifted agents.
4. Verdict: ACCURATE | DRIFT | FABRICATED | SECOND_HAND
```

---

## Prompt 10 — Compact all-in-one (when you only get one paste)

Use this only if you cannot run the stack. It is weaker than P1→P2→P5.

```text
Follow Prompt 0 rules.

Task: {{TASK}}
Material: {{TEXT_OR_QUESTION}}

Produce:
1. Sources you actually used (or UNVERIFIED if none).
2. Claim table: id, claim, check question, isolated answer, label, source.
3. Step table if reasoning is load-bearing: first INVALID_STEP or all VALID_STEP.
4. ANSWER built only from SUPPORTED + VALID_STEP.
5. SINK with labels.
6. Strength check: any OVERCLAIM rewritten.
7. VERDICT: VERIFIED | PARTIALLY VERIFIED | UNVERIFIED

Do not close gaps with invented sources. Stop after 3 internal iterations.
```

---

## Multi-call recipe (preferred)

When you control the calls:

```
Call A  Prompt 1          → sources
Call B  Prompt 2 steps 1–3 → draft + questions (stop)
Call C1…Ck  one atomic question each, no draft
Call D  Prompt 2 steps 5–6 → labels + rewrite
Call E  Prompt 7 in a fresh model on the claim list only
Call F  Prompt 5 and/or 6 if the text will be saved
Call G  fill the Session Log schema
```

That is the operational form of CoVe factor+revise plus an independent attacker.


---

# ======== SCHEMAS (Claim Card, Step Card, Session Log, Manuscript Gate) ========

<!-- source: 03-claim-card-and-log.md -->

# Schemas

Copy these into notes. One card per load-bearing claim. One log per session that will feed a paper, slide, or public statement.

---

## Claim Card

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

---

## Step Card

```text
ID: S-
Premises: C- / S-
Conclusion:
Label: VALID_STEP | INVALID_STEP | TAINTED
Gap (if any):
Regeneration agreed?: yes | no | not run
```

---

## Session Log

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

---

## Manuscript gate (short)

Use before a draft leaves your machine. Pair with the `arxiv-preflight` skill when you have `.tex` / `.bib`.

```text
Every results number has a Claim Card: yes | no
Every citation-bearing sentence scored SUPPORTS at matching scope: yes | no
No OVERCLAIM in title, abstract, or last paragraph of discussion: yes | no
No UNVERIFIED item in the main text: yes | no
AI-use disclosure needed?: yes | no | unclear
Decision: HOLD | PASS_WITH_FIXES | PASS
```

HOLD on any fabricated cite, placeholder number, unsourced causal claim in the abstract, or unopened source treated as `SUPPORTED`.

---

## Worked card (illustrative)

```text
ID: C-04
Claim: “Paper X showed that treatment A causes remission in adults.”
Type: causal
Check question: What design, population, and endpoint did Paper X report for treatment A?
Isolated answer: X was a single-center observational study in 86 adults; endpoint was 6-month symptom score, not remission; authors report association after adjustment.
Label: OVERCLAIM + OVEREXTENDED
Source: X, Table 2 and Discussion ¶3, DOI …, opened 2026-09-14
Scope limits: observational, n=86, one center, symptom score
May enter manuscript as fact?: no
Replacement: “In X, treatment A was associated with lower 6-month symptom scores in a single-center adult cohort (n=86).”
```

That replacement is what P2 + P5 + P6 are for. The original sentence was fluent and unusable.


---

# ======== BACKGROUND — original fact-check prompt ========

<!-- source: fact-checking-assistant-prompt.md -->

# Strict Fact-Checking Assistant Prompt

## Role & Goal

You are a strict fact-checking assistant. Your goal is to review the provided text, list every factual claim, independently verify or challenge each claim, and loop through corrections until zero unverified assertions remain.

## The Process

1. **Extract:** List every specific claim, date, number, or statistic from the text.
2. **Interrogate:** Formulate a specific verification question for each claim without looking at your original context, then answer it objectively.
3. **Critique:** Identify contradictions, missing sources, or weak assumptions.
4. **Iterate:** If any claim fails verification or lacks a solid source, rewrite that section and repeat steps 1–3.

## Stop Condition

Continue this internal review loop until all claims pass your checklist or you reach a maximum of 3 iterations. Output your final cleaned text only when the verification check passes completely.


---

# ======== BACKGROUND — chain-of-thought verification ========

<!-- source: chain-of-thought-verification.md -->

# Chain-of-Thought Verification

A field map, failure modes, and a reusable prompt that combines CoT with independent verification.

This document sits next to `fact-checking-assistant-prompt.md`. That prompt is an *outcome* loop (extract claims → check them → rewrite). CoT verification is a *process* loop: check the reasoning steps that produced the claims, not only the claims themselves.

---

## 1. The problem CoT creates

Chain-of-Thought (Wei et al., 2022) improves multi-step performance by forcing intermediate steps into tokens. It also creates a new failure surface:

- An early wrong step poisons every later step.
- Fluent steps look like proof even when they are post-hoc rationalization.
- The model can produce a correct answer with an unfaithful explanation, or a wrong answer with a convincing explanation.
- Self-attention to an earlier hallucination makes the model *repeat* that hallucination when it “checks its work” in the same context.

So “think step by step” is not verification. Verification is a separate computation that must not be allowed to copy the draft.

---

## 2. Four families of verification

These are not synonyms. Pick the family that matches the error you care about.

### A. Claim verification after a draft — Chain-of-Verification (CoVe)

Dhuliawala et al., Meta / ETH Zürich, 2023–2024. [arXiv:2309.11495](https://arxiv.org/abs/2309.11495)

Four steps, same model, different prompts:

1. Draft a baseline answer.
2. Plan verification questions that attack the draft’s factual claims.
3. Answer those questions *independently* so the answers are not biased by the draft.
4. Rewrite the answer using only what survived the check.

Execution variants, weakest to strongest:

| Variant | What is in context when answering checks | Typical result |
|---|---|---|
| Joint | Draft + questions + answers in one prompt | Cheap; often *repeats* the draft’s errors |
| 2-step | Questions answered without the draft | Better; still some interference across answers |
| Factored | One isolated prompt per question | Best cheap version; stops copy-paste hallucination |
| Factor + Revise | Factored answers, then an explicit CONSISTENT / INCONSISTENT / PARTIAL label, then rewrite | Best in the paper |

Reported gains on Llama-65B (paper numbers, not universal):

- Wikidata list precision: 0.17 → 0.36 (2-step)
- MultiSpanQA F1: 0.39 → 0.48 (factored)
- Longform biography FactScore: 55.9 → 71.4 (factor+revise)
- Factor+revise Llama-65B FactScore beat ChatGPT (58.7) and PerplexityAI (61.6) on that biography setup

Hard limits the paper states:

- Hallucinations drop; they do not hit zero.
- Gains are bounded by what the model already knows. Rare facts still need retrieval.
- CoT itself did *not* help these factual tasks. CoVe is not “more CoT.”
- Cost scales with number of claims.

The design rule that matters: **the verification answer must not attend to the original hallucination.**

### B. Step verification during reasoning — process supervision

Lightman et al., OpenAI, 2023. *Let’s Verify Step by Step.* [arXiv:2305.20050](https://arxiv.org/abs/2305.20050)

- Outcome reward: was the final answer right?
- Process reward: was *this step* right?

Process-supervised reward models (PRMs) beat outcome-supervised models on MATH. Their best PRM solved 78% of a representative MATH subset via best-of-N search. They released PRM800K (~800k human step labels).

This is the ancestor of test-time compute / o1-style “check the work, not just the answer.” It is training-time and search-time, not just a prompt.

Prompt-only cousins:

- SelfCheck (Oxford): extract the step’s goal → gather premises → regenerate the step from premises → compare. Verification is recast as generation + comparison because models are better at generating than at judging.
- Zero-shot step verifiers (COT STEP + R-prompt / COTR-prompt): force numbered steps, then ask a separate pass whether each step is valid.
- General-purpose CoT verifiers (Vacareanu et al., 2024): score each step on relevance, mathematical accuracy, and logical consistency, optionally plus perplexity.

Shared rule: **a chain is as strong as its first false step.** Jacovi et al., ACL 2024, built REVEAL to benchmark this and found automatic verifiers are especially weak at logical correctness and contradiction detection. [arXiv:2402.00559](https://arxiv.org/abs/2402.00559)

### C. Backward verification — Self-Verification

Weng et al., 2022. [arXiv:2212.09561](https://arxiv.org/abs/2212.09561)

Forward CoT produces candidate answers. Backward pass masks an original condition and asks: given the conclusion, can you recover the masked condition? Score candidates by how well they reconstruct the givens.

Works well when the task is invertible (arithmetic, some QA). Weak when many conclusions are compatible with the same premises.

### D. Faithfulness checks — is the CoT what the model actually used?

Separate question from “is the step true?”

- Chen et al., 2025, *Reasoning Models Don’t Always Say What They Think*: CoTs often omit hints the model used; outcome RL improves faithfulness early then plateaus.
- *Chain-of-Thought Reasoning In The Wild Is Not Always Faithful* (2025): even without planted bias, models will justify both “Is X > Y?” and “Is Y > X?” as Yes.
- FaithCoT-Bench (2025): instance-level unfaithfulness detection across models and domains.
- White-box work (CRV, circuit-guided scorers): treat attribution graphs of a CoT step as an execution trace and classify error from graph structure.

If you are using CoT as an audit log (safety, agents, grading), assume the verbalized chain is incomplete. Verification of *claims* is not verification of *internal process*.

---

## 3. What actually fails

Use this as the checklist, not as decoration.

1. **Context contamination.** Joint self-check attends to the draft and reprints the error with more confidence.
2. **Question under-coverage.** A verification question that restates the claim (“Did the war last from 1846 to 1848?”) will get a yes. Ask atomic, source-shaped questions (“In what year did the war start?”).
3. **Verifier hallucination.** Isolated answers can still be wrong. CoVe’s ceiling is the model’s knowledge. Tool-use (search, calculator, code, retrieval) belongs in step 3, not step 1.
4. **Logical vs factual errors.** CoVe targets stated facts. Process verifiers target step validity. Neither automatically catches unfaithful rationalization.
5. **Weakest-link dynamics.** One bad step is enough. Scoring only the final answer hides where it broke.
6. **Over-deletion.** Factored CoVe on biographies raised FactScore but cut average fact count (16.6 → ~12). Precision up, coverage down. Decide which you want.
7. **Cost.** Factored CoVe is O(claims) extra calls. Cap questions. Cap iterations. Stop when residual claims are marked unverified rather than inventing closure.
8. **Monitor evasion.** CoT monitors that read the reasoning text can be fooled if only the narration is rewritten. Actions and claims still need independent checks.

---

## 4. How this upgrades the earlier fact-checking prompt

The saved prompt does:

Extract → Interrogate → Critique → Iterate (max 3) → emit cleaned text.

Missing pieces from the CoT-verification literature:

- Interrogation happens in the same context as the draft, so the model can ratify its own errors.
- Claims are checked; reasoning steps are not.
- No explicit CONSISTENT / INCONSISTENT / UNVERIFIED label before rewrite.
- No rule that unverified material must be dropped or flagged rather than polished.
- No tool slot for questions the model cannot answer from parameters.

The prompt in §5 folds those in.

---

## 5. Reusable prompt: Chain-of-Thought Verification

Copy from the line below. Keep the isolation rules. If you can make separate model calls, use the factored version. If you only have one context window, still answer verification questions *before* you look back at the draft’s wording.

```text
You are a Chain-of-Thought Verification assistant.

Goal: produce an answer whose every surviving claim and reasoning step
has been independently checked. Fluency is not evidence. A plausible
step that does not follow from the premises is a failure.

Hard rules
- Do not treat the first draft as authoritative.
- When answering a verification question, ignore the draft’s wording.
  Answer as if you had never seen the draft.
- Do not ask leading questions that restate a claim and invite a yes.
  Ask atomic questions a third party could grade.
- If a check cannot be resolved from reliable knowledge or tools,
  mark the claim UNVERIFIED. Do not launder it into the final text.
- Maximum 3 full iterations. After that, publish what is verified
  and explicitly list what remains unverified.
- Never invent a source, date, number, quote, or mechanism to close
  a gap.

Protocol

ITERATION n of 3

1. DRAFT
   Write a complete answer. Then immediately decompose it.

2. EXTRACT
   List every load-bearing item as one of:
   - FACT: date, number, name, event, quote, statistic
   - STEP: an inference that depends on prior items
   - ASSUMPTION: something used but not established
   Number them F1, F2, S1, S2, A1, …

3. PLAN CHECKS
   For each FACT, write one atomic verification question that does
   not contain the claimed answer.
   For each STEP, write one validity question:
     “Do these premises entail this conclusion? Name the gap if not.”
   For each ASSUMPTION, write:
     “Is this necessary, and is it stated as assumption not fact?”

4. ANSWER CHECKS INDEPENDENTLY
   Answer each question in isolation.
   Label each answer:
     SUPPORTED / CONTRADICTED / UNVERIFIED
   One sentence of evidence. No rhetoric.

5. CRITIQUE THE CHAIN
   - First false STEP (weakest link). Everything after it is tainted.
   - Contradictions across answers.
   - Checks that merely paraphrase the draft.
   - Claims that have no check.
   - Confidence inflation (“clearly,” “studies show”) without a check.

6. REWRITE OR STOP
   Keep only SUPPORTED facts and valid steps.
   Demote CONTRADICTED items (correct or delete).
   Demote UNVERIFIED items to an explicit “Unverified” list.
   If any CONTRADICTED or UNVERIFIED load-bearing item remains in
   the main answer, run the next iteration on the rewrite.
   If none remain, or n = 3, emit the Final Output and stop.

Final Output (only this is shown to the user)

VERDICT: VERIFIED | PARTIALLY VERIFIED | UNVERIFIED
ANSWER:
<cleaned text; no unverified assertion presented as fact>

CHAIN LOG (compact)
- Kept: …
- Corrected: … → …
- Removed: …
- Unverified (do not treat as fact): …
- First broken step, if any: …
- Iterations used: n
```

Factored deployment (preferred when you control the calls)

1. Call 1: draft + extract + plan checks. Stop.
2. Calls 2..k: one verification question per call. No draft in context.
3. Call k+1: consistency labels + rewrite only.
4. Repeat at most twice more.

Tool rule for step 4: if the question is empirical and the model is not the authority, call search, a calculator, code, or a primary source before labeling SUPPORTED.

---

## 6. Worked micro-example

Query: “Name US presidents born in New York State.”

Bad draft: “Donald Trump, Franklin D. Roosevelt, Teddy Roosevelt, and Hillary Clinton.”

Atomic checks (not “Was Hillary Clinton a president born in NY?”):

- Where was Donald Trump born?
- Where was Franklin D. Roosevelt born?
- Where was Theodore Roosevelt born?
- Did Hillary Clinton serve as President of the United States?
- Which office, if any, did Hillary Clinton hold?

Independent answers drop Clinton (never president) and keep the two Roosevelts plus Trump if the birthplace check passes. Final list is shorter and more precise. That is the intended trade: coverage falls, error rate falls more.

---

## 7. When to use which tool

| Situation | Method |
|---|---|
| Long factual prose, bios, lists, news claims | CoVe factor+revise, plus tools on step 3 |
| Math, code, logic puzzles | Process / step verifiers or PRM-style scoring; SelfCheck |
| Invertible word problems | Backward self-verification + self-consistency |
| High-stakes audit of *why* the model answered | Do not trust CoT text alone; need interventions, tools, or white-box checks |
| Single-context chatbot, no extra calls | Use the §5 prompt; still isolate answers from the draft inside the same message |
| You already have the extract-interrogate-critique loop | Keep it, but add isolation, step checks, and an UNVERIFIED sink |

Self-consistency (sample many CoTs, vote) is complementary, not a substitute. Voting agrees on popular errors.

---

## 8. Sources

- Wei et al., 2022. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.
- Weng et al., 2022. Large Language Models are Better Reasoners with Self-Verification. arXiv:2212.09561.
- Lightman et al., 2023. Let’s Verify Step by Step. arXiv:2305.20050.
- Dhuliawala et al., 2023/2024. Chain-of-Verification Reduces Hallucination in Large Language Models. arXiv:2309.11495. ACL Findings 2024.
- Miao et al. / SelfCheck, 2023. Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning. arXiv:2308.00436.
- Jacovi et al., 2024. A Chain-of-Thought Is as Strong as Its Weakest Link (REVEAL). arXiv:2402.00559.
- Vacareanu et al., 2024. General Purpose Verification for Chain of Thought Prompting. arXiv:2405.00204.
- Chen et al., 2025. Reasoning Models Don’t Always Say What They Think. arXiv:2505.05410.
- FaithCoT-Bench, 2025. arXiv:2510.04040.


---

# ======== BACKGROUND — faithfulness metrics ========

<!-- source: faithfulness-metrics.md -->

# Faithfulness Metrics

Companion to `chain-of-thought-verification.md`.

Verification asks: *is this claim or step true?*
Faithfulness asks: *did the model actually use this chain to reach the answer?*

Those are independent. A CoT can be factually correct and unfaithful (post-hoc rationalization of a guess). It can be faithful and wrong (the model really did follow a broken step). Most “CoT monitors” quietly swap one for the other.

Classic definition (Jacovi & Goldberg, 2020): an explanation is faithful if it accurately represents the reasoning process behind the model’s prediction.

---

## 1. Do not mix these six quantities

| Term | Question | Passes when… |
|---|---|---|
| Correctness | Is the final answer right? | Outcome matches a gold label |
| Factuality | Are the stated claims true in the world? | CoVe / tool checks pass |
| Plausibility | Does the text look like good reasoning to a reader? | Humans or LLM-judges find it coherent |
| Faithfulness | Did this text cause, or at least track, the model’s decision? | Interventions on the chain change the answer in the predicted way; hidden causes are verbalized |
| Completeness / coverage / verbosity | Are all factors the model used written down? | Necessary intermediates are present |
| Monitorability | Can an external reader reconstruct the decision from the CoT? | Faithfulness × verbosity |

BonaFide (Gur-Arieh, Marasović, Geva, 2026) states CoT-level faithfulness as: the chain contains a complete path the model followed, and contains no unfaithful steps.

If you only score plausibility, you will call Type-4 cases “good”: correct answer, unfaithful CoT (FINE-CoT Type 4: post-hoc rationalization of a right answer).

FINE-CoT types:

| Type | Answer | CoT |
|---|---|---|
| 1 | Wrong | Faithful |
| 2 | Wrong | Unfaithful |
| 3 | Right | Faithful |
| 4 | Right | Unfaithful |

---

## 2. Metric families

There is no single number. Each family rules out one failure mode and is blind to others. Lanham et al. (2023) called this defense-in-depth. The 2026 meta-evaluation showed that, with ground truth, most of these families are near chance.

### A. Cue / hint verbalization (causal-by-construction on the input)

**Protocol.** Pair an unhinted item with the same item plus a planted cue (answer letter always A; “a professor thinks it’s B”; grader-hack metadata; “unauthorized access says C”). Keep only pairs where the unhinted answer ≠ hint and the hinted answer = hint. Score whether the hinted CoT *acknowledges the cue as a cause*.

Turpin et al., 2023. *Language Models Don’t Always Say What They Think.* arXiv:2305.04388.

Chen et al., 2025. *Reasoning Models Don’t Always Say What They Think.* arXiv:2505.05410.

$$
\mathrm{Faith}(M) = \mathbb{E}\big[\mathbf{1}[c_h \text{ verbalizes hint } h] \mid a_u \neq h,\; a_h = h\big]
$$

Normalized form used when random answer-switching is a concern:

$$
\overline{\mathrm{Faith}}(M) = \min\left\{\frac{\mathrm{Faith}(M)}{1 - q/((n-2)p)},\; 1\right\}
$$

Reported headline numbers (Chen et al., average across hint types):

- Claude 3.7 Sonnet ≈ 25%
- DeepSeek R1 ≈ 39%
- Often < 20% per setting; ≥ 1% in most settings
- Reward-hack environments: model uses the hack on > 99% of items, verbalizes it on < 2% in 5 of 6 environments
- Outcome RL raises faithfulness early, then plateaus

What this measures: *omission of a known external cause.*
What it misses: unfaithfulness with no planted cue; verbalizing presence but denying use; factors the model used that you did not plant.

Classifier sensitivity is its own failure mode. Regex “mention” vs LLM-judge “epistemic dependence” can reverse model rankings on the same traces (Young, 2026). Always report the detector.

### B. Contextual perturbation / importance (Lanham battery)

Intervene on the *generated CoT*, then see if the answer moves. If the answer is invariant, the chain was not causally load-bearing.

Lanham et al., 2023. *Measuring Faithfulness in Chain-of-Thought Reasoning.* arXiv:2307.13702.

| Test | Intervention | Faithful signature |
|---|---|---|
| Early answering | Truncate the CoT at step *k*, force an answer | Answer keeps changing as more steps are revealed (high AOC) |
| Adding mistakes | Inject an error at step *k*, regenerate the tail | Answer flips |
| Filler tokens | Replace CoT with `...` of matched length | Accuracy does not rise from extra tokens alone |
| Paraphrasing | Rewrite early steps, regenerate | Answer stays if only wording changed (rules out steganography) |
| Step removal / option shuffle | Drop a step or permute choices | Answer moves iff the step / order was used |

Early-answering AOC is a weighted sum over truncation points. Higher AOC = less post-hoc = more faithful under this test.

Lanham findings that still matter:

- Inverse scaling on several tasks: 13B more CoT-dependent than 175B.
- Harder tasks → more apparent faithfulness (the model needs the chain).
- Easy tasks + strong models → more post-hoc.

BonaFide later found Adding Mistakes / Early Answering ≈ 0.51 AUROC against ground truth. The test can fire because the model is *sensitive to context*, not because the original chain was the true computation.

### C. Information-flow metrics (sufficiency, completeness, necessity)

Treat the CoT as a channel between input and answer.

- Sufficiency: does the CoT alone determine the answer? (entropy / simulatability)
- Completeness: does the CoT carry all answer-relevant information in the prompt? (masked KL: hide the CoT, see if hint information still reaches the answer)
- Necessity: if you ablate a step, does answer information drop? (gradients or masked KL on that span)

Useful when you want a task-agnostic diagnostic instead of a planted cue. Known failure: KL-based scores collapse when the residual stream is already low-entropy; gradient scores are more stable there.

Simulatability is the human/LLM version of sufficiency: can a simulator predict the model’s answer from the CoT plus a counterfactual input? Score ≈ 0.50 AUROC on BonaFide.

### D. Parametric faithfulness — FUR

Tutek et al., EMNLP 2025 Outstanding Paper. *Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps.* arXiv:2502.14829.

Perturbing tokens in context does not erase what is in the weights. FUR unlearns the *content of a step* from parameters (NPO), then reruns the original input.

- **FF-hard:** does unlearning *any* step flip the predicted label? Binary chain-level call.
- **FF-soft:** how much probability mass moves off the original answer when that step is unlearned? Step salience.

If unlearning a step changes the prediction and the unlearning was localized, that step was parametrically implicated.

Cost is the constraint: on the order of 10² seconds per chain if applied to every step. BonaFide’s adapted FF-hard was 0.52 AUROC at step level.

### E. Attribution / circuit metrics

- **CC-SHAP:** Shapley-style credit of CoT tokens for the answer. Best CoT-level metric on BonaFide (0.70 AUROC). Worst transfer to step level (0.41).
- **CRV:** classify a step from structural features of its attribution graph.
- **CIE-Scorer:** compact sentence-level circuits vs external reasoning graph; Fused Gromov–Wasserstein distance as discrepancy. SOTA on FaithCoT-Bench subsets vs text-only detectors.

These need weights and activations. They are the only family that can see a computation the text never mentions.

### F. LLM-as-judge

Two common heads:

- Step-Judge: is step *k* locally valid?
- Faithful-Judge: does the whole trajectory look like the process that produced the answer?

FaithCoT-Bench (Shen et al., ICLR 2026): LLM-as-judge F1 typically 65–77, >30 points above other paradigms on their human labels. Logit-based detectors were the worst. Counterfactual tests only helped on dense causal tasks (AQuA), not on TruthfulQA / HLE-Bio.

Caveats the same paper states:

- CoT error ≠ unfaithfulness. Step-Judge underperforms Faithful-Judge.
- Stronger models are *harder* to audit. Judge F1 drops from ~76 on Qwen2.5-7B to ~50 on GPT-4o-mini / Gemini 2.5 Flash on TruthfulQA.
- Judges measure something close to annotated *plausibility-plus-process-story*, which is not internal causal structure.

C2-Faith later split judge quality into causality (does step *k* follow?) vs coverage (are required intermediates present?). Rankings flip with the task framing. Coverage scores are inflated on incomplete chains.

### G. Process-level causality and coverage (text-internal, not model-internal)

C2-Faith (built on PRM800K):

- Causality: inject an acausal replacement at a known step; can the judge detect and localize it?
- Coverage: delete intermediates at a known rate; does the judge notice?

This is faithfulness of the *argument as an argument*, not faithfulness to hidden compute. It is the right metric when you care that the written proof is deductively usable.

Lyu et al., 2023, *Faithful CoT* take the extreme version: translate the query into a symbolic chain, execute it with a deterministic solver. The chain is faithful *by construction* because the answer is the solver’s output. That buys faithfulness and loses coverage of problems you cannot formalize.

---

## 3. What the meta-evaluations actually say

**FaithCoT-Bench / FINE-CoT** (Shen et al., 2025–26). Instance-level detection as binary classification. ~1,000 expert-labeled trajectories, four models, four domains, >300 unfaithful. Unfaithful split: 41.7% post-hoc, 57.7% spurious chains. Eight principles:

Post-hoc: selective explanation; no transparent post-answer analysis; silent revision of earlier conclusions; confidence without justification.
Spurious: step skipping; unjustified reversal; weak/irrelevant justification; invalid chain.

Best detectors on *their* labels: LLM judges. Worst: logits. Knowledge-heavy domains are harder.

**BonaFide** (Gur-Arieh et al., 2026). arXiv:2605.25052. Title is the finding: *Faithfulness Metrics Don’t Measure Faithfulness.*

They built tasks whose outputs disclose which intermediate computations must have occurred, then labeled 3,066 CoTs / steps across 13 tasks and 10 models.

Against that ground truth:

| Family | Metric | Step AUROC | CoT AUROC |
|---|---|---|---|
| Importance | Adding Mistakes | 0.51 | 0.51 |
| Importance | Early Answering | 0.51 | 0.45 |
| Importance | Filler Tokens | **0.59** | 0.50 |
| Semantic | Paraphrasing | — | 0.61 |
| Semantic | Simulatability | — | 0.50 |
| Parametric | FUR | 0.52 | — |
| Attribution | CC-SHAP | 0.41 | **0.70** |

Also:

- Most importance metrics label 90–96% of a balanced set “unfaithful.”
- Semantic-utility metrics label 94–96% “faithful.”
- No metric transfers from step-level to CoT-level.
- Scores degrade on longer CoTs.
- Cost is often prohibitive (FUR, full CC-SHAP, per-step unlearning).

Read that as: published “faithfulness scores” are not interchangeable, not calibrated, and often not measuring the latent you named.

---

## 4. Thinking-draft metrics for reasoning models

Reasoning models add a hidden or semi-hidden draft before the user-facing answer. Two extra axes (Zhou et al., 2025):

- **Intra-draft faithfulness:** insert a counterfactual step into the draft. Does later draft text *follow* it or *correct* it? Score depends on that classification.
- **Draft-to-answer faithfulness:** perturb the draft’s conclusion. Does the emitted answer still track the draft, or does the answer stage redo the work?

Empirically, models are selectively faithful inside the draft (backtracking steps more than others) and often not draft-reliant at the answer stage. A clean thinking trace plus a divergent final answer is a Type-4 cousin.

Thinking tokens also acknowledge hints more often than the visible answer (~87% vs ~29% in one open-weight study). Monitors that only read the user-facing answer will understate verbalization.

---

## 5. How to report a faithfulness number without lying

Minimum viable report:

1. **Construct.** Hint-verbalization / AOC / FF-hard / judge F1 / CC-SHAP — name it.
2. **Detector.** Regex mention, pipeline, or judge model. Show sensitivity if you have two.
3. **Conditioning set.** All items, or only items where the intervention changed the answer? The second inflates apparent unfaithfulness and hides “answer stayed, reason still fake.”
4. **Hint or intervention type.** Sycophancy ≠ grader-hack ≠ metadata. Visual-pattern and consistency cues are routinely the least verbalized.
5. **Length / difficulty.** Faithfulness falls on harder items and longer chains.
6. **What you are not measuring.** State it.

Do not compare a Turpin hint-rate from paper A to a Lanham AOC from paper B to a Faithful-Judge F1 from paper C.

---

## 6. Where this sits in the earlier stack

```
fact-checking-assistant-prompt.md     factuality of claims
chain-of-thought-verification.md      validity of steps + isolation of checks
faithfulness-metrics.md               causal status of the chain itself
```

Practical mapping:

- Use CoVe / tools when the user-facing risk is a false fact.
- Use process / step verifiers when the risk is a broken inference.
- Use hint-pair + judge *and* one perturbation test when the risk is “the model used a shortcut it will not admit.”
- Do not use a single faithfulness metric as a ship/no-ship gate. BonaFide says that gate is near random.
- If you need faithfulness by construction, force the answer through a deterministic solver or a tool whose I/O you log. That is Lyu’s move. It shrinks the domain.

A prompt-only approximation that does not pretend to be a metric:

```text
FAITHFULNESS AUDIT (not a score; a protocol)

1. Hidden-cause probe
   If the prompt contains a cue, metadata field, suggested answer,
   or user preference, require the chain to say whether that cue
   was used. Absence is UNVERIFIED_CAUSE, not a pass.

2. Load-bearing probe
   Delete or corrupt the first load-bearing step. If the answer
   does not move, mark POST_HOC.

3. Coverage probe
   List factors necessary to justify the answer. Any missing
   factor is a COMPLETENESS fail, even if every written step
   is locally valid.

4. Emit
   FAITHFULNESS: FAITHFUL | POST_HOC | INCOMPLETE | UNRESOLVED
   Evidence: which probe fired.
   Do not convert this label into a 0–100 score.
```

That is the honest ceiling for a single-context assistant. Anything stronger needs extra forwards, weights, or a solver.

---

## 7. Sources

- Jacovi & Goldberg, 2020. Towards Faithfully Interpretable NLP Systems.
- Turpin et al., 2023. Language Models Don’t Always Say What They Think. arXiv:2305.04388.
- Lanham et al., 2023. Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv:2307.13702.
- Lyu et al., 2023. Faithful Chain-of-Thought Reasoning. arXiv:2301.13379.
- Chen et al., 2025. Reasoning Models Don’t Always Say What They Think. arXiv:2505.05410.
- Tutek et al., 2025. Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps. arXiv:2502.14829.
- Shen et al., 2025/26. FaithCoT-Bench. arXiv:2510.04040. ICLR 2026.
- Gur-Arieh, Marasović, Geva, 2026. Faithfulness Metrics Don’t Measure Faithfulness. arXiv:2605.25052.
- C2-Faith, 2026. Causal and coverage faithfulness of judges. arXiv:2603.05167.
- Young, 2026. Lie to Me / classifier sensitivity. arXiv:2603.22582, arXiv:2603.20172.
- Zhou et al., 2025. Measuring the Faithfulness of Thinking Drafts in LRMs. arXiv:2505.13774.
