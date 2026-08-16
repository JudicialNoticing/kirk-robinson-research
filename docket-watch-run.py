#!/usr/bin/env python3
"""docket-watch-run.py — the DOCKET-WATCH.md spec, executable.

Written 2026-08-16 for the Tue 2026-08-18 State's-reply window, which has NO
document-capable scheduled cover: the cloud routine next fires Wed 08-19 (AFTER
the deadline) and is egress-blind. A LOCAL by-hand run is the only cover.

This turns that run from a from-scratch search into a DIFF against a stored
baseline, per DOCKET-WATCH.md's access-routes table.

    ./docket-watch-run.py                 # run all checks, diff vs baseline
    ./docket-watch-run.py --baseline      # (re)write the baseline, then diff
    ./docket-watch-run.py --only rev      # one check: dc | fox | rev | utcourts

DESIGN RULE, and it is the whole point of the file
--------------------------------------------------
A route that CANNOT BE ATTEMPTED is not a route that found nothing.
Every check returns one of: OK (with findings) / EMPTY (attempted, nothing
found) / **BLOCKED** (could not attempt). BLOCKED is never reported as a null.
This exists because the DocumentCloud route 403'd at 09:00 on 2026-08-16 and was
fully open at 14:05, unchanged — see CR-ACQ-2026-08-16 §1.

It writes NOTHING into the library. It prints a report for a human to read and
paste into CR-WATCH-log.md, per DOCKET-WATCH.md "Output". It resolves nothing,
characterises no filing's contents, and touches no case-posture statement —
those are human gates in every mode (LOOP.md §3).
"""
import argparse, json, os, re, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, "files - Court record",
                        "CR-ACQ-2026-07-27_court-record-artifacts",
                        "docket-watch-baseline.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

OK, EMPTY, BLOCKED = "OK", "EMPTY", "BLOCKED"


