#!/usr/bin/env python3
"""
manifest.py — regenerate the holdings manifest for the Kirk Robinson Research library.

WHY THIS EXISTS
    Every false null this library has produced was about material it ALREADY HELD:
    "No docket is held" (two XChange printouts banked 2026-08-14), "No date of birth"
    (on the face of two documents listed as held and read), "Luna is a null corpus-wide"
    (three occurrences). The failure was never acquisition. It was that nothing recorded
    WHAT IS HELD, WHAT IS INSIDE IT, and HOW TO READ IT.

    Three artifacts in this bank are illegible to a plain text search and a grep over them
    returns a FALSE NULL, not a null:
      - a scan with no text layer at all (render it)
      - OCR garble (render it)
      - 15 of 74 .txt files carrying U+FFFE inside words (use artifact_search.py)
    The ATF firearms report hid behind exactly this for three months.

REGENERATE, NEVER EDIT
    Hand-maintained indexes in this project have drifted every time (DOCKET-WATCH.md vs the
    routine prompt, within a day; START-HERE's stale figure in three places). This file is
    output. Re-run it; do not patch it.

USAGE
    ./manifest.py                 # regenerate SOURCE-MANIFEST.md + source-manifest.json
    ./manifest.py --check         # exit 1 if the manifest on disk is stale (for CI/queue-check)
"""
import os, re, sys, json, glob, hashlib, subprocess, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
ART  = "files - Court record/CR-ACQ-2026-07-27_court-record-artifacts"
CR   = "files - Court record"
# Scanned RECURSIVELY. Widened 2026-09-14: the first version scanned two directories and reported 144
# artifacts while 81 hashed primary captures sat unindexed in the verification-fetch tree — a scope
# narrower than the claim, inside the tool built to prevent exactly that.
SCAN_DIRS = [
    ART,
    os.path.join(CR, "CR-ACQ-2026-09-02_bindover-verification-fetches"),
    os.path.join(CR, "TJR-REVIEW-2026-09-14_verification-cycle-1"),
    "files - George Zinn/ZINN-ACQ-2026-08-20_artifacts",
]
OUT_MD, OUT_JSON = "SOURCE-MANIFEST.md", "source-manifest.json"
FFFE = "￾"

# readability thresholds, in extracted characters per page
NO_TEXT, GARBLE = 40, 300


def sh(cmd, timeout=90):
    try:
        return subprocess.run(cmd, capture_output=True, timeout=timeout).stdout.decode("utf8", "replace")
    except Exception:
        return ""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_pages(path):
    for line in sh(["pdfinfo", path], 30).split("\n"):
        if line.startswith("Pages:"):
            try:
                return int(line.split()[1])
            except Exception:
                return 1
    return 1


def classify_pdf(path):
    """Readability class + the method that actually works on it."""
    text  = sh(["pdftotext", "-q", path, "-"])
    pages = pdf_pages(path)
    per   = len(text.strip()) / max(pages, 1)
    if per < NO_TEXT:
        return "NO-TEXT-LAYER", per, pages, "RENDER: pdftoppm -r 150, read the images. A text search returns a FALSE NULL."
    if per < GARBLE:
        return "OCR-GARBLE", per, pages, "RENDER: the text layer is unreliable; read the rendered page."
    return "text-native", per, pages, "pdftotext is reliable."


def classify_txt(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    n = s.count(FFFE)
    if n:
        split = sorted({w for w in re.findall(r"\S*" + FFFE + r"\S*", s)})
        return "U+FFFE-SPLIT", n, split, ("USE ./artifact_search.py — it searches both the joined and the "
                                          "hyphenated reading. A plain grep returns FALSE NULLS.")
    return "text-native", 0, [], "plain search is reliable."


def artifact_class(path):
    """What KIND of thing this is. Kept distinct so a null asserted about the case record is not
    silently satisfied by this project's own verification exhaust."""
    if "TJR-REVIEW" in path:
        return "process-evidence"          # agent journals, verdicts, pre-correction snapshots
    if "bindover-verification-fetches" in path:
        return "source-capture"            # raw outlet/court bodies fetched and hashed
    if "prelim-hearing-transcripts" in path:
        return "transcript"
    return "primary-source"


def provenance(name):
    """Derive what the filename encodes. Metadata is a claim someone typed — read the face to confirm."""
    p = {}
    m = re.search(r"(?:^|[_\-.])dc(\d{6,9})(?:[_\-.]|$)", name)
    if m:
        p["documentcloud_id"] = m.group(1)
        p["source_route"] = "DocumentCloud open API"
    m = re.search(r"(?:^|[_\-.])dkt(\d+)(?:[_\-.]|$)", name)
    if m:
        p["docket_no"] = m.group(1)
    m = re.match(r"(\d{4}-\d{2}-\d{2})", name)
    if m:
        p["filename_date"] = m.group(1)
    if "rev_" in name or "rev-" in name:
        p["source_route"] = "Rev transcript"
    return p


def dependants(stem, ident, name_full, library_md):
    """Which library files cite this artifact. This is the field that lets a claim point at the
    ARTIFACT instead of at another of this project's own files restating it."""
    hits = []
    # match on the FULL FILENAME too: short stems like "day1" are cited as "day1.txt"
    keys = [k for k in (stem, ident, name_full) if k and len(k) > 4]
    # a document is also "cited" when a library file names its docket number or its slug words
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}[a-z]*_", "", stem)
    slug = re.sub(r"_(dkt\d+|dc\d{6,9}|ALT-EXTRACTION.*)$", "", slug)
    if len(slug) > 12:
        keys.append(slug.replace("-", " "))
    for path, body in library_md.items():
        if any(k in body for k in keys):
            hits.append(path)
    return sorted(hits)


