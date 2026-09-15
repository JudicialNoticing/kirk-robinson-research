# AUDIT — Kirk Robinson Research library

**Prepared:** 2026-09-15 · **Phase:** 1 of 2 (read-only) · **Status:** awaiting owner approval before any move
**Scope:** every file and directory under `~/Documents/Kirk Robinson Research` excluding `.git/` internals.
**Method:** filesystem census (`find`/`stat`), MD5 hashing for duplicates, a cross-reference scan of all 409 text files for filenames, DocumentCloud ids and declared File IDs, a read of every script, `git ls-files`/`git status --ignored`, and a dry run of the three read-only entry points. **Nothing was moved, renamed, edited or deleted.** The only file written is this one.

**What this audit did not do:** it did not open every banked PDF or transcript, did not re-verify any research claim, and did not run `manifest.py` or `docket-watch-run.py` (both write files).

---

## 0 · Headline

This is not a code project. It is a research library of **499 files (116.6 MB, plus a 58 MB `.git`)** in which **~85 MB is banked primary evidence that must never move**, **~5 MB is verified research prose that cites that evidence by literal path**, and the rest is tooling, process evidence, tracking documents and generated output that has accreted at the root and inside the evidence folders.

The organising fact for Phase 2 is this: **the folder and file names are the citation namespace.** 46 markdown files carry 226 literal `files - <Topic>/…` paths; 43 carry the literal path of the court-record bank; the deployed cloud routine names two files by path; and six scripts hard-code the bank's location. Renaming a topic folder or moving a banked artifact would silently break citations inside files that carry version numbers, revision logs and `VERIFIED` stamps. So the proposal below **freezes the namespace** and reorganises *around* it: everything that is not evidence or a citation target moves into `scripts/`, `docs/`, `ops/`, `deliverables/`, `verification/` and `archive/`, and the root drops from 30 files to about 12.

**94 files move, 405 stay** (Appendix C has every path). Eleven decisions are marked ❓ for you in §8.

---

## 1 · Inventory

| Measure | Value |
|---|---|
| Files (excluding `.git`) | 499 |
| Directories below root | 30 |
| On-disk size (excluding `.git`) | 116.6 MB |
| `.git` | 58 MB, 148 commits since 2026-07-26 |
| Files at the root | 30 |
| Files over 10 MB | **1** (below) |
| File-age distribution (mtime) | Jul 2026: 93 · Aug 2026: 229 · Sep 2026: 177 |

