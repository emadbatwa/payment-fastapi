from factories.payment_service_factory import PaymentServiceFactory
from models.db import SessionDep
from models.transaction import Transaction
from schemas.payment_request import PaymentRequest
from services.transaction_service import TransactionService


class PaymentService:
    @staticmethod
    async def process_payment_(payment_request: PaymentRequest, session: SessionDep):
        payment_service = PaymentServiceFactory.create(payment_request.method)
        transaction_id = await payment_service.checkout(payment_request.price)
        transaction = Transaction(id=transaction_id, method=payment_request.method.value, price=payment_request.price)
        return await TransactionService.store(transaction, session)
