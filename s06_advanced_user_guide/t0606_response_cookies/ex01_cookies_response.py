from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    """
    Set a cookie and return a message
    
    Parameters:
    - `response`: Response object
    
    Returns:
    - `dict`: A dictionary with a message
    """
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    
    return {"message": "Come to the dark side, we have cookies"}
