from liku_backend.birthday.domain.birthday import Birthday
from liku_backend.entrypoint.items.birthday_item import BirthdayItem


def invoke(birthday_item: BirthdayItem) -> Birthday:
    return Birthday(
        birthday_item.id_,
        birthday_item.user_id,
        birthday_item.birthday_person,
        birthday_item.date_,
    )
