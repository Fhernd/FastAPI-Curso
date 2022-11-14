from unittest import result
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(
    q: str
    | None = Query(
        default=None,
        alias='item-query',
        title='Query string',
        description='Query string for the items to search in the database',
        min_length=3,
        max_length=50,
        regex='^fixedquery$',
        deprecated=True
    )
):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'XYZ'}
        ]
    }

    if q:
        results.update({'q': q})
    
    return results
