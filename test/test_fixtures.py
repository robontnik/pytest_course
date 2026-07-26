import pytest


@pytest.fixture
def user_data():
    print('создаем пользователя до теста')
    yield {'username' : 'user', 'email' : 'test@example.com'}
    print('удаляем пользователя после теста')


def test_user_email(user_data):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_username(user_data):
    print(user_data)
    assert user_data['username'] == 'user'