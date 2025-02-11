from pydantic import BaseModel, Field
from enums.payment_method_enum import PaymentMethod

class PaymentResponse(BaseModel):
    transaction_id: str