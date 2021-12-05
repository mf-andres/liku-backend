from liku_backend.birthday.domain.gift import Gift
from liku_backend.birthday.domain.gift_repository import GiftRepository


class GiftListRetriever:
    def __init__(self, gift_repository: GiftRepository):
        self.gift_repository = gift_repository

    def invoke(self, user_id: str, birthday_id: str):
        self.gift_repository.retrieve(user_id, birthday_id, gifted=False)
