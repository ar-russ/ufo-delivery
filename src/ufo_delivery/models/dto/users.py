from pydantic import BaseModel


class AddressDTO(BaseModel):
    street: str | None
    reference: str | None


class UserDTO(BaseModel):
    id: int
    name: str
    phone: str
    password: str
    address: AddressDTO | None
    is_superuser: bool


class CreateUser(BaseModel):
    name: str
    phone: str
    password: str


class EditUser(BaseModel):
    name: str | None = None
    phone: str | None = None
    password: str | None = None


class EditAddress(BaseModel):
    street: str
    reference: str


class LoginCredentials(BaseModel):
    phone: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
