import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_api_create_stream(async_client: AsyncClient):
    headers = {"X-Device-ID": "api-device-1"}
    response = await async_client.post("/api/v1/streams/", json={}, headers=headers)
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["streamer_device_id"] == "api-device-1"
    assert "stream_code" in data
    assert data["status"] == "active"


@pytest.mark.asyncio
async def test_api_get_stream(async_client: AsyncClient):
    # First create
    headers = {"X-Device-ID": "api-device-2"}
    create_res = await async_client.post("/api/v1/streams/", json={}, headers=headers)
    stream_id = create_res.json()["id"]
    
    # Then get
    response = await async_client.get(f"/api/v1/streams/{stream_id}")
    assert response.status_code == 200
    assert response.json()["id"] == stream_id


@pytest.mark.asyncio
async def test_api_stop_stream(async_client: AsyncClient):
    # First create
    headers = {"X-Device-ID": "api-device-3"}
    create_res = await async_client.post("/api/v1/streams/", json={}, headers=headers)
    stream_id = create_res.json()["id"]
    
    # Then stop
    response = await async_client.post(f"/api/v1/streams/{stream_id}/stop", headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "ended"
    assert response.json()["ended_at"] is not None
