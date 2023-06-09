from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_read_item():
    """
    Check that the endpoint returns the correct item.
    """
    response = client.get("/items/foo", headers={"X-Token": "llosavargasmario"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    """
    Check that the endpoint returns an error if the token is invalid.
    """
    
    response = client.get("/items/foo", headers={"X-Token": "mendozamario"})
    
    assert response.status_code == 400
    
    assert response.json() == {
        'detail': 'Invalid X-Token header'
    }


def test_create_item():
    """
    Check that the endpoint creates an item.
    """
    
    response = client.post(
        '/items/',
        headers={"X-Token": "llosavargasmario"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    """
    Check that the endpoint returns an error if the token is invalid.
    """
    response = client.post(
        "/items/",
        headers={"X-Token": "mendozamario"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    
    assert response.status_code == 400
    print(response.json())
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "llosavargasmario"},
        json={
            "id": "foobar",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}
