from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": "Item not found", "item_id": item_id, 'code': status.HTTP_404_NOT_FOUND})
    
    return {"item": items[item_id]}
