from sqlalchemy import Column, String, DateTime, func, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    action = Column(String(100))
    resource_type = Column(String(50))
    resource_id = Column(UUID(as_uuid=True))
    ip_address = Column(BigInteger)  # store as inet
    user_agent = Column(String)
    created_at = Column(DateTime, server_default=func.now())