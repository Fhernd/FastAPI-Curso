from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
