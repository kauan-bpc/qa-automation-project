import pytest
import requests
from faker import Faker
fake = Faker()

@pytest.fixture
def new_order():
    return {
        "id": fake.random_number(digits=4),
        "petId": fake.random_number(digits=4),
        "quantity": 2,
        "status": "placed"
    }

def test_get_order_by_id(base_url_api, new_order):
    # Criar um pedido para garantir que ele exista
    response = requests.post(f"{base_url_api}/store/order", json=new_order)
    assert response.status_code == 200

    # Obter o pedido criado
    response = requests.get(f"{base_url_api}/store/order/{new_order['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == new_order["id"]
    assert response.json()["petId"] == new_order["petId"]
    assert response.json()["quantity"] == new_order["quantity"]
    assert response.json()["status"] == new_order["status"]

def test_delete_order(base_url_api, new_order):
    # Criar um pedido para garantir que ele exista
    response = requests.post(f"{base_url_api}/store/order", json=new_order)
    assert response.status_code == 200

    # Deletar o pedido criado
    response = requests.delete(f"{base_url_api}/store/order/{new_order['id']}")
    assert response.status_code == 200

