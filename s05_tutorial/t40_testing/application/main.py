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