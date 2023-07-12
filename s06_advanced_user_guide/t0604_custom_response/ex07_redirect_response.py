from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/typer/')
async def redirect_typer():
    return RedirectResponse('https://www.openai.com/')
