# INDEX — every significant file, one sentence each, and when you would need it

**Prepared:** 2026-09-15 · Regenerate mentally, not mechanically: this is a hand-written map. `SOURCE-MANIFEST.md` (generated) lists every banked artifact; this file lists the research, the tools and the process. Paths are relative to the repo root. Versions are as of 2026-09-15.

**Reading order for a newcomer:** `README.md` → `START-HERE.md` → `QUEUE.md` → the profile `TJR-P01` → `DNA-E01` → `CR-E19`/`E20`/`E21` → `docs/ARCHITECTURE.md`.

---

## Root

| File | What it is | Use when |
|---|---|---|
| `README.md` | What the library is, the layout, how to run the tools, where to start | First visit; after a break |
| `START-HERE.md` | The dated session snapshot: what is time-critical, what waits on the owner, traps. Sections are stacked newest-first (§0AF = 2026-09-02). ⚠ No row yet for 2026-09-14 | Beginning any session |
| `QUEUE.md` | The work graph: every open item (`Q-nnn`) with status, blocker, decisive artifact, cost and gate; the **canonical D-register ceiling** in its header; the standing hazards | Choosing what to do next; assigning a D-number; before dispatching anything |
| `LOOP.md` | The autonomous execution protocol: the cycle, provisional-findings rule, the three gates and the always-human list, hard stops | Before running any cycle unattended |
| `DOCKET-WATCH.md` | The court-calendar half: deadlines, access routes, the routine's history, observed statuses | Anything with a date on the docket |
| `CLAUDE.md` | The library's constitution: purpose, two-layer rule, tiers, registers, objectivity mechanics, living-persons care, file conventions | Before creating or editing any file |
| `VERIFICATION-PROTOCOL.md` | The Research Verification Kit as adopted: labels, isolation rule, taint, iteration cap, sink, no self-certification, the router (which protocols to run) | Before any verification, audit, correction or new evidence file |
| `SOURCE-MANIFEST.md` / `source-manifest.json` | **Generated** holdings index: every artifact's hash, class, readability hazard, how to read it, who cites it. Never hand-edit; run `./scripts/manifest.py` | Before asserting any null; to find out whether something is already held |
| `INDEX.md` | This file | Finding things |
| `AUDIT.md` | The 2026-09-15 audit and reorganisation plan, with the per-file mapping | Understanding why the layout is what it is |
| `.gitignore` | Ignores Finder metadata, Obsidian workspace state, bytecode, the harness checkpoint | — |

## files - Person profiles/

| File | What it is | Use when |
|---|---|---|
| `robinson-tyler-james-comprehensive-profile.md` | **TJR-P01 v2.5 `[PROVISIONAL]`**: the defendant end to end — identity, household, charges, the State's narrative, the surrender, the forensic record naming him, digital material, media narratives, case posture as of 2026-09-14. Carries its own P2/P3/P5/P7/P8/P9 registers (§15–§19) and a sink (§16) | Any question about Robinson; the model for a fully protocol-verified file |
| `lance-twiggs-comprehensive-profile.md` | The roommate and partner, compiled 2026-07-10 from charging documents, warrants, hearing testimony and reporting; reconciled against later T1 material by `CR-REVIEW-2026-08-16G` | Twiggs' statements, the Discord/phone material, D-75 |
| `erika-kirk-background-family-contested-claims-dossier.md` | Erika Kirk's documented background separated from the contested claims about it; her role in the proceeding | Any Owens-series claim about her; the victim-representative filings |
| `PP-ACQ-2026-09-15_platform-imports.md` | **PP-ACQ-2026-09-15**: the acquisition record for the 2026-09-15 platform imports — what arrived from the owner's Grok workspace, hashes, what it does and does not establish (nothing: all T4) | Before touching anything in the bank below; Q-185 |
| `PP-ACQ-2026-09-15_platform-imports/` | The platform-import bank: *Charlie Kirk on Israel and the Jewish World — A Documented Record* (HTML + text extraction), two verbatim Grok conversations of 2026-08-22 about Robinson (charging-document quote; "political leftist motive"), and the Grok project's own instructions. `manifest.py` classes all of it `platform-import` | Reading what the model said; never citing it |

