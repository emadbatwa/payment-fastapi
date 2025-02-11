from interfaces.payment_service_interface import PaymentServiceInterface
import uuid

class PayPalService(PaymentServiceInterface):
    async def checkout(self, price: float) -> str:
        transaction_id = f"PP-{uuid.uuid4()}"
        return transaction_id