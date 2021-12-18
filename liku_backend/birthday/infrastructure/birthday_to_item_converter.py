from typing import List

from liku_backend.birthday.domain.birthday import Birthday
from liku_backend.entrypoint.items.birthday_item import BirthdayItem


def convert_many(birthdays: List[Birthday]) -> List[BirthdayItem]:
    return [convert(birthday) for birthday in birthdays]


def convert(birthday: Birthday) -> BirthdayItem:
    return BirthdayItem(
        id=birthday.id_,
        userId=birthday.user_id,
        birthdayPerson=birthday.birthday_person,
        date=birthday.date_,
    )
