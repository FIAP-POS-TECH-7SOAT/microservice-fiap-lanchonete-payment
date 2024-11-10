from core.domain.application.ports.providers.dtos.success_payment_response_dto import SuccessPaymentResponse
from src.core.domain.application.ports.services.Ipayment_service import IPaymentService
from src.core.domain.application.ports.repositories.Ipayment_repository import IPaymentRepository
from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.process_payment_response_dto import ProcessPaymentResponse
from src.core.domain.models.payment_model import Payment

class PaymentService(IPaymentService):
    def __init__(self, payment_gateway, payment_repository: IPaymentRepository):
        self.payment_gateway = payment_gateway
        self.payment_repository = payment_repository

    def process_payment(self, payment_request: ProcessPaymentRequest) -> ProcessPaymentResponse:
        payment_result = self.payment_gateway.process_payment(payment_request)
        
        new_payment = Payment(
            order_id=payment_request.order_id,
            gateway_info="MercadoPago",
            qr_code=payment_result.qr_code,
            total_amount=payment_request.amount,
            status=payment_result.status
        )
        self.payment_repository.save(new_payment)

        return payment_result
    
    def success_payment(self, payment_response: SuccessPaymentResponse):
        try:
            self.payment_repository.update(order_id=payment_response.id)
        
        except:
            pass
