import pytest
from pydantic import ValidationError

from app.schemas.contact_request import ContactRequestCreate

# UNIT TEST: prüft, dass eine leere Nachricht nicht erlaubt ist
def test_contact_schema_rejects_empty_message():
    with pytest.raises(ValidationError):
        ContactRequestCreate(sender_contact="a@b.at", message="")
