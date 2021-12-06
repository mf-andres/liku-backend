from liku_backend.entrypoint.items.gift_item import GiftItem
from liku_backend.gift.domain.gift import Gift


def invoke(gift_item: GiftItem) -> Gift:
    return Gift(
        gift_item.id_,
        gift_item.user_id,
        gift_item.birthday_id,
        gift_item.gifted,
        gift_item.description,
    )
