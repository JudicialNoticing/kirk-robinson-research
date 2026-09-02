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
| **Stored at** | ~~`~/kirk-capture/3f3EMabrrFQ_20260828_pool-feed.mp4`~~ — **deliberately OUTSIDE this repository**. 🛠 **Corrected 2026-09-02: that merged file never came to exist** — the recorder died before yt-dlp's merge step (§2c). The holdings are the four files in §2c's table, all in `~/kirk-capture/`. |

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

## 2c. 🚨 How the capture ended — BOTH recorders died at 15:47 EDT, and the VOD was pulled the next morning

**Established 2026-09-02 09:00 EDT from the recorders' own logs.** The 09-01 session-close note said the recorders were *"independent of any Claude session"* and would *"finish on their own."* The first half was true; the second was not. **Both logs end at the same minute with the same error:**

> R1 (`yt-dlp.log`): `ERROR: 3f3EMabrrFQ: Unable to download API page: HTTPSConnection(host='www.youtube.com', port=443): Failed to resolve 'www.youtube.com' ([Errno 8] nodename nor servname provided, or not known)` — after three retries.
> R2 (`yt-dlp-liveedge.log`): `Failed to resolve hostname rr3---sn-uhvcpax0n5-4gbd.googlevideo.com: nodename nor servname provided, or not known` … `Segment 3567 of playlist 0 failed too many times, skipping`, last frame at `time=03:22:15.02`.

▶️ **Cause: DNS resolution failed on this machine at ~15:47 EDT — a network loss, not a process kill.** Every file in the directory carries mtime `Sep 1 15:47`, one minute after the session-close commit (`15:46`). ⚠️ **What actually happened is that the session's health monitors died with the session, the network went a minute later, and nothing was left to notice.** A `nohup` survives a closed terminal; it does not survive the network, and a watcher that lives inside a Claude session cannot outlive it. **Lesson for the next live capture: the watcher belongs in launchd, and a recorder needs `--retries infinite`/reconnect semantics or a supervisor that restarts it.**

**What the recorders hold** (probed with `ffprobe` and hashed 2026-09-02 09:07 EDT):

| File (`~/kirk-capture/`) | Covers (EDT) | Duration | Bytes | SHA-256 |
|---|---|---|---|---|
| `R1_3f3EMabrrFQ_pool-feed_from-start_1051-1547.mp4` — **R1, remuxed by hand** from its two `.part` files (`ffmpeg -c copy`, both streams present) | 10:50:31 → ~15:47 | **4:57:10** (17,830 s) | 1,239,558,221 | `b5b2f8939a723080f0180ac6b7589f5750c8346c0f84a9afc0f4d98c52ca2bd0` |
| `3f3EMabrrFQ_20260828_pool-feed.f137.mp4.part` — R1 video, as left by yt-dlp (`.ytdl` state: fragment 3565 of 3566) | same | 17,830 s | 947,593,716 | `40bf146b47a475bf9dc5fb2f434930245c1eb5dc1b85d77d67176434420460fe` |
| `3f3EMabrrFQ_20260828_pool-feed.f140.mp4.part` — R1 audio, as left by yt-dlp | same | 17,830 s | 292,110,006 | `bf1457e8871d7cfacb0e2f035b50345171024be7116ac8202206e2f793b9ac43` |
| `LIVEEDGE_3f3EMabrrFQ_pool-feed.mp4` — **R2**, HLS via ffmpeg from the live edge | 12:24 → ~15:46 | **3:22:15** (12,135 s) | 1,175,191,552 | `33dfc44b2bdc7d345cc151bf622072e6e667a0a0d9155a03e9ca82fadcf82a82` |

⚠️ **The broadcast ran far past the recorders.** YouTube's watch-page JSON on 09-02 gives `startTimestamp 2026-09-01T14:50:31Z` (10:50:31 EDT) and `endTimestamp 2026-09-02T00:35:37Z` (**20:35:37 EDT**), `lengthSeconds 35110`. **R1 therefore holds the first 4h57m of a 9h45m broadcast — 51%.** What the feed carried after 15:47 (argument, recess, ruling, arraignment, or a static slate) is **not established from the recorders** and is not asserted here.

### ✅ The VOD persists — and it is now held

**Checked 2026-09-02 08:59 EDT:** `playabilityStatus: OK`, `isLiveNow: false`, `isLiveContent: true`, oEmbed 200 (*"Tyler Robinson Trial Pool Feed"*, KUTV 2 News Salt Lake City). `yt-dlp`'s metadata records `availability: unlisted`, `live_status: was_live`, `view_count: 900` at fetch time. ⚠️ **Unlisted means it is reachable only by the URL the court's notice published — not discoverable, and removable at the host's discretion at any time.** That is why it was pulled immediately rather than queued:

