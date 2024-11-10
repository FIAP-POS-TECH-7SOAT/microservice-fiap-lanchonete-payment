from src.core.domain.application.ports.repositories.Ipayment_repository import IPaymentRepository
from src.core.domain.models.payment_model import Payment
from src.config import db

class PaymentRepository(IPaymentRepository):
    def save(self, payment: Payment) -> None:
        db.session.add(payment)
        db.session.commit()

    def find_by_order_id(self, order_id: str) -> Payment:
        return Payment.query.filter_by(order_id=order_id).first()
    
    def update(self, payload:Payment) -> None:
        payment = self.find_by_order_id(payload.order_id)
        payment.status = payload.status
        db.session.commit()
