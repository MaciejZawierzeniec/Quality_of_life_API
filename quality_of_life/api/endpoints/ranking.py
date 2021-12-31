from fastapi import APIRouter

from quality_of_life.domain.quality_of_life_ranking import get_city_ranking


router = APIRouter()


@router.get("/ranking/")
async def get_ranking(limit: int = 1):
    return get_city_ranking(limit)
