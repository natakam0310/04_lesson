import pytest
import requests
BASE_URL = "https://ru.yougile.com/api-v2/projects"
HEADERS = {
    "Authorization": "Bearer rc3WYFVI1546EP0jY4IIc41Gdutrl2a6Bi5TBdbTKRxFFF9fAYphBMgwNi0qVaCM",
    "Content-Type": "application/json"
}
# --- POST /api-v2/projects ---


@pytest.mark.positive
def test_create_project_success():
    data = {
        "name": "Госуслуги",
        "description": "Valid project creation"
    }
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
    json_data = response.json()
    assert "id" in json_data, f"'id' not found in response: {json_data}"
    assert json_data["name"] == data["name"]
   

@pytest.mark.negative
def test_create_project_missing_name():
    data = {
        "description": "Missing name field"
    }
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 400

# --- PUT /api-v2/projects/{id} ---

@pytest.mark.positive
def test_update_project_success():
    # Сначала создаем проект для обновления
    create_data = {"name": "Госуслуги", "description": "Temp"}
    create_resp = requests.post(BASE_URL, json=create_data, headers=HEADERS)
    project_id = create_resp.json()["id"]

    update_data = {"name": "Госуслуги обновление", "description": "Updated description"}
    put_resp = requests.put(f"{BASE_URL}/{project_id}", json=update_data, headers=HEADERS)
    assert put_resp.status_code == 200

    # Проверяем, что данные обновились
    get_resp = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert get_resp.status_code == 200
    project = get_resp.json()
    assert project["name"] == update_data["name"]
    assert project["description"] == update_data["description"]

@pytest.mark.negative
def test_update_project_not_found():
    invalid_id = 99999999
    update_data = {"name": "Nonexistent project"}
    response = requests.put(f"{BASE_URL}/{invalid_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 400

# --- GET /api-v2/projects/{id} ---

@pytest.mark.positive
def test_get_project_success():
    # Создаем проект для теста
    data = {"name": "Госуслуги GET", "description": "Test"}
    create_resp = requests.post(BASE_URL, json=data, headers=HEADERS)
    project_id = create_resp.json()["id"]

    get_resp = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert get_resp.status_code == 200
    project = get_resp.json()
    assert project["id"] == project_id
    assert project["name"] == data["name"]

@pytest.mark.negative
def test_get_project_not_found():
    invalid_id = 99999999
    response = requests.get(f"{BASE_URL}/{invalid_id}", headers=HEADERS)
    assert response.status_code == 404
