# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy configuration
COPY pyproject.toml .
COPY uv.lock .
COPY README.md .
COPY .python-version .

# Install dependencies (creates .venv)
RUN uv sync --frozen --no-dev

# Runtime stage
FROM python:3.12-slim

WORKDIR /app

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy virtual env from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY src /app/src
COPY pyproject.toml .

# Expose port
EXPOSE 8000

# Set user and default command
USER appuser
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
