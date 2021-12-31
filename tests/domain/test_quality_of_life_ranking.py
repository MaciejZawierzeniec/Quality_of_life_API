from quality_of_life.domain.quality_of_life_ranking import get_city_ranking


def test_get_city_ranking():
    limit = 3
    ranking = get_city_ranking(limit)
    assert ranking[:limit] == [{'city': 'Singapore', 'ranking': 7.1},
                               {'city': 'London', 'ranking': 6.89}, {'city': 'Munich', 'ranking': 6.89}]
