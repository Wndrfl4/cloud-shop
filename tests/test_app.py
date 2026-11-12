
from app import app


def test_addition():
    assert 2 + 2 == 4


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Cloud Shop" in response.data


def test_products():
    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json) == 5


def test_product_detail():
    client = app.test_client()
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json["name"] == "Gaming PC"


def test_product_not_found():
    client = app.test_client()
    response = client.get("/products/999")

    assert response.status_code == 404


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"
