Feature: Paylink Endpoint

##################################################################################
##############################  Positive Scenarios  ##############################
##################################################################################

  Scenario: Unverified user can create new paylink
    Given I generate new api key
    When I create a new paylink with "create_paylink_sp.json" payload
    Then I confirm paylink is created

##################################################################################
#############################  Negative Scenarios  ###############################
##################################################################################

  Scenario Outline: Unverified user cannot create new paylink with "<invalid_payload_file>" payload
    Given I generate new api key
    When I make a "POST" request to "/paylink/create/api-key" with the "<invalid_payload_file>" payload
    Then the response code is "<status_code>"
    And I see error message with key "message" displaying "<error_msg>"

    Examples:
      | invalid_payload_file                           | status_code | error_msg             |
      | create_paylink_sp_without_features.json        | 400         | Bad Request Exception |
      | create_paylink_sp_without_name.json            | 400         | Bad Request Exception |
      | create_paylink_sp_without_pricingCurrency.json | 400         | Bad Request Exception |

  Scenario Outline: User cannot create paylink if auth token or api key is invalid
    Given I generate new api key
    When I attempt to create a new paylink with "<header_authorization>" and "<query_api_key>" payload
    Then the response code is "<status_code>"
    And I see error message with key "message" displaying "<error_msg>"

    Examples:
      | header_authorization         | query_api_key       | status_code | error_msg                   |
      | valid_authorization          | invalid_api_key.txt | 401         | Api key or token is invalid |
      | valid_authorization          | missing_api_key.txt | 401         | Api key or token is invalid |
      | invalid_authorization.txt    | valid_api_key       | 401         | Api key or token is invalid |
      | missing_authorization.txt    | valid_api_key       | 401         | Api key or token is invalid |
