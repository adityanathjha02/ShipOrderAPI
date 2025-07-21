from database import products_collection, orders_collection
from models import Product, Order

async def create_product(product: Product):
    result = await products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

async def get_products():
    products = []
    async for product in products_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products

async def create_order(order: Order):
    result = await orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

async def get_orders_by_user(user_id: str):
    orders = []
    async for order in orders_collection.find({"user_id": user_id}):
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders
