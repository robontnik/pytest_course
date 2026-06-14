

from httpx import Client

from clients.auth.auth_client import get_auth_client
from pydantic import BaseModel, EmailStr

from clients.auth.auth_schema import LoginRequestSchema

class AuthenticationUserSchema(BaseModel):

    email : EmailStr
    password : str

def get_private_http_client(user : AuthenticationUserSchema) -> Client:

    auth_client = get_auth_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = auth_client.login(login_request)

    return Client(timeout=100, base_url='http://localhost:8000', headers={'Authorization' : f'Bearer {login_response.token.access_token}'})