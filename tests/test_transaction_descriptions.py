from generators import transaction_descriptions
from generators import list_of_transactions
import pytest


def test_transaction_descriptions(transaction_list):
    num = transaction_descriptions(transaction_list)
    assert next(num) == "Перевод организации "
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод с карты на карту"
