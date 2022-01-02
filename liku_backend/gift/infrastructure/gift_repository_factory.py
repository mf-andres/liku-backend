from liku_backend.gift.infrastructure.atlas_gift_repository import AtlasGiftRepository
from liku_backend.gift.infrastructure.mongo_gift_repository import MongoGiftRepository
from liku_backend.shared.infrastructure.settings import Settings


def get_repository(settings: Settings):
    if settings.gift_repository_type == "mongo":
        return MongoGiftRepository(
            host=settings.gift_repository_host,
            port=settings.gift_repository_port,
            user=settings.gift_repository_user,
            password=settings.gift_repository_password,
            database_name=settings.gift_repository_database_name,
        )
    if settings.gift_repository_type == "atlas":
        return AtlasGiftRepository(
            password=settings.gift_repository_password,
        )
    raise NotImplemented("wrong repository type")
