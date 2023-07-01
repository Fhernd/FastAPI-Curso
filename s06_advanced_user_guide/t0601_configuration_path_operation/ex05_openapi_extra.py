from fastapi import FastAPI

app = FastAPI(
    title='My Super Project',
    openapi_extra={
        "info": {
            "contact": {
                "name": "Soporte",
                "url": "https://example.com/contacto",
                "email": "soporte@example.com",
            },
            "termsOfService": "https://example.com/terminos",
        },
    },
)


@app.get("/items/", openapi_extra={"x-aperture-labs-portal": "blue"})
async def read_items():
    return [{"item_id": "portal-gun"}]
