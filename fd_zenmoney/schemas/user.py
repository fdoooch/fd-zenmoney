from pydantic import BaseModel
from .utils import to_camel


class User(BaseModel):
    id: int
    country: int
    login: str
    parent: int | None
    country_code: str
    email: str | None
    changed: int
    currency: int
    paid_till: int
    month_start_day: int
    is_forecast_enabled: bool
    plan_balance_mode: str
    plan_settings: str
    subscription: str
    subscription_renewal_date: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
