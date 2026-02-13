from typing import Optional
from sqlmodel import SQLModel, Field


class ContactRequestCreate(SQLModel):
    sender_contact: Optional[str] = None
    message: str = Field(min_length=1)