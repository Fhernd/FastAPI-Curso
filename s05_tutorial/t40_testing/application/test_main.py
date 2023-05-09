from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "llosavargasmario"})
    
    assert response.status_code == 200
    
    assert response.json() == {
        'id': 'foo',
        'title': 'Foo',
        'description': 'There goes my hero'
    }
