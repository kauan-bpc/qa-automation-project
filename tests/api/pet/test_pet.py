import pytest
import requests
from faker import Faker

fake = Faker()


@pytest.fixture
def new_pet():
    return {
        "id": fake.random_int(min=10000, max=99999),
        "name": fake.first_name(),
        "status": "available",
        "photoUrls": ["https://example.com/photo.jpg"]
    }


def test_create_pet(base_url_api, new_pet):
    response = requests.post(f"{base_url_api}/pet", json=new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == new_pet["name"]
    assert response.json()["status"] == "available"


def test_get_pet_by_id(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)
    response = requests.get(f"{base_url_api}/pet/{new_pet['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == new_pet["id"]


def test_update_pet(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)
    new_pet["status"] = "sold"
    response = requests.put(f"{base_url_api}/pet", json=new_pet)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"


def test_update_pet_with_form_data(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)
    response = requests.post(
        f"{base_url_api}/pet/{new_pet['id']}",
        data={"name": "NomeAtualizado", "status": "pending"}
    )
    assert response.status_code == 200
    assert response.json()["code"] == 200


def test_delete_pet(base_url_api, new_pet):
    requests.post(f"{base_url_api}/pet", json=new_pet)
    response = requests.delete(f"{base_url_api}/pet/{new_pet['id']}")
    assert response.status_code == 200


def test_find_pets_by_status(base_url_api):
    response = requests.get(f"{base_url_api}/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_upload_pet_image(base_url_api, new_pet, tmp_path):
    requests.post(f"{base_url_api}/pet", json=new_pet)
    image = tmp_path / "foto.png"
    image.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)
    with open(image, "rb") as f:
        response = requests.post(
            f"{base_url_api}/pet/{new_pet['id']}/uploadImage",
            files={"file": ("foto.png", f, "image/png")}
        )
    assert response.status_code == 200
    assert response.json()["code"] == 200