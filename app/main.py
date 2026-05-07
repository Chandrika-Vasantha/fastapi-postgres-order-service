from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routes.order_routes import router as order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Order Service API",
    description="FastAPI backend service for managing customer orders.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Order Service API is running"}

app.include_router(order_router)
