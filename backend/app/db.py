from sqlmodel import create_engine

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)

from sqlmodel import Session

def get_session():
    with Session(engine) as session:
        yield session
