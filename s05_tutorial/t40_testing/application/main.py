from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel


fake_secret_token = "llosavargasmario"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()


class Item(BaseModel):
    """
    Representación de un item.
    """
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    """
    Busca un item en la base de datos.
    
    :param item_id: ID del item a buscar.
    :param x_token: Token de autenticación.
    """
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return fake_db[item_id]


@app.post("/items", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header(...)]):
    """
    Crea un item en la base de datos.
    
    :param item: Item a crear.
    :param x_token: Token de autenticación.
    """
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    fake_db[item.id] = item
    
    return item
