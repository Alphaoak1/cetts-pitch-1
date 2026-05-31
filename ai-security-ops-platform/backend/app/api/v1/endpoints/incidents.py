from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.core.database import get_db
from app.services.incident_service import IncidentService
from app.schemas.incident import IncidentCreate, IncidentResponse, IncidentUpdate
from app.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()

@router.post("/", response_model=IncidentResponse)
async def create_incident(
    incident: IncidentCreate,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    service = IncidentService(db)
    return await service.create(incident, token)

@router.get("/", response_model=List[IncidentResponse])
async def list_incidents(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    service = IncidentService(db)
    return await service.get_all(skip, limit, token)

@router.get("/{incident_id}", response_model=IncidentResponse)
async def get_incident(incident_id: str, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    service = IncidentService(db)
    return await service.get_by_id(incident_id, token)

@router.put("/{incident_id}")
async def update_incident(incident_id: str, update: IncidentUpdate, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    service = IncidentService(db)
    return await service.update(incident_id, update, token)