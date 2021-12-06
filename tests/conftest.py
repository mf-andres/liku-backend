import pytest

from liku_backend.birthday.infrastructure.mongo_birthday_repository import MongoBirthdayRepository
from liku_backend.gift.infrastructure.mongo_gift_repository import MongoGiftRepository


@pytest.fixture
def mongo_birthday_repository_setup_and_teardown() -> MongoBirthdayRepository:
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


@pytest.fixture
def mongo_gift_repository_setup_and_teardown() -> MongoGiftRepository:
    mongo_gift_repository = MongoGiftRepository(
        host="localhost",
        port=27017,
        user="root",
        password="root",
        database_name="liku"
    )
    mongo_gift_repository.empty()
    yield mongo_gift_repository
    mongo_gift_repository.empty()
