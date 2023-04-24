from typing import Annotated
from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    """
    Get token header.

    :param: x_token: Token header
    -returns: token header
    """
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail='X-Token header invalid')


async def get_query_token(token: str):
    """
    Get query token.

    :param: token: Query token
    -returns: query token
    """
    if token != 'jessica':
        raise HTTPException(status_code=400, detail='Query token invalid')
