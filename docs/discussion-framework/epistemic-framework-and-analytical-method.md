# Epistemic Framework and Analytical Method
### A shared protocol for evaluating competing models of a contested event

**Version 1.0 · Prepared for a structured discussion regarding the facts surrounding the killing of Charlie Kirk and the prosecution of Tyler Robinson**

---

## Note on the design of this document

This document contains **no factual claims about the case**. That is deliberate and it is the point.

A method framework is only useful if both parties can accept it *before* knowing where it leads. If a proposed set of rules can only be accepted by someone who already agrees with your conclusion, the rules are smuggling the conclusion. Every rule below is designed to bind both participants symmetrically and to be equally costly to whichever side happens to be wrong.

If your interlocutor objects to a specific rule, that objection is itself informative and worth resolving before any evidence is discussed. It is far cheaper to argue about method in the abstract than to argue about method retroactively, once each side can see which rule is hurting them.

---

## Part 0 — Opening protocol

A suggested sequence for the first portion of the discussion, before any specific evidence is raised.

1. **Agree on the object.** State precisely which question is being adjudicated (see §I.9 on scope discipline). Most disputes about this case are actually several distinct disputes braided together.
2. **Each party states their model.** Fully, in advance, using the Model Specification Sheet (Table A). Including its mechanism, its requirements, and its falsifiers.
3. **Each party states their prior.** Approximate, with the reference class that generates it. This reveals whether the disagreement is prior-driven or evidence-driven.
4. **Each party states their update conditions.** "What would move me, and how far." Pre-commitment before evidence is on the table.
5. **Agree on the tier system and the chain-labeling convention.** (Part II.)
6. **Agree on the correlation and independence rules.** (Part III.)

Only then begin on evidence.

---

# PART I — SHARED PREMISES

These are the propositions to establish at the outset. They are not concessions by either side; they are descriptions of the epistemic situation both parties are actually in.

## I.1 — We are modeling, not adjudicating

Three distinct objects must be kept separate, and conflating them is the source of a large fraction of unproductive argument:

| Object | Definition | Accessibility |
|---|---|---|
| **The world (W)** | What actually happened. Single-valued, fixed, indifferent to our beliefs. | Not directly accessible to either party. |
| **The record (R)** | The subset of W that has been documented, preserved, and released. | Partially accessible; incomplete; non-randomly filtered. |
| **Our credence (C)** | Our graded confidence across competing models, given R. | Fully ours; the only thing we can actually argue about. |

Neither participant has direct access to W. Both are reasoning from R to build C. Therefore:

- A disagreement in C is **not necessarily** a disagreement about W. It can be a disagreement about how R maps onto W — about weighting, about priors, about what silence means.
- Statements should be spoken at the correct layer. "X happened" is a claim about W. "The record supports X" is a claim about R. "I hold X at 70%" is a claim about C. Mixing these makes disagreements unresolvable because the parties are contesting different objects.

**Practical rule:** when a disagreement stalls, identify which layer it lives on before continuing.

## I.2 — The record is structurally incomplete, and the incompleteness is not random

This is the premise most worth establishing explicitly, because both sides tend to treat gaps as supportive of themselves.

Generic mechanisms that shape R in *any* active high-profile prosecution — none of which are specific to this case or indicative of anything unusual:

- **Active prosecution.** Discovery material is exchanged between parties and not published. Protective orders restrict dissemination. Filings may be sealed in whole or part.
- **Adversarial document structure.** Charging documents and probable cause affidavits state the prosecution's best case. They are *argument*, not neutral summary. They are not designed to include exculpatory nuance, and the absence of such nuance in them carries little information.
- **Strategic defense silence.** Pre-trial, a defense has strong incentives not to disclose its theory. Defense silence therefore carries close to zero evidentiary content. It should not be read as either capitulation or concealment.
- **Selective and timed institutional release.** Agencies release material on institutional timelines shaped by investigative integrity, liability exposure, statutory obligation, and public-relations considerations. Timing of release is weak evidence about content.
- **Media selection.** Newsworthiness and probative value are different variables. Highly probative material can be dull and go unreported; low-probative material can be vivid and saturate coverage.
- **Platform selection.** What circulates in social and algorithmic environments is selected for engagement, not accuracy. The volume of a claim online is close to uncorrelated with its truth.

