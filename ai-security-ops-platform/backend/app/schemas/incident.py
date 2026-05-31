from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional, Dict, Any

class IncidentCreate(BaseModel):
    client_incident_id: Optional[str] = None
    incident_type: Optional[str] = None
    location: Optional[Dict[str, Any]] = None
    occurred_at: datetime
    transcript: Optional[str] = None
    summary: Optional[str] = None
    structured_data: Optional[Dict[str, Any]] = None
    status: Optional[str] = "draft"

class IncidentUpdate(BaseModel):
    status: Optional[str] = None
    summary: Optional[str] = None

class IncidentResponse(BaseModel):
    id: str
    incident_type: Optional[str]
    location: Optional[Dict]
    occurred_at: datetime
    transcript: Optional[str]
    summary: Optional[str]
    status: str

    @field_validator("id", mode="before")
    @classmethod
    def coerce_uuid(cls, v):
        return str(v)