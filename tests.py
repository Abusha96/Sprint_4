import pytest

""" Начало прекода """

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    """ Конец прекода """

    # метод set_book_genre (устанавливаем жанр книги)
    @pytest.mark.parametrize('name', ['Белоснежка'])
    def test_set_book_genre_if_genre_equal_fantasy_true(self, collector, name):
        collector.set_book_genre(name, 'Фантастика')

        assert collector.books_genre[name] == 'Фантастика'

    # метод get_book_genre (получаем жанр книги)
    @pytest.mark.parametrize('name', ['Дом тысячи трупов'])
    def test_get_book_genre_compare_with_correct_is_comedy_true(self, collector, name):
        assert collector.get_book_genre(name) == 'Комедия'

    # метод get_books_with_specific_genre (выводим список книг с определённым жанром)
    @pytest.mark.parametrize('expected_result', [['Крик', 'Ужасы Аммитивиля']])
    def test_get_books_with_specific_genre_horror_genre_true(self, collector, expected_result):
        assert collector.get_books_with_specific_genre('Ужасы') == expected_result

    # метод get_books_genre (получаем словарь books_genre)
    @pytest.mark.parametrize('expected_result',
                             [{'Белоснежка': 'Фантастика',
                               'Гордость и предубеждение и зомби': '',
                               'Крик': 'Ужасы',
                               'Красная шапочка': 'Фантастика',
                               'Унесённые ветром': '',
                               'Ужасы Аммитивиля': 'Ужасы',
                               'Дом тысячи трупов': 'Комедия'
                               }])
    def test_get_books_genre_nothing_dict_true(self, collector, expected_result):
        assert collector.get_books_genre() == expected_result

    # метод get_books_for_children (возвращаем книги, подходящие детям)
    @pytest.mark.parametrize('expected_result', [['Белоснежка', 'Красная шапочка']])
    def test_get_books_for_children_wait_that_returned_two_books(self, collector, expected_result):
        assert collector.get_books_for_children() == expected_result

    # метод add_book_in_favorites (добавляем книгу в Избранное)
    @pytest.mark.parametrize('name', ['Сумерки'])
    def test_add_book_in_favorites_book_in_dict_book_added_in_favorites(self, name, collector):
        collector.add_book_in_favorites(name)

        assert name in collector.favorites

    # метод delete_book_from_favorites (удаляем книгу из Избранного)
    @pytest.mark.parametrize('name', ['Сумерки', 'Блейд'])
    def test_delete_book_from_favorites_name_book_book_deleted(self, collector, name):
        collector.delete_book_from_favorites(name)

        assert name not in collector.favorites

    # метод get_list_of_favorites_books (получаем список Избранных книг)
    @pytest.mark.parametrize('expected_result', [['Сумерки', 'Блейд', 'Белоснежка']])
    def test_get_list_of_favorites_books_return_all_fav_books(self, collector, expected_result):

        assert collector.get_list_of_favorites_books() == expected_result
