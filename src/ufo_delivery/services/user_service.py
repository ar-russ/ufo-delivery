from ufo_delivery.models.db.users import User, Address
from ufo_delivery.models.dto.users import (
    UserDTO,
    AddressDTO,
    EditAddress,
    CreateUser,
    EditUser,
)
from ufo_delivery.repositories.db.users import UserRepository
from ufo_delivery.core.security import AuthenticationManager
from ufo_delivery.core.exceptions import UserAlreadyExistsException, UserNotFound
from ufo_delivery.utils.dto_utils import is_empty, dump_non_null_fields


class UserService:
    def __init__(self, repository: UserRepository, auth_manager: AuthenticationManager):
        self._repository = repository
        self._auth_manager = auth_manager

    async def get(self, user_id: int) -> UserDTO | None:
        """
        Get User from database with given ID.
        Returns:
            UserDTO representing User if found, otherwise None.
        """
        user = await self._repository.get(user_id)
        if not user:
            return None

        return user.to_dto()

    async def get_by_phone(self, phone: str) -> UserDTO | None:
        """
        Get User from database with given phone.
        Returns:
            UserDTO representing User if found, otherwise None.
        """
        user = await self._repository.get_by_phone(phone)
        if not user:
            return None

        return user.to_dto()

    async def add(self, data: CreateUser) -> UserDTO:
        """
        Creates new User. UserAlreadyExistsException will be
        raised if phone number given in data is already in use.

        Args:
            data: CreateUser model containing data mandatory for creating a new User.

        Returns: UserDTO model representing created User.

        """
        user = await self.get_by_phone(data.phone)
        if user:
            raise UserAlreadyExistsException

        hashed_password = self._auth_manager.hash_password(data.password)
        data.password = hashed_password

        user = User(
            name=data.name,
            password=data.password,
            phone=data.phone,
            address=Address(street=None, reference=None),
        )

        await self._repository.add(user)
        await self._repository.session.commit()
        await self._repository.session.refresh(user)

        return user.to_dto()

    async def edit(self, user_id: int, data: EditUser) -> UserDTO:
        """
        Edit User data.

        Args:
            user_id: ID of User to edit data for.
            data: EditUser model containing data for editing a User.

        Returns:
            UserDTO representing edited User.
        """
        user = await self._repository.get(user_id)
        if not user:
            raise UserNotFound

        if is_empty(data):
            return user.to_dto()

        if data.password:
            hashed_password = self._auth_manager.hash_password(data.password)
            data.password = hashed_password

        updated_user = await self._repository.update(user_id, dump_non_null_fields(data))
        await self._repository.session.commit()

        return updated_user.to_dto()

    async def get_address(self, user_id: int) -> AddressDTO:
        """
        Get Address of User with given ID.
        Args:
            user_id: ID of User whose Address should be retrieved.

        Returns:
            AddressDTO representing Adress.
        """
        address = await self._repository.get_address(user_id)
        return address.to_dto()

    async def edit_address(self, user_id: int, data: EditAddress) -> AddressDTO:
        """
        Edit Address of User with given ID.
        Args:
            user_id: ID of User whose Address should be edited.
            data: EditAddress model containing data mandatory for editing an Address

        Returns:
            AddressDTO representing edited Address.
        """
        user = await self._repository.get(user_id)
        if not user:
            raise UserNotFound

        if is_empty(data):
            return user.address.to_dto()

        updated_addres = await self._repository.update_address(user_id, dump_non_null_fields(data))
        await self._repository.session.commit()

        return updated_addres.to_dto()
