#!/usr/bin/env python3
"""Flattened-context search over the banked preliminary-hearing transcripts.

WHY THIS EXISTS. The banked Rev transcripts are broken into timestamp blocks,
so a fixed-width context window spanning line breaks silently matches nothing.
BOC-AUDIT-2026-07-27B §4 records the near-miss: a naive `grep -o ".\\{300\\}woolsey"`
returned nothing for a carrier that plainly contained the passage, and taking
that null at face value would have supported a false and serious conclusion.

Standing rule (QUEUE.md hazard 5): **a null from a text search is a claim about
the search, not about the corpus, until the method has been validated against a
known positive.** This tool flattens whitespace first, and `--validate` runs the
known-positive check so you can state a null honestly.

Usage
-----
    ./scripts/tsearch.py --validate                       # confirm the method works
    ./scripts/tsearch.py "use pliers" --days 4
    ./scripts/tsearch.py "engraving cutter" -B 800 -A 800
    ./scripts/tsearch.py "Matthew Robinson" --days 5 -n 10

Written 2026-07-28 during the Q-02 independent pass (CR-AUDIT-2026-07-28 §7).
"""
import re
import os
import sys
import argparse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # scripts/ -> library root
BASE = os.path.join(
    REPO,
    "files - Court record",
    "CR-ACQ-2026-07-27_court-record-artifacts",
    "prelim-hearing-transcripts",
)

# A passage known to exist, used to prove the search method works before any
# null is believed. Karner, Day 4, 06:39:54.
KNOWN_POSITIVE = ("use pliers", "4")


def load(day):
    path = os.path.join(BASE, "day%s.txt" % day)
    if not os.path.exists(path):
        sys.exit("no such transcript: %s" % path)
    with open(path, errors="replace") as fh:
        return re.sub(r"\s+", " ", fh.read())


def search(pattern, days, before, after, limit, quiet=False):
    rx = re.compile(pattern, re.I)
    total = 0
    for day in days:
        text = load(day)
        hits = list(rx.finditer(text))
        total += len(hits)
        if quiet:
            continue
        print("\n===== day%s.txt : %d hit(s) for /%s/ =====" % (day, len(hits), pattern))
        for i, m in enumerate(hits[:limit]):
            start = max(0, m.start() - before)
            end = min(len(text), m.end() + after)
            print("\n--- hit %d @ char %d ---" % (i + 1, m.start()))
            print(text[start:end])
        if len(hits) > limit:
            print("\n[%d further hits suppressed — raise -n to see them]" % (len(hits) - limit))
    if not quiet:
        print("\nTOTAL: %d" % total)
    return total


def validate():
    pattern, day = KNOWN_POSITIVE
    found = search(pattern, [day], 0, 0, 0, quiet=True)
    if found:
        print("✓ method validated — known positive /%s/ found in day%s.txt" % (pattern, day))
        return 0
    print("✗ METHOD FAILED — known positive /%s/ NOT found in day%s.txt." % (pattern, day))
    print("  Do not trust any null from this tool until this passes.")
    print("  Check that the transcripts are still at: %s" % BASE)
    return 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern", nargs="?", help="regex, case-insensitive")
    ap.add_argument("--days", default="1,2,3,4,5", help="comma-separated, default all five")
    ap.add_argument("-B", "--before", type=int, default=400, help="chars of leading context")
    ap.add_argument("-A", "--after", type=int, default=600, help="chars of trailing context")
    ap.add_argument("-n", "--limit", type=int, default=6, help="max hits shown per day")
    ap.add_argument("--validate", action="store_true", help="run the known-positive check and exit")
    args = ap.parse_args()

    if args.validate:
        sys.exit(validate())
    if not args.pattern:
        ap.error("give a pattern, or --validate")
    if validate() != 0:
        sys.exit(1)
    search(args.pattern, [d.strip() for d in args.days.split(",")],
           args.before, args.after, args.limit)