**The one file over 10 MB:** `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.pdf` (23.1 MB). It is a **known mis-banked federal filing from an unrelated case** (the library's own files call it "the BAM Franchising contaminant"), kept in place deliberately because 23 files cite it as the named exclusion and `queue-check.sh` bakes it into its "sweepable artifacts" arithmetic. See ❓ Q9.

### 1.1 By directory

| Directory | Files | Size | What it is |
|---|---:|---:|---|
| `files - Court record/` | 363 | 102 MB | 44 evidence/audit/review files at top level (1.9 MB) plus three banks (below) |
| ↳ `CR-ACQ-2026-07-27_court-record-artifacts/` | 179 | 78 MB | The primary bank: 59 PDFs with text extractions, 5 hearing-day transcripts + raw HTML, official-statement transcripts, and (mixed in) 18 JSON/JSONL process outputs, 5 markdown drafts/notes, 1 Python and 2 JS one-off scripts, 4 rendered PNG pages |
| ↳ `CR-ACQ-2026-09-02_bindover-verification-fetches/` | 81 | 14.5 MB | Raw HTTP bodies from the 09-02 verification run, with its own SHA-256 `MANIFEST.md` |
| ↳ `TJR-REVIEW-2026-09-14_verification-cycle-1/` | 59 | 11.5 MB | The TJR-P01 verification bank: 33 agent journals/verdict files, 13 frozen pre-correction snapshots of the profile |
| `files - Bride of Charlie series/` | 61 | 12 MB | 16 claim inventories/audits/roadmaps + 45 web/feed/API captures in three artifact sub-folders |
| `files - George Zinn/` | 10 | 244 KB | 4 files + 6 DocumentCloud JSON captures |
| `files - Event security/` | 4 | 536 KB | 2 evidence files, 1 transcript, 1 raw HTML capture |
| `files - DNA evidence/` | 3 | 356 KB | DNA-E01 (303 KB), a roadmap, a consolidated audit |
| `files - Arrest chronology/` | 2 | 52 KB | timeline + roadmap |
| `files - Kirk assassination questions/` | 2 | 64 KB | official timeline + roadmap |
| `files - Losee building/` | 2 | 24 KB | evidence + roadmap (untouched since 2026-07-18) |
| `VerificationAndFactCheckProtocol copy/` | 13 | 268 KB | The adopted verification kit (10 files) + a duplicate drop file, an index, and the original zip |
| root | 30 | 1.8 MB | See §1.2 |
| `tools/` | 2 | 24 KB | HTML and DOCX builders, **untracked** |
| `__pycache__/` | 1 | 8 KB | Bytecode, **tracked** |
| `.obsidian/`, `.claude/` | 6 | 28 KB | Vault config; a stale harness checkpoint |

### 1.2 The 30 root files

| Group | Files |
|---|---|
| Entry points and tracking (stay) | `README.md`, `START-HERE.md`, `QUEUE.md`, `LOOP.md`, `DOCKET-WATCH.md`, `CLAUDE.md`, `VERIFICATION-PROTOCOL.md` |
| Generated index (stay) | `SOURCE-MANIFEST.md`, `source-manifest.json` |
| Routine-prompt versions (6) | `DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md`, `…-DRAFT-2026-08-14/08-16/08-17/09-02/09-14.md` |
| Evidence files loose at root (4) | `robinson-tyler-james-comprehensive-profile.md` (TJR-P01, 278 KB), `lance-twiggs-comprehensive-profile.md`, `erika-kirk-background-family-contested-claims-dossier.md`, `evidence-rifle-photo-nypost-authenticity.md` |
| Rendered deliverables (3) | `Tyler-Robinson_Comprehensive-Profile_2026-09-14.html/.docx`, `Forensic-Sampling-Summary_2026-08-30.docx` |
| Tooling (6) | `manifest.py`, `artifact_search.py`, `tsearch.py`, `docket-watch-run.py`, `queue-check.sh`, `migrate-files.sh` |
| Config / noise (2) | `.gitignore`, `.DS_Store` |

The full tree with per-file sizes is **Appendix A**.

---

## 2 · Classification

| Category | Files | Bytes |
|---|---:|---:|
| source code | 5 | 37.7 KB |
| config | 7 | 17.2 KB |
| data (raw) | 204 | 85.1 MB |
| data (processed/derived) | 73 | 5.0 MB |
| notebooks/experiments | 67 | 18.1 MB |
| scripts/one-offs | 7 | 90.7 KB |
| documentation | 109 | 5.2 MB |
| generated artifacts | 26 | 3.1 MB |
| tests | 0 | 0 B |
| assets | 0 | 0 B |
| unknown | 1 | 0 B |

Notes on the buckets (the per-file table is **Appendix B**):

- **data (raw)** is "the artifact as received": court PDFs, raw HTML/HTTP bodies, feed XML, API JSON, screenshots, transcripts saved as text. **data (processed/derived)** is anything computed from those: the `.txt` extraction that sits beside each PDF, the hearing-day `.txt` extracted from `_raw.html`, the `_condensed` views, the four rendered ATF pages. The library cites both forms, so the distinction matters for provenance, not for whether they may move (neither may).
- **notebooks/experiments** is where this project's "experiments" actually live: the agent journals, verdict files and candidate banks written by verification cycles. They are process evidence that the protocol requires be banked, and `manifest.py` indexes them as a separate class so a null about the case record is never satisfied by them.
- **documentation** is the research itself: 72 files declare a File ID, and the rest are roadmaps, audits, reviews, acquisition logs, the tracking documents, the kit, and 5 drafts/notes that live inside the raw bank.
- **tests: none.** The closest things are three self-checking entry points (§3.1), which is what Phase 2 will use as its regression check.
- **assets: none.** The 10 PNGs are evidence captures or rendered pages, not UI assets.
- **unknown: 1**, `BOC-E08_transcript-artifacts/yt_captions.json3`, which is zero bytes (a capture that failed silently).

---

## 3 · Entry points and the dependency graph

### 3.1 Scripts: what runs, what it reads, what it writes

| Script | Kind | Reads | Writes | Baseline today |
|---|---|---|---|---|
| `manifest.py` | maintained tool | every `**/*.md` (except the kit and its own output) and four artifact directories, hard-coded: the court bank, the 09-02 fetches, the TJR review bank, the Zinn bank | `SOURCE-MANIFEST.md`, `source-manifest.json` | not run (writes). ⚠ `--check` **also writes both files** and then exits 0; it is not a staleness check |
| `artifact_search.py` | maintained tool + importable module | `<bank>/*.txt`; `find()` is imported by instructions in 20 md files | nothing | ✅ audit ran: 17 U+FFFE/ligature hazards reported |
| `tsearch.py` | maintained tool | `<bank>/prelim-hearing-transcripts/day{1..5}.txt` | nothing | ✅ `--validate` passed (known positive found in day4) |
| `queue-check.sh` | maintained tool | `QUEUE.md`; greps all `*.md` for D-numbers and `[PROVISIONAL]`; counts bank PDFs/txts | nothing | ⚠ **exit 1** on two known conditions: 2 PDFs have no `.txt` sibling (the bindover order, no text layer; the redacted hearing transcript) and the working tree is dirty. This is the pre-existing baseline, not something Phase 2 introduces |
| `docket-watch-run.py` | maintained tool, network | DocumentCloud API, Wayback CDX, rev.com sitemap, utcourts news; `<bank>/docket-watch-baseline.json` | the baseline JSON; its report is pasted by hand into `CR-WATCH-log.md` | not run (network + writes). Its banner hard-codes "Next hard date: Tue 2026-08-18", four weeks stale |
| `migrate-files.sh` | utility | any dir | copies to a destination, verifies counts and bytes | not run |
| `tools/build-html.py`, `tools/build-docx.js` | build scripts | a markdown source (argv) | the HTML/DOCX renders | not run; **untracked**; `build-docx.js` requires the `docx` module by absolute Homebrew path |
| in-bank one-offs (4) | one-off | `sweep_extract.py` (BOC feed → episode table), `docket-artifacts_2026-08-16_NUL-repair.py` (rewrote NUL page separators, applied 08-16), two Workflow `.js` scripts (08-17 agent fan-outs) | their `*_RAW.json` / `_SUPERSESSION.json` outputs, which are cited | historical; all four hard-code the absolute repo path |

**Path coupling that Phase 2 must respect or fix.** The five root Python/shell tools locate the bank by a **cwd-relative** literal (`files - Court record/CR-ACQ-2026-07-27_court-record-artifacts`), so they only work when run from the repo root. `docket-watch-run.py` instead uses `dirname(__file__)`. `manifest.py` additionally excludes the kit by the prefix `VerificationAndFactCheckProtocol` and indexes the TJR review bank by path. Moving scripts into `scripts/` therefore needs a one-line root-resolution fix in each, and moving the kit or the TJR bank needs a string change in `manifest.py`.

### 3.2 The document graph

Inbound references were counted by scanning all 409 text files for each file's basename, DocumentCloud id, or declared File ID. The hubs:

| File | Files that reference it |
|---|---:|
| `QUEUE.md` | 84 |
| `CLAUDE.md` | 64 |
| `artifact_search.py` | 64 |
| `lance-twiggs-comprehensive-profile.md` | 57 |
| `files - Arrest chronology/robinson-surrender-timeline.md` | 52 |
| `DOCKET-WATCH.md` | 51 |
| `START-HERE.md` | 42 |
| `robinson-tyler-james-comprehensive-profile.md` (TJR-P01) | 38 |
| `tsearch.py` | 27 |
| `LOOP.md` | 25 |
| `queue-check.sh` | 23 |
| the mis-banked 23 MB PDF | 23 |

Three linking mechanisms coexist, and only one of them survives a move without edits:

| Mechanism | Count | Survives a folder move? |
|---|---:|---|
| Literal path in backticks, e.g. `` `files - Court record/CR-E08…` `` | 226 occurrences in 46 files | **No** |
| Markdown link with a path, often URL-encoded (`files%20-%20Court%20record/…`) | 137 | **No** |
| Bare filename or File ID (`CR-E19`, `day4.txt`, `lance-twiggs-comprehensive-profile.md`) | the majority of citations | **Yes** (and Obsidian resolves `[[name]]` by basename; the 161 `[[…]]` strings found are nearly all numeric footnote markers, only ~8 are real note links) |

### 3.3 External dependents (outside this folder)

| Dependent | What it names | Consequence |
|---|---|---|
| The deployed cloud routine `trig_016faLfbQWCz72M463Dy8HsL` (its prompt is mirrored in `DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md`) | `files - Court record/CR-WATCH-log.md`, `DOCKET-WATCH.md` | **These two files must not move.** Changing the routine is an owner-gated action |
| `~/.claude/settings.json` | the repo's absolute path, as the trusted repo | Path of the folder itself must not change |
| Obsidian vault `01 Projects/Kirk Robinson Research.md`, `AGENTS.md`, `02 Areas/Research Practice.md` | the repo by name and some root files | Root entry points stay |
| GitHub `JudicialNoticing/kirk-robinson-research` | remote of `main` | 11 local commits are not pushed (§5) |

### 3.4 Files referenced by nothing

51 files have no inbound reference by filename, id or File ID. Most are expected or are false positives of a filename-based scan:

- **Expected:** `.gitignore`, 5 `.obsidian/*`, `.claude/RESUME.md`, the `.pyc`, the 2 untracked `tools/*`.
- **Referenced at folder level, not by filename:** 17 captures in `BOC-ACQ-2026-07-20_F2-artifact-copies/` and 12 in its `neffmar/` sub-folder (the phase-0 pull log describes them by subject and names the folder), 4 files in `BOC-E08_transcript-artifacts/`.
- **False positive:** `files - Event security/2026-08-20_singju-srs254-harpole-transcript.txt` is cited by speaker and series name in four files.
- **Cited by their outputs instead:** the two Workflow `.js` scripts (their `*_RAW.json` results are cited), and the five newest `p5-*.json` logs in the TJR bank (the profile's revision log names the pass, not the file).
- **Genuinely dangling:** `yt_captions.json3` (0 bytes) and `tmp_at.html` (an archive.ph capture saved under a temp name).

---

## 4 · Problems found

### 4.1 Exact duplicates (byte-identical, by MD5)

| Group | Files | Assessment |
|---|---|---|
| Kit drop file | `VerificationAndFactCheckProtocol copy/COMPLETE-DROP-FILE.md` = `…/research-verification-kit/COMPLETE-DROP-FILE.md` | Real duplicate. The inner one is the copy the kit's own `MANIFEST.md` hashes; the outer one goes to `archive/` |
| Same court document under two DocumentCloud ids | `2025-09-16_5_dc26099252.txt` = `2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.txt` | Both ids are cited (23 and more). Keep both; note in INDEX |
| Same motion under three ids | `2026-04-02_motion-vacate-continue-march-27-2026_dc27998184/88/89.txt` | Three DocumentCloud postings of one filing; all cited. Keep |
| Court-site fetches returning one body | 5 `legacy.utcourts.gov_utc_news_*.html`; 8 `www.utcourts.gov_*.html.html`; `probe_media.html` = `ua_media.html`; `ua.html` = `ucao_k.html` | Legitimate: different URLs answered with the same page on 2026-09-02, and the folder's `MANIFEST.md` records each fetch. Keep |
| `.obsidian/app.json` = `appearance.json` | both are `{}` | Trivial |

### 4.2 Stale copies and version series

- **Six versions of the docket-watch routine prompt at the root.** `LIVE-2026-08-29` is the deployed text; `DRAFT-2026-09-14` is the pending replacement; the 08-14, 08-16, 08-17 and 09-02 drafts are each superseded by the next (they say so in their headers). The older four → `archive/`.
- **Thirteen frozen snapshots** `profile_v1.0 … v2.3` in the TJR bank. Intentional: each is the pre-correction state of the profile, banked so a correction pass can be audited. They are generated and must never be edited; they travel with the bank.
- **The kit exists three times:** extracted (indexed, hash-verified), as the outer duplicate drop file, and as the original `.zip`. Only the extracted copy is needed.
- **Derived transcript views** `day2/3/5_condensed.txt`, `faumuina_condensed.txt` (2026-07-27) are cited 18–43 times each and stay.

### 4.3 Abandoned or dangling

| Item | Why it looks abandoned | Recommendation |
|---|---|---|
| `…artifacts/2026-08-01_BLOCKED-DRAFT_q08-dna_DO-NOT-PUBLISH.md` | Header: legal/ethical review returned DO_NOT_PUBLISH; the file ends mid-sentence; superseded by `DNA-E01` v4.9 | Cannot move: **89 files** cite it by path as the record of the blocked attempt. Leave; list in INDEX as superseded (❓ Q8) |
| `…artifacts/2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md` | Adversarial review never completed; declares a File ID `LOSEE-E01` that was **never ratified** (pending Q-62) | Leave in place (10 referrers); flag the unratified ID in INDEX |
| `…artifacts/2026-08-14_Q61-candidate-bank_INDEX.md` + 4 `*_RAW-CANDIDATES.jsonl` | A harvest of candidates that "NOTHING HERE MAY BE CITED"; the verification stage never ran | Leave (process evidence); note in INDEX |
| `yt_captions.json3` | 0 bytes | ❓ leave as evidence of a failed capture, or archive |
| `tmp_at.html` | temp name, uncited | Leave; naming noted |
| `.claude/RESUME.md` | Harness checkpoint from a 2026-08-17 session, ignored via `.git/info/exclude` only | ❓ Q11: move to `~/.Trash` |
| Two local branches `forensic-exhibit-map-and-print-null-2026-08-30`, `limits-resolution-2026-08-30` | Fully merged into `main` | ❓ Q10: delete the branch refs (not files) |
| `docket-watch-run.py` banner | Hard-codes "Next hard date: Tue 2026-08-18" | Fix the string in Phase 2 (allowed: it is a path/label, not logic) |

### 4.4 Generated files committed alongside source

| File(s) | Verdict |
|---|---|
| `__pycache__/artifact_search.cpython-314.pyc` | Accident. Untrack and ignore |
| `Tyler-Robinson_Comprehensive-Profile_2026-09-14.html`, `.docx` | Regenerable from the markdown with `tools/`; committed as shareable deliverables and currently **modified but uncommitted** (rebuilt 22:57 on 09-14, after the v2.4 commit). → `deliverables/`, keep tracked (❓ Q7) |
| `Forensic-Sampling-Summary_2026-08-30.docx` | Not regenerable (no markdown source). → `deliverables/`, keep tracked |
| `SOURCE-MANIFEST.md`, `source-manifest.json` | Generated by design ("DO NOT EDIT, re-run manifest.py"). Stay tracked at root because 14 and 17 files cite them and `manifest.py` writes there |
| 13 `profile_v*.md` snapshots, `atf_page-26…29.png`, `*_SUPERSESSION.json`, `*_bank_receipts.json`, `docket-watch-baseline.json` | Generated but intentionally banked as process evidence or as the readable form of an illegible PDF. Stay |

### 4.5 Hard-coded absolute paths

| File | Path | Impact |
|---|---|---|
| `…/BOC-ROUTE-2026-07-27_artifacts/sweep_extract.py` | `~/Documents/Kirk Robinson Research/files - Bride of Charlie series/…/feed.xml` | one-off, historical |
| `…artifacts/docket-artifacts_2026-08-16_NUL-repair.py` | `~/Documents/Kirk Robinson Research/…` | one-off, applied 08-16 |
| `…artifacts/2026-08-17_Q137-Q138-workflow-script.js`, `…SEC-E01-workflow-script.js` | `const ROOT = '~/Documents/Kirk Robinson Research'` | one-off Workflow scripts |
| `tools/build-docx.js` | `/opt/homebrew/lib/node_modules/docx` | machine-specific; fix to `require('docx')` with `NODE_PATH`, or document |
| `…artifacts/2026-08-16_Q140-twiggs-analytic-pass_RAW.md` | absolute path inside a banked agent report | historical record, leave |

The four in-bank scripts are records of what was run and are cited; **they will not be edited.** The root tools use cwd-relative paths instead, which is the opposite fragility (they break when run from anywhere else).

### 4.6 Secrets and credentials

**None found.** A scan for key/token/password/bearer/private-key patterns across all text files hit only third-party HTML captured as evidence (Twitter login forms from 2012–2017 snapshots, an AP page's public `apiKey=apnews.com` analytics parameter). Eight distinct email addresses appear, all public court, counsel or outlet addresses printed inside banked court filings; none belongs to the owner. No `.env`, no key files. The routine identifier `trig_016faLfbQWCz72M463Dy8HsL` appears in three tracking files; it is an object id, not a credential.

### 4.7 Missing or misleading documentation

| Document | Problem |
|---|---|
| `README.md` (2026-07-28) | Lists 6 of the 8 topic folders and **omits `files - Court record/`, which is 363 files and 102 MB, and `files - Event security/`**. Names 2 of 8 tools. Says nothing about `SOURCE-MANIFEST`, `VERIFICATION-PROTOCOL.md`, the TJR profile, the deliverables, or the `TJR-REVIEW` bank |
| `START-HERE.md` | Header says "Written: 2026-08-01"; the body carries dated sections through 2026-09-02 and **nothing for the 2026-09-14 session** (the TJR profile, the kit adoption, the bindover order acquisition). Its own text says it is stale after 09-01 |
| `QUEUE.md` | Header "Last updated 2026-08-17" against content through 08-30; **no entry for TJR-P01** or the 09-14 work |
| `robinson-tyler-james-comprehensive-profile.md` | Three defects in its executive summary survived eleven versions: a leaked agent instruction printed as body text (line 37), a duplicated sentence (line 35), a garbled splice (line 43). Propagated into both renders. Found 2026-09-15; not a reorganisation matter but it is the document a new reader opens first (❓ Q5 offers to fix it alongside the move) |
| `CLAUDE.md`, `VERIFICATION-PROTOCOL.md` | Cite the kit at `VerificationAndFactCheckProtocol copy/research-verification-kit/`; must be updated if the kit moves |
| `LOOP.md` v1.0 (2026-07-28) | Describes a loop that, per the project's own memory, has never run; still accurate as protocol |
| No `INDEX.md`, no architecture note, no glossary | The conventions (tiers, D/V/F/M/Q numbers, labels, `[PROVISIONAL]`, the "T1 via T3" rule) are defined only inside `CLAUDE.md` and the kit |

### 4.8 Naming conventions (three generations coexist)

- **ID-prefixed** (current standard): `CR-E19_latent-print-record.md`, `BOC-E01_…`, `SEC-E01_…`.
- **Pre-ID descriptive**: `robinson-surrender-timeline.md`, `zinn-george-evidence.md`, `kirk-shooting-official-timeline.md`, and the roadmap spelled four ways: `tier1-acquisition-roadmap.md`, `t1 source acquisition roadmap - George Zinn.md`, `tier1 source acquisition roadmap - forensic evidence for Losee building shot.md`, `Kirk-Robinson_DNA-Evidence_Acquisition-Roadmap_2026-07-15.md`.
- **Bank files**: the `YYYY-MM-DD_slug_dktN_dcID` scheme beside ad-hoc names (`oct24_clean.txt`, `tyler-robinson-ballistics-motion.pdf`, `tyler-robinson-redacted-hearing-transcript.pdf`).

**No renames are proposed** for any cited file (namespace freeze). `INDEX.md` will map every file to its role so the inconsistency stops mattering.

---

## 5 · Git

| Check | Result |
|---|---|
| Repository | Yes. `main`, 148 commits (2026-07-26 → 2026-09-14). Remote `origin` = `github.com/JudicialNoticing/kirk-robinson-research` |
| Tracked | 493 files |
| Untracked, not ignored | `tools/build-html.py`, `tools/build-docx.js` |
| Modified, uncommitted | the two profile renders (rebuilt after the last commit) |
| Ignored and present | `.DS_Store`, `.obsidian/workspace.json`, `.obsidian/graph.json` (via `.gitignore`); `.claude/RESUME.md` (via `.git/info/exclude`, which **does not travel with a clone**) |
| Tracked junk | `__pycache__/artifact_search.cpython-314.pyc` |
| `.gitignore` coverage | Four lines. Missing: `__pycache__/`, `*.pyc`, `.claude/` (or `RESUME.md`), `*.pyo`. Working as intended for Obsidian state |
| Large tracked blobs | 6 files over 2 MB; largest 24.3 MB (the contaminant PDF). All under GitHub's limits |
| **Unpushed** | **`main` is 11 commits ahead of `origin/main`.** The entire 2026-09-14 session (kit adoption, TJR-P01 and its verification bank, the bindover order) exists on this machine only. START-HERE lists "push main" as an owner action |
| Branches | `forensic-exhibit-map-and-print-null-2026-08-30`, `limits-resolution-2026-08-30`: both fully merged into `main` |

---

## 6 · Noticed, out of scope for the reorganisation

- The docket watch's three September firings ran dark and were transcribed on 09-14 (`CR-WATCH-log.md` v2.4); the pending prompt draft (09-14) is unapplied. Owner-gated, unchanged by this plan.
- Neither `START-HERE.md` nor `QUEUE.md` knows the TJR profile exists; the write-back for 2026-09-14 was never done. Phase 2's INDEX/README will point at it, but the tracking docs still owe a session row.

---

## 7 · Proposed target structure

### 7.1 The one design principle: freeze the citation namespace

The user's template (`src/`, `data/raw/`, `data/processed/`, `notebooks/`) is adapted as follows, and the adaptation is the whole plan:

- **`files - <Topic>/` folders keep their names and stay at the root.** They are `data/raw` + `docs` fused, and 46 verified files cite into them by literal path. Renaming them to `data/raw/court-record/` would mean rewriting 226 path strings inside files that carry revision logs, or leaving the citations broken. Neither is acceptable for a research record.
- **Nothing inside an artifact bank moves**, including the eight non-artifact files that live in the court bank (❓ Q8). This is the `data/raw` rule applied literally.
- **Evidence-file bodies are not edited.** Phase 2 edits path strings only in the *live* documents (`README`, `START-HERE`, `QUEUE`, `LOOP`, `DOCKET-WATCH`, `CLAUDE.md`, `VERIFICATION-PROTOCOL.md`) and in scripts. Historical references to `./tsearch.py` inside dated audits are records of what was run and stay as written. The one exception is ❓ Q5.
- **Everything that is not evidence moves out of the root** into six new top-level folders.

### 7.2 Target tree

```
Kirk Robinson Research/
├── README.md                     rewritten: what this is, how to run the tools, where to start reading
├── INDEX.md                      NEW: every significant file, one sentence each, when you'd need it
├── AUDIT.md                      this file
├── CLAUDE.md                     stays (path to the kit updated)
├── VERIFICATION-PROTOCOL.md      stays (path to the kit updated)
├── START-HERE.md · QUEUE.md · LOOP.md · DOCKET-WATCH.md      stay (entry points; named by the cloud routine)
├── SOURCE-MANIFEST.md · source-manifest.json                 stay (generated; regenerated at the end of Phase 2)
├── .gitignore                    extended
│
├── docs/
│   ├── ARCHITECTURE.md           NEW: how the pieces fit, data flow from acquisition → bank → evidence file → register → deliverable
│   ├── DECISIONS.md              NEW: why things are the way they are, inferences marked as such
│   ├── GLOSSARY.md               NEW: tiers, labels, D/V/F/M/Q numbers, [PROVISIONAL], "T1 via T3", U+FFFE, the contaminant …
│   ├── VERIFICATION-KIT-INDEX.md         ← "VerificationAndFactCheckProtocol copy/"
│   └── research-verification-kit/        ← the 10 indexed kit files, layout unchanged (its MANIFEST.md still verifies)
│
├── scripts/                      ← manifest.py, artifact_search.py, tsearch.py, docket-watch-run.py,
│                                   queue-check.sh, migrate-files.sh, build-html.py, build-docx.js
│                                   (each made repo-root-aware; each already has a docstring/usage header)
│
├── ops/
│   └── docket-watch/             ← DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md, …-DRAFT-2026-09-14.md
│
├── deliverables/                 ← the two TJR-P01 renders, Forensic-Sampling-Summary_2026-08-30.docx
│
├── verification/
│   └── TJR-REVIEW-2026-09-14_verification-cycle-1/   ← from files - Court record/ (❓ Q5)
│
├── archive/
│   ├── README.md                 NEW: what is here and why
│   ├── docket-watch-prompts/     ← the four superseded DRAFTs (08-14, 08-16, 08-17, 09-02)
│   └── verification-kit-drop/    ← the outer COMPLETE-DROP-FILE.md duplicate, research-verification-kit.zip
│
├── files - Arrest chronology/            unchanged
├── files - Bride of Charlie series/      unchanged
├── files - Court record/                 unchanged except the TJR-REVIEW bank leaving (Q5)
├── files - DNA evidence/                 unchanged
├── files - Event security/               unchanged
├── files - George Zinn/                  unchanged
├── files - Kirk assassination questions/ + evidence-rifle-photo-nypost-authenticity.md (❓ Q4)
├── files - Losee building/               unchanged
├── files - Person profiles/              NEW: TJR-P01, the Twiggs profile, the Erika Kirk dossier (❓ Q3)
│
└── .obsidian/  .claude/                  unchanged
```

Root file count: 30 → 12 (plus `.DS_Store`).

### 7.3 What Phase 2 would edit (and nothing else)

| File | Edit |
|---|---|
| `scripts/*.py`, `scripts/*.sh` | resolve the repo root from `__file__`/`$0` instead of cwd; `manifest.py`: kit prefix, TJR bank path, output paths; `docket-watch-run.py`: baseline path, stale banner string; `build-docx.js`: module path |
| `CLAUDE.md`, `VERIFICATION-PROTOCOL.md` | kit path; the `tsearch.py`/`migrate-files.sh` mentions |
| `README.md` | rewritten |
| `START-HERE.md`, `QUEUE.md`, `LOOP.md`, `DOCKET-WATCH.md` | only literal `./tool` invocations and root-file paths that move; **no content changes**; one dated note each |
| `SOURCE-MANIFEST.md`, `source-manifest.json` | regenerated by `manifest.py` |
| `.gitignore` | add `__pycache__/`, `*.pyc`, `.claude/RESUME.md` |
| `robinson-tyler-james-comprehensive-profile.md` | **only if Q5 is approved:** the 10 path references to the TJR bank, as one v2.5 revision row |
| New: `INDEX.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/GLOSSARY.md`, `archive/README.md` | created |

Not edited: any `files - <Topic>/*.md` evidence, audit, review or roadmap file; anything in a bank; any frozen snapshot.

### 7.4 Phase 2 commit plan (one commit per group, all moves via `git mv`)

1. `chore: gitignore + untrack bytecode; bring tools/ under scripts/`
2. `scripts/: move the six root tools, make them root-aware` → run `tsearch.py --validate`, `artifact_search.py`, `queue-check.sh`, `manifest.py` (dry: diff the regenerated manifest against the committed one; counts must stay 294 artifacts / 17 hazards)
3. `docs/: move the verification kit; update CLAUDE.md and VERIFICATION-PROTOCOL.md` → verify the kit's `MANIFEST.md` hashes still match (9/9)
4. `archive/: superseded routine-prompt drafts and the kit drop duplicates; archive/README.md`
5. `ops/docket-watch/: LIVE and current DRAFT prompt`
6. `deliverables/: the three rendered outputs` (commit the pending render changes first, as they are)
7. `files - Person profiles/: the three dossiers; rifle-photo file to its topic folder` (if Q3/Q4 approved)
8. `verification/: the TJR review bank; manifest.py path; TJR-P01 v2.5 row` (if Q5 approved)
9. `docs: README rewrite, INDEX.md, ARCHITECTURE.md, DECISIONS.md, GLOSSARY.md`
10. `regenerate SOURCE-MANIFEST; final baseline run` → the same four checks as step 2, plus `git status` clean

After each move group I will re-grep for the *old* path of everything moved and report any reference I did not update, by file, so nothing is silently left pointing at an old location.

### 7.5 Mapping summary (every path is in Appendix C)

| Current | Proposed | Files | Reason |
|---|---|---:|---|
| `*.py`, `*.sh` at root; `tools/*` | `scripts/` | 8 | one place for tooling (❓ Q2) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/**`, `…/VERIFICATION-KIT-INDEX.md` | `docs/research-verification-kit/**`, `docs/VERIFICATION-KIT-INDEX.md` | 11 | methodology belongs in docs; kit layout preserved |
| `…copy/COMPLETE-DROP-FILE.md`, `…copy/research-verification-kit.zip` | `archive/verification-kit-drop/` | 2 | duplicate + redundant archive |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14/16/17, 09-02` | `archive/docket-watch-prompts/` | 4 | superseded |
| `…-LIVE-2026-08-29.md`, `…-DRAFT-2026-09-14.md` | `ops/docket-watch/` | 2 | deployed config text (❓ Q6) |
| the three person dossiers at root | `files - Person profiles/` | 3 | give them a topic folder (❓ Q3) |
| `evidence-rifle-photo-nypost-authenticity.md` | `files - Kirk assassination questions/` | 1 | nearest topic (❓ Q4) |
| the two renders + the sampling summary | `deliverables/` | 3 | outputs, not sources (❓ Q7) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/**` | `verification/…` | 59 | process evidence out of the evidence folder (❓ Q5) |
| `__pycache__/*.pyc` | untracked, ignored | 1 | accident |
| everything else | stays | 405 | evidence, banks, entry points, config |

---

## 8 · Questions for you

Each is marked in Appendix C. My recommendation is first.

- **❓ Q1 — Approve the namespace freeze?** Keep `files - <Topic>/` names and bank contents exactly as they are, reorganising around them (recommended). The alternative, a literal `data/raw/…` layout, costs about 226 path rewrites in 46 verified files plus a revision-log row in each, and I would advise against it.
- **❓ Q2 — Move the six root tools into `scripts/`?** Yes (recommended). Live docs get updated; the 12–20 historical mentions of `./tsearch.py` and `artifact_search.py` inside dated audit and evidence files are left as records. Alternative: keep the tools at the root and only fold `tools/` into them.
- **❓ Q3 — Create `files - Person profiles/` for TJR-P01, the Twiggs profile and the Erika Kirk dossier?** Yes (recommended). They are cited by bare filename, so nothing breaks; `README`, `QUEUE` and `CLAUDE.md` mentions get the folder added.
- **❓ Q4 — Where does `evidence-rifle-photo-nypost-authenticity.md` go?** `files - Kirk assassination questions/` (recommended), or a new `files - Rifle photo/`, or stay at root.
- **❓ Q5 — Move the TJR verification bank to `verification/`, and fix the three executive-summary defects in the same v2.5 revision row?** Yes to both (recommended). This is the only edit to an evidence-file body in the plan. Alternative: move only, or leave the bank where it is.
- **❓ Q6 — `ops/docket-watch/` for the LIVE and current DRAFT prompt files?** Yes (recommended). The cloud routine holds its own copy, so nothing external breaks.
- **❓ Q7 — Deliverables: keep the HTML/DOCX renders tracked in `deliverables/`?** Yes (recommended), and commit the pending rebuilt renders as they are before moving them. Alternative: ignore the renders and regenerate on demand (the sampling summary has no source and must stay tracked regardless).
- **❓ Q8 — The eight non-artifact files inside the court bank** (two DO-NOT-PUBLISH drafts, three `_RAW.md` reports, the Q61 index, one Python and two JS scripts): leave in place (recommended, because 89 files cite the DNA draft by its bank path), or move them to `archive/` and rewrite those citations.
- **❓ Q9 — The 23 MB mis-banked contaminant PDF and its `.txt`:** leave (recommended; 23 citations and the `queue-check.sh` arithmetic depend on its presence), or move to `archive/` and adjust the script.
- **❓ Q10 — Before Phase 2 starts: push the 11 unpushed commits, and delete the two merged local branches?** Both are yours to do; I recommend pushing first so the reorganisation is never the only copy of the September work.
- **❓ Q11 — `.claude/RESUME.md`:** move to `~/.Trash` (recommended; stale harness checkpoint outside git), or leave.

---

## Appendix A · Full tree with sizes

Directories show file count and total size; the one file over 10 MB is flagged.

```
📁 ./  — 499 files, 116.6 MB (excluding .git, 58 MB)
  📁 .claude/  — 1 files, 694 B
    RESUME.md  (694 B)
  📁 .obsidian/  — 5 files, 5.7 KB
    app.json  (2 B)
    appearance.json  (2 B)
    core-plugins.json  (696 B)
    graph.json  (494 B)
    workspace.json  (4.6 KB)
  📁 VerificationAndFactCheckProtocol copy/  — 13 files, 237.8 KB
    📁 research-verification-kit/  — 10 files, 120.7 KB
      📁 background/  — 3 files, 29.3 KB
        chain-of-thought-verification.md  (13.3 KB)
        fact-checking-assistant-prompt.md  (946 B)
        faithfulness-metrics.md  (15.1 KB)
      📁 prompts/  — 1 files, 8.7 KB
        02-prompt-pack.md  (8.7 KB)
      📁 protocols/  — 1 files, 9.3 KB
        01-research-protocols.md  (9.3 KB)
      📁 schemas/  — 1 files, 2.6 KB
        03-claim-card-and-log.md  (2.6 KB)
      00-doctrine-and-router.md  (4.4 KB)
      COMPLETE-DROP-FILE.md  (61.4 KB)
      MANIFEST.md  (1.2 KB)
      README.md  (3.6 KB)
    COMPLETE-DROP-FILE.md  (61.4 KB)
    VERIFICATION-KIT-INDEX.md  (1.0 KB)
    research-verification-kit.zip  (54.6 KB)
  📁 __pycache__/  — 1 files, 7.4 KB
    artifact_search.cpython-314.pyc  (7.4 KB)
  📁 files - Arrest chronology/  — 2 files, 49.5 KB
    robinson-surrender-timeline.md  (34.4 KB)
    tier1-acquisition-roadmap.md  (15.1 KB)
  📁 files - Bride of Charlie series/  — 61 files, 12.3 MB
    📁 BOC-ACQ-2026-07-20_F2-artifact-copies/  — 30 files, 4.6 MB
      📁 neffmar/  — 12 files, 354.2 KB
        2028271192042586183.json  (7.2 KB)
        2028271884647944515.json  (138.9 KB)
        2028287292922814792.json  (138.9 KB)
        2028429731729977830.json  (9.9 KB)
        2028520462108799255.json  (6.6 KB)
        2028556678283853959.json  (4.5 KB)
        2028577525149139216.json  (7.4 KB)
        2028621723608989835.json  (10.0 KB)
        2028624883417219159.json  (5.7 KB)
        2028634485651378634.json  (6.7 KB)
        2028642700841615563.json  (7.8 KB)
        2028689687028846716.json  (10.5 KB)
      aurora_tweet.png  (491.0 KB)
      cdx_neff_tw.json  (193.8 KB)
      cdx_neff_x.json  (31.4 KB)
      cocopah_20170130.html  (358.0 KB)
      cocopah_tweet.png  (245.4 KB)
      ef_20151022.html  (254.6 KB)
      factually.html  (5.7 KB)
      frantzve_bio_20240612.html  (381.8 KB)
      img_07049361.png  (301.6 KB)
      img_57d2149a.png  (344.2 KB)
      img_8c35c695.png  (351.4 KB)
      img_8f838a9d.png  (624.4 KB)
      missaz_20121112.html  (184.7 KB)
      neff_20260629.json  (13.9 KB)
      primetimer_shabbat.html  (43.5 KB)
      rmazusa_status_2011.html  (50.6 KB)
      substack_e06.html  (388.7 KB)
      tmp_at.html  (54.2 KB)
    📁 BOC-E08_transcript-artifacts/  — 12 files, 4.6 MB
      caption_tracks.json  (546 B)
      feed.xml  (1.9 MB)
      happyscribe_raw.html  (5.7 KB)
      podscripts_extract.txt  (51.3 KB)
      podscripts_raw.html  (441.4 KB)
      podwave_extract.txt  (49.5 KB)
      podwave_raw.html  (281.5 KB)
      rumble_raw.html  (510.1 KB)
      transcript_primary.txt  (52.7 KB)
      transcript_secondary.txt  (50.6 KB)
      yt_captions.json3  (0 B)
      yt_watch.html  (1.2 MB)
    📁 BOC-ROUTE-2026-07-27_artifacts/  — 3 files, 2.5 MB
      cia_directors_gallery_20260727.html  (570.4 KB)
      feed_20260727.xml  (2.0 MB)
      sweep_extract.py  (1.1 KB)
    BOC-ACQ-2026-07-19_phase0-pull-log.md  (108.3 KB)
    BOC-AUDIT-2026-07-18B_library-audit.md  (21.5 KB)
    BOC-AUDIT-2026-07-18_library-audit.md  (10.3 KB)
    BOC-AUDIT-2026-07-20_session-audit.md  (16.5 KB)
    BOC-AUDIT-2026-07-27B_adversarial-pass.md  (12.5 KB)
    BOC-AUDIT-2026-07-27_session-audit.md  (39.5 KB)
    BOC-E01_Wrinkle-in-Time_claim-inventory.md  (33.1 KB)
    BOC-E02_Dr-Jerri-and-Mrs-Hyde_claim-inventory.md  (31.9 KB)
    BOC-E03_Have-No-Fear-Lori-Is-Here_claim-inventory.md  (45.2 KB)
    BOC-E04_The-Ties-That-Bind_claim-inventory.md  (27.7 KB)
    BOC-E05_The-Lost-Years_claim-inventory.md  (39.2 KB)
    BOC-E06_What-Happened-In-Romania_claim-inventory.md  (50.7 KB)
    BOC-E07_Crazy-In-Love_claim-inventory.md  (54.9 KB)
    BOC-E08_Red-Sparrow_claim-inventory.md  (80.8 KB)
    BOC-ROUTE-2026-07-27_post-series-case-claims-corpus.md  (37.0 KB)
    BOC-T1_Tier1-Acquisition-Roadmap_all-episodes.md  (48.3 KB)
  📁 files - Court record/  — 363 files, 101.1 MB
    📁 CR-ACQ-2026-07-27_court-record-artifacts/  — 179 files, 74.4 MB
      📁 prelim-hearing-transcripts/  — 16 files, 5.3 MB
        2026-09-01_final-prelim-argument.txt  (232.0 KB)
        2026-09-01_final-prelim-argument_raw.html  (461.0 KB)
        day1.txt  (319.8 KB)
        day1_raw.html  (821.0 KB)
        day2.txt  (315.7 KB)
        day2_condensed.txt  (288.1 KB)
        day2_raw.html  (769.9 KB)
        day3.txt  (130.5 KB)
        day3_condensed.txt  (124.3 KB)
        day3_raw.html  (357.2 KB)
        day4.txt  (305.5 KB)
        day4_raw.html  (756.3 KB)
        day5.txt  (105.7 KB)
        day5_condensed.txt  (99.2 KB)
        day5_raw.html  (320.7 KB)
        faumuina_condensed.txt  (71.3 KB)
      2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.pdf  (97.5 KB)
      2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.txt  (1.6 KB)
      2025-09-12_public-safety-assessment-report_dkt3_dc27880877.pdf  (719.4 KB)
      2025-09-12_public-safety-assessment-report_dkt3_dc27880877.txt  (3.4 KB)
      2025-09-16_5_dc26099252.pdf  (378.5 KB)
      2025-09-16_5_dc26099252.txt  (8.3 KB)
      2025-09-16_affidavit-of-probable-cause_dc27880530.pdf  (77.3 KB)
      2025-09-16_affidavit-of-probable-cause_dc27880530.txt  (10.3 KB)
      2025-09-16_bail-order_dkt4_dc27880869.pdf  (707.8 KB)
      2025-09-16_bail-order_dkt4_dc27880869.txt  (700 B)
      2025-09-16_information-charging-document_dc27880532.pdf  (277.9 KB)
      2025-09-16_information-charging-document_dc27880532.txt  (21.8 KB)
      2025-09-16_pretrial-protective-order_dkt14_dc27880872.pdf  (770.0 KB)
      2025-09-16_pretrial-protective-order_dkt14_dc27880872.txt  (8.1 KB)
      2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.pdf  (378.5 KB)
      2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.txt  (8.3 KB)
      2025-09-16_request-designation-victim-representative_dkt12_dc27880865.pdf  (94.8 KB)
      2025-09-16_request-designation-victim-representative_dkt12_dc27880865.txt  (1.6 KB)
      2025-09-22_prosecutor-chad-grunander-biography_dc27880539.pdf  (160.1 KB)
      2025-09-22_prosecutor-chad-grunander-biography_dc27880539.txt  (2.1 KB)
      2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.pdf  (190.3 KB)
      2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.txt  (2.0 KB)
      2025-09-22_prosecutor-david-sturgill-biography_dc27880538.pdf  (146.6 KB)
      2025-09-22_prosecutor-david-sturgill-biography_dc27880538.txt  (1.7 KB)
      2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.pdf  (220.8 KB)
      2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.txt  (2.3 KB)
      2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.pdf  (187.8 KB)
      2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.txt  (1.4 KB)
      2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.pdf  (180.3 KB)
      2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.txt  (2.1 KB)
      2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.pdf  (768.7 KB)
      2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.txt  (782 B)
      2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.pdf  (128.2 KB)
      2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.txt  (553 B)
      2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.pdf  (115.0 KB)
      2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.txt  (2.1 KB)
      2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.pdf  (118.5 KB)
      2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.txt  (2.1 KB)
      2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.pdf  (133.4 KB)
      2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.txt  (1.3 KB)
      2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.pdf  (169.1 KB)
      2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.txt  (5.6 KB)
      2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.pdf  (439.6 KB)
      2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.txt  (10.6 KB)
      2025-10-22_state-motion-to-set-aside-order_dc27880864.pdf  (167.0 KB)
      2025-10-22_state-motion-to-set-aside-order_dc27880864.txt  (3.4 KB)
      2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.pdf  (174.7 KB)
      2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.txt  (11.4 KB)
      2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.pdf  (3.3 MB)
      2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.txt  (14.2 KB)
      2025-10-27_state-open-file-policy-notice_dc27880871.pdf  (162.2 KB)
      2025-10-27_state-open-file-policy-notice_dc27880871.txt  (2.0 KB)
      2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.pdf  (135.1 KB)
      2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.txt  (3.4 KB)
      2025-11-04_stipulated-order-preserve-evidence_dc27880862.pdf  (742.1 KB)
      2025-11-04_stipulated-order-preserve-evidence_dc27880862.txt  (2.8 KB)
      2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.pdf  (185.5 KB)
      2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.txt  (10.1 KB)
      2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.pdf  (49.3 KB)
      2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.txt  (1.3 KB)
      2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.pdf  (216.9 KB)
      2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.txt  (15.6 KB)
      2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.pdf  (228.1 KB)
      2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.txt  (3.4 KB)
      2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.pdf  (2.6 MB)
      2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.txt  (33.1 KB)
      2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.pdf  (54.6 KB)
      2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.txt  (622 B)
      2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.pdf  (4.3 MB)
      2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.txt  (49.2 KB)
      2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.pdf  (141.0 KB)
      2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.txt  (10.4 KB)
      2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.pdf  (164.8 KB)
      2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.txt  (8.1 KB)
      2026-01-19_4_dc26493871.pdf  (97.3 KB)
      2026-01-19_4_dc26493871.txt  (1.9 KB)
      2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.pdf  (868.8 KB)
      2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.txt  (5.0 KB)
      2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.pdf  (211.8 KB)
      2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.txt  (20.6 KB)
      2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.pdf  (141.5 KB)
      2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.txt  (3.0 KB)
      2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.pdf  (167.2 KB)
      2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.txt  (5.2 KB)
      2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.pdf  (218.3 KB)
      2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.txt  (22.4 KB)
      2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.pdf  (712.4 KB)
      2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.txt  (5.1 KB)
      2026-03-15_xchange-case-history-full_dc27880531.pdf  (57.9 KB)
      2026-03-15_xchange-case-history-full_dc27880531.txt  (70.7 KB)
      2026-03-15_xchange-short-case-history_dc27880533.pdf  (27.6 KB)
      2026-03-15_xchange-short-case-history_dc27880533.txt  (42.4 KB)
      2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.pdf  (244.8 KB)
      2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.txt  (472 B)
      2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.pdf  (386.8 KB)
      2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.txt  (788 B)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.pdf  (1.5 MB)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.txt  (110.1 KB)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.pdf  (1.5 MB)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.txt  (110.1 KB)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.pdf  (1.5 MB)
      2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.txt  (110.1 KB)
      2026-06-23-pub_rev-contempt-hearing-transcript.html  (201.3 KB)
      2026-06-23-pub_rev-contempt-hearing-transcript.txt  (36.0 KB)
      2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.pdf  (122.8 KB)
      2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.txt  (7.6 KB)
      2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.pdf  (23.1 MB)  ⚠ >10 MB
      2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt  (1.1 MB)
      2026-07-08_supplemental-notice-access-to-evidence_dc28443912.pdf  (561.5 KB)
      2026-07-08_supplemental-notice-access-to-evidence_dc28443912.txt  (5.0 KB)
      2026-08-01_BLOCKED-DRAFT_q08-dna_DO-NOT-PUBLISH.md  (162.9 KB)
      2026-08-01_Q58-completion-60-verdicts.json  (447.5 KB)
      2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md  (106.2 KB)
      2026-08-01_q08-reviews-and-register-proposal.json  (98.8 KB)
      2026-08-01_round2-Q58-raw-output.json  (468.5 KB)
      2026-08-01_verification-cycle-raw-output.json  (1.0 MB)
      2026-08-01_verification-cycle-workflow-result.json  (1.1 MB)
      2026-08-11_defendant-prelim-hearing-briefing.pdf  (380.0 KB)
      2026-08-11_defendant-prelim-hearing-briefing.txt  (91.2 KB)
      2026-08-11_defendant-prelim-hearing-briefing_ALT-EXTRACTION-dc28551955.txt  (92.0 KB)
      2026-08-14_CRE07-completeness-inventory_RAW-CANDIDATES.jsonl  (428.3 KB)
      2026-08-14_CRE08-completeness-state-filings_RAW-CANDIDATES.jsonl  (270.9 KB)
      2026-08-14_Q61-candidate-bank_INDEX.md  (13.6 KB)
      2026-08-14_Q61-completeness-day2-bakker_RAW-CANDIDATES.jsonl  (628.5 KB)
      2026-08-14_Q61-completeness-day5-oliver_RAW-CANDIDATES.jsonl  (728.6 KB)
      2026-08-14_Q61-finder-DNAE01-sections6-14_RAW-CANDIDATES.jsonl  (570.9 KB)
      2026-08-16_Q140-twiggs-analytic-pass_RAW.md  (507.6 KB)
      2026-08-16_Q70-completion-six-reader-reports_RAW.md  (186.8 KB)
      2026-08-16_rev-q120-acquisition_RECEIPTS.json  (1.6 KB)
      2026-08-16_rev-q120-bodies.json  (1.4 KB)
      2026-08-16_rev_fbi-captures-kirk-shooter.txt  (27.0 KB)
      2026-08-16_rev_fbi-captures-kirk-shooter_raw.html  (203.5 KB)
      2026-08-16_rev_fbi-press-conference-on-kirk-shooting.txt  (11.1 KB)
      2026-08-16_rev_fbi-press-conference-on-kirk-shooting_raw.html  (177.7 KB)
      2026-08-16_rev_press-conference-on-charlie-kirk-shooting.txt  (13.3 KB)
      2026-08-16_rev_press-conference-on-charlie-kirk-shooting_raw.html  (184.2 KB)
      2026-08-16_rev_update-on-charlie-kirk-shooter.txt  (31.2 KB)
      2026-08-16_rev_update-on-charlie-kirk-shooter_raw.html  (207.5 KB)
      2026-08-17_Q136-zinn-reconciliation_RAW.json  (395.6 KB)
      2026-08-17_Q137-Q138-person-files_RAW.json  (1.2 MB)
      2026-08-17_Q137-Q138-workflow-script.js  (34.2 KB)
      2026-08-17_Q142-Q143-Q144-Q145-twiggs-programme_RAW.json  (907.1 KB)
      2026-08-17_SEC-E01-security-posture_RAW.json  (826.4 KB)
      2026-08-17_SEC-E01-workflow-script.js  (26.2 KB)
      2026-08-18_states-reply-memo-bindover.pdf  (271.0 KB)
      2026-08-18_states-reply-memo-bindover.txt  (40.1 KB)
      2026-08-20_Q182-crosswalk-anchors_RAW.json  (26.3 KB)
      2026-08-20_Q182-crosswalk-locates_RAW.json  (57.0 KB)
      2026-09-01_ruling-and-order-on-preliminary-hearing-bindover_signed.pdf  (1.4 MB)
      atf_page-26.png  (310.3 KB)
      atf_page-27.png  (181.7 KB)
      atf_page-28.png  (163.6 KB)
      atf_page-29.png  (245.3 KB)
      dc224251_bank_receipts.json  (35.7 KB)
      dc224251_manifest.json  (21.3 KB)
      dc_casenumber_bank_receipts.json  (7.6 KB)
      docket-artifacts_2026-08-16_NUL-repair.py  (4.0 KB)
      docket-artifacts_2026-08-16_NUL-repair_SUPERSESSION.json  (24.3 KB)
      docket-watch-baseline.json  (23.0 KB)
      oct24_clean.txt  (172.0 KB)
      tyler-robinson-ballistics-motion.pdf  (1.3 MB)
      tyler-robinson-ballistics-motion.txt  (69.8 KB)
      tyler-robinson-redacted-hearing-transcript.pdf  (1.0 MB)
    📁 CR-ACQ-2026-09-02_bindover-verification-fetches/  — 81 files, 13.9 MB
      📁 court-and-prosecutor/  — 40 files, 4.4 MB
        legacy.utcourts.gov_cal_.raw  (64.3 KB)
        legacy.utcourts.gov_cal_search.php_t_c_c_251403576_d_all_loc_all.raw  (31.4 KB)
        legacy.utcourts.gov_cal_search.php_t_j_j_Graf_d_all_loc_all.raw  (1.3 MB)
        legacy.utcourts.gov_cal_search.php_t_p_p_Robinson_2C_Tyler_d_all_loc_all.raw  (33.6 KB)
        legacy.utcourts.gov_judgments_view.php_loc_fourth.raw  (22.5 KB)
        legacy.utcourts.gov_utc_news_.html  (64.5 KB)
        legacy.utcourts.gov_utc_news_2026_07_.raw  (38.8 KB)
        legacy.utcourts.gov_utc_news_2026_08_.html  (44.5 KB)
        legacy.utcourts.gov_utc_news_2026_08_28_public-attendance-for-tyler-robinson-preliminary-hearing_.html  (41.9 KB)
        legacy.utcourts.gov_utc_news_2026_09_.html  (151.2 KB)
        legacy.utcourts.gov_utc_news_2026_09_01_.html  (151.2 KB)
        legacy.utcourts.gov_utc_news_2026_09_02_.html  (151.2 KB)
        legacy.utcourts.gov_utc_news__s_Robinson.html  (42.7 KB)
        legacy.utcourts.gov_utc_news_category_high-profile-cases_.html  (151.2 KB)
        legacy.utcourts.gov_utc_news_tag_tyler-robinson_.html  (151.2 KB)
        legacy.utcourts.gov_utc_notices_category_utah_.raw  (50.6 KB)
        probe_media.html  (40.1 KB)
        probe_root.html  (45.7 KB)
        provo_robinson.raw  (54.5 KB)
        ua.html  (7.1 KB)
        ua_media.html  (40.1 KB)
        uc_news.html  (52.1 KB)
        uc_root.html  (168.4 KB)
        ucao_k.html  (7.1 KB)
        wb_ckpr_20260613.html  (51.2 KB)
        www.utcourts.gov_.html  (184.0 KB)
        www.utcourts.gov_content_utcourts_us_en_about_miscellaneous_directory_court-details.html_id_utah-county-provo-district-court.raw  (120.2 KB)
        www.utcourts.gov_en_about_news-press.html.html  (89.2 KB)
        www.utcourts.gov_en_about_news.html.html  (89.2 KB)
        www.utcourts.gov_en_court-records-publications_publications_public-notices_courts.html.raw  (106.3 KB)
        www.utcourts.gov_en_court-records-publications_records_xchange.html.raw  (97.9 KB)
        www.utcourts.gov_en_courts_court-types_dist_dist-sites_4th.html.raw  (94.7 KB)
        www.utcourts.gov_en_media_media.html.html  (92.8 KB)
        www.utcourts.gov_en_media_media_Media-Policies-Resources.html.html  (91.8 KB)
        www.utcourts.gov_en_media_media_high-profile-cases.html.html  (89.2 KB)
        www.utcourts.gov_en_media_media_robinson.html.html  (89.2 KB)
        www.utcourts.gov_en_media_media_state-v-robinson.html.html  (89.2 KB)
        www.utcourts.gov_en_media_media_tyler-robinson.html.html  (89.2 KB)
        www.utcourts.gov_en_news.html.html  (89.2 KB)
        www.utcourts.gov_news_.html  (89.2 KB)
      📁 outlets/  — 32 files, 6.9 MB
        abc.html  (214.4 KB)
        ap1.html  (1001.0 KB)
        ap2.html  (955.8 KB)
        ap3.html  (832.2 KB)
        cbs.html  (608.9 KB)
        chn_article.html  (103.8 KB)
        chn_feed.xml  (57.0 KB)
        deseret-0901.html  (327.6 KB)
        ksl-51618264.html  (186.1 KB)
        nbc.html  (442.7 KB)
        sltrib-0901.html  (323.4 KB)
        utahb_page_1.html  (111.3 KB)
        utahb_page_1.url.txt  (121 B)
        utahb_page_10.html  (88.9 KB)
        utahb_page_10.url.txt  (98 B)
        utahb_page_16.html  (41.4 KB)
        utahb_page_16.url.txt  (88 B)
        utahb_page_17.html  (44.5 KB)
        utahb_page_17.url.txt  (91 B)
        utahb_page_18.html  (350.7 KB)
        utahb_page_18.url.txt  (103 B)
        utahb_page_19.html  (302.9 KB)
        utahb_page_2.html  (114.4 KB)
        utahb_page_2.url.txt  (131 B)
        utahb_page_6.html  (320.8 KB)
        utahb_page_6.url.txt  (104 B)
        utahb_page_7.html  (318.8 KB)
        utahb_page_7.url.txt  (105 B)
        utahb_page_8.html  (213.3 KB)
        utahb_page_8.url.txt  (80 B)
        utahb_page_9.html  (94.5 KB)
        utahb_page_9.url.txt  (137 B)
      📁 transcripts-and-docs/  — 6 files, 2.3 MB
        dc_proj.json  (5.7 KB)
        dc_search.json  (5.7 KB)
        rev_day5.html  (343.5 KB)
        rev_sitemap_dec.xml  (724.8 KB)
        xchange.html  (2.0 KB)
        yt.html  (1.2 MB)
      MANIFEST.md  (10.7 KB)
      workflow-results_fetched-and-verdicts.json  (235.0 KB)
      workflow-synthesis.md  (28.7 KB)
    📁 TJR-REVIEW-2026-09-14_verification-cycle-1/  — 59 files, 11.0 MB
      cycle1_adjudication-journal.jsonl  (143.5 KB)
      cycle1_finder-defects.json  (44.2 KB)
      cycle1_panel-verdicts.json  (52.8 KB)
      cycle2_journal.jsonl  (333.8 KB)
      cycle2_results.json  (168.4 KB)
      cycle3_journal.jsonl  (276.3 KB)
      cycle3_queue.json  (118.4 KB)
      cycle3_results.json  (163.8 KB)
      journal_wf_1f229a39-bd3.jsonl  (239.2 KB)
      journal_wf_3fe455fb-26a.jsonl  (190.3 KB)
      journal_wf_8951c2ef-e9c.jsonl  (271.1 KB)
      journal_wf_f2c380ea-788.jsonl  (619.2 KB)
      journal_wf_f79b4b05-205.jsonl  (105.4 KB)
      p2_facts.json  (110.0 KB)
      p2_questions-that-leaked-their-answers.json  (15.1 KB)
      p2_results.json  (622.0 KB)
      p3-iteration2_chains.json  (276.8 KB)
      p3-iteration2_comparison.json  (4.1 KB)
      p3-iteration2_verdicts.json  (301.9 KB)
      p3_chains.json  (203.7 KB)
      p3_steps.json  (257.2 KB)
      p5-iteration2_journal.jsonl  (275.2 KB)
      p5-iteration2_queue.json  (37.3 KB)
      p5-iteration2_results.json  (275.2 KB)
      p5-repair_applied.json  (45.2 KB)
      p5-repair_blind-reread.json  (168.9 KB)
      p5-repair_false-positives.json  (4.8 KB)
      p5-secondhand_applied.json  (11.3 KB)
      p5-secondhand_decisions.json  (122.7 KB)
      p5_citations.json  (50.9 KB)
      p5_results.json  (271.6 KB)
      p7_attack-results.json  (382.6 KB)
      p7_claim-list-as-attacked.json  (38.3 KB)
      p7_journal.jsonl  (376.3 KB)
      p8-iteration2_journal.jsonl  (304.8 KB)
      p8-iteration2_masked-payloads-sent-to-agents.json  (39.9 KB)
      p8-iteration2_source-rebuilds.json  (305.1 KB)
      p8-iteration2_values-withheld-from-agents.json  (1.9 KB)
      p8_document-ledger-locked-before-results.json  (5.7 KB)
      p8_journal.jsonl  (434.3 KB)
      p8_quantity-census.json  (22.7 KB)
      p8_source-rebuilds.json  (433.3 KB)
      p9_document-attribution-ledger-locked-before-results.json  (43.2 KB)
      p9_journal.jsonl  (409.4 KB)
      p9_quotation-census.json  (52.4 KB)
      p9_source-locations.json  (414.2 KB)
      profile_v1.0_pre-correction.md  (62.1 KB)
      profile_v1.1_pre-cycle2.md  (79.8 KB)
      profile_v1.2_pre-cycle3.md  (91.7 KB)
      profile_v1.3_pre-scaffolding-repair.md  (146.0 KB)
      profile_v1.4_pre-P8.md  (147.8 KB)
      profile_v1.5_pre-P9.md  (159.9 KB)
      profile_v1.6_pre-P7.md  (169.0 KB)
      profile_v1.7_pre-P2.md  (182.1 KB)
      profile_v1.9_pre-P8-iteration2.md  (217.6 KB)
      profile_v2.0_pre-P5-iteration2.md  (222.4 KB)
      profile_v2.1_pre-P3-iteration2.md  (228.1 KB)
      profile_v2.2_pre-P5-repair.md  (236.6 KB)
      profile_v2.3_pre-secondhand-upgrade.md  (258.9 KB)
    CR-ACQ-2026-07-27_court-record-acquisition.md  (93.5 KB)
    CR-ACQ-2026-08-14B_supplemental-notice-2026-07-08.md  (11.0 KB)
    CR-ACQ-2026-08-14C_xchange-docket.md  (14.5 KB)
    CR-ACQ-2026-08-14_contempt-transcript.md  (6.8 KB)
    CR-ACQ-2026-08-16B_rev-official-statements.md  (8.7 KB)
    CR-ACQ-2026-08-16_documentcloud-complete-sweep.md  (55.0 KB)
    CR-ACQ-2026-08-20_states-reply.md  (6.8 KB)
    CR-ACQ-2026-09-01_hearing-livestream-capture.md  (14.3 KB)
    CR-AUDIT-2026-07-27_adversarial-pass.md  (11.5 KB)
    CR-AUDIT-2026-07-28_independent-pass.md  (35.6 KB)
    CR-AUDIT-2026-08-01_session-audit.md  (33.9 KB)
    CR-AUDIT-2026-08-20_session-audit.md  (10.2 KB)
    CR-E01_prelim-hearing-Day4_Karner-ATF-testimony.md  (43.5 KB)
    CR-E02_prelim-hearing-Day4_Faumuina-Davis-Twiggs.md  (83.3 KB)
    CR-E03_prelim-hearing-Days2-3-5.md  (89.7 KB)
    CR-E04_prelim-hearing-Day2_Hull-UVU-surveillance.md  (26.6 KB)
    CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md  (101.8 KB)
    CR-E06_Bakker-Day2_Oliver-Day5_full-read.md  (186.8 KB)
    CR-E07_defence-prelim-briefing-2026-08-11.md  (67.1 KB)
    CR-E08_state-information-and-pc-affidavit-2025-09-16.md  (34.7 KB)
    CR-E09_evidence-preservation-order-and-pretrial-practice.md  (21.4 KB)
    CR-E10_publicity-order-and-record-classification.md  (41.4 KB)
    CR-E11_prosecutor-disqualification-track.md  (41.3 KB)
    CR-E12_closure-classification-and-sealing-map.md  (36.9 KB)
    CR-E13_evidence-preservation-chain-complete.md  (28.5 KB)
    CR-E14_continuance-motion-and-the-discovery-record.md  (55.1 KB)
    CR-E15_ATF-firearms-report-2025-09-17.md  (57.2 KB)
    CR-E16_participant-roster-and-label-reconciliation.md  (34.5 KB)
    CR-E17_states-reply-2026-08-18.md  (38.1 KB)
    CR-E18_certified-transcript-crosswalk.md  (25.6 KB)
    CR-E19_latent-print-record.md  (66.3 KB)
    CR-E20_forensic-exhibit-map.md  (53.2 KB)
    CR-E21_forensic-discovery-census.md  (45.4 KB)
    CR-REVIEW-2026-08-14_losee-draft-Q07.md  (22.3 KB)
    CR-REVIEW-2026-08-16B_xchange-null-audit.md  (15.2 KB)
    CR-REVIEW-2026-08-16C_Q61-tranche3.md  (13.8 KB)
    CR-REVIEW-2026-08-16D_Q105-null-re-runs.md  (14.7 KB)
    CR-REVIEW-2026-08-16E_Q111-legacy-file-audit.md  (13.4 KB)
    CR-REVIEW-2026-08-16F_Q89-losee-draft-vs-sworn-geometry.md  (15.1 KB)
    CR-REVIEW-2026-08-16G_twiggs-profile-reconciliation.md  (15.2 KB)
    CR-REVIEW-2026-08-16_Q61-carried-nulls.md  (14.6 KB)
    CR-REVIEW-2026-08-17_Q146-Q148-Q131.md  (16.3 KB)
    CR-REVIEW-2026-08-30_CR-E19-E20-E21-verification-cycle.md  (31.8 KB)
    CR-WATCH-log.md  (215.3 KB)
  📁 files - DNA evidence/  — 3 files, 350.3 KB
    DNA-E01_DNA-evidence-what-it-can-bear.md  (296.4 KB)
    Kirk-Robinson_DNA-Evidence_Acquisition-Roadmap_2026-07-15.md  (19.7 KB)
    Kirk-Robinson_DNA-Evidence_Consolidated-Audit_2026-07-15.md  (34.2 KB)
  📁 files - Event security/  — 4 files, 529.9 KB
    2026-08-20_singju-srs254-harpole-transcript.txt  (133.8 KB)
    2026-08-20_singju-srs254-harpole-transcript_RAW.html  (282.2 KB)
    SEC-E01_security-posture-2025-09-10.md  (79.3 KB)
    SEC-E02_security-team-allegations-assessment.md  (34.7 KB)
  📁 files - George Zinn/  — 10 files, 225.9 KB
    📁 ZINN-ACQ-2026-08-20_artifacts/  — 6 files, 141.6 KB
      2025-09-16_zinn_obstruction_pca_dc26098558.pdf  (61.6 KB)
      2025-09-16_zinn_obstruction_pca_dc26098558.txt  (4.7 KB)
      2025-09-16_zinn_sex_charges_pca_dc26098557.pdf  (65.4 KB)
      2025-09-16_zinn_sex_charges_pca_dc26098557.txt  (7.4 KB)
      dc26098557.json  (1.2 KB)
      dc26098558.json  (1.2 KB)
    ZINN-ACQ-2026-08-20_zinn-pcas.md  (11.6 KB)
    ZINN-REVIEW-2026-08-17_partial-reconciliation.md  (17.3 KB)
    t1 source acquisition roadmap - George Zinn.md  (7.8 KB)
    zinn-george-evidence.md  (47.6 KB)
  📁 files - Kirk assassination questions/  — 2 files, 59.8 KB
    kirk-shooting-official-timeline.md  (46.5 KB)
    t1 source acquisition roadmap - Kirk assassination questions.md  (13.3 KB)
  📁 files - Losee building/  — 2 files, 21.1 KB
    losee-rooftop-firing-evidence.md  (10.6 KB)
    tier1 source acquisition roadmap - forensic evidence for Losee building shot.md  (10.4 KB)
  📁 tools/  — 2 files, 22.8 KB
    build-docx.js  (7.2 KB)
    build-html.py  (15.6 KB)
  .DS_Store  (14.0 KB)
  .gitignore  (88 B)
  CLAUDE.md  (11.4 KB)
  DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md  (8.5 KB)
  DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md  (7.4 KB)
  DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md  (8.3 KB)
  DOCKET-WATCH-routine-prompt-DRAFT-2026-09-02.md  (11.6 KB)
  DOCKET-WATCH-routine-prompt-DRAFT-2026-09-14.md  (15.5 KB)
  DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md  (14.8 KB)
  DOCKET-WATCH.md  (45.6 KB)
  Forensic-Sampling-Summary_2026-08-30.docx  (22.9 KB)
  LOOP.md  (7.1 KB)
  QUEUE.md  (193.4 KB)
  README.md  (2.8 KB)
  SOURCE-MANIFEST.md  (38.5 KB)
  START-HERE.md  (74.1 KB)
  Tyler-Robinson_Comprehensive-Profile_2026-09-14.docx  (148.0 KB)
  Tyler-Robinson_Comprehensive-Profile_2026-09-14.html  (355.6 KB)
  VERIFICATION-PROTOCOL.md  (17.0 KB)
  artifact_search.py  (5.2 KB)
  docket-watch-run.py  (11.9 KB)
  erika-kirk-background-family-contested-claims-dossier.md  (77.9 KB)
  evidence-rifle-photo-nypost-authenticity.md  (20.0 KB)
  lance-twiggs-comprehensive-profile.md  (145.0 KB)
  manifest.py  (11.2 KB)
  migrate-files.sh  (2.2 KB)
  queue-check.sh  (5.4 KB)
  robinson-tyler-james-comprehensive-profile.md  (271.4 KB)
  source-manifest.json  (228.5 KB)
  tsearch.py  (4.0 KB)
```

---

## Appendix B · Classification of every file

Summary by category, then by sub-class, then per file.

| Category | Files | Bytes |
|---|---:|---:|
| source code | 5 | 37.7 KB |
| config | 7 | 17.2 KB |
| data (raw) | 204 | 85.1 MB |
| data (processed/derived) | 73 | 5.0 MB |
| notebooks/experiments | 67 | 18.1 MB |
| scripts/one-offs | 7 | 90.7 KB |
| documentation | 109 | 5.2 MB |
| generated artifacts | 26 | 3.1 MB |
| tests | 0 | 0 B |
| assets | 0 | 0 B |
| unknown | 1 | 0 B |

| Sub-class | Files | Bytes |
|---|---:|---:|
| config | 7 | 17.2 KB |
| data (derived: extraction/condensation) | 10 | 1.9 MB |
| data (derived: rendered page) | 4 | 901.0 KB |
| data (derived: text extraction of PDF) | 57 | 2.1 MB |
| data (derived: transcript extraction) | 2 | 100.7 KB |
| data (raw: HTTP body capture) | 78 | 13.6 MB |
| data (raw: court document) | 59 | 54.6 MB |
| data (raw: feed capture) | 2 | 2.5 MB |
| data (raw: transcript capture) | 6 | 3.4 MB |
| data (raw: transcript) | 1 | 133.8 KB |
| data (raw: transcript/text as received) | 7 | 382.6 KB |
| data (raw: web capture) | 6 | 1.2 MB |
| data (raw: web/API capture) | 36 | 4.7 MB |
| data (raw: web/feed capture) | 9 | 4.5 MB |
| documentation | 91 | 4.0 MB |
| documentation (bank manifest) | 1 | 10.7 KB |
| documentation (draft/process note, inside data bank) | 5 | 977.2 KB |
| documentation (methodology kit) | 12 | 183.1 KB |
| experiments (process evidence, inside data bank) | 21 | 9.3 MB |
| experiments (verification-cycle bank) | 46 | 8.8 MB |
| generated (archive) | 1 | 54.6 KB |
| generated (cache/checkpoint) | 3 | 22.1 KB |
| generated (frozen snapshot) | 13 | 2.2 MB |
| generated (index, committed on purpose) | 2 | 267.0 KB |
| generated (receipt/state, inside data bank) | 4 | 87.5 KB |
| generated (render/deliverable) | 3 | 526.5 KB |
| scripts (one-off, inside a data bank) | 4 | 65.7 KB |
| scripts (utility/build) | 3 | 25.0 KB |
| source code (maintained tool) | 5 | 37.7 KB |
| unknown (zero-byte capture) | 1 | 0 B |

| Path | Class |
|---|---|
| `.DS_Store` | generated (cache/checkpoint) |
| `.claude/RESUME.md` | generated (cache/checkpoint) |
| `.gitignore` | config |
| `.obsidian/app.json` | config |
| `.obsidian/appearance.json` | config |
| `.obsidian/core-plugins.json` | config |
| `.obsidian/graph.json` | config |
| `.obsidian/workspace.json` | config |
| `CLAUDE.md` | config |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md` | documentation |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md` | documentation |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md` | documentation |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-02.md` | documentation |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-14.md` | documentation |
| `DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md` | documentation |
| `DOCKET-WATCH.md` | documentation |
| `Forensic-Sampling-Summary_2026-08-30.docx` | generated (render/deliverable) |
| `LOOP.md` | documentation |
| `QUEUE.md` | documentation |
| `README.md` | documentation |
| `SOURCE-MANIFEST.md` | generated (index, committed on purpose) |
| `START-HERE.md` | documentation |
| `Tyler-Robinson_Comprehensive-Profile_2026-09-14.docx` | generated (render/deliverable) |
| `Tyler-Robinson_Comprehensive-Profile_2026-09-14.html` | generated (render/deliverable) |
| `VERIFICATION-PROTOCOL.md` | documentation |
| `VerificationAndFactCheckProtocol copy/COMPLETE-DROP-FILE.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/VERIFICATION-KIT-INDEX.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit.zip` | generated (archive) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/00-doctrine-and-router.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/COMPLETE-DROP-FILE.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/MANIFEST.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/README.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/chain-of-thought-verification.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/fact-checking-assistant-prompt.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/faithfulness-metrics.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/prompts/02-prompt-pack.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/protocols/01-research-protocols.md` | documentation (methodology kit) |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/schemas/03-claim-card-and-log.md` | documentation (methodology kit) |
| `__pycache__/artifact_search.cpython-314.pyc` | generated (cache/checkpoint) |
| `artifact_search.py` | source code (maintained tool) |
| `docket-watch-run.py` | source code (maintained tool) |
| `erika-kirk-background-family-contested-claims-dossier.md` | documentation |
| `evidence-rifle-photo-nypost-authenticity.md` | documentation |
| `files - Arrest chronology/robinson-surrender-timeline.md` | documentation |
| `files - Arrest chronology/tier1-acquisition-roadmap.md` | documentation |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-19_phase0-pull-log.md` | documentation |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/aurora_tweet.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cdx_neff_tw.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cdx_neff_x.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cocopah_20170130.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cocopah_tweet.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/ef_20151022.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/factually.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/frantzve_bio_20240612.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_07049361.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_57d2149a.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_8c35c695.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_8f838a9d.png` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/missaz_20121112.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neff_20260629.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028271192042586183.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028271884647944515.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028287292922814792.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028429731729977830.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028520462108799255.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028556678283853959.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028577525149139216.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028621723608989835.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028624883417219159.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028634485651378634.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028642700841615563.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028689687028846716.json` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/primetimer_shabbat.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/rmazusa_status_2011.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/substack_e06.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/tmp_at.html` | data (raw: web/API capture) |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-18B_library-audit.md` | documentation |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-18_library-audit.md` | documentation |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-20_session-audit.md` | documentation |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-27B_adversarial-pass.md` | documentation |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-27_session-audit.md` | documentation |
| `files - Bride of Charlie series/BOC-E01_Wrinkle-in-Time_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E02_Dr-Jerri-and-Mrs-Hyde_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E03_Have-No-Fear-Lori-Is-Here_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E04_The-Ties-That-Bind_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E05_The-Lost-Years_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E06_What-Happened-In-Romania_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E07_Crazy-In-Love_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E08_Red-Sparrow_claim-inventory.md` | documentation |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/caption_tracks.json` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/feed.xml` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/happyscribe_raw.html` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podscripts_extract.txt` | data (derived: transcript extraction) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podscripts_raw.html` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podwave_extract.txt` | data (derived: transcript extraction) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podwave_raw.html` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/rumble_raw.html` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/transcript_primary.txt` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/transcript_secondary.txt` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/yt_captions.json3` | unknown (zero-byte capture) |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/yt_watch.html` | data (raw: web/feed capture) |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/cia_directors_gallery_20260727.html` | data (raw: feed capture) |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/feed_20260727.xml` | data (raw: feed capture) |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/sweep_extract.py` | scripts (one-off, inside a data bank) |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_post-series-case-claims-corpus.md` | documentation |
| `files - Bride of Charlie series/BOC-T1_Tier1-Acquisition-Roadmap_all-episodes.md` | documentation |
| `files - Court record/CR-ACQ-2026-07-27_court-record-acquisition.md` | documentation |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-12_public-safety-assessment-report_dkt3_dc27880877.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-12_public-safety-assessment-report_dkt3_dc27880877.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_5_dc26099252.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_5_dc26099252.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_affidavit-of-probable-cause_dc27880530.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_affidavit-of-probable-cause_dc27880530.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_bail-order_dkt4_dc27880869.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_bail-order_dkt4_dc27880869.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_information-charging-document_dc27880532.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_information-charging-document_dc27880532.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_pretrial-protective-order_dkt14_dc27880872.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_pretrial-protective-order_dkt14_dc27880872.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_request-designation-victim-representative_dkt12_dc27880865.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_request-designation-victim-representative_dkt12_dc27880865.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-chad-grunander-biography_dc27880539.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-chad-grunander-biography_dc27880539.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-david-sturgill-biography_dc27880538.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-david-sturgill-biography_dc27880538.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-motion-to-set-aside-order_dc27880864.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-motion-to-set-aside-order_dc27880864.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_state-open-file-policy-notice_dc27880871.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_state-open-file-policy-notice_dc27880871.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-04_stipulated-order-preserve-evidence_dc27880862.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-04_stipulated-order-preserve-evidence_dc27880862.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-19_4_dc26493871.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-19_4_dc26493871.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-case-history-full_dc27880531.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-case-history-full_dc27880531.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-short-case-history_dc27880533.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-short-case-history_dc27880533.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-23-pub_rev-contempt-hearing-transcript.html` | data (raw: web capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-23-pub_rev-contempt-hearing-transcript.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-08_supplemental-notice-access-to-evidence_dc28443912.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-08_supplemental-notice-access-to-evidence_dc28443912.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_BLOCKED-DRAFT_q08-dna_DO-NOT-PUBLISH.md` | documentation (draft/process note, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_Q58-completion-60-verdicts.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md` | documentation (draft/process note, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_q08-reviews-and-register-proposal.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_round2-Q58-raw-output.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_verification-cycle-raw-output.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_verification-cycle-workflow-result.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing_ALT-EXTRACTION-dc28551955.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_CRE07-completeness-inventory_RAW-CANDIDATES.jsonl` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_CRE08-completeness-state-filings_RAW-CANDIDATES.jsonl` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-candidate-bank_INDEX.md` | documentation (draft/process note, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-completeness-day2-bakker_RAW-CANDIDATES.jsonl` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-completeness-day5-oliver_RAW-CANDIDATES.jsonl` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-finder-DNAE01-sections6-14_RAW-CANDIDATES.jsonl` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q140-twiggs-analytic-pass_RAW.md` | documentation (draft/process note, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q70-completion-six-reader-reports_RAW.md` | documentation (draft/process note, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev-q120-acquisition_RECEIPTS.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev-q120-bodies.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-captures-kirk-shooter.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-captures-kirk-shooter_raw.html` | data (raw: web capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-press-conference-on-kirk-shooting.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-press-conference-on-kirk-shooting_raw.html` | data (raw: web capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_press-conference-on-charlie-kirk-shooting.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_press-conference-on-charlie-kirk-shooting_raw.html` | data (raw: web capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_update-on-charlie-kirk-shooter.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_update-on-charlie-kirk-shooter_raw.html` | data (raw: web capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q136-zinn-reconciliation_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q137-Q138-person-files_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q137-Q138-workflow-script.js` | scripts (one-off, inside a data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q142-Q143-Q144-Q145-twiggs-programme_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_SEC-E01-security-posture_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_SEC-E01-workflow-script.js` | scripts (one-off, inside a data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-20_Q182-crosswalk-anchors_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-20_Q182-crosswalk-locates_RAW.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-09-01_ruling-and-order-on-preliminary-hearing-bindover_signed.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-26.png` | data (derived: rendered page) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-27.png` | data (derived: rendered page) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-28.png` | data (derived: rendered page) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-29.png` | data (derived: rendered page) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc224251_bank_receipts.json` | generated (receipt/state, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc224251_manifest.json` | generated (receipt/state, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc_casenumber_bank_receipts.json` | generated (receipt/state, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-artifacts_2026-08-16_NUL-repair.py` | scripts (one-off, inside a data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-artifacts_2026-08-16_NUL-repair_SUPERSESSION.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-watch-baseline.json` | generated (receipt/state, inside data bank) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/oct24_clean.txt` | data (raw: transcript/text as received) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/2026-09-01_final-prelim-argument.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/2026-09-01_final-prelim-argument_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day1.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day1_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2_condensed.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3_condensed.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day4.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day4_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5_condensed.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5_raw.html` | data (raw: transcript capture) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/faumuina_condensed.txt` | data (derived: extraction/condensation) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.txt` | data (derived: text extraction of PDF) |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-redacted-hearing-transcript.pdf` | data (raw: court document) |
| `files - Court record/CR-ACQ-2026-08-14B_supplemental-notice-2026-07-08.md` | documentation |
| `files - Court record/CR-ACQ-2026-08-14C_xchange-docket.md` | documentation |
| `files - Court record/CR-ACQ-2026-08-14_contempt-transcript.md` | documentation |
| `files - Court record/CR-ACQ-2026-08-16B_rev-official-statements.md` | documentation |
| `files - Court record/CR-ACQ-2026-08-16_documentcloud-complete-sweep.md` | documentation |
| `files - Court record/CR-ACQ-2026-08-20_states-reply.md` | documentation |
| `files - Court record/CR-ACQ-2026-09-01_hearing-livestream-capture.md` | documentation |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/MANIFEST.md` | documentation (bank manifest) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_c_c_251403576_d_all_loc_all.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_j_j_Graf_d_all_loc_all.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_p_p_Robinson_2C_Tyler_d_all_loc_all.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_judgments_view.php_loc_fourth.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_07_.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_08_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_08_28_public-attendance-for-tyler-robinson-preliminary-hearing_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_01_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_02_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news__s_Robinson.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_category_high-profile-cases_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_tag_tyler-robinson_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_notices_category_utah_.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/probe_media.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/probe_root.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/provo_robinson.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ua.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ua_media.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/uc_news.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/uc_root.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ucao_k.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/wb_ckpr_20260613.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_content_utcourts_us_en_about_miscellaneous_directory_court-details.html_id_utah-county-provo-district-court.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_about_news-press.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_about_news.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_court-records-publications_publications_public-notices_courts.html.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_court-records-publications_records_xchange.html.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_courts_court-types_dist_dist-sites_4th.html.raw` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_Media-Policies-Resources.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_high-profile-cases.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_robinson.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_state-v-robinson.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_tyler-robinson.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_news.html.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_news_.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/abc.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap1.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap2.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap3.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/cbs.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/chn_article.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/chn_feed.xml` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/deseret-0901.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ksl-51618264.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/nbc.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/sltrib-0901.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_1.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_1.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_10.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_10.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_16.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_16.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_17.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_17.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_18.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_18.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_19.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_2.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_2.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_6.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_6.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_7.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_7.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_8.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_8.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_9.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_9.url.txt` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/dc_proj.json` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/dc_search.json` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/rev_day5.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/rev_sitemap_dec.xml` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/xchange.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/yt.html` | data (raw: HTTP body capture) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/workflow-results_fetched-and-verdicts.json` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/workflow-synthesis.md` | experiments (process evidence, inside data bank) |
| `files - Court record/CR-AUDIT-2026-07-27_adversarial-pass.md` | documentation |
| `files - Court record/CR-AUDIT-2026-07-28_independent-pass.md` | documentation |
| `files - Court record/CR-AUDIT-2026-08-01_session-audit.md` | documentation |
| `files - Court record/CR-AUDIT-2026-08-20_session-audit.md` | documentation |
| `files - Court record/CR-E01_prelim-hearing-Day4_Karner-ATF-testimony.md` | documentation |
| `files - Court record/CR-E02_prelim-hearing-Day4_Faumuina-Davis-Twiggs.md` | documentation |
| `files - Court record/CR-E03_prelim-hearing-Days2-3-5.md` | documentation |
| `files - Court record/CR-E04_prelim-hearing-Day2_Hull-UVU-surveillance.md` | documentation |
| `files - Court record/CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md` | documentation |
| `files - Court record/CR-E06_Bakker-Day2_Oliver-Day5_full-read.md` | documentation |
| `files - Court record/CR-E07_defence-prelim-briefing-2026-08-11.md` | documentation |
| `files - Court record/CR-E08_state-information-and-pc-affidavit-2025-09-16.md` | documentation |
| `files - Court record/CR-E09_evidence-preservation-order-and-pretrial-practice.md` | documentation |
| `files - Court record/CR-E10_publicity-order-and-record-classification.md` | documentation |
| `files - Court record/CR-E11_prosecutor-disqualification-track.md` | documentation |
| `files - Court record/CR-E12_closure-classification-and-sealing-map.md` | documentation |
| `files - Court record/CR-E13_evidence-preservation-chain-complete.md` | documentation |
| `files - Court record/CR-E14_continuance-motion-and-the-discovery-record.md` | documentation |
| `files - Court record/CR-E15_ATF-firearms-report-2025-09-17.md` | documentation |
| `files - Court record/CR-E16_participant-roster-and-label-reconciliation.md` | documentation |
| `files - Court record/CR-E17_states-reply-2026-08-18.md` | documentation |
| `files - Court record/CR-E18_certified-transcript-crosswalk.md` | documentation |
| `files - Court record/CR-E19_latent-print-record.md` | documentation |
| `files - Court record/CR-E20_forensic-exhibit-map.md` | documentation |
| `files - Court record/CR-E21_forensic-discovery-census.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-14_losee-draft-Q07.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16B_xchange-null-audit.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16C_Q61-tranche3.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16D_Q105-null-re-runs.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16E_Q111-legacy-file-audit.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16F_Q89-losee-draft-vs-sworn-geometry.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16G_twiggs-profile-reconciliation.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-16_Q61-carried-nulls.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-17_Q146-Q148-Q131.md` | documentation |
| `files - Court record/CR-REVIEW-2026-08-30_CR-E19-E20-E21-verification-cycle.md` | documentation |
| `files - Court record/CR-WATCH-log.md` | documentation |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_adjudication-journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_finder-defects.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_panel-verdicts.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_queue.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_1f229a39-bd3.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_3fe455fb-26a.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_8951c2ef-e9c.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f2c380ea-788.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f79b4b05-205.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_facts.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_questions-that-leaked-their-answers.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_chains.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_comparison.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_verdicts.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_chains.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_steps.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_queue.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_applied.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_blind-reread.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_false-positives.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_applied.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_decisions.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_citations.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_attack-results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_claim-list-as-attacked.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_masked-payloads-sent-to-agents.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_source-rebuilds.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_values-withheld-from-agents.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_document-ledger-locked-before-results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_quantity-census.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_source-rebuilds.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_document-attribution-ledger-locked-before-results.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_journal.jsonl` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_quotation-census.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_source-locations.json` | experiments (verification-cycle bank) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.0_pre-correction.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.1_pre-cycle2.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.2_pre-cycle3.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.3_pre-scaffolding-repair.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.4_pre-P8.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.5_pre-P9.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.6_pre-P7.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.7_pre-P2.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.9_pre-P8-iteration2.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.0_pre-P5-iteration2.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.1_pre-P3-iteration2.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.2_pre-P5-repair.md` | generated (frozen snapshot) |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.3_pre-secondhand-upgrade.md` | generated (frozen snapshot) |
| `files - DNA evidence/DNA-E01_DNA-evidence-what-it-can-bear.md` | documentation |
| `files - DNA evidence/Kirk-Robinson_DNA-Evidence_Acquisition-Roadmap_2026-07-15.md` | documentation |
| `files - DNA evidence/Kirk-Robinson_DNA-Evidence_Consolidated-Audit_2026-07-15.md` | documentation |
| `files - Event security/2026-08-20_singju-srs254-harpole-transcript.txt` | data (raw: transcript) |
| `files - Event security/2026-08-20_singju-srs254-harpole-transcript_RAW.html` | data (raw: web capture) |
| `files - Event security/SEC-E01_security-posture-2025-09-10.md` | documentation |
| `files - Event security/SEC-E02_security-team-allegations-assessment.md` | documentation |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_obstruction_pca_dc26098558.pdf` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_obstruction_pca_dc26098558.txt` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_sex_charges_pca_dc26098557.pdf` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_sex_charges_pca_dc26098557.txt` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/dc26098557.json` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/dc26098558.json` | data (raw: web/API capture) |
| `files - George Zinn/ZINN-ACQ-2026-08-20_zinn-pcas.md` | documentation |
| `files - George Zinn/ZINN-REVIEW-2026-08-17_partial-reconciliation.md` | documentation |
| `files - George Zinn/t1 source acquisition roadmap - George Zinn.md` | documentation |
| `files - George Zinn/zinn-george-evidence.md` | documentation |
| `files - Kirk assassination questions/kirk-shooting-official-timeline.md` | documentation |
| `files - Kirk assassination questions/t1 source acquisition roadmap - Kirk assassination questions.md` | documentation |
| `files - Losee building/losee-rooftop-firing-evidence.md` | documentation |
| `files - Losee building/tier1 source acquisition roadmap - forensic evidence for Losee building shot.md` | documentation |
| `lance-twiggs-comprehensive-profile.md` | documentation |
| `manifest.py` | source code (maintained tool) |
| `migrate-files.sh` | scripts (utility/build) |
| `queue-check.sh` | source code (maintained tool) |
| `robinson-tyler-james-comprehensive-profile.md` | documentation |
| `source-manifest.json` | generated (index, committed on purpose) |
| `tools/build-docx.js` | scripts (utility/build) |
| `tools/build-html.py` | scripts (utility/build) |
| `tsearch.py` | source code (maintained tool) |

---

## Appendix C · Mapping of every current path to its proposed path

*(stays)* means no move. The Q column points at the question in §8 that governs the row.

| Current path | Proposed path | Reason | Q |
|---|---|---|---|
| `.DS_Store` | *(stays)* | Already ignored; Finder metadata, leave |  |
| `.claude/RESUME.md` | *(stays)* | Ignored via .git/info/exclude; stale harness checkpoint from 2026-08-17 (see §4.3), leave outside git |  |
| `.gitignore` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `.obsidian/app.json` | *(stays)* | Obsidian vault config; stays |  |
| `.obsidian/appearance.json` | *(stays)* | Obsidian vault config; stays |  |
| `.obsidian/core-plugins.json` | *(stays)* | Obsidian vault config; stays |  |
| `.obsidian/graph.json` | *(stays)* | Obsidian vault config; stays |  |
| `.obsidian/workspace.json` | *(stays)* | Obsidian vault config; stays |  |
| `CLAUDE.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md` | `archive/docket-watch-prompts/DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md` | Superseded draft of the routine prompt; each later draft names the one it supersedes |  |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md` | `archive/docket-watch-prompts/DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md` | Superseded draft of the routine prompt; each later draft names the one it supersedes |  |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md` | `archive/docket-watch-prompts/DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md` | Superseded draft of the routine prompt; each later draft names the one it supersedes |  |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-02.md` | `archive/docket-watch-prompts/DOCKET-WATCH-routine-prompt-DRAFT-2026-09-02.md` | Superseded draft of the routine prompt; each later draft names the one it supersedes |  |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-14.md` | `ops/docket-watch/DOCKET-WATCH-routine-prompt-DRAFT-2026-09-14.md` | Deployed-configuration text for the cloud routine (LIVE) and its pending replacement (current DRAFT); operational, not research | Q6 |
| `DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md` | `ops/docket-watch/DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md` | Deployed-configuration text for the cloud routine (LIVE) and its pending replacement (current DRAFT); operational, not research | Q6 |
| `DOCKET-WATCH.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `Forensic-Sampling-Summary_2026-08-30.docx` | `deliverables/Forensic-Sampling-Summary_2026-08-30.docx` | Rendered/published outputs, regenerable from the markdown (profile) or produced for sharing; separate from sources | Q7 |
| `LOOP.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `QUEUE.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `README.md` | *(stays)* | Stays; rewritten in Phase 2 |  |
| `SOURCE-MANIFEST.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `START-HERE.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `Tyler-Robinson_Comprehensive-Profile_2026-09-14.docx` | `deliverables/Tyler-Robinson_Comprehensive-Profile_2026-09-14.docx` | Rendered/published outputs, regenerable from the markdown (profile) or produced for sharing; separate from sources | Q7 |
| `Tyler-Robinson_Comprehensive-Profile_2026-09-14.html` | `deliverables/Tyler-Robinson_Comprehensive-Profile_2026-09-14.html` | Rendered/published outputs, regenerable from the markdown (profile) or produced for sharing; separate from sources | Q7 |
| `VERIFICATION-PROTOCOL.md` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `VerificationAndFactCheckProtocol copy/COMPLETE-DROP-FILE.md` | `archive/verification-kit-drop/COMPLETE-DROP-FILE.md` | Byte-identical duplicate of the copy inside research-verification-kit/ (the indexed one) |  |
| `VerificationAndFactCheckProtocol copy/VERIFICATION-KIT-INDEX.md` | `docs/VERIFICATION-KIT-INDEX.md` | Index of the kit; its relative link `research-verification-kit/README.md` keeps working from docs/ |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit.zip` | `archive/verification-kit-drop/research-verification-kit.zip` | Original drop archive; contents are extracted and integrity-checked, zip is redundant |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/00-doctrine-and-router.md` | `docs/research-verification-kit/00-doctrine-and-router.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/COMPLETE-DROP-FILE.md` | `docs/research-verification-kit/COMPLETE-DROP-FILE.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/MANIFEST.md` | `docs/research-verification-kit/MANIFEST.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/README.md` | `docs/research-verification-kit/README.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/chain-of-thought-verification.md` | `docs/research-verification-kit/background/chain-of-thought-verification.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/fact-checking-assistant-prompt.md` | `docs/research-verification-kit/background/fact-checking-assistant-prompt.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/background/faithfulness-metrics.md` | `docs/research-verification-kit/background/faithfulness-metrics.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/prompts/02-prompt-pack.md` | `docs/research-verification-kit/prompts/02-prompt-pack.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/protocols/01-research-protocols.md` | `docs/research-verification-kit/protocols/01-research-protocols.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `VerificationAndFactCheckProtocol copy/research-verification-kit/schemas/03-claim-card-and-log.md` | `docs/research-verification-kit/schemas/03-claim-card-and-log.md` | The adopted methodology kit belongs under docs/; internal layout kept so its own MANIFEST.md hashes still verify |  |
| `__pycache__/artifact_search.cpython-314.pyc` | `(untrack: git rm --cached; add __pycache__/ and *.pyc to .gitignore; file left on disk, ignored)` | Python bytecode cache committed by accident |  |
| `artifact_search.py` | `scripts/artifact_search.py` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |
| `docket-watch-run.py` | `scripts/docket-watch-run.py` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |
| `erika-kirk-background-family-contested-claims-dossier.md` | `files - Person profiles/erika-kirk-background-family-contested-claims-dossier.md` | Three person-level dossiers sit loose at the root while every other evidence file has a topic folder; gives them one, in the existing `files - <Topic>` convention | Q3 |
| `evidence-rifle-photo-nypost-authenticity.md` | `files - Kirk assassination questions/evidence-rifle-photo-nypost-authenticity.md` | Loose root evidence file on the rifle photograph; nearest existing topic folder | Q4 |
| `files - Arrest chronology/robinson-surrender-timeline.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Arrest chronology/tier1-acquisition-roadmap.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-19_phase0-pull-log.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/aurora_tweet.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cdx_neff_tw.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cdx_neff_x.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cocopah_20170130.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/cocopah_tweet.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/ef_20151022.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/factually.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/frantzve_bio_20240612.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_07049361.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_57d2149a.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_8c35c695.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/img_8f838a9d.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/missaz_20121112.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neff_20260629.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028271192042586183.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028271884647944515.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028287292922814792.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028429731729977830.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028520462108799255.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028556678283853959.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028577525149139216.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028621723608989835.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028624883417219159.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028634485651378634.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028642700841615563.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/neffmar/2028689687028846716.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/primetimer_shabbat.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/rmazusa_status_2011.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/substack_e06.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ACQ-2026-07-20_F2-artifact-copies/tmp_at.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-18B_library-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-18_library-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-20_session-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-27B_adversarial-pass.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-AUDIT-2026-07-27_session-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E01_Wrinkle-in-Time_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E02_Dr-Jerri-and-Mrs-Hyde_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E03_Have-No-Fear-Lori-Is-Here_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E04_The-Ties-That-Bind_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E05_The-Lost-Years_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E06_What-Happened-In-Romania_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E07_Crazy-In-Love_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E08_Red-Sparrow_claim-inventory.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/caption_tracks.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/feed.xml` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/happyscribe_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podscripts_extract.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podscripts_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podwave_extract.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/podwave_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/rumble_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/transcript_primary.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/transcript_secondary.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/yt_captions.json3` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-E08_transcript-artifacts/yt_watch.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/cia_directors_gallery_20260727.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/feed_20260727.xml` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_artifacts/sweep_extract.py` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Bride of Charlie series/BOC-ROUTE-2026-07-27_post-series-case-claims-corpus.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Bride of Charlie series/BOC-T1_Tier1-Acquisition-Roadmap_all-episodes.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-acquisition.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-10_utah-county-attorney-press-release-uvu-shooting-investigation_dc27880543.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-12_public-safety-assessment-report_dkt3_dc27880877.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-12_public-safety-assessment-report_dkt3_dc27880877.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_5_dc26099252.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_5_dc26099252.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_affidavit-of-probable-cause_dc27880530.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_affidavit-of-probable-cause_dc27880530.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_bail-order_dkt4_dc27880869.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_bail-order_dkt4_dc27880869.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_information-charging-document_dc27880532.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_information-charging-document_dc27880532.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_pretrial-protective-order_dkt14_dc27880872.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_pretrial-protective-order_dkt14_dc27880872.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_proposed-pretrial-protective-order_dkt7_dc27880860.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_request-designation-victim-representative_dkt12_dc27880865.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-16_request-designation-victim-representative_dkt12_dc27880865.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-chad-grunander-biography_dc27880539.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-chad-grunander-biography_dc27880539.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-christopher-ballard-biography_dc27880541.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-david-sturgill-biography_dc27880538.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-david-sturgill-biography_dc27880538.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-jeffrey-gray-biography_dc27880536.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-lauren-hunt-biography_dc27880540.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_prosecutor-ryan-mcbride-biography_dc27880537.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-22_utah-county-attorney-press-release-trial-team-roster_dc27880535.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_copy-video-audio-record-completed_dkt74_dc27880859.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_defendant-motion-to-preserve-evidence_dkt75_dc27880857.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-08_proposed-order-granting-motion-preserve-evidence_dkt76_dc27880875.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-13_both-parties-motion-discovery-protective-order-stipulated_dkt91_dc27880863.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-21_defendant-motion-strike-response-defendant-motion-appear-all_dkt111_dc27880867.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-motion-to-set-aside-order_dc27880864.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-motion-to-set-aside-order_dc27880864.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-22_state-response-to-motion-to-preserve_dkt117_dc27880878.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_ruling-order-defendant-motion-strike-appear-civilian-clothing_dkt137_dc27880868.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_state-open-file-policy-notice_dc27880871.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-10-27_state-open-file-policy-notice_dc27880871.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-03_stipulated-motion-classify-transcript-private_dkt152_dc27880861.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-04_stipulated-order-preserve-evidence_dc27880862.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-04_stipulated-order-preserve-evidence_dc27880862.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-11-10_defendant-response-notice-of-motions-to-close_dc27880858.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-08_defendant-response-media-limited-intervention_dkt197_dc27880876.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-15_ruling-clarifying-publicity-order_dkt242_dc27880866.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2025-12-17_defendant-motion-disqualify-utah-county-attorneys-office_dkt250_dc27880873.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-02_utah-supreme-court-order-denying-interlocutory-appeal_dc27880887.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-05_prosecutor-opposition-defendant-motion-disqualify-utah-county-attorney_dkt289_dc27880888.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-08_defendant-reply-prosecutor-opposition-motion-disqualify-public_dkt293_dc27881513.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-09_subpoena-sgt-david-hull_dkt291_dc27881510.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-19_4_dc26493871.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-19_4_dc26493871.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_attachment-A-prosecutor-office-media-guidance_dkt355_dc27881506.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_defendant-renewed-request-to-refer-motion-to-utah-attorney-general_dkt348_dc27881509.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-01-30_prosecutor-opposition-defendant-motion-classify-motion-exclude-still_dkt346_dc27881511.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-02_prosecutor-memorandum-opposition-defendant-renewed-request-motion-disqualify_dkt366_dc27881512.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-02-03_minute-order-evidentiary-hearing-disqualification_dkt413_dc27881507.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-case-history-full_dc27880531.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-case-history-full_dc27880531.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-short-case-history_dc27880533.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15_xchange-short-case-history_dc27880533.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_case-search-utah-state-court-online-xchange-service_dc27880529.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998184.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998188.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-04-02_motion-vacate-continue-march-27-2026_dc27998189.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-23-pub_rev-contempt-hearing-transcript.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-23-pub_rev-contempt-hearing-transcript.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-06-25_reply-states-response-motion-defendant-be-unshackled_dc28324423.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-08_supplemental-notice-access-to-evidence_dc28443912.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-07-08_supplemental-notice-access-to-evidence_dc28443912.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_BLOCKED-DRAFT_q08-dna_DO-NOT-PUBLISH.md` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_Q58-completion-60-verdicts.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_q08-reviews-and-register-proposal.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_round2-Q58-raw-output.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_verification-cycle-raw-output.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-01_verification-cycle-workflow-result.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-11_defendant-prelim-hearing-briefing_ALT-EXTRACTION-dc28551955.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_CRE07-completeness-inventory_RAW-CANDIDATES.jsonl` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_CRE08-completeness-state-filings_RAW-CANDIDATES.jsonl` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-candidate-bank_INDEX.md` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-completeness-day2-bakker_RAW-CANDIDATES.jsonl` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-completeness-day5-oliver_RAW-CANDIDATES.jsonl` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-14_Q61-finder-DNAE01-sections6-14_RAW-CANDIDATES.jsonl` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q140-twiggs-analytic-pass_RAW.md` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_Q70-completion-six-reader-reports_RAW.md` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev-q120-acquisition_RECEIPTS.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev-q120-bodies.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-captures-kirk-shooter.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-captures-kirk-shooter_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-press-conference-on-kirk-shooting.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_fbi-press-conference-on-kirk-shooting_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_press-conference-on-charlie-kirk-shooting.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_press-conference-on-charlie-kirk-shooting_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_update-on-charlie-kirk-shooter.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-16_rev_update-on-charlie-kirk-shooter_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q136-zinn-reconciliation_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q137-Q138-person-files_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q137-Q138-workflow-script.js` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_Q142-Q143-Q144-Q145-twiggs-programme_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_SEC-E01-security-posture_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-17_SEC-E01-workflow-script.js` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-20_Q182-crosswalk-anchors_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-08-20_Q182-crosswalk-locates_RAW.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/2026-09-01_ruling-and-order-on-preliminary-hearing-bindover_signed.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-26.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-27.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-28.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/atf_page-29.png` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc224251_bank_receipts.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc224251_manifest.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/dc_casenumber_bank_receipts.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-artifacts_2026-08-16_NUL-repair.py` | *(stays)* | NOT an artifact but lives inside the raw bank and is cited by path from many files (the DNA draft alone: 89 referrers); leave in place, flagged in §4 | Q8 |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-artifacts_2026-08-16_NUL-repair_SUPERSESSION.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/docket-watch-baseline.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/oct24_clean.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/2026-09-01_final-prelim-argument.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/2026-09-01_final-prelim-argument_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day1.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day1_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2_condensed.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day2_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3_condensed.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day3_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day4.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day4_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5_condensed.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/day5_raw.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/prelim-hearing-transcripts/faumuina_condensed.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-ballistics-motion.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/tyler-robinson-redacted-hearing-transcript.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-08-14B_supplemental-notice-2026-07-08.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-08-14C_xchange-docket.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-08-14_contempt-transcript.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-08-16B_rev-official-statements.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-08-16_documentcloud-complete-sweep.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-08-20_states-reply.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-09-01_hearing-livestream-capture.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/MANIFEST.md` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_c_c_251403576_d_all_loc_all.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_j_j_Graf_d_all_loc_all.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_cal_search.php_t_p_p_Robinson_2C_Tyler_d_all_loc_all.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_judgments_view.php_loc_fourth.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_07_.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_08_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_08_28_public-attendance-for-tyler-robinson-preliminary-hearing_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_01_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_2026_09_02_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news__s_Robinson.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_category_high-profile-cases_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_news_tag_tyler-robinson_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/legacy.utcourts.gov_utc_notices_category_utah_.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/probe_media.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/probe_root.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/provo_robinson.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ua.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ua_media.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/uc_news.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/uc_root.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/ucao_k.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/wb_ckpr_20260613.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_content_utcourts_us_en_about_miscellaneous_directory_court-details.html_id_utah-county-provo-district-court.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_about_news-press.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_about_news.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_court-records-publications_publications_public-notices_courts.html.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_court-records-publications_records_xchange.html.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_courts_court-types_dist_dist-sites_4th.html.raw` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_Media-Policies-Resources.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_high-profile-cases.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_robinson.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_state-v-robinson.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_media_media_tyler-robinson.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_en_news.html.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/court-and-prosecutor/www.utcourts.gov_news_.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/abc.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap1.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap2.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ap3.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/cbs.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/chn_article.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/chn_feed.xml` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/deseret-0901.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/ksl-51618264.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/nbc.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/sltrib-0901.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_1.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_1.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_10.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_10.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_16.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_16.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_17.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_17.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_18.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_18.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_19.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_2.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_2.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_6.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_6.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_7.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_7.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_8.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_8.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_9.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/outlets/utahb_page_9.url.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/dc_proj.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/dc_search.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/rev_day5.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/rev_sitemap_dec.xml` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/xchange.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/transcripts-and-docs/yt.html` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/workflow-results_fetched-and-verdicts.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-ACQ-2026-09-02_bindover-verification-fetches/workflow-synthesis.md` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - Court record/CR-AUDIT-2026-07-27_adversarial-pass.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-AUDIT-2026-07-28_independent-pass.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-AUDIT-2026-08-01_session-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-AUDIT-2026-08-20_session-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E01_prelim-hearing-Day4_Karner-ATF-testimony.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E02_prelim-hearing-Day4_Faumuina-Davis-Twiggs.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E03_prelim-hearing-Days2-3-5.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E04_prelim-hearing-Day2_Hull-UVU-surveillance.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E06_Bakker-Day2_Oliver-Day5_full-read.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E07_defence-prelim-briefing-2026-08-11.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E08_state-information-and-pc-affidavit-2025-09-16.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E09_evidence-preservation-order-and-pretrial-practice.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E10_publicity-order-and-record-classification.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E11_prosecutor-disqualification-track.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E12_closure-classification-and-sealing-map.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E13_evidence-preservation-chain-complete.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E14_continuance-motion-and-the-discovery-record.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E15_ATF-firearms-report-2025-09-17.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E16_participant-roster-and-label-reconciliation.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E17_states-reply-2026-08-18.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E18_certified-transcript-crosswalk.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E19_latent-print-record.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E20_forensic-exhibit-map.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-E21_forensic-discovery-census.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-14_losee-draft-Q07.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16B_xchange-null-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16C_Q61-tranche3.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16D_Q105-null-re-runs.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16E_Q111-legacy-file-audit.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16F_Q89-losee-draft-vs-sworn-geometry.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16G_twiggs-profile-reconciliation.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-16_Q61-carried-nulls.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-17_Q146-Q148-Q131.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-REVIEW-2026-08-30_CR-E19-E20-E21-verification-cycle.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/CR-WATCH-log.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_adjudication-journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_adjudication-journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_finder-defects.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_finder-defects.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_panel-verdicts.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle1_panel-verdicts.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle2_results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_queue.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_queue.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/cycle3_results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_1f229a39-bd3.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_1f229a39-bd3.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_3fe455fb-26a.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_3fe455fb-26a.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_8951c2ef-e9c.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_8951c2ef-e9c.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f2c380ea-788.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f2c380ea-788.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f79b4b05-205.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/journal_wf_f79b4b05-205.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_facts.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_facts.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_questions-that-leaked-their-answers.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_questions-that-leaked-their-answers.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p2_results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_chains.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_chains.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_comparison.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_comparison.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_verdicts.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p3-iteration2_verdicts.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_chains.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_chains.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_steps.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p3_steps.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_queue.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_queue.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-iteration2_results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_applied.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_applied.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_blind-reread.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_blind-reread.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_false-positives.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-repair_false-positives.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_applied.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_applied.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_decisions.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5-secondhand_decisions.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_citations.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_citations.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p5_results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_attack-results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_attack-results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_claim-list-as-attacked.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_claim-list-as-attacked.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p7_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_masked-payloads-sent-to-agents.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_masked-payloads-sent-to-agents.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_source-rebuilds.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_source-rebuilds.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_values-withheld-from-agents.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8-iteration2_values-withheld-from-agents.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_document-ledger-locked-before-results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_document-ledger-locked-before-results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_quantity-census.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_quantity-census.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_source-rebuilds.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p8_source-rebuilds.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_document-attribution-ledger-locked-before-results.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_document-attribution-ledger-locked-before-results.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_journal.jsonl` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_journal.jsonl` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_quotation-census.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_quotation-census.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_source-locations.json` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/p9_source-locations.json` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.0_pre-correction.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.0_pre-correction.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.1_pre-cycle2.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.1_pre-cycle2.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.2_pre-cycle3.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.2_pre-cycle3.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.3_pre-scaffolding-repair.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.3_pre-scaffolding-repair.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.4_pre-P8.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.4_pre-P8.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.5_pre-P9.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.5_pre-P9.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.6_pre-P7.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.6_pre-P7.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.7_pre-P2.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.7_pre-P2.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.9_pre-P8-iteration2.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v1.9_pre-P8-iteration2.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.0_pre-P5-iteration2.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.0_pre-P5-iteration2.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.1_pre-P3-iteration2.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.1_pre-P3-iteration2.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.2_pre-P5-repair.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.2_pre-P5-repair.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - Court record/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.3_pre-secondhand-upgrade.md` | `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/profile_v2.3_pre-secondhand-upgrade.md` | Verification-cycle bank (agent journals, verdicts, snapshots) is process evidence, not court record; move out of the topic folder so the folder holds only evidence files and the artifact bank | Q5 |
| `files - DNA evidence/DNA-E01_DNA-evidence-what-it-can-bear.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - DNA evidence/Kirk-Robinson_DNA-Evidence_Acquisition-Roadmap_2026-07-15.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - DNA evidence/Kirk-Robinson_DNA-Evidence_Consolidated-Audit_2026-07-15.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Event security/2026-08-20_singju-srs254-harpole-transcript.txt` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Event security/2026-08-20_singju-srs254-harpole-transcript_RAW.html` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Event security/SEC-E01_security-posture-2025-09-10.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Event security/SEC-E02_security-team-allegations-assessment.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_obstruction_pca_dc26098558.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_obstruction_pca_dc26098558.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_sex_charges_pca_dc26098557.pdf` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/2025-09-16_zinn_sex_charges_pca_dc26098557.txt` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/dc26098557.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_artifacts/dc26098558.json` | *(stays)* | Raw bank contents: never moved or renamed (data/raw rule; cited by filename/dc-id across the library and indexed by manifest.py) |  |
| `files - George Zinn/ZINN-ACQ-2026-08-20_zinn-pcas.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - George Zinn/ZINN-REVIEW-2026-08-17_partial-reconciliation.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - George Zinn/t1 source acquisition roadmap - George Zinn.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - George Zinn/zinn-george-evidence.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Kirk assassination questions/kirk-shooting-official-timeline.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Kirk assassination questions/t1 source acquisition roadmap - Kirk assassination questions.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Losee building/losee-rooftop-firing-evidence.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `files - Losee building/tier1 source acquisition roadmap - forensic evidence for Losee building shot.md` | *(stays)* | Topic-folder evidence/roadmap/audit file; folder names are the citation namespace (see §7.1) and stay |  |
| `lance-twiggs-comprehensive-profile.md` | `files - Person profiles/lance-twiggs-comprehensive-profile.md` | Three person-level dossiers sit loose at the root while every other evidence file has a topic folder; gives them one, in the existing `files - <Topic>` convention | Q3 |
| `manifest.py` | `scripts/manifest.py` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |
| `migrate-files.sh` | `scripts/migrate-files.sh` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |
| `queue-check.sh` | `scripts/queue-check.sh` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |
| `robinson-tyler-james-comprehensive-profile.md` | `files - Person profiles/robinson-tyler-james-comprehensive-profile.md` | Three person-level dossiers sit loose at the root while every other evidence file has a topic folder; gives them one, in the existing `files - <Topic>` convention | Q3 |
| `source-manifest.json` | *(stays)* | Root entry point or generated index referenced by many files and by scripts/the cloud routine; stays (path references edited only where §7.3 says) |  |
| `tools/build-docx.js` | `scripts/build-docx.js` | Untracked build scripts for the HTML/DOCX renders; commit them next to the other tooling | Q2 |
| `tools/build-html.py` | `scripts/build-html.py` | Untracked build scripts for the HTML/DOCX renders; commit them next to the other tooling | Q2 |
| `tsearch.py` | `scripts/tsearch.py` | All project tooling in one place; each already carries a docstring/usage header; paths inside will be made repo-root-relative from __file__ | Q2 |

---

*End of Phase 1. No file was moved, renamed, edited or deleted. Awaiting approval of §7 and answers to §8 before Phase 2.*
