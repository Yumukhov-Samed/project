import pytest




@pytest.fixture
def numbers_16():
    return "7000792289606361"





@pytest.fixture
def numbers_zero():
    return ''


@pytest.fixture
def test_dict_list_incorrect_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'}]


@pytest.fixture
def test_dict_list_not_correct_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': 'asfsadasda'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '********'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '-----'},
            {'id': 615064591, 'state': 'CANCELED', 'date': ' '}]


