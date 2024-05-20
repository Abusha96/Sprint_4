import pytest

from main import BooksCollector

# Добавляем фикстуру
@pytest.fixture()
def collector():
    collector = BooksCollector()
    collector.books_genre = {'Белоснежка': 'Фантастика',
                             'Гордость и предубеждение и зомби': '',
                             'Крик': 'Ужасы',
                             'Красная шапочка': 'Фантастика',
                             'Унесённые ветром': '',
                             'Ужасы Аммитивиля': 'Ужасы',
                             'Дом тысячи трупов': 'Комедия'
                             }

    collector.favorites = ['Сумерки', 'Блейд', 'Белоснежка']
    return collector