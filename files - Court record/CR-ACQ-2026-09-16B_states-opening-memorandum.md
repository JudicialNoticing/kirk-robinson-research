# CR-ACQ-2026-09-16B — Acquisition: the State's opening *Memorandum in Support of Preliminary Hearing Bindover* (filed 2026-07-28), from the Scribd mirror

**File ID:** CR-ACQ-2026-09-16B · **Scope:** the banking of the one bindover-cycle document the library held nowhere for 50 days (Q-45, Q-56), as Scribd renders the copy uploaded by *The Post Millennial*; facial provenance verification; nothing else. · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-09-16 · **Status/version:** v1.0 — an inventory with hashes and one verification act (§3). **The document's contents are deliberately NOT characterised here** beyond title, date, signatories and page count; the reasoned read is a separate act (→ Q-187), as `CR-ACQ-2026-08-20` did for the State's reply.

> ⚖️ **Presumption of innocence.** This is a party's brief. Every proposition in it is the State's claim, made under the probable-cause standard, and is adopted nowhere in this library by the act of banking it. Mr. Robinson is reported bound over and has pleaded not guilty.

---

## §0 · Sourcing framework (project standard)

Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting/analysis · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim carries a locator; every retrieval a date.

## §1 · Access-path caveats — read before using any line

- **What was retrievable, and what was not.** Scribd document `1067587104` (*"Memorandum in Support of Preliminary Hearing Bindover in Tyler Robinson case"*, uploader shown as **The Post Millennial**, 28 pages) has been challenge-gated to this library's fetches since 2026-08-13 (`CR-WATCH-log` v1.3; seven endpoints). **On 2026-09-16 ~16:40 EDT the document page answered HTTP 200 with its full HTML5 reader**, and the page renderings Scribd serves to any reader of a free document were fetched: pages 1–3 inline in the page, pages 4–28 as per-page `.jsonp` files under asset key `5jsfxjgxkwi2pub0`, each gzip-compressed. **The PDF itself was NOT retrieved** — Scribd's download requires an account and none was created. So what is banked is **Scribd's text-layer rendering of the uploaded PDF, not the PDF**, plus the five small page graphics the rendering references (caption rules, not page scans). ⚠ **No page images exist for this artifact; "render, don't grep" cannot be applied to it.** The text layer is the only form held.
- 🚨 **Text-layer hazard: small-caps names are split.** Scribd renders small capitals as two runs, so page 1's signature caption and page 28's block read, e.g., *"J S. G (5852) | EFFREY RAY"* for **JEFFREY S. GRAY**. **A search for a counsel's name in the caption or signature block returns a false null; search the body text instead, or read the page.** Body text (pages 2–27) extracts cleanly with line order recovered from the spans' positions.
- **Provenance of the copy: two-of-three, the same grade as the other two briefs.** Signature block ✅ (*"Dated July 28, 2026 … Utah County Attorney /s/ Jeffrey S. Gray"*, p. 28); certificate of service ✅ (*"I certify that on July 28, 2026, I filed the foregoing MEMORANDUM IN SUPPORT OF PRELIMINARY HEARING BINDOVER through the Court's electronic filing system … /s/ Christopher D. Ballard"*, p. 28); **clerk file-stamp ❌ not present in the text layer** — and since no page images are held, whether the uploaded PDF carries one is **not established**. It is an outlet-mirrored copy carrying the State's own attestation. A court-stamped copy is still sought (Q-63; XChange, $1).
- **28 pages is the LENGTH; 35 pages was the LIMIT** set on Day 4 (`CR-ACQ` §5.1). The uploaded copy's 28 matches the length six outlets reported on 07-28/29 (`CR-WATCH-log` Run 2). Do not conflate.
- **Retrieval record (2026-09-16 EDT):** Wayback CDX 503 and the availability API 429 (both retried; the three 2026-08-20 captures recorded on 08-29 remain unreachable); archive.today 404; DocumentCloud search API 403 (third block of the day); outlet articles of 07-28/29 (Deseret, KSL, KUTV) carry no document link. **Scribd was the only route that opened, and it opened without any change on this side** — the same URL, the same user-agent, a different day. Consistent with the route's recorded intermittency; not evidence that the gate is gone.
- **Tools:** `urllib` with a browser user-agent and the document page as referer; `gzip`; text order recovered by sorting spans on their CSS `top`/`left`. SHA-256 on every fetched byte-stream at banking time.

