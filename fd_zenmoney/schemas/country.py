from pydantic import BaseModel
from .utils import to_camel


class Country(BaseModel):
    id: int
    title: str
    currency: int
    domain: str | None

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
