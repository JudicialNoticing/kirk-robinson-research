#!/usr/bin/env python3
"""artifact_search.py — the ONE safe way to search the banked court artifacts.

Written 2026-08-16 after two extraction defects in the same family each produced
false nulls in files this library had already searched.

    import sys; sys.path.insert(0, 'scripts')          # the module lives in scripts/ (since 2026-09-15)
    from artifact_search import load, norm, find
    hits = find(r'77-11c-401', 'files - Court record/CR-ACQ-.../dkt117.txt')

WHY THIS FILE EXISTS
--------------------
Two defects, and they need OPPOSITE remedies. That is the whole point.

1. NUL page separators (0x00 where 0x0C belonged) — 1,189 of them across 50 files.
   `grep` skipped those files silently (ugrep -I, no output, exit 0), and because
   \\x00 is NOT whitespace to \\s, `re.sub(r'\\s+',' ')` left them in place, so
   phrases spanning a page break returned false nulls in Python too.
   ==> REPAIRED IN THE DATA on 2026-08-16 (0x00 -> 0x0C), because 0x0C is
       unambiguously the character that belonged there. Content-preserving by
       construction, verified against git HEAD on 50/50 files.

2. U+FFFE line-break hyphenation — 131 occurrences across 15 files, splitting 83
   distinct words, 43 of which exist ONLY in split form. Affected terms include
   `11c401` (the statute CR-E13 quotes), `W000401` (the ATF case number CR-E14
   records as an acquisition identifier), `PreTrial`, and `probabilistic-genotyping`.
   ==> DELIBERATELY *NOT* REPAIRED IN THE DATA. The correct expansion is
       AMBIGUOUS BY CONSTRUCTION and differs per word:
           'addi\\ufffetional'  -> "additional"      (join, no hyphen)
           'death\\ufffepenalty' -> "death-penalty"   (real hyphen)
           '2025-W\\ufffe000401' -> "2025-W-000401"   (real hyphen)
       There is no single substitution that is correct for all of them, so
       mutating the bytes would CORRUPT the record rather than repair it.
       The remedy is therefore a SEARCH-METHOD fix: match BOTH readings.

The general rule this encodes: repair the data only where the correct value is
unambiguous; otherwise repair the method and leave the evidence alone.
"""
import re

# U+FFFE (noncharacter, used here as a soft hyphen), U+019F (mis-mapped "ti"
# ligature: "DeclaraƟon"), and the real soft hyphen.
SPLIT = "￾"
LIGATURES = {"Ɵ": "ti"}


def load(path):
    """Read a banked artifact. Raises if the NUL defect has reappeared."""
    text = open(path, encoding="utf-8", errors="replace").read()
    if "\x00" in text:
        raise ValueError(
            f"{path}: NUL bytes present — the 2026-08-16 repair has been reverted "
            f"or this file was re-banked unrepaired. Do NOT trust any null from it."
        )
    return text


def norm(text, join=True):
    """Whitespace-normalise, expand ligatures, and resolve the U+FFFE split.

    join=True  -> 'death￾penalty' becomes 'deathpenalty'   (hyphenless reading)
    join=False -> 'death￾penalty' becomes 'death-penalty'  (hyphenated reading)

    ⚠️ A null is only real if it holds under BOTH readings. Use find(), which
    checks both for you, rather than calling norm() once and believing it.
    """
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    text = text.replace("­", "" if join else "-")
    text = text.replace(SPLIT, "" if join else "-")
    return re.sub(r"\s+", " ", text).strip()


def find(pattern, path, flags=re.I):
    """Search a banked artifact under BOTH readings of every split word.

    Returns a list of (reading, match, context) tuples. An empty list is a real
    null; a non-empty list must have every hit OPENED AND READ, never counted
    (standing hazards 5 and 12).
    """
    raw = load(path)
    out = []
    for label, joined in (("join", True), ("hyphen", False)):
        t = norm(raw, join=joined)
        for m in re.finditer(pattern, t, flags):
            ctx = t[max(0, m.start() - 90):m.end() + 90]
            out.append((label, m.group(0), ctx))
    return out


def audit(paths):
    """Report the defect census for a set of banked artifacts."""
    rows = []
    for p in paths:
        raw = open(p, encoding="utf-8", errors="replace").read()
        rows.append({
            "path": p,
            "nul": raw.count("\x00"),          # must be 0 post-repair
            "formfeed": raw.count("\x0c"),     # page separators
            "split": raw.count(SPLIT),         # U+FFFE, unrepaired by design
            "ligature": sum(raw.count(k) for k in LIGATURES),
        })
    return rows


if __name__ == "__main__":
    import glob, os, sys
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # scripts/ -> library root
    d = (sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(ROOT, "files - Court record/CR-ACQ-2026-07-27_court-record-artifacts"))
    rows = audit(sorted(glob.glob(os.path.join(d, "*.txt"))))
    nul = sum(r["nul"] for r in rows)
    split = sum(r["split"] for r in rows)
    lig = sum(r["ligature"] for r in rows)
    print(f"{len(rows)} artifacts audited")
    print(f"  NUL bytes      : {nul}   (MUST be 0 — repaired 2026-08-16)")
    print(f"  U+FFFE splits  : {split}   (expected ~131 — NOT repaired, by design)")
    print(f"  ligature defects: {lig}")
    if nul:
        print("\n🚨 NULs present — the repair has been reverted. Nulls are unsafe.")
    for r in rows:
        if r["split"] or r["ligature"]:
            print(f"    {r['split']:>4} split  {r['ligature']:>3} lig  "
                  f"{os.path.basename(r['path'])[:64]}")
