import abc
from typing import List

from liku_backend.birthday.domain.gift import Gift


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
