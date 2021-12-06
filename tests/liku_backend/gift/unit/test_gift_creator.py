from unittest.mock import Mock

from liku_backend.gift.application.gift_creator import GiftCreator
from tests.liku_backend.gift.utils import gift_mother


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.store = Mock()
    gift_creator = GiftCreator(gift_repository)
    gift = gift_mother.get_gift()
    gift_creator.invoke(gift)
    gift_repository.store.assert_called_once_with(gift)
