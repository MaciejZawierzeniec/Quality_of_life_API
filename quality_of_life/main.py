import uvicorn
from fastapi import FastAPI

from quality_of_life.api.router import api_router
from quality_of_life.db import models
from quality_of_life.db.database import engine


def create_db():
    models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


def main():
    # create_db()
    uvicorn.run("quality_of_life.main:app", host="0.0.0.0", port=8000, reload=True)
