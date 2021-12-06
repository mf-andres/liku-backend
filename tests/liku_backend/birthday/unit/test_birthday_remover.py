from unittest.mock import Mock

from liku_backend.birthday.application.birthday_remover import BirthdayRemover


def test_calls_birthday_repository():
    birthday_repository = Mock()
    birthday_repository.remove = Mock()
    birthday_remover = BirthdayRemover(birthday_repository)
    birthday_id = "birthday_id"
    birthday_remover.invoke(birthday_id)
    birthday_repository.remove.assert_called_once_with(birthday_id)
