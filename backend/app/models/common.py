from datetime import datetime, timezone
from enum import Enum


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ItemStatus(str, Enum):
    verfuegbar = "verfuegbar"
    reserviert = "reserviert"
    verkauft = "verkauft"