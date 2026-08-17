export const meta = {
  name: 'q137-q138-person-files',
  description: 'Q-137 the Robinson arrest chronology and Q-138 the Erika Kirk dossier: reconcile both against the primary court record they predate, run living-persons passes, and produce apply-ready plans',
  phases: [
    { title: 'Find137', detail: 'arrest chronology — custody chain, filename dates, officials, living-persons, completeness' },
    { title: 'Find138', detail: 'Erika Kirk — court-record spine, the family roster, the claims register, scope, completeness' },
    { title: 'Verify', detail: 'adversarial refutation, two lenses per finding' },
    { title: 'Plan', detail: 'two apply plans + a completeness critic across both' },
  ],
}

const ROOT = '~/Documents/Kirk Robinson Research'
const ART = `${ROOT}/files - Court record/CR-ACQ-2026-07-27_court-record-artifacts`
const TX = `${ART}/prelim-hearing-transcripts`
const CHRON = `${ROOT}/files - Arrest chronology/robinson-surrender-timeline.md`
const CHRON_RM = `${ROOT}/files - Arrest chronology/tier1-acquisition-roadmap.md`
const ERIKA = `${ROOT}/erika-kirk-background-family-contested-claims-dossier.md`

const RULES = `
YOU ARE WORKING INSIDE A LEGAL-RESEARCH LIBRARY WITH STRICT STANDING RULES. Obey them.
PATHS CONTAIN SPACES — quote them in shell commands. Repo root: "${ROOT}"

🚨 CASE POSTURE, verified 2026-08-17. TYLER ROBINSON HAS NOT BEEN BOUND OVER. The preliminary hearing is UNFINISHED: 2026-07-06 → 07-10 were five days OF EVIDENCE; 2026-09-01 is its LAST DAY, ARGUMENT ONLY, on a closed evidentiary record. Never write that the hearing "concluded" on 07-10. PRESUMPTION OF INNOCENCE IS ABSOLUTE and is load-bearing in the arrest-chronology file more than in any other file in this library — it narrates the conduct of a capital defendant before any adjudication whatsoever.

THE TWO LAYERS, NEVER BLENDED. (1) Recording layer — what a claimant actually said, cited, even when false. (2) Analyst layer — what the established record shows, with tier and confidence. Recording a claim is never endorsing it. Asserting analyst-layer fact without independent verification is this project's cardinal error.

SOURCE TIERS. T1 = sworn testimony and primary court filings. T2 = named official statements. T3 = named journalism. T4 = anonymous / low-verification / genealogy-aggregator material. Mark "T1 via T3" when primary-document content is known only through reporting — NEVER silently promote. A grade must trace to AN ACTUAL VERIFICATION ACT BY THIS PROJECT: not inherited from a claimant, not inherited from repetition across outlets (syndicated recaps are ONE source, not many).

LIVING-PERSONS RULES — the hardest constraint in this task.
- Private individuals get ROLE AND RELEVANCE ONLY. No home addresses, no contact details, no identifying information about uninvolved parties — EVEN WHEN SOURCES PUBLISH IT.
- Allegations are attributed, never adopted.
- Quotations from filings are kept minimal; paraphrase everything else.
- 🚨 THE INCLUSION TEST IS NOT THE ACCURACY TEST. Recording-layer fidelity governs whether a claim is reported FAITHFULLY. The living-persons rule governs whether it belongs in the file AT ALL. A passage can be perfectly faithful to its source and still fail the inclusion test. This distinction has already had to be applied twice in this library; apply it here.

SEARCH HAZARDS, all measured in this library:
- Files in "${ART}" carry U+FFFE where a hyphen + line break belonged, so "Pre-Trial", "Pre Trial" and "PreTrial" can ALL miss. Use "${ROOT}/artifact_search.py" (find(pattern, path)), which searches BOTH readings. A null is real only if it holds under both, and you must SAY you checked both.
- Some artifacts contain NUL bytes and are "data" to file(1); grep can return NOTHING AT ALL on a file with matches. Read in Python with errors='replace' where a grep null looks suspicious.
- 🚨 CORPUS CONTAMINATION, AND THE REMEDY IS PER-TERM, NOT PER-FILE. "${ART}/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt" is a mis-banked unrelated case (BAM Franchising v. "Reckless Ben"). Measured false hits: 9 "roommate", 6 "partner", 5 "cop car". ⚠️ BUT "Robinson" returns 4 hits in it and ALL FOUR ARE TRUE — genuine citations to this case. So EXCLUDE IT PER TERM AND SAY WHICH TERM; a blanket exclusion would destroy true hits.
- A NULL BATTERY CANNOT TEST WHAT ITS PATTERNS CANNOT REACH. When claiming absence, at least one pattern must be CAPABLE of matching the thing claimed absent — say which. (A "Charlie Kirk = 0" check was once used to conclude a file was unrelated to this case; it cites the case by docket number four times.)
- SEARCH THE STEM, and search NUMERALS AND WORDS for any number. A plural-only search against a singular transcript has already produced a false null here.
- SELF-COUNTS IN THIS LIBRARY RUN ONE LOW. Recount by parsing any cardinal number in a file's self-description.
- UTAH CASE NUMBERS ARE NOT UNIQUE ACROSS COURTS. 251403576 returns both this case and an unrelated Salt Lake City Justice Court matter. Any case number needs court + county.
- REV TRANSCRIPT SPEAKER LABELS ARE NOT EVIDENCE. Infer every speaker from CONTENT; where label and content disagree, content wins. Rev timestamps are stream offsets, ±5 minutes as clock times, never converted to a time of day without that mark.
- 🚨 F-39 / METADATA IS NOT CONTENT: A FILENAME IS A CLAIM SOMEONE TYPED. Banked filenames were generated from uploader-supplied DocumentCloud titles and several are WRONG. Read the document's FACE for its date, its parties and its docket number — never the filename.

VERIFY IN BOTH DIRECTIONS. Search for evidence that SUPPORTS the file as hard as for evidence that undercuts it, and LOG CONFIRMATIONS EXPLICITLY. An audit trail that only ever moves one way is itself a bias signal.
`

