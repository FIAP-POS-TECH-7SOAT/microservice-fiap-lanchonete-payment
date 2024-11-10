from dataclasses import dataclass

@dataclass
class ProcessPaymentResponse:
    id: str
    qr_code: str
    qr_code_base64: str
    status: str