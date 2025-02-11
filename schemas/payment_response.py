from pydantic import BaseModel

class PaymentResponse(BaseModel):
    id: str
    method: str
    price: float