from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.db import Base
from src.models.dto.items import ItemDTO, CategoryDTO


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=64))
    description: Mapped[str] = mapped_column(String(length=255))
    price: Mapped[float] = mapped_column()
    image_path: Mapped[str] = mapped_column(String(length=255))
    categories: Mapped[list["Category"]] = relationship(
        back_populates="items",
        secondary="item_category",
        lazy="joined"
    )
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="item",
        lazy="joined",
    )
    is_available: Mapped[bool] = mapped_column()

    def to_dto(self) -> ItemDTO:
        return ItemDTO(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            image_path=self.image_path,
            categories=[
                category.to_dto() for category in self.categories
            ],
            is_available=self.is_available,
        )


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=32))
    items: Mapped[list["Item"]] = relationship(
        back_populates="categories",
        secondary="item_category",
        lazy="joined"
    )

    def to_dto(self) -> CategoryDTO:
        return CategoryDTO(
            id=self.id,
            name=self.name,
        )


class ItemCategoryRelation(Base):
    __tablename__ = "item_category"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)
