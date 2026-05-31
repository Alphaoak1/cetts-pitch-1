from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.media_service import MediaService
from app.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()

@router.post("/upload/{incident_id}")
async def upload_media(
    incident_id: str,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    service = MediaService(db)
    url = await service.upload(file, incident_id, token)
    return {"media_url": url}