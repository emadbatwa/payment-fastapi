from abc import ABC, abstractmethod

class PaymentServiceInterface(ABC):
    @abstractmethod
    async def checkout(self, price: float) -> str:
        """Process payment and return transaction ID"""
        pass