from liku_backend.gift.domain.gift import Gift


def invoke(gift: Gift) -> dict:
    return {
        "id_": gift.id_,
        "user_id": gift.user_id,
        "birthday_id": gift.birthday_id,
        "gifted": gift.gifted,
        "description": gift.description,
    }
