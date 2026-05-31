from pydantic import BaseModel
from typing import List, Dict, Any

class SyncIncident(BaseModel):
    client_incident_id: str
    incident_type: str
    location: Dict[str, Any]
    occurred_at: str
    transcript: str

class SyncPayload(BaseModel):
    incidents: List[SyncIncident]
    # media would be handled separately in multipart