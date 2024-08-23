from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.car import Car
from app.schemas.car import CarCreate, CarUpdate
from app.filters.car import CarFilter


class CRUDCar(CRUDBase[
    Car,
    CarCreate,
    CarUpdate
]):
    """
    Класс для операций CRUD с моделью Car.
    """

    async def get_multi_filtered(
        self,
        filter: CarFilter,
        session: AsyncSession,
    ) -> list[Car]:
        query = select(self.model)
        query = filter.filter(query)
        query = filter.sort(query)
        result = await session.execute(query)
        return result.scalars().all()


car_crud = CRUDCar(Car)
