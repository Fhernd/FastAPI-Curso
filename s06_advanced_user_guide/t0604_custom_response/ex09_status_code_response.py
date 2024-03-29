from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/pydantic', response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    """
    Redirect to a website.
    """
    return 'https://pydantic-docs.helpmanual.io/'
