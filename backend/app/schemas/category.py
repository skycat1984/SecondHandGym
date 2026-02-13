from sqlmodel import SQLModel, Field

class CategoryCreate(SQLModel):
    name: str = Field(min_length=1)