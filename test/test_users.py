
from curses import OK
from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.usersSchema import CreateUserRequestSchema


def test_create_user():

    public_users_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request )

    assert response.status_code == HTTPStatus.OK