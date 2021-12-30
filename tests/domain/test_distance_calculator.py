import pytest

from quality_of_life.errors import DomainError
from quality_of_life.domain.distance_calculator import get_city_coordinates, calculate_distance, \
    calculate_distances_between_cities, find_nearest, filter_by_max_distance


@pytest.mark.parametrize("city, country, expected",
                         [('Gdańsk', 'Poland', ('54.36119285', '18.62860883362069')),
                          ('Moscow', 'Russia', ('55.7504461', '37.6174943'))
                          ])
def test_get_city_coordinates(city, country, expected):
    coordinates = get_city_coordinates(city, country)
    assert coordinates == expected


def test_get_city_coordinates_wrong_data():
    city, country = 'Gdańsk', 'Russia'
    with pytest.raises(DomainError) as error:
        get_city_coordinates(city, country)
    assert error.value.message == 'Could not find city Gdańsk in country Russia.'


def test_calculate_distance():
    distance = calculate_distance(50, 5, -80, 4.5)
    assert distance == 14426.022458879059


def test_calculate_distances_between_cities():
    city, country = 'Gdańsk', 'Poland'
    distances = calculate_distances_between_cities(city, country)
    assert distances[:2] == [{'city': 'Aarhus', 'distance': 570.4869561445178},
                             {'city': 'Adelaide', 'distance': 14972.697601855514}]


@pytest.mark.parametrize("searched_city, searched_country, max_distance, limit, expected",
                         [('Gdańsk', 'Poland', 1000, 3,
                           [{'city': 'Gdansk', 'distance': 0.0}, {'city': 'Warsaw', 'distance': 285.08721275216277},
                            {'city': 'Wroclaw', 'distance': 377.59837864857184}]),
                          ('Moscow', 'Russia', 10000, 2, [{'city': 'Moscow', 'distance': 0.0},
                                                          {'city': 'Saint Petersburg', 'distance': 636.1695135872066}])
                          ])
def test_find_nearest(searched_city, searched_country, max_distance, limit, expected):
    nearest = find_nearest(searched_city, searched_country, max_distance, limit)
    assert nearest == expected


@pytest.mark.parametrize("searched_city, searched_country, max_distance, limit", [('test', 'Bolzga', 1000, 3)])
def test_find_nearest_should_raise_error_on_not_found_city(searched_city, searched_country, max_distance, limit):
    with pytest.raises(DomainError) as error:
        find_nearest(searched_city, searched_country, max_distance, limit)
    assert error.value.message == 'Could not find city test in country Bolzga.'


@pytest.mark.parametrize("distances, max_distance, expected",
                         [
                             ([{'city': 'A', 'distance': 500}, {'city': 'B', 'distance': 400},
                               {'city': 'C', 'distance': 300}], 400,
                              [{'city': 'B', 'distance': 400},
                               {'city': 'C', 'distance': 300}]),
                             ([], 1, []),
                             ([{'city': 'Gdańsk', 'distance': 500}], 500, [{'city': 'Gdańsk', 'distance': 500}]),
                             ([{'city': 'Gdańsk', 'distance': 0}], 0, [{'city': 'Gdańsk', 'distance': 0}])
                         ])
def test_filter_by_max_distance(distances, max_distance, expected):
    results = filter_by_max_distance(distances, max_distance)
    assert results == expected
