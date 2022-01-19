from sqlalchemy import desc, column, func
from sqlalchemy.orm import Session

from quality_of_life.db import models
from quality_of_life.enums import ScoreColumn, GeoHierarchy


def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities(
    db: Session,
    score_column: ScoreColumn = ScoreColumn.MEAN,
    skip: int = 0,
    limit: int = 10,
):
    return (
        db.query(models.City.city, column(score_column.value).label("ranking"))
        .order_by(desc(column(score_column.value)))
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_countries(
    db: Session,
    score_column: ScoreColumn = ScoreColumn.MEAN,
    skip: int = 0,
    limit: int = 10,
):
    return _group_ranking_geo_area(db=db, score_column=score_column, geo_area=GeoHierarchy.COUNTRY, skip=skip, limit=limit)


def get_continents(
    db: Session,
    score_column: ScoreColumn = ScoreColumn.MEAN,
    skip: int = 0,
    limit: int = 10,
):
    return _group_ranking_geo_area(db=db, score_column=score_column, geo_area=GeoHierarchy.CONTINENT, skip=skip, limit=limit)


def get_cities_coordinates(db: Session):
    return db.query(models.City.city, models.City.longitude, models.City.latitude).all()


def _group_ranking_geo_area(
        db: Session,
        score_column: ScoreColumn = ScoreColumn.MEAN,
        geo_area: GeoHierarchy = GeoHierarchy.COUNTRY,
        skip: int = 0,
        limit: int = 10,
):
    return (
        db.query(getattr(models.City, geo_area.value), func.sum(column(score_column.value)).label("ranking"))
        .group_by(column(geo_area.value))
        .order_by(desc(func.sum(column(score_column.value))))
        .offset(skip)
        .limit(limit)
        .all()
    )
