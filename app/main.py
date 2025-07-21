from fastapi import FastAPI
from app import products, orders

app = FastAPI(
    title="Ecommerce Backend API",
    version="1.0.0"
)

app.include_router(products.router)
app.include_router(orders.router)
