from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/', response_class=PlainTextResponse)
async def main():
    """
    This is a plain text response.
    """
    return '¡Hola, Mundo!'
