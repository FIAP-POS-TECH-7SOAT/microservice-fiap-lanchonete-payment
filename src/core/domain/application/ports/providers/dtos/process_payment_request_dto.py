from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class ProcessPaymentRequest:
    amount: float
    order_id: str
    customer: Optional[Dict[str, str]] = None 
