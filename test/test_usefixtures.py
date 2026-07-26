import pytest


@pytest.fixture
def clear_books_database():
    print('[Fixture] удаляем все данные из базы данных')

@pytest.fixture
def fill_books_database():
    print('[Fixture] заполняем все данные в базу данных')


class TestLibrary:
    @pytest.mark.usefixtures('clear_books_database','fill_books_database')
    def test_read_book_from_lib(self):

        pass

    
    @pytest.mark.usefixtures('clear_books_database','fill_books_database')
    def test_delete_book_from_lib(self):

        pass

