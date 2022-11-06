import pytest
from fastapi.testclient import TestClient
from src.app.app_prime import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


def test_is_prime_number(client):
    number = 86486646
    resp = client.get(f"/prime/{number}")
    assert resp.json() == {"false"}
