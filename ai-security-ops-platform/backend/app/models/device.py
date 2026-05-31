from sqlalchemy import Column, String, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    device_uuid = Column(String(255), unique=True, nullable=False)
    device_name = Column(String(255))
    last_seen_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())