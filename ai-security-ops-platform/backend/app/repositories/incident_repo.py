from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.incident import Incident

class IncidentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, incident: Incident) -> Incident:
        self.db.add(incident)
        await self.db.commit()
        await self.db.refresh(incident)
        return incident

    async def get_by_id(self, incident_id: str) -> Incident | None:
        result = await self.db.execute(select(Incident).where(Incident.id == incident_id))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int, limit: int, user_id: str = None):
        query = select(Incident)
        if user_id:
            query = query.where(Incident.user_id == user_id)
        query = query.offset(skip).limit(limit).order_by(Incident.occurred_at.desc())
        result = await self.db.execute(query)
        return result.scalars().all()