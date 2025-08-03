# pylint: disable=unused-argument
from fastapi import APIRouter, Depends

from ufo_delivery.core.dependencies.services.item_service import get_item_service
from ufo_delivery.core.dependencies.auth.user import get_current_superuser
from ufo_delivery.services.item_service import ItemService
from ufo_delivery.models.dto.users import UserDTO
from ufo_delivery.models.dto.items import (
    ItemDTO,
    CreateItem,
    EditItem,
    DeleteItemResponse,
    CategoryDTO,
)

router = APIRouter(
    prefix="/item",
    tags=["Items"],
)


@router.get("/items", summary="Get Items")
async def get_items(
        category_id: int | None = None,
        item_service: ItemService = Depends(get_item_service),
) -> list[ItemDTO]:
    """
    Get all Items. Items in corresponding Category will
    be returned if category_id is specified.
    Args:
        category_id: ID of category to get Items from.
        item_service: Injected business logic layer handling Item operations.

    Returns:
        List of ItemDTOs representing Items.
    """
    items = await item_service.get_all(category_id)
    return items


@router.get("/categories", summary="Get Categories")
async def get_categories(
        item_service: ItemService = Depends(get_item_service),
) -> list[CategoryDTO]:
    """
    Get all Categories.
    Args:
        item_service: Injected business logic layer handling Item operations.

    Returns:
        List of CategoryDTOs representing Categories.
    """
    categories = await item_service.get_all_categories()
    return categories


@router.get("/{item_id}", summary="Get Item by ID")
async def get_item(
        item_id: int,
        item_service: ItemService = Depends(get_item_service)
) -> ItemDTO:
    """
    Get Item by given ID.

    Args:
        item_id: ID of Item to retrieve.
        item_service: Injected business logic layer handling Item operations.

    Returns:
        ItemDTO representing Item instance.
    """
    item = await item_service.get(item_id)
    return item


@router.post("", summary="Create new Item")
async def create_item(
        item_data: CreateItem,
        item_service: ItemService = Depends(get_item_service),
        user: UserDTO = Depends(get_current_superuser)
) -> ItemDTO:
    """
    Create new Item instance.

    Args:
        item_data: CreateItem model containing data mandatory for creating a new Item.
        item_service: Injected business logic layer handling Item operations.

    Returns:
        ItemDTO representing created Item.

    """
    item = await item_service.add(item_data)
    return item


@router.put("/{item_id}", summary="Edit Item information")
async def edit_item(
        item_id: int,
        edited_data: EditItem,
        item_service: ItemService = Depends(get_item_service),
        user: UserDTO = Depends(get_current_superuser)
) -> ItemDTO:
    """
    Edit Item data.

    Args:
        item_id: ID of Item to edit.
        edited_data: EditUser model containing data for editing a User.
        item_service:  Injected business logic layer handling Item operations.
        user: Dependency Injection responsible for
            extracting User with superuser rights from Authorization header.

    Returns:
        UserDTO representing edited User.
    """
    item = await item_service.edit(item_id, edited_data)
    return item


@router.delete("/{item_id}", summary="Delete Item")
async def delete_item(
        item_id: int,
        item_service: ItemService = Depends(get_item_service),
        user: UserDTO = Depends(get_current_superuser)
) -> DeleteItemResponse:
    """
    Delete Item with given ID.

    Args:
        item_id: ID of Item to delete.
        item_service:  Injected business logic layer handling Item operations.
        user: Dependency Injection responsible for
            extracting User with superuser rights from Authorization header.

    Returns:
        DeleteItemResponse model.
    """
    await item_service.delete(item_id)
    return DeleteItemResponse(success=True)
