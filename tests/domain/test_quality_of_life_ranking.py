from quality_of_life.domain.quality_of_life_ranking import get_ranking_by


def test_get_continent_ranking():
    limit = 7
    ranking = get_ranking_by('Continent', limit)
    assert ranking[:limit] == [{'Continent': 'Europe', 'ranking': 625.2299999999996},
                               {'Continent': 'North America', 'ranking': 457.46},
                               {'Continent': 'Asia', 'ranking': 191.54000000000005},
                               {'Continent': 'South America', 'ranking': 68.25},
                               {'Continent': 'Oceania', 'ranking': 46.529999999999994},
                               {'Continent': 'Africa', 'ranking': 33.199999999999996}]


def test_get_country_ranking():
    limit = 5
    ranking = get_ranking_by('Country', limit)
    assert ranking[:limit] == [{'Country': ' United Kingdom', 'ranking': 77.61000000000001},
                               {'Country': ' Canada', 'ranking': 66.23},
                               {'Country': ' Germany', 'ranking': 65.82},
                               {'Country': ' France', 'ranking': 48.79},
                               {'Country': ' Spain', 'ranking': 40.160000000000004}]


def test_get_city_ranking():
    limit = 5
    ranking = get_ranking_by('City', limit)
    assert ranking[:limit] == [{'City': 'Birmingham', 'ranking': 10.01},
                               {'City': 'Portland', 'ranking': 9.89},
                               {'City': 'Singapore', 'ranking': 7.1},
                               {'City': 'London', 'ranking': 6.89},
                               {'City': 'Munich', 'ranking': 6.89}]
