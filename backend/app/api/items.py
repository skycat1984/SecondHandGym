from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlmodel import Session, select

from ..db import get_session
from ..models.item import Item
from ..schemas.item import ItemCreate, ItemRead, ItemStatusUpdate
from ..models.common import ItemStatus

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemRead)
def create_item(payload: ItemCreate, session: Session = Depends(get_session)):
    item = Item.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/", response_model=list[ItemRead])
def list_items(
    session: Session = Depends(get_session),
    status: Optional[ItemStatus] = None,
    category_id: Optional[int] = None,
):
    stmt = select(Item)

    if status is not None:
        stmt = stmt.where(Item.status == status)

    if category_id is not None:
        stmt = stmt.where(Item.category_id == category_id)

    return session.exec(stmt).all()


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.patch("/{item_id}/status", response_model=ItemRead)
def update_item_status(
    item_id: int,
    payload: ItemStatusUpdate,
    session: Session = Depends(get_session),
):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.status = payload.status
    item.updated_at = datetime.now(timezone.utc)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(item)
    session.commit()
    return Response(status_code=204)

