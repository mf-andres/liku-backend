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


# def test_removes_one_gift(mongo_gift_repository_setup_and_teardown):
#     mongo_gift_repository = mongo_gift_repository_setup_and_teardown
#     gift = gift_mother.get_gift()
#     mongo_gift_repository.store(gift)
#     mongo_gift_repository.remove(gift.id_)
#     gifts = mongo_gift_repository.retrieve(gift.user_id, gift.birthday_id)
#     assert len(gifts) == 0
