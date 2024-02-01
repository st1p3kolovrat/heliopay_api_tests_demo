import json
import requests
from behave import when, then
from assertpy import assert_that


@when('I make a "{request_method}" request to "{endpoint}" with the "{payload_file}" payload')
def send_request(context, request_method, endpoint, payload_file):
    full_endpoint_url = f"{context.base_url}{endpoint}"

    headers = {
        "Origin": "https://app.dev.hel.io",
        "Authorization": f"Bearer {context.secret_hash}"
    }
    query = {"apiKey": context.public_key}

    # Open and use payload from file
    with open(f"features/data/payload/{payload_file}", "r") as file:
        payload_dict = json.load(file)

    context.response = requests.request(request_method, full_endpoint_url, json=payload_dict, headers=headers,
                                        params=query)


@then('the response code is "{expected_status}"')
def expected_status_code(context, expected_status):
    assert_that(context.response.status_code).is_equal_to(int(expected_status))


@then('I see error message displaying "{expected_error_msg}"')
def error_msg(context, expected_error_msg):
    actual_error_msg = context.response.json()
    # Convert dict actual_error_msg into str
    actual_error_msg_str = json.dumps(actual_error_msg)

    assert_that(actual_error_msg_str).is_equal_to(expected_error_msg)


@then('I see error message with key "{key}" displaying "{expected_error_msg}"')
def error_msg_with_key(context, key, expected_error_msg):
    actual_raw_error_msg = context.response.json()

    if key not in actual_raw_error_msg:
        raise AssertionError(f"Provided key: '{key}' is not present in the error message")
    # Extract the key from actual_error_msg
    actual_error_msg = actual_raw_error_msg.get(key, "")

    assert_that(actual_error_msg).is_equal_to(expected_error_msg)
