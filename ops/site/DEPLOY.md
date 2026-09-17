# Deploying the site — the runbook

**Status as of 2026-09-17: NOT DEPLOYED.** Everything below the owner's step is done and tested.
Creating the public surface is the owner's action — both by this library's own rule
(`LOOP.md` §3: outward-facing actions are the owner's) and by the assistant's harness, which
refused it as a "create public surface" action. That refusal was not routed around.

## What is already true

- `netlify.toml` carries the build command and publish directory.
- **The build was tested from a clean checkout on 2026-09-17** — a fresh `git clone` of
  `983c1a7` with **no `.venv-site`**, exactly as Netlify sees it: `pip install -r
  ops/site/requirements.txt && python3 scripts/build-site.py` → **54 pages, 12 MB**, publish
  directory `.site-build/site` present, `robots.txt` = `Disallow: /`, the licence page built,
  and **no held file in the output** (checked: `QUEUE` is absent).
- Indexing is blocked two ways until deliberately flipped: `noindex: true` in
  `ops/site/site.yml`, which emits the `robots.txt`.

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

`ops/site/BUILD-REPORT.md`, regenerated on every build. As of 2026-09-17: **54 published · 42
held · 3 hard-blocked**, every artifact bank excluded wholesale, and 28 of the 54 pages carrying
a `[PROVISIONAL]` banner. Read it before the domain goes on anything.
