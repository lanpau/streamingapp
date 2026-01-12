from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.schemas.stream import StreamCreate, StreamResponse
from app.services import stream_service

router = APIRouter(prefix="/streams", tags=["streams"])


@router.post("/", response_model=StreamResponse, status_code=status.HTTP_201_CREATED)
async def create_stream(
    stream_in: StreamCreate, db: AsyncSession = Depends(get_db)
):
    return await stream_service.create_stream(db, stream_in.streamer_device_id)


@router.get("/{stream_id}", response_model=StreamResponse)
async def get_stream(stream_id: str, db: AsyncSession = Depends(get_db)):
    stream = await stream_service.get_stream(db, stream_id)
    if not stream:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Stream not found"
        )
    return stream


@router.post("/{stream_id}/stop", response_model=StreamResponse)
async def stop_stream(stream_id: str, db: AsyncSession = Depends(get_db)):
    try:
        return await stream_service.stop_stream(db, stream_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)
        )
