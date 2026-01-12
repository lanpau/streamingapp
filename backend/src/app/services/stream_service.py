from datetime import datetime, timezone
import random
import string
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.stream import Stream


async def generate_unique_code(db: AsyncSession) -> str:
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Check if code is already in use by an active stream
        result = await db.execute(
            select(Stream).where(Stream.stream_code == code, Stream.status == "active")
        )
        if result.scalar_one_or_none() is None:
            return code


async def create_stream(db: AsyncSession, device_id: str) -> Stream:
    # Check if this device already has an active stream
    result = await db.execute(
        select(Stream).where(Stream.streamer_device_id == device_id, Stream.status == "active")
    )
    existing_stream = result.scalar_one_or_none()
    
    if existing_stream:
        return existing_stream
    
    # Generate code and create new stream
    stream_code = await generate_unique_code(db)
    
    # Mock URLs for now - will be integrated with MediaMTX later if needed
    # Usually: rtmp://server/app/stream_code
    rtmp_url = f"rtmp://localhost/live/{stream_code}"
    hls_url = f"http://localhost:8888/live/{stream_code}/index.m3u8"
    
    new_stream = Stream(
        streamer_device_id=device_id,
        stream_code=stream_code,
        rtmp_url=rtmp_url,
        hls_url=hls_url,
        status="active"
    )
    
    db.add(new_stream)
    await db.commit()
    await db.refresh(new_stream)
    return new_stream


async def stop_stream(db: AsyncSession, stream_id: str) -> Stream:
    result = await db.execute(select(Stream).where(Stream.id == stream_id))
    stream = result.scalar_one_or_none()
    
    if not stream:
        raise ValueError("Stream not found")
    
    stream.status = "ended"
    stream.ended_at = datetime.now(timezone.utc)
    
    await db.commit()
    await db.refresh(stream)
    return stream


async def get_stream(db: AsyncSession, stream_id: str) -> Stream | None:
    result = await db.execute(select(Stream).where(Stream.id == stream_id))
    return result.scalar_one_or_none()


async def get_stream_by_code(db: AsyncSession, code: str) -> Stream | None:
    result = await db.execute(
        select(Stream).where(Stream.stream_code == code, Stream.status == "active")
    )
    return result.scalar_one_or_none()
