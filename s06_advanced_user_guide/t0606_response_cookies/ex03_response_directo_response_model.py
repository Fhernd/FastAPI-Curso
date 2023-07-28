from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    nombre: str


app = FastAPI()


@app.post('/cookie/', response_model=Item)
def create_cookie():
    """
    Set a cookie and return a message.
    """
    contenido = {"message": "Come to the dark side, we have cookies"}
    # contenido = {"id": "1", "nombre": "galleta"}
    response = JSONResponse(content=contenido)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    
    return response