const RECON = `
✅ RECONNAISSANCE ALREADY PERFORMED BY THE COORDINATOR — verified by direct reading, 2026-08-17. Build on it; do not re-derive it, but DO test it if your lens bears on it.

1. 🚨 THE BAIL ORDER'S FILENAME DATE IS WRONG. "${ART}/2025-09-16_bail-order_dkt4_dc27880869.txt" is dated ON ITS FACE "Dated: September 12, 2025 … 08:40:00 AM", signed "/s/ SHAWN R HOWELL, DISTRICT COURT JUDGE". It carries "Probable Cause ID : 505275" and "Submission ID : 3307381", the caption "IN THE PROVO DISTRICT COURT DISTRICT COURT" (the duplication is in the document), and NO case number — consistent with its having been signed before the case number existed. It recites "the affirmation of Brian Davis, the arresting officer" and finds "The current offense is a Capital Felony".
2. 🚨 THE BOOKING RECORD IS A DEGRADED-OCR NEAR-NULL AND MUST NOT BE SEARCHED AS TEXT. "${ART}/2026-03-15ca_utah-county-sheriff-office-inmate-custody-booking_dc27880534.txt" is 788 bytes of garble. Fragments legible: "ROBINSON, TYLER JAMES"; "Aree 09122025 040000"; "Soket: 0912720751758 1500"; charge strings resembling felony discharge of a firearm causing serious bodily injury and obstruction of justice capital/first-degree felony. ⚠️ THE .pdf SIBLING EXISTS. RENDER IT (pdftoppm at high DPI, or pdftotext -layout) RATHER THAN TRUSTING THE TEXT LAYER — this library has already had one document stay unread for three weeks because its text layer was mojibake. Any timestamp read out of the garble is Tier 4 UNTIL the render confirms it.
3. THE PUBLIC SAFETY ASSESSMENT is at "${ART}/2025-09-12_public-safety-assessment-report_dkt3_dc27880877.txt". 🚨 HARD PII GATE, OWNER DECISION OF 2026-08-16, STANDING: ITS SCORES, ITS FACTORS AND ITS RECOMMENDATION STAY WITHHELD. You may establish and report ONLY its existence, its date/time, the instrument used, and its procedural function. DO NOT quote, paraphrase, summarise, characterise or allude to any score, any risk factor, any subscale, or any recommendation. If your finding needs one to make sense, the finding does not go in the file.
4. Other held primaries for the chronology: "${ART}/2025-09-16_affidavit-of-probable-cause_dc27880530.txt"; "${ART}/2025-09-16_information-charging-document_dc27880532.txt"; "${ART}/2026-08-16_rev_fbi-captures-kirk-shooter.txt" (the 2025-09-12 arrest-announcement press conference, Gov. Cox and FBI Director Patel); "${ART}/2025-09-24_order-transport-in-person-waiver-hearing_dkt24_dc27880870.txt"; the XChange docket exports (coverage ends 2026-03-14 — a hard ceiling); and day1–day5 in "${TX}".
5. Held primaries bearing on Erika Kirk: "${ART}/2025-09-16_request-designation-victim-representative_dkt12_dc27880865.txt" — READ BY THE COORDINATOR: filed 2025-09-16 by Jeffrey A. Neiman (Neiman Mays Floch & Almeida PLLC, Miami) and Brennan Moss (Utah Bar #10267, Parkinson Benson Potter, Park City) "Attorneys for the Victim", requesting that Erika Kirk, "the widow of Charles James Kirk", be designated the representative of the deceased victim under Utah Code Ann. 77-38-9(2) to exercise rights under Chapters 77-37 and 77-38. ALSO: "${ART}/2025-12-04_utah-office-victims-crime-restitution-notice-claim-1113665_dkt211_dc27880874.txt" (a restitution notice, ~1.3 KB, NEVER OPENED BY ANY PASS) and "${ART}/2026-07-08_supplemental-notice-access-to-evidence_dc28443912.txt" (the Victim's Family's demand that admitted exhibits be published to the courtroom).
6. Evidence files that already carry relevant findings: "${ROOT}/files - Court record/CR-E14_continuance-motion-and-the-discovery-record.md" (the F-84 chain, into which the 2026-01-16 Invocation of Speedy Trial Rights was deployed as scheduling pressure); CR-E10 and CR-E12 (publicity, closure and classification); CR-E16 (the participant roster, which resolves counsel identities); CR-ACQ-2026-08-14B (the 2026-07-08 supplemental notice, banked and read).
`

