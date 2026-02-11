from sqlmodel import SQLModel


class CategoryCreate(SQLModel):
    name: str