## §2 · What was banked

All in `CR-ACQ-2026-07-27_court-record-artifacts/2026-07-28_states-memorandum-prelim-bindover_scribd-1067587104/` (62 files; per-file SHA-256 in its `SHA256SUMS.txt`):

| Item | Files | Note |
|---|---|---|
| Scribd document page as served | `scribd-document-page_2026-09-16.html` (1,209,617 B) · `scribd-embed-content_2026-09-16.html` | the page that carries pages 1–3 inline and the asset key; `sha256 570dc3837da53c75…` |
| Page renderings, raw | `page-04…28-<hash>.jsonp` (25 files, gzip as served) | Scribd's own per-page HTML5 payloads |
| Page renderings, decompressed | `page-01…03-inline.html` · `page-04…28-<hash>.html` | the HTML fragment for every page, 1–28 |
| Page graphics | `image-01, 06, 07, 14, 28-<hash>.jpg` | the only five images the rendering references; caption rules and the signature-block graphic, **not page scans** |
| Extracted text | `extracted-text.txt` — and, at the bank root for sweeps, `2026-07-28_states-memorandum-prelim-bindover_scribd-1067587104.txt` | 28 pages, 50,809 chars, 8,792 words; `sha256 bfa9de9e31232a2882c7956e0f5be2f8d585630daa769de7f796185c2b61fcec` |

**Face of the document (recorded from pages 1 and 28; no characterisation of the argument):** caption *"Memorandum in Support of Preliminary Hearing Bindover"*, Case No. 251403576, Judge Tony F. Graf, Jr.; the Utah County Attorney's Office (Jeffrey S. Gray; deputies Grunander, McBride, Hunt, Sturgill, Ballard); dated and served **2026-07-28**; **28 pages**; signed */s/ Jeffrey S. Gray*; certificate of service */s/ Christopher D. Ballard*.

## §3 · What this acquisition does and does not establish

- ✅ **Q-45's document is HELD, in the only form the route offered** — 50 days after the filing was first reported (Run 1, 2026-07-28), 46 days after the Scribd mirror was located (Run 2), 34 days after the first retrieval attempt failed at the challenge (2026-08-13).
- ✅ **The filing date is now on the document's own face** (dated and certificate of service both 2026-07-28), where until today it was T1 via T3 across six outlets. The State's 07-28 deadline (`CR-ACQ` §5.1) was met on the document's own showing.
- ⚠ **Not established:** that the uploaded PDF is the as-filed document (no file-stamp; outlet upload); that the text layer is complete and faithful to the PDF at every line (spans were re-ordered by position; small-caps runs are split; one page — p. 3 — shows the same 63-column line-wrap artefacts as the other briefs, e.g. *"positioned"* rendered *"tioned"* after a wrap). **Quote from this text only after checking the surrounding lines, and never a name from the caption.**
- 🚫 **Nothing here characterises the memorandum's contents.** Its argument, its exhibit citations, its treatment of the medical examiner's report that the defence brief says it quotes (`CR-E07` F-20 → Q-51) and its transcript pin-cites (`CR-E18`'s crosswalk can now be extended to it) are all **the reasoned read's business — Q-187**, gate `verify`, in the pattern of Q-181 for the reply.

## §4 · Open items

- **Q-187 (new):** the reasoned read → a `CR-E` evidence file, under P1 → P2 with the isolation rule; extends `CR-E18`'s crosswalk to the State's `Tr. Day N at page:line` cites; tests `CR-E07` F-20 (the ME-report quotation claim) against the face.
- **Q-63:** a court-stamped copy (XChange, $1, once Q-31 is bought).
- The routine's live prompt still says *"DOCUMENT IS NOT HELD (Q-45)"*; the 09-14 draft has been updated in this session; the live text is 👤.

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-09-16** | Created. Scribd's HTML5 rendering of the State's 07-28 memorandum fetched page by page (28/28), banked with hashes; provenance two-of-three on the face (signature block and certificate of service, no file-stamp visible, no page images held); contents not characterised; Q-45 and Q-56 closed, Q-187 opened. |
