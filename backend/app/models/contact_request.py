from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

from app.models.common import utc_now


class ContactRequest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    item_id: int = Field(foreign_key="item.id")

    sender_contact: Optional[str] = None
    message: str

    created_at: datetime = Field(default_factory=utc_now)