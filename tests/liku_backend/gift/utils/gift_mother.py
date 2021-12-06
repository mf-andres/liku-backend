from liku_backend.gift.domain.gift import Gift


def get_gift():
    id_ = "id_"
    user_id = "user_id"
    birthday_id = "birthday_id"
    gifted = False
    description = "description"
    birthday = Gift(id_, user_id, birthday_id, gifted, description)
    return birthday