### The resulting rule on silence

> **Absence of evidence is evidence of absence only to the degree that you would expect the evidence to have surfaced by now, conditional on the model being true.**

Formally: the informativeness of a gap is proportional to `P(we would have seen it | model true)`. If a model predicts that a piece of evidence would be non-public at this stage anyway, its non-appearance is ~zero evidence against the model. If a model predicts evidence that should be trivially available and it isn't there, that gap is real evidence.

**This must be applied symmetrically.** Both parties must be willing to say, for any gap they invoke, why they would have expected that item to be public by now.

## I.3 — Neither party has privileged access

Both participants are outside the discovery process. Neither can demand of the other a level of proof that the public record is structurally incapable of supplying.

The move "you can't prove X" is therefore usually not a winning move. The honest response is frequently: *"Correct, and you cannot prove not-X. The question is not proof. The question is which direction the available evidence leans, and by how much."*

## I.4 — Models are specified before evidence is weighed

Evidence cannot be evaluated except relative to specified alternatives. "Is this suspicious?" is not a well-formed question. "Is this more expected under Model A or Model B?" is.

Each model must be written down in advance and must specify:

- **Actors and roles** — who does what
- **Mechanism** — how it operationally works, step by step
- **Necessary conditions** — what must be true for it to hold
- **Predictions** — what we should observe in the record if it is true
- **Falsifiers** — what observation would defeat it
- **Coincidence budget** — what facts it must treat as coincidental

A model that cannot supply falsifiers is not competing with the others. It is insulated from evidence, and insulation is a defect, not a strength. This applies to official accounts and alternative accounts identically: an official narrative that absorbs every contrary datum by adding qualifications is failing the same test.

## I.5 — The question is comparative, not absolute

Possibility is cheap. Almost any model is *possible*. The analytical question is:

> Given the totality of evidence available to us, is that evidence better predicted by Model A or by Model B — and by what margin?

This reframing does substantial work. It eliminates:
- "It could have happened" as an argument (it could; so what)
- "There's no proof" as an argument (rarely is there, either way)
- "Explain this anomaly" as an argument, unless the anomaly is *differentially* expected under one model

## I.6 — Complexity carries a probability cost

For any conjunction, `P(A ∧ B ∧ C) ≤ min(P(A), P(B), P(C))`. Every additional required element multiplies in and can only reduce the total probability.

This produces a well-documented cognitive trap: **detailed, specific narratives feel more plausible while being mathematically less probable.** Vividness and coherence are not evidence.

This tax applies to every model, including simple-sounding official accounts that in fact require many independent conjuncts to all hold. The correct procedure is to enumerate each model's required conjuncts explicitly, rather than assuming the "mainstream" model is automatically parsimonious or that an "alternative" model is automatically baroque.

## I.7 — Priors are declared, not smuggled

Each party should state, approximately and honestly:
- their prior credence in each model before considering case-specific evidence
- the reference class that generates that prior (e.g., "base rates of lone-actor political violence," "base rates of institutional coverup in comparable cases")

This is diagnostic. If two parties agree on every likelihood ratio and still disagree on the conclusion, the disagreement is entirely in the priors and should be argued there instead. A great deal of apparent evidentiary dispute is a proxy war over priors.

## I.8 — Terms of update are agreed in advance

Each party names, before evidence review: *"Here is the class of evidence that would move me, and roughly how far."*

This is the single highest-value ground rule. If neither party can name anything that would move them, the exercise is not truth-seeking, and it is more honest to reclassify it as something else (advocacy, exploration, entertainment) than to conduct it under a false description.

## I.9 — Scope discipline

Four distinct question-types are routinely braided together and must be separated:

| | Question type | Example form |
|---|---|---|
| **(a)** | **Forensic/factual** | Who did what, when, from where, by what means |
| **(b)** | **Institutional performance** | Were investigation, custody, communication, and disclosure competent, consistent, and candid |
| **(c)** | **Motive and ideology** | Why, and what that implies |
| **(d)** | **Political/normative** | What the event means, who benefits, what should follow |