const FIND = {
  type: 'object',
  required: ['findings', 'scope_checked', 'dropped'],
  properties: {
    scope_checked: { type: 'string', description: 'exactly what you opened and what you did not' },
    dropped: { type: 'string', description: 'what you found but did not return under the cap; "none" if nothing' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['label', 'file_says', 'record_says', 'locator', 'kind', 'direction', 'apply_ready', 'confidence'],
        properties: {
          label: { type: 'string' },
          file_says: { type: 'string', description: 'verbatim from the target file, or "ABSENT — the file never says this"' },
          record_says: { type: 'string', description: 'verbatim from the source, kept minimal' },
          locator: { type: 'string', description: 'file + page/offset so another reader can go straight to it' },
          kind: { type: 'string', enum: ['contradiction', 'tier upgrade', 'omission', 'stale null', 'overclaim', 'confirmation', 'living-persons', 'metadata defect'] },
          direction: { type: 'string', description: 'does this claim MORE or LESS about any living person than the file currently does?' },
          apply_ready: { type: 'string', description: 'the exact prose to put in the file, or the exact edit to make' },
          confidence: { type: 'string', enum: ['High', 'Medium-high', 'Medium', 'Low'] },
        },
      },
    },
  },
}

const REMOVALS = {
  type: 'object',
  required: ['candidates', 'kept_deliberately'],
  properties: {
    kept_deliberately: { type: 'string', description: 'passages you considered and decided DO bear on a public question, with the question NAMED. You MUST fill this.' },
    candidates: {
      type: 'array',
      items: {
        type: 'object',
        required: ['section', 'what_it_is', 'who_it_concerns', 'public_question', 'recommendation'],
        properties: {
          section: { type: 'string' },
          what_it_is: { type: 'string', description: 'describe the CATEGORY of material without reproducing identifying detail — a removal note must not restate what it removed' },
          who_it_concerns: { type: 'string' },
          public_question: { type: 'string', description: 'the public question it bears on, or "NONE"' },
          recommendation: { type: 'string', enum: ['remove entirely', 'trim to role and relevance', 'keep'] },
        },
      },
    },
  },
}

const VERDICT = {
  type: 'object',
  required: ['refuted', 'reason', 'corrected_form', 'what_i_opened'],
  properties: {
    refuted: { type: 'boolean' },
    reason: { type: 'string' },
    corrected_form: { type: 'string' },
    what_i_opened: { type: 'string' },
  },
}

