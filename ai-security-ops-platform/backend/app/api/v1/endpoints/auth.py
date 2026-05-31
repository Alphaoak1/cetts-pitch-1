from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.repositories.user_repo import UserRepository
from app.schemas.auth import Token, LoginRequest, DeviceBindRequest
from app.models.device import Device

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.get_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/device/bind")
async def bind_device(request: DeviceBindRequest, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # decode token to get user
    from jose import jwt
    from app.core.config import settings
    payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    email = payload.get("sub")
    user_repo = UserRepository(db)
    user = await user_repo.get_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    device = Device(user_id=user.id, device_uuid=request.device_uuid, device_name=request.device_name)
    db.add(device)
    await db.commit()
    return {"status": "bound"}