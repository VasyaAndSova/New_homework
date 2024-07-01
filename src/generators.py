from typing import Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict], currency_code: str) -> Iterator[dict]:
    """
    Функция, которая принимает список словарей с банковскими операциями
    и возвращает итератор, который выдает по очереди операции,
    в которых указана заданная валюта.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """
    Функция, которая принимает список словарей и возвращает итератор,
    который выдает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт, в формате XXXX XXXX XXXX XXXX
    (диапазоны передаются как параметры генератора).
    """
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        card_number = f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        yield card_number
