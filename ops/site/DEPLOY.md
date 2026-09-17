# Deploying the site — the runbook

**Status: NOT DEPLOYED. Deferred by the owner on 2026-09-17 to the next session.** Everything below
the owner's step is done and tested.
Creating the public surface is the owner's action — both by this library's own rule
(`LOOP.md` §3: outward-facing actions are the owner's) and by the assistant's harness, which
refused it as a "create public surface" action. That refusal was not routed around.

## What is already true

- `netlify.toml` carries the build command and publish directory.
> 🛠 **The numbers in this table are from the `c672f06` pre-flight and are now STALE: the site is **55 pages**, not 54,
> since `CR-E22` was added on 2026-09-17 (28 of 54 provisional → **29 of 55**; held stays 43).
> **This is exactly why the three-command check below exists — run it and read the report, do not deploy from this table.**
> The table is left as the record of what was tested at that commit.

- **The build was tested from a clean checkout on 2026-09-17, at commit `c672f06`** — a fresh
  `git clone` with **no `.venv-site`** and the virtualenv **outside** the working tree, which is
  what Netlify does: `pip install -r ops/site/requirements.txt && python3 scripts/build-site.py`.
  Checked against the built artifact, not against the config meant to produce it:

  | Check | Result |
  |---|---|
  | pages built | **54** |
  | publish directory `.site-build/site` | present, 12 MB |
  | `robots.txt` | `User-agent: *` / `Disallow: /` |
  | `QUEUE` published | no |
  | `START-HERE` published | no |
  | artifact-bank files published | **0** |
  | unclassified markdown files | none |
  | licence page | built |
- Indexing is blocked two ways until deliberately flipped: `noindex: true` in
  `ops/site/site.yml`, which emits the `robots.txt`.

## Before you deploy next session — three commands, two minutes

The build was tested against a specific commit. Between then and the deploy, `main` may have
moved: **the docket-watch routine fires Sat 2026-09-19 13:00Z** and lands a `claude/` branch to
review and merge. Re-establish the ground rather than trusting this file's numbers.

    git pull                                              # and merge any claude/ branch first
    ./.venv-site/bin/python scripts/build-site.py         # rebuild from the current tree
    open ops/site/BUILD-REPORT.md                         # read the counts before deploying

**Look for one thing in particular: the `🚨 Unclassified` section.** The allow-list denies by
default, so a markdown file added since `site.yml` was written is **silently absent from the
site** — not visibly excluded, just gone. The build names them; if that section exists, every
file in it needs a state in `ops/site/site.yml` before you deploy. As of 2026-09-17 the section
is absent, which is what "ready" looks like.

Expected as of 2026-09-17 (second session): **55 published · 43 held · 3 hard-blocked**, **29 of
the 55** pages carrying a `[PROVISIONAL]` banner, `robots.txt` = `Disallow: /`.
🛠 *Read "54 · 28" until `CR-E22` landed. Corrected 2026-09-17; the figure that governs is always
the one `BUILD-REPORT.md` prints on the run you just did, never a figure in this file.*

## 🚨 PREREQUISITE THE FIRST VERSION OF THIS RUNBOOK NEVER STATED: PUSH FIRST

**Continuous deployment builds from GitHub `main`, not from your disk.** So a local commit that
has not been pushed **is not in the deployed site**, and the three-command check above will
disagree with what Netlify builds — the check reads your working tree, Netlify reads the remote.

    git status -sb        # expect "## main...origin/main" with no "ahead"
    git push              # if it says ahead

⚠ **Before any push, run the standing check** (`boc-state-current`): `git merge-base --is-ancestor
8910af3 origin/main`. It must succeed — it confirms the surname-removal commit is already public,
so the push exposes no withdrawn name that is not already exposed. *(Verified true on 2026-09-17.)*

**As of 2026-09-17, second session, `main` is 3 commits ahead of `origin/main`** (`81bd640`,
`0d186cd`, `ee4cf69`). **Deploying before pushing would publish the 54-page site without `CR-E22`.**

## The owner's step — continuous deployment (recommended)

In the Netlify UI, on the `personal-account` team:

1. **Add new site → Import an existing project → GitHub**, authorise if asked.
2. Pick **`JudicialNoticing/kirk-robinson-research`**.
3. Netlify reads `netlify.toml`; **do not override** the build command or publish directory.
4. Set the site name (suggested: `kirk-robinson-research` → `kirk-robinson-research.netlify.app`).
5. Deploy.

**Why continuous deployment rather than a one-off upload:** it keeps the invariant the whole
design rests on — the site is regenerated from the markdown on every push, so there is never a
separate rendered copy that can drift. A hand-uploaded build is exactly the defect `Q-188` was.

### Fallback, if you would rather not grant Netlify access to GitHub

    netlify sites:create --name kirk-robinson-research
    netlify link --name kirk-robinson-research
    ./.venv-site/bin/python scripts/build-site.py
    netlify deploy --prod --dir=.site-build/site

⚠ **This path deploys whatever is on your disk, not what is on `main`.** If you use it, rebuild
immediately before every deploy and never deploy from a dirty working tree.

## After the first deploy

1. **Read the live site before telling anyone it exists.** It is `noindex` and unlisted, so this
   is a genuine preview.
2. Then decide, and they are separate decisions:
   - **the domain** — a custom domain, or stay on `*.netlify.app`;
   - **indexing** — flip `noindex: false` in `ops/site/site.yml`, push, and the `robots.txt`
     changes on the next build. ⚠ **Indexing is the irreversible-in-practice step:** once search
     engines and archives have crawled the pages, taking the site down does not take back what
     was copied.
3. Set `site.url` in `ops/site/site.yml` once the address is settled.

## What the site does NOT contain

`ops/site/BUILD-REPORT.md`, regenerated on every build. As of 2026-09-17 (second session):
**55 published · 43 held · 3 hard-blocked**, every artifact bank excluded wholesale, and **29 of
the 55** pages carrying a `[PROVISIONAL]` banner. Read it before the domain goes on anything.
🛠 *Corrected 2026-09-17 from "54 · 28".*
