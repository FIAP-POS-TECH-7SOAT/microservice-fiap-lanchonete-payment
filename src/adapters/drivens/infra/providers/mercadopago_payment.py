import mercadopago
from mercadopago.config import RequestOptions
import uuid

from src.core.domain.application.ports.providers.Ipayment_gateway import IPaymentGateway
from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.process_payment_response_dto import ProcessPaymentResponse

class MercadoPagoPixPaymentGateway(IPaymentGateway):
    def __init__(self, access_token: str):
        self.client = mercadopago.SDK(access_token)
    
    def process_payment(self, payload: ProcessPaymentRequest) -> ProcessPaymentResponse:
        try:
            payment_data = {
                "transaction_amount": payload.amount,
                "description": payload.order_id,
                "payment_method_id": "pix",
                "notification_url": "https://www.suaurl.com/notificacoes/",
                "external_reference": payload.order_id,
                "payer": payload.customer if payload.customer else {
                    "email": "non-valid@mail.com"
                }
            }
            if payload.customer:
                payment_data["payer"] = {
                    "email": payload.customer["email"],
                    "identification": {
                        "type": "CPF",
                        "number": payload.customer["doc_number"]
                    }
                }
            
            request_options = RequestOptions()
            request_options.custom_headers = {
                "x-idempotency-key": str(uuid.uuid4())
            }
            
            payment_response = self.client.payment().create(payment_data, request_options)
            payment_info = payment_response.get("response", {})
            
            return ProcessPaymentResponse(
                id=str(payment_info.get("id")),
                qr_code=payment_info.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code", ""),
                qr_code_base64=payment_info.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code_base64", ""),
                status=payment_info.get("status", "")
            )
        
        except Exception as error:
            raise RuntimeError(f"Failed to process payment: {error}")
