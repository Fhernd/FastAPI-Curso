from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI()


@app.get('/items/')
async def read_items():
    return [{'item_id': 'Foo'}]


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    This function will iterate over all the routes in the app and set the operation_id to the route name.
    
    :param app: FastAPI instance
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
