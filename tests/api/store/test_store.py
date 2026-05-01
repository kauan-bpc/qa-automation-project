import pytest
import requests
from faker import Faker

fake = Faker()


@pytest.fixture
def new_order():
    return {
        "id": fake.random_int(min=10000, max=99999),
        "petId": fake.random_int(min=10000, max=99999),
        "quantity": 2,
        "status": "placed"
    }


def test_create_order(base_url_api, new_order):
    response = requests.post(f"{base_url_api}/store/order", json=new_order)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"
    assert response.json()["quantity"] == new_order["quantity"]


def test_get_order_by_id(base_url_api, new_order):
    requests.post(f"{base_url_api}/store/order", json=new_order)
    response = requests.get(f"{base_url_api}/store/order/{new_order['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == new_order["id"]


def test_delete_order(base_url_api, new_order):
    requests.post(f"{base_url_api}/store/order", json=new_order)
    response = requests.delete(f"{base_url_api}/store/order/{new_order['id']}")
    assert response.status_code == 200


def test_get_inventory(base_url_api):
    response = requests.get(f"{base_url_api}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)