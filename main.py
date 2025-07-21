from fastapi import FastAPI
from models import Product, Order
from crud import create_product, get_products, create_order, get_orders_by_user

app = FastAPI()

@app.post("/products")
async def add_product(product: Product):
    return await create_product(product)

@app.get("/products")
async def fetch_products():
    return await get_products()

@app.post("/orders")
async def place_order(order: Order):
    return await create_order(order)

@app.get("/orders/{user_id}")
async def fetch_orders(user_id: str):
    return await get_orders_by_user(user_id)
