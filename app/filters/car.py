from fastapi_filter.contrib.sqlalchemy.filter import Filter

from app.models.car import Car


class CarFilter(Filter):
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    fuel_type: str | None = None
    transmission: str | None = None
    mileage__gte: int | None = None
    mileage__lte: int | None = None
    price__gte: int | None = None
    price__lte: int | None = None

    order_by: list[str] = []

    class Constants(Filter.Constants):
        model = Car
