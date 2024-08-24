from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class FuelType(str, Enum):
    """
    Тип топлива.
    """
    benzine = 'бензин'
    diesel = 'дизель'
    electric = 'электричество'
    hybrid = 'гибрид'


class TransmissionType(str, Enum):
    """
    Тип КПП.
    """
    manual = 'механическая'
    automatic = 'автоматическая'
    variator = 'вариатор'
    robot = 'робот'


class CarBase(BaseModel):
    """
    Базовая схема авто.

    Attributes:
        brand str: Марка авто.
        model str: Модель авто.
        year int: Год производства авто.
        fuel_type str: Тип топлива.
        transmission str: Тип КПП.
        mileage int: Пробег.
        price int: Цена.
    """
    brand: str = Field(..., min_length=1, max_length=50)
    model: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1886, le=datetime.now().year)
    fuel_type: FuelType
    transmission: TransmissionType
    mileage: int = Field(..., ge=0)
    price: int = Field(..., ge=0)


class CarCreate(CarBase):
    """
    Схема для создания нового авто.
    """
    pass


class CarUpdate(CarBase):
    """
    Схема для обновления авто.
    """

    brand: str | None = None
    model: str | None = None
    year: int | None = None
    fuel_type: FuelType | None = None
    transmission: TransmissionType | None = None
    mileage: int | None = None
    price: int | None = None


class CarDB(CarBase):
    """
    Схема авто в базе данных.

    Inherits:
        CarBase: Базовая схема авто.

    Attributes:
        id (int): Идентификатор авто.
        model_config (ConfigDict): Конфигурация схемы для сериализации объектов
        базы данных, а не только Python-словарь или JSON-объект.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
