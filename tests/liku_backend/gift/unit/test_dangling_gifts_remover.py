from unittest.mock import Mock

from liku_backend.gift.application.dangling_gifts_remover import DanglingGiftsRemover


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.remove = Mock()
    dangling_gifts_remover = DanglingGiftsRemover(gift_repository)
    user_id = "user_id"
    birthday_id = "birthday_id"
    dangling_gifts_remover.invoke(user_id, birthday_id)
    gift_repository.remove_dangling.assert_called_once_with(user_id, birthday_id)
