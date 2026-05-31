from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import uuid

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class DeviceBindRequest(BaseModel):
    device_uuid: str
    device_name: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    role: str

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    role: str

    @field_validator("id", mode="before")
    @classmethod
    def coerce_uuid(cls, v):
        return str(v)