from sqlalchemy import Column, String, Boolean, DateTime, func, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_incident_id = Column(UUID(as_uuid=True), nullable=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    device_id = Column(UUID(as_uuid=True), nullable=True)
    incident_type = Column(String(100))
    location = Column(JSON)
    occurred_at = Column(DateTime, nullable=False)
    transcript = Column(String)
    summary = Column(String)
    structured_data = Column(JSON)
    status = Column(String(50), default="draft")
    is_synced = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())