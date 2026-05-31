from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.sync_service import SyncService
from app.schemas.sync import SyncPayload
from app.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()

@router.post("/upload")
async def sync_upload(
    payload: SyncPayload,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    service = SyncService(db)
    result = await service.process_sync(payload, token)
    return result