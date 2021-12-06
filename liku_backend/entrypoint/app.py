from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from liku_backend.birthday.infrastructure.mongo_birthday_repository import MongoBirthdayRepository
from liku_backend.entrypoint.routers import birthday_router, birthdays_router, gift_router, gifts_router, \
    ungifted_gifts_router
from liku_backend.gift.infrastructure.mongo_gift_repository import MongoGiftRepository

app = FastAPI(
    title="Liku Backend",
)


def inject_dependencies():
    app.birthday_repository = MongoBirthdayRepository(
        host="localhost",
        port=27017,
        user="root",
        password="root",
        database_name="liku"
    )
    app.gift_repository = MongoGiftRepository(
        host="localhost",
        port=27017,
        user="root",
        password="root",
        database_name="liku"
    )


def include_routers():
    app.include_router(birthday_router.router, tags=["birthday"])
    app.include_router(birthdays_router.router, tags=["birthdays"])
    app.include_router(gift_router.router, tags=["gift"])
    app.include_router(gifts_router.router, tags=["gifts"])
    app.include_router(ungifted_gifts_router.router, tags=["ungifted gifts"])


def configure_cors():
    origins = ["http://localhost:4200"]
    app.add_middleware(
        CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )


inject_dependencies()
include_routers()
configure_cors()
