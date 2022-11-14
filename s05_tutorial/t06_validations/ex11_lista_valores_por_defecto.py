from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: list[str] = Query(default=['ABC', 'XYZ'])):
    query_items = {'q': q}

    return query_items
