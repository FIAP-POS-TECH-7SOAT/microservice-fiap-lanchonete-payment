from src.config import db

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100), nullable=False)
    qr_code = db.Column(db.String(120), nullable=True)
    gateway_info = db.Column(db.String(20), nullable=True)
    total_amount = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Payment {self.order_id}>"