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
