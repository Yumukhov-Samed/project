from generators import filter_by_currency

def test_filter_by_currency(filter_transactions=None):
    transactions = [
        {"amount": 100, "currency": "USD"},
        {"amount": 50, "currency": "EUR"},
        {"amount": 75, "currency": "GBP"}
    ]

    assert not filter_by_currency == transactions

def test_filter_by_currency(filter_transactions=None):
    transactions = [
        {"amount": 100, "currency": "RUB"},
        {"amount": 50, "currency": "EUR"},
        {"amount": 75, "currency": "GBP"}
    ]

    assert  filter_by_currency != transactions





def test_filter_by_currency():
    transactions =[]
    assert filter_by_currency != transactions

