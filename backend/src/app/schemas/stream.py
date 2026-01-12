from datetime import datetime
from pydantic import BaseModel, ConfigDict


class StreamBase(BaseModel):
    stream_code: str
    rtmp_url: str
    hls_url: str


class StreamCreate(BaseModel):
    pass


class StreamUpdate(BaseModel):
    status: str
    ended_at: datetime | None = None


class StreamResponse(StreamBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    streamer_device_id: str
    status: str
    started_at: datetime
    ended_at: datetime | None = None
