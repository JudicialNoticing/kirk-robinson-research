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
