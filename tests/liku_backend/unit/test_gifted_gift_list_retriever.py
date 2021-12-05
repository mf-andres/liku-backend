from unittest.mock import Mock

from liku_backend.birthday.application.gift_list_retriever import GiftListRetriever
from liku_backend.birthday.application.gifted_gift_list_retriever import GiftedGiftListRetriever


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update = Mock()
    gift_list_retriever = GiftedGiftListRetriever(gift_repository)
    user_id = "user_id"
    birthday_id = "birthday_id"
    gift_list_retriever.invoke(user_id, birthday_id)
    gift_repository.retrieve.assert_called_once_with(user_id, birthday_id, gifted=True)
