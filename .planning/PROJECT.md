# StreamLive - Mobile Live Streaming Platform

**One-liner**: Invite-only mobile live streaming with RTMP ingest and HLS playback - streamer broadcasts from iPhone, viewers watch via stream codes.

## Overview

A minimal viable live streaming platform where:
- One user launches a video stream from their iPhone
- Other users join via a stream code to watch
- Clean, simple UX: Start stream → Share code → Others join → Watch live

This is a prototype focused on proving the core streaming mechanics work reliably before adding social features (chat, view counts, discovery).

## Requirements

### Validated

(None yet — ship to validate)

### Active

**Phase 1: Core Streaming (MVP)**
- [ ] Streamer can start a live stream from iPhone
- [ ] Streamer can stop their stream
- [ ] Stream generates a reusable code/identifier
- [ ] Viewer can enter stream code to join
- [ ] Viewer can watch live stream with reasonable latency (<20s)
- [ ] Viewer can close/leave stream
- [ ] Backend handles RTMP ingest from streamer
- [ ] Backend transcodes to HLS for playback
- [ ] Backend tracks active streams with metadata

**Phase 2: Social Features (Future)**
- [ ] Live chat (viewers + streamer can message)
- [ ] View count display for streamer
- [ ] Chat toggle (show/hide) on both screens
- [ ] Auto-reconnect for viewers on network hiccups

### Out of Scope

- **No VOD/Recording** — Only live streams, no replay capability
- **No discovery feed** — No browsing/exploring streams, direct join only
- **No monetization** — No tips, subscriptions, ads, payments
- **No moderation tools** — No blocking, banning, timeouts, reporting
- **No multi-stream** — One stream per user at a time
- **No stream history** — No analytics, past stream tracking (for MVP)

## User Experience

### Streamer Flow
1. Open app → Home screen with 2 buttons: "Start Stream" | "Find Stream"
2. Tap "Start Stream" → Opens streaming screen
3. Streaming screen shows:
   - Main view (camera feed being broadcast)
   - Stream controls (Start/Stop button)
   - Stream code display (to share with viewers)
   - (Phase 2: View count, Chat toggle)
4. Tap "Stop Stream" → Stream ends, code can be reused

### Viewer Flow
1. Open app → Home screen
2. Tap "Find Stream" → "Enter code" screen
3. Enter stream code → Opens viewer screen
4. Viewer screen shows:
   - Live video stream
   - Close button to exit
   - (Phase 2: Chat toggle)

## Architecture

### Backend Stack
- **Framework**: FastAPI (Python)
- **Package Manager**: uv (modern, fast alternative to poetry/pip)
- **Media Server**: Self-hosted (nginx-rtmp or MediaMTX/SRS)
- **Streaming Protocol**: RTMP ingest → HLS (or LL-HLS) playback
- **Database**: SQLite or PostgreSQL (minimal - just stream metadata)
- **Auth**: Device ID based (no login/signup for MVP)
- **Hosting**: Local/VPS (free tier or self-hosted to minimize costs)

### iOS Stack
- **Language**: Swift
- **UI Framework**: SwiftUI
- **Project Management**: Tuist (NOT Xcode projects/SPM)
- **Video Capture**: AVFoundation for camera
- **RTMP Publishing**: iOS RTMP library (HaishinKit or similar)
- **HLS Playback**: AVPlayer with HLS manifest
- **Min iOS Version**: TBD (recommend iOS 17+ for modern SwiftUI)

### Data Model (Minimal)

**Stream:**
- `id` (UUID)
- `streamer_device_id` (string)
- `stream_code` (string, reusable identifier)
- `status` (enum: active, ended)
- `started_at` (timestamp)
- `ended_at` (timestamp, nullable)
- `rtmp_url` (string)
- `hls_url` (string)

**Device:**
- `device_id` (UUID, generated on first launch)
- `created_at` (timestamp)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| RTMP→HLS instead of WebRTC | Simpler implementation, 10-20s latency acceptable for MVP | — Pending |
| Device ID auth (no signup) | Minimize friction, validate concept first | — Pending |
| Self-hosted media server | Zero cost constraint, acceptable complexity tradeoff | — Pending |
| Tuist for iOS project | User preference, avoids Xcode project management pain | — Pending |
| Stream codes are reusable | Same streamer = same code, simplifies UX | — Pending |
| One stream per user | Scope constraint, reduces backend complexity | — Pending |
| No persistence of stream history | MVP focuses on live experience only | — Pending |

## Constraints

### Hard Constraints
- **Budget**: Free or near-zero cost (no paid services until validated)
- **Timeline**: No hard deadline (prototype-driven)
- **Platforms**: iOS only for client (no Android, no web)
- **Tooling**: Prefer modern, fast tools (e.g., uv over poetry, avoid slow legacy tooling)

### Technical Constraints
- **Latency**: <20 seconds acceptable for MVP
- **Concurrent streams**: Start with low scale (1-10 concurrent streams)
- **Video quality**: Adaptive HLS bitrates, prioritize reliability over 4K

## Success Criteria

**Phase 1 is successful when:**
1. ✅ Streamer can reliably start/stop stream from iPhone
2. ✅ Viewer can join via code and watch with <20s latency
3. ✅ Backend handles transcoding without crashes
4. ✅ Streams auto-cleanup when ended
5. ✅ No crashes during 5-minute continuous stream test

**Ready for Phase 2 when:**
- All Phase 1 criteria met
- Tested with 3+ concurrent viewers on one stream
- Code shared with 2-3 friends for dogfooding

## Open Questions

- [ ] Which iOS RTMP library? (HaishinKit vs LFLiveKit vs custom)
- [ ] Which media server? (nginx-rtmp vs MediaMTX vs SRS)
- [ ] HLS segment duration? (2s, 4s, 6s chunks)
- [ ] Stream code format? (6-digit numeric, alphanumeric, UUID)
- [ ] Error handling on stream failure? (reconnect logic, retry limits)
- [ ] Server deployment target? (Local docker, Railway, Render, Fly.io)

## Next Steps

1. Set up project structure (backend + iOS with Tuist)
2. Choose and configure media server
3. Build backend API (start/stop stream, stream metadata)
4. Build iOS streamer (camera capture → RTMP publish)
5. Build iOS viewer (HLS playback)
6. Test end-to-end flow

---

*Last updated: 2026-01-09 after initialization*
