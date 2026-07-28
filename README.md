# Kirk Robinson Research

> ### 👉 Opening this workspace after a break? Read **[START-HERE.md](START-HERE.md)** first.
> The first five minutes, what is time-critical on the court calendar, the decisions waiting on you, a recommended work order, and the traps. Written at the close of each working session.

Open-source research library on the September 10, 2025 assassination of Charlie Kirk (*State of Utah v. Tyler James Robinson*) — claim inventories, Tier 1 source-acquisition roadmaps, and evidence dossiers. Methodology, sourcing tiers, register conventions, and file rules live in [CLAUDE.md](CLAUDE.md); read it before adding or editing any file.

This folder is both a git repository and an Obsidian vault. It was consolidated from `~/Desktop/Kirk Staging` on 2026-07-26 (69 files, byte-verified).

## Topic folders

- `files - Arrest chronology` — Robinson surrender timeline and acquisition roadmap
- `files - Bride of Charlie series` — claim inventories for Candace Owens' episodes E01–E08, library/session audits, phase-0 pull logs, and archived web artifacts
- `files - DNA evidence` — consolidated audit and acquisition roadmap
- `files - George Zinn` — evidence file and roadmap
- `files - Kirk assassination questions` — official shooting timeline and roadmap
- `files - Losee building` — rooftop firing evidence and forensic-source roadmap

## Root dossiers

- `erika-kirk-background-family-contested-claims-dossier.md`
- `lance-twiggs-comprehensive-profile.md`
- `evidence-rifle-photo-nypost-authenticity.md`

## Tools

- `migrate-files.sh` — non-destructive verified copy of a research folder (used for all bulk file moves per CLAUDE.md operational rules)
- `tsearch.py` — flattened-context search over the banked hearing transcripts. **Validates its method against a known positive before every query**, because the transcripts' timestamp-block structure silently defeats naive fixed-width grep (BOC-AUDIT-2026-07-27B §4). Run `./tsearch.py --validate` after any change to the artifacts folder

## Autonomous operation

- **[START-HERE.md](START-HERE.md)** — session entry point. Time-critical docket state, decisions awaiting the user, recommended work order, active traps.
- **[QUEUE.md](QUEUE.md)** — the work graph. Every open item across the library, with its decisive artifact, blockers, cost and gate. This is what a loop dispatches from.
- **[LOOP.md](LOOP.md)** — the execution protocol. Cycle definition, the provisional-findings rule, three gates with an always-human list, and hard stops. Written out of four real failures on 2026-07-27.
- **[DOCKET-WATCH.md](DOCKET-WATCH.md)** — the calendar-driven half. Court deadlines through the bindover ruling; may acquire, may never touch case posture.
- **`./queue-check.sh`** — integrity check for the queue and register. Run before and after any cycle.
