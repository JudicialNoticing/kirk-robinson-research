# GLOSSARY — the library's terms

**Prepared:** 2026-09-15. Definitions are taken from `CLAUDE.md`, `VERIFICATION-PROTOCOL.md`, `LOOP.md`, `QUEUE.md` (standing hazards) and the evidence files; where a term is used loosely in older files, the strict sense is given.

## Sources and confidence

| Term | Meaning |
|---|---|
| **Tier 1 (T1)** | Sworn testimony; primary court filings and primary documents, read directly |
| **Tier 2 (T2)** | Named official statements, including named first-person statements by principals |
| **Tier 3 (T3)** | Named journalistic reporting or analysis |
| **Tier 4 (T4)** | Anonymous-source or low-verification material. Never load-bearing; a register entry is never resolved on T4 alone |
| **T1 via T3** | Primary-document content known only through reporting, not from reading the filing. Never silently promoted to T1 |
| **Confidence grade** | High / Medium-high / Medium / Low / unverified. Must trace to a verification act by this library, not to the claimant or to repetition across outlets |
| **— (checkable)** | Verifiable but not yet verified. Feeds the acquisition roadmaps; never counted as a finding |
| **Access-path caveat** | Anything standing between the file and the primary artifact (paywall, bot-block, machine transcript, no text layer). Goes first in every file (§1) |
| **Outlet orientation** | hostile / neutral / sympathetic, noted for calibration; context, not disqualification |

## Layers, labels and status

