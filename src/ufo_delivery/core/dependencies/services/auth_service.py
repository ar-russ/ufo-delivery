from fastapi import Depends

from ufo_delivery.services.auth_service import AuthService
from ufo_delivery.repositories.db.users import UserRepository
from ufo_delivery.core.security import AuthenticationManager
from ufo_delivery.core.dependencies.auth.authentication_manager import get_authentication_manager
from ufo_delivery.core.dependencies.repositories.user_repository import get_user_repository


def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository),
        authentication_manager: AuthenticationManager = Depends(get_authentication_manager)
) -> AuthService:
    """
    Constructs an AuthService instance with injected UserRepository and AuthenticationManager.
    """
    return AuthService(user_repository, authentication_manager)
