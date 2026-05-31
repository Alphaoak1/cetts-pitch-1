from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.incident_repo import IncidentRepository
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentUpdate
from jose import jwt
from app.core.config import settings
from datetime import datetime

class IncidentService:
    def __init__(self, db: AsyncSession):
        self.repo = IncidentRepository(db)
        self.db = db

    async def create(self, incident_data: IncidentCreate, token: str) -> Incident:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email = payload.get("sub")
        # In real impl you'd get user_id from db
        user_id = "00000000-0000-0000-0000-000000000001"  # placeholder
        incident = Incident(
            client_incident_id=incident_data.client_incident_id,
            user_id=user_id,
            incident_type=incident_data.incident_type,
            location=incident_data.location,
            occurred_at=incident_data.occurred_at,
            transcript=incident_data.transcript,
            summary=incident_data.summary,
            structured_data=incident_data.structured_data,
            status=incident_data.status
        )
        return await self.repo.create(incident)

    async def get_all(self, skip: int, limit: int, token: str):
        return await self.repo.get_all(skip, limit)

    async def get_by_id(self, incident_id: str, token: str):
        return await self.repo.get_by_id(incident_id)

    async def update(self, incident_id: str, update: IncidentUpdate, token: str):
        incident = await self.repo.get_by_id(incident_id)
        if not incident:
            return None
        if update.status:
            incident.status = update.status
        if update.summary:
            incident.summary = update.summary
        await self.db.commit()
        return incident