from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.car import car_crud
from app.models import Car


async def check_car_exists(
        car_id: int,
        session: AsyncSession,
) -> Car:
    """
    Проверяет существование авто по его идентификатору.

    Parameters:
        car_id (int): Идентификатор авто.
        session (AsyncSession): Сессия базы данных.

    Returns:
        Car: Найденный авто.

    Raises:
        HTTPException: Если авто не найден.
    """
    car = await car_crud.get(car_id, session)
    if car is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Авто не найден!'
        )
    return car
