from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    user_id: str
    items: List[str]  # product IDs as strings
