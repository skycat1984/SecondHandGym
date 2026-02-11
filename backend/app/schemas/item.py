from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel
from app.models.common import ItemStatus


class ItemCreate(SQLModel):
    title: str
    description: str
    category_id: int
    price: Optional[float] = None


class ItemRead(SQLModel):
    id: int
    title: str
    description: str
    price: Optional[float]
    status: ItemStatus
    created_at: datetime
    updated_at: Optional[datetime]
    category_id: int