// ───────────────────────── TRACK A · Q-137 ─────────────────────────
phase('Find137')

const A_LENSES = [
  {
    key: 'custody-chain',
    prompt: `Establish the 2025-09-11/12 custody chain AT TIER 1 from the held primaries, and grade the SOURCING of each timestamp rather than just collecting the numbers.

The library has an unbanked extraction claiming: **booking 07:58:15 → PSA 08:21:35 → hold-without-bail 08:40:00**, one shared probable-cause ID, and **3 offences at booking versus 7 counts charged**. 🚨 TEST EVERY LINK. Where does each figure actually come from, and is that source readable?

Specifically: (a) the bail order's 08:40:00 and its Probable Cause ID — confirm on the face; (b) the PSA's timestamp — ⚠️ TIMESTAMP AND PROCEDURAL FUNCTION ONLY, the PII gate is absolute; (c) the booking time — ⚠️ THE TEXT LAYER IS GARBLE, so RENDER THE PDF before asserting anything, and if the render fails say the figure is unsourced rather than repeating it; (d) whether the probable-cause ID is genuinely SHARED across documents, which would tie them into one procedural act; (e) the 3-vs-7 charge comparison — name the three, name the seven, and say what the difference means procedurally *(a booking charge sheet and a charging Information are different instruments; a difference is not a discrepancy)*.

Then compare all of it against "${CHRON}" and say precisely which of its timeline entries are now T1, which stay T1-via-T3, and which are CONTRADICTED.`,
  },
  {
    key: 'filename-dates',
    prompt: `🚨 A FILENAME IS A CLAIM SOMEONE TYPED, AND ONE IS ALREADY KNOWN WRONG. "${ART}/2025-09-16_bail-order_dkt4_dc27880869.txt" is dated **September 12, 2025** on its face.

Your job is to find out how far this goes. **Sweep the banked artifacts in "${ART}" for filename-date-versus-document-face mismatches.** For each .txt whose name asserts a date, open it and check the date on the document's face (the signature block, the certificate of service, the file-stamp, the "Dated:" line). Report every mismatch, and report the RATE — how many you checked and how many diverged.

⚠️ Distinguish carefully between the kinds of date a document can carry: the date it was SIGNED, the date it was E-FILED, the date it was ENTERED, and the date it was UPLOADED to DocumentCloud. A filename derived from an upload date is not "wrong" in the same way as one derived from nothing. Say which kind each mismatch is.

Then: does anything in the library CITE these documents by their filename dates? If a wrong date has propagated into an evidence file, that is the finding that matters.`,
  },
  {
    key: 'officials-and-surrender',
    prompt: `Read the 2025-09-12 arrest-announcement press conference at "${ART}/2026-08-16_rev_fbi-captures-kirk-shooter.txt" IN FULL, and the probable-cause affidavit.

Establish what officials said ON THE RECORD about the surrender and the arrest: who said what, when, in what capacity, and how it compares to "${CHRON}"'s account. ⚠️ Speakers from CONTENT, never Rev labels.

Pay particular attention to: the sequence and timing of the surrender; the role of the intermediary the file calls a "family friend"; the role of the father; how the tip reached investigators; and any official characterisation of Robinson's conduct. 🚨 Every one of those touches either a presumed-innocent capital defendant or a private individual. Separate what officials ASSERTED from what has been ESTABLISHED, and flag anything the chronology states in its own analyst voice that is really an official's assertion.

Log CONFIRMATIONS explicitly where the chronology is right — this file has never been checked against the primary record at all.`,
  },
  {
    key: 'living-persons-137',
    prompt: `Apply the living-persons rule to "${CHRON}" IN FULL, and to its companion roadmap "${CHRON_RM}".

The file's §3 is about "the intermediary (family friend)" and its §4 is "the father's role: claim vs. record". **Both concern private individuals who are accused of nothing and who are in this story only because of their proximity to someone else's alleged crime.** Ask, passage by passage: does this bear on a public question, or is it here because a source published it?

🚨 THE PII GATE IS ABSOLUTE AND SEPARATE: the public safety assessment's scores, factors and recommendation stay WITHHELD by owner decision. Check whether the file — or its roadmap — currently carries, seeks, or would be improved by any of that material, and if the ROADMAP targets it, say so, because an acquisition target for withheld material is itself a defect.

Also check: does the file name or identify any family member beyond what the public questions require? Does it carry any address, workplace, or contact detail? Does it reproduce the defendant's family's private communications beyond what the charging documents put in the public record?

You MUST fill kept_deliberately — an audit that only ever removes is itself a bias signal.`,
  },
  {
    key: 'completeness-137',
    prompt: `COMPLETENESS PASS on "${CHRON}". Your question is NOT "is the file right" — it is **"WHAT IS IN THE HELD PRIMARY RECORD THAT THIS FILE NEVER MENTIONS AT ALL?"** A claim-by-claim reconciliation cannot find what a file never said; that is your entire job.

Read the file, then sweep: the probable-cause affidavit, the Information, the bail order, the transport/waiver order dkt24, the XChange docket exports (⚠️ read in Python — grep fails silently on them), the arrest-announcement transcript, and day1–day5 for any arrest/surrender/custody testimony.

Name every procedural event, document, actor, date or fact in those sources that the chronology does not carry. Also identify: any place where the file's SILENCE is itself a finding; any claim in the file that rests on a source this library will never obtain; and 🚨 any point where the file states as fact something that is an ALLEGATION against a presumed-innocent defendant.`,
  },
]

