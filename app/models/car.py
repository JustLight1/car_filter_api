from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Car(Base):
    """
    Модель переговорной комнаты.

    Inherits:
        Base: Базовый класс для всех моделей.
        Attributes:
            __tablename__ (str): Имя таблицы, устанавливается как имя класса
                                в нижнем регистре.
            id (Mapped[int]): Первичный ключ.

    Attributes:
        name (Mapped[str]): Название переговорной комнаты.
        description (Mapped[str or None]): Описание переговорной комнаты.
        reservations (relationship): Связь с моделью бронирований.
    """
    brand: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(50), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    fuel_type: Mapped[str] = mapped_column(String(50), index=True)
    transmission: Mapped[str] = mapped_column(String(50), index=True)
    mileage: Mapped[int] = mapped_column(Integer, index=True)
    price: Mapped[int] = mapped_column(Integer, index=True)
