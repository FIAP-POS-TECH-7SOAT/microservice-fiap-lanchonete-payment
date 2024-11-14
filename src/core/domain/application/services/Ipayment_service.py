from abc import ABC, abstractmethod
from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.success_payment_response_dto import SuccessPaymentResponse
from src.core.domain.application.ports.providers.dtos.process_payment_response_dto import ProcessPaymentResponse

class IPaymentService(ABC):
    @abstractmethod
    def process_payment(self, payment_request: ProcessPaymentRequest) -> ProcessPaymentResponse:
        """Process a payment and return the result."""
        pass

    @abstractmethod
    def success_payment(self, payment_request: SuccessPaymentResponse) -> ProcessPaymentResponse:
        """Update a payment"""
        pass
