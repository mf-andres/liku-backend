from liku_backend.birthday.infrastructure.atlas_birthday_repository import AtlasBirthdayRepository
from liku_backend.birthday.infrastructure.mongo_birthday_repository import MongoBirthdayRepository
from liku_backend.shared.infrastructure.settings import Settings


def get_repository(settings: Settings):
    if settings.birthday_repository_type == "mongo":
        return MongoBirthdayRepository(
            host=settings.birthday_repository_host,
            port=settings.birthday_repository_port,
            user=settings.birthday_repository_user,
            password=settings.birthday_repository_password,
            database_name=settings.birthday_repository_database_name,
        )
    if settings.birthday_repository_type == "atlas":
        return AtlasBirthdayRepository(
            password=settings.birthday_repository_password,
        )
    raise NotImplemented("wrong repository type")
