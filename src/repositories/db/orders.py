from sqlalchemy import select, update as sql_update

from src.repositories.db.base import BaseSQLAlchemyRepository
from src.models.db.orders import Order, OrderItem


class OrderRepository(BaseSQLAlchemyRepository):
    async def add(self, model: Order) -> None:
        self.session.add(model)

    async def get(self, id_: int) -> Order | None:
        statement = select(Order).where(Order.id == id_)
        return await self.session.scalar(statement)

    async def update(self, id_: int, updated_data: dict) -> Order:
        statement = sql_update(Order).where(Order.id == id_).values(**updated_data)
        await self.session.execute(statement)
        return await self.get(id_)

    async def delete(self, id_: int) -> None:
        order = await self.get(id_)

        await self.session.delete(order)

    async def get_by_user_id(self, user_id: int) -> Order | None:
        """
        Get Order attached to User with given ID.
        Args:
            user_id: ID of User whose Order should be returned.

        Returns:
            Order model instance if found, otherwise None.
        """
        statement = select(Order).where(
            (Order.user_id == user_id) & (Order.is_placed == False)
        )
        return await self.session.scalar(statement)

    async def add_item_to_order(self, order_id: int, new_order_item: OrderItem) -> None:
        """
        Add given OrderItem to Order with corresponding ID. If such OrderItem is already
        attached to the Order, quantity field of existing OrderItem will be incremented.
        Args:
            order_id: ID of Order to which OrderItem should be attached.
            new_order_item: OrderItem which should be added to Order.
        """
        order = await self.get(order_id)

        order_item = await self.get_order_item(order_id, new_order_item.item_id)
        if order_item:
            order_item.quantity = order_item.quantity + 1
            return

        order.order_items.append(new_order_item)

    async def remove_item_from_order(self, order_id: int, order_item: OrderItem) -> None:
        """
        Removes given OrderItem from Order with corresponding ID. If amount of OrderItems in
        given Order is more than 1, quantity field will be decremented.
        Args:
            order_id: ID of Order from which OrderItem should be removed.
            order_item: OrderItem to remove from Order.
        """
        order = await self.get(order_id)

        if order_item.quantity > 1:
            order_item.quantity -= 1
            return

        order.order_items.remove(order_item)
        await self.session.delete(order_item)

    async def set_order_placed(self, order: Order) -> None:
        """
        Mark given Order as placed.
        """
        order.is_placed = True

    async def get_order_item(self, order_id: int, item_id: int) -> OrderItem | None:
        """
        Get OrderItem with corresponding Order ID and Item ID from database.
        Returns:
            OrderItem model instance.
        """
        statement = select(OrderItem).where(
            (OrderItem.order_id == order_id) & (OrderItem.item_id == item_id)
        )
        return await self.session.scalar(statement)
