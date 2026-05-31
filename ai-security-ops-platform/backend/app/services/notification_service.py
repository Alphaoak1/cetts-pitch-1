from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.incident_repo import IncidentRepository

class NotificationService:
    def __init__(self, db: AsyncSession):
        self.incident_repo = IncidentRepository(db)

    async def get_recent_incidents(self, token: str):
        return await self.incident_repo.get_all(0, 20)