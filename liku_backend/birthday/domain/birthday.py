from datetime import date


class Birthday:
    def __init__(self, id_: str, user_id: str, birthday_person: str, date_: date):
        self.id_ = id_
        self.user_id = user_id
        self.birthday_person = birthday_person
        self.date_ = date_

# TODO validate
#  create vo for uuid objects
