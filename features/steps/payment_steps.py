from behave import given, when, then
from src.adapters.drivens.infra.providers.mercadopago_payment import MercadoPagoPixPaymentGateway
from src.adapters.drivens.infra.repositories.payment_repository import PaymentRepository

@given('the MercadoPago payment provider is configured correctly')
def step_configure_payment_provider(context):
    context.payment_provider = MercadoPagoPixPaymentGateway(config={"api_key": "valid_key"})

@given('a user initiates a payment of ${amount}')
def step_initiate_payment(context, amount):
    context.amount = float(amount)
    context.user_id = "user_123"

@when('the payment is processed through the MercadoPago provider')
def step_process_payment(context):
    context.result = context.payment_provider.process_payment(context.user_id, context.amount)

@then('the payment status should be "{status}"')
def step_verify_payment_status(context, status):
    assert context.result["status"] == status

@then('the user\'s account balance should be updated')
def step_verify_account_balance(context):
    account_balance = PaymentRepository().get_balance(context.user_id)
    assert account_balance == context.result["new_balance"]

@then('a payment confirmation should be sent to the user')
def step_verify_confirmation_sent(context):
    # Assuming a mock or check that verifies the confirmation was sent
    assert context.result["confirmation_sent"] == True
