from fastapi import APIRouter, Depends

from ufo_delivery.models.dto.users import (
    LoginCredentials,
    LoginResponse,
)
from ufo_delivery.core.dependencies.services.auth_service import get_auth_service
from ufo_delivery.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login", summary="Login to existing account")
async def login(
        credentials: LoginCredentials,
        auth_service: AuthService = Depends(get_auth_service)
) -> LoginResponse:
    """
    Authenticate user with given credentials.

    Args:
        credentials: LoginCredentials model containing data mandatory for authentication.
        auth_service: Injected business logic layer handling authentication.

    Returns:
        LoginResponse model with access_token and token_type.
    """
    access_token = await auth_service.login(credentials)
    return LoginResponse(access_token=access_token)
