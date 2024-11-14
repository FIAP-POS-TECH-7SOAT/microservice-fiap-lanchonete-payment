from behave import given, when, then
from src.adapters.drivens.infra.repositories.payment_repository import PaymentRepository
from src.exceptions import DatabaseConnectionError

@given('a new payment record with transaction ID "{transaction_id}" and amount ${amount}')
def step_new_payment_record(context, transaction_id, amount):
    context.payment_record = {
        "transaction_id": transaction_id,
        "amount": float(amount),
        "user_id": "user_123",
        "status": "Pending"
    }

@given('a user with transaction history')
def step_user_with_history(context):
    context.user_id = "user_123"
    PaymentRepository().save_payment({
        "transaction_id": "history_1",
        "amount": 50.0,
        "status": "Success",
        "user_id": context.user_id
    })

@given('the database connection is unavailable')
def step_database_unavailable(context):
    context.repository = PaymentRepository()
    context.repository.database_connected = False  # Mocking a disconnection

@when('the record is saved to the payment repository')
def step_save_payment_record(context):
    try:
        context.result = PaymentRepository().save_payment(context.payment_record)
        context.db_error = None
    except DatabaseConnectionError as e:
        context.db_error = str(e)

@when("the user's transaction history is requested")
def step_request_transaction_history(context):
    context.history = PaymentRepository().get_history(context.user_id)

@when('the transaction is requested by its ID')
def step_request_transaction_by_id(context):
    context.transaction = PaymentRepository().get_payment_by_id(context.payment_record["transaction_id"])

@then('the repository should confirm the payment was saved successfully')
def step_verify_payment_saved(context):
    assert context.result == "Payment saved successfully"

@then('the repository should return a list of transactions')
def step_verify_transaction_history(context):
    assert isinstance(context.history, list)
    assert len(context.history) > 0

@then('the repository should return the correct transaction')
def step_verify_correct_transaction(context):
    assert context.transaction["transaction_id"] == context.payment_record["transaction_id"]

@then('the payment record should not be saved')
def step_verify_payment_not_saved(context):
    assert context.db_error is not None

@then('each transaction should contain an "{field}" and "{status}"')
def step_verify_transaction_fields(context, field, status):
    for transaction in context.history:
        assert field in transaction
        assert status in transaction
