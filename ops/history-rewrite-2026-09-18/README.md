# The 2026-09-18 history rewrite — what changed, and how to resolve an old hash

**Prepared:** 2026-09-18 · **Status:** v1.1 · **Queue item:** Q-198

🚨 **NOT PUSHED AS OF 2026-09-18. The rewrite exists only on this machine; `origin` still carries the pre-rewrite history.** See *Finishing this* at the foot of the file.

## What happened

Every commit in this repository was rewritten on 2026-09-18. The repository's entire history —
all 212 commits on all 5 refs — now carries the pen name **William Whitehead** as author and
committer, and carries no personal filesystem paths, account handles or email addresses.

Before the rewrite the history carried, in files and in commit metadata, the owner's legal name,
their macOS username as an absolute path (`/Users/<username>/Documents/Kirk Robinson Research`,
3,186 occurrences), a machine-default commit email on the initial commit, and a personal Google
address in six places. **Editing files could not reach any of it** — that is the whole reason a
rewrite was needed, and it is the same lesson the library already recorded when three protected
surnames were removed in place and remained retrievable from the parent commit.

## What this means for a hash you are holding

🚨 **Every commit hash written down before 2026-09-18 is dead.** A file, a note or a session log
that cites `983c1a7` or `8910af3` is citing a commit that no longer exists.

`commit-crosswalk.txt` in this folder maps **old → new** for all 212 commits, tab-separated, full
40-character hashes. To resolve a short hash, match it as a prefix of the left column.

🚨 **`git-filter-repo` composes its commit-map across runs.** Each pass writes a map keyed by the
**original** hash that yields *that pass's* output — so **the final pass's map IS the old→new
crosswalk.** Chaining the per-pass maps together double-applies them and produces hashes that
never existed. This file was first written that wrong way on 2026-09-18 and corrected the same
day, after a check found its targets were not objects in this repository. **When you build a
crosswalk, verify the right-hand column with `git cat-file --batch-check` before trusting it** —
a map that maps to nothing looks exactly like a map that works.

    grep '^983c1a7' ops/history-rewrite-2026-09-18/commit-crosswalk.txt

## What was repaired, and what was deliberately left alone

**Repaired — 75 citations across 18 live documents** (77 on the first, wrong pass; see the v1.1 row). `START-HERE.md` (32), `QUEUE.md` (9),
`CR-WATCH-log.md` (7), `ops/site/DEPLOY.md` (7), `CR-AUDIT-2026-08-20` (4), and fourteen others
including four evidence files and one comment in `scripts/queue-check.sh`. These are documents
someone acts on, so a dead hash in them is a broken instruction.

**Left alone — 1,220 citations in frozen records.** 1,174 in `verification/` cycle banks and 46
inside artifact-bank subdirectories. **These are records of what was written at the time, and
rewriting them would make them disagree with the process they document.** The recording layer is
not corrected to match a later state; that is the project's prime directive. Use the crosswalk
when reading them.

## What was verified after the rewrite

| Check | Result |
| --- | --- |
| Commits preserved | 212 → 212, no commit dropped (`--prune-empty never`) |
| Refs preserved | all 5 |
| Author/committer names across all history | one name only, plus `Claude` / `Claude Code` on 4 tool commits |
| Author/committer emails | two only, both no-reply; no personal address |
| Identifier in any commit message | 0 |
| Identifier in any blob of any commit (1,288 blobs scanned) | **0** |
| Identifier in any path in history | **0** |
| Binary artifacts byte-identical (82 PDFs, images, `.docx`) | **82 / 82 unchanged** |
| `git fsck` | clean |

⚠ **The binary check is not a formality.** A byte-level replacement that changes string length
inside a PDF corrupts its cross-reference table silently. `git-filter-repo` skips blobs containing
NUL bytes, which is why the banked filings survived untouched — **and is also why one compiled
`.pyc` in history kept the path string and had to be removed by a separate pass.** A text-only
sweep would have reported success and been wrong; see [[render-dont-grep]] for the same shape.

## What this does NOT reach

- **Objects GitHub already held** *(once the push happens)*. A force-push leaves the pre-rewrite commits unreferenced but
  present on GitHub's side until it garbage-collects them. They are unreachable to anyone who
  cannot already read the repository. 🚨 **The repository was made private on 2026-09-18, which is
  what makes that acceptable. Before it is ever made public again, ask GitHub Support to purge
  unreachable objects, or delete and recreate the repository.** This is a prerequisite, not a
  nicety: this library publishes its own commit hashes, so the old ones are a working index.
- **Anything already copied** by a third party while the repository was public.
- **Accounts named after the owner.** The Netlify team slug and one GitHub account still carry the
  name; those are platform settings, not repository content.

## Finishing this — the push has NOT happened

The rewrite is committed locally and verified. `origin` is configured again. **What remains:**

    git push --force origin main
    git push --force origin claude/docket-watch-run-10-2026-09-16

Those were the only two branches on the remote when the rewrite was made. Before running them,
re-check that nothing new has landed:

    git ls-remote --heads origin

