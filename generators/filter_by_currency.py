from typing import Union


def filter_by_currency(transaction_list: Union[list, dict], currency: str) -> Union[list, dict]:
    """Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной """

    filter(lambda x: x['currency']['code'] == currency, transaction_list)

    return transaction_list

def transaction_descriptions(list_of_transactions: Union[list, dict]) -> None:
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    id_transaction = filter(lambda x: x['id'] is True, list_of_transactions)
    description_transaction = filter(lambda x: x['description'] is True, list_of_transactions)
    while True:
        print(id_transaction['id'])
        yield description_transaction['description']

transactions = [{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
},
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]
