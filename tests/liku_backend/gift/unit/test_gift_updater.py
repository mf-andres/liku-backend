from unittest.mock import Mock

from liku_backend.gift.application.gift_updater import GiftUpdater
from tests.liku_backend.gift.utils import gift_mother


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update = Mock()
    gift_updater = GiftUpdater(gift_repository)
    gift = gift_mother.get_gift()
    gift_updater.invoke(gift)
    gift_repository.update.assert_called_once_with(gift)
