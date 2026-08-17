export const meta = {
  name: 'security-posture-2025-09-10',
  description: 'Build the Tier 1 record of the security posture at the 2025-09-10 UVU event: who was responsible, who was present, where they stood, what they did, and what the record does NOT establish',
  phases: [
    { title: 'Find', detail: 'six lenses over the sworn record, the filings and the official statements' },
    { title: 'Verify', detail: 'adversarial refutation, two lenses per finding' },
    { title: 'Write', detail: 'evidence file draft + completeness critic' },
  ],
}

const ROOT = '~/Documents/Kirk Robinson Research'
const ART = `${ROOT}/files - Court record/CR-ACQ-2026-07-27_court-record-artifacts`
const TX = `${ART}/prelim-hearing-transcripts`

const RULES = `
YOU ARE WORKING INSIDE A LEGAL-RESEARCH LIBRARY WITH STRICT STANDING RULES. Obey them.
PATHS CONTAIN SPACES — quote them in shell commands. Repo root: "${ROOT}"

🚨 CASE POSTURE, verified 2026-08-17. TYLER ROBINSON HAS NOT BEEN BOUND OVER. The preliminary hearing is UNFINISHED: 2026-07-06 → 07-10 were five days OF EVIDENCE; 2026-09-01 is its LAST DAY, ARGUMENT ONLY, on a closed evidentiary record. Never write that the hearing "concluded" on 07-10. Presumption of innocence is absolute.

🚨🚨 THE GOVERNING CONSTRAINT OF THIS ENTIRE TASK, AND IT COMES FROM THE COURT RECORD ITSELF, NOT FROM POLICY.
A sworn proffer filed 2026-02-02 by a Deputy Utah County Attorney (docket 368, held at "${ART}/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.txt") states at paragraph 6:
    "Members of Charlie Kirk's security team have reported threats, doxing – the publication of personal information online for harassment purposes, and risks to them since Charlie Kirk's murder."
and at paragraph 5 that witnesses "have received threats because of their involvement. Some have relocated to avoid these threats. Many have deleted online accounts and changed usernames and social media handles."

THEREFORE, AND THIS IS NOT NEGOTIABLE:
- The subject of this file is THE SECURITY POSTURE AND THE PROFESSIONAL CONDUCT OF PERSONNEL ACTING IN A PUBLIC CAPACITY ON 2025-09-10. That is a legitimate public question: it bears on how the shooter reached the roof, on the State's charged grave-risk-of-death aggravator, and on the defence's answer to it.
- THE PERSONAL BACKGROUNDS OF INDIVIDUAL PRIVATE SECURITY PERSONNEL ARE NOT THE SUBJECT AND MUST NOT BE COMPILED. No employment histories, no residences, no family, no social media, no photographs, no physical descriptions, no vehicle or licensing details, no prior careers — for any individual member of Mr. Kirk's private security team.
- DO NOT NAME any individual member of Mr. Kirk's private security team, even if a source names them. The project rule is explicit: no identifying information about uninvolved private parties EVEN WHEN SOURCES PUBLISH IT — and here the record establishes that publication of exactly this material is an ongoing, reported harm. Refer to them by ROLE ("a member of Mr. Kirk's security team", "the individual on the Hall of Flags").
- NAMED PUBLIC OFFICIALS ACTING IN THEIR PUBLIC ROLES ARE A DIFFERENT CATEGORY and may be named: sworn police witnesses, agency chiefs speaking at press conferences, counsel of record, the judge. Say which category each person falls into and why.
- None of these people is accused of anything by anyone. Nothing in this file may imply otherwise, and any framing that reads as insinuation about a security team member's conduct must be refused and flagged.

THE TWO LAYERS, NEVER BLENDED. (1) Recording layer — what a claimant actually said, cited, even when false. (2) Analyst layer — what the established record shows, with tier and confidence. Asserting analyst-layer fact without independent verification is this project's cardinal error.

SOURCE TIERS. T1 = sworn testimony and primary court filings. T2 = named official statements. T3 = named journalism. T4 = anonymous / low-verification. Mark "T1 via T3" when primary-document content is known only through reporting. A grade must trace to an ACTUAL VERIFICATION ACT BY THIS PROJECT.

SEARCH HAZARDS, all measured here:
- Artifacts in "${ART}" carry U+FFFE where a hyphen + line break belonged. Use "${ROOT}/artifact_search.py" (find(pattern, path)) which tests BOTH readings, and SAY you checked both.
- Some artifacts contain NUL bytes and are "data" to file(1); grep returns NOTHING on a file with matches. Read in Python with errors='replace'.
- CORPUS CONTAMINATION, EXCLUDE PER TERM AND SAY WHICH: "${ART}/2026-07-06_gov-uscourts-utd-165286-1-4-1_dc28417731.txt" is a mis-banked unrelated case. Measured false hits: 9 "roommate", 6 "partner", 5 "cop car". But "Robinson" returns 4 TRUE hits in it, so a blanket exclusion destroys true hits.
- A NULL BATTERY CANNOT TEST WHAT ITS PATTERNS CANNOT REACH. When claiming absence, at least one pattern must be CAPABLE of matching the thing claimed absent — say which. Search STEMS, and numerals AND words for any number.
- 🚨 REV SPEAKER LABELS ARE NOT EVIDENCE, AND THIS TASK HITS THE WORST INSTANCE. In "day1.txt" OFFICER BAGLEY'S ANSWERS CARRY THE LABEL "Richard Novak", a defence attorney's name. Bagley holds the stand from roughly line 628 to line 6299. Infer every speaker from CONTENT; where label and content disagree, CONTENT WINS. Never resolve a label to a real person without a stated basis.
- Rev timestamps are stream offsets, ±5 min as clock times, never converted to a time of day without that mark.
- A FILENAME IS A CLAIM SOMEONE TYPED. Read the document's face for its date and parties.

VERIFY IN BOTH DIRECTIONS. Look for evidence that the security arrangement was adequate as hard as for evidence it was not, and LOG CONFIRMATIONS EXPLICITLY. An audit trail that only runs one way is a bias signal. 🚨 THIS MATTERS ESPECIALLY HERE: a file about security failures at an assassination is the natural home of insinuation, and the record's own answer — that Utah is an open-carry state, that the event was outdoors on a public campus, that the responsibility was split across at least three bodies — must be given its full weight.
`

