# archive/ — superseded material, kept rather than deleted

Nothing in this folder is current. Each item is here because something newer replaced it, and the library's rule is to archive, never delete. Moved here on **2026-09-15** in the Phase 2 reorganisation (`AUDIT.md` §7). Git history for every file is preserved (`git log --follow`).

## docket-watch-prompts/

Four superseded drafts of the cloud routine's prompt. Each later draft names the one it replaced, so the chain is: 08-14 → 08-16 → 08-17 → 09-02 → **09-14 (current draft, in `ops/docket-watch/`)**. The text actually deployed on the routine is `ops/docket-watch/DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md`.

| File | Was at | Superseded by | Why keep it |
|---|---|---|---|
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md` | repo root | the 08-16 draft | It was the text applied to the routine on 2026-08-14 (DOCKET-WATCH.md §history); the application record cites it |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-16.md` | repo root | the 08-17 draft | Draft and application record, linked from DOCKET-WATCH.md |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-17.md` | repo root | the 09-02 draft | Draft and application record, linked from DOCKET-WATCH.md and QUEUE.md; `CR-WATCH-log.md` line 539 still links it at the old root path |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-02.md` | repo root | the 09-14 draft | Written for the post-bindover window before the order and transcript were acquired; cited by name in START-HERE and CR-WATCH-log |

## verification-kit-drop/

| File | Was at | Replaced by | Why keep it |
|---|---|---|---|
| `COMPLETE-DROP-FILE.md` | `VerificationAndFactCheckProtocol copy/` | the byte-identical copy inside `docs/research-verification-kit/`, which the kit's `MANIFEST.md` names as the fallback | Provenance of the 2026-09-14 15:41 drop (VERIFICATION-PROTOCOL.md §0) |
| `research-verification-kit.zip` | `VerificationAndFactCheckProtocol copy/` | the extracted, hash-verified kit in `docs/research-verification-kit/` | The original delivery artifact |

## What is deliberately NOT here

- The two `DO-NOT-PUBLISH` drafts, the `_RAW.md` reports and the one-off scripts inside `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/` stay where they are: 89 files cite the DNA draft by that path (AUDIT.md §4.3, owner decision Q8).
- The 23 MB mis-banked federal filing stays in the bank: 23 files cite it as the named exclusion and `scripts/queue-check.sh` counts it (Q9).
- The 13 `profile_v*.md` snapshots in `verification/TJR-REVIEW-2026-09-14_verification-cycle-1/` are frozen baselines, not stale copies.
