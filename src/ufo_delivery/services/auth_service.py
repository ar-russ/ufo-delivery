from ufo_delivery.models.dto.users import LoginCredentials
from ufo_delivery.repositories.db.users import UserRepository
from ufo_delivery.core.exceptions import InvalidCredentialsException
from ufo_delivery.core.security import AuthenticationManager


class AuthService:
    def __init__(
            self,
            user_repository: UserRepository,
            auth_manager: AuthenticationManager,
    ):
        self._user_repository = user_repository
        self._auth_manager = auth_manager

    async def login(self, credentials: LoginCredentials) -> str:
        """
        Authenticates given credentials. InvalidCredentialsException
        will be raised if authentication process failed.
        Args:
            credentials: LoginCredentials model containing data mandatory for authentication.

        Returns:
            Generated JWT Token.
        """
        is_authenticated = await self._is_user_authenticated(
            credentials.phone,
            credentials.password
        )
        if not is_authenticated:
            raise InvalidCredentialsException

        return self._auth_manager.create_access_token({"sub": credentials.phone})

    async def _is_user_authenticated(self, phone: str, password: str) -> bool:
        user = await self._user_repository.get_by_phone(phone)
        if not user:
            return False

        if not self._auth_manager.is_password_valid(password, user.password):
            return False

        return True