const HELD = `
WHAT THE COORDINATOR HAS ALREADY ESTABLISHED BY DIRECT READING, 2026-08-17. Build on it; test it if your lens bears on it.

✅ A MEASURED NULL, METHOD VALIDATED: the surname "Cutler" returns ZERO hits across all 71 sweepable banked artifacts (72 minus the mis-banked contaminant) AND zero across every .md file in the repository, under both U+FFFE readings. Positive controls in the same run: "Bagley" 37 hits / 3 files, "Faumuina" 804 hits / 9 files — so the method demonstrably finds surnames in this corpus. THE NULL IS REAL AND IS A FACT ABOUT THIS LIBRARY'S HOLDINGS.

WHAT IS HELD ON THE SECURITY POSTURE:
1. TIER 1, day1.txt ~02:46:30–02:47:29 — Officer Bagley on cross by Ms. Nestor (⚠️ his answers are LABELLED "Richard Novak"): Utah "is an open carry state"; he saw nobody armed "other than law enforcement"; asked whether Mr. Kirk "had his own security team present there with him" — "Yes"; asked whether he communicated with any of them — "I saw one of the individuals that was on top of the Hall of Flags right next to me, yes"; asked whether that person was armed — "I was aware he was armed"; asked whether any agency besides "Mr. Kirk's private security team and your six officers" covered the event — "I don't know."
2. TIER 1, day1.txt ~05:58:03 — Agent David Hull on direct by Mr. McBride: "Mr. Kirk's detail, his own security team removed him from the scene whilst administering first aid and they conducted what would be called a hasty transport to Timpanogos Hospital," and this is portrayed in State's Exhibit 9.
3. TIER 1, day2.txt ~00:57:54 — Hull: a vehicle "made contact with an officer who was doing security detail" — Officer Goforth, Spanish Fork Police. ⚠️ THIS IS A SWORN POLICE OFFICER ON A SECURITY DETAIL, NOT A MEMBER OF MR. KIRK'S PRIVATE TEAM. Do not merge the two categories anywhere in this task.
4. TIER 1, day2.txt ~01:58:06 — Ms. Nestor to Hull: the Ty Phillips video "showed a dead-on view of Mr. Kirk and his parts of his security team."
5. TIER 1, the defence's 2026-08-11 preliminary-hearing briefing: State's Exhibit 8 "depicts... what appear to be two security personnel in front and diagonal to Mr. Kirk, standing in the grass area by the barrier"; "One of Mr. Kirk's security guards comes into frame from the right of Mr. Kirk three seconds after the shot." The brief also attacks the State's grave-risk theory as resting on speculation "That the shooter actually observed security personnel standing an unknown distance from Mr. Kirk."
6. TIER 2, the same-day 2025-09-10 press conference: a speaker identified from content as Jeff Long — "we did have officers there. We had Charlie Kirk's team. He has a security team that travels with him and they were here with him when he was shot."
7. TIER 1, CR-E08 records the State's grave-risk factual theory in its own words: "Mr. Kirk's team members were very close to him..." — read CR-E08 for the full formulation.
8. ALREADY IN THE LIBRARY: "${ROOT}/files - Court record/CR-E05_prelim-hearing-Day1_Bagley-Hull-first-tranche.md" carries Bagley's account — the overtime shift, check-in about 11:00 a.m., the Hall of Flags overlook, and "no briefing, no debrief, no meeting that morning; no operational or tactical plan, no written materials." VERIFY these against day1.txt rather than inheriting them. Also relevant: CR-E04 (UVU surveillance), CR-E07 (the defence briefing), and "${ROOT}/files - Kirk assassination questions/kirk-shooting-official-timeline.md" ("Six officers were working an event with roughly 3,000 attendees", T3).
`

