Feature: Application Configuration
  To ensure the application functions correctly
  Configurations should be loaded and validated accurately

  Scenario: Successful configuration load
    Given the application has access to all necessary environment variables
    When the configuration file is loaded
    Then the application should load the configuration successfully

  Scenario: Missing required environment variable
    Given the application configuration is missing the "API_KEY" variable
    When the configuration file is loaded
    Then the application should throw a "ConfigurationError"
    And the error message should indicate "API_KEY is missing"

  Scenario: Invalid API endpoint format
    Given the configuration includes an invalid API endpoint URL format
    When the configuration file is loaded
    Then the application should throw a "ConfigurationError"
    And the error message should indicate "Invalid API endpoint format"

  Scenario: Validating configuration reload after update
    Given the application is already running with valid configuration
    When the configuration is updated with new values
    Then the application should reload the configuration successfully
