from typing import Any

import orjson
from fastapi import FastAPI, Response

app = FastAPI()


class CustomORJSONResponse(Response):
    media_type = 'application/json'

    def render(self, content: Any) -> bytes:
        """
        This method is called internally by FastAPI to render the response.
        """
        assert orjson is not None, 'orjson must be installed to use this response class'
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)


@app.get('/sin-orjson-custom')
def main():
    return {'message': 'Hello, World!'}


@app.get('/con-orjson-custom', response_class=CustomORJSONResponse)
def main_custom_orjson():
    return {'message': 'Hello, World!'}
