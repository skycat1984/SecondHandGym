from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from ..models.common import ItemStatus


class ItemCreate(SQLModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    category_id: int
    price: Optional[float] = Field(default=None, ge=0)


class ItemRead(SQLModel):
    id: int
    title: str
    description: str
    price: Optional[float]
    status: ItemStatus
    created_at: datetime
    updated_at: Optional[datetime]
    category_id: int


class ItemStatusUpdate(SQLModel):
    status: ItemStatus
