from fastapi import FastAPI
from schemas.payment_request import PaymentRequest
from schemas.payment_response import PaymentResponse
from factories.payment_service_factory import PaymentServiceFactory

app = FastAPI()

@app.post("/api/pay", response_model=PaymentResponse)
async def process_payment(payment_request: PaymentRequest):
    payment_service = PaymentServiceFactory.create(payment_request.method)

    transaction_id = await payment_service.checkout(payment_request.price)
    return PaymentResponse(transaction_id=transaction_id)