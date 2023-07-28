from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/headers-and-object/")
def get_headers(response: Response):
    """
    Return the headers and an object.
    """
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}
