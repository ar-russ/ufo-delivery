from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.db import Base
from src.models.dto.users import UserDTO, AddressDTO


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=32))
    password: Mapped[str] = mapped_column(String(length=255))
    phone: Mapped[str] = mapped_column(String(length=15))
    address: Mapped["Address"] = relationship(back_populates="user", uselist=False, lazy="joined")
    is_superuser: Mapped[bool] = mapped_column(default=False)
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

    def to_dto(self) -> UserDTO:
        return UserDTO(
            id=self.id,
            name=self.name,
            phone=self.phone,
            password=self.password,
            address=self.address.to_dto() if self.address else None,
            is_superuser=self.is_superuser,
        )


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(length=255), nullable=True)
    reference: Mapped[str] = mapped_column(String(length=255), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True, nullable=True)
    user: Mapped["User"] = relationship(back_populates="address")

    def to_dto(self) -> AddressDTO:
        return AddressDTO(
            street=self.street,
            reference=self.reference,
        )
