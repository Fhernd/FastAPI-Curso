from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()


@app.get("/")
async def read_main():
    """
    Test client.
    
    :return: Mensaje de bienvenida en formato JSON.
    """
    return {"message": "Hello World"}


client = TestClient(app)


def test_read_main():
    """
    Test client.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
