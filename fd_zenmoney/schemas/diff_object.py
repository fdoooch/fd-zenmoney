from pydantic import BaseModel
# from .utils import to_camel
from .instrument import Instrument
from .account import Account
from .budget import Budget
from .company import Company
from .user import User
from .tag import Tag
from .merchant import Merchant
from .reminder import Reminder
from .reminder_marker import ReminderMarker
from .transaction import Transaction
from .deletion_object import DeletionObject


class DiffObject(BaseModel):
    currentClientTimestamp: int | None = None # unix timestamp
    serverTimestamp: int # last sync unix timestamp
    forceFetch: list | None = None

    instrument: list[Instrument] | None = None
    company: list[Company] | None = None
    user: list[User] | None = None
    account: list[Account] | None = None
    tag: list[Tag] | None = None
    merchant: list[Merchant] | None = None
    budget: list[Budget] | None = None
    reminder: list[Reminder] | None = None
    reminderMarker: list[ReminderMarker] | None = None
    transaction: list[Transaction] | None = None

    deletion: list[DeletionObject] | None = None


    class Config:
        use_enum_values = True
