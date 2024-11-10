from src.core.domain.application.ports.repositories.Ipayment_repository import IPaymentRepository
from src.core.domain.models.payment_model import Payment

class RetrievePaymentUseCase:
    def __init__(self, payment_repository: IPaymentRepository):
        self.payment_repository = payment_repository

    def execute(self, order_id: str) -> Payment:
        """Retrieve payment details by order ID."""
        return self.payment_repository.find_by_order_id(order_id)
