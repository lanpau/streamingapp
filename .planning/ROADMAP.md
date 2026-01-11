# Roadmap: StreamLive

## Overview

StreamLive MVP will be built in 6 phases, starting with project scaffolding, then establishing the media server infrastructure, building the backend API, implementing the iOS streamer and viewer apps, and finally integrating and validating the end-to-end flow. The goal is to prove core streaming mechanics work reliably: streamer broadcasts from iPhone, viewers watch via stream codes.

## Domain Expertise

None

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Foundation** - Project scaffolding with backend (FastAPI + uv) and iOS (Tuist)
- [x] **Phase 2: Media Server** - Self-hosted RTMP→HLS infrastructure setup
- [ ] **Phase 3: Backend API** (In progress) - FastAPI stream management endpoints
- [ ] **Phase 4: iOS Streamer** - Camera capture and RTMP publishing
- [ ] **Phase 5: iOS Viewer** - HLS playback and stream joining
- [ ] **Phase 6: Integration** - End-to-end testing and MVP validation

## Phase Details

### Phase 1: Foundation
**Goal**: Set up project structure with backend (FastAPI + uv) and iOS (Tuist) scaffolding
**Depends on**: Nothing (first phase)
**Research**: Unlikely (standard project setup patterns)
**Plans**: TBD

Plans:
- [x] 01-01: Initialize FastAPI backend with uv
- [x] 01-02: Initialize iOS project with Tuist
- [x] 01-03: Local development environment setup

### Phase 2: Media Server
**Goal**: Configure self-hosted media server for RTMP ingest and HLS output
**Depends on**: Phase 1
**Research**: Likely (external technology choice)
**Research topics**: nginx-rtmp vs MediaMTX vs SRS comparison, HLS segment duration, Docker setup, RTMP auth patterns
**Plans**: TBD

Plans:
- [x] 02-01: Research and select media server (Merged with 02-02)
- [x] 02-02: Configure RTMP ingest and HLS output (MediaMTX)
- [x] 02-03: Docker-based local development setup

### Phase 3: Backend API
**Goal**: FastAPI endpoints for stream lifecycle management
**Depends on**: Phase 1, Phase 2
**Research**: Unlikely (standard FastAPI patterns)
**Plans**: TBD

Plans:
- [x] 03-01: Database models and stream management
- [ ] 03-02: Stream API endpoints (create, get, list)
- [ ] 03-03: Device ID authentication

### Phase 4: iOS Streamer
**Goal**: Camera capture and RTMP publishing from iPhone
**Depends on**: Phase 2, Phase 3
**Research**: Likely (iOS RTMP library choice)
**Research topics**: HaishinKit vs LFLiveKit, AVFoundation streaming, RTMP connection management
**Plans**: TBD

Plans:
- [ ] 04-01: Research and integrate RTMP library
- [ ] 04-02: Camera capture with AVFoundation
- [ ] 04-03: Streamer UI and controls
- [ ] 04-04: Backend API integration

### Phase 5: iOS Viewer
**Goal**: HLS playback and stream joining via code
**Depends on**: Phase 2, Phase 3
**Research**: Unlikely (standard AVPlayer/HLS patterns)
**Plans**: TBD

Plans:
- [ ] 05-01: Stream code entry UI
- [ ] 05-02: HLS playback with AVPlayer
- [ ] 05-03: Error handling and exit flow

### Phase 6: Integration
**Goal**: End-to-end testing and MVP validation
**Depends on**: Phase 4, Phase 5
**Research**: Unlikely (internal testing)
**Plans**: TBD

Plans:
- [ ] 06-01: End-to-end stream flow testing
- [ ] 06-02: Latency and reliability validation
- [ ] 06-03: Multi-viewer testing

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 3/3 | Completed | 2026-01-10 |
| 2. Media Server | 3/3 | Completed | 2026-01-11 |
| 3. Backend API | 1/3 | In progress | 2026-01-11 |
| 4. iOS Streamer | 0/4 | Not started | - |
| 5. iOS Viewer | 0/3 | Not started | - |
| 6. Integration | 0/3 | Not started | - |
