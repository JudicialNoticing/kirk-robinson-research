#!/usr/bin/env bash
# queue-check.sh — integrity check for QUEUE.md and the register.
# Run before dispatching a loop cycle and after any cycle that touches the queue.
# Exit 0 = clean, 1 = problems found. Read-only; never modifies anything.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1   # the script lives in scripts/; checks run from the library root
fail=0
say() { printf '%s\n' "$*"; }
bad() { printf '  ✗ %s\n' "$*"; fail=1; }
ok()  { printf '  ✓ %s\n' "$*"; }

say "== QUEUE.md integrity =="
[ -f QUEUE.md ] || { bad "QUEUE.md missing"; exit 1; }

# Q-IDs must be unique.
# ⚠ The ID pattern is BOLD- AND STRIKETHROUGH-TOLERANT (fixed 2026-08-17, Q-131). It used to be
# '^\| Q-[0-9]+ \|', which matches only UNADORNED rows — but almost every row is now written
# '| **Q-NNN** |' or '| ~~Q-NN~~ |', so the ID list was nearly EMPTY and both checks below were
# nearly blind. They only appeared to pass because genuine 'Q-NNN (' references are rare.
# 🚨 The REFERENCE pattern below is deliberately left NOISY. Do not make it cleverer: a smarter
# matcher risks a false NEGATIVE, which would let an unverified finding escape, and START-HERE's
# standing note is that a noisy validator is the safe failure direction.
qids() { grep -oE '^\| *~{0,2}\*{0,2}Q-[0-9]+' QUEUE.md | grep -oE 'Q-[0-9]+'; }

dupes=$(qids | sort | uniq -d)
if [ -n "$dupes" ]; then bad "duplicate Q-IDs: $(echo "$dupes" | tr '\n' ' ')"; else ok "Q-IDs unique ($(qids | sort -u | wc -l | tr -d ' ') distinct)"; fi

# every Blocked-by reference must exist
ids=$(qids | sort -u)
refs=$(grep -oE 'Q-[0-9]+ \(' QUEUE.md | sed 's/ (//' | sort -u)
orphan=0
for r in $refs; do
  echo "$ids" | grep -qx "$r" || { bad "blocked-by references non-existent $r"; orphan=1; }
done
[ "$orphan" = 0 ] && ok "no orphaned blocked-by references"

# actionable items need a decisive artifact
noart=$(awk -F'|' '/\| ready \|/ {gsub(/^ +| +$/,"",$6); if ($6=="" || $6=="—") print $2}' QUEUE.md | tr -d ' ')
if [ -n "$noart" ]; then bad "ready items with no decisive artifact: $(echo "$noart" | tr '\n' ' ')"; else ok "all ready items have a decisive artifact"; fi

say ""
say "== Register integrity =="
# docs/ and archive/ are not library prose (the imported discussion framework uses its own D-01 notation).
# That exclusion now lives in lib_md() below; the old DX=(--exclude-dir=…) array it used to live in
# was removed 2026-09-17 with its last caller, rather than left behind to read as still in force.

# 🚨 THE FILE LIST IS THE GIT INDEX, NOT THE DISK (fixed 2026-09-17).
# Every scan below used to walk `.` recursively. That was correct until 2026-09-17, when
# `scripts/build-site.py` began staging a rendered COPY of the library into `.site-build/`.
# The copies are gitignored but they are still on disk and still full markdown, so a disk walk
# read each published file TWICE: 30 of the 95 lines this check printed were build output, and
# the "assignment sites" counts were inflated by up to four files per D-number. A validator that
# reports phantom files is a validator nobody finishes reading.
# This is the same cure commit c672f06 applied to the site build's own unclassified scan:
# enumerate git-tracked files. A file that is not tracked is not library prose.
# ⚠ The ceiling and the gap set were NOT affected (a copy carries the same numbers) — the damage
# was noise and inflated counts, not a wrong number. Verified both ways before the change.
tracked_md() {
  if git rev-parse --git-dir >/dev/null 2>&1; then
    git ls-files -z '*.md' | tr '\0' '\n'
  else
    # no git (a tarball, an export): fall back to the disk walk, but prune the build outputs
    find . -name '*.md' -not -path './.*' | sed 's|^\./||'
  fi
}
# the same exclusions the disk walk carried, applied to the tracked list
lib_md() { tracked_md | grep -vE '^(docs|archive)/'; }

