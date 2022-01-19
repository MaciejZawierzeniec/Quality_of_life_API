from typing import Optional

from pydantic import BaseModel


class CityBase(BaseModel):
    city: str


class CityCoordinates(CityBase):
    distance: float

    class Config:
        orm_mode = True


class CityCreate(CityBase):
    pass


class City(CityBase):
    ranking: Optional[float]

    class Config:
        orm_mode = True


class CountryBase(BaseModel):
    country: str
    ranking: float


class Country(CountryBase):
    class Config:
        orm_mode = True


class ContinentBase(BaseModel):
    continent: str
    ranking: float


class Continent(ContinentBase):
    class Config:
        orm_mode = True
