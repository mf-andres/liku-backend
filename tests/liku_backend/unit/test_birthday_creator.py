from unittest.mock import Mock
from datetime import date

from liku_backend.birthday.application.birthday_creator import BirthdayCreator
from liku_backend.birthday.domain.birthday import Birthday


def test_calls_birthday_repository():
    birthday_repository = Mock()
    birthday_repository.store = Mock()
    birthday_creator = BirthdayCreator(birthday_repository)
    birthday_person = "birthday_person"
    _date = date.today()
    birthday = Birthday(birthday_person, _date)
    birthday_creator.invoke(birthday)
    birthday_repository.store.assert_called_once_with(birthday)
