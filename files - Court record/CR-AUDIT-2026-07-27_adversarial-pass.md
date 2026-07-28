# CR-AUDIT-2026-07-27 — Adversarial Verification Pass on the 2026-07-27 Court-Record Output

**File ID:** CR-AUDIT-2026-07-27
**Scope:** a deliberately skeptical re-read of everything this project produced from the court record on 2026-07-27 — **CR-ACQ v1.2**, **CR-E01 v1.1**, **CR-E02 v1.0** — checking each load-bearing claim against the banked primary artifacts. Commissioned because the pass had been "owed" all day and because one finding had already reversed once under scrutiny.
**Method:** default-skeptical. For each finding, the question asked was *"what would have to be true for this to be wrong, and does the artifact actually say it?"* — not *"can I find support for this?"* Register integrity, tiering, and scope statements checked by grep and by re-reading source passages in context.
**Prepared:** July 27, 2026
**Status:** v1.1 — **§2.2's D-50 finding has since dissolved.** The full reading of Faumuina (CR-E02 v1.2) shows 415 ft / 410 ft / 68 ft are the slope, horizontal and vertical legs of one consistent survey, not competing figures. The pass was right to refuse to pick one from a fragment; the underlying defect was the sampling, not the witness. §2.3's Dremel finding also **understated** the record — the tool was *identified*, not merely class-consistent.

**Headline result: the pass was worth running.** It found **four defects, two of them material** — including one that forced **D-48's third resolution in a single day**. The single most significant finding is that **CR-ACQ's headline `source identification` was over-weighted**: the identified cartridge case was recovered from inside the rifle's chamber, which makes the identification close to tautological as a link between the weapon and the shooting. Both of this file's parent resolutions of D-48 — the original *for* Owens and the correction *against* — were too simple.

---

## 1. WHAT WAS CHECKED

| Claim checked | Verdict |
|---|---|
| ATF `source identification` of the cartridge case (CR-ACQ §3.1) | **Accurate as to the report — but over-weighted in use.** See §2.1 |
| `Inconclusive` on fragment 6A rests on data insufficiency, not dissimilarity (CR-E01 §3.3) | **CONFIRMED.** Karner's own words; defense counsel conceded the distinction |
| Karner used pliers (CR-E01 §3.2) | **CONFIRMED** verbatim |
| Perch-to-tent distance "410 feet" (CR-E02 §2) | **DEFECT — the witness said 415.** See §2.2 |
| Three-way Dremel convergence (CR-E02 §5.4) | **CONFIRMED, and understated** — engraved ammunition was omitted. See §2.3 |
| Stipulated fingerprint exclusion (CR-E02 §3) | **CONFIRMED** as a party stipulation |
| ATF Exhibit 2 = the chamber case (CR-E02 §4) | **Inference, not fact** — re-graded Medium-high. See §2.1 |
| DNA likelihood ratios (CR-E02 §5.1) | **CONFIRMED as incomplete**, correctly flagged unusable |
| Register integrity D-1–D-50 | **PASS** — no gaps, single assignment site per number |
| Tiering discipline | **PASS** — no silent promotions found |

## 2. DEFECTS FOUND

### 2.1 MATERIAL — the `source identification` was over-weighted, and D-48 was wrong twice

**What the files said.** CR-ACQ v1.1 made the cartridge-case `source identification` its headline, and resolved D-48 **against** Owens on the basis that her description omitted it.

**What the record actually supports.** Faumuina testified that the case was **recovered from the rifle's chamber** ("this is what was in the chamber"), and that the gun's contents went to the FBI and then to the ATF lab. A fired case found *inside* a rifle is expected to identify to that rifle. On the portion of the record read, **no cartridge case was recovered at the perch or anywhere at the scene**, and the only projectile evidence from the body was **inconclusive**. **The ATF firearms examination therefore did not link the rifle to the shooting** — which is substantially what Owens' description claimed.

**But the correction does not simply revert**, because the ATF *also* performed the DNA testing (Exhibit 30), which produced very large likelihood ratios for Robinson on the trigger, trigger guard and scope. So the claim is **true of ATF ballistics and false of the ATF's work as a whole**.

**Fixed:** D-48 re-resolved as an explicit split at **CR-ACQ §6.1 (v1.3)**; CR-E02 §4 rewritten to carry the limitation forward.

**Root cause — and it is the same one as this morning's.** CR-ACQ read the ATF report *in isolation from the provenance of the items it examined*. This morning's error was reading a report through an adversary's selective quotation; this one was reading a report without asking where its exhibits came from. **Both are failures to ask what the document does not say about itself.** The standing rule at CR-ACQ §0 is extended accordingly (§4).

### 2.2 MATERIAL — a measurement was recorded that the witness did not give

CR-E02 v1.0 recorded "**410 feet** from the perch to the tent." Faumuina, asked the distance directly, said "**approximately 415 feet**." The 410 figure came from **counsel's restatement**, which she then affirmed. v1.0 recorded counsel's number and dropped the witness's.

This is a small numeric spread with an outsized propagation risk: a distance figure written into this library would be re-cited indefinitely, and `files - Losee building` is exactly the file it would land in. **Fixed:** registered as **D-50**, with both figures preserved and neither adopted.

### 2.3 MATERIAL OMISSION — the engraved ammunition

