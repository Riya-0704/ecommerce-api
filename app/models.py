from pydantic import BaseModel
from typing import List

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    sizes: List[str]

class ProductOut(ProductCreate):
    id: str

class OrderCreate(BaseModel):
    user_id: str
    products: List[str]
    total_price: float

class OrderOut(OrderCreate):
    id: str
