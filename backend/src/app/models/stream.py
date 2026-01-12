import uuid
from datetime import datetime, timezone
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Stream(Base):
    __tablename__ = "streams"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    streamer_device_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    stream_code: Mapped[str] = mapped_column(String(32), nullable=False)
    rtmp_url: Mapped[str] = mapped_column(String(255), nullable=False)
    hls_url: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")
    started_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