const a_found = await parallel(A_LENSES.map(l => () =>
  agent(`${RULES}\n${RECON}\n\nTASK — Q-137, THE ROBINSON ARREST CHRONOLOGY. Target file: "${CHRON}" (last touched 2026-07-26, before this library's entire court-record acquisition programme).\n\nLENS "${l.key}".\n\n${l.prompt}\n\nCAP: return your FIVE most consequential findings, ranked. Everything else in "dropped", one line each — a silent cap reads as full coverage.`,
    { label: `q137:${l.key}`, phase: 'Find137', schema: l.key === 'living-persons-137' ? REMOVALS : FIND })
))

// ───────────────────────── TRACK B · Q-138 ─────────────────────────
phase('Find138')

const B_LENSES = [
  {
    key: 'court-record-spine',
    prompt: `The dossier "${ERIKA}" predates the court record that now exists about her ROLE IN THIS PROCEEDING. Establish that spine at Tier 1 and say what the dossier does not know.

Read directly: dkt12 (the 2025-09-16 Request for Designation of Victim Representative); the 2026-07-08 supplemental notice; the restitution notice at dkt211 (⚠️ NEVER OPENED BY ANY PASS — open it); the XChange docket exports for every victim-related entry; and "${ROOT}/files - Court record/CR-E14_continuance-motion-and-the-discovery-record.md" for the F-84 chain and the 2026-01-16 Invocation of Speedy Trial Rights.

Establish: when victim's counsel first appeared (the library previously believed this was ten months later than it was); when the designation was GRANTED and by what means; what rights the designation carries under Utah Code Chapters 77-37 and 77-38; what the Invocation of Speedy Trial Rights actually said and how the State deployed it; and what the 2026-07-08 notice sought.

🚨 LAYER DISCIPLINE: a filing made BY counsel FOR the victim is Tier 1 for what was filed, never Tier 1 for the truth of what it asserts. And a procedural right exercised is not a claim about character.`,
  },
  {
    key: 'family-roster',
    prompt: `🚨 THIS IS THE MOST CONSEQUENTIAL LENS IN THE TASK. Read "${ERIKA}" Part II in full — a roster of named family members: mother, father, stepfather, sister, paternal grandfather, maternal grandparents, a paternal aunt with a birth year, the aunt's late husband with birth and death years, and a person captioned "cousin".

**Apply the living-persons rule to every one of them, and make the distinction that governs this file:**
- (a) family members who are THE SUBJECT OF A PUBLIC CLAIM this dossier exists to test — e.g. anyone named in the "Rothstein connection" allegation or in the "parents' intelligence/defense framing" claim. **These are load-bearing: the claim cannot be tested without them, and removing them would disable the dossier's own purpose.**
- (b) family members swept in by GENEALOGICAL COMPLETENESS — present because a genealogy aggregator lists them, bearing on no claim anyone has made. **These are private individuals with no connection to any public question, and birth years, maiden names and genealogy-site provenance are identifying information.**

For each person: name the public question or write NONE. 🚨 Note that genealogy-aggregator sourcing is TIER 4 and this dossier appears to carry T4 identifying detail about uninvolved private people — the exact combination the project rule forbids.

⚠️ WRITE YOUR REMOVAL NOTES WITHOUT RESTATING WHAT THEY REMOVE. Name the CATEGORY (e.g. "a birth year", "a maiden name") — never the value. You MUST fill kept_deliberately.`,
  },
  {
    key: 'claims-register',
    prompt: `Read "${ERIKA}" Part IV — the contested biographical claims register, nine claims — and Part V, the Source Discrepancy Register.

For each claim establish: (a) is the CLAIM still accurately stated, in the claimant's own terms? (b) is the dossier's ASSESSMENT of it still correct, and does its confidence grade trace to a verification act by THIS project rather than to repetition? (c) has anything changed since the file was last touched on 2026-07-26 — this is a CURRENCY re-check, and a dated null is a claim about the world on a date.

🚨 SEPARATE ANCHORS FROM CONNECTIONS, which is this project's core mechanic: a claimant's checkable facts (dates, venues, names) verifying as TRUE does not verify the CONNECTIONS asserted between them. Grade the anchor and the connection independently for every claim, and say where the dossier has run them together.

⚠️ Several claims concern a bereaved woman's biography — a birthdate, a birthplace, a degree, dating history, athletic history. Ask for EACH one whether testing it serves a public question at all, or whether the dossier is auditing a private life because a commentator made it a topic. **Recording that a claim was MADE is different from litigating whether it is true.** Where the second serves nothing, say so.

Use web search where a currency check needs it; record a retrieval date for everything and log every failed retrieval as an access-path caveat rather than dropping it.`,
  },
  {
    key: 'scope-and-purpose',
    prompt: `Read "${ERIKA}" IN FULL, including its Bottom-line synthesis and its Open questions.

The Q-138 specification says: **"She is a public figure in this proceeding AND a bereaved private person. The dossier exists because CLAIMS ABOUT HER became a subject — that scope must be preserved, not widened."**

Audit the file against exactly that. Where has it widened? Where does it investigate HER rather than the claims about her? Does its Part I "verified core biography" serve the claims register, or has it become an independent biographical project? Does the "Rothstein connection" section (Part III) test a claim, or does it build one?

🚨 Also apply the guard test this library learned the hard way: **strip the disclaimers from any passage and read what remains. If what remains is an argument, the disclaimers are decoration.** Run that test on the file's most heavily hedged passages and report what you find.

Finally: is the dossier's stated PURPOSE still accurate, and does its header tell a reader what it is for and what it must not be used for?`,
  },
  {
    key: 'completeness-138',
    prompt: `COMPLETENESS PASS on "${ERIKA}". Your question is **"WHAT IS MISSING?"** — not "what is wrong".

(a) What does the held court record say about Erika Kirk's role that the dossier never mentions? Sweep the artifacts folder and day1–day5 with patterns capable of matching (her name, "victim representative", "widow", "the Victim", victim's counsel's name).
(b) What claims has the claimant made that the register does not carry at all? Check the Bride of Charlie series files in "${ROOT}/files - Bride of Charlie series/" for claims about her that are recorded there and not here — 🚨 and check whether the two folders CONTRADICT each other or duplicate register numbers.
(c) Where is the dossier's SILENCE itself a finding?
(d) Does the dossier carry a revision log, a File ID, retrieval dates, confidence grades, outlet-orientation notes and "— (checkable)" markers? Report what is missing as a conventions defect.
(e) 🚨 What would a real Tier 1 acquisition programme for this file consist of — and is any of it improper to seek? An acquisition target for private material about an uninvolved person is itself a defect.`,
  },
]

