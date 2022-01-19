from typing import List, Dict

import geopy.distance
from OSMPythonTools.nominatim import Nominatim
from sqlalchemy.orm import Session

from quality_of_life.db.repository import get_cities_coordinates
from quality_of_life.errors import DomainError


def calculate_distances_between_cities(db: Session, searched_city: str, searched_country: str) -> list:
    searched_city_latitude, searched_city_longitude = get_city_coordinates(
        searched_city, searched_country
    )

    distances = get_cities_coordinates(db)

    city_distances = []
    for city in distances:
        distance_between_cities = calculate_distance(
            searched_city_latitude,
            searched_city_longitude,
            city["latitude"],
            city["longitude"],
        )
        city_distances.append(
            {"city": city["city"], "distance": distance_between_cities}
        )

    return city_distances


def calculate_distance(
        latitude_searched: float,
        longitude_searched: float,
        latitude_ua: float,
        longitude_ua: float,
) -> float:
    return geopy.distance.distance(
        (latitude_searched, longitude_searched), (latitude_ua, longitude_ua)
    ).km


def get_city_coordinates(city: str, country: str):
    nominatim = Nominatim()
    try:
        city_json = nominatim.query(f"{city}, {country}").toJSON()[0]
    except IndexError:
        raise DomainError(message=f"Could not find city {city} in country {country}.")
    return city_json["lat"], city_json["lon"]


def find_nearest(db: Session, searched_city: str, searched_country: str, max_distance: int, limit: int = 1) -> List[
    Dict]:
    distances = calculate_distances_between_cities(db=db, searched_city=searched_city,
                                                   searched_country=searched_country)
    distances = filter_by_max_distance(distances, max_distance)
    distances = sorted(distances, key=lambda x: x["distance"])[:limit]
    return distances


def filter_by_max_distance(distances: List[Dict], max_distance: int) -> List[Dict]:
    return [
        city_distance
        for city_distance in distances
        if city_distance["distance"] <= max_distance
    ]
