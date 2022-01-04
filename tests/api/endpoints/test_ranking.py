from fastapi.testclient import TestClient

from quality_of_life.main import app

client = TestClient(app)


def test_get_continent_ranking():
    response = client.get(
        '/api/v1/ranking/continent/')
    assert response.status_code == 200
    assert response.json() == [{'Continent': 'Europe', 'ranking': 625.2299999999996}]


def test_get_country_ranking():
    response = client.get(
        '/api/v1/ranking/country/')
    assert response.status_code == 200
    assert response.json() == [{'Country': ' United Kingdom', 'ranking': 77.61000000000001}]


def test_get_city_ranking():
    response = client.get(
        '/api/v1/ranking/city/')
    assert response.status_code == 200
    assert response.json() == [{'City': 'Birmingham', 'ranking': 10.01}]