const b_found = await parallel(B_LENSES.map(l => () =>
  agent(`${RULES}\n${RECON}\n\nTASK — Q-138, THE ERIKA KIRK DOSSIER. Target file: "${ERIKA}" (last touched 2026-07-26, before this library's entire court-record acquisition programme).\n\n🚨 THE SUBJECT. Erika Kirk is the widow of the deceased victim and the designated victim representative in this proceeding. She is simultaneously A PUBLIC FIGURE IN THIS LITIGATION and A BEREAVED PRIVATE PERSON. This dossier exists because CLAIMS ABOUT HER — principally Candace Owens' — became a subject this library investigates. That scope must be PRESERVED, NOT WIDENED. Nothing here is an allegation against her, and she is accused of nothing by anyone official.\n\nLENS "${l.key}".\n\n${l.prompt}\n\nCAP: return your FIVE most consequential findings, ranked. Everything else in "dropped", one line each.`,
    { label: `q138:${l.key}`, phase: 'Find138', schema: l.key === 'family-roster' ? REMOVALS : FIND })
))

// ───────────────────────── VERIFY ─────────────────────────
phase('Verify')

const pool = [...a_found, ...b_found].filter(Boolean).flatMap((r, i) =>
  (r.findings || []).slice(0, 3).map((f, j) => ({ ...f, id: `f${i}-${j}`, track: i < A_LENSES.length ? 'Q-137' : 'Q-138' }))
)
log(`${pool.length} findings to verify adversarially, two lenses each`)

