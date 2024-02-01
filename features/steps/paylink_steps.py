import json
import requests
from jsonpath_ng import parse
from behave import when, then
from assertpy import assert_that
from features.data.http_status_codes import CREATED_201


@when('I create a new paylink with "{payload_file}" payload')
def create_new_paylink(context, payload_file):
    full_endpoint_url = f"{context.base_url}/paylink/create/api-key"

    headers = {
        "Origin": "https://app.dev.hel.io",
        "Authorization": f"Bearer {context.secret_hash}"
    }
    query = {"apiKey": context.public_key}

    # Open and use payload from file
    with open(f"features/data/payload/{payload_file}", "r") as file:
        payload_dict = json.load(file)

    context.response = requests.post(full_endpoint_url, headers=headers, params=query, json=payload_dict)
    assert_that(context.response.status_code).is_equal_to(CREATED_201)


@when('I attempt to create a new paylink with "{header_authorization}" and "{query_api_key}" payload')
def create_new_paylink_header_query(context, header_authorization, query_api_key):
    full_endpoint_url = f"{context.base_url}/paylink/create/api-key"

    # Use valid_authorization from context or read form file.
    if header_authorization == "valid_authorization":
        header_authorization = context.secret_hash
    else:
        with open(f"features/data/authorization/{header_authorization}", "r") as file:
            header_authorization = file.read().strip()

    headers = {
        "Origin": "https://app.dev.hel.io",
        "Authorization": f"Bearer {header_authorization}"
    }

    # Use valid_api_key from context or read from file.
    if query_api_key == "valid_api_key":
        query_api_key = context.public_key
    else:
        with open(f"features/data/api_key/{query_api_key}") as file:
            query_api_key = file.read().strip()

    query = {"apiKey": query_api_key}

    # Use payload from file.
    with open(f"features/data/payload/create_paylink_sp.json", "r") as file:
        payload_dict = json.load(file)

    context.response = requests.post(full_endpoint_url, headers=headers, params=query, json=payload_dict)


@then('I confirm paylink is created')
def verify_paylink_created(context):
    # Grab paylink id
    jsonpath_expression = parse("$.id")
    context.paylink_id = [json_path.value for json_path in jsonpath_expression.find(context.response.json())]

    # Open json file / expected response
    with open("features/data/response/paylink_single_payment_created.json", "r") as file:
        expected_response = json.load(file)

    # Update the "id" in the json file / expected response.
    expected_response["id"] = context.paylink_id[0]
    # Assert response json is equal to json from a file.
    assert_that(context.response.json()).is_equal_to(expected_response)
