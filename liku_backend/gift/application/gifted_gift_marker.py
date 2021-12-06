from liku_backend.gift.domain.gift_repository import GiftRepository


class GiftedGiftMarker:
    def __init__(self, gift_repository: GiftRepository):
        self.gift_repository = gift_repository

    def invoke(self, gift_id: str):
        self.gift_repository.update_as_gifted(gift_id)
