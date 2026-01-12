from typing import Annotated
from fastapi import Header, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import get_db
from app.models.device import Device


async def get_current_device(
    x_device_id: Annotated[str | None, Header()] = None,
    db: AsyncSession = Depends(get_db)
) -> str:
    if not x_device_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="X-Device-ID header is missing"
        )
    
    # Check if device exists
    result = await db.execute(select(Device).where(Device.device_id == x_device_id))
    device = result.scalar_one_or_none()
    
    if not device:
        # Auto-registration
        device = Device(device_id=x_device_id)
        db.add(device)
        await db.commit()
        await db.refresh(device)
        
    return x_device_id
