from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Car(Base):
    """
    Модель авто.

    Inherits:
        Base: Базовый класс для всех моделей.
        Attributes:
            __tablename__ (str): Имя таблицы, устанавливается как имя класса
                                в нижнем регистре.
            id (Mapped[int]): Первичный ключ.

    Attributes:
        brand str: Марка авто.
        model str: Модель авто.
        year int: Год производства авто.
        fuel_type str: Тип топлива.
        transmission str: Тип КПП.
        mileage int: Пробег.
        price int: Цена.
    """
    brand: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    model: Mapped[str] = mapped_column(String(50), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    fuel_type: Mapped[str] = mapped_column(String(50), index=True)
    transmission: Mapped[str] = mapped_column(String(50), index=True)
    mileage: Mapped[int] = mapped_column(Integer, index=True)
    price: Mapped[int] = mapped_column(Integer, index=True)
