from liku_backend.gift.domain.gift_repository import GiftRepository


class GiftedGiftListRetriever:
    def __init__(self, gift_repository: GiftRepository):
        self.gift_repository = gift_repository

    def invoke(self, user_id: str, birthday_id: str):
        self.gift_repository.retrieve(user_id, birthday_id, gifted=True)
