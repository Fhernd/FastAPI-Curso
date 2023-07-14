from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_video_streamer():
    """
    This is a generator that yields bytes as it is received from a video stream.
    """
    for i in range(10):
        yield b'frame %s\n' % i


@app.get('/')
async def main():
    """
    This is a plain text response.
    """
    return StreamingResponse(fake_video_streamer())
