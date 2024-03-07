from pydantic import BaseModel
from .utils import to_camel


class Tag(BaseModel):
    id: str
    user: int
    changed: int
    icon: str | None
    budget_income: bool
    budget_outcome: bool
    required: bool | None
    color: int | None
    picture: str | None
    title: str
    show_income: bool
    show_outcome: bool
    parent: str | None
    static_id: str | None
   

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        use_enum_values = True
