import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.device import Device
from app.models.stream import Stream

@pytest.mark.anyio
async def test_db_fixtures_work(db_session: AsyncSession):
    # Create a device
    device = Device(device_id="test-device-id")
    db_session.add(device)
    await db_session.commit()
    
    # Query the device
    result = await db_session.execute(select(Device).where(Device.device_id == "test-device-id"))
    db_device = result.scalar_one()
    assert db_device.device_id == "test-device-id"
    
    # Create a stream
    stream = Stream(
        id="test-stream-id",
        streamer_device_id="test-device-id",
        stream_code="test-code",
        rtmp_url="rtmp://test",
        hls_url="http://test/hls",
        status="active"
    )
    db_session.add(stream)
    await db_session.commit()
    
    # Query the stream
    result = await db_session.execute(select(Stream).where(Stream.id == "test-stream-id"))
    db_stream = result.scalar_one()
    assert db_stream.id == "test-stream-id"
    assert db_stream.stream_code == "test-code"