## files - Court record/

### Evidence files (`CR-E*`)

| File | What it is | Use when |
|---|---|---|
| `CR-E01_prelim-hearing-Day4_Karner-ATF-testimony.md` | Sworn testimony of the ATF firearm/toolmark examiner who wrote the 2025-09-17 report (v1.3) | Toolmarks, the rifle, the engraved cartridges |
| `CR-E02_prelim-hearing-Day4_Faumuina-Davis-Twiggs.md` | Day 4: Sgt. Faumuina (lead scene witness, 330 turns), SBI Agent Davis, and the Twiggs sworn statement (v1.8) | Scene processing, exhibit numbers read into the record, the Twiggs account |
| `CR-E03_prelim-hearing-Days2-3-5.md` | Days 2, 3 and 5: Bakker (FBI), Davis, Oliver (ATF); **partial and says so** (v1.5) | Which testimony has and has not been read |
| `CR-E04_prelim-hearing-Day2_Hull-UVU-surveillance.md` | Agent Hull and the UVU surveillance-video timeline (v1.2) | The 11:51 campus entry, the rooftop route, the timeline |
| `CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md` | Day 1 read end to end: Officer Bagley and Hull's first tranche (v1.4, VERIFIED) | Event security, first response, the Day 1 label hazard |
| `CR-E06_Bakker-Day2_Oliver-Day5_full-read.md` | The two DNA analysts read in full: FBI (Day 2) and ATF (Day 5) (v1.7) | Anything about what a DNA analyst actually said |
| `CR-E07_defence-prelim-briefing-2026-08-11.md` | The defence's preliminary-hearing brief: identity contested on all seven counts as hearsay, the single aggravator attacked (v1.6) | The defence's position before bindover |
| `CR-E08_state-information-and-pc-affidavit-2025-09-16.md` | The Information and the Affidavit of Probable Cause, read directly; 26 claims adversarially tested (v1.1) | The charges, the State's pleaded narrative, D-74/D-75 |
| `CR-E09_evidence-preservation-order-and-pretrial-practice.md` | The preservation-order chain, the open-file policy, the pretrial protective order (v1.1) | Discovery practice |
| `CR-E10_publicity-order-and-record-classification.md` | The pretrial publicity order and the classification of records (v1.4) | What may be said publicly; which records are classified |
| `CR-E11_prosecutor-disqualification-track.md` | The motion to disqualify the county attorney, both sides read in full, and the T1 evidence that entered the record as its exhibits (v1.0) | The sworn sight-line re-enactment; the proffer of 2026-02-02 |
| `CR-E12_closure-classification-and-sealing-map.md` | Every closure, sealing and classification event; the four confusable "protective orders" (v1.0) | Whether something is public, sealed or closed |
| `CR-E13_evidence-preservation-chain-complete.md` | The complete preservation dispute from the primary documents (v1.0) | What the preservation order requires and does not reach |
| `CR-E14_continuance-motion-and-the-discovery-record.md` | The motion to vacate or continue (69 pp., Exhibits A–G) and the speedy-trial invocation; the discovery record it puts on file (v1.3) | The forensic discovery letter; the chronology gap; D-70 |
| `CR-E15_ATF-firearms-report-2025-09-17.md` | The ATF firearms report read directly from the document (State's Exhibit 32) (v1.2, `[PROVISIONAL]`) | The only laboratory report the library has read |
| `CR-E16_participant-roster-and-label-reconciliation.md` | Who is who: every participant verified against held sources, and the Rev-label reconciliation (v1.1) | Naming any speaker; resolving a transcript label |
| `CR-E17_states-reply-2026-08-18.md` | The State's reply memorandum on bindover, a reasoned read (v1.1, VERIFIED) | The State's position before bindover |
| `CR-E18_certified-transcript-crosswalk.md` | Both briefs' certified-page pin-cites located in the Rev renderings (v1.1, VERIFIED) | Following a brief's citation into `dayN.txt` |
| `CR-E19_latent-print-record.md` | The complete friction-ridge record: what was printed, the exclusions, the nulls on rifle, towel and screwdriver (v2.3, `[PROVISIONAL]`) | Fingerprints; the window latents; D-76 |
| `CR-E20_forensic-exhibit-map.md` | Which laboratory report is which State's exhibit; the "Exhibit 30" collision (v1.6, `[PROVISIONAL]`) | Before citing any exhibit number |
| `CR-E21_forensic-discovery-census.md` | The laboratory reports named in the defence's 2026-03-25 discovery letter, fifteen across three labs, one held (v1.3, `[PROVISIONAL]`) | What forensic reports exist that the library has not read |

### Acquisition logs (`CR-ACQ-*`)

| File | What it is | Use when |
|---|---|---|
| `CR-ACQ-2026-07-27_court-record-acquisition.md` | The first acquisition pass: the access-path map (free / paywalled / bot-gated), what was banked, what it establishes (v2.0) | Any question of how a court document was obtained |
| `CR-ACQ-2026-08-14_contempt-transcript.md` | The Rev contempt-hearing transcript (Q-46) | The contempt proceeding |
| `CR-ACQ-2026-08-14B_supplemental-notice-2026-07-08.md` | The victim's family's supplemental notice on access to evidence (Q-57) | Victim-representative filings |
| `CR-ACQ-2026-08-14C_xchange-docket.md` | Two XChange case-history printouts; partial execution of Q-03 | The docket as of 2026-03-14 |
| `CR-ACQ-2026-08-16_documentcloud-complete-sweep.md` | DocumentCloud project 224251 completed (46/46) plus nine filings found outside it; provenance and hash discipline (v1.5) | The bank's provenance |
| `CR-ACQ-2026-08-16B_rev-official-statements.md` | Four official-statement transcripts the surname filter had hidden (Q-120) | Press conferences of 2025-09-10 to 09-12 |
| `CR-ACQ-2026-08-20_states-reply.md` | Banking of the State's reply; facial verification only | Provenance of `CR-E17`'s source |
| `CR-ACQ-2026-09-01_hearing-livestream-capture.md` | The capture record of the 2026-09-01 livestream: two recorders, the stall, the 9:45:10 VOD held | The bindover hearing audio/video |
| `CR-ACQ-2026-09-16_prelim-hearing-audio-capture.md` | Audio of the five July evidence days from two independent pool-feed uploads (Court TV, KSL), held outside the repo; hashes, durations, and ten spot-checks against the Rev transcripts — Court TV's clock is Rev's clock | The evidence-day audio; testing Rev's speaker labels and garbles |
| `CR-ACQ-2026-09-16B_states-opening-memorandum.md` | Banking of the State's 07-28 opening memorandum from the Scribd mirror's page renderings (28/28, hashed); facial provenance two-of-three; contents not characterised | Provenance of the last bindover brief; feeds Q-187 |

### Audits and reviews (`CR-AUDIT-*`, `CR-REVIEW-*`)

| File | What it is | Use when |
|---|---|---|
| `CR-AUDIT-2026-07-27_adversarial-pass.md` | Self-audit of the first court-record output; §2.2's D-50 later dissolved (v1.1) | History of D-50/D-51 |
| `CR-AUDIT-2026-07-28_independent-pass.md` | The first independent adversarial pass (Q-02): six defects, three material (v1.2) | Why LOOP.md is cautious |
| `CR-AUDIT-2026-08-01_session-audit.md` | The 2026-08-01 session: Q-54, Q-52, Q-11, Q-06, Docket Watch run 2; the Q-08 DNA draft blocked (v1.4) | What that session did and did not verify |
| `CR-AUDIT-2026-08-20_session-audit.md` | One row per cycle of the 2026-08-20 research session, every file → version change | Same, for 08-20 |
| `CR-REVIEW-2026-08-14_losee-draft-Q07.md` | Three-reviewer review of the unpublishable Losee draft (v1.1) | Before any Losee work |
| `CR-REVIEW-2026-08-16_Q61-carried-nulls.md` | The five nulls carried from CR-E06 into DNA-E01 without re-running: 5/5 confirmed | Null hygiene |
| `CR-REVIEW-2026-08-16B_xchange-null-audit.md` | 26 claims resting on the XChange printouts re-run after `grep` was found to fail silently on them | Hazard 13 |
| `CR-REVIEW-2026-08-16C_Q61-tranche3.md` | Q-61 tranche 3: self-claims and completeness candidates; a revision log that lied about itself | Self-count hazard |
| `CR-REVIEW-2026-08-16D_Q105-null-re-runs.md` | Every null recorded under the broken tool, re-run by three readers (~70) | Hazard 13 remediation |
| `CR-REVIEW-2026-08-16E_Q111-legacy-file-audit.md` | ~100 nulls and counts in CR-E01–E07, CR-WATCH-log and the candidate banks, re-run | Same, for the legacy files |
| `CR-REVIEW-2026-08-16F_Q89-losee-draft-vs-sworn-geometry.md` | The Losee draft against the State's sworn sight-line re-enactment | Losee geometry |
| `CR-REVIEW-2026-08-16G_twiggs-profile-reconciliation.md` | The Twiggs profile against the T1 record it predates | Before citing the Twiggs profile |
| `CR-REVIEW-2026-08-17_Q146-Q148-Q131.md` | The Count-4 date conflict, the contaminant's measured profile, and a validator that was 75% blind (`[PROVISIONAL]`) | The contaminant; queue-check history |
| `CR-REVIEW-2026-08-30_CR-E19-E20-E21-verification-cycle.md` | Cycles 1 and 2 on the three 08-30 files: two falsified nulls, and every correction round introducing its own defects (v2.1, `[PROVISIONAL]`) | Before cycle 3 on those files |
| `CR-REVIEW-2026-09-16_cycle-3-propagation-sweep.md` | Cycle 3 on the three 08-30 files: the propagation sweep — script-first, 21 isolated readers, 124 stale hits and ~60 off-list carriers corrected across 27 files, the docx and the origin files themselves; the posture inference "closed evidentiary record" found standing in thirteen files; `[PROVISIONAL]` restated at the three-iteration cap (v1.0, `[PROVISIONAL]`)  |
| `CR-WATCH-log.md` | One row per docket-watch run, including runs that found nothing; v2.4 transcribes three September firings that ran dark and the root cause (routine cannot see the private repo). **Named by the cloud routine; never move** | What the watch saw, and when it was blind |

### The banks (raw evidence — never moved, renamed or edited)

| Folder / file | What it is | Use when |
|---|---|---|
| `CR-ACQ-2026-07-27_court-record-artifacts/` | The court bank: 59 PDFs with `.txt` extractions, named `YYYY-MM-DD_slug_dktN_dcID`, plus the transcripts folder, Rev official statements, rendered ATF pages, and (mixed in) process outputs. Full list with hashes and readability: `SOURCE-MANIFEST.md` | Reading any primary court document |
| ↳ `prelim-hearing-transcripts/day1.txt … day5.txt`, `*_raw.html`, `*_condensed.txt` | The five hearing days (2026-07-06 → 07-10) as Rev rendered them, with the raw HTML captures and older condensed views; `2026-09-01_final-prelim-argument.txt` is the bindover argument. Search with `scripts/tsearch.py` | Any quotation from the hearing |
| ↳ `2025-09-16_information-charging-document_dc27880532.*`, `2025-09-16_affidavit-of-probable-cause_dc27880530.*` | The charging documents (T1) | The charges; the DOB; the pleaded narrative |
| ↳ `2026-09-01_ruling-and-order-on-preliminary-hearing-bindover_signed.pdf` | The signed 26-page bindover order, clerk's certificate 09/02/2026. **No text layer**: render it | Case posture |
| ↳ `2026-08-11_defendant-prelim-hearing-briefing*.txt` | The defence brief (`CR-E07`) | — |
| ↳ `2026-04-02_motion-vacate-continue-march-27-2026_dc2799818{4,8,9}.*` | The continuance motion (`CR-E14`, `CR-E21`), three DocumentCloud postings of one filing | The forensic discovery letter (Exhibit F) |
| ↳ `2026-08-16_rev_*.txt` (4) | Official-statement transcripts: press conferences of 2025-09-10/11/12 | Tier 2 statements |
| ↳ `atf_page-26…29.png` | The rendered pages of the ATF firearms report (`CR-E15`); the readable form of an illegible PDF | The report's face |
| ↳ `2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.*` | **The contaminant**: a mis-banked unrelated federal filing, 23 MB. Excluded per term, never cited as case evidence | Knowing why counts say "excluding the contaminant" |
| ↳ `2026-08-01_BLOCKED-DRAFT_q08-dna_DO-NOT-PUBLISH.md`, `2026-08-01_UNREVIEWED-DRAFT_losee_DO-NOT-PUBLISH.md` | Drafts that must not be cited or published: the DNA draft superseded by `DNA-E01`; the Losee draft whose review never completed (its `LOSEE-E01` ID was never ratified) | Only as the input to a future attempt |
| ↳ `2026-08-14_Q61-candidate-bank_INDEX.md` + `*_RAW-CANDIDATES.jsonl` | A harvest of completeness candidates; nothing verified | Resuming Q-61 |
| ↳ `*_RAW.json`, `*_RAW.md`, `*-workflow-script.js`, `docket-artifacts_2026-08-16_NUL-repair.py`, `*_receipts.json`, `docket-watch-baseline.json` | Process evidence and one-off scripts from the August workflows, kept where their outputs are cited | Auditing what a past cycle actually did |
| `CR-ACQ-2026-09-02_bindover-verification-fetches/` (+ `MANIFEST.md`) | Raw HTTP bodies from the 09-02 verification run (court, prosecutor, outlets, transcripts), each hashed in its `MANIFEST.md` | What the world said on 2026-09-02 |
| `CR-ACQ-2026-09-16_prelim-hearing-audio-capture/` | Pointers for the July audio held in `~/kirk-capture/prelim-july-2026/`: `SHA256SUMS.txt`, `durations.tsv`, `sources.json`, and the ten whisper spot-check transcripts | Provenance of the evidence-day audio |

## files - DNA evidence/

| File | What it is | Use when |
|---|---|---|
| `DNA-E01_DNA-evidence-what-it-can-bear.md` | **v4.9**, 303 KB: the DNA evidence at the hearing, both laboratories, what it is asked to establish and what it can bear; the Rule 702 question expressly undecided | Anything about DNA, likelihood ratios, consumption, mixtures |
| `Kirk-Robinson_DNA-Evidence_Consolidated-Audit_2026-07-15.md` | The predecessor file (consolidates three July work products); still cited | History of the DNA file |
| `Kirk-Robinson_DNA-Evidence_Acquisition-Roadmap_2026-07-15.md` | The primaries that would lift "T1 via T3" DNA claims to T1 | Planning acquisition |

## files - Event security/

| File | What it is | Use when |
|---|---|---|
| `SEC-E01_security-posture-2025-09-10.md` | The security arrangement at the UVU event from sworn testimony and the proffer (v1.1, `[PROVISIONAL]`) | Who was responsible for what on the day |
| `SEC-E02_security-team-allegations-assessment.md` | The "palm pistol" and "Israeli security team" allegations recorded faithfully and tested against the T1 record (v1.1, VERIFIED) | Those allegations |
| `2026-08-20_singju-srs254-harpole-transcript.txt` (+ `_RAW.html`) | A captured interview transcript cited by `SEC-E02` and the Zinn file | Its quotations |

## files - Arrest chronology/

| File | What it is | Use when |
|---|---|---|
| `robinson-surrender-timeline.md` | The surrender of 2025-09-11/12: timeline, details, sourcing; 52 files cite it | The walk-in, the family's account, the name reaching investigators |
| `tier1-acquisition-roadmap.md` | Primaries that would firm up the chronology | Planning acquisition |

## files - Kirk assassination questions/

| File | What it is | Use when |
|---|---|---|
| `kirk-shooting-official-timeline.md` | "The Rifle's Path": the official timeline of the shooting | The event timeline as officials stated it |
| `evidence-rifle-photo-nypost-authenticity.md` | Authenticity of the NY Post rifle photograph: substantially resolved with authentication caveats | The photo |
| `t1 source acquisition roadmap - Kirk assassination questions.md` | Roadmap | Planning acquisition |

## files - George Zinn/

| File | What it is | Use when |
|---|---|---|
| `zinn-george-evidence.md` | **ZINN-E01**: Zinn's actions on 2025-09-10, motives, prosecution, the unverified "payment" claim | Zinn |
| `ZINN-ACQ-2026-08-20_zinn-pcas.md` | The two Zinn probable-cause affidavits; the sexual-exploitation PCA's narrative deliberately unread (`[PROVISIONAL]`) | Provenance of the PCAs |
| `ZINN-REVIEW-2026-08-17_partial-reconciliation.md` | Reconciliation of the evidence file against T2 material; three refutations | Before citing the Zinn file |
| `t1 source acquisition roadmap - George Zinn.md` | Roadmap | Planning acquisition |
| `ZINN-ACQ-2026-08-20_artifacts/` | Six DocumentCloud JSON captures | Provenance |

## files - Losee building/

| File | What it is | Use when |
|---|---|---|
| `losee-rooftop-firing-evidence.md` | Evidence that a gun was fired from the Losee Center rooftop (2026-07-18; predates the hearing files) | Losee, with `CR-REVIEW-2026-08-16F` beside it |
| `tier1 source acquisition roadmap - forensic evidence for Losee building shot.md` | Roadmap | Planning acquisition |

## files - Bride of Charlie series/

| File | What it is | Use when |
|---|---|---|
| `BOC-E01 … BOC-E08_*_claim-inventory.md` | One claim inventory per episode of Candace Owens' series: every checkable claim, its anchor, its status | Any claim from the series |
| `BOC-T1_Tier1-Acquisition-Roadmap_all-episodes.md` | Every T1-relevant open item across the episodes, mapped to acquisition mechanics (M-numbers) | Planning acquisition |
| `BOC-ACQ-2026-07-19_phase0-pull-log.md` | Execution log of Phase 0 (free, immediate sources): clusters A–F acquired and adjudicated | Provenance of the BOC artifacts |
| `BOC-AUDIT-2026-07-18_library-audit.md`, `…07-18B_library-audit.md` | The first library audits (status-line integrity, twelve external verifications) | History |
| `BOC-AUDIT-2026-07-20_session-audit.md`, `…07-27_session-audit.md`, `…07-27B_adversarial-pass.md` | Session audits and the adversarial pass that established hazard 5 (search nulls) | History; the origin of `tsearch.py` |
| `BOC-ROUTE-2026-07-27_post-series-case-claims-corpus.md` | Registration and routing of the regular episodes after the series (resolves D-46) | Post-series claims |
| `BOC-ACQ-2026-07-20_F2-artifact-copies/` (+ `neffmar/`) | Archive captures of tweets, pages and API JSON supporting the inventories | Provenance |
| `BOC-E08_transcript-artifacts/`, `BOC-ROUTE-2026-07-27_artifacts/` | Podcast feed XML and machine-transcript extractions (`yt_captions.json3` is an empty failed capture) | Provenance |

## verification/

| Folder | What it is | Use when |
|---|---|---|
| `TJR-REVIEW-2026-09-14_verification-cycle-1/` | The TJR-P01 verification bank: `cycle1–3_*` (the pre-protocol cycles that violated isolation), `p8_*`, `p9_*`, `p7_*`, `p2_*`, `p3_*`, `p5_*` and their iteration-2, repair and second-hand files, five workflow journals, and 13 frozen snapshots `profile_v1.0 … v2.3` | Auditing any TJR-P01 finding; re-running a protocol; never edit the snapshots |

## docs/

| File | What it is | Use when |
|---|---|---|
| `ARCHITECTURE.md` | The five layers and the data flow; scripts and what they touch; identifiers; external dependents | Understanding how the pieces fit |
| `DECISIONS.md` | Why things are the way they are, with inferences marked; open items | Before changing structure or tooling |
| `GLOSSARY.md` | Every term: tiers, labels, registers, hazards, artifact classes, case vocabulary | Any unfamiliar word |
| `VERIFICATION-KIT-INDEX.md` | Index of the kit | Finding a protocol or prompt |
| `research-verification-kit/` | The Research Verification Kit (P1–P10, prompt pack, schemas, background), hash-manifested | Running a verification cycle |
| `discussion-framework/` | The *Epistemic Framework and Analytical Method* v1.0 and its *Discussion Card* (T4 imports, 2026-09-15): an outward-facing method for discussing the case, no case claims, a tier system that differs from CLAUDE.md's (its README says how) | Talking about the case with someone outside the library; not for writing library files |

## scripts/

See `README.md` §Tools for usage. `manifest.py` (holdings index), `artifact_search.py` (safe search of the bank), `tsearch.py` (transcript search with a known-positive check), `queue-check.sh` (queue and register integrity), `docket-watch-run.py` (local docket check), `build-html.py` / `build-docx.js` (deliverables), `migrate-files.sh` (verified copy).

## ops/docket-watch/

| File | What it is | Use when |
|---|---|---|
| `DOCKET-WATCH-routine-prompt-LIVE-2026-08-29.md` | The prompt text deployed on the cloud routine, as of 2026-08-29 (kept because an `allowed_tools` change once wiped it) | Before touching the routine |
| `DOCKET-WATCH-routine-prompt-DRAFT-2026-09-14.md` | The replacement prompt for the post-acquisition window. **Not applied**; applying it is owner-gated | Updating the routine |

## deliverables/

| File | What it is | Use when |
|---|---|---|
| `Tyler-Robinson_Comprehensive-Profile_2026-09-17.html` / `.docx` | Renders of TJR-P01, **rebuilt from v2.7 on 2026-09-17 (Q-188)** — the first pair that carries the owner's 2026-09-16 posture ruling. The 09-14 pair (from v2.5) is at `archive/deliverables-superseded/` | Sharing the profile |
| `Forensic-Sampling-Summary_2026-08-30.docx` | DNA and print sample counts by item, from `CR-E21`; no markdown source | Sharing the forensic census |
| `Epistemic-Framework-and-Analytical-Method_2026-09-15.html` · `Discussion-Card-Kirk-Robinson-Case_2026-09-15.pdf` | Renders of `docs/discussion-framework/` as downloaded from the Grok workspace | Sharing the discussion framework |

## ops/site/ — the public-site build (Phase 1, not deployed)

Added 2026-09-17. **Nothing here deploys anything by existing**; a site appears only when the repository is connected to a host, which is an owner gate (`LOOP.md` §3).

| File | What it is | Use when |
|---|---|---|
| `ops/site/site.yml` | **The publish allow-list**, and the only thing that decides what a site contains. Each markdown file is `publish`, `hold` (owner decision pending) or `never` (named hard block, with a reason). Nothing publishes by being present on disk | Ruling on scope (Q-190); changing what the site carries |
| `ops/site/BUILD-REPORT.md` | **Generated on every build, never hand-edited.** Every file in exactly one state, plus the counts, the trees excluded wholesale, and the unpublished files that published pages cite most | Auditing what a build would expose |
| `ops/site/requirements.txt` | Build dependencies, used by `netlify.toml` and the local venv | — |
| `scripts/build-site.py` | Stages an allow-listed copy into `.site-build/` (gitignored), injects each page's source path, version and status token, rewrites internal links and neutralises links to unpublished files, then runs mkdocs. **The `files - <Topic>/` namespace is never touched** | `./.venv-site/bin/python scripts/build-site.py --serve` |
| `netlify.toml` | Build command and publish directory. Inert until someone connects the repo | Phase 3 |

⚠ **The site is generated on every build and never hand-maintained** — so there is one source of truth and no separate derived copy to sweep. This is the direct answer to the defect Q-188 was: a derived deliverable that left the repository and was missed by three correction rounds.

## archive/

Superseded routine-prompt drafts, the verification-kit drop duplicates, and (since 2026-09-17) the v2.5 profile renders replaced under Q-188. See `archive/README.md` for what is there and why.
