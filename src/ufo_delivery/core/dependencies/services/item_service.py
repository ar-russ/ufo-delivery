from fastapi import Depends

from ufo_delivery.repositories.db.items import ItemRepository
from ufo_delivery.services.item_service import ItemService
from ufo_delivery.core.dependencies.repositories.item_repository import get_item_repository


def get_item_service(
        repository: ItemRepository = Depends(get_item_repository)
) -> ItemService:
    """
    Constructs an ItemService instance with injected ItemRepository.
    """
    return ItemService(repository)
