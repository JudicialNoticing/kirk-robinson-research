# ARCHITECTURE — how the pieces fit, and how data flows

**Prepared:** 2026-09-15 (with the Phase 2 reorganisation, `AUDIT.md`). Describes the library as it is; inferences are marked *(inference)*.

## 1 · What kind of system this is

Not software. A **research record** with a strict provenance discipline: every sentence in the analyst layer must be traceable to a banked artifact, and every artifact must be findable, readable and cited. The "code" is a handful of tools that keep that discipline honest. The "data model" is the file and folder naming, the File IDs, and the cross-file registers.

## 2 · The five layers, and the flow between them

```
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │ 1. ACQUISITION                                                                     │
 │   CR-ACQ-* / BOC-ACQ-* / ZINN-ACQ-* files record how each artifact was obtained    │
 │   (route, date, hash, access-path caveats). The artifact itself is BANKED:          │
 │     files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/   (court PDFs + .txt,│
 │        hearing transcripts day1..5 + final argument, Rev official statements)       │
 │     files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/ (raw HTTP)│
 │     files - Bride of Charlie series/BOC-*_artifacts/, files - George Zinn/ZINN-ACQ-*│
 │   scripts/manifest.py indexes every bank → SOURCE-MANIFEST.md / source-manifest.json│
 └──────────────────────────────┬─────────────────────────────────────────────────────┘
                                │ read directly (never through a party's characterisation)
                                ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │ 2. EVIDENCE FILES  (<PREFIX>-E<nn>_slug.md, and the pre-ID files from July)         │
 │   §0 four-tier framework · §1 access-path caveats · recording layer vs analyst layer│
 │   · confidence grades · registers (D-/F-/V-/M-) · nulls with scope · open items ·   │
 │   findings · revision log.  Status: Draft → [PROVISIONAL] → VERIFIED (labels        │
 │   complete for the stated scope — never "true").                                     │
 │   Roadmaps (*-T1*, tier1-acquisition-roadmap*) list the primaries that would lift    │
 │   "T1 via T3" claims to T1.                                                          │
 └──────────────────────────────┬─────────────────────────────────────────────────────┘
                                │ claims extracted, checked in isolation, labeled
                                ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │ 3. VERIFICATION                                                                     │
 │   Reports: <PREFIX>-AUDIT-YYYY-MM-DD (session/adversarial audits),                  │
 │            <PREFIX>-REVIEW-YYYY-MM-DD (verification cycles on named files).         │
 │   Banks:   verification/<ID>-REVIEW-<date>_verification-cycle-<n>/ — agent journals,│
 │            verdict files, frozen pre-correction snapshots (process evidence).        │
 │   Method:  docs/research-verification-kit/ (P1–P10), as adopted in                  │
 │            VERIFICATION-PROTOCOL.md: isolation, taint, ≤3 iterations, the sink.      │
 │   Output flows BACK into layer 2 as corrections in place + a revision-log row.       │
 └──────────────────────────────┬─────────────────────────────────────────────────────┘
                                │ open items, blockers, decisions, calendar
                                ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │ 4. TRACKING & OPERATIONS                                                            │
 │   START-HERE.md (dated state, owner gates) · QUEUE.md (work graph, D-ceiling,       │
 │   standing hazards) · LOOP.md (cycle, gates auto/verify/human, hard stops) ·        │
 │   DOCKET-WATCH.md (court calendar) · files - Court record/CR-WATCH-log.md (one row  │
 │   per watch run) · ops/docket-watch/ (the prompt deployed on the cloud routine)     │
 │   scripts/queue-check.sh validates this layer; scripts/docket-watch-run.py runs a   │
 │   local watch.                                                                      │
 └──────────────────────────────┬─────────────────────────────────────────────────────┘
                                │ rendered for sharing
                                ▼
 ┌────────────────────────────────────────────────────────────────────────────────────┐
 │ 5. DELIVERABLES   deliverables/*.html, *.docx — built by scripts/build-html.py and   │
 │   scripts/build-docx.js from a markdown source; never edited by hand.               │
 └────────────────────────────────────────────────────────────────────────────────────┘
```

### The flow in words

