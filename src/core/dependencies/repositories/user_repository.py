from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.db import get_session
from src.repositories.db.users import UserRepository


def get_user_repository(
        session: AsyncSession = Depends(get_session)
) -> UserRepository:
    """
    Constructs a UserRepository instance with injected AsyncSession.
    """
    return UserRepository(session)
