from fastapi import APIRouter, Request

from liku_backend.entrypoint.items.gift_item import GiftItem
from liku_backend.gift.application.gift_creator import GiftCreator
from liku_backend.gift.application.gift_remover import GiftRemover
from liku_backend.gift.application.gift_updater import GiftUpdater
from liku_backend.gift.application.gifted_gift_marker import GiftedGiftMarker
from liku_backend.gift.application.gifted_gift_unmarker import GiftedGiftUnmarker
from liku_backend.gift.infrastructure import item_to_gift_converter

router = APIRouter()


@router.post(
    "/gift",
    status_code=201,
    response_model=None,
)
def post(request: Request, gift: GiftItem):
    gift = item_to_gift_converter.invoke(gift)
    gift_repository = request.app.gift_repository
    gift_creator = GiftCreator(gift_repository)
    gift_creator.invoke(gift)


@router.put(
    "/gift",
    status_code=200,
    response_model=None,
)
def put(request: Request, gift: GiftItem):
    gift = item_to_gift_converter.invoke(gift)
    gift_repository = request.app.gift_repository
    gift_updater = GiftUpdater(gift_repository)
    gift_updater.invoke(gift)


@router.delete(
    "/gift/{gift_id}",
    status_code=200,
    response_model=None,
)
def delete(request: Request, gift_id: str):
    gift_repository = request.app.gift_repository
    gift_remover = GiftRemover(gift_repository)
    gift_remover.invoke(gift_id)


@router.put(
    "/gift/{gift_id}/mark-as-gifted",
    status_code=200,
    response_model=None,
)
def mark_as_gifted(request: Request, gift_id: str):
    gift_repository = request.app.gift_repository
    gifted_gift_marker = GiftedGiftMarker(gift_repository)
    gifted_gift_marker.invoke(gift_id)


@router.put(
    "/gift/{gift_id}/unmark-as-gifted",
    status_code=200,
    response_model=None,
)
def unmark_as_gifted(request: Request, gift_id: str):
    gift_repository = request.app.gift_repository
    gifted_gift_unmarker = GiftedGiftUnmarker(gift_repository)
    gifted_gift_unmarker.invoke(gift_id)
