from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from ufo_delivery.models.db.base import Base


class BaseSQLAlchemyRepository(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def add(self, model: Base) -> None:
        """
        Adds given model to the current database session.
        This method does not commit the session - this should be done by caller.
        """
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: int) -> Base | None:
        """
        Get SQLAlchemy model instance from database.
        Args:
            id_: ID of the model to retrieve.

        Returns:
            SQLAlchemy model inherited from Base if found, otherwise None.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, id_: int, updated_data: dict) -> Base:
        """
        Update SQLAchemy model.
        This method does not commit the session - this should be done by caller.
        Args:
            id_: ID of the model to update.
            updated_data: Dictionary containing keys and values to update in model.

        Returns:
            Changed SQLAlchemy model instance before commit.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id_: int) -> None:
        """
        Delete SQlAlchemy model instance from database.
        This method does not commit the session - this should be done by caller.

        Args:
            id_: ID of the model to delete.
        """
        raise NotImplementedError
