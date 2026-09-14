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
