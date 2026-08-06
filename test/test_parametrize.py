
import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1,2,3])
def test_check(number : int):

    assert number>0

@pytest.mark.parametrize('number,expected', [(1,1),(2,4),(3,9),(2,5)])
def test_several(number: int, expected : int):

    assert number ** 2 == expected


@pytest.mark.parametrize('os',['macos','linux','windows','debian'])
@pytest.mark.parametrize('host',['https://dev.company.com','https://stable.company.com','https://prod.company.com'])
def test_meltiplication_of_numbers(os : str, host : str):

    assert len(os+host) > 0

@pytest.fixture(params = ['https://dev.company.com','https://stable.company.com','https://prod.company.com'])
def host(request : SubRequest) -> str:

    return request.param


def test_host(host : str):

    print(f'running test on host : {host}')

class TestOperations:

    def test_user_with_oper(self):
        print(f'user with oper')

    def test_user_without_oper(self):

        print(f'user without oper')


users = {
    '+4546465456' : 'lox', 
    '+3453455' : 'ne lox', 
    '+5675633453' : 'krasava'
}

@pytest.mark.parametrize('number', users.keys(), ids= lambda number : f'{number} : {users[number]}')
def test_identifiers(number : str):
 
    pass
