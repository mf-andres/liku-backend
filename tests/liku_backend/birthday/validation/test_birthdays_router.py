from starlette.testclient import TestClient

from liku_backend.entrypoint.app import app

client = TestClient(app)


def test_returns_no_birthdays(mongo_birthday_repository_setup_and_teardown):
    params = {"userId": "Andrés"}
    response = client.get("/birthdays", params=params)
    assert response.status_code == 200
    assert response.json() == []
