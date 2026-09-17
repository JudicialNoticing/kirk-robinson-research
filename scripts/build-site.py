#!/usr/bin/env python3
"""Static-site builder for the Kirk Robinson Research library.

    python3 scripts/build-site.py            # stage + build into .site-build/site/
    python3 scripts/build-site.py --serve     # stage + live-reload preview on localhost
    python3 scripts/build-site.py --report    # stage nothing, just print what would publish

Design constraints this script exists to honour:

  * The `files - <Topic>/` namespace is FROZEN (CLAUDE.md, AUDIT.md §7). Nothing here moves,
    renames or writes into it. Publishable copies are STAGED into .site-build/src/.
  * Nothing is published by being present on disk. `ops/site/site.yml` is an allow-list;
    a file appears on the site only if it is marked `publish` there.
  * The site is GENERATED on every build, never hand-maintained — so there is exactly one
    source of truth and no separate derived copy to sweep. (Cycle 3's lesson: derived
    deliverables leave the repo and get missed. Q-188 was that defect.)
  * Every page carries its source file's path, version and status token, so a stale read is
    visible ON the page rather than inferable from a filename.

Created 2026-09-17 (Phase 1, local only — nothing is deployed by running this).
"""
import argparse, html, json, os, re, shutil, subprocess, sys, urllib.parse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / '.site-build'
SRC = BUILD / 'src'
CFG = BUILD / 'mkdocs.yml'
OUT = BUILD / 'site'
REPORT = ROOT / 'ops' / 'site' / 'BUILD-REPORT.md'

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing — run: ./.venv-site/bin/python scripts/build-site.py ...")


# ---------------------------------------------------------------- source facts

STATUS_RE = re.compile(r'^\*\*Status(?:/version)?:\*\*\s*(.+)$', re.M)
# Some files state the version in a `**Compiled:** … **Version 1.7**` line instead.
ALTVER_RE = re.compile(r'\*\*Version\s+(\d+\.\d+)\*\*')
VERSION_RE = re.compile(r'v(\d+\.\d+)')
REVROW_RE = re.compile(r'^\|\s*\**v?([0-9]+\.[0-9]+)\**\s*\|\s*\**(\d{4}-\d{2}-\d{2})\**\s*\|', re.M)


def strip_md(s, limit=None):
    s = re.sub(r'`([^`]*)`', r'\1', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:limit].rstrip() + '…' if limit and len(s) > limit else s


def read_facts(text):
    """What the file says about itself. Reported, never inferred — if it is not stated,
    this returns None and the banner says so rather than guessing."""
    f = {'version': None, 'status_line': None, 'provisional': False,
         'verified_token': False, 'last_revision': None, 'version_from': 'status line'}
    m = STATUS_RE.search(text)
    if m:
        f['status_line'] = strip_md(m.group(1), 300)
        v = VERSION_RE.search(m.group(1))
        if v:
            f['version'] = 'v' + v.group(1)
    if not f['version']:
        a = ALTVER_RE.search(text)
        if a:
            f['version'] = 'v' + a.group(1)
    f['provisional'] = '[PROVISIONAL]' in text or '`[PROVISIONAL]`' in text
    f['verified_token'] = bool(re.search(r'\[VERIFIED\]', text))
    rows = REVROW_RE.findall(text)
    if rows:
        f['last_revision'] = max(d for _, d in rows)
        if not f['version']:
            # Stated in the revision log rather than in a status line. Reported, not inferred.
            top = max(rows, key=lambda r: [int(x) for x in r[0].split('.')])
            f['version'] = 'v' + top[0]
            f['version_from'] = 'revision log'
    return f


# ---------------------------------------------------------------- link rewriting

LINK_RE = re.compile(r'(?<!!)\[([^\]\n]*)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')


def resolve(src_rel: Path, target: str):
    """Resolve a relative markdown link to a repo-relative POSIX path, or None."""
    t = target.split('#', 1)[0]
    if not t:
        return None, target.split('#', 1)[1] if '#' in target else ''
    t = urllib.parse.unquote(t)
    base = (ROOT / src_rel).parent
    try:
        p = (base / t).resolve()
        rel = p.relative_to(ROOT)
    except (ValueError, OSError):
        return None, ''
    anchor = target.split('#', 1)[1] if '#' in target else ''
    return rel.as_posix(), anchor


