from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..models.category import Category
from ..schemas.category import CategoryCreate

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category)
def create_category(payload: CategoryCreate, session: Session = Depends(get_session)):
    category = Category.model_validate(payload)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


@router.get("/", response_model=list[Category])
def list_categories(session: Session = Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories
