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
