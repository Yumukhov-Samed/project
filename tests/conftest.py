import pytest


@pytest.fixture
def numbers_16():
    return "7000792289606361"


@pytest.fixture
def number_card():
    return ''


@pytest.fixture
def dict_list_correct_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '30.06.2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '12/09/2017 21;42'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'четырнадцатое октября две тысячи восемнадцатого года'}]


@pytest.fixture
def dict_list_not_correct_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': 'asfsadasda'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '********'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '-----'},
            {'id': 615064591, 'state': 'CANCELED', 'date': ' '}]


@pytest.fixture
def dict_list():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, ]


@pytest.fixture
def test_dict_list():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def get_date_valueerror():
    return [{" ", "Некорректная дата!"},
            {" ", "Некорректная дата!"}]


@pytest.fixture
def card_numbers():
    return range(1, 9999999999999999)



@pytest.fixture
def transaction_list():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод с карты на карту"}
    ]
