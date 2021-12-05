from unittest.mock import Mock

from liku_backend.birthday.application.gift_creator import GiftCreator
from liku_backend.birthday.application.gift_updater import GiftUpdater
from liku_backend.birthday.application.gifted_gift_marker import GiftedGiftMarker
from liku_backend.birthday.application.gifted_gift_unmarker import GiftedGiftUnmarker
from tests.liku_backend.utils import gift_mother


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update = Mock()
    gifted_gift_marker = GiftedGiftUnmarker(gift_repository)
    gift = gift_mother.get_gift()
    gifted_gift_marker.invoke(gift)
    gift_repository.update.assert_called_once_with(gift)
