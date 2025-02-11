from pydantic import BaseModel, Field
from enums.payment_method_enum import PaymentMethod

class PaymentRequest(BaseModel):
    price: float = Field(..., gt=0)
    method: PaymentMethod