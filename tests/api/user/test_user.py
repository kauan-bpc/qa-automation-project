import pytest
import requests
from faker import Faker

fake = Faker()

#dados de teste para criar um usuário
@pytest.fixture
def new_user():
    return {
        "id": fake.random_int(min=1000, max=9999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": 1
    }

#teste de criar um usuário
def test_create_user(base_url_api, new_user):
    response = requests.post(f"{base_url_api}/user", json=new_user)

    assert response.status_code == 200
    assert response.json()["code"] == 200

def test_get_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)

    response = requests.get(f"{base_url_api}/user/{new_user['username']}")

    assert response.status_code == 200
    assert response.json()["username"] == new_user["username"]
    assert response.json()["email"] == new_user["email"]

def test_delete_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)

    response = requests.delete(f"{base_url_api}/user/{new_user['username']}")

    assert response.status_code == 200
   