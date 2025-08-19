import pytest
import requests


BASE_URL = "https://ru.yougile.com/api-v2"
HEADERS = {
"Authorization":
"Bearer nuxFXzhKRaVyH1rrmSWVdRfURTkJOYHygmMQjggCPpmL6UktA6uYwYPOJvYdS2oM",
"Content-Type": "application/json"
}


# --- POST /api-v2/projects ---


@pytest.mark.positive
def test_create_project_success():
    my_project = {
    "title": "Госуслуги",
    "users": {
    "66a89519-0718-4600-93b1-72c61f2074e7": "worker"}
}
    response = requests.post(BASE_URL + '/projects',
    json=my_project, headers=HEADERS)
    assert response.status_code == 201


@pytest.mark.negative
def test_create_project_missing_name():
    data = {
    "user": "Missing name field"
}
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 404


# --- PUT /api-v2/projects/{id} ---
@pytest.mark.positive
def test_put_project_id():
    project_id = "e3dee103-5604-4c87-8e01-faa800997065"
    my_project_id = {
    "deleted": True,
    "title": "Госуслуги",
    "users": {
    "66a89519-0718-4600-93b1-72c61f2074e7": "worker"}
}
    response = requests.put(f"{BASE_URL}/projects/{project_id}",
    json=my_project_id, headers=HEADERS)
    assert response.status_code == 200


@pytest.mark.negative
def test_put_negative_id():
    project_id = " "
    my_project_id = {
    "deleted": True,
    "title": "ГосУслуги",
    "users": {
    "66a89519-0718-4600-93b1-72c61f2074e7": "worker"}
}
    response = requests.put(f"{BASE_URL}/projects/{project_id}",
    json=my_project_id, headers=HEADERS)
    assert response.status_code == 404


def test_get_project():
    project_id = "5d3305d1-8ce7-4260-80f2-6977caf7ef12"
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200


@pytest.mark.negative
def test_create_negative_get():
 project_id = ""
 url = f"{BASE_URL}/projects/{project_id}"
 response = requests.put(url, headers=HEADERS)
 assert response.status_code == 404
