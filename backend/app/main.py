from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .db import engine
from .api.items import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Second-Hand Boerse API", lifespan=lifespan)

app.include_router(items_router)


@app.get("/health")
def health():
    return {"status": "ok"}
