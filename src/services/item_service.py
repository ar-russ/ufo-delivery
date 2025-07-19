from src.models.db.items import Item
from src.models.dto.items import (
    ItemDTO,
    CreateItem,
    EditItem,
    CategoryDTO,
)
from src.repositories.db.items import ItemRepository
from src.core.exceptions import ItemNotFound
from src.utils.dto_utils import is_empty, dump_non_null_fields


class ItemService:
    def __init__(self, repository: ItemRepository):
        self._repository = repository

    async def get(self, item_id: int) -> ItemDTO:
        """
        Get Item from database.

        Args:
            item_id: ID of the Item to retrieve.

        Returns:
            ItemDTO representing Item if found, otherwise None.
        """
        item = await self._repository.get(item_id)
        if not item:
            raise ItemNotFound

        return item.to_dto()

    async def get_all(self, category_id: int | None = None) -> list[ItemDTO]:
        """
        Get all Items. Items in corresponding Category will
        be returned if category_id is specified.
        Args:
            category_id: ID of category to get Items from.

        Returns:
            List of ItemDTOs representing Items.
        """
        if category_id:
            items = await self._repository.get_all_in_category(category_id)
        else:
            items = await self._repository.get_all()

        return [item.to_dto() for item in items]

    async def get_all_categories(self) -> list[CategoryDTO]:
        """
        Get all Categories.

        Returns:
            List of CategoryDTOs representing Categories.
        """
        categories = await self._repository.get_all_categories()
        return [category.to_dto() for category in categories]

    async def add(self, data: CreateItem) -> ItemDTO:
        """
        Create new Item instance.
        Args:
            data: CreateItem model containing data mandatory for creating a new Item.

        Returns:
            ItemDTO representing created Item.
        """
        categories = await self._repository.get_categories(data.categories)

        item = Item(
            name=data.name,
            description=data.description,
            price=data.price,
            image_path=data.image_path,
            categories=categories,
            is_available=True
        )

        await self._repository.add(item)
        await self._repository.session.commit()
        await self._repository.session.refresh(item)

        return item.to_dto()

    async def edit(self, item_id: int, data: EditItem) -> ItemDTO:
        """
        Edit Item data.

        Args:
            item_id: ID of Item to edit data for.
            data: EditItem model containing data for editing a Item.

        Returns:
            ItemDTO representing edited Item.
        """
        item = await self._repository.get(item_id)
        if not item:
            raise ItemNotFound

        if is_empty(data):
            return item.to_dto()

        updated_item = await self._repository.update(item_id, dump_non_null_fields(data))
        await self._repository.session.commit()

        return updated_item.to_dto()

    async def delete(self, item_id: int) -> None:
        """
        Delete Item with given ID.

        Args:
            item_id: ID of Item to delete.
        """
        item = await self._repository.get(item_id)
        if not item:
            raise ItemNotFound

        await self._repository.delete(item.id)
        await self._repository.session.commit()
