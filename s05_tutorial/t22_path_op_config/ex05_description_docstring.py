from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post(
    "/items/",
    response_model=Item,
    tags=["items"],
    summary="Create an item and store it in the database")
async def create_item(item: Item):
    """
    Create an item with all the information, name, description, price, tax and a set of unique tags

    - **name**: each item must have a name
    - **description**: a description of the item
    - **price**: the price must be a positive float
    - **tax**: the tax must be a positive float
    - **tags**: a set of unique tags for this item
    """
    return item
