# CR-ACQ-2026-09-01 — Preliminary-hearing livestream, capture record

**Acquisition record for the 2026-09-01 hearing's public livestream.** Written at capture time, before the
hearing began, so the provenance is contemporaneous rather than reconstructed.

---

## 1. What was captured

| Field | Value |
|---|---|
| **Source URL** | `https://youtube.com/live/3f3EMabrrFQ` |
| **Feed title** | *Tyler Robinson Trial Pool Feed* |
| **Host channel** | KUTV 2 News Salt Lake City (`@KUTV2News`, `UCFVUStJ4azXbWMhFO4yTELg`) |
| **Announced by** | [Utah Courts press notification, posted 2026-08-28](https://legacy.utcourts.gov/utc/news/2026/08/28/public-attendance-for-tyler-robinson-preliminary-hearing/) — *"The preliminary hearing will be live streamed. Please tune into your preferred news outlet or click …"* |
| **Capture tool** | `yt-dlp --live-from-start`, video `f137` + audio `f140`, merged to mp4 |
| **Capture started** | 2026-09-01 **11:04 EDT** |
| **Stored at** | `~/kirk-capture/3f3EMabrrFQ_20260828_pool-feed.mp4` — **deliberately OUTSIDE this repository** |

⚠️ **Why the file is not in the repo.** It is multi-gigabyte, and this repository sits in `~/Documents`, which is
iCloud-synced. Eviction of large files in that container is a **recorded, repeated failure on this machine** — it
cost a sibling project a nine-day silent outage. A capture stored where iCloud can evict it is a capture that may
not exist when it is needed. The file lives outside the container; this record is the repo's pointer to it.

---

## 2. Timeline observed at capture

| Time (EDT) | Observation |
|---|---|
| 10:48 | Watch page HTTP **200**, `playabilityStatus: UNPLAYABLE`, `liveBroadcastDetails.isLiveNow: false` |
| 10:51 | `isLiveNow` → **true**, still `UNPLAYABLE` |
| 10:54 | `playabilityStatus` → **OK** — feed genuinely up |
| 11:04 | Capture started, `--live-from-start` back-filling from the broadcast's beginning |
| **12:00** | **Announced start of the hearing** (10:00 a.m. MDT) |

---

## 2b. 🚨 The capture stalled mid-hearing, and there are now TWO recorders

**At 12:24 EDT — 24 minutes into the hearing — the capture stopped growing.** A health watcher caught it. The
diagnosis: `yt-dlp` sat at `frag 1136/1136` with **81:17 downloaded** against a broadcast that had been live for
~93 minutes, i.e. **about twelve minutes behind the live edge and not advancing.** The process was alive and the
stream was `playabilityStatus: OK`, `isLiveNow: true`.

▶️ **Action taken: a SECOND, independent recorder was started rather than the first one repaired.** The content is
perishable and irreplaceable; diagnosing a stall while a hearing runs spends the only thing that cannot be
recovered. Redundancy first, diagnosis after.

| | Recorder 1 (`3f3EMabrrFQ_…pool-feed`) | Recorder 2 (`LIVEEDGE_3f3EMabrrFQ_…`) |
|---|---|---|
| Started | 11:04 EDT | 12:24 EDT |
| Mode | `--live-from-start` (DASH fragments) | live edge, HLS via ffmpeg |
| Holds | **the backfill from broadcast start** — unique to it | from 12:24 forward |

✅ **The stall was transient.** Recorder 1 resumed within ~2 minutes (88.5 → 89.6 MB) — a manifest-refresh pause at
the live edge, not a death. **The watcher's 4-minute threshold was too tight for a live stream** and produced a
false positive. That is the correct direction to be wrong in, and the threshold is now 6 minutes.

🚨 **A blind spot created by the fix, and closed.** The original watcher measured the *directory*, so once recorder
2 was running its steady growth would have **masked recorder 1 dying entirely**. The watcher now tracks each
recorder's own file and each process separately. ⚠️ **Recorder 1 is the one that matters most** — it alone holds
10:51 → 12:24, and if it dies before finishing, its `.part` files need remuxing by hand rather than yt-dlp's own
merge step.

---

## 3. 🚨 The timezone correction this acquisition depends on

**The hearing begins 10:00 a.m. MDT = 12:00 EDT.** The court's notice says *"10:00 a.m. **local time** at the
Provo Courthouse"*; Provo is Mountain. **Every statement of this time in this library and in the vault previously
read a bare "10:00"**, inside dated lists that are otherwise Eastern.

▶️ **This is not a pedantic point — it nearly cost the observation.** A check made at 10:48 EDT found the announced
stream returning HTTP 200 with `UNPLAYABLE`. Read on Eastern assumptions that is *"the hearing is 48 minutes old
and the stream has failed."* Read correctly it is *"the hearing has not started."* The first reading closes the
only observation route; the second waits sixteen minutes and captures it.

⚠️ **And a caution against this record's own method:** `UNPLAYABLE` from an anonymous, cookieless `curl` is
evidence about **our fetch**, not about the broadcast — YouTube gates such requests. The timezone finding rests on
the **court's own notice read from the page body**, not on the stream's state. Corrected in place at
`START-HERE.md` (×3), `DOCKET-WATCH.md`, the LIVE routine-prompt file, and the vault's project note and register.
🚩 **The DEPLOYED docket-watch routine's inlined prompt still carries the bare time** — the file is the source of
record, the routine is a separate copy, and editing it is owner-gated.

---

## 4. Standing and use

⚖️ **What this capture is.** A private working copy of a broadcast the **court itself publicly announced**, taken
for research use inside this library. It is not a certified record and **must not be cited as one**. The certified
preliminary-hearing transcript (SEC-A6) remains the authoritative artifact and is still unheld.

🚨 **Do not redistribute, re-publish, or quote this file as a broadcast source.** The library records that on
**2026-08-22 the defence filed oppositions to electronic media coverage of this hearing, together with motions to
seal** the unredacted EMC material, and that **no ruling on the sealing motions has been located**. A pending
motion is not a ruling and **no outcome is inferred from it here** — but a pending sealing question is exactly the
condition under which a private copy stays private.

⚖️ **Presumption of innocence.** Mr. Robinson has not been bound over. This record notes only that a proceeding
occurred and was streamed. **Nothing about the hearing's content, argument, or outcome is asserted anywhere in
this file.**

---

## 5. Owed next

- [ ] On capture completion: record final byte size, duration, and **SHA-256** in this file.
- [ ] Verify the merged mp4 opens and carries both streams before treating the capture as successful.
- [ ] Note whether the VOD persists at the source URL after the broadcast ends — **the library holds no record of
      Utah Courts' or KUTV's retention policy for these streams**, which is why the capture was taken at all.
- [ ] 👤 Decide whether a transcript is wanted (the on-call audio-transcription tooling can take the audio track).
- [ ] Fold this acquisition into the `DOCKET-WATCH` access-routes table — **the livestream URL previously appeared
      exactly once in the entire library**, inside a quoted notice at `CR-WATCH-log.md`, in no queue row and no
      access-routes table.

---

## 6. Provenance

Captured and recorded 2026-09-01 by a Claude Code session working from the Obsidian vault. Court notice re-read
the same day from the page body (HTTP 200, 42,873 bytes), not from a search summariser — the discipline this
library adopted after a summariser twice rendered the hearing date as 2026-08-28.
