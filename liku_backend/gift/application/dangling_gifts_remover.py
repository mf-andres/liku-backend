from liku_backend.gift.domain.gift_repository import GiftRepository


class DanglingGiftsRemover:
    def __init__(self, gift_repository: GiftRepository):
        self.gift_repository = gift_repository

    def invoke(self, user_id: str, birthday_id: str):
        self.gift_repository.remove_dangling(user_id, birthday_id)
