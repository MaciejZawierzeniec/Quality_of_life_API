from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from quality_of_life.db.database import Base
from quality_of_life.db.dependencies import get_db
from quality_of_life.main import app

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db



def test_get_continent_ranking():
    test_client = TestClient(app)
    response = test_client.get(
        '/api/v1/ranking/continent?limit=1')
    assert response.status_code == 200
    assert response.json() == [{'continent': 'Europe', 'ranking': 625.23}]

#
# def test_get_country_ranking():
#     response = client.get(
#         '/api/v1/ranking/country/')
#     assert response.status_code == 200
#     assert response.json() == [{'Country': ' United Kingdom', 'ranking': 77.61000000000001}]
#
#
# def test_get_city_ranking():
#     response = client.get(
#         '/api/v1/ranking/city/')
#     assert response.status_code == 200
#     assert response.json() == [{'City': 'Birmingham', 'ranking': 10.01}]
