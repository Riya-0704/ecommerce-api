from fastapi import APIRouter, Path
from app.database import order_collection
from app.models import OrderCreate, OrderOut

router = APIRouter()

def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "products": order["products"],
        "total_price": order["total_price"]
    }

@router.post("/orders", response_model=OrderOut, status_code=201)
async def create_order(order: OrderCreate):
    order_doc = order.dict()
    result = await order_collection.insert_one(order_doc)
    order_doc["_id"] = result.inserted_id
    return order_helper(order_doc)

@router.get("/orders/{user_id}")
async def get_orders(
    user_id: str = Path(...),
    limit: int = 10,
    offset: int = 0
):
    query = {"user_id": user_id}
    cursor = order_collection.find(query).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        orders.append(order_helper(order))

    return orders
