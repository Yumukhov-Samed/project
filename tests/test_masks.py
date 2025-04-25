import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(numbers_16):
    assert get_mask_card_number(numbers_16) == "7000 79** **** 6361"





def test_get_mask_card_number_0(number_card):
    assert get_mask_card_number(number_card)== ' ** **** '


@pytest.mark.parametrize("value, expected", [
    ("70007922896063611234", "**1234"),
    ("70007 92289 60636 11234", "**1234"),
    (70007922896063611234, "**1234"), ])
def test_get_mask_account_correrct(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("70007922896063611234", " "),
    ("70007 92289 60636 11234", " "),
    ("70007922896063611234", " "),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) != expected



