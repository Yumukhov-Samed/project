from typing import Union


def filter_by_currency(transactions: Union[list, dict], currency: str) -> Union[list, dict]:
    """Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной """

    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction

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


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))




def transaction_descriptions(list_of_transactions: Union[list, dict]) -> None:
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for id_transaction in list_of_transactions:
        print(id_transaction['id'])
        yield id_transaction['description']

descriptions = transaction_descriptions(transactions)
for _ in range(5):
        print(next(descriptions))

def card_number_generator(start, end):
    for i in range(start, end + 1):
        card_number = '{:0>16}'.format(str(i))
        card_number = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
        yield card_number

for card_number in card_number_generator(1, 5):
    print(card_number)


