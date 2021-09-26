from datetime import date, datetime
from typing import List

from liku_backend.birthday.domain.birthday import Birthday


def convert_many(birthdays_as_dict: List[dict]) -> List[Birthday]:
    return [convert(birthday_as_dict) for birthday_as_dict in birthdays_as_dict]


def convert(birthday_as_dict: dict) -> Birthday:
    return Birthday(
        birthday_as_dict["birthday_person"],
        convert_datetime_to_day(birthday_as_dict["date_"])
    )


def convert_datetime_to_day(datetime_: datetime) -> date:
    return date(datetime_.year, datetime_.month, datetime_.day)
