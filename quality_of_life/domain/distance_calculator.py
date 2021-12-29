import geopy.distance
from OSMPythonTools.nominatim import Nominatim

from quality_of_life.errors import DomainError
from quality_of_life.repo.repository import read_dataset


def calculate_distances_between_cities(searched_city: str, searched_country: str, max_distance: int) -> dict:
    searched_city_latitude, searched_city_longitude = get_city_coordinates(searched_city, searched_country)
    qol = read_dataset('../../quality_of_life_extended.csv')
    city_distances = {}
    for i in qol.index:
        distance_between_cities = calculate_distance(searched_city_latitude, searched_city_longitude,
                                                     qol.at[i, 'latitude'], qol.at[i, 'longitude'])
        if distance_between_cities < max_distance:
            city_distances[distance_between_cities] = qol.at[i, 'UA_Name']

    return city_distances


def calculate_distance(latitude_searched: float, longitude_searched: float, latitude_ua: float,
                       longitude_ua: float) -> float:
    return geopy.distance.distance((latitude_searched, longitude_searched), (latitude_ua, longitude_ua)).km


def get_city_coordinates(city: str, country: str):
    nominatim = Nominatim()
    try:
        city_json = nominatim.query(f'{city}, {country}').toJSON()[0]
    except IndexError:
        raise DomainError(message=f'Could not find city {city} in country {country}.')
    return city_json["lat"], city_json["lon"]


def find_nearest_city(searched_city: str, searched_country: str, max_distance: int) -> dict:
    distances = calculate_distances_between_cities(searched_city, searched_country, max_distance)
    min_distance = min(distances)
    nearest_city = distances[min_distance]
    return {nearest_city: min_distance}

