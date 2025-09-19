from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World from FastAPI"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/items/")
def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "query": q}
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True   # default value

@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }
