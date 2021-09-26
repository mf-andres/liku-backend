from typing import List

from liku_backend.birthday.domain.birthday import Birthday
from liku_backend.birthday.domain.birthday_repository import BirthdayRepository
from liku_backend.birthday.infrastructure import birthday_to_mongo_object_converter, mongo_object_to_birthday_converter
from liku_backend.birthday.infrastructure.mongo_repository import MongoRepository


class MongoBirthdayRepository(MongoRepository, BirthdayRepository):
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str,
    ):
        collection_name = "birthdays"
        super().__init__(
            host,
            port,
            user,
            password,
            database_name,
            collection_name
        )

    def store(self, birthday: Birthday):
        birthday_as_dict = birthday_to_mongo_object_converter.invoke(birthday)
        self.collection.insert_one(birthday_as_dict)

    def load(self) -> List[Birthday]:
        query = dict()
        cursor = self.collection.find(query, {"id": False})
        birthdays_as_dict = list(cursor)
        birthdays = mongo_object_to_birthday_converter.convert_many(birthdays_as_dict)
        return birthdays

    def empty(self):
        self.collection.delete_many({})
