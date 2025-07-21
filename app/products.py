from fastapi import APIRouter
from app.database import product_collection
from app.models import ProductCreate, ProductOut
import re

router = APIRouter()

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "sizes": product["sizes"]
    }

@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(product: ProductCreate):
    product_doc = product.dict()
    result = await product_collection.insert_one(product_doc)
    product_doc["_id"] = result.inserted_id
    return product_helper(product_doc)

@router.get("/products")
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}

    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}

    if size:
        query["sizes"] = size

    cursor = product_collection.find(query).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        products.append(product_helper(product))

    return products
