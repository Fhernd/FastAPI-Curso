from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/typer/', response_class=RedirectResponse)
async def redirect_typer():
    """
    Redirect to a website.
    """
    return 'https://ortizol.blogspot.com'
