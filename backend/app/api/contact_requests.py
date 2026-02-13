from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..db import get_session
from ..models.contact_request import ContactRequest
from ..models.item import Item
from ..schemas.contact_request import ContactRequestCreate

router = APIRouter(tags=["contact"])


@router.post("/items/{item_id}/contact", response_model=ContactRequest)
def create_contact_request(
    item_id: int,
    payload: ContactRequestCreate,
    session: Session = Depends(get_session),
):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    contact_request = ContactRequest.model_validate(payload, update={"item_id": item_id})
    session.add(contact_request)
    session.commit()
    session.refresh(contact_request)
    return contact_request


@router.get("/items/{item_id}/contacts", response_model=list[ContactRequest])
def list_item_contacts(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    stmt = select(ContactRequest).where(ContactRequest.item_id == item_id)
    return session.exec(stmt).all()


@router.get("/contact-requests", response_model=list[ContactRequest])
def list_all_contact_requests(session: Session = Depends(get_session)):
    return session.exec(select(ContactRequest)).all()
