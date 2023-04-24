from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_token_header


router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get('/')
async def read_items():
    """
    Get all items.

    -returns: a list of items
    """
    return fake_items_db


