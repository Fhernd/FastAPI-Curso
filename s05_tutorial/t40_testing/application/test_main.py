from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_item():
    """
    Check that the endpoint returns the correct item.
    """
    
    response = client.get("/items/foo", headers={"X-Token": "llosavargasmario"})
    
    assert response.status_code == 200
    
    assert response.json() == {
        'id': 'foo',
        'title': 'Foo',
        'description': 'There goes my hero'
    }


def test_read_item_bad_token():
    """
    Check that the endpoint returns an error if the token is invalid.
    """
    
    response = client.get("/items/foo", headers={"X-Token": "mendozamario"})
    
    assert response.status_code == 400
    
    assert response.json() == {
        'detail': 'X-Token header invalid'
    }
