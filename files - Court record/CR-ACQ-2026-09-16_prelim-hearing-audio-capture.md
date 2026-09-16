# CR-ACQ-2026-09-16 — Audio of the five preliminary-hearing evidence days (2026-07-06 → 07-10), capture record

**File ID:** CR-ACQ-2026-09-16 · **Scope:** the acquisition, outside this repository, of audio recordings of all five evidence days of the preliminary hearing, from two independent public YouTube uploads of the court's pool feed (Court TV; KSL News Utah), with hashes, durations, stream-start times, and a ten-slice content check against the banked Rev transcripts. · **Case context:** *State of Utah v. Tyler James Robinson*, No. 251403576, Fourth Judicial District Court, Provo — Hon. Tony F. Graf, Jr. · **Prepared:** 2026-09-16 · **Status/version:** v1.0 — an inventory with hashes and one verification act (§3); it makes no claim about the case record.

> ⚖️ **Presumption of innocence.** Mr. Robinson is reported bound over on all seven counts (2026-09-01; the signed order is held, `CR-ACQ`/`TJR-P01` §11) and has pleaded not guilty. A recording of a hearing establishes that the hearing occurred and what was said in it; it adjudicates nothing. **Nothing about the hearing's content or outcome is asserted in this file.**

---

## §0 · Sourcing framework (project standard)

Tier 1 — sworn testimony and primary court filings/documents · Tier 2 — named official statements · Tier 3 — named journalistic reporting/analysis · Tier 4 — anonymous/low-verification. "T1 via T3" marks primary-document content known only through reporting. Every claim carries a locator; every retrieval a date.

## §1 · Access-path caveats — read before using any file

