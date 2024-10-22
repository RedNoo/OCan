from app.models import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select


class UserCrud:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        print("async", async_session)
        async with async_session() as session:
            statement = select(User).order_by(User.id)
            result = await session.execute(statement)
            return result.scalars().all()

    async def add(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            return user

    async def get_by_id(self, async_session: async_sessionmaker[AsyncSession], id: int):
        async with async_session() as session:
            statement = select(User).filter(User.id == id)
            result = await session.execute(statement)
            return result.scalars().one()

    async def update(
        self, async_session: async_sessionmaker[AsyncSession], id: int, data
    ):
        async with async_session() as session:
            statement = select(User).filter(User.id == id)
            result = await session.execute(statement)
            user = result.scalars().one()

            user.email = data.title
            user.content = data.content

            await session.commit()
            return user

    async def delete(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            await session.delete(user)
            await session.commit()
            return user
