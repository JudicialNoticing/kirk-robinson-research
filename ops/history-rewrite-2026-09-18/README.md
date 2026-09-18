# The 2026-09-18 history rewrite — what changed, and how to resolve an old hash

**Prepared:** 2026-09-18 · **Status:** v1.0 · **Queue item:** Q-198

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

    grep '^983c1a7' ops/history-rewrite-2026-09-18/commit-crosswalk.txt

## What was repaired, and what was deliberately left alone

**Repaired — 77 citations across 18 live documents.** `START-HERE.md` (32), `QUEUE.md` (9),
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
| Identifier in any blob of any commit (1,266 blobs scanned) | **0** |
| Identifier in any path in history | **0** |
| Binary artifacts byte-identical (82 PDFs, images, `.docx`) | **82 / 82 unchanged** |
| `git fsck` | clean |

⚠ **The binary check is not a formality.** A byte-level replacement that changes string length
inside a PDF corrupts its cross-reference table silently. `git-filter-repo` skips blobs containing
NUL bytes, which is why the banked filings survived untouched — **and is also why one compiled
`.pyc` in history kept the path string and had to be removed by a separate pass.** A text-only
sweep would have reported success and been wrong; see [[render-dont-grep]] for the same shape.

## What this does NOT reach

- **Objects GitHub already held.** The force-push leaves the pre-rewrite commits unreferenced but
  present on GitHub's side until it garbage-collects them. They are unreachable to anyone who
  cannot already read the repository. 🚨 **The repository was made private on 2026-09-18, which is
  what makes that acceptable. Before it is ever made public again, ask GitHub Support to purge
  unreachable objects, or delete and recreate the repository.** This is a prerequisite, not a
  nicety: this library publishes its own commit hashes, so the old ones are a working index.
- **Anything already copied** by a third party while the repository was public.
- **Accounts named after the owner.** The Netlify team slug and one GitHub account still carry the
  name; those are platform settings, not repository content.

## Reproducing or reverting

The pre-rewrite repository is backed up in full at
`~/Documents/kirk-repo-history-backup-2026-09-18/git-dir-copy` (95 MB, 212 commits, all 7 original
refs, `fsck` clean). It is **outside this repository and outside any backup this repository
performs** — it contains exactly what the rewrite removed, so treat it as sensitive and delete it
once you are satisfied.

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-18 | Written at the rewrite (Q-198). |
