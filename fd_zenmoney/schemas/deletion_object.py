from pydantic import BaseModel
from .utils import to_camel


class DeletionObject(BaseModel):
    id: str | int
    object: str
    user: int
    stamp: int

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
