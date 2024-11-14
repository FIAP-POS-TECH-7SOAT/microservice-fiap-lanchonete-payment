Feature: REST API for Payment Processing
  As a user of the REST API
  I want to interact with payment endpoints
  So that I can initiate payments, check statuses, and handle errors

  Scenario: Successful payment initiation through REST API
    Given a valid payment request payload with amount $100.00
    When the request is sent to the "/" endpoint
    Then the API should return a status code 200
    And the response body should contain "status: Success"
    And a "id" should be present in the response

  Scenario: Invalid request payload
    Given a payment request payload missing the "amount" field
    When the request is sent to the "/" endpoint
    Then the API should return a status code 400
    And the response body should contain an error message "Missing required field: amount"

  Scenario: Querying payment status
    Given a previously successful payment with transaction ID "12345"
    When the request is sent to "/api/payment/status/12345"
    Then the API should return a status code 200
    And the response should indicate "status: Success"

  Scenario: Invalid transaction ID for payment status
    Given a non-existent transaction ID "99999"
    When the request is sent to "/api/payment/status/99999"
    Then the API should return a status code 404
    And the response body should contain an error message "Transaction not found"