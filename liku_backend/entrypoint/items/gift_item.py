from pydantic import BaseModel


class GiftItem(BaseModel):
    id_: str
    user_id: str
    birthday_id: str
    gifted: bool
    description: str
