from unittest.mock import Mock

from liku_backend.birthday.application.gift_remover import GiftRemover


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.remove = Mock()
    gift_remover = GiftRemover(gift_repository)
    gift_id = "gift_id"
    gift_remover.invoke(gift_id)
    gift_repository.remove.assert_called_once_with(gift_id)
