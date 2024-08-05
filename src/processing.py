import re
from collections import Counter
from typing import Any

from src.generators import transaction_descriptions


def get_dict_by_key_state(list_dict: list[dict[str, object]], key_state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает список тех словарей, у которых ключ state содержит переданное в функцию значение"""
    new_list_dict = []
    for dicts in list_dict:
        if dicts.get("state") == key_state:
            new_list_dict.append(dicts)
    return new_list_dict


def get_dict_date_dicrease(list_dict: Any, sorting_order: bool = True) -> list[dict[str, object]]:
    """Функция возвращает список словарей отсортированных по убыванию даты"""
    if sorting_order is True:
        new_list_dict = sorted(list_dict, key=lambda dicts: dicts["date"], reverse=sorting_order)
        return new_list_dict
    else:
        new_list_dict = sorted(list_dict, key=lambda dicts: dicts["date"])
        return new_list_dict


def filter_by_line_in_description(operations: list[dict], search_string: str) -> list[dict]:
    """Функция принимает список словарей с транзакциями и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""
    search_results_list = []
    for operation in operations:
        if re.search(search_string, operation["description"], flags=re.IGNORECASE):
            search_results_list.append(operation)

    return search_results_list


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict:
    """Функция принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой категории"""
    count_list = [x for x in transaction_descriptions(transactions) if x in categories]
    return dict(Counter(count_list))
