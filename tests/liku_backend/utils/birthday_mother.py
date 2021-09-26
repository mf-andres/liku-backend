from datetime import date

from liku_backend.birthday.domain.birthday import Birthday


def get_birthday():
    birthday_person = "birthday_person"
    date_ = date.today()
    birthday = Birthday(birthday_person, date_)
    return birthday
