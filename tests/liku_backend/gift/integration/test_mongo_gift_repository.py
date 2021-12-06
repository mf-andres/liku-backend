from tests.liku_backend.gift.utils import gift_mother


def test_stores_one_gift(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gift = gift_mother.get_gift()
    mongo_gift_repository.store(gift)
    gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id, gifted=False)
    assert len(gifts) == 1


def test_updates_one_gift(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gift = gift_mother.get_gift()
    mongo_gift_repository.store(gift)
    gift.description = "description_2"
    mongo_gift_repository.update(gift)
    gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id, gifted=False)
    assert gifts[0].description == gift.description


def test_removes_one_gift(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gift = gift_mother.get_gift()
    mongo_gift_repository.store(gift)
    mongo_gift_repository.remove(gift.id_)
    gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id, gifted=False)
    assert len(gifts) == 0


def test_updates_one_gift_as_gifted(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gift = gift_mother.get_gift()
    mongo_gift_repository.store(gift)
    mongo_gift_repository.update_as_gifted(gift.id_)
    gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id, gifted=True)
    assert len(gifts) == 1


def test_updates_one_gifted_gift_as_not_gifted(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gifted_gift = gift_mother.get_gifted_gift()
    mongo_gift_repository.store(gifted_gift)
    mongo_gift_repository.update_as_not_gifted(gifted_gift.id_)
    gifted_gifts = mongo_gift_repository.retrieve(gifted_gift.user_id, gifted_gift.birthday_id, gifted=True)
    assert len(gifted_gifts) == 0


def test_removes_dangling_gifts(mongo_gift_repository_setup_and_teardown):
    mongo_gift_repository = mongo_gift_repository_setup_and_teardown
    gift = gift_mother.get_gift()
    mongo_gift_repository.store(gift)
    mongo_gift_repository.store(gift)
    mongo_gift_repository.store(gift)
    mongo_gift_repository.remove_dangling(gift.user_id, gift.birthday_id)
    gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id, gifted=False)
    assert len(gifts) == 0
