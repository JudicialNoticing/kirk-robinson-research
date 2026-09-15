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