| Term | Meaning |
|---|---|
| **Recording layer** | What a claimant, official, witness, outlet or filing actually said, quoted or closely paraphrased, even when false. Fidelity is the standard |
| **Analyst layer** | What the record independently establishes, with tier and confidence. Independent verification is the standard. Blending the layers is the cardinal error |
| **Label** | What a check of a sentence returned (kit vocabulary): `SUPPORTED` (may be stated as fact, with citation) · `CONTRADICTED` (correct or delete) · `UNVERIFIED` (a check ran and found nothing; sink only) · `SECOND_HAND` (support runs only through this library's own restatement; flag as such) · `VALID_STEP` / `INVALID_STEP` (an inference holds / fails; an invalid step taints everything after it) · `POST_HOC` · `OVERCLAIM` (rewrite before use). Orthogonal to tier: both are written |
| **`[PROVISIONAL]`** | Labels incomplete for the file's stated scope. Findings may not be cited by another file, propagated to another topic folder, or used to resolve a register entry until a verification cycle clears them (`LOOP.md` §2). Not a synonym for "wrong" |
| **VERIFIED** | Labels complete for the stated scope. Never "true"; no file certifies itself |
| **Sink** | The section at the foot of a file where unverified, contradicted, second-hand and overclaimed material is kept, labeled, rather than polished into the analyst layer |
| **Isolation rule** | A checker receives the target sentence and the sources, never the finder's diagnosis or proposed correction. Violated by the first three TJR-P01 cycles, which returned 65 confirmations out of 65 |
| **Taint propagation** | A `CONTRADICTED` fact taints every sentence that used it; an `INVALID_STEP` taints every later inference. Sweeping the footprint is its own pass |
| **Three-iteration cap** | At most three verification iterations per protocol, then publish what is labeled. "Loop until no more errors" is retired |
| **Footprint** | Everywhere a claim appears: body, findings, headings, revision-log rows, sibling files, deliverables. Corrections are scoped to the footprint, not the reported sentence |
| **Steelman** | The strongest reading of a claimant's claim, shown before a register entry resolves against them |
| **Both-directions rule** | Search for evidence that supports the claimant as hard as for evidence that refutes them; an audit trail that only weakens one side is a bias signal |

## Registers and identifiers

| Term | Meaning |
|---|---|
| **D-number** | Discrepancy register. Cross-file, sequential, no gaps, no duplicates. The ceiling is stated once, in `QUEUE.md`'s header; everything else points there. Assign by reading the highest existing assignment, never by counting strings (a forward-looking "next is D-nn" note matches the pattern) |
| **F-number** | Flag. Older files use a bare series (to F-143, with gaps); newer files write `<FILE-ID> F-n` |
| **V-number, M-number** | Verification items; roadmap mechanics |
| **Q-number** | Queue item in `QUEUE.md`. Never reused. Columns: Status (ready/blocked/done…), Blocked by, Decisive artifact, Cost, Gate |
| **File ID** | `<PREFIX>-<TYPE><nn>` or `<PREFIX>-<TYPE>-<date>[letter]`. Prefixes: `BOC` Bride of Charlie · `CR` court record · `DNA` · `SEC` event security · `ZINN` · `TJR` Tyler James Robinson · `LOSEE` (proposed, never ratified). Types: `E` evidence · `T1` roadmap · `ACQ` acquisition log · `AUDIT` · `REVIEW` · `ROUTE` · `P` profile · `WATCH` |
| **Revision log** | The `| Version | Date | Change |` table every file ends with. One version bump and one combined row per file per session |
| **Supersession** | When a file or section replaces another, both ends get a matching revision row |
| **WIP file** | `*_WIP-state.md` in a topic folder means a session paused mid-work; resume from its NEXT STEPS, then retire it |

## Artifacts and the bank

| Term | Meaning |
|---|---|
| **Bank / banked** | An artifact saved into the library with its route, date and hash recorded. The court bank is `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/` |
| **Artifact class** (manifest) | `primary-source` (court documents, official statements) · `transcript` (hearing days) · `source-capture` (raw HTTP bodies from a verification fetch) · `process-evidence` (agent journals, verdicts, snapshots). A null about the case record is never satisfied by process evidence |
| **Readability class** (manifest) | `text-native` · `U+FFFE-SPLIT` (words split by a noncharacter used as a soft hyphen; search both readings) · `NO-TEXT-LAYER` (render it) · `OCR-GARBLE` (render it) · `IMAGE-ONLY` (a rendered page) · `raw-capture` (prefer its extraction) · `structured-data` (parse, do not prose-search) |
| **dc-id, dkt** | DocumentCloud document id and court docket number encoded in a bank filename. Metadata is a claim someone typed: read the face |
| **DocumentCloud project 224251** | The public project through which most court filings were obtained; completed 46/46 on 2026-08-16, then found not to be the whole corpus |
| **XChange** | Utah's paid court-records portal. Two case-history printouts are banked; a `grep` over them fails silently (hazard 13) |
| **Rev** | The transcript service whose renderings of the five hearing days are banked. Its timestamps are recording-stream locators, not clock time; **its speaker labels are not evidence** (witness answers routinely carry counsel's name) |
| **`day1.txt` … `day5.txt`** | The preliminary hearing, 2026-07-06 to 2026-07-10, as Rev rendered it. `2026-09-01_final-prelim-argument.txt` is the bindover argument |
| **The contaminant** | `2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.pdf/.txt`, a mis-banked unrelated federal filing ("BAM Franchising"). Kept, named, excluded per term |
| **NUL repair** | On 2026-08-16 the extractor's `0x00` page separators were replaced with `0x0C` in 50 `.txt` files, because that value was unambiguous. `artifact_search.load()` refuses a file where NULs have reappeared |
| **Null / scoped null / false null** | "No evidence found" with where you looked and what failed (scoped). A null from a method never validated against a known positive is a claim about the search, not the corpus (false null hazard) |
| **Known positive** | A passage known to exist, searched for before any null is believed (`tsearch.py --validate`) |
| **Frozen snapshot** | `profile_v<n>_pre-<pass>.md`: the state of a file before a correction pass, banked so the pass can be audited. Never edited |

## Operations

| Term | Meaning |
|---|---|
| **Cycle** | One iteration of `LOOP.md` §1: take the highest-priority ready item, execute, record findings as provisional, audit, update the queue |
| **Gate** | `auto` (execute and commit) · `verify` (execute; findings stay `[PROVISIONAL]`) · `human` (stop and write the question into the queue). Always human: case posture, conduct by a living person, spending, credentials, publishing, topic-folder changes, resolving a register entry against a named person |
| **Standing hazards** | The numbered list in `QUEUE.md` of measured ways this library has been wrong (selective quotation, provenance, sampling, metadata vs content, search nulls, register numbering, non-unique exhibit numbers, Rev labels, NULs, U+FFFE, null batteries, self-counts running one low…) |
| **Docket watch** | `DOCKET-WATCH.md` (the calendar and access routes), the cloud routine that fires on a schedule, `scripts/docket-watch-run.py` (a local run diffed against a baseline), and `CR-WATCH-log.md` (one row per run, even when nothing is found) |
| **Routine / trigger** | The scheduled cloud agent (`trig_016faLfbQWCz72M463Dy8HsL`). Its prompt is mirrored in `ops/docket-watch/`; applying a draft to it is owner-gated |
| **Session close (P10)** | The kit's last protocol: a session log written next to the notes, and the project's own tracking (START-HERE, QUEUE) updated |
| **Owner-gated (👤)** | An action only the owner may take: approvals, spending, applying the routine prompt, pushing `main`, the final publish click |

## Case vocabulary

| Term | Meaning |
|---|---|
| **Bindover** | The magistrate's finding of probable cause after a preliminary hearing, sending the case to trial. Not a finding of guilt. Ordered orally 2026-09-01; the signed 26-page order is banked |
| **Information / PCA** | The State's charging document (Information, 2025-09-16) and the Affidavit of Probable Cause (2025-09-12) |
| **Losee** | The Losee Center at Utah Valley University, from whose rooftop the shot is alleged to have been fired |
| **UVU** | Utah Valley University, Orem, site of the 2025-09-10 event |
| **State's Exhibit 30 / 32 / 33** | ATF laboratory reports entered at the hearing; "Exhibit 30" has had three referents in the record, see `CR-E20` |
| **Likelihood ratio** | The DNA statistic testified to; a ratio of conditional likelihoods, not the probability that a named person is the source (the "transposed conditional" error, `TJR-P01` §8.4) |
| **Bride of Charlie (BOC)** | Candace Owens' eight-episode series about Erika Kirk, inventoried claim by claim in `files - Bride of Charlie series/` |
