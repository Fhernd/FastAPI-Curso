from fastapi import FastAPI, Response

app = FastAPI()


@app.get('/legacy/')
def get_legacy_data():
    """
    This endpoint returns a legacy data.
    
    Returns:
    --------
    Response: Response. Respuesta en formato XML.
    """
    
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    
    return Response(content=data, media_type='application/xml')
