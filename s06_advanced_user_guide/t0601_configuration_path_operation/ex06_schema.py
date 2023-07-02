from fastapi import FastAPI, Request

app = FastAPI()


def magic_data_render(raw_body: bytes):
    return {
        'size': len(raw_body),
        'content': {
            'name': 'Maaagic! 🧙‍♂️',
            'price': 42,
            'description': "Just kiddin', no magic here. ✨"
        }
    }
    

@app.post("/items/", openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["name", "price"],
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "price": {"type": "number"},
                            "description": {"type": "string"},
                        },
                    }
                }
            },
            "required": True,
        },
    }
)
async def create_item(request: Request):
    """
    This endpoint is documented with OpenAPI extra data.
    
    Parameters:
    ----------
    request: Request: FastAPI request object.
    
    
    Returns:
    -------
    dict: A dict with the following structure:
    """
    raw_body = await request.body()
    data = magic_data_render(raw_body)
    
    return data
