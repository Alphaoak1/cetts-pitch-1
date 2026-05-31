from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.notification_service import NotificationService
from app.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()

@router.get("/incidents/recent")
async def recent_incidents(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    service = NotificationService(db)
    return await service.get_recent_incidents(token)

@router.websocket("/ws/notifications")
async def websocket_notifications(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # broadcast logic would go here (simplified)
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        pass