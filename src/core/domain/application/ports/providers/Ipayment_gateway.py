from abc import ABC, abstractmethod

from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.process_payment_response_dto import ProcessPaymentResponse

class IPaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, payload: ProcessPaymentRequest) -> ProcessPaymentResponse:
        pass