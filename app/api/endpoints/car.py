from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_filter.base.filter import FilterDepends

from app.core.db import get_async_session
from app.crud.car import car_crud
from app.schemas.car import (
    CarCreate, CarDB, CarUpdate
)
from app.filters.car import CarFilter
from app.api.validators import check_car_exists


router = APIRouter()


@router.post(
    '/',
    response_model=CarDB,
    status_code=status.HTTP_201_CREATED
)
async def create_car(
    car: CarCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создать авто.
    """
    new_car = await car_crud.create(car, session)
    return new_car


@router.get(
    '/',
    response_model=list[CarDB],
    status_code=status.HTTP_200_OK
)
async def get_cars(
    filter: CarFilter = FilterDepends(CarFilter),
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получить список отфильтрованных авто.
    """
    cars = await car_crud.get_multi_filtered(filter, session)
    return cars


@router.get(
    '/all_cars',
    response_model=list[CarDB],
    status_code=status.HTTP_200_OK
)
async def get_all_cars(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получить весь список авто.
    """
    all_cars = await car_crud.get_multi(session)
    return all_cars


@router.get(
    '/{car_id}',
    response_model=CarDB,
    status_code=status.HTTP_200_OK
)
async def get_car(
    car_id: int, session:
    AsyncSession = Depends(get_async_session)
):
    """
    Получить авто по его id.
    """
    await check_car_exists(
        car_id, session
    )
    car = await car_crud.get(car_id, session)
    return car


@router.patch(
    '/{car_id}',
    response_model=CarUpdate,
    status_code=status.HTTP_200_OK
)
async def update_car(
    car_id: int,
    obj_in: CarUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Обновить авто.
    """
    car = await check_car_exists(
        car_id, session
    )
    car = await car_crud.update(
        car, obj_in, session
    )
    return car


@router.delete(
    '/{car_id}',
    response_model=CarDB,
    status_code=status.HTTP_200_OK
)
async def delete_car(
    car_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Удалить авто.
    """
    car = await check_car_exists(
        car_id, session
    )
    car = await car_crud.remove(
        car, session
    )
    return car
