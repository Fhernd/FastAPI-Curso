from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tags(Enum):
    items = 'items'
    users = 'users'


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, tags=[Tags.items])
async def create_item(item: Item):
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{'name': 'foo', 'price': 42}]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{'username': 'johno'}]