1. **Acquire and bank.** A route (DocumentCloud, XChange, Rev, a court page, a podcast feed) yields an artifact. It is saved under a name that encodes what the filename claims (`YYYY-MM-DD_slug_dktN_dcID.pdf`), hashed, and paired with a `.txt` extraction where one is possible. The acquisition file records the route and every access-path caveat. `manifest.py` then classifies each artifact by **kind** (primary-source, transcript, source-capture, process-evidence) and by **readability** (text-native, U+FFFE-SPLIT, NO-TEXT-LAYER, OCR-GARBLE, IMAGE-ONLY, raw-capture, structured-data) and lists which library files cite it. A filename or a title is a claim someone typed; the face of the document is read before anything is asserted from it.
2. **Read and write.** An evidence file reads artifacts directly and writes two layers: what a claimant or filing says (recording layer, faithful even when false) and what the record establishes (analyst layer, tiered and graded). Nulls carry their scope ("searched X with method Y"); a null from a plain `grep` over the bank is not a null until the method is validated (`tsearch.py --validate`, `artifact_search.py`).
3. **Verify.** A cycle extracts the file's claims and hands each to a checker that sees the sentence and the sources and nothing else (the isolation rule). Results are labels (`SUPPORTED`, `CONTRADICTED`, `UNVERIFIED`, `SECOND_HAND`, …). Corrections land in place with a revision-log row; unverifiable material goes to the file's sink. The agent output is banked under `verification/` so the cycle can itself be audited. A contradicted fact taints every file that used it; the footprint is swept.
4. **Track.** New open items go to `QUEUE.md` with a decisive artifact, cost and gate. Register numbers are assigned by reading the highest existing assignment, never by counting strings. Time-critical court dates live in `DOCKET-WATCH.md`; a cloud routine and a local runner watch them and write rows to `CR-WATCH-log.md`.
5. **Render.** TJR-P01 and the forensic sampling summary are shared as HTML/DOCX from `deliverables/`.

## 3 · The scripts and what they touch

| Script | Reads | Writes | Depends on |
|---|---|---|---|
| `scripts/manifest.py` | every `**/*.md` (except `docs/`, `archive/`, `AUDIT.md`, `INDEX.md`, its own output, frozen snapshots) and four bank directories | `SOURCE-MANIFEST.md`, `source-manifest.json` | poppler (`pdftotext`, `pdfinfo`) |
| `scripts/artifact_search.py` | one `.txt` at a time; CLI audits `<court bank>/*.txt` | nothing | — |
| `scripts/tsearch.py` | `<court bank>/prelim-hearing-transcripts/day{1..5}.txt` | nothing | — |
| `scripts/queue-check.sh` | `QUEUE.md`, all `*.md`, the court bank, `git status` | nothing | git |
| `scripts/docket-watch-run.py` | DocumentCloud API, Wayback CDX, rev.com sitemap, utcourts news; `<court bank>/docket-watch-baseline.json` | the baseline (with `--baseline`) | network |
| `scripts/build-html.py`, `scripts/build-docx.js` | a markdown source | an HTML/DOCX file | Node + `docx` for the latter |
| `scripts/migrate-files.sh` | a folder | a verified copy | — |

Every path inside a script is resolved from the script's own location, so the tools run from any directory. The court bank path is hard-coded in five of them by design: it is the citation namespace and does not change.

## 4 · Identifiers that hold the system together

| Identifier | Form | Assigned where | Rule |
|---|---|---|---|
| File ID | `CR-E19`, `BOC-E01`, `TJR-P01`, `SEC-E02`, `CR-ACQ-2026-08-16B` | the file's own header | Unique library-wide; cited by ID, not path |
| D-number | `D-76` | the file that finds the discrepancy | Cross-file sequential, no gaps, no duplicates; the ceiling is stated once, in `QUEUE.md`'s header |
| F-number | `F-4`, `CR-E19 F-4` | evidence files | Flags; newer files prefix with their File ID because the bare series has gaps |
| V-, M- | `V-10`, `M-3` | evidence files, roadmaps | Verification items, roadmap mechanics |
| Q-number | `Q-162` | `QUEUE.md` | Never reused; `queue-check.sh` verifies uniqueness and blocked-by references |
| DocumentCloud id / docket no. | `dc27880869`, `dkt117` | artifact filenames | Metadata, not content: read the face |
| Rev locator | `day4.txt 04:51:57` | transcripts | Recording-stream time, a locator not a clock; speaker labels are not evidence |

## 5 · External dependents

| Outside this folder | Depends on |
|---|---|
| Cloud routine `trig_016faLfbQWCz72M463Dy8HsL` (prompt mirrored in `ops/docket-watch/…LIVE…md`) | `DOCKET-WATCH.md`, `files - Court record/CR-WATCH-log.md`, the GitHub repo (currently refused: the routine's account cannot see the private repo, see `CR-WATCH-log.md` v2.4) |
| `~/.claude/settings.json` | the repo's absolute path as the trusted repo |
| Obsidian vault (`01 Projects/Kirk Robinson Research.md`, `AGENTS.md`) | the repo by name; root entry points |
| GitHub `JudicialNoticing/kirk-robinson-research` | `main` |

## 6 · What is deliberately not here

- **Tests.** The regression suite is the three self-checking tools (`tsearch.py --validate`, `artifact_search.py`, `queue-check.sh`) plus `manifest.py`'s counts. Run all four after any structural change.
- **A build.** Nothing compiles. Deliverables are rebuilt on demand.
- **Automation that writes conclusions.** `LOOP.md` §3: case posture, conduct by a living person, spending, publishing, and topic-folder changes are always human gates.