**The critical rule:** a failure in (b) is not evidence for any *specific* alternative in (a).

Incompetence, bureaucratic self-protection, poor communication, and coordinated concealment produce **overlapping surface signatures**. Anomalies, inconsistencies, revisions, and defensiveness are generated abundantly by all of them. Distinguishing between them requires evidence that is *differentially* predicted — not merely the presence of anomaly.

Either party should be able to call a **scope flag** mid-discussion when the categories collapse into each other.

## I.10 — Every claim is time-indexed

Attach to every claim the date of the record supporting it, and the date it was first asserted.

High-profile events with rapid news cycles have a **high baseline revision rate** in early reporting and early official statements. Initial accounts in such events are routinely wrong in detail across cases where no one disputes the overall account. Therefore:

- The mere existence of revision is close to non-informative (see §III.5 on base rates).
- What *can* be informative is a revision pattern that is anomalous relative to that baseline — e.g., revisions moving consistently in one direction, revisions unacknowledged, revisions to elements not plausibly subject to early confusion.

---

# PART II — THE TIER SYSTEM

## II.0 — Two independent axes

The most common error in evidence discussions is treating "reliability" and "importance" as one thing. They are orthogonal:

- **Axis 1 — Provenance tier (T):** how much we can trust that the claim accurately reports what it purports to report.
- **Axis 2 — Probative weight (W):** how much the claim, *if true*, discriminates between the competing models.

A perfectly documented Tier-1 fact that is equally expected under both models moves nothing. A Tier-3 claim that would be astonishing under one model may be worth far more discussion. **Tier tells you whether to believe it. Weight tells you whether it matters.** You need both, and they multiply.

---

## II.1 — Axis 1: Provenance tiers

### T0 — Directly inspectable primary artifact
Raw, unedited material with known chain of custody, inspectable by us directly. Original unaltered recordings, original documents in hand, physical evidence.
*Rare in public discussion. Most material presented as T0 is actually T0-derived and has passed through hands.*

### T1 — Sworn testimony and primary court filings
Probable cause affidavits, charging documents, motions and responses, sworn testimony, certified transcripts, medical examiner reports, admitted exhibits.

Sub-levels:
- **T1a** — full document obtained and read directly
- **T1b** — document partially excerpted within another primary record

> **Important caveat:** T1 does not mean *true*. It means **attributable and accountable** — a named party staked professional and legal exposure on it. Adversarial filings remain *argument*. A probable cause affidavit is the state's assertion of its case, not a neutral finding. Its tier is high; the appropriate reading is "this is what the state asserts and will be held to," not "this is established."

### T2 — Named official statements, unsworn
Press conferences, agency press releases, named official spokespeople, on-record statements by identified officials.

Attributable, but without perjury exposure, frequently preliminary, and often produced under time pressure and institutional messaging constraints. High revision rate in early phases.

### T3 — Named journalistic reporting
Sub-levels by sourcing transparency:
- **T3a** — outlet reports and names its source
- **T3b** — outlet states it reviewed a specific document and characterizes it
- **T3c** — outlet reports from characterized-but-anonymous sources ("two officials familiar with…"), single outlet

### T4 — Low-verification material
Anonymous or uncharacterized sourcing, aggregator content, social media claims, screenshots, clips of unknown provenance, unattributed "analysis," recirculated claims with no identifiable origin.

---

## II.2 — Chain notation (the most important convention here)

**The effective tier of a claim is set by the weakest link in its chain of transmission, not by its origin.**

Notation, extending the convention already in use in this project:

| Notation | Meaning |
|---|---|
| `[T1]` | Primary court document obtained and read directly |
| `[T1 via T3]` | Court-document content known *only* through journalistic characterization. **Effective tier: T3.** |
| `[T2 via T4]` | An official statement known only via social media repost. **Effective tier: T4.** |
| `[T3 via T4]` | Reporting known only through a screenshot or aggregator |
| `[T? ⊘]` | **Citation dead-end.** The chain terminates without a retrievable original. |

