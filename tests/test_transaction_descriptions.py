from generators.filter_by_currency import transaction_descriptions


def test_transaction_descriptions(transaction_list):
    num = transaction_descriptions(transaction_list)
    assert next(num) == "Перевод организации"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод с карты на карту"

_name_='_main_'