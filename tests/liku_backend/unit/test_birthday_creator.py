from unittest.mock import Mock

from liku_backend.birthday.application.birthday_creator import BirthdayCreator
from tests.liku_backend.utils import birthday_mother


def test_calls_birthday_repository():
    birthday_repository = Mock()
    birthday_repository.store = Mock()
    birthday_creator = BirthdayCreator(birthday_repository)
    birthday = birthday_mother.get_birthday()
    birthday_creator.invoke(birthday)
    birthday_repository.store.assert_called_once_with(birthday)
