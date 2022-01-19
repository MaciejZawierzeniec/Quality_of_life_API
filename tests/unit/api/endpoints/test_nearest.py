# from fastapi.testclient import TestClient
#
# from quality_of_life.main import app
#
# client = TestClient(app)
#
#
# def test_get_nearest():
#     response = client.get(
#         '/api/v1/nearest/?city=gda%C5%84sk&country=Poland&distance=200&limit=1')
#     assert response.status_code == 200
#     assert response.json() == [
#         {
#             "city": "Gdansk",
#             "distance": 0
#         }
#     ]
#
#
# def test_get_nearest_non_existing_city():
#     response = client.get(
#         '/api/v1/nearest/?city=miasto123&country=Poland&distance=200&limit=1')
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Could not find city miasto123 in country Poland.'}
#
