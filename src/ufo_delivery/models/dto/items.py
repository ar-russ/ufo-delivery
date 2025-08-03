from pydantic import BaseModel


class CategoryDTO(BaseModel):
    id: int
    name: str


class ItemDTO(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_path: str
    categories: list[CategoryDTO]
    is_available: bool


class CreateItem(BaseModel):
    name: str
    description: str
    price: float
    image_path: str
    categories: list[int]
    is_available: bool = True


class EditItem(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    image_path: str | None = None
    categories: list[int] | None = None
    is_available: bool | None = None


class DeleteItemResponse(BaseModel):
    success: bool = True
