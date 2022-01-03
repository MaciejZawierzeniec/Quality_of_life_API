from fastapi import APIRouter

from quality_of_life.domain.quality_of_life_ranking import get_ranking_by


router = APIRouter()


@router.get("/ranking/")
async def get_ranking(get_by: str, limit: int = 1):
    return get_ranking_by(get_by, limit)
