from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str


app = FastAPI()


@app.get('/items/{item_id}', response_model=Item, responses={200: {"content": {'image/png': {}}, 'description': "Return the JSON item or an image."}})
async def read_item(item_id: str, img: Union[bool, None] = None):
    if img:
        return FileResponse('imagen.png', media_type='image/png')
    else:
        return {
            'id': 'foo',
            'value': 'there goes my hero'
        }
