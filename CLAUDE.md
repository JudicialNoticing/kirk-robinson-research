# CLAUDE.md — Kirk Staging Research Library

## What this project is

An open-source research library on the September 10, 2025 assassination of Charlie Kirk
(*State of Utah v. Tyler James Robinson*, Case No. 251403576, Fourth District Court, Provo),
related actors (George Zinn, Lance Twiggs, Erika Kirk), physical/forensic questions
(Losee building, rifle photo, DNA), and media narratives about the case — currently
Candace Owens' "Bride of Charlie" series.

The purpose is **not** to prove or debunk any narrative. It is to build files that separate,
claim by claim, what is *established* (and at what confidence) from what is merely *asserted* —
and then to state graded, falsifiable conclusions. A file that only inventories claims is
unfinished; a file that reaches conclusions its citations can't carry is worse than unfinished.

The deliverable is always the files. Every session's work lands in a versioned file with a
revision-log entry — no untracked conclusions in chat only.

## Prime directive: two layers, never blended

Every file maintains a strict separation:

1. **Recording layer** — what a claimant (Owens, an official, a witness, an outlet) actually said.
   Accuracy here means *fidelity to the claim*, quoted or closely paraphrased, cited, even when
   the claim is false.
2. **Analyst layer** — what the established record shows. Accuracy here means *independently
   verified fact*, with source tier and confidence grade attached.

Recording a claim faithfully is never an endorsement. Asserting a fact in the analyst layer
without independent verification is the project's cardinal error (see: the V-10 lesson — a
detail carried from the claimant at "High" confidence had to be recalibrated on audit).
When correcting, identify which layer the error lived in.

## Sourcing framework (project standard — reproduce in every evidence file §0)

- **Tier 1** — Sworn testimony and primary court filings / primary documents
- **Tier 2** — Named official statements (incl. named first-person statements by principals)
- **Tier 3** — Named journalistic reporting/analysis
- **Tier 4** — Anonymous-source or low-verification material

Marking rules:
- **"T1 via T3"** when primary-document content is known only through reporting, not direct
  reading of the filing. Never silently promote it to Tier 1.
- **Access-path caveats go first** in the file: paywalls, blocked retrievals, machine-transcript
  dependence (with garble-normalization noted, e.g. "Erica"→Erika), anything standing between
  the file and the primary artifact.
- Every claim gets a URL; every retrieval gets a date. Editorial characterizations from any
  outlet are labeled *assessments*, not established fact, with an outlet-orientation note
  (hostile / neutral / sympathetic) for calibration — orientation is context, not disqualification.

## Confidence and register conventions

- **Confidence grades:** High / Medium-high / Medium / Low / unverified. A grade must trace to
  an actual verification act by this project — not inherited from the claimant, not inherited
  from repetition across outlets (syndicated recaps are one source, not many).
- **"— (checkable)"** marks items that are verifiable but not yet verified — these feed the
  Tier 1 acquisition roadmaps, and are never counted as findings.
- **Registers:** D-numbers (discrepancy register — cross-file, sequential, no gaps or duplicate
  assignments), V-numbers (verification items), F-numbers (flags), M-numbers (roadmap mechanics).
  Check the highest existing number before assigning a new one.

## Objectivity mechanics (procedures, not vibes)

1. **Verify in both directions.** Actively search for evidence that *supports* the claimant as
   hard as for evidence that refutes them, and log confirmations explicitly. An audit trail that
   only ever weakens one side is itself a bias signal (BOC-AUDIT Part 5.2 states this rule; keep it).
2. **Separate anchors from connections.** A claimant's checkable facts (dates, venues, names —
   "calendar anchors") verifying as true does *not* verify the connections asserted between them.
   Grade the anchor and the connection independently, always.
3. **Absence of evidence is a finding with a scope.** "No evidence found" must state where you
   looked and what access failed. It is not "evidence of absence" unless the search space would
   necessarily contain the record.
4. **Corrections in place, never silent.** Fix the file, add a revision-log row saying what
   changed and why, bump the version. Supersessions get matching log rows on both ends.
5. **State residual scope.** Every audit or substantial file says plainly what it did *not*
   re-verify. Unstated scope reads as coverage that doesn't exist.
6. **Steelman before resolving.** Before a register entry resolves against a claimant, the file
   must show the strongest reading of their claim was considered.

## Conclusions standard (what "elucidating" means here)

- Files end in **findings, resolutions, and open items** — not a trailing pile of claims.
- Every conclusion is (a) stated plainly, (b) confidence-graded, (c) tied to the specific
  V-/D-items that carry it, and (d) accompanied by what evidence would change it.
- Prefer narrow resolutions ("resolved against Owens on the D-33 date sub-claim") over global
  verdicts ("Owens is wrong"). Pattern findings across many narrow resolutions are the
  project's strongest output — e.g., "checkable calendar anchors are usually right or nearly
  right; the asserted connections between them remain unevidenced."
- Never resolve a register entry on Tier 4 alone.

## Living persons and legal care

- Allegations are **attributed, never adopted**. Criminal accusations respect presumption of
  innocence; before writing about case posture, verify the *current* status as of the writing
  date and date-stamp it ("as of YYYY-MM-DD").
- Private individuals (family members, roommates, classmates): include only what bears on the
  public questions under investigation. No home addresses, contact details, or identifying
  information about uninvolved parties — even when sources publish them.
- Quotations from affidavits and filings are kept minimal; paraphrase everything else.
- Dream-derived, vibes-based, or self-labeled-opinion material (e.g., the Elizabeth Lane post)
  is recorded for completeness and assigned **zero evidentiary weight by its own terms**.

## File conventions

- **Topic folders:** `files - <Topic>` at the repo root (exact pattern: `files`, space, dash,
  space, topic name). Paths contain spaces — always quote them in shell commands.
- **Each topic** carries (1) an evidence/claim-inventory file and (2) a Tier 1 source-acquisition
  roadmap. Series files use IDs (`BOC-E01`, `BOC-T1`); audits are `<PREFIX>-AUDIT-YYYY-MM-DD`.
- **Every file header:** File ID (where applicable), scope, case context, Prepared date,
  Status/version. All dates absolute (never "last week").
- **Every file ends** with a revision log: | Version | Date | Change |.
- New evidence files reproduce the four-tier framework as §0 and the access-path caveat as §1.

## Operational rules

- File operations are non-destructive by default: copies/moves via `migrate-files.sh`
  (verifies file lists and byte totals; leaves source intact); deletions go to `~/.Trash`,
  not `rm`.
- Web research records the retrieval date and preserves the full URL. Failed retrievals
  (bot-blocks, paywalls) are logged as access-path caveats, not silently dropped.
- When an edit session touches multiple files, the audit/summary file lists every
  file → version change (BOC-AUDIT Part 3 is the model).
