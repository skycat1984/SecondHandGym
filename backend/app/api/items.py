from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db import get_session
from ..models.item import Item
from ..schemas.item import ItemCreate, ItemRead

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemRead)
def create_item(payload: ItemCreate, session: Session = Depends(get_session)):
    item = Item.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/", response_model=list[ItemRead])
def list_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return items

