from pydantic import BaseModel
from .utils import to_camel


class Budget(BaseModel):
    user: int
    changed: int
    date: str
    tag: str | None
    income: int
    outcome: int
    income_lock: bool
    outcome_lock: bool
    is_income_forecast: bool
    is_outcome_forecast: bool   

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
