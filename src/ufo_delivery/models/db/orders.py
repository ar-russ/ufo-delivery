from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ufo_delivery.models.db import Base
from ufo_delivery.models.dto.orders import OrderDTO, OrderItemDTO


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        lazy="joined",
    )
    is_placed: Mapped[bool] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders", lazy="joined")

    def to_dto(self) -> OrderDTO:
        return OrderDTO(
            id=self.id,
            items=[item.to_dto() for item in self.order_items],
            is_placed=self.is_placed,
        )


class OrderItem(Base):
    __tablename__ = "order_items"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(default=1)

    order: Mapped["Order"] = relationship(back_populates="order_items", lazy="joined")
    item: Mapped["Item"] = relationship(back_populates="order_items", lazy="joined")

    def to_dto(self) -> OrderItemDTO:
        return OrderItemDTO(
            item=self.item.to_dto(),
            quantity=self.quantity
        )
