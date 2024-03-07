from pydantic import BaseModel
from .utils import to_camel


class ReminderMarker(BaseModel):
    id: str
    user: int
    date: str
    income: float
    outcome: float
    changed: int
    income_instrument: int
    outcome_instrument: int
    state: str
    is_forecast: bool
    reminder: str
    income_account: str
    outcome_account: str
    comment: str | None
    payee: str | None
    merchant: str | None
    notify: bool
    tag: list[str] | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
