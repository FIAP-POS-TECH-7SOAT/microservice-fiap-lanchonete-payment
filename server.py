from flask import Flask

from src.adapters.drivens.infra.providers.mercadopago_payment import MercadoPagoPixPaymentGateway
from src.adapters.drivens.infra.repositories.payment_repository import PaymentRepository
from src.core.domain.application.services.payment_service import PaymentService
from src.adapters.drivers.http.controllers.payment_controller import payment_bp
from src.adapters.drivens.infra.database.config import Config
from src.adapters.drivens.infra.env.settings import ENV
# from src.core.domain.application.use_cases.process_payment_use_case import ProcessPaymentUseCase
# from src.core.domain.application.use_cases.retrieve_payment_use_case import RetrievePaymentUseCase

app = Flask(__name__)
env = ENV()
config = Config()
app.config['SQLALCHEMY_DATABASE_URI'] = env.URL_DB
config.db.init_app(app)

payment_gateway = MercadoPagoPixPaymentGateway(env.TOKEN_MELI)
payment_repository = PaymentRepository() 
payment_service = PaymentService(payment_gateway, payment_repository)

# process_payment_use_case = ProcessPaymentUseCase(payment_service)
# retrieve_payment_use_case = RetrievePaymentUseCase(payment_repository)

#BLUEPRINTS ADD
app.register_blueprint(payment_bp(payment_service))

if __name__ == "__main__":
    app.run(debug=True)
