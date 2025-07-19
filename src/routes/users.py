from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.models.dto.users import (
    LoginCredentials,
    LoginResponse,
    UserDTO,
    CreateUser,
    EditUser,
    AddressDTO,
    EditAddress,
)
from src.core.dependencies.auth.user import get_current_user
from src.core.dependencies.services.auth_service import get_auth_service
from src.core.dependencies.services.user_service import get_user_service
from src.services.auth_service import AuthService
from src.services.user_service import UserService

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post("/create", summary="Create new user")
async def create_user(
        user_data: CreateUser,
        user_service: UserService = Depends(get_user_service),
) -> UserDTO:
    """
    Create new User instance.

    Args:
        user_data: CreateUser model containing data mandatory for creating a new User.
        user_service:  Injected business logic layer handling User operations.

    Returns:
        UserDTO representing edited User.
    """
    user = await user_service.add(user_data)
    return user


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


@router.get("", summary="Get current user's information")
async def get_user(user: UserDTO = Depends(get_current_user)):
    """
    Get User from Authorization header.

    Args:
        user: Dependency Injection responsible for
            extracting User data from Authorization header.

    Returns:
        UserDTO representing authenticated user.
    """
    return user


@router.put("", summary="Edit current user's information")
async def edit_user(
        edited_data: EditUser,
        user: UserDTO = Depends(get_current_user),
        user_service: UserService = Depends(get_user_service),
) -> UserDTO:
    """
    Edit User data.

    Args:
        edited_data: EditUser model containing data for editing a User.
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        user_service:  Injected business logic layer handling User operations.

    Returns:
        UserDTO representing edited User.
    """
    user = await user_service.edit(user.id, edited_data)
    return user


@router.get("/address", summary="Get current user's address")
async def get_address(
        user: UserDTO = Depends(get_current_user),
        user_service: UserService = Depends(get_user_service)
) -> AddressDTO:
    """
    Get current user's Address.
    Args:
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        user_service:  Injected business logic layer handling User operations.

    Returns:
        AddressDTO representing Address.
    """
    address = await user_service.get_address(user.id)
    return address


@router.put("/address", summary="Edit current user's address")
async def edit_address(
        address_data: EditAddress,
        user: UserDTO = Depends(get_current_user),
        user_service: UserService = Depends(get_user_service)
) -> AddressDTO:
    """
    Edit current user's Address.
    Args:
        address_data: EditAddress model containing data mandatory for editing an Address.
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        user_service:  Injected business logic layer handling User operations.

    Returns:
        AddressDTO representing edited Address.
    """

    address = await user_service.edit_address(user.id, address_data)
    return address
