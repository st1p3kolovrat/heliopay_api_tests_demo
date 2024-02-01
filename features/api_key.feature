Feature: Api Key endpoint

###################################################################################
###############################  Positive Scenarios  ##############################
###################################################################################

  @not-implemented
  Scenario: User can generate new api key
    Given I generate new api key
    Then the response code is "201"
    Then json_schema looks as expected

###################################################################################
###############################  Negative Scenarios  ##############################
###################################################################################

  @not-implemented
  Scenario Outline: User cannot generate new api key with <invalid_jwt_authorization> authorization
    Given I attempt to generate new api key with <invalid_jwt_authorization>
    Then the response code is "<status_code>"
    And I see error message displaying <error_msg>
    Examples:
      | invalid_jwt_authorization | <status_code | error_msg                               |
      | jwt_not_provided          | 401          | {"message": "Unauthorized","code": 401} |
      | jwt_expired               | 401          | {"message": "Unauthorized","code": 401} |
      | bearer_text_missing       | 401          | {"message": "Unauthorized","code": 401} |

  @not-implemented
  Scenario: User cannot generate new api key with missing origin in the header
    Given I attempt to generate new api key with "missing origin"
    Then the response code is "400"
    And I see error message displaying "{"message": "The origin header is missing","code": 400}"

  @not-implemented
  Scenario: User cannot generate new api key with invalid origin
    Given I attempt to generate new api key with "invalid origin domain"
    Then the response code is "400"
    And I see error message displaying "{"message": "The jwt domain is incorrect: https://dummy.dev.hel.io !== app.dev.hel.io","code": 400}"

  @not-implemented
  Scenario: Without jwt user cannot generate new api key
    Given I generate new api key
    Then expected error message is thrown
    And the response code is "201"