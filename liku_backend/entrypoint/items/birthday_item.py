from datetime import date

from pydantic import BaseModel


class BirthdayItem(BaseModel):
    id_: str
    user_id: str
    birthday_person: str
    date_: date