The `⊘` marker deserves emphasis. **Citation laundering** is the process by which a claim of unknown origin acquires apparent authority by being cited, re-cited, and eventually attributed to "reports." A claim whose chain cannot be walked back to a retrievable source is not low-tier — it is *unrated*, and should be set aside rather than discounted, because we do not know what we are discounting.

> **The single most common failure in public argument about this case, on all sides, is tier inflation via chain collapse:** saying "court documents show X" when what one actually possesses is an outlet's paraphrase of a document one has never seen. Both parties should agree to police this in themselves and permit the other to call it.

---

## II.3 — Demotion modifiers

Each of these reduces effective tier below the nominal level:

- Media that has been re-encoded, cropped, edited, trimmed, or re-uploaded
- Translation presented without the original-language source
- Transcription presented without the underlying audio
- Paraphrase presented with quotation marks
- Aggregation (an outlet summarizing another outlet's reporting as if independent)
- Sources that have been retracted, corrected, or silently edited post-publication
- Sources maintaining no public corrections ledger
- Claims originating inside a monetized-attention or advocacy pipeline

On that last point, a necessary caution: originating inside an advocacy pipeline **adjusts the prior on accuracy; it does not establish falsity.** Dismissing a claim solely by its origin is a genetic fallacy and is itself a tier violation. The correct handling is: lower prior, then evaluate the chain on its merits. A checkable claim from a low-credibility source is still checkable, and should be checked rather than waved off.

## II.4 — Promotion modifiers

Each of these raises effective confidence above the nominal tier:

- **Causally independent corroboration** — a second source with a genuinely different error mode (see §III.2; most apparent corroboration fails this test)
- **Contemporaneity** — documentation created before the matter became contested, when no one had reason to shade it
- **Statement against interest** — a party asserting something contrary to their own position
- **Adversarial authentication** — a document tested in a proceeding where an opposing party had both motive and opportunity to challenge it and did not, or challenged it and failed
- **Material constraint** — claims resting on geometry, physics, timing, chemistry, or arithmetic. These do not depend on anyone's honesty and are therefore the most robust category available.

## II.5 — Rules of use

1. **No Tier-4 claim may be load-bearing.** T4 material may generate hypotheses and direct inquiry. It may not carry a conclusion.
2. **A conclusion inherits the tier of its weakest necessary link.** A chain of reasoning is only as strong as its worst step, regardless of how strong the other steps are.
3. **Corroboration counts only if causally independent.** See Part III.
4. **Tiers attach to claims, not to outlets.** There is no such thing as a reliable source, only a specific claim with a specific chain. A generally careful outlet can publish an unsourced claim; a generally unreliable one can publish a verifiable document.
5. **Tier binds symmetrically.** The test of whether you are applying the tier system honestly is whether you have ever demoted a source you agree with.
6. **"Debunked" and "suppressed" are both tier claims.** Each requires its own chain, at the same standard as the claim it addresses.
7. **Log discrepancies; do not smooth them.** Where sources conflict, register the conflict with a resolution path rather than quietly selecting the convenient one.

---

## II.6 — Axis 2: Probative weight classes

Weight is assessed **relative to the specified models**, and is independent of tier.

| Class | Name | Definition | Handling |
|---|---|---|---|
| **W0** | Non-discriminating | Equally expected under both models | **Zero weight, regardless of tier.** Should not consume discussion time. |
| **W1** | Weakly discriminating | Slightly more expected under one | Mention, don't lean on |
| **W2** | Moderately discriminating | Meaningfully more expected under one | Standard evidentiary currency |
| **W3** | Strongly discriminating | Highly expected under one, surprising under the other | Focus of discussion |
| **W4** | Near-dispositive | The disfavored model must add an auxiliary assumption to survive it | Decisive absent rebuttal |

A large majority of the material generated in public controversy about high-profile cases is **W0**: true, verifiable, and analytically inert, because it is exactly what both models predict. Identifying and setting aside W0 material early is the fastest way to make a discussion productive.

**The combined judgment on any item is the product of its axes.** A `T1/W0` item is a fact that changes nothing. A `T3/W3` item may deserve an hour. Arguing about tier on a W0 item is wasted effort; arguing about weight on an unrated item is premature.

---

# PART III — CROSS-CORRELATION ANALYSIS

The tier system tells us what to believe and how much each item matters. This part addresses how items **combine** — which is where most analytical errors actually occur.

## III.1 — The core engine: likelihood ratios, not confirmation counting

For each evidence item `E`, and models `A` and `B`:

```
LR(E) = P(E | A) / P(E | B)
```

- `LR > 1` → favors A
- `LR < 1` → favors B
- `LR ≈ 1` → noise (this is W0)

And accumulation happens in log-odds:

```
log(posterior odds) = log(prior odds) + Σ log LR(Eᵢ)
```

You do not need to compute precise numbers for this to be useful. The **discipline** is what matters, and it is this: for every item raised, both parties must state *how expected that item is under their own model, not merely under the opponent's.*

This one requirement dismantles the most common rhetorical structure in these debates — **confirmation counting**, the presentation of a long list of facts "consistent with" a model. Consistency is nearly worthless as evidence, because most facts are consistent with both models. Only *differential expectation* moves anything.

**Reframe to insist on:** not "is this consistent with my model?" but "how surprised would I be by this if I were wrong?"

## III.2 — Independence auditing (the substance of "cross-correlation")

The summation above is valid **only for independent items.** Correlated items double-count and can inflate confidence arbitrarily. This is the single largest source of overconfidence on all sides of contested events.

Tag every evidence item with an **independence cluster ID**, using these correlation classes:

| Class | Name | Description | Example form |
|---|---|---|---|
| **C1** | Common source | Multiple outlets, one origin | Twelve articles all tracing to one press conference or one wire report |
| **C2** | Common cause | Multiple items generated by one underlying process | Several claims all derived from a single affidavit, or all downstream of one witness |
| **C3** | Common method | Same measurement technique, same failure mode | All timestamps from one clock; all identifications from one photograph |
| **C4** | Common actor/incentive | Sources sharing an interest in one framing | Multiple statements from within one institution, or one advocacy network |

**Rule:** within a cluster, take the strongest member and heavily discount the remainder. Then report **effective independent items**, not raw item count.

A list of thirty sources that collapses to four independent clusters is four pieces of evidence, not thirty. Both parties should expect to see their own evidence lists shrink substantially under this audit — that is the audit working, not an attack.

## III.3 — Cross-modal convergence (the strongest signal available)

Where *different modalities* agree, the probability of coincidental agreement collapses, because each modality has a **different error mode** and they would all have to fail in a mutually consistent direction.

Modalities to cross-check against one another:

- **Physical/geometric** — distances, sightlines, trajectories, positions
- **Temporal** — timestamps from independent clocks (device, CCTV, dispatch, broadcast, transaction)
- **Digital/records** — device data, transactions, metadata, access logs
- **Testimonial** — witness accounts and statements
- **Documentary** — filings, institutional records, correspondence
- **Biological/forensic** — DNA, trace, pathology

**Implications:**

- A claim corroborated across **three modalities with distinct failure modes** is qualitatively stronger than one supported by ten items within a single modality. This is a difference in kind, not degree.
- Conversely, a **cross-modal contradiction** — where a testimonial account conflicts with a physical or temporal constraint — is the most informative single finding obtainable from a public record, precisely because it cannot be explained away by one source being mistaken or dishonest. Material constraints have no incentives.

This is where analytical effort is best spent. Cross-modal checks are laborious and rarely performed in public argument, which is exactly why they are where the remaining information is.

## III.4 — Discrepancy triage

Not all contradictions carry the same weight. Classify each:

| Class | Type | Weight | Notes |
|---|---|---|---|
| **D-I** | Terminological — different words, same referent | ~0 | Extremely common; frequently misread as substantive |
| **D-II** | Precision — rounding, approximation, "about" | ~0 | Normal in verbal accounts |
| **D-III** | Temporal revision — early statement later corrected | Depends on base rate | See §III.5 |
| **D-IV** | Source vs. source — two accounts conflict | Moderate | Resolvable via tier and independence |
| **D-V** | Source vs. physical constraint | **High** | Physics has no motive |
| **D-VI** | Unexplained persistence — a discrepancy surviving after actors had motive and opportunity to resolve it | **High** | The delta between "unresolved" and "unresolvable" is informative |

**Two symmetric failure modes to guard against:**

- **Anomaly inflation** — treating D-I and D-II items as substantive findings and accumulating them into an apparent pattern. Any complex event generates these in quantity.
- **Silent smoothing** — quietly selecting the convenient version when sources conflict, rather than registering the conflict.

The correct practice is to log every discrepancy with an explicit resolution path and a status, and to classify it before weighting it.

## III.5 — Base rates before anomaly

**Before treating any feature as anomalous, establish how often it occurs in comparable cases where the account is undisputed.**

Candidate reference classes: high-profile shootings; rapid-manhunt investigations; cases with saturation early media coverage; capital prosecutions; cases with substantial online attention.

If a feature occurs in most comparable cases, its presence here is approximately **W0** — regardless of how strange it feels in isolation.

This is the single most effective corrective to the "too many coincidences" argument. But note the **mirror-image error** is equally lazy: "coincidences happen, so ignore it" is not analysis either. The correct move for any coincidence is to estimate its probability **under both models** and take the ratio. Sometimes that ratio is large. Sometimes it is 1. You have to actually look.

## III.6 — Coincidence budgeting

Every model has a **coincidence budget**: the set of facts it must treat as coincidental or unexplained.

Procedure:
1. For each model, enumerate explicitly what it must call coincidence.
2. Estimate the individual improbability of each.
3. **Apply the independence audit first** — coincidences within one cluster are one coincidence, not five.
4. Compare the resulting budgets.

The model requiring fewer and less improbable independent coincidences is favored, other things equal. The step most often skipped is (3), which is precisely the step that usually does the work.

## III.7 — Auxiliary-hypothesis accounting

Maintain a running ledger, per model, of every unevidenced assumption the model must add in order to absorb contrary evidence.

Each addition costs twice:
- **Probabilistically**, via the conjunction rule (§I.6)
- **Structurally**, if the addition is itself unfalsifiable

**Diagnostic signature:** a model whose auxiliary-hypothesis count grows monotonically with each new piece of evidence is being *rescued*, not confirmed. A model that accommodates all possible evidence predicts none of it.

This test applies to official accounts and alternative accounts identically, and is one of the few tests that is genuinely hard to game.

## III.8 — Robustness checks

Before stating a conclusion, run these four and report the results:

1. **Leave-one-out** — remove your single strongest item. Does the conclusion survive?
2. **Cluster-out** — remove your largest independence cluster. Does it survive?
3. **Prior sensitivity** — substitute the other party's stated prior. Where does the posterior land? *If the conclusion flips under a plausible alternative prior, that is the honest finding and should be stated as such.*
4. **Adversarial reconstruction** — each party articulates the **strongest** version of the other's model, to the other's satisfaction, before attacking it. This prevents the extremely common pattern of defeating a weak variant and claiming the category.

## III.9 — Pre-registration of predictions

Before the next tranche of record becomes available — rulings, trial proceedings, discovery releases, document unsealing — each party writes down specific predictions with confidence levels, and both are scored afterward.

This is the only mechanism that converts a debate into a **calibration instrument**. It is also the strongest possible demonstration of good faith, in both directions, and costs nothing to agree to.

## III.10 — Selection-effect check on our own inputs

What reached either of us was filtered — by search algorithms, feeds, prior reading, and our own attention. Before concluding, each party should ask:

> *"If my model is correct, what evidence would exist that I would predictably **not** have encountered? Did I go looking for it?"*

A model that has never sent its holder looking for something they didn't want to find has not been tested.

---

# PART IV — WORKING ARTIFACTS

## Table A — Model Specification Sheet
*(One per model, completed before evidence review)*

| Field | Entry |
|---|---|
| Model ID | |
| One-sentence statement | |
| Actors and roles | |
| Mechanism (step-by-step) | |
| Necessary conditions | |
| Predictions (what the record should contain) | |
| Falsifiers (what would defeat it) | |
| Coincidence budget | |
| Required conjuncts (count) | |
| Auxiliary hypotheses added to date | |

## Table B — Evidence Ledger

| ID | Claim | Tier (with chain) | Cluster ID | Correlation class | Modality | P(E\|A) | P(E\|B) | LR | Weight class | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| E-01 | | `[T1 via T3]` | K-1 | C1 | Documentary | | | | W0–W4 | |

## Table C — Discrepancy Register

| ID | Description | Class (D-I…D-VI) | Sources | Tier of each | Resolution path | Status |
|---|---|---|---|---|---|---|
| D-01 | | | | | | Open / Resolved / Unresolvable |

## Table D — Scorecard

| Field | Model A | Model B |
|---|---|---|
| Stated prior (odds) | | |
| Effective independent items | | |
| Σ log LR | | |
| Posterior (odds) | | |
| Leave-one-out result | | |
| Cluster-out result | | |
| Prior-sensitivity result | | |
| Auxiliary hypotheses added | | |

---

# PART V — RULES OF ENGAGEMENT

A short list to agree to verbally at the outset.

1. **Claims get chains.** "Court documents say" requires the document, or an explicit `via` label.
2. **Tier binds symmetrically.** The same standard applies to sources we like.
3. **No load-bearing Tier 4.**
4. **Possibility is not evidence.** Discriminating power is.
5. **Steelman before attacking.** Each party states the other's model in its strongest form first.
6. **Anomalies require base rates** before they count as anomalies.
7. **Correlated sources count once.**
8. **Auxiliary assumptions get logged**, on both sides.
9. **"I don't know" is a permitted and often correct terminal state** for any sub-question. Neither party is obligated to have a complete account.
10. **Either party may call a scope flag** when question-types (a)–(d) collapse into each other.
11. **Distinguish belief from strength of belief.** State confidence, not just position.
12. **Update out loud.** Say when you have moved and why. Nothing is more corrosive to a good-faith exchange than silent revision.

---

# PART VI — FAILURE-MODE GLOSSARY

A quick-reference list. Each is available to either party as a named, callable objection.

| Term | Definition |
|---|---|
| **Citation laundering** | A claim of unknown origin acquiring authority through repeated citation |
| **Tier inflation / chain collapse** | Citing a claim at its origin tier when you only possess it at a lower conduit tier |
| **Confirmation counting** | Listing facts "consistent with" a model, without asking whether they are equally consistent with its rival |
| **Anomaly inflation** | Accumulating D-I/D-II noise into an apparent pattern |
| **Coincidence stacking** | Multiplying correlated coincidences as if independent |
| **Coincidence dismissal** | Waving away an improbable convergence without estimating it under either model |
| **Conjunction creep** | Adding specificity to a narrative, increasing its felt plausibility while decreasing its probability |
| **Motivated stopping** | Ending inquiry at the point the answer becomes congenial |
| **Asymmetric skepticism** | Applying different evidentiary standards to congenial and uncongenial claims |
| **Unfalsifiable insulation** | A model structured so no observation can count against it |
| **Incompetence/malice conflation** | Treating evidence of institutional failure as evidence for a specific coordinated alternative |
| **Genetic dismissal** | Rejecting a checkable claim solely because of who made it |
| **Argument from incredulity** | "I can't see how that would happen" treated as evidence it didn't |
| **Proof-demand asymmetry** | Demanding a standard of proof from the other side that your own position could not meet |
| **Silent smoothing** | Resolving source conflicts by quietly choosing the convenient version |
| **Layer confusion** | Arguing about W, R, and C as though they were one object |

---

## Closing note

The framework above is deliberately demanding, and it will be uncomfortable in both directions. If applied honestly it should produce, for each participant, at least one of the following outcomes:

- an evidence list that shrinks materially under the independence audit
- a conclusion that proves sensitive to the prior rather than to the evidence
- a set of claims that cannot be walked back to a retrievable source
- a discovery that a favored anomaly has a high base rate in comparable cases

If a participant completes the exercise and none of these occur, that is itself worth examining — it is more likely a sign that the framework was applied selectively than that the participant's model was unusually well-constructed.

The goal is not to reach agreement. The goal is to make any remaining disagreement **precise**: to be able to say exactly which item, which prior, or which independence judgment the disagreement rests on. A disagreement located that precisely is a productive result, even if it is never resolved.
