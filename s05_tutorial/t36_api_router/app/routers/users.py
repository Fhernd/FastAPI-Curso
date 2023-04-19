from fastapi import APIRouter

router = APIRouter()


@router.get("/users", tags=["users"])
async def read_users():
    """
    Get all users.

    -returns: a list of users
    """
    return [{"username": "Rick"}, {"username": "Morty"}]

