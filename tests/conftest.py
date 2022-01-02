import pytest

from liku_backend.birthday.infrastructure.mongo_birthday_repository import MongoBirthdayRepository
from liku_backend.gift.infrastructure.mongo_gift_repository import MongoGiftRepository
from liku_backend.shared.infrastructure.settings import Settings

settings = Settings()


@pytest.fixture
def mongo_birthday_repository_setup_and_teardown() -> MongoBirthdayRepository:
    mongo_birthday_repository = MongoBirthdayRepository(
        host=settings.birthday_repository_host,
        port=settings.birthday_repository_port,
        user=settings.birthday_repository_user,
        password=settings.birthday_repository_password,
        database_name=settings.birthday_repository_database_name,
    )
    mongo_birthday_repository.empty()
    yield mongo_birthday_repository
    mongo_birthday_repository.empty()


@pytest.fixture
def mongo_gift_repository_setup_and_teardown() -> MongoGiftRepository:
    mongo_gift_repository = MongoGiftRepository(
        host=settings.gift_repository_host,
        port=settings.gift_repository_port,
        user=settings.gift_repository_user,
        password=settings.gift_repository_password,
        database_name=settings.gift_repository_database_name,
    )
    mongo_gift_repository.empty()
    yield mongo_gift_repository
    mongo_gift_repository.empty()
