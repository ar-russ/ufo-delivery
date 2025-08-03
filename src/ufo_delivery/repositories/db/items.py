from sqlalchemy import select, update as sql_update

from ufo_delivery.models.db.items import Item, Category
from ufo_delivery.repositories.db.base import BaseSQLAlchemyRepository


class ItemRepository(BaseSQLAlchemyRepository):
    async def add(self, model: Item) -> None:
        self.session.add(model)

    async def get(self, id_: int) -> Item | None:
        statement = select(Item).where(Item.id == id_)
        result = await self.session.scalar(statement)
        return result

    async def update(self, id_: int, updated_data: dict) -> Item:
        categories = updated_data.get("categories")
        if categories:
            item = await self.get(id_)
            item.categories = await self.get_categories(categories)
            updated_data.pop("categories")

        if not updated_data:
            return await self.get(id_)

        statement = sql_update(Item).where(Item.id == id_).values(**updated_data)
        await self.session.execute(statement)
        return await self.get(id_)

    async def delete(self, id_: int) -> None:
        item = await self.get(id_)

        await self.session.delete(item)

    async def get_all(self) -> list[Item]:
        """
        Get all Items from database.
        Returns:
            Items as Item model instances.
        """
        statement = select(Item)
        result = await self.session.scalars(statement)
        return list(result.unique())

    async def get_all_in_category(self, category_id: int) -> list[Item]:
        """
        Get all Items in given category.
        Args:
            category_id: ID of category to get Items from.

        Returns:
            Items as Item model instances.
        """
        statement = select(Item).join(Item.categories).where(Category.id == category_id)
        result = await self.session.scalars(statement)
        return list(result.unique())

    async def get_categories(self, categories_id: list[int]) -> list[Category]:
        """
        Get categories with given IDs.
        Args:
            categories_id: categories IDs to retrieve.

        Returns:
            categories as Category model instances.
        """
        statement = select(Category).where(Category.id.in_(categories_id))
        result = await self.session.scalars(statement)
        return list(result.unique())

    async def get_all_categories(self) -> list[Category]:
        """
        Get all Categories.
        Returns:
            categories as Category model instances.
        """
        statement = select(Category)
        result = await self.session.scalars(statement)
        return list(result.unique())
