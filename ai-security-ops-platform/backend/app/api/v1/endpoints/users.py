from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.repositories.user_repo import UserRepository
from app.schemas.auth import UserCreate, UserResponse
from app.api.v1.endpoints.auth import oauth2_scheme

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    repo = UserRepository(db)
    return await repo.create(user)