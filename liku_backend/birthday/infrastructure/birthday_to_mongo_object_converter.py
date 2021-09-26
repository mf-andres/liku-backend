from datetime import datetime, date

from liku_backend.birthday.domain.birthday import Birthday


def invoke(birthday: Birthday) -> dict:
    return {
        "birthday_person": birthday.birthday_person,
        "date_": convert_date_to__datetime(birthday.date_)
    }


def convert_date_to__datetime(date_: date) -> datetime:
    return datetime(date_.year, date_.month, date_.day)
