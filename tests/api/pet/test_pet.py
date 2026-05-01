import pytest
import requests 
from faker import Faker

fake = Faker()

@pytest.fixture
def new_pet():
    return {
        "id": fake.random_int(min=1000, max=9999),
        "name": fake.first_name(),
        "status": "available"
    }

#teste de criar um pet
def test_create_pet(base_url_api, new_pet):
    response = requests.post(f"{base_url_api}/pet", json=new_pet)

    assert response.status_code == 200
    assert response.json()["id"] == new_pet["id"]
    assert response.json()["name"] == new_pet["name"]
    assert response.json()["status"] == new_pet["status"]


#teste do get pet by id
def test_get_pet(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)

    response = requests.get(f"{base_url_api}/pet/{new_pet['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == new_pet["id"]
    assert response.json()["name"] == new_pet["name"]
    assert response.json()["status"] == new_pet["status"]

#teste de deletar um pet
def test_delete_pet(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)

    response = requests.delete(f"{base_url_api}/pet/{new_pet['id']}")

    assert response.status_code == 200