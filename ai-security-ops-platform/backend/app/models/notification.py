from sqlalchemy import Column, String, Boolean, DateTime, func, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String(255))
    body = Column(String)
    data = Column(JSON)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())