from fastapi import APIRouter

from quality_of_life.domain.quality_of_life_ranking import get_ranking_by

router = APIRouter()


@router.get("/city")
async def get_city_ranking(limit: int = 1):
    return get_ranking_by('City', limit)


@router.get("/country")
async def get_country_ranking(limit: int = 1):
    return get_ranking_by('Country', limit)


@router.get("/continent")
async def get_continent_ranking(limit: int = 1):
    return get_ranking_by('Continent', limit)
