from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.db import get_session
from src.repositories.db.items import ItemRepository


def get_item_repository(
        session: AsyncSession = Depends(get_session)
) -> ItemRepository:
    """
    Constructs an ItemRepository instance with injected AsyncSession.
    """
    return ItemRepository(session)
