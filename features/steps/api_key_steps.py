import os
import requests
from behave import given
from assertpy import assert_that
from features.data.http_status_codes import CREATED_201


@given('I generate new api key')
def new_api_key(context):
    full_endpoint_url = f"{context.base_url}/api-key"

    jwt_token = os.environ.get('JWT_TOKEN')
    headers = {
        "Origin": "https://app.dev.hel.io",
        "Authorization": f"Bearer {jwt_token}"
    }

    context.response = requests.post(full_endpoint_url, headers=headers)
    assert_that(context.response.status_code).is_equal_to(CREATED_201)

    response_json = context.response.json()
    # Store apiKey, publicKey, secretHash to into context
    context.api_key = response_json.get("apiKey")
    context.public_key = response_json.get("publicKey")
    context.secret_hash = response_json.get("secretHash")
    # Fail if one of the keys is none
    assert_that(context.api_key).is_not_none()
    assert_that(context.public_key).is_not_none()
    assert_that(context.secret_hash).is_not_none()
