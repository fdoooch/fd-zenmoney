from pydantic import BaseModel
from .utils import to_camel


class Instrument(BaseModel):
    id: int
    title: str
    short_title: str
    symbol: str
    rate: float
    changed: int

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True

