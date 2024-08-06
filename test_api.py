import requests


ENDPOINT = "http://127.0.0.1:8000/api/Item_list/"

def test_can_get_objects():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_object():
    payload ={
        "name": "test name",
        "category": "test category",
        "description": "test desc",
        "quantity": 1 
    }

    response = requests.post(ENDPOINT,json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)

    global object_id
    object_id = data['id']
    get_object_response = requests.get(ENDPOINT + f"{object_id}/")
    assert get_object_response.status_code == 200

    get_object = get_object_response.json()
    print(get_object)

    assert get_object["name"] == payload["name"]
    assert get_object["category"] == payload["category"]
    assert get_object["description"] == payload["description"]
    assert get_object["quantity"] == payload["quantity"]


def test_can_update_object():
    payload = {
        "name": "Renetti 1",
        "category": "firearm",
        "description": "custom wooden design granulated grip-tape",
        "quantity": 15
    }

    response = requests.put(ENDPOINT + f"{object_id}/",json=payload)
    assert response.status_code == 200

    get_object_response = requests.put(ENDPOINT +f"{object_id}/",json=payload )
    assert response.status_code == 200

    get_object = get_object_response.json()
    print(get_object)

    assert get_object["name"] == payload["name"]
    assert get_object["category"] == payload["category"]
    assert get_object["description"] == payload["description"]
    assert get_object["quantity"] == payload["quantity"]


def test_can_delete():

    delete_object = requests.delete(ENDPOINT +f"{object_id}")
    assert delete_object.status_code ==204

    
    