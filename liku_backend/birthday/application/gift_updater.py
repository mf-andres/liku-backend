from liku_backend.birthday.domain.gift import Gift
from liku_backend.birthday.domain.gift_repository import GiftRepository


class GiftUpdater:
    def __init__(self, gift_repository: GiftRepository):
        self.gift_repository = gift_repository

    def invoke(self, gift: Gift):
        self.gift_repository.update(gift)
