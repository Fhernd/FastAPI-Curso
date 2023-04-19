from fastapi import APIRouter

router = APIRouter()


@router.get("/users", tags=["users"])
async def read_users():
    """
    Get all users.

    -returns: a list of users
    """
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    """
    Get current user.

    -returns: current user
    """
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    """
    Get a specific user.

    -returns: a specific user
    """
    return {"username": username}
