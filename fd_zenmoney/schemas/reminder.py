from pydantic import BaseModel
from .utils import to_camel


class Reminder(BaseModel):
    id: str
    user: int
    income: float
    outcome: float
    changed: int
    income_instrument: int
    outcome_instrument: int
    step: int
    points: list[int]
    tag: list[str] | None
    start_date: str
    end_date: str | None
    notify: bool
    interval: str | None
    income_account: str
    outcome_account: str
    comment: str | None
    payee: str | None
    merchant: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
