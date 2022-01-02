from typing import List

from pymongo import MongoClient

from liku_backend.birthday.infrastructure.errors import BirthdayDatabaseNotFoundError
from liku_backend.gift.domain.gift import Gift
from liku_backend.gift.domain.gift_repository import GiftRepository
from liku_backend.gift.infrastructure import gift_to_mongo_object_converter, mongo_object_to_gift_converter
from liku_backend.shared.infrastructure.mongo_repository import MongoRepository


class AtlasGiftRepository(GiftRepository):
    def __init__(
            self,
            password=str,
            database_name=str,
    ):
        self.password = password
        self.host = f"mongodb+srv://liku:{self.password}@cluster0.oib15.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.database_name = database_name
        self.collection_name = "gifts"
        self._connect()

    def _connect(self):
        try:
            self.database_connection = MongoClient(
                self.host, serverSelectionTimeoutMS=1000
            )
            self.database_connection.server_info()
            self.database = self.database_connection[self.database_name]
            self.collection = self.database[self.collection_name]
        except Exception:
            raise BirthdayDatabaseNotFoundError(f"Unable to connect to atlas database")

    def store(self, gift: Gift):
        gift_as_dict = gift_to_mongo_object_converter.invoke(gift)
        self.collection.insert_one(gift_as_dict)

    def update(self, gift: Gift):
        query = {"id_": gift.id_}
        update = {
            "$set": {
                "description": gift.description,
            }
        }
        self.collection.update_one(query, update)

    def remove(self, gift_id: str):
        query = {"id_": gift_id}
        self.collection.delete_one(query)

    def retrieve(self, user_id: str, birthday_id: str, gifted: bool) -> List[Gift]:
        query = {"user_id": user_id, "birthday_id": birthday_id, "gifted": gifted}
        cursor = self.collection.find(query, {"id": False})
        gifts_as_dict = list(cursor)
        gifts = mongo_object_to_gift_converter.convert_many(gifts_as_dict)
        return gifts

    def update_as_gifted(self, gift_id: str):
        query = {"id_": gift_id}
        update = {
            "$set": {
                "gifted": True,
            }
        }
        self.collection.update_one(query, update)

    def update_as_not_gifted(self, gift_id: str):
        query = {"id_": gift_id}
        update = {
            "$set": {
                "gifted": False,
            }
        }
        self.collection.update_one(query, update)

    def remove_dangling(self, user_id, birthday_id):
        query = {"user_id": user_id, "birthday_id": birthday_id}
        self.collection.delete_many(query)

    def empty(self):
        self.collection.delete_many({})
