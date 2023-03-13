from random import randint
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware que añade el tiempo de procesamiento de la petición.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/cargar-datos")
async def cargar_datos():
    """
    Simula la carga de datos.
    """
    time.sleep(randint(3, 7))
    datos = {"datos": "cargados"}
    return datos
