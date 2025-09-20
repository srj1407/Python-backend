from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
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

@app.get("/search/")
def search_items(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit}

class Address(BaseModel):
    city: str
    state: str
    country: str

class User(BaseModel):
    username: str
    email: str
    address: Address

@app.post("/users/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}