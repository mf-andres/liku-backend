import pytest

from liku_backend.birthday.infrastructure.mongo_birthday_repository import MongoBirthdayRepository


@pytest.fixture
def mongo_birthday_repository_setup_and_teardown():
    mongo_birthday_repository = MongoBirthdayRepository(
        host="localhost",
        port=27017,
        user="root",
        password="root",
        database_name="liku"
    )
    mongo_birthday_repository.empty()
    yield mongo_birthday_repository
    mongo_birthday_repository.empty()
