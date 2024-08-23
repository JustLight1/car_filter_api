from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class FuelType(str, Enum):
    benzine = 'бензин'
    diesel = 'дизель'
    electric = 'электричество'
    hybrid = 'гибрид'


class TransmissionType(str, Enum):
    manual = 'механическая'
    automatic = 'автоматическая'
    variator = 'вариатор'
    robot = 'робот'


class CarBase(BaseModel):
    brand: str = Field(..., min_length=1, max_length=50)
    model: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1886, le=datetime.now().year)
    fuel_type: FuelType
    transmission: TransmissionType
    mileage: int = Field(..., ge=0)
    price: int = Field(..., ge=0)


class CarCreate(CarBase):
    pass


class CarUpdate(CarBase):
    pass


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