const LENSES = [
  { key: 'source', ask: 'Go to the cited source and READ AROUND the quote. Does it say this, in this sense, said by whom the finding claims, in what capacity? Rev labels are not evidence. A questioner\'s premise is not an answer; a filing\'s assertion is not a finding; a judge\'s recital of an allegation is not an adjudication. If the finding rests on a null, re-run it with a pattern CAPABLE of matching and say which. If the finding targets text that is not in the file, it is REFUTED — check the file first.' },
  { key: 'stakes', ask: 'Ask whether the finding claims MORE about any living person — the defendant, a family member, the victim\'s widow, an uninvolved third party — than the source carries. Ask whether adopting it would WIDEN the file\'s scope beyond the public questions it exists to answer. Ask whether it would put identifying detail about an uninvolved private individual into the file. If any of those, refute it or give the narrower supported form. Also verify the file really does omit or misstate what the finding says it does.' },
]

const verified = await pipeline(
  pool,
  f => parallel(LENSES.map(v => () =>
    agent(`${RULES}\n${RECON}\n\nTASK — ADVERSARIALLY REFUTE this finding. YOUR DEFAULT IS REFUTED; let it survive only if it holds against the primary source.\n\nTRACK: ${f.track}\nFINDING: ${f.label}\nKind: ${f.kind}\nFile says: ${f.file_says}\nRecord says: ${f.record_says}\nLocator: ${f.locator}\nProposed edit: ${f.apply_ready}\n\nYOUR LENS — ${v.key}: ${v.ask}\n\nIf it survives but is OVERSTATED, set refuted=false and put the narrower supported form in corrected_form. Fill what_i_opened with the files you actually read.`,
      { label: `verify:${f.id}:${v.key}`, phase: 'Verify', schema: VERDICT })
  )).then(vs => ({ finding: f, verdicts: vs.filter(Boolean) }))
)

const survived = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.every(x => !x.refuted))
const split = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.some(x => x.refuted) && v.verdicts.some(x => !x.refuted))
const killed = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.every(x => x.refuted))
log(`${survived.length} survived · ${split.length} split · ${killed.length} refuted`)

const by = t => survived.filter(s => s.finding.track === t).map(s => ({ ...s.finding, verdicts: s.verdicts }))

// ───────────────────────── PLAN ─────────────────────────
phase('Plan')

const livingA = a_found.filter(Boolean).filter(r => r.candidates)
const livingB = b_found.filter(Boolean).filter(r => r.candidates)

