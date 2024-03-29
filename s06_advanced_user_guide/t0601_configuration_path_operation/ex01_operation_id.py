from fastapi import FastAPI

app = FastAPI()


@app.get('/items/', operation_id='some_specific_id_you_define')
async def read_items():
    """
    Lee un conjunto de ítems.
    
    :return: Lista de ítems.
    """
    return [{'item_id': 'Foo'}]
