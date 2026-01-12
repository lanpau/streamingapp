import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.stream_service import create_stream, stop_stream, get_stream
from app.models.stream import Stream


@pytest.mark.asyncio
async def test_create_stream_generates_unique_code(db_session: AsyncSession):
    device_id = "test-device-1"
    stream = await create_stream(db_session, device_id)
    
    assert stream.streamer_device_id == device_id
    assert stream.stream_code is not None
    assert stream.status == "active"
    assert stream.rtmp_url.startswith("rtmp://")
    assert stream.hls_url.endswith(".m3u8")


@pytest.mark.asyncio
async def test_create_stream_reuses_active_stream(db_session: AsyncSession):
    device_id = "test-device-2"
    stream1 = await create_stream(db_session, device_id)
    stream2 = await create_stream(db_session, device_id)
    
    assert stream1.id == stream2.id
    assert stream1.stream_code == stream2.stream_code


@pytest.mark.asyncio
async def test_stop_stream(db_session: AsyncSession):
    device_id = "test-device-3"
    stream = await create_stream(db_session, device_id)
    
    stopped_stream = await stop_stream(db_session, stream.id)
    
    assert stopped_stream.status == "ended"
    assert stopped_stream.ended_at is not None


@pytest.mark.asyncio
async def test_get_stream(db_session: AsyncSession):
    device_id = "test-device-4"
    stream = await create_stream(db_session, device_id)
    
    fetched_stream = await get_stream(db_session, stream.id)
    
    assert fetched_stream.id == stream.id
    assert fetched_stream.stream_code == stream.stream_code
