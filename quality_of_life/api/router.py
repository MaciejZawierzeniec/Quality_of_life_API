from fastapi import APIRouter

from quality_of_life.api.endpoints import nearest, ranking

api_router = APIRouter()
api_router.include_router(nearest.router, prefix='/nearest')
api_router.include_router(ranking.router, prefix="/ranking")
