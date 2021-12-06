from unittest.mock import Mock

from liku_backend.birthday.application.birthday_updater import BirthdayUpdater
from tests.liku_backend.birthday.utils import birthday_mother


def test_calls_birthday_repository():
    birthday_repository = Mock()
    birthday_repository.update = Mock()
    birthday_updater = BirthdayUpdater(birthday_repository)
    birthday = birthday_mother.get_birthday()
    birthday_updater.invoke(birthday)
    birthday_repository.update.assert_called_once_with(birthday)
