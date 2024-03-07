from pydantic import BaseModel
from .utils import to_camel


class Account(BaseModel):
    id: str
    user: int
    instrument: int
    type: str
    role: int | None
    private: bool
    savings: bool
    title: str
    in_balance: bool
    credit_limit: float
    start_balance: float
    balance: float
    company: int | None
    archive: bool
    enable_correction: bool
    balance_correction_type: str
    start_date: str | None
    capitalization: bool | None
    percent: float | None
    changed: int
    sync_ID: list[str] | None
    enable_SMS: bool
    end_date_offset: int | None
    end_date_offset_interval: str | None
    payoff_step: int | None
    payoff_interval: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
