from fastapi import FastAPI, HTTPException

from quality_of_life.domain.distance_calculator import find_nearest_city
from errors import DomainError

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.get("/nearest_city/")
async def get_nearest_city(city: str, country: str, distance: int):
    try:
        return find_nearest_city(city, country, distance)
    except DomainError as e:
        raise HTTPException(status_code=404, detail=e.message)
