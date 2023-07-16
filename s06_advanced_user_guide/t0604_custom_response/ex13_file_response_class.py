
from fastapi import FastAPI
from fastapi.responses import FileResponse

ruta = 'video.mp4'

app = FastAPI()


@app.get('/', response_class=FileResponse)
async def main():
    """
    This is a file response.
    
    :return: FileResponse
    """
    return ruta
