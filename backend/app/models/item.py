from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


from app.models.common import utc_now, ItemStatus


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str
    description: str
    price: Optional[float] = None

    status: ItemStatus = Field(default=ItemStatus.verfuegbar)

    created_at: datetime = Field(default_factory=utc_now)
    updated_at: Optional[datetime] = None

    category_id: int = Field(foreign_key="category.id")