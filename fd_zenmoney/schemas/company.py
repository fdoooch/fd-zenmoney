from pydantic import BaseModel
from .utils import to_camel


class Company(BaseModel):
    id: int
    title: str
    www: str | None
    country: int | None
    full_title: str | None
    changed: int
    deleted: bool
    country_code: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