def rewrite_links(text, src_rel: Path, urlmap, stats):
    def sub(m):
        label, target = m.group(1), m.group(2)
        if re.match(r'^(https?:|mailto:|tel:|#|data:)', target):
            return m.group(0)
        rel, anchor = resolve(src_rel, target)
        if rel is None:
            return m.group(0)
        if rel in urlmap:
            stats['internal'] += 1
            u = '/' + urlmap[rel].lstrip('/')
            if not u.endswith('/'):
                u += '/'
            return f'[{label}]({u}{"#" + anchor if anchor else ""})'
        # Target exists in the repository but is not published. Do not emit a dead link
        # and do not silently assume a GitHub URL — repo visibility is a Phase 2 gate.
        stats['unlinked'] += 1
        stats['unlinked_targets'].setdefault(rel, 0)
        stats['unlinked_targets'][rel] += 1
        return f'{label} <span class="unpublished" title="Source file not published">[not published]</span>'
    return LINK_RE.sub(sub, text)


# ---------------------------------------------------------------- banner

CASE_RE = re.compile(r'Robinson|251403576|Charlie Kirk', re.I)


def banner(src_rel, facts, posture_text, add_posture):
    b = []
    bits = []
    if facts['version']:
        via = '' if facts.get('version_from') == 'status line' else ' (from its revision log)'
        bits.append(f"**{facts['version']}**{via}")
    else:
        bits.append("**no version stated in the source**")
    if facts['last_revision']:
        bits.append(f"last revision **{facts['last_revision']}**")
    b.append('!!! abstract "Source of this page"')
    b.append(f"    Generated from `{src_rel}` — " + ', '.join(bits) + '.')
    b.append(f"    Built {date.today().isoformat()}. The markdown file is authoritative; this page is a render of it.")
    b.append('')
    if facts['provisional']:
        b.append('!!! danger "`[PROVISIONAL]` — not certified, not citable"')
        b.append('    This file carries the `[PROVISIONAL]` token. Its findings have not completed an')
        b.append('    independent verification cycle. It is **not citable by another file, not**')
        b.append('    **propagatable to another topic, and not usable to resolve a register entry.**')
        b.append('    No file in this library certifies itself as verified.')
        b.append('')
    if add_posture:
        b.append('!!! note "Case posture, as of 2026-09-16"')
        b.append('    ' + posture_text.strip())
        b.append('    Allegations are attributed, never adopted.')
        b.append('')
    return '\n'.join(b)


def inject(text, block):
    """Place the banner after the H1 if there is one, else at the top."""
    lines = text.split('\n')
    for i, ln in enumerate(lines[:40]):
        if ln.startswith('# '):
            return '\n'.join(lines[:i + 1]) + '\n\n' + block + '\n' + '\n'.join(lines[i + 1:])
    return block + '\n' + text


# ---------------------------------------------------------------- main

