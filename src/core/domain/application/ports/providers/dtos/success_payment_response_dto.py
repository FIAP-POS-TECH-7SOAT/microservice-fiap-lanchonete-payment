from dataclasses import dataclass

@dataclass
class SuccessPaymentResponse:
    id: str
    status: str