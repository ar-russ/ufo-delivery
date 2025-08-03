from fastapi import Depends

from ufo_delivery.core.dependencies.repositories.order_repository import get_order_repository
from ufo_delivery.core.dependencies.repositories.item_repository import get_item_repository
from ufo_delivery.repositories.db.orders import OrderRepository
from ufo_delivery.repositories.db.items import ItemRepository
from ufo_delivery.services.order_service import OrderService


def get_order_service(
        repository: OrderRepository = Depends(get_order_repository),
        item_repository: ItemRepository = Depends(get_item_repository),
) -> OrderService:
    """
    Constructs an OrderService instance with injected OrderRepository and ItemRepository.
    """
    return OrderService(repository, item_repository)