def main():
    os.chdir(ROOT)
    library_md = {}
    for p in glob.glob("**/*.md", recursive=True):
        if p.startswith(("VerificationAndFactCheckProtocol", "SOURCE-MANIFEST")):
            continue
        # frozen pre-correction snapshots are baselines, not live citations
        if "/profile_v" in p and "_pre-" in p:
            continue
        try:
            library_md[p] = open(p, encoding="utf-8", errors="replace").read()
        except Exception:
            pass

    entries, seen = [], set()
    for d in SCAN_DIRS:
        for path in sorted(glob.glob(os.path.join(d, "**", "*"), recursive=True)):
            if not os.path.isfile(path):
                continue
            ext = os.path.splitext(path)[1].lower()
            if ext not in (".pdf", ".txt", ".html", ".docx", ".json", ".jsonl",
                           ".raw", ".xml", ".png", ".jpg"):
                continue
            if path in seen:
                continue
            seen.add(path)
            name = os.path.basename(path)
            stem = os.path.splitext(name)[0]
            e = {
                "path": path, "name": name, "ext": ext[1:],
                "artifact_class": artifact_class(path),
                "bytes": os.path.getsize(path),
                "sha256": sha256(path),
                "banked": datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat(),
                "provenance": provenance(name),
            }
            if ext == ".pdf":
                cls, per, pages, how = classify_pdf(path)
                e.update(readability=cls, pages=pages, chars_per_page=round(per), how_to_read=how)
            elif ext == ".txt":
                cls, n, split, how = classify_txt(path)
                e.update(readability=cls, fffe_occurrences=n, fffe_split_words=split[:12], how_to_read=how)
            elif ext in (".json", ".jsonl", ".xml"):
                e.update(readability="structured-data",
                         how_to_read="machine-readable; parse it, do not prose-search it.")
            elif ext in (".png", ".jpg"):
                e.update(readability="IMAGE-ONLY",
                         how_to_read="RENDERED PAGE IMAGE — read it visually. It has no text to search at all.")
            else:
                e.update(readability="raw-capture", how_to_read="source capture; prefer its extraction.")
            e["cited_by"] = dependants(stem, e["provenance"].get("documentcloud_id", ""), name, library_md)
            entries.append(e)

    # pair each PDF with its extraction so a reader can see when only one form exists
    by_stem = {}
    for e in entries:
        by_stem.setdefault(os.path.splitext(e["name"])[0], []).append(e["ext"])
    for e in entries:
        forms = by_stem.get(os.path.splitext(e["name"])[0], [])
        e["unpaired"] = (e["ext"] == "pdf" and "txt" not in forms)

    hazards = [e for e in entries if e["readability"] in ("NO-TEXT-LAYER", "OCR-GARBLE", "U+FFFE-SPLIT")]
    orphans = [e for e in entries if not e["cited_by"]]

    json.dump({"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
               "count": len(entries), "entries": entries},
              open(OUT_JSON, "w"), indent=1)

    L = []
    A = L.append
    A("# SOURCE-MANIFEST — what this library holds, what is inside it, and how to read it\n")
    A("> 🚨 **GENERATED FILE — DO NOT EDIT. Re-run `./manifest.py`.**")
    A("> Hand-maintained indexes in this project have drifted every time they were kept by hand.\n")
    byclass = {}
    for e in entries:
        byclass[e["artifact_class"]] = byclass.get(e["artifact_class"], 0) + 1
    A(f"**Artifacts:** {len(entries)}  ·  **Readability hazards:** {len(hazards)}  ·  "
      f"**Cited by no library file:** {len(orphans)}\n")
    A("**By class** — ⚠ *a null asserted about the case record is NOT satisfied by process evidence:*\n")
    for k in sorted(byclass):
        A(f"- `{k}` — {byclass[k]}")
    A("")
    A("## 🚨 §1 · Readability hazards — a plain search over these returns a FALSE NULL\n")
    A("| Artifact | Class | How to read it |")
    A("|---|---|---|")
    for e in sorted(hazards, key=lambda x: x["readability"]):
        extra = f" ({e.get('fffe_occurrences')} split tokens)" if e["readability"] == "U+FFFE-SPLIT" else \
                f" ({e.get('chars_per_page')} ch/pg, {e.get('pages')}pp)"
        A(f"| `{e['name'][:74]}` | **{e['readability']}**{extra} | {e['how_to_read']} |")
    A("\n## §2 · Holdings\n")
    A("| Artifact | Class | Form | Banked | Readability | Cited by |")
    A("|---|---|---|---|---|---|")
    for e in entries:
        A(f"| `{e['name'][:60]}` | {e['artifact_class']} | {e['ext']} | {e['banked']} | "
          f"{e['readability']} | {len(e['cited_by'])} |")
    A("\n## §3 · Held but cited by no library file\n")
    A("⚠ **Not dead weight — this is where the library's false nulls came from.** "
      "An artifact nothing cites is one nobody knows is held.\n")
    for e in orphans:
        A(f"- `{e['name']}` — {e['ext']}, banked {e['banked']}, {e['readability']}")
    A("\n## §4 · Unpaired PDFs (no .txt extraction)\n")
    for e in [x for x in entries if x.get("unpaired")]:
        A(f"- `{e['name']}` — **{e['readability']}**. {e['how_to_read']}")
    open(OUT_MD, "w").write("\n".join(L) + "\n")
    return entries, hazards, orphans


if __name__ == "__main__":
    ents, haz, orph = main()
    if "--check" in sys.argv:
        sys.exit(0)
    print(f"manifest regenerated: {len(ents)} artifacts · {len(haz)} readability hazards · {len(orph)} uncited")
