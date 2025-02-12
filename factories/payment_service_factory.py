from enums.payment_method_enum import PaymentMethod
from services.applepay_service import ApplePayService
from services.paypal_service import PayPalService
from interfaces.payment_service_interface import PaymentServiceInterface

class PaymentServiceFactory:
    @staticmethod
    def create(payment_method: PaymentMethod) -> PaymentServiceInterface:
        service_mapping = {
            PaymentMethod.PAYPAL: PayPalService,
            PaymentMethod.APPLE_PAY: ApplePayService,
        }
        service_class = service_mapping.get(payment_method)
        if service_class: return service_class()
        else: raise ValueError(f"Unsupported payment method: {payment_method}")
