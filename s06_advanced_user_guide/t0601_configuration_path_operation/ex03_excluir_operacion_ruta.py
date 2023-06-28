from fastapi import FastAPI

app = FastAPI()


@app.get('/items/', include_in_schema=False)
async def read_items():
    """
    Lee un conjunto de ítems.
    
    :return: Lista de ítems.
    """
    return [{'item_id': 'Foo'}]