| File (`~/kirk-capture/`) | Duration | Streams | Bytes | SHA-256 |
|---|---|---|---|---|
| **`VOD_3f3EMabrrFQ_pool-feed.mp4`** — the full broadcast, downloaded 2026-09-02 09:03–09:08 EDT (`yt-dlp`, formats 137+140, merged) | **9:45:10** (35,110.06 s) | h264 1920×1080 + aac | **4,856,622,035** | `60fd70e91e8ec6c2d7ce52529de9f762ccb26d69241d60c39832713842b50ad0` |
| `VOD_3f3EMabrrFQ_pool-feed.info.json` — yt-dlp metadata as fetched | — | — | 160,676 | `b8c9dce09c0fd5389a38e04d818f000abf4b5f594162245aaf890e329cb2bfc3` |

**Verified opens and carries both streams** (`ffprobe`, 2026-09-02 09:10). Hash lists are alongside the files as `R1R2_sha256.txt` and `VOD_sha256.txt`.

⚖️ **Standing of the VOD versus the live captures.** The VOD is the host's post-broadcast rendering of the same feed, fetched **after** the event; R1 and R2 were taken **during** it. Where they overlap, R1 is the contemporaneous copy and the VOD the retrospective one — the same relationship as a same-day recording to an archive copy. None of the three is a certified record (§4). ⚠️ **Whether the VOD is byte-for-byte the broadcast as streamed — trimmed, re-encoded, or edited by the host — is not established and is not assumed.**

⚠️ **Disk:** the directory now holds ~8.5 GB and the machine has ~24 GB free. The two `.part` files are redundant with the R1 remux (which was built from them without re-encoding) — **deleting them is the owner's call; nothing here does it.**

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

> 🛠 **Dated note, 2026-09-02 — the sentence "Mr. Robinson has not been bound over" was true when written (09-01, before the hearing) and is now superseded by an observed status, not by this file:** a bindover on all seven counts is **reported** to have issued orally from the bench on the evening of 2026-09-01, verified at outlet grade (T1 via T3, no primary document) in [CR-WATCH-log Run 9](CR-WATCH-log.md). **This file still asserts nothing about the outcome; the posture line of record is `DOCKET-WATCH.md`'s, and its revision is the owner's.** The capture (§2c) is the only contemporaneous record of the ruling the library holds, and it has not been viewed or indexed for it.

---

## 5. Owed next

- [x] ~~On capture completion: record final byte size, duration, and **SHA-256** in this file.~~ ✅ **Done 2026-09-02 (§2c) — but "completion" never came: both recorders died at 15:47 EDT on a DNS failure.** Sizes, durations and SHA-256 for all four recorder files are in §2c.
- [x] ~~Verify the merged mp4 opens and carries both streams before treating the capture as successful.~~ ✅ **R1 remuxed by hand and verified 2026-09-02** (4:57:10, video + audio). The yt-dlp merge never ran.
- [x] ~~Note whether the VOD persists at the source URL after the broadcast ends~~ ✅ **It persists (checked 2026-09-02 08:59, `playabilityStatus: OK`, unlisted) — and it is now HELD: 9:45:10, 4.86 GB, SHA-256 in §2c.** Retention policy still unknown; the copy makes the question moot for this proceeding.
- [ ] ⚠️ **NEW 2026-09-02 — the recorders cover only the first 51% of the broadcast.** What the VOD carries after 15:47 EDT has not been viewed or indexed; any use of the capture for the ruling or the arraignment reported that day (see `CR-WATCH-log` 2026-09-02) must work from the VOD, with §2c's caveat that it is the host's retrospective rendering.
- [ ] 👤 Decide whether a transcript is wanted (the on-call audio-transcription tooling can take the audio track).
- [x] ~~Fold this acquisition into the `DOCKET-WATCH` access-routes table~~ ✅ **Done 2026-09-02 — `DOCKET-WATCH.md` v1.9, new "Court-announced livestream / VOD" row.** *(History: the livestream URL previously appeared exactly once in the entire library, inside a quoted notice at `CR-WATCH-log.md`, in no queue row and no access-routes table.)*

---

## 6. Provenance

Captured and recorded 2026-09-01 by a Claude Code session working from the Obsidian vault. **§2c and the §5 updates added 2026-09-02 by the next vault session**, from the recorders' logs, `ffprobe`, `shasum`, YouTube's watch-page JSON and yt-dlp's metadata — all read directly. Court notice re-read
the same day from the page body (HTTP 200, 42,873 bytes), not from a search summariser — the discipline this
library adopted after a summariser twice rendered the hearing date as 2026-08-28.
