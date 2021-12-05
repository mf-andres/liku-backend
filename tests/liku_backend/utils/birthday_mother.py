from datetime import date

from liku_backend.birthday.domain.birthday import Birthday


def get_birthday():
    id_ = "id_"
    user_id = "user_id"
    birthday_person = "birthday_person"
    date_ = date.today()
    birthday = Birthday(id_, user_id, birthday_person, date_)
    return birthday
