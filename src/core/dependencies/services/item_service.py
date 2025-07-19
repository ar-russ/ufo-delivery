from fastapi import Depends

from src.repositories.db.items import ItemRepository
from src.services.item_service import ItemService
from src.core.dependencies.repositories.item_repository import get_item_repository


def get_item_service(
        repository: ItemRepository = Depends(get_item_repository)
) -> ItemService:
    """
    Constructs an ItemService instance with injected ItemRepository.
    """
    return ItemService(repository)
