from fastapi import Depends

from src.core.dependencies.repositories.order_repository import get_order_repository
from src.core.dependencies.repositories.item_repository import get_item_repository
from src.repositories.db.orders import OrderRepository
from src.repositories.db.items import ItemRepository
from src.services.order_service import OrderService


def get_order_service(
        repository: OrderRepository = Depends(get_order_repository),
        item_repository: ItemRepository = Depends(get_item_repository),
) -> OrderService:
    """
    Constructs an OrderService instance with injected OrderRepository and ItemRepository.
    """
    return OrderService(repository, item_repository)
