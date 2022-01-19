from typing import List

from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session

from quality_of_life.db import schemas
from quality_of_life.db.dependencies import get_db
from quality_of_life.domain.distance_calculator import find_nearest
from quality_of_life.errors import DomainError

router = APIRouter()


@router.get("/", response_model=List[schemas.CityCoordinates])
async def get_nearest(city: str, country: str, distance: int, limit: int = 1, db: Session = Depends(get_db)):
    try:
        return find_nearest(db=db, searched_city=city, searched_country=country, max_distance=distance, limit=limit)
    except DomainError as e:
        raise HTTPException(status_code=404, detail=e.message)
