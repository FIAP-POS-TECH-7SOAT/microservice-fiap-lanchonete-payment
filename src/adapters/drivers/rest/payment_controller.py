from flask import Blueprint, render_template, request, jsonify, redirect
from marshmallow import ValidationError

from src.core.domain.application.ports.providers.dtos.process_payment_request_dto import ProcessPaymentRequest
from src.core.domain.application.ports.providers.dtos.success_payment_response_dto import SuccessPaymentResponse
from src.core.domain.application.use_cases.process_payment_use_case import ProcessPaymentUseCase
from src.core.domain.application.use_cases.success_payment_use_case import SuccessPaymentUseCase
from src.core.domain.application.services.payment_service import PaymentService

def payment_bp(payment_service:PaymentService):
    payment_blueprint = Blueprint('payment', __name__)

    @payment_blueprint.route("/", methods=["POST"])
    def process_payment():
        process_payment_use_case = ProcessPaymentUseCase(payment_service)

        payload = ProcessPaymentRequest(
            amount=request.json['amount'],
            order_id=request.json['order_id'],
            customer=request.json.get('customer')
        )
        try:
            result = process_payment_use_case.execute(payload)

            if result.status == 'pending':
                return render_template("qr_code.html", external_link=result.qr_code, base64_image=result.qr_code_base64)
            else:
                return render_template("error.html", message="Payment failed")
        
        except ValidationError as ex:
            return jsonify({"error":str(ex)}), 400
        
    @payment_blueprint.route("/success", methods=["GET"])
    def success_payment():

        success_payment_use_case = SuccessPaymentUseCase(payment_service)

        payload = SuccessPaymentResponse(
            order_id=request.json['order_id'],
            status=request.json.get('status')
        )

        try:
            success_payment_use_case.execute(payload)

            return redirect("http://www.site.com", code=302)
        
        except ValidationError as ex:
            return jsonify({"error":str(ex)}), 400

    return payment_blueprint
