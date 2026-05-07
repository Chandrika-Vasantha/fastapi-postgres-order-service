from fastapi import FastAPI

app = FastAPI(
    title="Order Service API",
    description="FastAPI backend service for managing customer orders.",
    version="1.0.0"
)

orders = []

@app.get("/")
def home():
    return {"message": "Order Service API is running"}

@app.get("/orders")
def get_orders():
    return {"orders": orders}

@app.post("/orders")
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order created successfully", "order": order}
