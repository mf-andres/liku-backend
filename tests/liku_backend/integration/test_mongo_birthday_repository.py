from tests.liku_backend.utils import birthday_mother


def test_stores_one_birthday(mongo_birthday_repository_setup_and_teardown):
    mongo_birthday_repository = mongo_birthday_repository_setup_and_teardown
    birthday = birthday_mother.get_birthday()
    mongo_birthday_repository.store(birthday)
    birthdays = mongo_birthday_repository.retrieve(birthday.user_id)
    assert len(birthdays) == 1
