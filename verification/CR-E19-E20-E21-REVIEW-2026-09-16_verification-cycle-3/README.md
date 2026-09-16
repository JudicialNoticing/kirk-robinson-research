# CR-E19-E20-E21 REVIEW — cycle 3 (propagation sweep), 2026-09-16 — STOPPED AFTER ENUMERATION

The cycle-3 brief (CR-REVIEW-2026-08-30 §10; START-HERE §0AE item 2) is a PROPAGATION sweep of every correction applied in cycles 1–2. A workflow was launched to enumerate the corrections and sweep each one's footprint with one sweeper and one isolated verifier per claim. **The owner stopped it before any sweeper ran** ("there should not be 79 agents"). What survives:

- `enumeration_merged-74-claims.json` — four enumerators' lists (E19 31, E20 26, E21 30, deliverables/carriers 21 = 108 entries) merged and de-duplicated to **74 corrected claims** (C-01…C-74), each with the withdrawn form, search terms, the corrected form and known record sites; plus the enumerators' `gaps` list.
- `journal_wf_49721daa-15d.jsonl` — the workflow journal (5 agents: four enumerators, one merge).

Three record-integrity defects the enumerators found while reading, none yet fixed: **CR-E19's revision log stops at 2.2 while its header says v2.3; CR-E20's log stops at 1.5 while nine inline stamps say v1.6; CR-E21's log stops at 1.2 while its status says v1.3.** Also: the three FBI surnames withdrawn from CR-E19 on 08-30 were re-imported into the TJR verification bank on 09-14 by the profile's cycles; and the 09-01 record is stale in one direction (the docx WAS corrected at d3b64a0; the artifact was not).

Recommended next shape (owner to size): a script greps all 74 withdrawn forms across the 109-file scope and the two deliverables first; readers go only to files with hits.

## Readers and applied fixes (running log, 2026-09-16)

- **Deliverables reader** (`reader_DELIVERABLES.json`): docx 63 hits → 13 STALE (5 claims, 8 sentences), all three 2026-09-01 defects already fixed; live artifact 58 hits → 39 STALE, all three 2026-09-01 defects still standing.
- **Docx corrected in place, 2026-09-16 ~20:40 EDT** (`deliverables/Forensic-Sampling-Summary_2026-08-30.docx`, sha256 `07b880b1…`, 23,874 bytes): ten replacements — C-14 ×2, C-30, C-56, C-62 ×3, C-66, and the owner's posture ruling ×2 (opening box; foot). C-62 was NOT applied as the reader proposed ("fifteen items") — 🛠 a first pass did apply it by mistake (a list-vs-string check in the script) and was corrected minutes later: the census total is an open register question (`D-70`; TJR-P01 §16 SINK holds four incompatible totals), so the document now says the count is unsettled instead of asserting a number. Method: run-level text replacement inside `word/document.xml` where the sentence sat in one run (7 of 10); three paragraphs (§6 "It is a census…", §6 "This was a probable-cause hearing…", §7 lead and §9 "What remains unobtained") were rebuilt as a single run, which flattened their inline bold. No other paragraph touched; the file re-validates as a zip and re-extracts.
- **Artifact patch banked** (`artifact-patch_2026-09-16.json`): 14 old→new replacements for the LIVE HTML (the twelve STALE items plus the posture ruling twice). **Not applied — publishing is owner-gated**; viewers see a pinned earlier version and re-pinning is a UI action.
