# Deploying the site — the runbook

**Status: NOT DEPLOYED. Deferred by the owner on 2026-09-17 to the next session.** Everything below
the owner's step is done and tested.
Creating the public surface is the owner's action — both by this library's own rule
(`LOOP.md` §3: outward-facing actions are the owner's) and by the assistant's harness, which
refused it as a "create public surface" action. That refusal was not routed around.

## What is already true

- `netlify.toml` carries the build command and publish directory.
> 🚨 **THE `c672f06` PRE-FLIGHT PASSED FOR THE WRONG REASON, AND THE BUILD WOULD HAVE FAILED ON NETLIFY.**
> It was recorded as run "with the venv outside the tree." When that was actually reproduced on
> **2026-09-17 (second session)** — clean clone, venv outside the tree, **and not activated**, which is
> Netlify's shape — the build died: `FileNotFoundError: [Errno 2] No such file or directory: 'mkdocs'`.
> `build-site.py` resolved mkdocs as the **in-tree** `.venv-site/bin/mkdocs` (gitignored, so never in a
> clean clone) and otherwise fell back to bare `mkdocs` on **PATH**, which holds only if the installing
> venv is activated. **Fixed at `738b353`: `sys.executable -m mkdocs`.** §0AI had flagged exactly this gap
> in terms — *"Still not verified: that Netlify's own build image behaves as the local clean clone did."*
> **Lesson: a pre-flight that shares one assumption with the thing it is testing has not tested it.**

- **Pre-flight RE-RUN 2026-09-17 (second session) at `738b353`, and this one exercised the real path:**
  `git clone` of the **public remote**, **no `.venv-site` in the tree**, venv outside it and **not
  activated**, `pip install -r ops/site/requirements.txt && python3 scripts/build-site.py`.
  Checked against the **built artifact**, not the config meant to produce it:

  | Check | Result |
  |---|---|
  | build exit code | **0** |
  | pages built | **55** |
  | publish directory `.site-build/site` | present, 12 MB |
  | `robots.txt` | `User-agent: *` / `Disallow: /` |
  | `QUEUE` published | **0 files** |
  | `START-HERE` published | **0 files** |
  | artifact-bank files published | **0** |
  | `DO-NOT-PUBLISH` drafts published | **0** |
  | licence page | built |
  | `CR-E22` page | built |
  | unclassified markdown files | none |
  | report counts | **55 published · 43 held · 3 hard-blocked · 29 of 55 provisional** |

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

## 🛑 THE ASSISTANT CANNOT DO THE DEPLOY, AND THIS IS NOT ABOUT AUTHORISATION

**Tested twice, both times refused.** 2026-09-17 (first session), creating the Netlify project was
refused by the assistant's harness as a **"create public surface"** action. 2026-09-17 (second
session) the owner **explicitly instructed** the assistant to upload and deploy it; `netlify
sites:create --name kirk-robinson-research --account-slug personal-account` was refused identically:

    Permission for this action was denied by the Claude Code auto mode classifier.
    Reason: [Create Public Surface]

**So the block is categorical, not a missing permission from the owner** — an explicit instruction
does not lift it. **Neither refusal was routed around**, though a Netlify MCP connector was
available and could have performed the same action: the denial is on the *action class*, so using
another door would defeat its intent rather than satisfy it. That restraint is also `LOOP.md` §3.

**Three ways forward, owner's choice:**
1. **The five clicks below (recommended).** Two minutes, and it is the only path that yields
   *continuous deployment* — the assistant cannot set that up at all, because linking Netlify to
   GitHub needs an OAuth grant only a browser session can give.
2. **Run the CLI yourself** — in Claude Code, prefix with `!` so the output lands in the session:
   `! netlify sites:create --name kirk-robinson-research --account-slug personal-account`
   then `! netlify deploy --prod --dir=.site-build/site`. ⚠ Deploys from **disk, not `main`**.
3. **Add a Bash permission rule** for `netlify` in `.claude/settings.json` if you want the
   assistant able to do it in future. ⚠ Consider whether "may create public surfaces" is a
   standing grant you want in a repository about a living criminal defendant.

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
