from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get('/')
def main():
    """
    This is a plain text response.
    """
    def iterfile():
        with open('video.mp4', mode='rb') as file:
            yield from file
    
    return StreamingResponse(iterfile(), media_type='video/mp4')
