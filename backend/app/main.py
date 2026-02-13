from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware

from .db import engine
from .api.items import router as items_router
from .api.contact_requests import router as contact_router
from .api.categories import router as categories_router

# DB-Modelle importieren
from .models.category import Category  # noqa: F401
from .models.item import Item          # noqa: F401
from .models.contact_request import ContactRequest  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Second-Hand Boerse API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items_router)
app.include_router(categories_router)
app.include_router(contact_router)


@app.get("/health")
def health():
    return {"status": "ok"}
