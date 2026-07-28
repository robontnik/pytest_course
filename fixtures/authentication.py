import pytest
from clients.auth.auth_client import AuthenticationClient, get_auth_client

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_auth_client()




