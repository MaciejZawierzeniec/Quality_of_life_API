from fastapi import APIRouter

from quality_of_life.enums import ScoreColumn, GeoHierarchy
from quality_of_life.domain.quality_of_life_ranking import get_ranking_by

router = APIRouter()


@router.get("/city")
async def get_city_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, limit: int = 1):
    return get_ranking_by(score_column=score_column, get_by=GeoHierarchy.CITY, limit=limit)


@router.get("/country")
async def get_country_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, limit: int = 1):
    return get_ranking_by(score_column=score_column, get_by=GeoHierarchy.COUNTRY, limit=limit)


@router.get("/continent")
async def get_continent_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, limit: int = 1):
    return get_ranking_by(score_column=score_column, get_by=GeoHierarchy.CONTINENT, limit=limit)
