from typing import List

from liku_backend.gift.domain.gift import Gift


def convert_many(gifts_as_dict: List[dict]) -> List[Gift]:
    return [convert(gift_as_dict) for gift_as_dict in gifts_as_dict]


def convert(gift_as_dict: dict) -> Gift:
    return Gift(
        gift_as_dict["id_"],
        gift_as_dict["user_id"],
        gift_as_dict["birthday_id"],
        gift_as_dict["gifted"],
        gift_as_dict["description"],
    )
