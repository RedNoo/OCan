from app.models import Order
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select

class OrderCrud:
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Order).order_by(Order.id)
            result = await session.execute(statement)
            return result.scalars().all()

    async def add(self, async_session: async_sessionmaker[AsyncSession], user: Order):
        async with async_session() as session:
            session.add(user)
            await session.commit()
            return user
    
    async def get_by_id(self, async_session: async_sessionmaker[AsyncSession], id: int):
        async with async_session() as session:
            statement = select(Order).filter(Order.id == id)
            result = await session.execute(statement)
            return result.scalars().one_or_none()

    async def update(
        self, async_session: async_sessionmaker[AsyncSession], id: int, data
    ):
        async with async_session() as session:
            statement = select(Order).filter(Order.id == id)
            result = await session.execute(statement)
            user = result.scalars().one()

            for var, value in vars(data).items():
                setattr(user, var, value) if value else None

            await session.commit()
            return user

    async def delete(self, async_session: async_sessionmaker[AsyncSession], user: Order):
        async with async_session() as session:
            await session.delete(user)
            await session.commit()
            return user
