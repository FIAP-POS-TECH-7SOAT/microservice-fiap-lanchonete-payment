import requests
from behave import given, when, then

API_BASE_URL = "http://localhost:5000/"

@given('a valid payment request payload with amount ${amount}')
def step_valid_payment_payload(context, amount):
    context.payload = {
        "amount": float(amount),
        "order_id": "123456"
    }

@given('a payment request payload missing the "{field}" field')
def step_missing_field_in_payload(context, field):
    context.payload = {
        "amount": 100.00,
        "order_id": "123456"
    }
    del context.payload[field]  # Simulating missing field

@when('the request is sent to the "{endpoint}" endpoint')
def step_send_request_to_endpoint(context, endpoint):
    url = f"{API_BASE_URL}{endpoint}"
    context.response = requests.post(url, json=context.payload)

@when('the request is sent to "{endpoint}"')
def step_send_request_to_status_endpoint(context, endpoint):
    url = f"{API_BASE_URL}{endpoint}"
    context.response = requests.get(url)

@then('the API should return a status code {status_code}')
def step_verify_status_code(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response body should contain "{message}"')
def step_verify_response_body_contains_message(context, message):
    assert message in context.response.json()["message"]

@then('a "{field}" should be present in the response')
def step_verify_field_in_response(context, field):
    assert field in context.response.json()
