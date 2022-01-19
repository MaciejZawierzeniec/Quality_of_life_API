from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from quality_of_life.db import schemas
from quality_of_life.db.dependencies import get_db
from quality_of_life.db.repository import get_cities, get_countries, get_continents
from quality_of_life.enums import ScoreColumn

router = APIRouter()


@router.get("/city", response_model=List[schemas.City])
async def get_city_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, skip: int = 0, limit: int = 10,
                           db: Session = Depends(get_db)):
    return get_cities(db=db, score_column=score_column, skip=skip, limit=limit)


@router.get("/country", response_model=List[schemas.Country])
async def get_country_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, skip: int = 0, limit: int = 10,
                              db: Session = Depends(get_db)):
    return get_countries(db=db, score_column=score_column, skip=skip, limit=limit)


@router.get("/continent", response_model=List[schemas.Continent])
async def get_continent_ranking(score_column: ScoreColumn = ScoreColumn.MEAN, skip: int = 0, limit: int = 10,
                                db: Session = Depends(get_db)):
    return get_continents(db=db, score_column=score_column, skip=skip, limit=limit)
