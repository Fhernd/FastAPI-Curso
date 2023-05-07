from fastapi import FastAPI


app = FastAPI(openapi_url='/api/v1/openapi.json')


@app.get('/items/')
async def read_items():
    """
    Read items with all the information.
    
    :returns: List of items.
    """
    return [{'name': 'Juan'}]
