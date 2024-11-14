Feature: Payment Repository
  The payment repository should manage payment records accurately
  Including saving new payments and retrieving transaction history

  Scenario: Successfully saving a new payment record
    Given a new payment record with transaction ID "12345" and amount $150.00
    When the record is saved to the payment repository
    Then the repository should confirm the payment was saved successfully

  Scenario: Retrieving transaction history for a user
    Given a user with transaction history
    When the user’s transaction history is requested
    Then the repository should return a list of transactions
    And each transaction should contain an "amount" and "status"

  Scenario: Handling database connection failure
    Given the database connection is unavailable
    When a payment record is saved to the repository
    Then the repository should return an error message "Database connection error"
    And the payment record should not be saved

  Scenario: Retrieving a specific transaction by ID
    Given a payment with transaction ID "12345" exists in the repository
    When the transaction is requested by its ID
    Then the repository should return the correct transaction
    And the transaction details should include "amount", "status", and "timestamp"
