from abc import ABC, abstractmethod
from src.core.domain.models.payment_model import Payment

class IPaymentRepository(ABC):
    @abstractmethod
    def save(self, payment: Payment) -> None:
        """Save a payment record in the database."""
        pass

    @abstractmethod
    def find_by_order_id(self, order_id: str) -> Payment:
        """Retrieve a payment by its order ID."""
        pass

    @abstractmethod
    def update(self, payment_response: dict) -> None:
        """Update a payment by its order ID and status"""
        pass
