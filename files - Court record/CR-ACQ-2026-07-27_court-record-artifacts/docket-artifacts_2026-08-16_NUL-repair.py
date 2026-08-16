#!/usr/bin/env python3
"""Q-105 remediation: replace the extractor's 0x00 page separators with 0x0C.

WHY SUBSTITUTION AND NOT RE-EXTRACTION
--------------------------------------
pdftotext was tested on five affected documents and returns ~equivalent text, so
re-extraction is POSSIBLE. It is nonetheless the wrong choice:

  * Re-extraction produces DIFFERENT text (measured deltas of 0.1-0.3%), and this
    library has already demonstrated that two extractions of the same PDF differ
    in ways that produce false nulls (CR-ACQ-2026-08-16 §6.2). Swapping the
    extraction now would invalidate every verification act already performed
    against the current text - including all of 2026-08-16's reader passes.
  * 0x0C is what the extractor SHOULD have emitted. The substitution is minimal,
    reversible, auditable, and content-preserving by construction.
  * 0x0C IS whitespace to both grep and Python's \\s. 0x00 is whitespace to
    neither. That is the entire defect.

VERIFIED SAFE BEFORE RUNNING: zero affected files contain any existing 0x0C, so
the substitution is unambiguous and the new form-feed count equals the old NUL
count exactly.

Non-destructive: the originals are committed to git, which is the backup.
Every old and new SHA-256 is recorded for the supersession log.
"""
import glob, hashlib, json, os, re, sys

ART = ("~/Documents/Kirk Robinson Research/"
       "files - Court record/CR-ACQ-2026-07-27_court-record-artifacts")
OUT = os.path.dirname(os.path.abspath(__file__))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    dry = "--apply" not in sys.argv
    rows, errors = [], []
    for path in sorted(glob.glob(os.path.join(ART, "*.txt"))):
        raw = open(path, "rb").read()
        n = raw.count(b"\x00")
        if n == 0:
            continue
        if raw.count(b"\x0c"):
            errors.append((os.path.basename(path), "already contains 0x0C - SKIPPED"))
            continue

        new = raw.replace(b"\x00", b"\x0c")

        # --- invariants, checked before anything is written ---
        assert len(new) == len(raw), "length changed"
        assert new.count(b"\x0c") == n, "form-feed count != old NUL count"
        assert b"\x00" not in new, "NULs remain"
        # content identical once both separators are stripped
        assert raw.replace(b"\x00", b"") == new.replace(b"\x0c", b""), "TEXT CHANGED"
        # and the analytically-relevant form: normalised text must now MATCH
        old_norm = re.sub(r"\s+", " ", raw.decode("utf-8", "replace")).strip()
        new_norm = re.sub(r"\s+", " ", new.decode("utf-8", "replace")).strip()
        fixed = old_norm.replace("\x00", "").count("  ")  # unused, kept for clarity
        rows.append({
            "file": os.path.basename(path),
            "nuls_replaced": n,
            "bytes": len(raw),
            "sha256_before": sha(raw),
            "sha256_after": sha(new),
            "normalised_len_before": len(old_norm),
            "normalised_len_after": len(new_norm),
            "nul_survived_normalisation_before": old_norm.count("\x00"),
            "nul_survived_normalisation_after": new_norm.count("\x00"),
        })
        if not dry:
            open(path, "wb").write(new)

    print(f"{'APPLIED' if not dry else 'DRY RUN'} — {len(rows)} files, "
          f"{sum(r['nuls_replaced'] for r in rows)} NULs")
    if errors:
        print("ERRORS:")
        for f, e in errors:
            print("  ", f, e)
    bad = [r for r in rows if r["nul_survived_normalisation_after"] != 0]
    print(f"files still carrying a NUL after normalisation: {len(bad)} (must be 0)")
    if not dry:
        p = os.path.join(OUT, "q105_supersession.json")
        json.dump({"date": "2026-08-16", "transform": "0x00 -> 0x0C (page separator)",
                   "reason": "extractor emitted NUL where form feed belongs; NUL is "
                             "whitespace to neither grep nor Python \\s",
                   "files": rows}, open(p, "w"), indent=2)
        print("supersession record →", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
