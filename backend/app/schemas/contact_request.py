from typing import Optional
from sqlmodel import SQLModel


class ContactRequestCreate(SQLModel):
    sender_contact: Optional[str] = None
    message: str