def get(url, timeout=45, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")


# ---------------------------------------------------------------- checks

def check_documentcloud():
    """Case-number search. Baseline is the set of DC ids already known."""
    q = urllib.parse.quote('"251403576"')
    url = f"https://api.www.documentcloud.org/api/documents/search/?q={q}&per_page=25"
    ids, pages = {}, 0
    try:
        while url and pages < 10:
            d = json.loads(get(url, 60))
            for x in d["results"]:
                ids[str(x["id"])] = {"title": x["title"], "pages": x["page_count"],
                                     "file_hash": x["file_hash"], "org": x["organization"]}
            url, pages = d.get("next"), pages + 1
    except Exception as e:
        return {"status": BLOCKED, "detail": f"{type(e).__name__}: {e}",
                "note": "DocumentCloud has 403'd behind Cloudflare before and recovered "
                        "the same day. DO NOT log this as 'no new filings'."}
    return {"status": OK, "ids": ids, "count": len(ids)}


def check_fox_mirror():
    """The outlet mirror that carried the defence brief. Enumerate via Wayback CDX.

    Match on the CASE, not the surname: 'bijan-robinson-*.jpg' also matches.
    """
    prefix = "static.foxnews.com/foxnews.com/content/uploads/2026/08/"
    url = ("http://web.archive.org/cdx/search/cdx?url="
           + urllib.parse.quote(prefix + "*")
           + "&output=json&fl=original&collapse=urlkey&limit=4000")
    try:
        rows = json.loads(get(url, 90))
    except Exception as e:
        return {"status": BLOCKED, "detail": f"{type(e).__name__}: {e}",
                "note": "Wayback CDX unavailable; the mirror itself has no index page, "
                        "so this route is UNATTEMPTABLE, not empty."}
    files = sorted({r[0] for r in rows[1:]}) if len(rows) > 1 else []
    pdfs = [f for f in files if f.lower().endswith(".pdf")]
    # Case items: deliberately OVER-inclusive. A noisy flag is the safe failure
    # direction here (same reasoning as queue-check.sh's validator) — a missed
    # filing cannot be caught up later; a false flag costs one click.
    # Known false positive already in the baseline, so the diff won't re-raise it:
    # 'Matthews_-_Memo_of_Law_in_Support_of_Motion_for_a_Preliminary_Injunction.pdf'
    # matches on 'Prelim'. Match on the CASE, not the surname: 'bijan-robinson-*'
    # is an unrelated athlete (DOCKET-WATCH.md access-routes table).
    case = [f for f in pdfs
            if re.search(r"robinson|kirk|prelim|filing|brief|reply", f, re.I)
            and not re.search(r"bijan", f, re.I)]
    return {"status": OK if pdfs else EMPTY, "pdf_count": len(pdfs),
            "pdfs": pdfs, "case_items": case}


def check_rev():
    """Rev transcripts. Enumerate from the sitemap - never guess slugs (hazard 5).

    Two known slug traps: day 1 sits at 'ut-v-tyler-robinson---day-1', not the
    '...-preliminary-hearing-day-N' pattern the other four use.
    """
    import gzip, io
    try:
        raw = get("https://www.rev.com/sitemap.xml", 60, binary=True)
        if raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        text = raw.decode("utf-8", "replace")
    except Exception as e:
        return {"status": BLOCKED, "detail": f"{type(e).__name__}: {e}",
                "note": "'/transcripts/search?q=' is a 404 and is NOT a search endpoint. "
                        "Without the sitemap this route is UNATTEMPTABLE, not empty."}
    locs = re.findall(r"<loc>([^<]+)</loc>", text)
    subs = [u for u in locs if u.endswith(".xml") or u.endswith(".xml.gz")]
    hits = sorted({u for u in locs if re.search(r"robinson", u, re.I)})
    scanned = ["https://www.rev.com/sitemap.xml"]
    for s in subs[:60]:
        try:
            raw = get(s, 60, binary=True)
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            t = raw.decode("utf-8", "replace")
            scanned.append(s)
            hits.extend(u for u in re.findall(r"<loc>([^<]+)</loc>", t)
                        if re.search(r"robinson", u, re.I))
        except Exception:
            continue
    hits = sorted(set(hits))
    return {"status": OK if hits else EMPTY, "hits": hits,
            "sitemaps_scanned": len(scanned)}


def check_utcourts():
    url = "https://legacy.utcourts.gov/utc/news/"
    try:
        html = get(url, 45)
    except Exception as e:
        return {"status": BLOCKED, "detail": f"{type(e).__name__}: {e}"}
    items = re.findall(r"<a[^>]+href=\"([^\"]+)\"[^>]*>(.{0,160}?)</a>", html, re.S)
    hits = [(h, re.sub(r"\s+", " ", re.sub("<[^>]+>", "", t)).strip())
            for h, t in items if re.search(r"robinson|kirk", t, re.I)]
    return {"status": OK if hits else EMPTY, "hits": hits}


CHECKS = {"dc": ("DocumentCloud case-number search", check_documentcloud),
          "fox": ("Fox outlet mirror (Wayback CDX)", check_fox_mirror),
          "rev": ("Rev transcripts (sitemap)", check_rev),
          "utcourts": ("Utah Courts press notices", check_utcourts)}


# ---------------------------------------------------------------- report

def diff_report(name, cur, base):
    """Return (lines, changed?) comparing a check result to its baseline."""
    out, changed = [], False
    if cur["status"] == BLOCKED:
        out.append(f"  🚨 **BLOCKED — route unattemptable.** {cur.get('detail','')}")
        if cur.get("note"):
            out.append(f"     ⚠️  {cur['note']}")
        out.append("     ⚠️  DO NOT record this as 'nothing found'.")
        return out, False
    if not base:
        out.append("  (no baseline stored — this run establishes one)")
        return out, False

    if name == "dc":
        new = set(cur["ids"]) - set(base.get("ids", {}))
        out.append(f"  {cur['count']} documents match (baseline {len(base.get('ids',{}))})")
        if new:
            changed = True
            out.append(f"  🚨 **{len(new)} NEW DOCUMENT(S):**")
            for i in sorted(new):
                m = cur["ids"][i]
                out.append(f"     • dc{i}  {m['pages']}pp  org{m['org']}  {m['title'][:80]}")
            out.append("     ⚠️  A search hit is not a case document — OPEN IT before")
            out.append("         recording relevance (CR-ACQ-2026-08-16 §3 correction).")
        else:
            out.append("  no new documents")
    elif name == "fox":
        new = set(cur["pdfs"]) - set(base.get("pdfs", []))
        out.append(f"  {cur['pdf_count']} PDFs (baseline {len(base.get('pdfs',[]))}); "
                   f"{len(cur['case_items'])} look case-related")
        if new:
            changed = True
            out.append(f"  🚨 **{len(new)} NEW PDF(S):**")
            for u in sorted(new):
                flag = " ← CASE?" if u in cur["case_items"] else ""
                out.append(f"     • {u}{flag}")
        else:
            out.append("  no new PDFs")
    elif name == "rev":
        new = set(cur["hits"]) - set(base.get("hits", []))
        out.append(f"  {len(cur['hits'])} robinson URLs (baseline {len(base.get('hits',[]))}), "
                   f"{cur['sitemaps_scanned']} sitemaps scanned")
        if new:
            changed = True
            out.append(f"  🚨 **{len(new)} NEW:**")
            for u in sorted(new):
                out.append(f"     • {u}")
        else:
            out.append("  no new transcripts")
    elif name == "utcourts":
        new = set(h for h, _ in cur["hits"]) - set(h for h, _ in base.get("hits", []))
        out.append(f"  {len(cur['hits'])} matching notices (baseline {len(base.get('hits',[]))})")
        if new:
            changed = True
            for h, t in cur["hits"]:
                if h in new:
                    out.append(f"     • {t[:100]} — {h}")
    return out, changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", action="store_true", help="(re)write the baseline")
    ap.add_argument("--only", choices=list(CHECKS))
    a = ap.parse_args()

    base = {}
    if os.path.exists(BASELINE):
        base = json.load(open(BASELINE))

    names = [a.only] if a.only else list(CHECKS)
    results, anychange, blocked = {}, False, []

    print("=" * 72)
    print("DOCKET WATCH — local run.  State v. Robinson, No. 251403576 (4th Dist., FS)")
    print("Spec: DOCKET-WATCH.md.  Next hard date: Tue 2026-08-18, State's reply (18pp limit).")
    print("=" * 72)

    for n in names:
        label, fn = CHECKS[n]
        print(f"\n### {label}")
        r = fn()
        results[n] = r
        lines, ch = diff_report(n, r, base.get("checks", {}).get(n))
        anychange = anychange or ch
        if r["status"] == BLOCKED:
            blocked.append(label)
        print("\n".join(lines))

    print("\n" + "=" * 72)
    if blocked:
        print(f"🚨 {len(blocked)} ROUTE(S) BLOCKED: {', '.join(blocked)}")
        print("   Record these as ACCESS-PATH CAVEATS, not as nulls.")
    print("CHANGES DETECTED" if anychange else
          "No changes against baseline on the routes that were attemptable.")
    print("⚠️  A run that finds nothing STILL WRITES A ROW in CR-WATCH-log.md.")
    print("⚠️  May not: change case posture, resolve a register entry, or characterise")
    print("    a filing's contents beyond title and date. Those are human gates.")
    print("=" * 72)

    if a.baseline or not base:
        os.makedirs(os.path.dirname(BASELINE), exist_ok=True)
        prev = base.get("checks", {})
        prev.update({k: v for k, v in results.items() if v["status"] != BLOCKED})
        json.dump({"written": "run --baseline to refresh", "checks": prev},
                  open(BASELINE, "w"), indent=2)
        print(f"\nbaseline written → {os.path.relpath(BASELINE, HERE)}")
        if any(v["status"] == BLOCKED for v in results.values()):
            print("⚠️  Blocked routes were NOT baselined (a block is not a state).")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
