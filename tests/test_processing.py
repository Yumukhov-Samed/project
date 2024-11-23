import pytest
from src.processing import filter_by_state, sort_by_date
from typing import Iterable, Any


def test_filter_by_state(test_dict_list_incorrect_date):
    assert filter_by_state(test_dict_list_incorrect_date) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'}]


def test_filter_by_state(test_dict_list_not_correct_date):
    assert filter_by_state(test_dict_list_not_correct_date) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': 'asfsadasda'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '********'}]

