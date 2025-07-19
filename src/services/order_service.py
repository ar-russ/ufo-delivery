from src.repositories.db.orders import OrderRepository
from src.repositories.db.items import ItemRepository
from src.models.dto.orders import OrderDTO, AddItemToOrder, RemoveItemFromOrder
from src.models.db.orders import Order, OrderItem
from src.core.exceptions import (
    ItemNotFound,
    ItemNotInOrder,
    OrderIsEmpty,
)


class OrderService():
    def __init__(self, repository: OrderRepository, item_repository: ItemRepository):
        self._repository = repository
        self._item_repository = item_repository

    async def get(self, user_id: int) -> OrderDTO:
        """
        Get Order from database. New one will be created if User
        with given ID does not have existing non-placed order.
        Args:
            user_id: ID of User whose order should be retrieved.

        Returns:
            OrderDTO representing Order.
        """
        order = await self._repository.get_by_user_id(user_id)

        if not order:
            order = await self._create_new_order(user_id)

        return order.to_dto()

    async def add_item_to_order(
            self,
            order_id: int,
            user_id: int,
            data: AddItemToOrder
    ) -> OrderDTO:
        """
        Add Item to Order with given ID. New Order with added Item will be
        created if User with given ID does not have existing non-placed order.

        Args:
            order_id: ID of Order to which Item should be added.
            user_id: ID of User to whose Order Item should be added.
            data: AddItemToOrder model containing data mandatory for adding Item to Order.

        Returns:
            OrderDTO representing Order with added Item.
        """
        item = await self._item_repository.get(data.item_id)
        if not item:
            raise ItemNotFound

        order = await self._repository.get_by_user_id(user_id)
        if not order:
            order = await self._create_new_order(user_id)
            order_id = order.id

        order_item = OrderItem(order=order, item=item, quantity=1)
        await self._repository.add_item_to_order(order_id, order_item)
        await self._repository.session.commit()

        order = await self._repository.get(order_id)
        return order.to_dto()

    async def remove_item_from_order(self, order_id: int, data: RemoveItemFromOrder) -> OrderDTO:
        """
        Remove Item from current user's Order.

        Args:
            order_id: ID of Order to which Item should be added.
            data: RemoveItemToOrder model containing data mandatory for removing Item from Order.

        Returns:
            OrderDTO representing Order without removed Item.
        """
        order_item = await self._repository.get_order_item(order_id, data.item_id)
        if not order_item:
            raise ItemNotInOrder

        try:
            await self._repository.remove_item_from_order(order_id, order_item)
        except ValueError as exc:
            raise ItemNotInOrder from exc

        await self._repository.session.commit()

        order = await self._repository.get(order_id)
        return order.to_dto()

    async def place_order(self, user_id: int) -> OrderDTO:
        """
        Mark Order of User with given ID as placed.
        Args:
            user_id: ID of User whose Order should be placed.

        Returns:
            OrderDTO representing placed Order
        """
        order = await self._repository.get_by_user_id(user_id)
        if not order:
            order = await self._create_new_order(user_id)

        if not order.order_items:
            raise OrderIsEmpty

        await self._repository.set_order_placed(order)
        await self._repository.session.commit()
        await self._repository.session.refresh(order)

        return order.to_dto()

    async def _create_new_order(self, user_id: int) -> Order:
        order = Order(user_id=user_id, is_placed=False, order_items=[])
        await self._repository.add(order)
        await self._repository.session.commit()
        return order
