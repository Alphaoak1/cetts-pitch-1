from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
import boto3
from botocore.config import Config
from app.core.config import settings
from app.models.media import Media
import uuid

class MediaService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.s3 = boto3.client(
            "s3",
            endpoint_url=f"http://{settings.MINIO_ENDPOINT}",
            aws_access_key_id=settings.MINIO_ACCESS_KEY,
            aws_secret_access_key=settings.MINIO_SECRET_KEY,
            config=Config(signature_version="s3v4"),
            region_name="us-east-1"
        )

    async def upload(self, file: UploadFile, incident_id: str, token: str) -> str:
        ext = file.filename.split(".")[-1]
        key = f"{incident_id}/{uuid.uuid4()}.{ext}"
        self.s3.upload_fileobj(file.file, settings.MINIO_BUCKET, key)
        url = f"http://{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET}/{key}"
        media = Media(
            incident_id=incident_id,
            file_path=key,
            file_size_bytes=file.size,
            mime_type=file.content_type
        )
        self.db.add(media)
        await self.db.commit()
        return url