🚨 **The docket-watch routine fires Sat 2026-09-19 13:00Z and writes a `claude/` branch.** If it
runs before the force-push, that branch is built on the **pre-rewrite** history and will not merge
cleanly afterwards. **Either push before it fires, or expect to rebase or re-run it.**

✅ **Nothing public carries the name in the meantime.** The live site's `/licence/` page was
deployed from the pen-name commit earlier the same day and was re-fetched to confirm it; the
repository is private; and the site still serves `robots.txt: Disallow: /`.

## 2026-11-26 — the routine kept writing to the OLD history, so the planned force-push became destructive

🚨 **Between 2026-09-19 and 2026-11-25 the docket-watch routine (`trig_016faLfbQWCz72M463Dy8HsL`) fired 21 times onto `origin/main`, which still carried the pre-rewrite history, and committed and pushed its own rows each time (Runs 11–30, plus the Run 24 correction).** `origin/main` moved from `fa305ef` (old) to `787cf95`. **The `git push --force origin main` this file's *Finishing this* section prescribed would have deleted all 21 commits** — two months of docket record — and nobody had re-checked the remote before re-reading that instruction. *A prescribed command is a claim about the state it was written against; re-check the state before running it.*

**What was done (2026-11-26, Claude Code, local only — nothing pushed):**
1. **The 21 commits were replayed onto the rewritten `main` (`e23a526`) as 21 commits**, each with its original message, author date and committer date. They touch exactly two files, `DOCKET-WATCH.md` and `files - Court record/CR-WATCH-log.md`.
2. **The rewrite's effect on those two files was measured, not assumed: it is exactly three string substitutions** — `d813dea`→`287c726`, `33bd7ec`→`51c6ee3`, and the account handle → `personal-account`. `sub(fa305ef:file) == e23a526:file` byte-for-byte for both files. Each replayed commit's files are therefore `sub(original)`; **verified for all 21 commits × 2 files, 0 mismatches.** One citation the routine added after the rewrite (Run 11 quoting Run 10's checkout `d813dea`) is carried to `287c726` by the same substitution — the same treatment that hash already had everywhere else in the file.
3. **Two routine commits carried the owner's personal email as author/committer** (Run 14 `eb2598f`, Run 17 `c75c354`; Run 17's author name was the account handle). Both normalised to `noreply@anthropic.com` / `Claude`; **every other author and committer field is unchanged.** Both run rows state they were cloud firings.
4. **Verified:** tree outside the two files identical to `e23a526`; 21/21 messages identical; 0 personal identifiers in the added content or metadata; all 21 new objects resolve (`git cat-file --batch-check`). **A clean clone of the result builds the site green** with a fresh venv outside iCloud: 55 published · 43 held · 3 hard-blocked · `robots.txt` = `Disallow: /` · 0 held files and 0 identifier hits in the output.
5. **Old → new map for the 21 commits:** [`commit-crosswalk-transplant-2026-11-26.txt`](commit-crosswalk-transplant-2026-11-26.txt), same format as the main crosswalk. **The routine's own rows cite their old hashes; they were left as written** (frozen-record rule) — resolve them through this map.

🚨 **A RESIDUE THE 09-18 VERIFICATION DID NOT SEE — truncated forms of the home path.** A full-history byte scan on 2026-11-26 (all 2,235 objects of the reconciled history) found **no full identifier**, but found **prefixes of the absolute home path cut off by an ellipsis** (`/Users/<first 5–11 characters of the username>…`) in agent-journal summaries inside three `*_RAW*.json` artifacts in `files - Court record/CR-ACQ-2026-07-27_court-record-artifacts/` (2026-08-17 batch). **Two of the three are still in the current tree; one exists in history only.** `--replace-text` matched the full string and the truncation defeated it — **an identifier has forms, and a truncated form is one of them.** Not published (artifact banks are excluded wholesale from the site) and the repository is private. **Not fixed: whether to edit in place, add a filter pass, or fold it into the delete-and-recreate route is the owner's call — `QUEUE.md` Q-199.** ⚠ This also means the *"0 hits across all blobs"* row in the table above was true **of the forms searched**, not of every form.

## Reproducing or reverting

The pre-rewrite repository is backed up in full at
`~/Documents/kirk-repo-history-backup-2026-09-18/git-dir-copy` (95 MB, 212 commits, all 7 original
refs, `fsck` clean). It is **outside this repository and outside any backup this repository
performs** — it contains exactly what the rewrite removed, so treat it as sensitive and delete it
once you are satisfied.

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-18 | Written at the rewrite (Q-198). |
| 1.2 | 2026-11-26 | **The 21 routine commits written onto the old history were replayed onto the rewritten one, locally; push still pending (Q-199).** New section above; new file `commit-crosswalk-transplant-2026-11-26.txt`; a truncated-path residue found by a full-history byte scan and recorded, not fixed. The banner at the top still reads *not pushed*, and that remains true. |
| 1.1 | 2026-09-18 | 🛠 **Crosswalk corrected.** It had been built by chaining the three per-pass commit-maps, which double-applies a mapping `filter-repo` has already composed; all 212 targets were dead hashes, and the 77 citations repaired from it pointed at commits that never existed. Rebuilt from the final pass's map alone; 75 citations re-repaired; both columns verified to resolve. |
