from unittest.mock import Mock

from liku_backend.birthday.application.birthday_remover import BirthdayRetriever


def test_calls_birthday_repository():
    birthday_repository = Mock()
    birthday_repository.update = Mock()
    birthday_retriever = BirthdayRetriever(birthday_repository)
    user_id = "user_id"
    birthday_retriever.invoke(user_id)
    birthday_repository.retrieve.assert_called_once_with(user_id)
