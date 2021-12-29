from fastapi import FastAPI, HTTPException

from errors import DomainError
from domain.distance_calculator import find_nearest

app = FastAPI()


@app.get("/nearest/")
async def get_nearest(city: str, country: str, distance: int, limit: int = 1):
    try:
        return find_nearest(city, country, distance, limit)
    except DomainError as e:
        raise HTTPException(status_code=404, detail=e.message)
