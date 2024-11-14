from behave import given, when, then
from src.adapters.drivens.infra.env.settings import ENV
from src.exceptions import ConfigurationError

@given('the application has access to all necessary environment variables')
def step_all_env_variables_present(context):
    context.config = ENV()

@given('the application configuration is missing the "{variable}" variable')
def step_missing_env_variable(context, variable):
    context.config = ENV()
    del context.config[variable]  # Mocking a missing variable

@given('the configuration includes an invalid API endpoint URL format')
def step_invalid_api_endpoint(context):
    context.config = ENV()
    context.config['API_ENDPOINT'] = "invalid_url"

@when('the configuration file is loaded')
def step_load_configuration(context):
    try:
        context.config.load()
        context.config_error = None
    except ConfigurationError as e:
        context.config_error = str(e)

@then('the application should load the configuration successfully')
def step_verify_successful_load(context):
    assert context.config_error is None

@then('the application should throw a "ConfigurationError"')
def step_verify_configuration_error(context):
    assert context.config_error is not None

@then('the error message should indicate "{message}"')
def step_verify_error_message(context, message):
    assert message in context.config_error
