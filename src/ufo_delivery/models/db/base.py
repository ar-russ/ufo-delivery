from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for ORM Models
    """

    def to_dto(self) -> BaseModel:
        """
        Convert this SQLAlchemy model to pydantic BaseModel.
        """
