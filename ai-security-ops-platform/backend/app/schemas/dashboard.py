from pydantic import BaseModel
from datetime import datetime

class RecentIncident(BaseModel):
    id: str
    incident_type: str
    occurred_at: datetime
    summary: str
    status: str