from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    product_name: str
    quantity: int
    price: float

class OrderResponse(OrderCreate):
    id: int

    class Config:
        from_attributes = True
