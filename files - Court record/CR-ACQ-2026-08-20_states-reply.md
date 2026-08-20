# CR-ACQ-2026-08-20 — Acquisition: the State's Reply Memorandum (filed 2026-08-18)

**File ID:** CR-ACQ-2026-08-20 · **Scope:** acquisition, banking and facial (caption/attestation-layer) verification of one court filing; **contents deliberately unread** · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-08-20 · **Status:** v1.0

**Sourcing framework (project standard):** Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim below carries a URL and a retrieval date.

**§1 Access-path caveat, first:** this is an **outlet-hosted mirror** (`static.foxnews.com`), the same dependency class as the banked defence brief — it carries the filer's own attestation, **not** a clerk's. It was located by the Wayback-CDX diff route Run 4 built for exactly this filing (CR-WATCH-log Run 7), and fetched by direct local fetch on **2026-08-20**. ⚠️ The CDX index itself was observed **blocked (Run 6, 2026-08-17, HTTP 504), open (2026-08-20 ~10:57), blocked again (~11:05) and open again (~11:07)** — the route is intermittent at the index layer and a blocked pass is unattemptable, not empty.

---

## 1. Outcome, stated first

**The State's reply is ACQUIRED AND BANKED — the third bindover-cycle brief window is covered by the document itself, not by reporting.** The 2026-08-18 deadline (18-page limit) that had *no document-capable cover on the day* (the scheduled routine fired 08-19, egress-blind; the planned 08-18 local run did not happen — see CR-WATCH-log Run 7 on the miss) is now resolved to a held artifact. **The State's opening brief (Q-45) remains unheld; this acquisition does not touch it.**

## 2. What was acquired

| | |
|---|---|
| **Document** | *"Reply Memorandum in Support of Preliminary Hearing Bindover"* — caption: Fourth Judicial District Court, Utah County; State of Utah v. Tyler James Robinson; **Case No. 251403576**; Judge Tony F. Graf, Jr. Filing counsel per caption block: Jeffrey S. Gray, Utah County Attorney, with five Deputy Utah County Attorneys listed |
| **URLs** | `https://static.foxnews.com/foxnews.com/content/uploads/2026/08/Prosecutor_Reply.pdf` **and** `https://static.foxnews.com/foxnews.com/content/uploads/2026/08/744b16b3-Prosecutor_Reply.pdf` — **two URLs, one document: byte-identical** (`cmp` clean, same SHA-256). Retrieved **2026-08-20**, direct local fetch |
| **Filed date** | **2026-08-18**, from the document's own certificate of service (*"I certify that on August 18, 2026, I filed the foregoing … through the Court's electronic filing system"*) and its dated signature block (*"Dated August 18, 2026"*). Independently: reported filed 08-18 by the 2026-08-19 scheduled watch firing (T1 via T3, Fox + ABC legs) — report transcribed in CR-WATCH-log |
| **Banked** | `CR-ACQ-2026-07-27_court-record-artifacts/2026-08-18_states-reply-memo-bindover.pdf` (**277,548 bytes**, SHA-256 `0e287a048829b100f9b7e003d2b1475c75b43d0e755fff4f7f6f9fa67dfd14f2`) + `….txt` (pdftotext `-layout` extraction, 41,016 bytes — **extraction banked, contents not read**) |
| **Length** | **19 PDF pages; internal printed numbering runs to 19; the 19th page is the certificate of service.** The court's limit for this brief is **18** pages. ⚠️ **19 vs 18 is recorded and deliberately NOT reconciled** — whether the certificate page counts against the limit is not this file's call (same discipline as the 28-vs-35 hazard on the opening brief, but note the direction differs: there the number was *below* the limit) |

## 3. Provenance — two of three, stated exactly

| Element | Status |
|---|---|
| Signature block | ✅ present — *"/s/ Christopher D. Ballard"* for Jeffrey S. Gray, Utah County Attorney, dated 2026-08-18 (p. 18) |
| Certificate of service | ✅ present — e-filing certification dated 2026-08-18, /s/ Christopher D. Ballard (p. 19) |
| Clerk file-stamp | ❌ **not visible on the caption page** |

**Identical provenance grade to the banked defence brief:** outlet-hosted document text carrying the filer's own attestation, **not silently promoted** to a stamped filing. A court-stamped copy of *both* briefs remains sought (the defence brief's stamp gap is Q-63).

## 4. What was looked at, and what was not

**Pages viewed for this acquisition: 1 (caption), 18 (signature block), 19 (certificate of service) — for case identification and provenance structure only.** Pages 2–17 were **not read**. The extraction exists on disk unread. **No content of the memorandum — its arguments, characterisations, or quotations — is recorded in this file or anywhere else in the library.** A reasoned read is a separate act (a CR-E evidence file under the two-layer discipline), not part of an acquisition.

## 5. Hazards and residue

- ⚠️ **Naming trap:** the mirror hosts the same bytes under two filenames, one with a hex prefix (`744b16b3-`). A future diff seeing "two new Prosecutor_Reply files" should hash before counting documents.
- ⚠️ **"Prosecutor_Reply" is a generic filename** — nothing in the URL names the case. Identification rests on the caption page, not the filename; the same run cleared two same-batch lookalikes (`abdulloi-toshpulodzoda-court-filing.pdf` — Fairfax County, VA; `order-081726.pdf` — Supreme Court of NY, an unrelated matter) by caption check.
- **Residue (open):** Q-45 (State's *opening* brief, 07-28) — a same-session CDX enumeration of the mirror's `2026/07/` folder found **56 PDFs, none case-related: an attempted null**. The opening brief is still held nowhere. Court-stamped copies of all three briefs remain unheld.

**No case-posture statement in any topic file is altered by this acquisition. No D-register entry is assigned, resolved or moved. The filing's contents are not characterised beyond its title and date.** As of 2026-08-20, Tyler Robinson has NOT been bound over for trial — the preliminary hearing is not concluded; its last day (argument only) is 2026-09-01. Presumption of innocence applies throughout.

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-20 | File created. State's reply located by the Run-4 Wayback-CDX diff route (16 new PDFs on the mirror; three flagged, two cleared by caption check), fetched from both URLs, verified byte-identical, banked with SHA-256 + unread extraction. Filed date 2026-08-18 read from the certificate of service. Provenance two-of-three (signature ✅, certificate ✅, clerk stamp ❌), same grade as the defence brief. 19 pp. vs 18-page limit recorded, not reconciled. Q-45 July-folder re-attempt: attempted null (56 PDFs, none case-related). |