const FIND = {
  type: 'object',
  required: ['findings', 'scope_checked', 'dropped'],
  properties: {
    scope_checked: { type: 'string', description: 'exactly what you opened, and what you did not' },
    dropped: { type: 'string', description: 'what you found but did not return under the cap; "none" if nothing' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['label', 'what_the_record_says', 'locator', 'tier', 'confidence', 'category', 'limits'],
        properties: {
          label: { type: 'string' },
          what_the_record_says: { type: 'string', description: 'verbatim where it matters, minimal quotation' },
          locator: { type: 'string', description: 'file + timestamp/offset so another reader goes straight to it' },
          tier: { type: 'string', enum: ['T1', 'T2', 'T3', 'T4', 'T1 via T3', 'analyst inference'] },
          confidence: { type: 'string', enum: ['High', 'Medium-high', 'Medium', 'Low', 'unverified'] },
          category: { type: 'string', enum: ['public official / sworn witness', 'private security personnel (role only)', 'institutional / UVU / agency', 'physical or geographic', 'litigated issue', 'null or absence'] },
          limits: { type: 'string', description: 'what this does NOT establish; the steelman; what would change it' },
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

phase('Find')

const LENSES = [
  {
    key: 'bagley-posture',
    prompt: `Read Officer Bagley's testimony in "${TX}/day1.txt" IN FULL — he holds the stand from roughly line 628 to line 6299. ⚠️ HIS ANSWERS ARE LABELLED "Richard Novak". Infer from content.

Establish, at Tier 1, EVERYTHING the sworn record carries about the LAW-ENFORCEMENT security posture at the event: how many officers, from what agency, under what assignment or shift arrangement, posted where, briefed how (or not), with what equipment, with what plan, and with what communications. Quote minimally and give a timestamp for each.

Then establish precisely what he says about MR. KIRK'S PRIVATE SECURITY TEAM — presence, arming, position, and any communication with them. 🚨 Report the individual on the Hall of Flags BY ROLE ONLY; do not name him even if the transcript does, and say whether the transcript names him.

⚠️ VERIFY IN BOTH DIRECTIONS. The library's CR-E05 says "no briefing, no debrief, no meeting that morning; no operational or tactical plan, no written materials." Test that against the transcript — is it his evidence, is it counsel's characterisation he assented to, and is it scoped to HIM or to the whole detail? A witness's account of his own briefing is not evidence about everyone else's. And log what the posture DID include.`,
  },
  {
    key: 'hull-and-response',
    prompt: `Read Agent David Hull's testimony across "${TX}/day1.txt" and "${TX}/day2.txt" for everything bearing on security at the event and on the response to the shot.

Establish: the detail's actions immediately after the shot (the "hasty transport"); what State's Exhibits 7, 8 and 9 show about positions and movement; Officer Goforth and the Spanish Fork Police security detail and how that vehicle contact fits the timeline; the Ty Phillips video and what it shows of "parts of his security team"; and any account of which bodies were responsible for what.

🚨 KEEP TWO CATEGORIES SEPARATE THROUGHOUT AND SAY SO: (a) SWORN POLICE OFFICERS on security details — public officials, nameable; (b) MR. KIRK'S PRIVATE SECURITY TEAM — private individuals, role only, never named. The record contains both and merging them would be a category error with living-persons consequences.

⚠️ Distinguish what Hull OBSERVED from what he was TOLD and from what he reconstructed from video. "My recollection is" is not the same tier as an eyewitness account.`,
  },
  {
    key: 'exhibits-and-the-litigated-issue',
    prompt: `Read "${ART}/2026-08-11_defendant-prelim-hearing-briefing.txt" and "${ROOT}/files - Court record/CR-E08_state-information-and-pc-affidavit-2025-09-16.md", plus day4/day5 for any exhibit testimony bearing on positions.

🚨 THE SECURITY TEAM'S POSITIONS ARE A LITIGATED ISSUE, NOT A BACKGROUND DETAIL, and that is the most important thing this lens must establish. The State's charged aggravating circumstance is that the defendant "knowingly created a great risk of death to another individual other than Charlie Kirk," and the State's factual theory rests on the proximity of Mr. Kirk's team members. The defence attacks it as speculation.

Establish precisely: what the State asserts about where security personnel were and what the shooter could see; what the defence answers; what the exhibits are said to depict, frame by frame where the brief does that; and what has actually been ESTABLISHED as against ARGUED.

⚠️ BOTH SIDES ARE RECORDING LAYER. A party's brief is Tier 1 for what was FILED, never Tier 1 for the truth of what it asserts. The State's own 2026-07-28 brief is NOT held by this library, so any account of the State's argument that comes through the defence's characterisation must be marked as such and never promoted.`,
  },
  {
    key: 'officials-and-responsibility',
    prompt: `Read all four official transcripts — "${ART}/2026-08-16_rev_press-conference-on-charlie-kirk-shooting.txt" (same-day 2025-09-10), ".../2026-08-16_rev_fbi-press-conference-on-kirk-shooting.txt" (09-11), ".../2026-08-16_rev_fbi-captures-kirk-shooter.txt" (09-12), ".../2026-08-16_rev_update-on-charlie-kirk-shooter.txt" (09-16 charging).

Establish what NAMED OFFICIALS said on the record about the security arrangement: who was responsible for securing the event, what the arrangement between UVU, local law enforcement and Mr. Kirk's private team was, what was said about the rooftop, and any official assessment of what went wrong. ⚠️ Speakers from CONTENT, never Rev labels — and identify each speaker's agency and role.

🚨 The same-day conference contains an official saying words to the effect of "You try to get your bases covered and unfortunately today we didn't." Establish exactly who said that, in what capacity, and what precisely he was conceding — an expression of regret at a press conference hours after a killing is NOT an admission of a security failure, and this file must not convert one into the other. Give the full surrounding context.

⚠️ Log confirmations: where officials described the arrangement as adequate or normal, record that with equal care.`,
  },
  {
    key: 'living-persons-and-naming',
    prompt: `🚨 THIS LENS GOVERNS WHAT THE FILE MAY CONTAIN. Read "${ART}/2026-02-02_proffer-facts-closure-poritons-evidentiary-hearing-motion-disqualify_dkt368_dc27881508.txt" IN FULL, and then sweep the whole corpus.

(a) Establish the full context and procedural function of the doxing proffer at ¶6 — who filed it, in support of what motion, what it says, and what the court did with it. ⚠️ It is a party's PROFFER, so it is Tier 1 for what the State represented, not an adjudicated finding — say so, while noting the court's own closure practice in CR-E10 and CR-E12.

(b) 🚨 SWEEP THE ENTIRE CORPUS AND THE ENTIRE REPOSITORY for any NAME attached to a member of Mr. Kirk's private security team. Report ONLY: whether any such name exists in the holdings, in how many places, and in what kind of document. 🚨 DO NOT REPRODUCE ANY SUCH NAME IN YOUR OUTPUT. Report the CATEGORY and the COUNT. If the answer is none, say so with your patterns stated.

(c) Test whether any EXISTING library file already carries identifying detail about private security personnel that should be reconsidered — check CR-E04, CR-E05, CR-E07, CR-E08, the Losee draft, and the Kirk-questions folder.

(d) Establish the threshold question that determines scope for any individual: is any member of Mr. Kirk's private security team a PUBLIC-FACING figure in this story — i.e. have they testified, been named in an official statement, or given public interviews about the event in their own name? A person who has publicly spoken about their own role is in a different category from one who has not. Answer from the HELD RECORD, and state what you could not determine.`,
  },
  {
    key: 'completeness-and-absence',
    prompt: `COMPLETENESS PASS. The question is NOT "what does the record say" — it is 🚨 "WHAT IS ABSENT, AND WHAT IS THE SCOPE OF EACH ABSENCE?"

Sweep every held artifact and all five transcripts for security-relevant material, then name what the record does NOT contain. Candidates to test, each with a CAPABLE pattern and both U+FFFE readings: any event security plan or operations order; any contract or agreement between the event organiser, the university and any private security provider; any advance threat assessment; any account of who decided the rooftops would not be covered; any testimony from any member of Mr. Kirk's private security team; any interview of one; any UVU policy on event security; any after-action review; any count of private security personnel present; any account of their communications or coordination with police.

For each absence: state WHERE you looked, and whether the search space would NECESSARILY contain the record if it existed. 🚨 An absence from a preliminary-hearing record is weak evidence of anything — a preliminary hearing tests probable cause for the CHARGED offences, and the adequacy of the victim's security arrangements is not an element of any of them. SAY THAT PLAINLY; it is the single most important calibration in this file.

Finally: name what a legitimate Tier 1 acquisition programme would consist of, and 🚨 flag any target that would be improper to seek because it is personal information about a private individual rather than institutional record.`,
  },
]

const found = await parallel(LENSES.map(l => () =>
  agent(`${RULES}\n${HELD}\n\nTASK — THE SECURITY POSTURE AT THE 2025-09-10 UVU EVENT. Lens "${l.key}".\n\n${l.prompt}\n\nCAP: return your SIX most consequential findings, ranked. Everything else in "dropped", one line each — a silent cap reads as full coverage.`,
    { label: `sec:${l.key}`, phase: 'Find', schema: FIND })
))

phase('Verify')

const pool = found.filter(Boolean).flatMap((r, i) =>
  (r.findings || []).slice(0, 3).map((f, j) => ({ ...f, id: `f${i}-${j}` }))
)
log(`${pool.length} findings to verify adversarially, two lenses each`)

const VLENSES = [
  { key: 'source', ask: 'Open the cited source and READ AROUND the passage. Does it say this, in this sense, said by whom the finding claims, in what capacity? Rev labels are not evidence — Bagley\'s answers carry a defence attorney\'s name. A questioner\'s premise is not an answer; counsel\'s characterisation assented to by a witness is not the witness\'s own measurement; a party\'s brief is not a finding. If the finding rests on a null, re-run it with a CAPABLE pattern and say which.' },
  { key: 'stakes', ask: 'Ask whether the finding (a) names or identifies a private security individual, or carries detail from which one could be identified — if so REFUTE it and give the role-only form; (b) implies fault, negligence or complicity by any security personnel, when the record establishes no such thing and no official has alleged it — if so refute or narrow it; (c) treats an ABSENCE from a preliminary-hearing record as evidence about the world, when a preliminary hearing tests probable cause for the charged offences and security adequacy is an element of none of them; (d) converts an expression of regret into an admission. Give the narrower supported form.' },
]

const verified = await pipeline(
  pool,
  f => parallel(VLENSES.map(v => () =>
    agent(`${RULES}\n${HELD}\n\nTASK — ADVERSARIALLY REFUTE this finding. YOUR DEFAULT IS REFUTED; let it survive only if it holds against the primary source.\n\nFINDING: ${f.label}\nRecord says: ${f.what_the_record_says}\nLocator: ${f.locator}\nTier claimed: ${f.tier} · Confidence claimed: ${f.confidence}\nStated limits: ${f.limits}\n\nYOUR LENS — ${v.key}: ${v.ask}\n\nIf it survives but is OVERSTATED, set refuted=false and put the narrower supported form in corrected_form. Fill what_i_opened with the files you actually read.`,
      { label: `verify:${f.id}:${v.key}`, phase: 'Verify', schema: VERDICT })
  )).then(vs => ({ finding: f, verdicts: vs.filter(Boolean) }))
)

const survived = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.every(x => !x.refuted))
const split = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.some(x => x.refuted) && v.verdicts.some(x => !x.refuted))
const killed = verified.filter(Boolean).filter(v => v.verdicts.length && v.verdicts.every(x => x.refuted))
log(`${survived.length} survived · ${split.length} split · ${killed.length} refuted`)

phase('Write')

const [draft, critic] = await parallel([
  () => agent(`${RULES}\n${HELD}\n\nTASK — WRITE THE EVIDENCE FILE, ready to save as "SEC-E01_security-posture-2025-09-10.md".

SURVIVING FINDINGS (only these may be asserted):
${JSON.stringify(survived.map(s => ({ ...s.finding, verdicts: s.verdicts.map(v => ({ reason: v.reason, corrected: v.corrected_form })) })), null, 2)}

SPLIT (NOT findings — record as unresolved, do not adopt):
${JSON.stringify(split.map(s => ({ label: s.finding.label, verdicts: s.verdicts.map(v => ({ refuted: v.refuted, reason: v.reason })) })), null, 2)}

REFUTED (record as refuted where instructive; never assert):
${JSON.stringify(killed.map(s => ({ label: s.finding.label, why: s.verdicts.map(v => v.reason.slice(0, 400)) })), null, 2)}

STRUCTURE:
- Header: File ID, scope, case context, Prepared date, Status/version, and 🚨 the case-posture stamp as of 2026-08-17.
- §0 the four-tier framework reproduced. §1 the access-path caveat FIRST, including the Rev label trap and which sources are uncertified machine transcripts.
- 🚨 §2 SCOPE AND THE NAMING RULE — state plainly what this file is about (professional conduct in a public capacity) and what it deliberately does NOT contain (personal backgrounds of private security personnel), WITH the dkt368 ¶6 proffer as the record-based reason, and the note that no security team member is accused of anything by anyone.
- §3 the law-enforcement posture. §4 Mr. Kirk's private security team, ROLE ONLY. §5 the response to the shot. §6 the litigated grave-risk issue, both sides, recording layer. §7 what officials said. §8 🚨 WHAT THE RECORD DOES NOT ESTABLISH — with each absence's scope stated, and the calibration that a preliminary hearing tests probable cause for the charged offences and that security adequacy is an element of none of them.
- §9 findings and open questions, each confidence-graded and tied to what would change it. §10 acquisition targets — institutional records only, with any improper target named and excluded. Revision log.

REQUIREMENTS: every claim carries a tier and a locator. Confidence grades trace to verification acts by this project. Quote minimally. NAME NO PRIVATE SECURITY INDIVIDUAL. Log confirmations as carefully as criticisms. State residual scope plainly.`,
    { label: 'draft', phase: 'Write' }),

  () => agent(`${RULES}\n${HELD}\n\nTASK — COMPLETENESS CRITIC. You are last.

Scope statements from the six lenses:
${JSON.stringify(found.filter(Boolean).map(r => ({ scope: r.scope_checked, dropped: r.dropped })), null, 2)}

Refuted findings:
${JSON.stringify(killed.map(s => ({ label: s.finding.label, why: s.verdicts.map(v => v.reason.slice(0, 300)) })), null, 2)}

Name, each actionable enough to become a queue item:
(a) any HELD source no lens opened — actually LIST "${ART}" and "${TX}" and check rather than reasoning about it;
(b) any security-relevant question no lens asked;
(c) 🚨 whether this file, as scoped, can honestly answer the question a reader will bring to it — "was the security adequate, and did anything about it go wrong?" — or whether the honest answer is that THE HELD RECORD CANNOT ANSWER IT and the file must say so in terms;
(d) any place where the pass risked insinuation about people accused of nothing, and whether the draft avoided it;
(e) what a Tier 1 acquisition programme would need, separating INSTITUTIONAL records (proper) from PERSONAL information about private individuals (improper, and to be named as excluded).`,
    { label: 'critic', phase: 'Write' }),
])

return {
  findings: found.filter(Boolean),
  tally: { survived: survived.length, split: split.length, refuted: killed.length },
  survived: survived.map(s => ({ ...s.finding, verdicts: s.verdicts })),
  split: split.map(s => ({ label: s.finding.label, verdicts: s.verdicts })),
  refuted: killed.map(s => ({ label: s.finding.label, reasons: s.verdicts.map(v => v.reason) })),
  draft,
  critic,
}
