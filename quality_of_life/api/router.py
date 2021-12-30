from fastapi import APIRouter

from api.endpoints import nearest, ranking

api_router = APIRouter()
api_router.include_router(nearest.router, prefix='/city')
api_router.include_router(ranking.router, prefix='/city')
