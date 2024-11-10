from flask import Flask

from src.adapters.drivens.infra.providers.mercadopago_payment import MercadoPagoPixPaymentGateway
from src.adapters.drivens.infra.repositories.payment_repository import PaymentRepository
from src.core.domain.application.services.payment_service import PaymentService
from src.core.domain.application.use_cases.process_payment_use_case import ProcessPaymentUseCase
from src.core.domain.application.use_cases.retrieve_payment_use_case import RetrievePaymentUseCase
from src.adapters.drivers.rest.payment_controller import payment_bp
from src.config import db
from src.adapters.drivens.infra.settings import ENV

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payment.db'
db.init_app(app)

env = ENV()
payment_gateway = MercadoPagoPixPaymentGateway(env.TOKEN_MELI)
payment_repository = PaymentRepository() 
payment_service = PaymentService(payment_gateway, payment_repository)

process_payment_use_case = ProcessPaymentUseCase(payment_service)
retrieve_payment_use_case = RetrievePaymentUseCase(payment_repository)

#BLUEPRINTS ADD
app.register_blueprint(payment_bp(payment_service))

if __name__ == "__main__":
    app.run(debug=True)
