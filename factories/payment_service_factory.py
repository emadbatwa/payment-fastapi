from enums.payment_method_enum import PaymentMethod
from services.applepay_service import ApplePayService
from services.paypal_service import PayPalService
from interfaces.payment_service_interface import PaymentServiceInterface

class PaymentServiceFactory:
    @staticmethod
    def create(payment_method: PaymentMethod) -> PaymentServiceInterface:
        if payment_method == PaymentMethod.PAYPAL: return PayPalService()
        elif payment_method == PaymentMethod.APPLE_PAY: return ApplePayService()
        raise ValueError(f"Unsupported payment method: {payment_method}")
