from pydantic import BaseModel
from .utils import to_camel


class Transaction(BaseModel):
    id: str
    user: int
    date: str
    income: float
    outcome: float
    changed: int
    income_instrument: int
    outcome_instrument: int
    created: int
    original_payee: str | None
    deleted: bool
    viewed: bool
    hold: int | None
    qr_code: str | None
    source: str | None
    income_account: str
    outcome_account: str | None
    tag: list[str] | None
    comment: str | None
    payee: str | None
    op_income: float | None
    op_outcome: float | None
    op_income_instrument: int | None
    op_outcome_instrument: int | None
    latitude: float | None
    longitude: float | None
    merchant: str | None
    income_bank_ID: str | None
    outcome_bank_ID: str | None
    reminder_marker: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
