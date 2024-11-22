import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Mastercard 1234567890123456", "Mastercard 1234 56** **** 3456"),
    ("Мир 2200123456789010", "Мир 2200 12** **** 9010"),
    ("Union Pay 6010203040506070", "Union Pay 6010 20** **** 6070"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("7000792289606361", "7000 79** **** 6361"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) != expected

@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum ", "номер карты не указан"),
    ("Счет ", "номер счета не указан"),
    ("", "нет данных"),
    ("1", "некорректный номер карты")
])
def test_mask_account_card_valueerror(value, expected):
    assert mask_account_card(value) != expected

@pytest.mark.parametrize("value, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-08-06", "06.08.2024")
])
def test_get_date(value, expected):
    assert get_date(value) == expected

