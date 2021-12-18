from datetime import date

from pydantic import BaseModel, Field


class BirthdayItem(BaseModel):
    id_: str = Field(..., alias="id")
    user_id: str = Field(..., alias="userId")
    birthday_person: str = Field(..., alias="birthdayPerson")
    date_: date = Field(..., alias="date")

