from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get('/items/{item_id}/{price}')
async def read_items(
    q: str | None = Query(default=None, alias='item-query'),
    item_id: int = Path(title='The ID of the item to get')
):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})
    
    return results
