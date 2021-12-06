from typing import List

from liku_backend.birthday.domain.birthday import Birthday
from liku_backend.birthday.domain.birthday_repository import BirthdayRepository
from liku_backend.birthday.infrastructure import birthday_to_mongo_object_converter, mongo_object_to_birthday_converter
from liku_backend.shared.infrastructure.mongo_repository import MongoRepository


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

    def update(self, birthday: Birthday):
        query = {"id_": birthday.id_}
        birthday_as_dict = birthday_to_mongo_object_converter.invoke(birthday)
        update = {
            "$set": {
                "birthday_person": birthday_as_dict["birthday_person"],
                "date_": birthday_as_dict["date_"],
            }
        }
        self.collection.update_one(query, update)

    def remove(self, birthday_id: str):
        query = {"id_": birthday_id}
        self.collection.delete_one(query)

    def retrieve(self, user_id: str) -> List[Birthday]:
        query = {"user_id": user_id}
        cursor = self.collection.find(query, {"id": False})
        birthdays_as_dict = list(cursor)
        birthdays = mongo_object_to_birthday_converter.convert_many(birthdays_as_dict)
        return birthdays

    def empty(self):
        self.collection.delete_many({})
