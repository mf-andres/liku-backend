from fastapi import APIRouter, Request

from liku_backend.birthday.application.birthday_creator import BirthdayCreator
from liku_backend.birthday.application.birthday_remover import BirthdayRemover
from liku_backend.birthday.application.birthday_updater import BirthdayUpdater
from liku_backend.birthday.infrastructure import item_to_birthday_converter
from liku_backend.entrypoint.items.birthday_item import BirthdayItem

router = APIRouter()


@router.post(
    "/birthday",
    status_code=201,
    response_model=None,
)
def post(request: Request, birthday: BirthdayItem):
    birthday = item_to_birthday_converter.invoke(birthday)
    birthday_repository = request.app.birthday_repository
    birthday_creator = BirthdayCreator(birthday_repository)
    birthday_creator.invoke(birthday)


@router.put(
    "/birthday",
    status_code=200,
    response_model=None,
)
def put(request: Request, birthday: BirthdayItem):
    birthday = item_to_birthday_converter.invoke(birthday)
    birthday_repository = request.app.birthday_repository
    birthday_updater = BirthdayUpdater(birthday_repository)
    birthday_updater.invoke(birthday)


@router.delete(
    "/birthday/{birthday_id}",
    status_code=200,
    response_model=None,
)
def post(request: Request, birthday_id: str):
    birthday_repository = request.app.birthday_repository
    birthday_remover = BirthdayRemover(birthday_repository)
    birthday_remover.invoke(birthday_id)