- **These are third-party uploads of the court's pool feed, not the court's own recording.** Both channels carried the single media pool camera the court permitted (`CR-E06` §§ on the media-camera orders; the Utah Courts' 2026-08-28 notice for the 09-01 day names the same arrangement). Neither upload is a certified record. **The certified transcript (Q-36) remains the authoritative artifact and is still unheld.**
- **Audio only, 128 kbps AAC (YouTube format 140), two channels, 44.1 kHz.** Chosen because the machine has 24 GB free and video of five full days runs to tens of GB. The video remains available at the same ids at the time of writing; nothing here says it will stay available.
- **Stored OUTSIDE this repository**, at `~/kirk-capture/prelim-july-2026/`, for the reason `CR-ACQ-2026-09-01` §1 records (iCloud eviction of large files in `~/Documents` is a recorded failure on this machine). This folder holds the pointers: `SHA256SUMS.txt`, `durations.tsv`, `sources.json` (per-video metadata as YouTube served it: title, channel, upload date, release timestamp, duration), and the spot-check transcripts. The full `*.info.json` files sit beside the audio.
- **Court TV's stream clock IS the clock the Rev transcripts use.** Verified in §3: at five Rev timestamps, one per day, the Court TV audio carries the words Rev prints at that timestamp. So every `dayN.txt` locator in this library (e.g. `day4.txt 05:39:52`) addresses the Court TV file directly. ⚠ **Court TV's stream carries the network's own studio segments during recesses**; those are not the court record and are not the object of this acquisition.
- **KSL's stream runs on its own clock and drops recess time.** Its recordings are shorter on Days 1–4 and, at the release-timestamp offset, four of five anchors land on different (later) passages of the same hearing (§3). **Rev locators do NOT transfer to the KSL files without a per-segment offset map, which has not been built.** KSL is held as the independent second copy, not as a locator target.
- **Not verified:** that either recording is complete and gapless across its whole length (only five 75-second slices per source were checked); that the pool feed itself was unbroken; anything about the stretches of Day 4 and Day 5 that the court ordered withheld from the stream (`CR-E06`: the livestream was cut to audio while State's Exhibit 12.1 was displayed — an audio capture is unaffected by that, but the fact of the order is recorded).
- **Tools:** `yt-dlp` 2026.08.19 · `ffmpeg`/`ffprobe` (Homebrew) · `whisper-cli` (whisper.cpp, Homebrew) with `ggml-large-v3-turbo.bin` for the spot-checks. Captured 2026-09-16 16:09–16:17 EDT.

## §2 · What was captured

| File (in `~/kirk-capture/prelim-july-2026/`) | Channel | YouTube id | Uploaded | Stream start | Duration | Bytes | SHA-256 |
|---|---|---|---|---|---|---|---|
| `2026-07-06_day1_COURTTV_6fq2kCMVMXI.m4a` | COURT TV | `6fq2kCMVMXI` | 20260706 | 08:58:31 MDT | 7:47:25 | 453,555,611 | `1df9c0893fc15f1171f9cce3ba13197246c200f0a86db9d8604355d9638a560c` |
| `2026-07-06_day1_KSL_6Z76La2OYKQ.m4a` | KSL News Utah | `6Z76La2OYKQ` | 20260706 | 08:57:01 MDT | 7:39:05 | 445,465,745 | `1fdbfa45760b7cb3ca2a79163f3c3736cbffc0c30d7e9c73aaf1de5e0581d0d0` |
| `2026-07-07_day2_COURTTV_y6ofpz6ReuE.m4a` | COURT TV | `y6ofpz6ReuE` | 20260707 | 08:52:57 MDT | 8:16:15 | 481,534,655 | `f8a3d1ec7a0cde947e1c277ce96c969b1d74f428de098347232d11241f21dc16` |
| `2026-07-07_day2_KSL_nHSOGFiAI28.m4a` | KSL News Utah | `nHSOGFiAI28` | 20260707 | 08:54:01 MDT | 8:05:44 | 471,322,800 | `a223fc9db6e4f71b437770a551f8c2bcaf6923cda3b59bf6a275e148e53b5137` |
| `2026-07-08_day3_COURTTV_szsmK2Ul9XY.m4a` | COURT TV | `szsmK2Ul9XY` | 20260708 | 12:58:17 MDT | 3:31:45 | 205,471,510 | `3e72023f408f318a6ef8a3e9b448ebe1e27bb81a66eae1fcae635db303cfccd0` |
| `2026-07-08_day3_KSL_uZSYb3o1e_o.m4a` | KSL News Utah | `uZSYb3o1e_o` | 20260708 | 12:53:37 MDT | 3:26:01 | 199,901,932 | `1b78926743b1ef875f8d73ef5b7589fde6965402b791030e9e1c2b57467acfd6` |
| `2026-07-09_day4_COURTTV_89ZKQIHaJpM.m4a` | COURT TV | `89ZKQIHaJpM` | 20260709 | 09:03:52 MDT | 8:24:48 | 489,829,547 | `a0c3664207855fa302d2454df6c33db2fc15fb0277a396ebc815788a026bd45c` |
| `2026-07-09_day4_KSL_G5csxeUf9ts.m4a` | KSL News Utah | `G5csxeUf9ts` | 20260709 | 08:59:03 MDT | 7:55:42 | 461,587,319 | `605c9dbdbd04b34693c68b08ee867b3cb0d26508319578302bef310238431624` |
| `2026-07-10_day5_COURTTV_bFwe5CwDudk.m4a` | COURT TV | `bFwe5CwDudk` | 20260710 | 09:18:52 MDT | 2:39:45 | 155,013,575 | `d822394390b24873a79997f1340e2ea2a13eab94a43820affab258f869d780db` |
| `2026-07-10_day5_KSL_XzHdjfX3SNE.m4a` | KSL News Utah | `XzHdjfX3SNE` | 20260710 | 08:54:51 MDT | 3:04:10 | 178,708,539 | `fb069e503bbef6452d84dc84a7dab1df83e3e475f0500c90c4a6751edc811555` |

Rev transcript time spans for comparison, from the banked `dayN.txt` (first and last timestamp): **Day 1** 00:06:57→07:46:52 · **Day 2** 00:09:23→08:14:51 · **Day 3** 00:22:11→03:30:58 · **Day 4** 00:47:39→08:23:59 · **Day 5** 01:04:27→02:39:06. The Court TV durations bracket every span; Day 5's Court TV length (2:39:45) ends 39 s after Rev's last stamp (02:39:06).

## §3 · Verification performed — ten spot-checks, one per day per source

**Method.** For each day, one Rev timestamp with distinctive content was chosen from `dayN.txt` before any audio was heard: Day 1 `04:12:40` (the "27 minute and 35 second" body-camera question), Day 2 `05:04:54` (State's Exhibit 31 shown to the witness), Day 3 `00:22:11` (the monitor failure), Day 4 `05:39:52` (the Exhibit 2 cartridge case and the 15A cutter), Day 5 `01:04:27` (the court's ruling on the Exhibit 16 publication). A 75-second slice starting at that time was cut from the Court TV file, transcribed by whisper.cpp, and compared with the Rev text. For KSL, the same anchors were offset by the difference between the two uploads' `release_timestamp` values (Court TV minus KSL: +90 s, −64 s, +280 s, +289 s, +1,441 s). The whisper outputs are banked verbatim in `spotcheck/`.

| Day | Court TV at the Rev timestamp | KSL at the release-offset time |
|---|---|---|
| 1 | `SUPPORTED` — verbatim match ("So that 27-minute and 35-second body cam that starts when you're at the Hall of Flags…") | different passage: the State calling Agent Hull — **the hearing, but later in it** |
| 2 | `SUPPORTED` — verbatim ("I'd like to show you State's Exhibit 31…") | different passage: a witness stepping down — the hearing, earlier |
| 3 | `SUPPORTED` — verbatim ("Is it not projecting on the monitors? … Technology is challenging us again.") | different passage: agencies working the case — the hearing |
| 4 | `SUPPORTED` — verbatim ("This would have been the cartridge case that was found in the gun… Exhibit 15A engraving cutter…") | different passage: the *"It's not SBI, it's actually the state crime lab"* exchange, which Rev places at `06:10:42` — **KSL runs about 26 minutes ahead of Rev here** |
| 5 | `SUPPORTED` — verbatim ("The court will issue its ruling on the request by defense…") | `SUPPORTED` — the same ruling, at +1,441 s |

**Labels written:** 5 `SUPPORTED` (Court TV, one per day) · 1 `SUPPORTED` (KSL Day 5) · 4 KSL slices confirmed as hearing audio but **not time-aligned** (recorded as an access-path caveat, not a defect). **Nothing `CONTRADICTED`.** A verbatim match at a pre-chosen timestamp is a strong test that the file is the proceeding Rev transcribed; it is not a completeness test.

## §4 · Standing and use

⚖️ **What this is.** A private working copy of a public broadcast the court permitted, held for research use inside this library. **Not a certified record; must not be cited as one.** Its proper uses: (a) testing Rev's speaker labels (standing hazard 9) and garbles against the audio at a given locator; (b) checking a quotation's wording where the Rev rendering is doubtful; (c) establishing that a passage was or was not spoken. A quotation checked against this audio may be graded higher than a Rev rendering alone, **with the check recorded as an act** (which file, which timestamp, what was heard).

🚨 **Do not redistribute, re-publish, or excerpt these files as a broadcast source.** The 2026-08-22 defence oppositions to electronic media coverage and the sealing motions are on the record; the 09-09 dark firing reported the sealing request *denied* (`CR-WATCH-log`, T1 via T3, ruling not held). Whatever that ruling says, a private research copy stays private.

## §5 · Owed next

1. A per-segment offset map for the KSL files, if they are ever to be used as locator targets (otherwise the Court TV files serve).
2. A gapless-ness check: compare each Court TV file's duration against the stream's own timeline (the `release_timestamp` and the last Rev stamp bracket it; a fragment-level check was not run).
3. If disk allows later: the video at the same ids (the visual record of exhibits displayed on the media monitor; `CR-E06` §§ on Exhibits 16 and 24).
4. `SOURCE-MANIFEST.md` regenerated with this folder registered (done in the same session).

## §6 · Provenance

Captured, hashed and spot-checked 2026-09-16 by a Claude Code session working from this repository; the owner directed the acquisition ("start with number one") after the 2026-09-16 holdings inventory found no audio or video of the July evidence days anywhere in the library. Sources selected from a YouTube search the same afternoon: Court TV because it was the one channel with all five days complete and its clock matched Rev's; KSL because it is a Utah newsroom carrying the pool feed without a national network's chrome, and complete for all five days. Alternatives seen and not captured: The Salt Lake Tribune "full day" uploads (shorter — recesses cut), Associated Press (Days 3–5), Law&Crime (Day 5), the *Charlie Kirk* channel (Days 1 and 5), Forbes, BlazeTV, The Christian Post.

## Revision log

| Version | Date | Change |
|---|---|---|
| **1.0** | **2026-09-16** | Created. Ten audio files captured (3.4 GB, outside the repo), hashed and measured; ten 75-second spot-checks transcribed and compared: 5/5 Court TV verbatim at Rev's own timestamps, KSL confirmed as the hearing but on its own clock. No case claim made; no register entry assigned. |
