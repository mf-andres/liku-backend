from pymongo import MongoClient

from liku_backend.birthday.infrastructure.errors import BirthdayDatabaseNotFoundError


class MongoRepository:
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str,
            collection_name=str,
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name
        self.collection_name = collection_name
        self._connect()

    def _connect(self):
        try:
            self.database_connection = MongoClient(
                self.host, self.port, username=self.user, password=self.password, serverSelectionTimeoutMS=1000
            )
            self.database_connection.server_info()
            self.database = self.database_connection[self.database_name]
            self.collection = self.database[self.collection_name]
        except Exception:
            raise BirthdayDatabaseNotFoundError(f"Unable to connect to database at host={self.host}, port ={self.port}")

