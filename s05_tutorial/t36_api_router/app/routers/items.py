from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_token_header


router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}},
)
