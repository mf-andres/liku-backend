from tests.liku_backend.utils import birthday_mother


def test_stores_one_birthday(mongo_birthday_repository_setup_and_teardown):
    mongo_birthday_repository = mongo_birthday_repository_setup_and_teardown
    birthday = birthday_mother.get_birthday()
    mongo_birthday_repository.store(birthday)
    birthdays = mongo_birthday_repository.retrieve(birthday.user_id)
    assert len(birthdays) == 1


def test_updates_one_birthday(mongo_birthday_repository_setup_and_teardown):
    mongo_birthday_repository = mongo_birthday_repository_setup_and_teardown
    birthday = birthday_mother.get_birthday()
    mongo_birthday_repository.store(birthday)
    birthday.birthday_person = "birthday_person_2"
    mongo_birthday_repository.update(birthday)
    birthdays = mongo_birthday_repository.retrieve(birthday.user_id)
    assert birthdays[0].birthday_person == birthday.birthday_person


def test_removes_one_birthday(mongo_birthday_repository_setup_and_teardown):
    mongo_birthday_repository = mongo_birthday_repository_setup_and_teardown
    birthday = birthday_mother.get_birthday()
    mongo_birthday_repository.store(birthday)
    mongo_birthday_repository.remove(birthday.id_)
    birthdays = mongo_birthday_repository.retrieve(birthday.user_id)
    assert len(birthdays) == 0
