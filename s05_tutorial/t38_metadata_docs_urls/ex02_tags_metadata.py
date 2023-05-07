from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
]


app = FastAPI(openapi_tags=tags_metadata)


@app.get("/users/", tags=["Users"])
async def get_users():
    """
    Get all users.
    
    :returns: List of users.
    """
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/", tags=["Items"])
async def get_items():
    """
    Get all items.
    
    :returns: List of items.
    """
    return [{"name": "wand"}, {"name": "flying broom"}]
