from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router
from app.core.config import settings
from app.core.database import engine
from app.models import Base

app = FastAPI(title="AI Security Ops API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"}