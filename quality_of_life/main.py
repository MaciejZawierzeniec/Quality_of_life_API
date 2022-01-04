from fastapi import FastAPI

from quality_of_life.api.router import api_router

app = FastAPI()

app.include_router(api_router, prefix='/api/v1')
