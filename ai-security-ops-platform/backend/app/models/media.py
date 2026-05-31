from sqlalchemy import Column, String, BigInteger, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.database import Base

class Media(Base):
    __tablename__ = "media"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    incident_id = Column(UUID(as_uuid=True), ForeignKey("incidents.id", ondelete="CASCADE"))
    file_path = Column(String(500), nullable=False)
    file_size_bytes = Column(BigInteger)
    mime_type = Column(String(100))
    thumbnail_path = Column(String(500))
    uploaded_at = Column(DateTime, server_default=func.now())