# pylint: disable=unused-argument
from fastapi import APIRouter, Depends

from src.core.dependencies.auth.user import get_current_user
from src.core.dependencies.services.order_service import get_order_service
from src.services.order_service import OrderService
from src.models.dto.users import UserDTO
from src.models.dto.orders import OrderDTO, AddItemToOrder, RemoveItemFromOrder


router = APIRouter(
    prefix="/order",
    tags=["Orders"],
)


@router.get("", summary="Get current user's Order")
async def get_order(
        user: UserDTO = Depends(get_current_user),
        order_service: OrderService = Depends(get_order_service),
) -> OrderDTO:
    """
    Get Order of current user.
    Args:
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        order_service: Injected business logic layer handling Order operations.

    Returns:
        OrderDTO representing Order.
    """
    order = await order_service.get(user.id)
    return order


@router.put("/add-item", summary="Add Item to current user's Order")
async def add_item_to_order(
        data: AddItemToOrder,
        user: UserDTO = Depends(get_current_user),
        order_service: OrderService = Depends(get_order_service),
) -> OrderDTO:
    """
    Add Item to current user's Order.
    Args:
        data: AddItemToOrder model containing data mandatory for adding Item to Order.
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        order_service: Injected business logic layer handling Order operations.

    Returns:
        OrderDTO representing Order with added Item.
    """
    order = await order_service.get(user.id)
    return await order_service.add_item_to_order(order.id, user.id, data)


@router.put("/remove-item", summary="Remove Item from current user's Order")
async def remove_item_from_order(
        data: RemoveItemFromOrder,
        user: UserDTO = Depends(get_current_user),
        order_service: OrderService = Depends(get_order_service),
) -> OrderDTO:
    """
    Remove Item from current user's Order.
    Args:
        data: RemoveItemToOrder model containing data mandatory for removing Item from Order.
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        order_service: Injected business logic layer handling Order operations.

    Returns:
        OrderDTO representing Order without removed Item.
    """
    order = await order_service.get(user.id)
    return await order_service.remove_item_from_order(order.id, data)


@router.post("/place", summary="Place current user's Order")
async def place_order(
        user: UserDTO = Depends(get_current_user),
        order_service: OrderService = Depends(get_order_service),
) -> OrderDTO:
    """
    Mark current user's Order as placed.
    Args:
        user: Dependency Injection responsible for
            extracting User data from Authorization header.
        order_service: Injected business logic layer handling Order operations.

    Returns:
        OrderDTO representing placed Order.
    """
    return await order_service.place_order(user.id)
