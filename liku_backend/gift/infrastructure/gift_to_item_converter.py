from typing import List

from liku_backend.entrypoint.items.gift_item import GiftItem
from liku_backend.gift.domain.gift import Gift


def convert_many(gifts: List[Gift]) -> List[GiftItem]:
    return [convert(gift) for gift in gifts]


def convert(gift: Gift) -> GiftItem:
    return GiftItem(
        id=gift.id_,
        userId=gift.user_id,
        birthdayId=gift.birthday_id,
        gifted=gift.gifted,
        description=gift.description,
    )
