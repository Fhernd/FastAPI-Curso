from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)


@app.get('/items/')
async def read_items():
    """
    This is a default response class.
    """
    return [{'item_id': 'Foo'}]
