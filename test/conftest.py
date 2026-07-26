from httpx import request
import pytest
from pydantic import BaseModel, EmailStr
from clients.auth.auth_client import AuthenticationClient, get_auth_client
from clients.courses.courses_schema import CreateCourseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_user_client
from clients.users.public_users_client import PublicUserClient, get_public_users_client
from clients.users.usersSchema import CreateUserRequestSchema, CreateUserResponseSchema

class UserFixture(BaseModel):

    request : CreateUserRequestSchema
    response : CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password
    
    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_auth_client()

@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client() 

@pytest.fixture
def private_user_client(function_user : UserFixture) -> PrivateUsersClient:
    return get_private_user_client(function_user.authentication_user)


@pytest.fixture
def function_user(public_users_client : PublicUserClient) ->  UserFixture:
    
    create_user_request = CreateUserRequestSchema()
    response = public_users_client.create_user(create_user_request)

    return UserFixture(request = create_user_request, response = response) 

