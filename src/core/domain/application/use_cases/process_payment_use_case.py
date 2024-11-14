from src.core.domain.application.services.Ipayment_service import IPaymentService
from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.process_payment_response_dto import ProcessPaymentResponse
from src.core.domain.validators.process_payment_request_validator import ProcessPaymentRequestValidator

from marshmallow import ValidationError


class ProcessPaymentUseCase:
    def __init__(self, payment_service: IPaymentService):
        self.payment_service = payment_service
        self.validator = ProcessPaymentRequestValidator()

    def execute(self, payment_request: ProcessPaymentRequest) -> ProcessPaymentResponse:
        """Executes the payment processing logic."""
        try:
            self.validator.load(payment_request.__dict__)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")
        
        return self.payment_service.process_payment(payment_request)
