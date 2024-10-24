from app.models import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from app.schemas.auth_schema import UserLogin


class AuthCrud:
    async def get_by_email(
        self,
        async_session: async_sessionmaker[AsyncSession],
        email: str,
    ):
        async with async_session() as session:
            statement = select(User).filter(User.email == email)
            result = await session.execute(statement)
            return result.scalars().one_or_none()
