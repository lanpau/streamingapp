import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.device import Device


@pytest.mark.asyncio
async def test_create_stream_no_header(async_client: AsyncClient):
    # Should fail because X-Device-ID header is missing
    response = await async_client.post("/api/v1/streams/", json={})
    assert response.status_code == 422  # FastAPI validation error if we make it required


@pytest.mark.asyncio
async def test_create_stream_auto_creates_device(async_client: AsyncClient, db_session: AsyncSession):
    device_id = "test-device-auto-create"
    headers = {"X-Device-ID": device_id}
    
    # Create stream
    response = await async_client.post("/api/v1/streams/", json={}, headers=headers)
    assert response.status_code == 201
    
    # Verify device exists in DB
    result = await db_session.execute(select(Device).where(Device.device_id == device_id))
    device = result.scalar_one_or_none()
    assert device is not None
    assert device.device_id == device_id


@pytest.mark.asyncio
async def test_stop_stream_wrong_device(async_client: AsyncClient):
    # Create stream with device A
    device_a = "device-a"
    headers_a = {"X-Device-ID": device_a}
    create_res = await async_client.post("/api/v1/streams/", json={}, headers=headers_a)
    stream_id = create_res.json()["id"]
    
    # Try to stop with device B
    device_b = "device-b"
    headers_b = {"X-Device-ID": device_b}
    response = await async_client.post(f"/api/v1/streams/{stream_id}/stop", headers=headers_b)
    
    assert response.status_code == 403
    assert "Forbidden" in response.json()["detail"]


@pytest.mark.asyncio
async def test_stop_stream_correct_device(async_client: AsyncClient):
    # Create stream with device A
    device_a = "device-a-stop"
    headers_a = {"X-Device-ID": device_a}
    create_res = await async_client.post("/api/v1/streams/", json={}, headers=headers_a)
    stream_id = create_res.json()["id"]
    
    # Stop with device A
    response = await async_client.post(f"/api/v1/streams/{stream_id}/stop", headers=headers_a)
    
    assert response.status_code == 200
    assert response.json()["status"] == "ended"
