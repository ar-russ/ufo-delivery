from jwt import decode
from jwt.exceptions import InvalidTokenError

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ufo_delivery.models.dto.users import UserDTO
from ufo_delivery.core.dependencies.services.user_service import get_user_service
from ufo_delivery.services.user_service import UserService
from ufo_delivery.core.exceptions import InvalidCredentialsException, InsufficientRightsException
from config.config import settings

scheme_factory = HTTPBearer(auto_error=False)


async def get_current_user(
        token: HTTPAuthorizationCredentials = Depends(scheme_factory),
        user_service: UserService = Depends(get_user_service)
) -> UserDTO:
    """
    Retrieves current user from the request's JWT Token.
    InvalidCredentialsException will be raised if token is invalid, expired, or missing.

    Returns:
        UserDTO: DTO object with current authenticated user's data.
    """
    try:
        decoded_token = decode(
            token.credentials,
            key=settings.auth.secret_key,
            algorithms=[settings.auth.algorithm]
        )
        phone = decoded_token.get("sub")
        if not phone:
            raise InvalidCredentialsException
    except InvalidTokenError as exc:
        raise InvalidCredentialsException from exc

    user = await user_service.get_by_phone(phone)
    if not user:
        raise InvalidCredentialsException

    return user


async def get_current_superuser(
        user: UserDTO = Depends(get_current_user)
) -> UserDTO:
    """
    Retrieves current user from the request's JWT Token and ensures it has rights of superuser.

    Raises:
        InvalidCredentialsException will be raised if token is invalid, expired, or missing.
        InsufficientRightsException will be raised if user is not superuser.

    Returns:
        UserDTO: DTO object with current authenticated user's data.
    """
    if not user.is_superuser:
        raise InsufficientRightsException

    return user
