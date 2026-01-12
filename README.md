# StreamLive

## Meta

The project's main goal is to explore the [Get Shit Done](https://github.com/glittercowboy/get-shit-done) spec-driven workflow for agentic coding.

Almost everything in this repo is written by an AI.

## Description 
**Invite-only mobile live streaming with RTMP ingest and HLS playback.**


One user launches a video stream from their iPhone, others join via a stream code to watch.

## Quick Start

### Prerequisites

1. **uv** (for Python backend)
2. **Tuist** (for iOS project management) - Recommended via [mise](https://mise.jdx.dev/)
3. **Docker** (optional, for containerization)

### Setup

```bash
make setup
```

### Development

| Command | Description |
|---------|-------------|
| `make backend-dev` | Start FastAPI server on http://localhost:8000 |
| `make ios-open` | Open the iOS workspace in Xcode |
| `make ios-generate` | Regenerate iOS project files |
| `make help` | List all available commands |

### Architecture

- **Backend**: FastAPI (Python 3.12+), managed by uv
- **iOS**: SwiftUI (iOS 17+), managed by Tuist
- **Media Server**: NGINX-RTMP (Phase 2)