def load_cfg():
    with open(ROOT / 'ops' / 'site' / 'site.yml', encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def collect(cfg):
    pub, hold, never = [], [], []
    for sec in cfg.get('pages', []):
        for it in sec.get('items', []):
            rec = dict(it, section=sec['section'])
            {'publish': pub, 'hold': hold}.get(it.get('state'), never).append(rec)
    for it in cfg.get('never_publish', []) or []:
        never.append(dict(it, state='never', section='(named hard block)'))
    return pub, hold, never


def find_unclassified(cfg, pub, hold, never):
    """Markdown files on disk that site.yml does not mention in any state.

    The allow-list denies by default, which is right — but it means a new evidence file is
    silently absent rather than visibly excluded. Silence is the failure mode here, so the
    build names them."""
    named = {p['src'] for p in pub + hold + never}
    trees = [t['path'] for t in cfg.get('exclude_trees', [])] + ['.git/']

    # Enumerate what GIT TRACKS, not what is on disk. A build environment (a venv, a pip
    # cache) can sit inside the working tree and carry hundreds of dependency LICENSE.md
    # files; on a clean clone with the venv inside it this listed 9 of them. Noise in this
    # particular section is worse than no section, because this is the one that must never
    # be skimmed. Falls back to a disk walk only if git is unavailable.
    try:
        listing = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z', '*.md'],
                                 capture_output=True, check=True, text=True).stdout
        candidates = [c for c in listing.split('\0') if c]
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        candidates = [f.relative_to(ROOT).as_posix() for f in ROOT.rglob('*.md')]

    out = []
    for rel in sorted(candidates):
        if rel in named or any(rel.startswith(t) for t in trees):
            continue
        # Bank subdirectories inside a topic folder are excluded wholesale by design.
        parts = rel.split('/')
        if parts[0].startswith('files - ') and len(parts) > 2:
            continue
        out.append(rel)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--serve', action='store_true')
    ap.add_argument('--report', action='store_true')
    ap.add_argument('--port', default='8000')
    args = ap.parse_args()

    cfg = load_cfg()
    pub, hold, never = collect(cfg)

    missing = [p['src'] for p in pub + hold if not (ROOT / p['src']).exists()]
    unclassified = find_unclassified(cfg, pub, hold, never)
    urlmap = {p['src']: p['url'] for p in pub if p.get('url')}
    noindex = bool(cfg['site'].get('noindex', True))

    stats = {'internal': 0, 'unlinked': 0, 'unlinked_targets': {}, 'pages': 0,
             'provisional': 0, 'posture': 0, 'no_version': []}

    if not args.report:
        if BUILD.exists():
            shutil.rmtree(BUILD)
        SRC.mkdir(parents=True)

    nav, staged = [], []
    for sec in cfg.get('pages', []):
        entries = []
        for it in sec.get('items', []):
            if it.get('state') != 'publish':
                continue
            src_rel = Path(it['src'])
            if not (ROOT / src_rel).exists():
                continue
            text = (ROOT / src_rel).read_text(encoding='utf-8')
            facts = read_facts(text)
            banners_on = it.get('banner', True)
            if banners_on and not facts['version']:
                stats['no_version'].append(it['src'])
            if banners_on and facts['provisional']:
                stats['provisional'] += 1
            add_posture = banners_on and bool(CASE_RE.search(text))
            if add_posture:
                stats['posture'] += 1

            body = rewrite_links(text, src_rel, urlmap, stats)
            if banners_on:
                body = inject(body, banner(src_rel.as_posix(), facts,
                                           cfg.get('posture_banner', ''), add_posture))

            url = it['url'].strip('/')
            dest = SRC / (('index.md' if url == 'index' else url + '/index.md'))
            if not args.report:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(body, encoding='utf-8')
            title = it.get('title') or re.sub(r'\.md$', '', src_rel.name)
            entries.append({title: ('index.md' if url == 'index' else url + '/index.md')})
            staged.append((it['src'], url, facts))
            stats['pages'] += 1
        if entries:
            nav.append({sec['section']: entries} if len(entries) > 1 or sec['section'] != 'The library'
                       else {sec['section']: entries})

    # ---- mkdocs config (generated; never hand-edited)
    mk = {
        'site_name': cfg['site']['name'],
        'site_description': cfg['site'].get('description', ''),
        'docs_dir': str(SRC),
        'site_dir': str(OUT),
        'use_directory_urls': True,
        'strict': False,
        'theme': {
            'name': 'material',
            'features': ['navigation.sections', 'navigation.top', 'navigation.indexes',
                         'search.highlight', 'search.suggest', 'content.code.copy', 'toc.follow'],
            'palette': [
                {'media': '(prefers-color-scheme: light)', 'scheme': 'default',
                 'primary': 'blue grey', 'accent': 'indigo',
                 'toggle': {'icon': 'material/brightness-7', 'name': 'Dark mode'}},
                {'media': '(prefers-color-scheme: dark)', 'scheme': 'slate',
                 'primary': 'blue grey', 'accent': 'indigo',
                 'toggle': {'icon': 'material/brightness-4', 'name': 'Light mode'}},
            ],
        },
        'markdown_extensions': [
            'tables', 'footnotes', 'attr_list', 'md_in_html', 'sane_lists',
            {'toc': {'permalink': True, 'toc_depth': 3}},
            {'admonition': {}}, {'pymdownx.details': {}},
            {'pymdownx.superfences': {}},
        ],
        'plugins': ['search'],
        'copyright': ('Library prose CC BY 4.0 · scripts MIT · '
                      'the artifact banks are third-party material and are not licensed here'),
        'extra_css': ['assets/library.css'],
        'nav': nav,
    }
    if cfg['site'].get('url'):
        mk['site_url'] = cfg['site']['url']

    if not args.report:
        (SRC / 'assets').mkdir(parents=True, exist_ok=True)
        (SRC / 'assets' / 'library.css').write_text(CSS, encoding='utf-8')
        if noindex:
            (SRC / 'robots.txt').write_text("User-agent: *\nDisallow: /\n", encoding='utf-8')
        CFG.write_text(yaml.safe_dump(mk, sort_keys=False, allow_unicode=True), encoding='utf-8')

    write_report(cfg, pub, hold, never, missing, stats, staged, noindex, unclassified)

    print(f"staged {stats['pages']} pages · {stats['internal']} internal links rewritten · "
          f"{stats['unlinked']} links to unpublished files neutralised")
    print(f"held: {len(hold)} · hard-blocked: {len(never)} · report: {REPORT.relative_to(ROOT)}")
    if unclassified:
        print(f"⚠ {len(unclassified)} markdown file(s) are in NO state in site.yml — "
              f"silently absent from the site. See the report.")
    if missing:
        print(f"⚠ {len(missing)} allow-list entries name files that do not exist:")
        for m in missing:
            print('   ', m)
    if args.report:
        return 0

    # 🚨 INVOKE MKDOCS THROUGH THE RUNNING INTERPRETER, NOT THROUGH PATH (fixed 2026-09-17).
    # This used to be: the in-tree `.venv-site/bin/mkdocs` if it existed, else bare `'mkdocs'`.
    # Both halves fail where it matters most — on Netlify. `.venv-site/` is gitignored, so it is
    # never in a clean clone; and the fallback needs `mkdocs` on PATH, which is true only if the
    # installing venv happens to be ACTIVATED. Netlify runs
    #     pip install -r ops/site/requirements.txt && python3 scripts/build-site.py
    # with no activation step, so the old code took the fallback and died with
    #     FileNotFoundError: [Errno 2] No such file or directory: 'mkdocs'
    # — which is exactly what a clean-clone pre-flight produced on 2026-09-17, the first time the
    # build was run with the venv genuinely outside the tree AND unactivated. **The deploy would
    # have failed at build time.** `sys.executable -m mkdocs` always resolves to the mkdocs
    # installed for the interpreter actually running this file: venv or system, activated or not.
    cmd = [sys.executable, '-m', 'mkdocs']
    cmd += ['serve', '-f', str(CFG), '-a', f'127.0.0.1:{args.port}'] if args.serve \
        else ['build', '-f', str(CFG)]
    return subprocess.call(cmd)


