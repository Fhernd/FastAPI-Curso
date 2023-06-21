import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """
    Check that the endpoint returns the correct item.
    """
    a = 'a'
    b = a + 'b'
    
    return {'hello world': b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
