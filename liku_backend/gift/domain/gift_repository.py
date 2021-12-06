import abc
from typing import List

from liku_backend.gift.domain.gift import Gift


class GiftRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, gift: Gift):
        pass

    @abc.abstractmethod
    def update(self, gift: Gift):
        pass

    @abc.abstractmethod
    def remove(self, gift_id: str):
        pass

    @abc.abstractmethod
    def retrieve(self, user_id: str, birthday_id: str, gifted: bool) -> List[Gift]:
        pass

    @abc.abstractmethod
    def update_as_gifted(self, gift_id: str):
        pass

    @abc.abstractmethod
    def update_as_not_gifted(self, gift_id: str):
        pass

    @abc.abstractmethod
    def remove_dangling(self, user_id, birthday_id):
        pass
