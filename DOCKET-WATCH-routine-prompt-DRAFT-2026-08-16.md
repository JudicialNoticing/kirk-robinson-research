# DOCKET-WATCH routine prompt — DRAFT 2026-08-16

**Status:** 👤 **AWAITING OWNER AUTHORISATION. Not yet applied to the routine.**
**Target:** cloud routine `trig_016faLfbQWCz72M463Dy8HsL` ("DOCKET-WATCH — State v. Robinson, Case 251403576 (report-only)").
**Supersedes:** `DOCKET-WATCH-routine-prompt-DRAFT-2026-08-14.md`, applied 2026-08-14T20:23 EDT and confirmed live from the API.

---

## Why this draft exists — the reason is a posture error, not housekeeping

🚨 **The routine's live prompt tells it the preliminary hearing was "HELD."** Verified against the API on 2026-08-16 at 22:4x EDT: the inlined calendar reads

> `- 2026-07-06 to 07-10: preliminary hearing, five days. HELD.`

and the routine's `updated_at` is **2026-08-15T00:23:59Z**, i.e. **2026-08-14 evening ET** — *before* the 2026-08-16 evening correction.

⚠️ **On 2026-08-16 this library established, directly against `day5.txt`, that the preliminary hearing was NOT concluded on 2026-07-10.** Those were five days **of evidence**; **2026-09-01 is the hearing's last day**; and that is why Robinson has not been bound over. The correction was propagated to `DOCKET-WATCH.md` and `START-HERE.md` — **and stopped there.**

🚨 **`DOCKET-WATCH.md` says in its own words that the file and the routine's prompt "are not automatically in sync."** So the next firing — **Wed 2026-08-19, 09:00 ET, the morning after the State's reply** — would run carrying a superseded posture statement **inside the one spec whose absolute prohibition is that it must not state case posture.**

⚠️ **Note what the prohibition alone could not prevent.** The prompt already forbids the routine to state a new posture conclusion. It does not help, because the wrong posture is supplied to the run **as background fact**, above the prohibition. **A prohibition on concluding does not protect against a false premise.**

---

## The changes, and nothing else

Only the marked passages change. Everything else — the prohibitions, the sourcing discipline, the escalation triggers, the report headings — is carried across verbatim, because it works.

### 1. The calendar's first bullet — REPLACE

**From:**
> `- 2026-07-06 to 07-10: preliminary hearing, five days. HELD.`

**To:**
> `- 2026-07-06 to 07-10: FIVE DAYS OF EVIDENCE in the preliminary hearing. THE HEARING WAS NOT CONCLUDED — it was continued. Do NOT describe it as "held," "concluded," "completed" or "closed." Established Tier 1 against the Day 5 transcript: defence counsel refers to "the last day of the preliminary hearing, which will be September 1st"; the court speaks of motions "ahead of the September 1st hearing"; the State addresses "the continued taking of evidence today."`

### 2. The 09-01 bullet — REPLACE

**From:**
> `- 2026-09-01, 10:00 a.m.: ORAL ARGUMENT, in person, up to two hours per side.`

**To:**
> `- 2026-09-01, 10:00 a.m.: THE LAST DAY OF THE PRELIMINARY HEARING, given over to argument — in person, up to two hours per side. This is not a separate proceeding following a completed hearing; it is the hearing's final day. Confirmed standing by a Tier 2 named-official item dated 2026-08-11.`

### 3. The presumption-of-innocence prohibition — ADD one sentence

**Append to the existing bullet:**
> `AND the preliminary hearing itself is UNFINISHED. Robinson has not been bound over BECAUSE THE HEARING IS NOT OVER — not because anything anomalous has occurred. Reporting the non-bindover without that fact makes the posture read as an anomaly. If you cannot state the posture in those terms, state no posture at all.`

### 4. Route status — REPLACE the "as of 2026-08-14" paragraph

**To:**
> `Route status as of 2026-08-16, from LOCAL runs: DocumentCloud's API is INTERMITTENT — 403 behind a Cloudflare interstitial at 09:00, fully open at 14:05 and again at 22:47 the same day, with nothing changed in between. NEVER log its silence as a null; a blocked route is unattemptable, not empty. rev.com is open and is enumerable FROM ITS SITEMAP — /transcripts/search?q= is a 404 and is not a search endpoint. The Fox outlet mirror (static.foxnews.com uploads) is open and BASELINED at 55 PDFs under 2026/08 with exactly one genuine case item, so detection there is a diff rather than a search. atty.utahcounty.gov is open but structurally hosts NO filings (four consecutive failures for that purpose). Scribd is challenge-gated. Utah XChange is paywalled (owner-only). From CLOUD runs, all direct fetches have been egress-blocked since 2026-08-05 — that is the environment, not the sites, and the control fetch tells you which.`

### 5. The 08-18 bullet — REPLACE the status half

**To:**
> `- 2026-08-18: State's reply due, 18-page limit. As of 2026-08-16 not yet due and not filed: no early filing indexed, no mirror. ⚠️ YOUR OWN NEXT FIRING IS 2026-08-19, THE DAY AFTER THIS DEADLINE, AND YOU ARE PROBABLY EGRESS-BLIND. A local by-hand run is the only document-capable cover, and one was scheduled for 08-18. If you are reading this on 08-19: check whether that local run happened before treating your own findings as the first look, and if it did not, say so at the TOP of your report.`

---

## What is deliberately NOT changed

- **The report-only delivery path.** Fixing that needs `/web-setup` plus adding a repository source to the routine's config — 👤 owner actions, unchanged and still outstanding. `No sources configured` remains true.
- **The egress blindness.** Still an environment network-access setting (Default env, Trusted level). No prompt wording fixes it.
- **The Wed/Sat cadence.** ⚠️ Moving it would not help: the reply is due Tuesday and a Tuesday-morning firing would run before any filing appears. **The gap is the blindness, not the day** — a scheduled run that cannot fetch documents cannot cover a filing window whatever time it fires.

---

## Revision log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-16 | Created (Q-140 session). Drafted after an API read of the live routine showed its inlined prompt still carries `preliminary hearing, five days. HELD.` — the exact formulation corrected library-wide on 2026-08-16 evening — with `updated_at` 2026-08-15T00:23:59Z, predating the correction. Five targeted replacements; prohibitions, sourcing discipline, escalation triggers and report headings carried across verbatim. **Not applied — awaiting owner authorisation, as the 2026-08-14 draft was.** |
