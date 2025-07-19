from fastapi import Depends

from src.repositories.db.users import UserRepository
from src.services.user_service import UserService
from src.core.dependencies.repositories.user_repository import get_user_repository
from src.core.dependencies.auth.authentication_manager import get_authentication_manager
from src.core.security import AuthenticationManager


def get_user_service(
        repository: UserRepository = Depends(get_user_repository),
        authentication_manager: AuthenticationManager = Depends(get_authentication_manager),
) -> UserService:
    """
    Constructs a UserService instance with injected UserRepository and AuthenticationManager.
    """
    return UserService(repository, authentication_manager)
