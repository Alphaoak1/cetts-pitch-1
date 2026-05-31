from sqlalchemy.ext.asyncio import AsyncSession
from app.models.media import Media

class MediaRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, media: Media) -> Media:
        self.db.add(media)
        await self.db.commit()
        await self.db.refresh(media)
        return media