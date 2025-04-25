import pytest
from generators import filter_by_currency
from generators.filter_by_currency import card_number_generator


def test_card_number_generator():
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(9999999999999998, 9999999999999999)

    assert next(card_number) == "9999 9999 9999 9998"
    assert next(card_number) == "9999 9999 9999 9999"

