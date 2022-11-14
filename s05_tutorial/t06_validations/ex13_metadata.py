from turtle import up, update
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str | None = Query(default=None, title='Query string', description='Query string for the items to search in the database', min_length=3)):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'XYZ'}
        ]}

    if q:
        results.update({'q': q})

    return results
