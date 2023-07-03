from typing import Annotated

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put('/items/{item_id}')
async def upsert_item(
    item_id: str,
    name: Annotated[str | None, Body()] = None,
    size: Annotated[int | None, Body()] = None,
):
    """
    If the item already exists, it will be updated.
    
    Parameters:
    ----------
    item_id: str: required
    
    Returns:
    -------
    JSONResponse: status_code=201 if the item was created, status_code=200 if it was updated.
    """
    if item_id in items:
        item = items[item_id]
        item['name'] = name
        item['size'] = size
        return item
    else:
        item = {'name': name, 'size': size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
