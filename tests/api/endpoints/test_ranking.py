from fastapi.testclient import TestClient

from quality_of_life.main import app

client = TestClient(app)


def test_get_ranking():
    response = client.get(
        '/api/v1/city/ranking/?limit=1')
    assert response.status_code == 200
    assert response.json() == [{'city': 'Singapore', 'ranking': 7.1}]
