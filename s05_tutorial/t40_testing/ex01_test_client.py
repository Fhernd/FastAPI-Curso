from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()


@app.get("/")
async def root():
    """
    Test client.
    
    :return: Mensaje de bienvenida en formato JSON.
    """
    return {"message": "Hello World"}
