#!/usr/bin/env bash
# queue-check.sh — integrity check for QUEUE.md and the register.
# Run before dispatching a loop cycle and after any cycle that touches the queue.
# Exit 0 = clean, 1 = problems found. Read-only; never modifies anything.

set -uo pipefail
cd "$(dirname "$0")" || exit 1
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
top=$(grep -rhoE 'D-[0-9]+' --include='*.md' . | sed 's/D-//' | sort -n | tail -1)
gaps=$(grep -rhoE 'D-[0-9]+' --include='*.md' . | sed 's/D-//' | sort -n | uniq \
       | awk 'NR>1 && $1!=prev+1 {printf "D-%s->D-%s ", prev, $1} {prev=$1}')
if [ -n "$gaps" ]; then bad "register gaps: $gaps"; else ok "no register gaps (highest string D-$top)"; fi

# forward-looking "next is D-nn" notes inflate the ceiling; report both
declared=$(grep -ohE 'next (number )?is \*{0,2}D-[0-9]+' QUEUE.md 2>/dev/null | grep -oE '[0-9]+' | head -1)
[ -n "${declared:-}" ] && say "  note: QUEUE.md declares next = D-$declared; highest string on disk = D-$top (a forward-looking note legitimately sits one above the ceiling)"

# single assignment site per number: a D-number should be *assigned* in exactly one file
say ""
say "== Assignment sites (informational) =="
for n in $(seq $((top-3)) "$top"); do
  c=$(grep -rl "D-$n" --include='*.md' . 2>/dev/null | wc -l | tr -d ' ')
  say "  D-$n appears in $c file(s)"
done

say ""
say "== Provisional findings outstanding =="
prov=$(grep -rc '\[PROVISIONAL\]' --include='*.md' . 2>/dev/null | grep -v ':0' | grep -vE './(LOOP|QUEUE)\.md' || true)
if [ -n "$prov" ]; then say "$prov" | sed 's/^/  /'; say "  → these may NOT be cited elsewhere until a verification cycle clears them (LOOP.md §2)"; else ok "none outstanding"; fi

say ""
say "== Working tree =="
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then say "  uncommitted changes present"; else ok "clean"; fi

say ""
[ "$fail" = 0 ] && say "RESULT: clean" || say "RESULT: problems found (exit 1)"
exit "$fail"
