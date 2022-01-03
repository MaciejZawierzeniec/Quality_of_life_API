from fastapi.testclient import TestClient

from quality_of_life.main import app

client = TestClient(app)


def test_get_ranking():
    response = client.get(
        '/api/v1/city/ranking/?get_by=Continent&limit=1')
    assert response.status_code == 200
    assert response.json() == [{'Continent': 'Europe', 'ranking': 625.2299999999996}]
