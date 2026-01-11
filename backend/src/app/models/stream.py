from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Stream(Base):
    __tablename__ = "streams"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    stream_code: Mapped[str] = mapped_column(String(32), nullable=False)
    rtmp_url: Mapped[str] = mapped_column(String(255), nullable=False)
    hls_url: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")
