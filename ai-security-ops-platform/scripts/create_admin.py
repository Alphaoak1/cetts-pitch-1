import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.core.security import get_password_hash
import os

async def main():
    engine = create_async_engine(os.getenv("DATABASE_URL"))
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        admin = User(
            email="admin@example.com",
            full_name="Admin",
            hashed_password=get_password_hash("admin123"),
            role="admin",
            is_active=True
        )
        session.add(admin)
        await session.commit()
        print("Admin created")
asyncio.run(main())