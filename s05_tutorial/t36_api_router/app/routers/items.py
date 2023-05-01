from fastapi import APIRouter, Depends, HTTPException

import dependencies


router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(dependencies.get_token_header)],
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


@router.get('/{item_id}')
async def read_item(item_id: str):
    """
    Get a specific item.

    :param: item_id: Item ID
    -returns: a specific item
    """
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail='Item not found')
    
    return fake_items_db[item_id]


@router.put('/{item_id}', tags=['custom'], responses={403: {'description': 'Operation forbidden'}})
async def update_item(item_id: str):
    """
    Update a specific item.

    :param: item_id: Item ID
    -returns: a specific item
    """
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail='Item not found')
    
    return {'item_id': item_id, 'name': 'The great Plumbus'}
