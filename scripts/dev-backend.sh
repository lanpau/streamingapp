#!/bin/bash
set -e

# Default values
HOST="${STREAMLIVE_HOST:-0.0.0.0}"
PORT="${STREAMLIVE_PORT:-8000}"

echo "🚀 Starting Backend Server on http://$HOST:$PORT"
cd backend
uv run uvicorn app.main:app --host "$HOST" --port "$PORT" --reload
