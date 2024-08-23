from fastapi import APIRouter

from app.api.endpoints import car_router


main_router = APIRouter()
main_router.include_router(
    car_router, prefix='/api/cars', tags=['Car']
)
