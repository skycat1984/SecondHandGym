from datetime import timezone

from app.models.common import utc_now, ItemStatus

# UNIT TEST: prüft, dass utc_now() ein Datum mit UTC-Zeitzone zurückgibt
def test_utc_now_returns_utc():
    dt = utc_now()
    assert dt.tzinfo == timezone.utc

# UNIT TEST: prüft die korrekten Enum-Werte von ItemStatus
def test_item_status_enum_values():
    assert ItemStatus.verfuegbar.value == "verfuegbar"
    assert ItemStatus.reserviert.value == "reserviert"
    assert ItemStatus.verkauft.value == "verkauft"
