from liku_backend.birthday.domain.birthday import Birthday
from liku_backend.birthday.domain.birthday_repository import BirthdayRepository


class BirthdayCreator:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    def invoke(self, birthday: Birthday):
        self.birthday_repository.store(birthday)
