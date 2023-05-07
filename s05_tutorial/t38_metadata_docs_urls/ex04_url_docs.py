from fastapi import FastAPI


app = FastAPI()


@app.get('/items/')
async def read_items():
    """
    Read items with all the information.
    
    :returns: List of items.
    """
    return [{'name': 'Juan'}]
