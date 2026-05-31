from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.sync import SyncPayload
from app.services.incident_service import IncidentService

class SyncService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.incident_service = IncidentService(db)

    async def process_sync(self, payload: SyncPayload, token: str):
        results = []
        for inc in payload.incidents:
            # check for duplicate using client_incident_id
            # simplified: just create
            created = await self.incident_service.create(inc, token)
            results.append({"client_id": inc.client_incident_id, "server_id": str(created.id)})
        return {"synced": results}