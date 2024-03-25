import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, add_books):
        assert len(add_books.get_books_genre()) == 2

    def test_add_new_book_add_book_twice(self, add_books):
        add_books.add_new_book('Гордость и предубеждение и зомби')
        assert len(add_books.get_books_genre()) == 2

    def test_add_new_book_book_has_not_genre(self, add_books):
        assert add_books.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_add_genre(self, add_books):
        add_books.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert add_books.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_for_children_return_book_age_rating(self, add_books):
        add_books.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        add_books.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert add_books.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_with_specific_genre_return_book_genre(self, add_books):
        add_books.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        add_books.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert add_books.get_books_with_specific_genre('Комедии') == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_add_one_book(self, add_books):
        add_books.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_books.add_book_in_favorites('Незнайка на луне')
        assert len(add_books.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_stay_one_book(self, add_books):
        add_books.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_books.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        add_books.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(add_books.get_list_of_favorites_books()) == 1

    def test_get_books_genre_return_two_books(self, add_books):
        assert len(add_books.get_books_genre()) == 2
