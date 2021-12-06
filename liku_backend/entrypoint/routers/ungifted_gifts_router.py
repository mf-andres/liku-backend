from typing import List

from fastapi import APIRouter, Request

from liku_backend.entrypoint.items.gift_item import GiftItem
from liku_backend.gift.application.gifted_gift_list_retriever import GiftedGiftListRetriever
from liku_backend.gift.infrastructure import gift_to_item_converter

router = APIRouter()


@router.get(
    "/ungifted-gifts",
    status_code=200,
    response_model=List[GiftItem],
)
def get(request: Request, user_id: str, birthday_id: str):
    gift_repository = request.app.gift_repository
    gift_retriever = GiftedGiftListRetriever(gift_repository)
    gifts = gift_retriever.invoke(user_id, birthday_id)
    gifts = gift_to_item_converter.convert_many(gifts)
    return gifts
