from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .db import engine
from .api.items import router as items_router

# 👇 wichtig: DB-Modelle importieren, damit metadata sie kennt
from .models.category import Category  # noqa: F401
from .models.item import Item          # noqa: F401
from .models.contact_request import ContactRequest  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Second-Hand Boerse API", lifespan=lifespan)

app.include_router(items_router)


@app.get("/health")
def health():
    return {"status": "ok"}