# ⚠ NORMALISE BEFORE DEDUPING (fixed 2026-09-17). `uniq` compares STRINGS, so the zero-padded
# `D-01` of the imported discussion framework and this library's own `D-1` survived as two
# entries with the same numeric value, and the gap walker then reported a permanent phantom
# `D-01->D-1`. The single occurrence outside docs/ is START-HERE.md line 76 — the sentence that
# DOCUMENTS the collision. The validator was reading its own hazard note as an instance of the
# hazard, and had been failing on it every run. `$1+0` collapses the two; the match itself is
# left as noisy as it was, because a narrower pattern risks the false NEGATIVE (see line 21).
dnums() { lib_md | tr '\n' '\0' | xargs -0 grep -hoE 'D-[0-9]+' 2>/dev/null | sed 's/D-//' | awk '{print $1+0}'; }
top=$(dnums | sort -n | tail -1)
gaps=$(dnums | sort -n | uniq \
       | awk 'NR>1 && $1!=prev+1 {printf "D-%s->D-%s ", prev, $1} {prev=$1}')
if [ -n "$gaps" ]; then bad "register gaps: $gaps"; else ok "no register gaps (highest string D-$top)"; fi

# forward-looking "next is D-nn" notes inflate the ceiling; report both
declared=$(grep -ohE 'next (number )?is \*{0,2}D-[0-9]+' QUEUE.md 2>/dev/null | grep -oE '[0-9]+' | head -1)
[ -n "${declared:-}" ] && say "  note: QUEUE.md declares next = D-$declared; highest string on disk = D-$top (a forward-looking note legitimately sits one above the ceiling)"

# single assignment site per number: a D-number should be *assigned* in exactly one file
say ""
say "== Assignment sites (informational) =="
for n in $(seq $((top-3)) "$top"); do
  c=$(lib_md | tr '\n' '\0' | xargs -0 grep -l "D-$n" 2>/dev/null | wc -l | tr -d ' ')
  say "  D-$n appears in $c file(s)"
done

say ""
say "== Provisional findings outstanding =="
prov=$(lib_md | tr '\n' '\0' | xargs -0 grep -c '\[PROVISIONAL\]' 2>/dev/null | grep -v ':0' \
       | grep -vE '^(LOOP|QUEUE|AUDIT|INDEX)\.md:' || true)
if [ -n "$prov" ]; then say "$prov" | sed 's/^/  /'; say "  → these may NOT be cited elsewhere until a verification cycle clears them (LOOP.md §2)"; else ok "none outstanding"; fi

say ""
say "== Artifacts folder integrity =="
# Added 2026-08-17 (Q-159). A PDF with no .txt sibling is STRUCTURALLY INVISIBLE to every
# "searched all the .txt artifacts" sweep this library runs — the sweep cannot report a gap
# it cannot see. One such file already existed unnoticed. This makes the gap visible.
ART="files - Court record/CR-ACQ-2026-07-27_court-record-artifacts"
if [ -d "$ART" ]; then
  npdf=$(find "$ART" -maxdepth 1 -name '*.pdf' | wc -l | tr -d ' ')
  ntxt=$(find "$ART" -maxdepth 1 -name '*.txt' | wc -l | tr -d ' ')
  nsub=$(find "$ART/prelim-hearing-transcripts" -maxdepth 1 -name '*.txt' 2>/dev/null | wc -l | tr -d ' ')
  unpaired=""
  while IFS= read -r p; do
    [ -f "${p%.pdf}.txt" ] || unpaired="$unpaired $(basename "$p")"
  done < <(find "$ART" -maxdepth 1 -name '*.pdf')
  nun=$(printf '%s' "$unpaired" | wc -w | tr -d ' ')
  say "  $npdf PDF · $ntxt txt (+$nsub in prelim-hearing-transcripts)"
  # 71 = 63 + 9 - 1 contaminant. If this arithmetic changes, every "71 artifacts" null is re-scoped.
  say "  sweepable .txt excluding the BAM Franchising contaminant: $((ntxt + nsub - 1))"
  if [ "$nun" = "1" ] && [ -n "$(printf '%s' "$unpaired" | grep -c 'tyler-robinson-redacted-hearing-transcript')" ]; then
    ok "1 unpaired PDF, and it is the known-cleared one (duplicates oct24_clean.txt; zinn=0)"
  elif [ "$nun" = "0" ]; then
    ok "no unpaired PDFs"
  else
    bad "$nun PDF(s) with no .txt sibling — INVISIBLE to every .txt sweep:$unpaired"
  fi
  # degraded-OCR near-nulls: a .txt this small is not searchable text
  tiny=$(find "$ART" -maxdepth 1 -name '*.txt' -size -1k | while read -r f; do basename "$f"; done | tr '\n' ' ')
  [ -n "$tiny" ] && say "  ⚠ near-null extractions (<1KB, may be degraded OCR): $tiny"
else
  say "  (artifacts folder not found — skipped)"
fi

say ""
say "== Working tree =="
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then say "  uncommitted changes present"; else ok "clean"; fi

say ""
[ "$fail" = 0 ] && say "RESULT: clean" || say "RESULT: problems found (exit 1)"
exit "$fail"
