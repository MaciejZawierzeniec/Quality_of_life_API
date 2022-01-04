from fastapi import HTTPException, APIRouter

from quality_of_life.errors import DomainError
from quality_of_life.domain.distance_calculator import find_nearest


router = APIRouter()


@router.get("/")
async def get_nearest(city: str, country: str, distance: int, limit: int = 1):
    try:
        return find_nearest(city, country, distance, limit)
    except DomainError as e:
        raise HTTPException(status_code=404, detail=e.message)
