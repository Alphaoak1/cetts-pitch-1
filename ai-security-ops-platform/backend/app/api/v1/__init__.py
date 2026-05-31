from fastapi import APIRouter
from app.api.v1.endpoints import auth, incidents, media, sync, dashboard, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(incidents.router, prefix="/incidents", tags=["incidents"])
api_router.include_router(media.router, prefix="/media", tags=["media"])
api_router.include_router(sync.router, prefix="/sync", tags=["sync"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(users.router, prefix="/users", tags=["users"])