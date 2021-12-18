from typing import List

from fastapi import APIRouter, Request, Query

from liku_backend.birthday.application.birthday_retriever import BirthdayRetriever
from liku_backend.birthday.infrastructure import birthday_to_item_converter
from liku_backend.entrypoint.items.birthday_item import BirthdayItem

router = APIRouter()


@router.get(
    "/birthdays",
    status_code=200,
    response_model=List[BirthdayItem],
)
def get(request: Request, user_id: str = Query(..., alias="userId")):
    birthday_repository = request.app.birthday_repository
    birthday_retriever = BirthdayRetriever(birthday_repository)
    birthdays = birthday_retriever.invoke(user_id)
    birthdays = birthday_to_item_converter.convert_many(birthdays)
    return birthdays
