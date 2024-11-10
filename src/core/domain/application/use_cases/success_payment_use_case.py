from src.core.domain.application.ports.services.Ipayment_service import IPaymentService
from src.core.domain.application.ports.providers.dtos.success_payment_response_dto import SuccessPaymentResponse


class SuccessPaymentUseCase:
    def __init__(self, payment_service: IPaymentService):
        self.payment_service = payment_service

    def execute(self, payment_response: SuccessPaymentResponse):
        """Executes the payment processing logic."""
        
        return self.payment_service.success_payment(payment_response)
