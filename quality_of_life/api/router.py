from fastapi import APIRouter

from api.endpoints import nearest

api_router = APIRouter()
api_router.include_router(nearest.router, prefix='/city')
