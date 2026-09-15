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
