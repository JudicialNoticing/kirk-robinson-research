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
