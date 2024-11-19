import typing


def filter_by_state(dictionaries: list[dict[str, typing.Any]], state: str = "EXECUTED") -> list[dict[str, typing.Any]]:
    """
    Функция принимает на вход список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное в функцию
    значение.
    """
    executed_list = []
    for i in dictionaries:
        if i["state"] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(dictioanaris: list[dict[str, typing.Any]], reverse: bool = True) -> list[dict[str, typing.Any]]:
    """
    Функия по сортировкам по датам
    """
    list_for_date = sorted(dictioanaris, key=lambda x: x["date"], reverse=reverse)

    return list_for_date
