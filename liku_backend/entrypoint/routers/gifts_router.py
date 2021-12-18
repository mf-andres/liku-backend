from typing import List

from fastapi import APIRouter, Request, Query

from liku_backend.entrypoint.items.gift_item import GiftItem
from liku_backend.gift.application.gift_list_retriever import GiftListRetriever
from liku_backend.gift.infrastructure import gift_to_item_converter

router = APIRouter()


@router.get(
    "/gifts",
    status_code=200,
    response_model=List[GiftItem],
)
def get(request: Request, user_id: str = Query(..., alias="userId"), birthday_id: str = Query(..., alias="birthdayId")):
    gift_repository = request.app.gift_repository
    gift_retriever = GiftListRetriever(gift_repository)
    gifts = gift_retriever.invoke(user_id, birthday_id)
    gifts = gift_to_item_converter.convert_many(gifts)
    return gifts
