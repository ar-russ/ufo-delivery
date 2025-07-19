from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config.config import settings

engine = create_async_engine(settings.database.url)


async def get_session() -> AsyncGenerator[AsyncSession]:
    """
    Yields a fresh SQLAlchemy AsynsSession.
    """
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with session_factory() as session:
        yield session