CR-E02 v1.0 built a three-way Dremel convergence but **omitted the engravings themselves**: Exhibit 20 (the cartridges from the gun) bears markings read into the record as "A fascist," and Exhibit 23 (five casings on a safe at the residence) includes one engraved "**test shot**." These are the direct product-level link between the rotary tool and the ammunition, and their omission understated the convergence. **Fixed:** CR-E02 §5.2b added, with the content and completeness of the inscriptions expressly **not** established.

### 2.4 MINOR — an inference presented as a fact

CR-E02 v1.0 stated flatly that the chamber case "is" the ATF's source-identified Exhibit 2. The two use different exhibit-numbering systems and the identity is an **inference** — well-supported (one fired case plus three cartridges, Remington headstamp, custody chain) but not stated by any witness. **Fixed:** re-graded **Medium-high** and labelled an inference.

## 3. WHAT SURVIVED

Stated because an audit that only ever finds fault is as unreliable as one that never does:

- **Karner's pliers testimony, the data-insufficiency basis of `inconclusive`, and the DOJ limiting language** — all confirmed verbatim, all correctly characterized.
- **The State's cross-examination material** in CR-E01 §3.6 — confirmed, including the AFTE proficiency-test provenance of the defence's three comparison photographs.
- **The fingerprint exclusion** — confirmed as a stipulation agreed by both parties, and correctly bounded (three prints of comparable value; not an exclusion from the scene).
- **The DNA caveat** — CR-E02 correctly refused to use likelihood ratios captured without their alternative hypotheses. **That restraint was right and should be the template.**
- **Scope statements** — every file declared what it had not read. No file claimed coverage it lacked. The keyword-sampling method in CR-E02 §1 was declared as sampling rather than presented as a full read.
- **Register integrity** — D-1–D-50, no gaps, one assignment site per number, forward-looking notes read rather than pattern-matched.

## 4. STANDING RULE, EXTENDED

CR-ACQ §0 already held: *a quotation by an interested party is reliable as to the words, not as to the document.* Today's second defect extends it:

> **A forensic report is reliable as to the items it examined, and silent about where those items came from.** An identification is only as probative as the provenance of the thing identified. **Always ask what the document does not say about itself** — who selected the exhibits, where they were recovered, and what was *not* submitted.

Both of the day's material errors were instances of this one failure. **Neither was caught by careful reading of the document in hand; both were caught by reading a second source.** The operational lesson: for any load-bearing forensic finding, **provenance is a separate verification act** from the finding itself.

## 5. RESIDUAL — WHAT THIS PASS DID NOT DO

1. **It is a self-audit.** The same analyst produced and checked the work; an independent reader would likely find more.
2. **It checked claims against the banked artifacts, not against the certified record.** Every transcript quotation remains subject to the commercial-rendering caveat.
3. **It did not re-read anything unread.** Days 1/2/3/5, most of Faumuina, and every exhibit remain outside the checked set — so defects arising from *absence* of material are largely invisible to this pass.
4. **It did not re-audit the BOC side of the day's work** (D-45/D-46/D-47, BOC-ROUTE, T1, E07/E08). **That remains owed.**
5. **Exhibit 30 and the full fingerprint stipulation were not obtained**, so two of the day's biggest caveats stand exactly where they were.

---

## REVISION LOG

| Version | Date | Change |
|---|---|---|
| 1.1 | 2026-07-27 | **Two of this pass's own findings revised by the full reading of Faumuina (CR-E02 v1.2).** (a) **D-50 dissolved:** §2.2 registered a 415-vs-410 conflict from a truncated extract; the complete answer gives 415 ft slope, 410 ft horizontal, 68 ft vertical for one geometry, internally consistent by Pythagoras. **The skepticism was correct on the evidence then held — refusing to silently pick a number from a fragment was right — but the defect it identified was in the sampling, not in the testimony.** (b) **§2.3 understated rather than overstated:** the engraved ammunition was not merely omitted; the ATF **identified the Dremel bit** as having made the marks (Exhibit 34), so CR-E02's class-level bounding was wrong in the State's favour. **Lesson for future passes: auditing a summary against a *sample* of the source can only find errors the sample contains.** An adversarial pass is bounded by the completeness of what it re-reads. |
| 1.0 | 2026-07-27 | Initial file. Adversarial pass over CR-ACQ v1.2, CR-E01 v1.1, CR-E02 v1.0. **Four defects found, two material.** (a) The `source identification` was over-weighted: the identified case came from the rifle's own chamber, no case was recovered at the scene on the record read, and the body fragment was inconclusive — so ATF **ballistics did not link the rifle to the shooting**, while ATF **DNA** does link the gun to Robinson. **D-48 re-resolved a second time, as an explicit split** (CR-ACQ §6.1). (b) A measurement was recorded from counsel's restatement (410 ft) rather than the witness's answer (415 ft) — **registered as D-50**, neither figure adopted. (c) The **engraved ammunition** ("A fascist" on the cartridges in the gun; "test shot" on a casing at the residence) was omitted from the Dremel convergence — added at CR-E02 §5.2b. (d) An exhibit-identity inference was stated as fact — re-graded Medium-high. **Standing rule extended:** a forensic report is reliable as to the items examined and silent about their provenance; both material errors were instances of that single failure, and both were caught only by reading a second source. Confirmations logged for what survived, including the restraint shown on the incomplete DNA likelihood ratios. Residual stated: this is a self-audit, checked against banked rather than certified records, and **the BOC side of the day's work remains un-audited**. |
