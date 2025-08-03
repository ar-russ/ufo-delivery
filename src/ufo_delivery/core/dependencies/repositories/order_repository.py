from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ufo_delivery.core.dependencies.db import get_session
from ufo_delivery.repositories.db.orders import OrderRepository


def get_order_repository(
        session: AsyncSession = Depends(get_session),
) -> OrderRepository:
    """
    Constructs an OrderRepository instance with injected AsyncSession.
    """
    return OrderRepository(session)
