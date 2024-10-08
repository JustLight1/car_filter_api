from fastapi_filter.contrib.sqlalchemy.filter import Filter

from pydantic import Field

from app.models.car import Car


class CarFilter(Filter):
    """
    Фильтр для авто

    Attributes:
        brand str: Марка авто.
        model str: Модель авто.
        year int: Год производства авто.
        fuel_type str: Тип топлива.
        transmission str: Тип КПП.
        mileage int: Пробег.
        price int: Цена.
    """
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    fuel_type: str | None = None
    transmission: str | None = None
    mileage__gte: int | None = Field(None, alias='mileage_min')
    mileage__lte: int | None = Field(None, alias='mileage_max')
    price__gte: int | None = Field(None, alias='price_min')
    price__lte: int | None = Field(None, alias='price_max')

    order_by: list[str] = []

    class Constants(Filter.Constants):
        model = Car

    class Config:
        extra = "allow"