def write_report(cfg, pub, hold, never, missing, stats, staged, noindex, unclassified):
    L = []
    A = L.append
    A('# Site build report')
    A('')
    A(f"**Generated** {date.today().isoformat()} by `scripts/build-site.py` — **never hand-edited.**")
    A('')
    A('This report exists because an exclusion nobody can see is an exclusion nobody can audit.')
    A('Every markdown file named in `ops/site/site.yml` appears below in exactly one state.')
    A('')
    A(f"- **Published:** {stats['pages']} pages")
    A(f"- **Held** (owner decision pending, Phase 2): {len(hold)}")
    A(f"- **Hard-blocked:** {len(never)}")
    A(f"- Pages whose source carries `[PROVISIONAL]`, banner rendered: **{stats['provisional']}** of {stats['pages']}")
    A(f"- Pages carrying the case-posture banner: **{stats['posture']}**  *(2 pages — home and licence — render no banners by design)*")
    A(f"- Internal links rewritten to site URLs: {stats['internal']}")
    A(f"- Links to unpublished files neutralised (text kept, link removed): {stats['unlinked']}")
    A(f"- Search-engine indexing: **{'BLOCKED (robots.txt Disallow /)' if noindex else 'ALLOWED'}**")
    A('')
    if unclassified:
        A('## 🚨 Unclassified — on disk, in no state, silently absent from the site')
        A('')
        A('The allow-list denies by default, so these are not published — but nothing marked')
        A('them as excluded either. **Any new evidence file lands here until `ops/site/site.yml`')
        A('gives it a state.** Decide each one; do not let this list become normal.')
        A('')
        for m in unclassified:
            A(f'- `{m}`')
        A('')
    if missing:
        A('## ⚠ Allow-list entries with no file on disk')
        A('')
        for m in missing:
            A(f'- `{m}`')
        A('')
    if stats['no_version']:
        A('## ⚠ Published pages whose source states no version')
        A('')
        A('The banner on these pages says so rather than guessing one.')
        A('')
        for m in stats['no_version']:
            A(f'- `{m}`')
        A('')
    A('## Published')
    A('')
    A('| Source (frozen citation path) | URL | Version | Status |')
    A('|---|---|---|---|')
    for src, url, f in staged:
        st = '`[PROVISIONAL]`' if f['provisional'] else ('`[VERIFIED]` token' if f['verified_token'] else '—')
        A(f"| `{src}` | `/{url if url != 'index' else ''}` | {f['version'] or '—'} | {st} |")
    A('')
    A('## Held — not published, owner decision pending')
    A('')
    A('| Source | Why it is held |')
    A('|---|---|')
    for h in sorted(hold, key=lambda x: x['src']):
        A(f"| `{h['src']}` | {h.get('reason','—')} |")
    A('')
    A('## Hard-blocked')
    A('')
    A('| Source | Why |')
    A('|---|---|')
    for n in sorted(never, key=lambda x: x['src']):
        A(f"| `{n['src']}` | {n.get('reason','—')} |")
    A('')
    A('## Excluded wholesale, by tree')
    A('')
    A('| Path | Reason |')
    A('|---|---|')
    for t in cfg.get('exclude_trees', []):
        A(f"| `{t['path']}` | {t['reason']} |")
    A('')
    A('Every artifact bank (any subdirectory inside a `files - <Topic>/` folder) is excluded')
    A('wholesale. 103 banked raw news-article bodies live in those; archiving a copy in a')
    A('repository and republishing it on a public website are different postures.')
    A('')
    if stats['unlinked_targets']:
        A('## Most-referenced unpublished files')
        A('')
        A('These are cited by published pages. Each is a candidate for the Phase 2 scope ruling —')
        A('a file cited often by published work is the one whose absence readers will notice.')
        A('')
        A('| Target | Times cited from published pages |')
        A('|---|---|')
        for t, c in sorted(stats['unlinked_targets'].items(), key=lambda kv: -kv[1])[:25]:
            A(f'| `{t}` | {c} |')
        A('')
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text('\n'.join(L) + '\n', encoding='utf-8')


CSS = """/* Kirk Robinson Research — reading styles over mkdocs-material */
.md-grid { max-width: 68rem; }
.md-typeset { font-size: .78rem; line-height: 1.7; }
.md-typeset table:not([class]) { font-size: .68rem; display: table; width: 100%; }
.md-typeset table:not([class]) td,
.md-typeset table:not([class]) th { padding: .5em .7em; vertical-align: top; }
.md-typeset h1, .md-typeset h2 { font-weight: 700; letter-spacing: -.01em; }
.md-typeset .unpublished {
  font-size: .72em; opacity: .62; white-space: nowrap;
  border-bottom: 1px dotted currentColor; cursor: help;
}
.md-typeset blockquote { border-left: .2rem solid var(--md-default-fg-color--lighter); }
"""

if __name__ == '__main__':
    sys.exit(main())
