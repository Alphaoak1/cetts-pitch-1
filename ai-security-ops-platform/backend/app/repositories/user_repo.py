from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create(self, user_data) -> User:
        hashed = get_password_hash(user_data.password)
        user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=hashed,
            role=user_data.role
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user