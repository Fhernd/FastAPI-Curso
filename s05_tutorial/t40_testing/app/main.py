from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_main():
    """
    Test client.
    
    :return: Mensaje de bienvenida en formato JSON.
    """
    return {"message": "Hello World"}
