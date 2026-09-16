# Kirk Robinson Research

> ### 👉 Opening this workspace after a break? Read **[START-HERE.md](START-HERE.md)**, then **[QUEUE.md](QUEUE.md)**, then **[INDEX.md](INDEX.md)**.

Open-source research library on the September 10, 2025 assassination of Charlie Kirk and the prosecution *State of Utah v. Tyler James Robinson* (Case No. 251403576, Fourth Judicial District Court, Provo). Its purpose is not to prove or debunk any narrative. It separates, claim by claim, what the primary record **establishes** (at a stated source tier and confidence) from what is merely **asserted**, and states graded, falsifiable conclusions with the evidence that would change them.

Two documents govern everything here. **[CLAUDE.md](CLAUDE.md)** says what the library is and how files are written (tiers, registers, the two-layer rule, living-persons care). **[VERIFICATION-PROTOCOL.md](VERIFICATION-PROTOCOL.md)** says how a claim earns the right to be written (the adopted Research Verification Kit: labels, the isolation rule, taint, the three-iteration cap, the sink). Read both before editing any file.

The folder is a git repository (`main`, remote `JudicialNoticing/kirk-robinson-research`, private) and an Obsidian vault.

## Where to start reading

| If you want… | Open |
|---|---|
| The state of play and what is waiting on the owner | `START-HERE.md` |
| Every open item, the D-register ceiling, the standing hazards | `QUEUE.md` |
| One sentence on every significant file, and when you would need it | `INDEX.md` |
| The defendant, end to end | `files - Person profiles/robinson-tyler-james-comprehensive-profile.md` (TJR-P01) |
| What the DNA evidence can and cannot bear | `files - DNA evidence/DNA-E01_DNA-evidence-what-it-can-bear.md` |
| What is held, what is inside it, how to read it | `SOURCE-MANIFEST.md` (generated) |
| How the pieces fit together and how data flows | `docs/ARCHITECTURE.md` |
| Why things are the way they are | `docs/DECISIONS.md` |
| What a term means (tier, label, D-number, PROVISIONAL, U+FFFE…) | `docs/GLOSSARY.md` |
| What the 2026-09-15 reorganisation did and why | `AUDIT.md` |

## Layout

```
CLAUDE.md · VERIFICATION-PROTOCOL.md      the rules
START-HERE.md · QUEUE.md · LOOP.md · DOCKET-WATCH.md    session entry, work graph, execution protocol, court calendar
INDEX.md · AUDIT.md · README.md           finding things
SOURCE-MANIFEST.md · source-manifest.json  generated holdings index (never hand-edited)

files - <Topic>/        the research: evidence files, roadmaps, audits, reviews, acquisition logs,
                        and the artifact banks (raw evidence, never moved or renamed)
  Arrest chronology · Bride of Charlie series · Court record · DNA evidence · Event security ·
  George Zinn · Kirk assassination questions · Losee building · Person profiles
verification/           banks written by verification cycles (agent journals, verdicts, frozen snapshots)
docs/                   architecture, decisions, glossary, the verification kit, and the public
                        discussion framework (docs/discussion-framework/, a T4 import)
scripts/                every tool (run from anywhere; each finds the library root)
ops/docket-watch/       the text deployed on the cloud docket-watch routine, and its pending replacement
deliverables/           rendered outputs shared outside the repo
archive/                superseded material, kept rather than deleted (see archive/README.md)
```

The `files - <Topic>/` folder names and everything inside an artifact bank are the library's **citation namespace**: hundreds of verified sentences cite them by literal path. They do not move or get renamed. Everything else was reorganised around them on 2026-09-15 (`AUDIT.md` §7).

## Tools

All tools live in `scripts/` and resolve the library root from their own location, so they can be run from any directory.

| Command | What it does | When |
|---|---|---|
| `./scripts/queue-check.sh` | Integrity check: Q-IDs unique, blocked-by references resolve, D-register has no gaps, `[PROVISIONAL]` files listed, every bank PDF has a `.txt`, working tree clean. Exit 1 on any problem | Before and after any cycle that touches `QUEUE.md` or the register |
| `./scripts/tsearch.py --validate` then `./scripts/tsearch.py "pattern" --days 4` | Flattened-context search over the five hearing-day transcripts; refuses to report a null until a known positive is found | Any search of `day1`–`day5.txt` |
| `python3 scripts/artifact_search.py [bank-dir]` | Defect census of the court bank (NUL bytes must be 0; U+FFFE splits ≈131 by design). Import `find()` to search an artifact under **both** readings of every split word | Any null claimed against a banked `.txt` |
| `./scripts/manifest.py` | Regenerates `SOURCE-MANIFEST.md` and `source-manifest.json`: every artifact's hash, class, readability hazard, how to read it, and which files cite it. Needs poppler (`pdftotext`, `pdfinfo`) | After banking, moving or citing anything. ⚠ `--check` also regenerates; it is not yet a dry run |
| `./scripts/docket-watch-run.py` | Local docket check (DocumentCloud, Wayback, Rev, Utah Courts) diffed against a stored baseline; prints a report to paste into `files - Court record/CR-WATCH-log.md`. Network | When the cloud routine cannot cover a deadline |
| `python3 scripts/build-html.py <md> <html>` · `node scripts/build-docx.js <md> <docx>` | Rebuild the deliverables from a markdown source. Node needs the `docx` module | After any change to TJR-P01 |
| `./scripts/migrate-files.sh <src> <dst>` | Non-destructive verified copy of a folder (counts and bytes checked) | Bulk file moves outside git |

## Conventions in one breath

Four source tiers (T1 sworn/primary → T4 anonymous), with "T1 via T3" when a primary is known only through reporting. Confidence grades trace to a verification act, never to repetition. Every file keeps a **recording layer** (what a claimant said) apart from an **analyst layer** (what the record establishes). Cross-file registers: `D-` discrepancies, `V-` verification items, `F-` flags, `M-` roadmap mechanics, `Q-` queue items. `[PROVISIONAL]` means labels incomplete for the stated scope, not "wrong", and such findings may not be cited elsewhere. Corrections are made in place with a revision-log row; protected names are removed, never struck through. Full definitions: `docs/GLOSSARY.md`.

## History

Consolidated 2026-07-26 from `~/Desktop/Kirk Staging` (69 files, byte-verified). Verification kit adopted 2026-09-14. Reorganised 2026-09-15 (`AUDIT.md`).
