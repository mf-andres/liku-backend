from unittest.mock import Mock

from liku_backend.birthday.application.gift_creator import GiftCreator
from liku_backend.birthday.application.gift_updater import GiftUpdater
from tests.liku_backend.utils import gift_mother


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update = Mock()
    gift_updater = GiftUpdater(gift_repository)
    gift = gift_mother.get_gift()
    gift_updater.invoke(gift)
    gift_repository.update.assert_called_once_with(gift)
