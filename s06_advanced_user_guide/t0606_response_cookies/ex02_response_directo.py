from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post('/cookie/')
def create_cookie():
    """
    Set a cookie and return a message.
    """
    contenido = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=contenido)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    
    return response
