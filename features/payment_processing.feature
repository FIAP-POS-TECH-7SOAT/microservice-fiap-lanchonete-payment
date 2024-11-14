Feature: Payment Processing
  As a user of the payment system
  I want to be able to process payments through MercadoPago
  So that I can complete transactions securely and efficiently

  Background:
    Given the MercadoPago payment provider is configured correctly

  Scenario: Successful payment processing
    Given a user initiates a payment of $50.00
    When the payment is processed through the MercadoPago provider
    Then the payment status should be "Success"
    And the user's account balance should be updated
    And a payment confirmation should be sent to the user

  Scenario: Failed payment due to insufficient funds
    Given a user initiates a payment of $5000.00
    When the payment is processed through the MercadoPago provider
    Then the payment status should be "Failed"
    And the reason should indicate "Insufficient Funds"
    And no charge should be made to the user's account

  Scenario: Payment provider configuration error
    Given the MercadoPago provider is not configured correctly
    When a user tries to process a payment
    Then the system should return an error message indicating "Configuration Error"
    And the payment status should be "Failed"
