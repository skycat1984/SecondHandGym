import pytest
from pydantic import ValidationError

from app.schemas.item import ItemCreate

# UNIT TEST: prüft, dass negative Preise vom Schema abgelehnt werden
def test_item_schema_rejects_negative_price():
    with pytest.raises(ValidationError):
        ItemCreate(
            title="X",
            description="Y",
            price=-1,
            category_id=1,
        )

# UNIT TEST: prüft, dass ein leerer Titel nicht erlaubt ist
def test_item_schema_rejects_empty_title():
    with pytest.raises(ValidationError):
        ItemCreate(
            title="",
            description="Y",
            price=0,
            category_id=1,
        )
