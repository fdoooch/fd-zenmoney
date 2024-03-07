from pydantic import BaseModel
from .utils import to_camel


class Merchant(BaseModel):
    id: str
    user: int
    title: str
    changed: int

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
