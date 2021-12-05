from unittest.mock import Mock

from liku_backend.birthday.application.gift_creator import GiftCreator
from liku_backend.birthday.application.gift_updater import GiftUpdater
from liku_backend.birthday.application.gifted_gift_marker import GiftedGiftMarker
from tests.liku_backend.utils import gift_mother


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update_as_gifted = Mock()
    gifted_gift_marker = GiftedGiftMarker(gift_repository)
    gift_id = "gift_id"
    gifted_gift_marker.invoke(gift_id)
    gift_repository.update_as_gifted.assert_called_once_with(gift_id)
