class Gift:
    def __init__(self, id_: str, user_id: str, birthday_id: str, gifted: bool, description: str):
        self.id_ = id_
        self.user_id = user_id
        self.birthday_id = birthday_id
        self.gifted = gifted
        self.description = description

# TODO validate
#  value objects uuid
