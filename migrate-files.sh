#!/usr/bin/env bash
#
# migrate-files.sh — copy a research folder to a new location, then verify.
#
# Non-destructive: the source directory is left completely untouched.
# Names and structure are preserved exactly. Only ".DS_Store" (macOS Finder
# metadata) and this script itself are excluded from the copy.
#
# Usage: ./migrate-files.sh <source-dir> <destination-dir>

set -euo pipefail

SRC="${1:-}"
DST="${2:-}"
SELF="$(basename "$0")"

if [[ -z "$SRC" || -z "$DST" ]]; then
  echo "Usage: $0 <source-dir> <destination-dir>" >&2
  exit 2
fi
if [[ ! -d "$SRC" ]]; then
  echo "Error: source directory does not exist: $SRC" >&2
  exit 1
fi

mkdir -p "$DST"

echo "Copying (source will NOT be modified):"
echo "  from: $SRC"
echo "    to: $DST"
echo

# -a preserves structure, names, timestamps, permissions. Trailing slash on
# SRC copies the *contents* of SRC into DST (not SRC itself as a subfolder).
rsync -a \
  --exclude='.DS_Store' \
  --exclude="$SELF" \
  "$SRC"/ "$DST"/

echo "Verifying..."

src_list="$(cd "$SRC" && find . -type f ! -name '.DS_Store' ! -name "$SELF" | sort)"
dst_list="$(cd "$DST" && find . -type f ! -name '.DS_Store' ! -name "$SELF" | sort)"

src_bytes="$(cd "$SRC" && find . -type f ! -name '.DS_Store' ! -name "$SELF" -exec stat -f '%z' {} + 2>/dev/null | awk '{s+=$1} END{print s+0}')"
dst_bytes="$(cd "$DST" && find . -type f ! -name '.DS_Store' ! -name "$SELF" -exec stat -f '%z' {} + 2>/dev/null | awk '{s+=$1} END{print s+0}')"

dst_count="$(printf '%s\n' "$dst_list" | grep -c . || true)"

if [[ "$src_list" == "$dst_list" && "$src_bytes" == "$dst_bytes" ]]; then
  echo "OK: $dst_count files copied; file lists and total bytes ($dst_bytes) match."
  echo "Source left intact at: $SRC"
else
  echo "WARNING: verification mismatch — inspect before trusting the copy." >&2
  if [[ "$src_list" != "$dst_list" ]]; then
    echo "  files only in source:" >&2
    comm -23 <(printf '%s\n' "$src_list") <(printf '%s\n' "$dst_list") >&2 || true
    echo "  files only in destination:" >&2
    comm -13 <(printf '%s\n' "$src_list") <(printf '%s\n' "$dst_list") >&2 || true
  fi
  if [[ "$src_bytes" != "$dst_bytes" ]]; then
    echo "  byte total: source=$src_bytes destination=$dst_bytes" >&2
  fi
  exit 1
fi
