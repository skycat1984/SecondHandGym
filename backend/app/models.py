from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field



class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    title: str
    description: str
    category: str

    price: Optional[float] = None
    status: str = "verfuegbar"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = None

class ItemCreate(SQLModel):
    title: str
    description: str
    category: str
    price: Optional[float] = None
