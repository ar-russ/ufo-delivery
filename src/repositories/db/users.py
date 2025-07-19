from sqlalchemy import select, update as sql_update

from src.models.db.users import User, Address
from src.repositories.db.base import BaseSQLAlchemyRepository


class UserRepository(BaseSQLAlchemyRepository):
    async def add(self, model: User) -> None:
        self.session.add(model)

    async def get(self, id_: int) -> User | None:
        statement = select(User).where(User.id == id_)
        return await self.session.scalar(statement)

    async def get_by_phone(self, phone: str) -> User | None:
        """
        Get User with given phone number.

        Returns:
            User model instance if found, otherwise None
        """
        statement = select(User).where(User.phone == phone)
        return await self.session.scalar(statement)

    async def update(self, id_: int, updated_data: dict) -> User:
        statement = sql_update(User).where(User.id == id_).values(**updated_data)
        await self.session.execute(statement)
        return await self.get(id_)

    async def delete(self, id_: int) -> None:
        pass

    async def get_address(self, user_id: int) -> Address:
        """
        Get Address of User with given ID.
        Returns:
            Address model instance.
        """
        statement = select(Address).where(Address.user_id == user_id)
        return await self.session.scalar(statement)

    async def update_address(self, user_id: int, updated_data: dict) -> Address:
        """
        Update Address of User with given ID.
        Args:
            user_id: ID of User whose Address should be updated.
            updated_data: Dictionary with updated Address data.

        Returns:
            Updated Address model instance.
        """
        statement = sql_update(Address).where(Address.user_id == user_id).values(**updated_data)
        await self.session.execute(statement)
        return await self.get_address(user_id)
