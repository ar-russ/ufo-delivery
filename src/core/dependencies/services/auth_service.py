from fastapi import Depends

from src.services.auth_service import AuthService
from src.repositories.db.users import UserRepository
from src.core.security import AuthenticationManager
from src.core.dependencies.auth.authentication_manager import get_authentication_manager
from src.core.dependencies.repositories.user_repository import get_user_repository


def get_auth_service(
        user_repository: UserRepository = Depends(get_user_repository),
        authentication_manager: AuthenticationManager = Depends(get_authentication_manager)
) -> AuthService:
    """
    Constructs an AuthService instance with injected UserRepository and AuthenticationManager.
    """
    return AuthService(user_repository, authentication_manager)
