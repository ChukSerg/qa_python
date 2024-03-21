import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def add_books(self):
        self.collector = BooksCollector()
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    def test_add_new_book_add_two_books(self):
        assert len(self.collector.books_genre) == 2

    def test_add_new_book_add_book_twice(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(self.collector.books_genre) == 2

    def test_add_new_book_book_has_not_genre(self):
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_add_genre(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_for_children_return_book_age_rating(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert self.collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_with_specific_genre_return_book_genre(self):
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert self.collector.get_books_with_specific_genre('Комедии') == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_add_one_book(self):
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.collector.add_book_in_favorites('Незнайка на луне')
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_stay_one_book(self):
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        self.collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_get_books_genre_return_two_books(self):
        assert len(self.collector.get_books_genre()) == 2
