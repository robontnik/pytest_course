from http import HTTPStatus

import pytest

from clients.auth.auth_client import AuthenticationClient, get_auth_client
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUserClient, get_public_users_client
from clients.users.usersSchema import CreateUserRequestSchema



from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema



@pytest.mark.regression
@pytest.mark.authentication
def test_login( function_user : UserFixture, public_users_client: PublicUserClient, authentication_client : AuthenticationClient):

    
    request = LoginRequestSchema(
        email = function_user.email,
        password = function_user.password
    )

    response  = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code,HTTPStatus.OK)
    assert_login_response(response_data)

    validate_json_schema(response.json(),response_data.model_json_schema())
 