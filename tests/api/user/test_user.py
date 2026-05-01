import pytest
import requests
from faker import Faker

fake = Faker()


@pytest.fixture
def new_user():
    return {
        "id": fake.random_int(min=10000, max=99999),
        "username": fake.user_name() + fake.bothify("###"),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.numerify("##########"),
        "userStatus": 1
    }


def test_create_user(base_url_api, new_user):
    response = requests.post(f"{base_url_api}/user", json=new_user)
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_get_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)
    response = requests.get(f"{base_url_api}/user/{new_user['username']}")
    assert response.status_code == 200
    assert response.json()["username"] == new_user["username"]


def test_update_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)
    new_user["firstName"] = "NomeAtualizado"
    response = requests.put(f"{base_url_api}/user/{new_user['username']}", json=new_user)
    assert response.status_code == 200


def test_delete_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)
    response = requests.delete(f"{base_url_api}/user/{new_user['username']}")
    assert response.status_code == 200


def test_login_user(base_url_api, new_user):
    requests.post(f"{base_url_api}/user", json=new_user)
    response = requests.get(
        f"{base_url_api}/user/login",
        params={"username": new_user["username"], "password": new_user["password"]}
    )
    assert response.status_code == 200
    assert "logged in" in response.json()["message"].lower()


def test_logout_user(base_url_api):
    response = requests.get(f"{base_url_api}/user/logout")
    assert response.status_code == 200


def test_create_users_with_array(base_url_api, new_user):
    users = [new_user, {
        "id": fake.random_int(min=10000, max=99999),
        "username": fake.user_name() + fake.bothify("###"),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.numerify("##########"),
        "userStatus": 1
    }]
    response = requests.post(f"{base_url_api}/user/createWithArray", json=users)
    assert response.status_code == 200


def test_create_users_with_list(base_url_api, new_user):
    users = [new_user, {
        "id": fake.random_int(min=10000, max=99999),
        "username": fake.user_name() + fake.bothify("###"),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.numerify("##########"),
        "userStatus": 1
    }]
    response = requests.post(f"{base_url_api}/user/createWithList", json=users)
    assert response.status_code == 200