const [plan137, plan138, critic] = await parallel([
  () => agent(`${RULES}\n${RECON}\n\nTASK — PRODUCE ONE ORDERED APPLY PLAN for "${CHRON}", v1.0 → v1.1.\n\nSurviving findings (Q-137):\n${JSON.stringify(by('Q-137'), null, 2)}\n\nLiving-persons candidates:\n${JSON.stringify(livingA.flatMap(r => r.candidates || []), null, 2)}\nDeliberately kept:\n${JSON.stringify(livingA.map(r => r.kept_deliberately), null, 2)}\n\nSplit verdicts (NOT findings — record, do not adopt):\n${JSON.stringify(split.filter(s => s.finding.track === 'Q-137').map(s => ({ label: s.finding.label, reasons: s.verdicts.map(v => v.reason) })), null, 2)}\n\nFor each edit: target section, exact current text (or "insert after X"), exact replacement, the Q-number it discharges, and one line naming the primary source. Group by file position so edits apply top-to-bottom without collisions.\n\n🚨 REQUIREMENTS:\n- Separate SAFE TO APPLY from NEEDS AN OWNER DECISION, and say which is which.\n- Flag PAIRED edits that must move together.\n- 🚨 Flag every edit that would put MORE about a living person into the file, and justify it by naming the public question, or drop it. The defendant's presumption of innocence is load-bearing here.\n- ⚠️ CONFIRM that no edit reproduces any PSA score, factor or recommendation. State that you checked.\n- Where findings CONFLICT, say so; do not resolve silently.\n- Write the revision-log row: what changed and WHY. It must not merely restate what was removed.\n- Name explicitly what this pass did NOT re-verify.`,
    { label: 'plan:q137', phase: 'Plan' }),

  () => agent(`${RULES}\n${RECON}\n\nTASK — PRODUCE ONE ORDERED APPLY PLAN for "${ERIKA}", v1.0 → v1.1.\n\n🚨 GOVERNING CONSTRAINT: the dossier exists because CLAIMS ABOUT HER became a subject. Preserve that scope; do not widen it. She is a bereaved private person as well as a participant in this proceeding.\n\nSurviving findings (Q-138):\n${JSON.stringify(by('Q-138'), null, 2)}\n\nFamily-roster living-persons candidates:\n${JSON.stringify(livingB.flatMap(r => r.candidates || []), null, 2)}\nDeliberately kept:\n${JSON.stringify(livingB.map(r => r.kept_deliberately), null, 2)}\n\nSplit verdicts (NOT findings):\n${JSON.stringify(split.filter(s => s.finding.track === 'Q-138').map(s => ({ label: s.finding.label, reasons: s.verdicts.map(v => v.reason) })), null, 2)}\n\nSame output requirements as the other plan, plus:\n- 🚨 Handle the FAMILY ROSTER first and separately. For each person: remove, trim to role and relevance, or keep — with the public question named. **Write every removal note WITHOUT restating what it removes: name the category, never the value.**\n- Distinguish sharply between (a) material serving no public question, (b) material load-bearing BECAUSE a claimant made it an issue, and (c) the court-record facts about her role, which must stay.\n- ⚠️ Say plainly whether the dossier should continue to exist in its current form, or whether its scope needs re-stating in its header.`,
    { label: 'plan:q138', phase: 'Plan' }),

  () => agent(`${RULES}\n${RECON}\n\nTASK — COMPLETENESS CRITIC ACROSS BOTH FILES. You are last.\n\nQ-137 scope statements:\n${JSON.stringify(a_found.filter(Boolean).map(r => ({ scope: r.scope_checked, dropped: r.dropped })), null, 2)}\n\nQ-138 scope statements:\n${JSON.stringify(b_found.filter(Boolean).map(r => ({ scope: r.scope_checked, dropped: r.dropped })), null, 2)}\n\nRefuted:\n${JSON.stringify(killed.map(s => ({ track: s.finding.track, label: s.finding.label, why: s.verdicts.map(v => v.reason.slice(0, 300)) })), null, 2)}\n\nName, and make each actionable enough to become a queue item:\n(a) any HELD source no reader in this pass opened — actually LIST "${ART}" and "${TX}" and check, rather than reasoning about it;\n(b) any section of either target file no lens touched;\n(c) any place where a file's SILENCE is itself a finding;\n(d) 🚨 the CROSS-FILE question: Q-135 opened four person files. Two are now done (Twiggs, Zinn) and these two are in hand. **What does the SET tell you that no individual file could — recurring defect classes, shared stale premises, contradictions BETWEEN the four person files, duplicated register numbering, or the same source being tiered differently in different files?**\n(e) whether either file should exist in its current form at all.`,
    { label: 'critic', phase: 'Plan' }),
])

return {
  q137: { findings: a_found.filter(Boolean), plan: plan137 },
  q138: { findings: b_found.filter(Boolean), plan: plan138 },
  verified: { survived: survived.length, split: split.length, refuted: killed.length },
  survived: survived.map(s => ({ track: s.finding.track, ...s.finding, verdicts: s.verdicts })),
  split: split.map(s => ({ track: s.finding.track, label: s.finding.label, verdicts: s.verdicts })),
  refuted: killed.map(s => ({ track: s.finding.track, label: s.finding.label, reasons: s.verdicts.map(v => v.reason) })),
  critic,
}
