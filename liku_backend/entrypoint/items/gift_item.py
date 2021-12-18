from pydantic import BaseModel, Field


class GiftItem(BaseModel):
    id_: str = Field(..., alias="id")
    user_id: str = Field(..., alias="userId")
    birthday_id: str = Field(..., alias="birthdayId")
    gifted: bool = Field(..., alias="gifted")
    description: str = Field(..., alias="description")
