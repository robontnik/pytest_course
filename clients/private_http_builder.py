

from httpx import Client

from clients.auth.auth_client import LoginRequestDict, get_auth_client
from typing import TypedDict

class AuthenticationUserDict(TypedDict):

    email : str
    password : str

def get_private_http_client(user : AuthenticationUserDict) -> Client:

    auth_client = get_auth_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = auth_client.login(login_request)

    return Client(timeout=100, base_url='http://localhost:8000', headers={'Authorization' : f'Bearer {login_response['token']["accessToken"]}'})