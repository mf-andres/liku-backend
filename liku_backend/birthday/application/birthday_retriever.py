from liku_backend.birthday.domain.birthday_repository import BirthdayRepository


class BirthdayRetriever:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    def invoke(self, user_id: str):
        return self.birthday_repository.retrieve(user_id)
