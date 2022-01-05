import uvicorn
from fastapi import FastAPI

from quality_of_life.api.router import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
