# Discovery: Phase 2 - Media Server

## Decision: Media Server Selection

**Verdict:** Selected **MediaMTX** (formerly `rtsp-simple-server`).

### Options Considered

1.  **nginx-rtmp**
    *   **Pros:** Standard, very stable, widely used.
    *   **Cons:** Configuration can be verbose, requires compilation for advanced features (or finding the right Docker image), older architecture.
    *   **Fit:** Good fallback, but less feature-rich out of the box for modern protocols.

2.  **SRS (Simple Key Server)**
    *   **Pros:** High performance, extensive feature set, low latency focus.
    *   **Cons:** Documentation can be complex (translated), "Swiss-army knife" might be overkill for MVP.
    *   **Fit:** Strong contender, but slightly higher learning curve.

3.  **MediaMTX**
    *   **Pros:**
        *   **Zero Dependency:** Single Go binary (or simple Docker image).
        *   **Modern Protocols:** Native support for RTMP, HLS, LL-HLS, WebRTC, SRT.
        *   **Configuration:** Simple YAML file (`mediamtx.yml`).
        *   **Active Development:** strong community momentum.
    *   **Cons:** Newer than nginx-rtmp (though stable).
    *   **Fit:** **Best.** Perfect for a "self-hosted" MVP that needs to bear minimal operational burden while supporting critical features like HLS/LL-HLS for the viewer.

### Implementation Strategy

We will use the official Docker image `bluenviron/mediamtx:latest` (formerly `aler9/rtsp-simple-server`).

**Architecture:**
*   **Ingest:** RTMP on port 1935 (Streamer -> MediaMTX)
*   **Playback:** HLS on port 8888 (MediaMTX -> Viewer)
*   **Mode:** Start with standard HLS. Can switch to LL-HLS via config if latency > 20s.

**Why Docker?**
*   Matches our "hard constraint" for local dev environment consistency.
*   Easy deployment to VPS later (just `docker compose up`).
